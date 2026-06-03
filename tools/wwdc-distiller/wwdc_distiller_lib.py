#!/usr/bin/env python3
"""Shared standard-library helpers for the WWDC distiller."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

DISTILLER_DIR = Path(__file__).resolve().parent
CONFIG_DIR = DISTILLER_DIR / "config"
STATE_DIR = DISTILLER_DIR / "state"
STOP_CONCEPTS = {
    "app",
    "api",
    "bool",
    "button",
    "code",
    "contentview",
    "data",
    "design",
    "double",
    "field",
    "float",
    "int",
    "model",
    "scene",
    "set",
    "string",
    "swift",
    "swiftui",
    "swiftui & ui frameworks",
    "swift & ui",
    "url",
    "uikit",
    "appkit",
    "available",
    "value",
    "view",
    "void",
    "wwdc",
    "应用",
    "数据",
    "设计",
}
ALLOW_CODE_CONCEPTS = {
    "Actor",
    "AppIntent",
    "AppIntents",
    "AVFoundation",
    "CloudKit",
    "CoreData",
    "CoreML",
    "MainActor",
    "NavigationStack",
    "Observable",
    "RealityKit",
    "ScrollView",
    "Sendable",
    "SwiftData",
    "Task",
    "WidgetKit",
    "WindowGroup",
}


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records),
        encoding="utf-8",
    )


def taxonomy() -> dict[str, dict[str, Any]]:
    return read_json(CONFIG_DIR / "taxonomy.json")["domains"]


def overrides() -> dict[str, Any]:
    return read_json(CONFIG_DIR / "overrides.json", {"sessions": {}, "domainIntroductions": {}})


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def slugify(text: str) -> str:
    value = normalize(text)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value).strip("-")
    return value[:80] or "concept"


def keyword_in(text: str, keyword: str) -> bool:
    normalized_keyword = normalize(keyword)
    if re.search(r"[\u4e00-\u9fff]", normalized_keyword):
        return normalized_keyword in text
    return bool(re.search(rf"(?<![a-z0-9_]){re.escape(normalized_keyword)}(?![a-z0-9_])", text))


def plain_text(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_>#-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def short(text: str, limit: int = 280) -> str:
    text = plain_text(text)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    if not raw.startswith("---\n"):
        raise ValueError("missing frontmatter")
    _, frontmatter, body = raw.split("---", 2)
    result: dict[str, Any] = {}
    for line in frontmatter.strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("["):
            result[key.strip()] = json.loads(value)
        elif len(value) >= 2 and value[0] == value[-1] == '"':
            result[key.strip()] = value[1:-1]
        elif re.fullmatch(r"\d+", value):
            result[key.strip()] = int(value)
        else:
            result[key.strip()] = value
    return result, body.strip()


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {"正文": []}
    current = "正文"
    for line in body.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
        else:
            sections[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items() if any(line.strip() for line in lines)}


def list_items(text: str, limit: int = 8) -> list[str]:
    values: list[str] = []
    for line in text.splitlines():
        value = re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", line).strip()
        if not value or value.startswith("```") or value.startswith("#"):
            continue
        if line.lstrip().startswith(("-", "*")) or re.match(r"^\s*\d+[.)]\s+", line):
            values.append(short(value, 360))
    return values[:limit]


def bold_points(text: str, limit: int = 8) -> list[str]:
    return list(dict.fromkeys(short(match, 180) for match in re.findall(r"\*\*([^*]+)\*\*", text)))[:limit]


def identifiers(text: str, limit: int = 18) -> list[str]:
    candidates = re.findall(r"`([^`\n]{2,80})`|@([A-Z][A-Za-z0-9_]+)|\b([A-Z][A-Za-z0-9_]{2,})\b", text)
    values: list[str] = []
    for groups in candidates:
        value = next((group for group in groups if group), "")
        if value and value not in values and not value.startswith(("http", "//")):
            values.append(value)
    return values[:limit]


def classify(meta: dict[str, Any], body: str, domain_map: dict[str, dict[str, Any]], manual: dict[str, Any]) -> list[str]:
    source = f"WWDC{str(meta['year'])[-2:]}-{meta['id']}"
    if source in manual and "domains" in manual[source]:
        return manual[source]["domains"]
    primary_haystacks = [
        (normalize(str(meta.get("track", ""))), 8),
        (normalize(" ".join(meta.get("tags", []))), 7),
        (normalize(str(meta.get("title", "")) + " " + str(meta.get("titleZh", ""))), 5),
    ]
    scores: list[tuple[int, str]] = []
    for slug, domain in domain_map.items():
        score = sum(weight for haystack, weight in primary_haystacks for keyword in domain["keywords"] if keyword_in(haystack, keyword))
        if score:
            scores.append((score, slug))
    if not scores:
        body_haystack = normalize(body)
        for slug, domain in domain_map.items():
            score = sum(1 for keyword in domain["keywords"] if keyword_in(body_haystack, keyword))
            if score:
                scores.append((score, slug))
    scores.sort(key=lambda item: (-item[0], item[1]))
    if not scores:
        return ["platform-services"]
    threshold = max(3, scores[0][0] // 3)
    return [slug for score, slug in scores if score >= threshold][:3]


def article_record(path: Path, domain_map: dict[str, dict[str, Any]], manual: dict[str, Any]) -> tuple[dict[str, Any], str]:
    raw = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)
    year_match = re.fullmatch(r"wwdc(\d{4})", path.parent.name)
    if not year_match:
        raise ValueError(f"unexpected content directory: {path.parent}")
    year = int(year_match.group(1))
    meta["year"] = year
    sections = parse_sections(body)
    source = f"WWDC{str(year)[-2:]}-{meta['id']}"
    video_url = meta.get("videoUrl", "")
    if not str(video_url).startswith(f"https://developer.apple.com/videos/play/wwdc{year}/"):
        video_url = f"https://developer.apple.com/videos/play/wwdc{year}/{meta['id']}/"
    one_liner = short(sections.get("一句话判断", ""), 420)
    summary = one_liner or short(sections.get("这场 Session 讲了什么", body), 420)
    searchable = " ".join(
        [
            str(meta.get("title", "")),
            str(meta.get("titleZh", "")),
            str(meta.get("track", "")),
            " ".join(meta.get("tags", [])),
            body,
        ]
    )
    record = {
        "source": source,
        "year": year,
        "id": str(meta["id"]),
        "title": meta.get("title", ""),
        "titleZh": meta.get("titleZh", ""),
        "track": meta.get("track", ""),
        "tags": meta.get("tags", []),
        "videoUrl": video_url,
        "domains": classify(meta, body, domain_map, manual),
        "summary": summary,
        "deepPoints": bold_points(sections.get("值得深挖的点", "")),
        "bestPractices": list_items(sections.get("最佳实践", "")),
        "codeTopics": identifiers(sections.get("代码片段", "")),
        "pitfalls": list_items(sections.get("还有什么值得关注", ""), 5),
        "searchText": short(searchable, 2600),
    }
    record.update(manual.get(source, {}).get("fields", {}))
    return record, hashlib.sha256(raw.encode("utf-8")).hexdigest()


def concept_seed(session: dict[str, Any]) -> list[str]:
    values = []
    values.extend(point for point in session["deepPoints"] if 4 <= len(point) <= 48)
    values.extend(tag for tag in session["tags"] if not re.fullmatch(r"WWDC \d{4}", tag))
    values.extend(topic for topic in session["codeTopics"] if topic in ALLOW_CODE_CONCEPTS or topic.startswith("@"))
    filtered = []
    for value in values:
        normalized = normalize(value)
        if normalized in STOP_CONCEPTS or re.fullmatch(r"wwdc[- ]?\d{4}", normalized):
            continue
        if normalized not in {normalize(item) for item in filtered}:
            filtered.append(value)
    return filtered[:10]


def concept_records(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for session in sessions:
        for domain in session["domains"]:
            seeds = concept_seed(session) or [session["track"]]
            for seed in seeds[:5]:
                groups[(domain, seed)].append(session)

    concepts = []
    for (domain, seed), related in groups.items():
        related = sorted(related, key=lambda item: (-item["year"], item["source"]))
        years = defaultdict(list)
        for session in related:
            years[session["year"]].append(session["source"])
        top = related[:10]
        concepts.append(
            {
                "key": f"{domain}-{slugify(seed)}",
                "title": seed,
                "domains": [domain],
                "summary": short("；".join(session["summary"] for session in top[:3]), 520),
                "timeline": [
                    {"year": year, "sources": sources[:5]}
                    for year, sources in sorted(years.items(), key=lambda item: item[0], reverse=True)
                ],
                "decisionRules": list(dict.fromkeys(rule for session in top for rule in session["bestPractices"]))[:8],
                "pitfalls": list(dict.fromkeys(point for session in top for point in session["pitfalls"]))[:6],
                "sources": [session["source"] for session in top],
            }
        )
    concepts.sort(key=lambda concept: (-len(concept["sources"]), concept["key"]))
    return concepts


def source_sort_key(session: dict[str, Any]) -> tuple[int, str]:
    return (-session["year"], session["source"])


def domain_reference(slug: str, domain: dict[str, Any], sessions: list[dict[str, Any]], concepts: list[dict[str, Any]], introduction: str = "") -> str:
    selected = sorted((session for session in sessions if slug in session["domains"]), key=source_sort_key)
    selected_concepts = [concept for concept in concepts if slug in concept["domains"]][:14]
    years = Counter(session["year"] for session in selected)
    tags = Counter(tag for session in selected for tag in session["tags"] if not re.fullmatch(r"WWDC \d{4}", tag))
    practices = Counter(rule for session in selected for rule in session["bestPractices"])
    pitfalls = Counter(point for session in selected for point in session["pitfalls"] + session["deepPoints"])
    key_sessions = selected[:18]

    lines = [
        f"# {domain['label']}",
        "",
        "## 领域判断",
        "",
        introduction or f"{domain['description']}。本领域覆盖 {len(selected)} 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。",
        "",
        "## 核心模型",
        "",
    ]
    if selected_concepts:
        for concept in selected_concepts[:7]:
            sources = "、".join(f"[{source}]" for source in concept["sources"][:4])
            lines.append(f"- **{concept['title']}**：{concept['summary']} 来源：{sources}")
    else:
        lines.append("- 暂无足够跨 Session 聚合的概念卡；使用本地索引检索具体 Session。")

    lines.extend(["", "## API 演进时间线", ""])
    for year in sorted(years, reverse=True):
        examples = [session for session in selected if session["year"] == year][:5]
        lines.append(f"- **WWDC{str(year)[-2:]}**：{years[year]} 场，代表来源：" + "、".join(f"[{session['source']}]" for session in examples))

    lines.extend(["", "## 决策启发式", ""])
    for rule, _ in practices.most_common(10):
        lines.append(f"- {rule}")
    if not practices:
        lines.append("- 先用本地索引定位具体 Session，再根据来源回答。")

    lines.extend(["", "## 反模式与坑", ""])
    for point, _ in pitfalls.most_common(8):
        lines.append(f"- {point}")
    if not pitfalls:
        lines.append("- 不要把 WWDC Session 中的设计建议当成当前 SDK 的完整 API 文档。")

    lines.extend(["", "## 高频主题", ""])
    lines.append("、".join(f"`{tag}` ({count})" for tag, count in tags.most_common(18)) if tags else "暂无稳定标签。")

    lines.extend(["", "## 关键 Session", ""])
    for session in key_sessions:
        title = session["titleZh"] or session["title"]
        lines.append(f"- [{session['source']}] {title}：{session['summary']}")
    lines.append("")
    return "\n".join(lines)


def overview_reference(domain_map: dict[str, dict[str, Any]], sessions: list[dict[str, Any]]) -> str:
    years = Counter(session["year"] for session in sessions)
    lines = [
        "# WWDC Notes Overview",
        "",
        "此文件用于跨领域综述、年度主题和路由兜底。具体问题优先读取对应领域文件。",
        "",
        "## 覆盖范围",
        "",
        f"- Session 总数：{len(sessions)}",
        f"- 年份范围：{min(years) if years else '-'}-{max(years) if years else '-'}",
        "",
        "## 年份",
        "",
    ]
    lines.extend(f"- WWDC{str(year)[-2:]}：{years[year]} 场" for year in sorted(years, reverse=True))
    lines.extend(["", "## 领域", ""])
    for slug, domain in domain_map.items():
        count = sum(slug in session["domains"] for session in sessions)
        lines.append(f"- [{domain['label']}]({slug}.md)：{count} 场。{domain['description']}")
    lines.append("")
    return "\n".join(lines)
