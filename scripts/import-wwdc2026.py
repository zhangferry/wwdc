#!/usr/bin/env python3
"""Import the currently published WWDC 2026 session metadata from Apple."""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "src/content/wwdc2026"
IMAGE_DIR = ROOT / "public/images/sessions/2026"
USER_AGENT = "Mozilla/5.0 WWDC-Notes-Importer/1.0"

TRACK_RULES = [
    ("Essentials", ["keynote", "platforms state of the union", "get ready for wwdc"]),
    ("Accessibility & Inclusion", ["accessibility", "dynamic type"]),
    ("App Store & Distribution", ["app store", "storekit", "purchase", "subscription", "testflight"]),
    ("SwiftUI & UI Frameworks", ["swiftui", "uikit", "appkit", "textkit", "pencilkit", "paperkit"]),
    ("Swift & Data", ["swift ", "swiftdata", "swift testing", "grpc"]),
    ("AI & Machine Learning", ["foundation model", "agentic", "core ai", "mlx", "machine learning", "llm", "image understanding", "evaluations framework", "siri"]),
    ("visionOS & Spatial Computing", ["visionos", "realitykit", "reality composer", "spatial", "openusd", "usdkit", "immersive"]),
    ("Xcode & Developer Tools", ["xcode", "instruments", "device hub", "metric kit", "metrickit"]),
    ("Web & Safari", ["safari", "webkit", "html ", "css "]),
    ("Graphics, Games & Media", ["metal", "game", "camera", "photo", "image", "music", "subtitle", "now playing"]),
    ("Privacy & Security", ["secure", "security", "privacy", "trust", "app attest"]),
    ("System Services", ["app intent", "shortcut", "widget", "live activit", "wallet", "healthkit", "carplay", "bluetooth", "virtualization", "container"]),
    ("Design", ["design", "brand", "prototype"]),
]

DOMAIN_RULES = {
    "swiftui": ["swiftui", "widgetkit"],
    "swift-concurrency": ["concurr", "actor", "sendable", "swift 6"],
    "uikit-appkit": ["uikit", "appkit", "textkit", "pencilkit", "paperkit"],
    "xcode-tools": ["xcode", "instruments", "device hub", "metric kit", "metrickit", "testing"],
    "spatial-computing": ["visionos", "realitykit", "reality composer", "spatial", "openusd", "usdkit", "immersive"],
    "machine-learning": ["foundation model", "agentic", "core ai", "mlx", "machine learning", "llm", "siri", "image understanding", "evaluations"],
    "networking-storage": ["swiftdata", "grpc", "cloud", "storage", "document"],
    "graphics-media": ["metal", "game", "camera", "photo", "image", "music", "subtitle", "webkit"],
    "platform-services": ["app intent", "shortcut", "widget", "live activit", "wallet", "healthkit", "carplay", "bluetooth", "now playing"],
    "app-distribution": ["app store", "storekit", "purchase", "subscription", "testflight", "xcode cloud"],
    "privacy-security": ["secure", "security", "privacy", "trust", "app attest"],
    "design-accessibility": ["design", "accessibility", "dynamic type", "brand", "prototype"],
}


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def first(pattern: str, source: str, default: str = "") -> str:
    match = re.search(pattern, source, re.S)
    return strip_tags(match.group(1)) if match else default


def classify_track(text: str) -> str:
    normalized = text.lower()
    for track, keywords in TRACK_RULES:
        if any(keyword in normalized for keyword in keywords):
            return track
    return "Other"


def classify_domains(text: str) -> list[str]:
    normalized = text.lower()
    domains = [
        domain
        for domain, keywords in DOMAIN_RULES.items()
        if any(keyword in normalized for keyword in keywords)
    ]
    return domains or ["platform-services"]


def tags_for(title: str, description: str, track: str) -> list[str]:
    text = f"{title} {description}"
    candidates = re.findall(
        r"\b(?:SwiftUI|SwiftData|Swift|UIKit|AppKit|Xcode|Instruments|visionOS|RealityKit|"
        r"Metal|MLX|Core AI|Foundation Models|App Intents|Siri|Safari|WebKit|StoreKit|"
        r"HealthKit|Wallet|CarPlay|WidgetKit|PencilKit|TextKit|PaperKit|MusicKit|Core Image)\b",
        text,
        re.I,
    )
    canonical = {}
    for tag in candidates:
        canonical[tag.lower()] = tag
    result = list(canonical.values())[:5]
    if not result:
        result.append(track)
    return result


def parse_session(session_id: str) -> dict:
    english_url = f"https://developer.apple.com/videos/play/wwdc2026/{session_id}/"
    chinese_url = f"https://developer.apple.com/cn/videos/play/wwdc2026/{session_id}/"
    english = fetch(english_url)
    chinese = fetch(chinese_url)

    title = first(r"<title>(.*?)\s+-\s+WWDC26\s+-\s+Videos", english)
    title_zh = first(
        r'<li class="supplement details[^"]*"[^>]*>.*?<h1>(.*?)</h1>',
        chinese,
        title,
    )
    description_zh = first(
        r'<li class="supplement details[^"]*"[^>]*>.*?<h1>.*?</h1>\s*</div>\s*<p>(.*?)</p>',
        chinese,
    )
    description_en = first(
        r'<li class="supplement details[^"]*"[^>]*>.*?<h1>.*?</h1>\s*</div>\s*<p>(.*?)</p>',
        english,
    )
    image_url = first(r'<meta property="og:image" content="([^"]+)"', english)
    date = first(r'<meta itemprop="datePublished" content="([^"]+)"', english, "2026-06-08")

    chapter_items = re.findall(
        r'<li class="chapter-item"[^>]*data-start-time="(\d+)"[^>]*>.*?'
        r'data-chapter-end-time="(\d+)".*?>([^<]+)</a></li>',
        english,
        re.S,
    )
    chapter_summaries = [
        strip_tags(item)
        for item in re.findall(r'<li class="chapter-summary"><p>(.*?)</p></li>', english, re.S)
    ]
    chapters = []
    for index, (start, end, chapter_title) in enumerate(chapter_items):
        chapters.append(
            {
                "start": int(start),
                "end": int(end),
                "title": strip_tags(chapter_title),
                "summary": chapter_summaries[index] if index < len(chapter_summaries) else "",
            }
        )

    code_topics = [
        strip_tags(item)
        for item in re.findall(
            r'<a class="jump-to-time-sample"[^>]*>(.*?)</a>',
            english,
            re.S,
        )
    ]
    duration = max((chapter["end"] for chapter in chapters), default=0)
    combined = " ".join([title, title_zh, description_en, description_zh, *code_topics])
    track = classify_track(combined)

    return {
        "id": session_id,
        "title": title,
        "titleZh": title_zh,
        "descriptionZh": description_zh,
        "descriptionEn": description_en,
        "track": track,
        "domains": classify_domains(combined),
        "tags": tags_for(title, description_en, track),
        "duration": duration,
        "date": date,
        "thumbnailSource": image_url,
        "videoUrl": english_url,
        "chapters": chapters,
        "codeTopics": code_topics,
    }


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_article(session: dict) -> str:
    tags = ", ".join(yaml_string(tag) for tag in session["tags"])
    chapter_lines = []
    for chapter in session["chapters"]:
        minutes, seconds = divmod(chapter["start"], 60)
        line = f"- **{minutes}:{seconds:02d} · {chapter['title']}**"
        if chapter["summary"]:
            line += f"：{chapter['summary']}"
        chapter_lines.append(line)
    if not chapter_lines:
        chapter_lines.append("- Apple 暂未提供章节划分，后续会随官方资料补充。")

    code_lines = [f"- `{topic}`" for topic in session["codeTopics"][:12]]
    if not code_lines:
        code_lines.append("- 当前页面没有独立的示例代码片段。")

    description = session["descriptionZh"] or session["descriptionEn"]
    return f"""---
id: {yaml_string(session["id"])}
title: {yaml_string(session["title"])}
titleZh: {yaml_string(session["titleZh"])}
track: {yaml_string(session["track"])}
level: "intermediate"
duration: {session["duration"]}
date: {yaml_string(session["date"])}
thumbnail: {yaml_string(f"/images/sessions/2026/{session['id']}.jpg")}
videoUrl: {yaml_string(session["videoUrl"])}
tags: [{tags}]
---

## 一句话判断

我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：{description}

## 这场 Session 讲了什么

{description}

这篇内容依据 Apple 在 {session["date"]} 发布的官方页面整理。当前页面已提供视频、简介、章节摘要和部分示例代码，但完整 transcript 尚未上线，因此本版以准确收录和快速检索为目标，不对尚未公开的实现细节做推断。

## 官方章节速览

{chr(10).join(chapter_lines)}

> 章节摘要暂沿用 Apple 当前发布的英文原文；完整逐字稿上线后会升级为中文深度总结。

## 代码与 API 线索

Apple 官方页面当前列出的代码主题包括：

{chr(10).join(code_lines)}

建议直接打开 [Apple Developer 视频页面]({session["videoUrl"]}) 查看完整示例代码和最新资源链接。

## 最佳实践

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。

## 资料状态

- 发布日期：{session["date"]}
- 视频：已发布
- 官方章节摘要：{"已发布" if session["chapters"] else "暂未发布"}
- 示例代码索引：{"已发布" if session["codeTopics"] else "暂未发布"}
- 完整 transcript：暂未发布
"""


def download_image(url: str, target: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            target.write_bytes(response.read())
    except Exception:
        fallback = url.replace("_wide_1280x720_2x", "_wide_250x141_2x")
        with urllib.request.urlopen(
            urllib.request.Request(fallback, headers={"User-Agent": USER_AGENT}),
            timeout=30,
        ) as response:
            target.write_bytes(response.read())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Regenerate articles from the saved metadata without fetching Apple pages.",
    )
    args = parser.parse_args()
    metadata_path = ROOT / "scripts/wwdc2026-metadata.json"
    if args.render_only:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        CONTENT_DIR.mkdir(parents=True, exist_ok=True)
        for session in metadata:
            (CONTENT_DIR / f"{session['id']}.md").write_text(
                render_article(session),
                encoding="utf-8",
            )
        print(f"Rendered {len(metadata)} sessions from saved metadata")
        return

    listing = fetch("https://developer.apple.com/videos/all-videos/")
    ids = sorted(set(re.findall(r"wwdc2026/(\d+)", listing)), key=int)
    if not ids:
        raise SystemExit("No WWDC 2026 sessions found")

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    metadata = []
    for index, session_id in enumerate(ids, start=1):
        print(f"[{index:03d}/{len(ids):03d}] {session_id}", flush=True)
        session = parse_session(session_id)
        metadata.append(session)
        (CONTENT_DIR / f"{session_id}.md").write_text(render_article(session), encoding="utf-8")
        image_target = IMAGE_DIR / f"{session_id}.jpg"
        if session["thumbnailSource"]:
            download_image(session["thumbnailSource"], image_target)

    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Imported {len(metadata)} sessions")


if __name__ == "__main__":
    main()
