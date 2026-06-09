#!/usr/bin/env python3
"""Enhanced WWDC26 importer: downloads subtitles, extracts code, uses LLM to generate
deep summaries matching the WWDC25 article format."""

from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import os
import re
import sys
import time
import traceback
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "src/content/wwdc2026"
METADATA_PATH = ROOT / "scripts/wwdc2026-metadata.json"
USER_AGENT = "Mozilla/5.0 WWDC-Notes-Importer/2.0"

# ── Network helpers ──────────────────────────────────────────────────────────

def fetch(url: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(1 * (attempt + 1))

def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


# ── Subtitle extraction ─────────────────────────────────────────────────────

def extract_m3u8_url(page_html: str, session_id: str) -> str | None:
    """Find the HLS m3u8 URL from the video page."""
    pattern = rf'https://devstreaming-cdn\.apple\.com/videos/wwdc/2026/{session_id}/[^"\']+cmaf\.m3u8'
    m = re.search(pattern, page_html)
    return m.group(0) if m else None


def download_subtitles(m3u8_url: str) -> str | None:
    """Download English subtitles from the HLS stream. Returns full transcript text."""
    try:
        m3u8_content = fetch(m3u8_url)
        # Find English subtitle playlist
        sub_match = re.search(
            r'LANGUAGE="en"[^>]*URI="([^"]+)"', m3u8_content
        )
        if not sub_match:
            return None
        sub_playlist_url = sub_match.group(1)
        if not sub_playlist_url.startswith("http"):
            base = m3u8_url.rsplit("/", 1)[0] + "/"
            sub_playlist_url = base + sub_playlist_url

        sub_playlist = fetch(sub_playlist_url)
        segments = re.findall(r'(sequence_\d+\.webvtt)', sub_playlist)
        if not segments:
            return None

        base_url = sub_playlist_url.rsplit("/", 1)[0] + "/"
        transcript_lines: list[str] = []
        prev_line = ""
        for seg in segments:
            try:
                content = fetch(base_url + seg)
                for line in content.splitlines():
                    line = line.strip()
                    if not line or line.startswith("WEBVTT") or line.startswith("NOTE"):
                        continue
                    if "-->" in line or line.isdigit():
                        continue
                    clean = re.sub(r"<[^>]+>", "", line)
                    clean = clean.strip()
                    if clean and clean != prev_line:
                        transcript_lines.append(clean)
                        prev_line = clean
            except Exception:
                continue

        # Deduplicate adjacent repeated lines (common in subtitle streams)
        deduped: list[str] = []
        for line in transcript_lines:
            if not deduped or line != deduped[-1]:
                deduped.append(line)

        return "\n".join(deduped) if deduped else None
    except Exception:
        return None


# ── Page data extraction ─────────────────────────────────────────────────────

def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def extract_code_blocks(page_html: str) -> list[dict]:
    """Extract sample code blocks with titles and actual code."""
    blocks = re.findall(
        r'<p>(\d+:\d+)\s*-\s*<a class="jump-to-time-sample"[^>]*>(.*?)</a></p>\s*'
        r'<pre class="code-source"><code>(.*?)</code></pre>',
        page_html, re.S,
    )
    results = []
    for time_str, title_html, code_html in blocks:
        code = re.sub(r"<[^>]+>", "", code_html)
        code = html.unescape(code).strip()
        title = html.unescape(re.sub(r"<[^>]+>", "", title_html)).strip()
        results.append({"time": time_str, "title": title, "code": code})
    return results


def extract_chapters(page_html: str) -> list[dict]:
    """Extract chapter list with titles, times, and summaries."""
    chapter_items = re.findall(
        r'<li class="chapter-item"[^>]*data-start-time="(\d+)"[^>]*>'
        r'.*?data-chapter-end-time="(\d+)".*?>([^<]+)</a></li>',
        page_html, re.S,
    )
    chapter_summaries = [
        strip_tags(item)
        for item in re.findall(r'<li class="chapter-summary"><p>(.*?)</p></li>', page_html, re.S)
    ]
    chapters = []
    for idx, (start, end, title) in enumerate(chapter_items):
        chapters.append({
            "start": int(start),
            "end": int(end),
            "title": strip_tags(title),
            "summary": chapter_summaries[idx] if idx < len(chapter_summaries) else "",
        })
    return chapters


# ── LLM-based article generation ────────────────────────────────────────────

def build_system_prompt() -> str:
    return """你是一个资深 iOS/macOS 开发者，正在为 WWDC 技术博客写文章。你的写作风格：

1. 先给判断，再讲理由。第一段必须回答"这场 Session 最值得关注的一件事是什么"。
2. 说人话。像在 Slack 里给同事讲这个 Session。
3. 有立场。觉得好就说好，觉得鸡肋就说鸡肋。
4. 一个核心洞察 > 五个浅层要点。
5. 具体 > 抽象。给出 API 名、场景、数字。
6. 中文为主，术语保留英文。首次出现时括号标注。
7. 代码注释用中文。
8. 避免的词：值得注意的是、进一步、核心在于、本质上、综上所述、首先...其次...最后。
9. 避免五段式、编号列表超过3项、"总结"段落。"""


def build_user_prompt(session: dict, transcript: str | None, code_blocks: list[dict]) -> str:
    parts = []
    parts.append(f"# 任务\n为 WWDC26 Session {session['id']} 写一篇深度技术博客文章。\n")

    parts.append(f"## 基本信息\n- 标题: {session['title']}\n- 中文标题: {session['titleZh']}")
    parts.append(f"- Track: {session['track']}\n- 时长: {session['duration']}秒")
    parts.append(f"- 官方简介: {session['descriptionZh'] or session['descriptionEn']}\n")

    if session.get("chapters"):
        parts.append("## 章节列表")
        for ch in session["chapters"]:
            m, s = divmod(ch["start"], 60)
            summary = f"：{ch['summary']}" if ch.get("summary") else ""
            parts.append(f"- {m}:{s:02d} - {ch['title']}{summary}")
        parts.append("")

    if transcript:
        # Limit transcript to ~8000 chars to stay within context limits
        truncated = transcript[:8000]
        if len(transcript) > 8000:
            truncated += f"\n\n...(truncated, total {len(transcript)} chars)"
        parts.append(f"## 完整字幕（英文）\n{truncated}\n")

    if code_blocks:
        parts.append("## Apple 官方示例代码")
        for block in code_blocks[:8]:
            parts.append(f"### {block['time']} - {block['title']}\n```{guess_lang(block['code'])}\n{block['code'][:600]}\n```\n")

    parts.append("""## 输出格式要求

严格按照以下 Markdown 结构输出，不要加任何前缀说明：

```
---
id: "SESSION_ID"
title: "ENGLISH_TITLE"
titleZh: "中文标题"
track: "TRACK_NAME"
level: "beginner|intermediate|advanced"
duration: SECONDS
date: "YYYY-MM-DD"
thumbnail: "/images/sessions/2026/SESSION_ID.jpg"
videoUrl: "https://developer.apple.com/videos/play/wwdc2026/SESSION_ID/"
tags: ["Tag1", "Tag2"]
---

## 一句话判断

一个具体的判断，不是概括。例：✅ "SwiftUI 终于能做真正的文本编辑器了" ❌ "SwiftUI 带来了很多新特性"

## 这场 Session 讲了什么

2-3 段话，像给同事口述：从哪里来（背景/痛点）→ 现在变成什么（具体 API 变化）→ 对谁影响最大。不要用"首先...其次...最后"。

## 值得深挖的点

挑 1-2 个最值得深入分析的技术点，每个 300-500 字。分析：
- 为什么 Apple 要做这个？
- 设计选择背后的 trade-off？
- 和旧方案/竞品相比，好在哪，可能的坑在哪？

### 子标题1

内容...

### 子标题2

内容...

## 代码片段

2-3 个最实用的代码示例。每个：
- 一句话说明场景
- 代码本身（简洁，可运行）
- 一句话说最容易踩的坑

### 1. 示例标题

场景：...

\```swift
// 代码
\```

坑：...

### 2. 示例标题

...

## 最佳实践

以迁移/采用建议为主，口吻专业：
- 已有项目的迁移策略
- 新项目的采用建议
- 实战中容易踩的坑

## 还有什么值得关注

2-3 个次要但有趣的变化，每个一句话带过。

- **要点1**：描述
- **要点2**：描述
- **要点3**：描述
```

注意事项：
- 如果字幕内容不足以支撑"值得深挖的点"，基于章节摘要和代码示例合理分析，但不要编造 Apple 未声明的细节
- 代码片段优先使用 Apple 官方示例代码，可以简化和加中文注释
- tags 从内容中提取 3-5 个关键技术名词
- level 根据内容深度判断：入门概念=beginner，日常开发=intermediate，底层/高级=advanced
""")
    return "\n".join(parts)


def guess_lang(code: str) -> str:
    if "import SwiftUI" in code or "struct " in code and ": View" in code:
        return "swift"
    if "import Metal" in code or "MTL" in code:
        return "swift"
    if code.strip().startswith("{") or '"format"' in code:
        return "json"
    if "func " in code or "let " in code or "var " in code:
        return "swift"
    if "import PackageDescription" in code:
        return "swift"
    return ""


def generate_article_with_llm(session: dict, transcript: str | None, code_blocks: list[dict]) -> str:
    """Call Anthropic API to generate the article."""
    import anthropic

    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        base_url=os.environ.get("ANTHROPIC_BASE_URL"),
    )

    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250514")
    system = build_system_prompt()
    user_prompt = build_user_prompt(session, transcript, code_blocks)

    resp = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    )

    text = resp.content[0].text.strip()
    # The LLM may wrap in code fences — strip them
    if text.startswith("```"):
        text = re.sub(r"^```(?:markdown|md)?\s*\n?", "", text)
        text = re.sub(r"\n?```\s*$", "", text)
    return text


# ── Fallback for sessions without video ──────────────────────────────────────

def generate_stub_article(session: dict) -> str:
    """Generate a minimal article for sessions without video/subtitles."""
    tags = ", ".join(f'"{t}"' for t in session.get("tags", []))
    desc = session.get("descriptionZh") or session.get("descriptionEn") or ""
    return f"""---
id: "{session['id']}"
title: "{session['title']}"
titleZh: "{session['titleZh']}"
track: "{session['track']}"
level: "intermediate"
duration: {session.get('duration', 0)}
date: "{session['date']}"
thumbnail: "/images/sessions/2026/{session['id']}.jpg"
videoUrl: "{session['videoUrl']}"
tags: [{tags}]
---

## 一句话判断

这场 Session 的完整视频和字幕尚未发布，当前依据 Apple 官方页面信息整理速览。

## 这场 Session 讲了什么

{desc}

Apple 官方页面提供了简介和章节信息，但完整视频内容尚未上线。待字幕发布后会升级为深度分析文章。

## 最佳实践

- 先用本页确认 Session 是否与你的项目相关。
- 关注 [Apple Developer 视频页面]({session['videoUrl']}) 获取最新内容。

## 资料状态

- 发布日期：{session['date']}
- 完整视频/字幕：暂未发布
"""


# ── Main pipeline ────────────────────────────────────────────────────────────

def process_session(session: dict, force: bool = False) -> dict:
    """Process a single session. Returns status dict."""
    sid = session["id"]
    target = CONTENT_DIR / f"{sid}.md"

    if not force and target.exists():
        content = target.read_text(encoding="utf-8")
        # Skip if already has deep content (more than just stub)
        if "## 值得深挖的点" in content and len(content) > 2000:
            return {"id": sid, "status": "skipped", "reason": "already has deep content"}

    url = session["videoUrl"]
    result = {"id": sid, "status": "unknown"}

    try:
        # 1. Fetch the Apple video page
        page_html = fetch(url)

        # 2. Try to get subtitles
        m3u8_url = extract_m3u8_url(page_html, sid)
        transcript = None
        if m3u8_url:
            transcript = download_subtitles(m3u8_url)

        # 3. Extract code blocks and chapters from page
        code_blocks = extract_code_blocks(page_html)
        chapters = extract_chapters(page_html)
        # Update session with latest chapter data
        if chapters:
            session["chapters"] = chapters

        # 4. Generate article
        if transcript or code_blocks:
            article = generate_article_with_llm(session, transcript, code_blocks)
            target.write_text(article, encoding="utf-8")
            result["status"] = "generated"
            result["has_transcript"] = transcript is not None
            result["code_blocks"] = len(code_blocks)
            result["chars"] = len(article)
        else:
            # No video content at all — write stub
            article = generate_stub_article(session)
            target.write_text(article, encoding="utf-8")
            result["status"] = "stub"

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        traceback.print_exc()

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Enhanced WWDC26 importer with LLM summaries")
    parser.add_argument("--sessions", nargs="*", help="Specific session IDs to process (default: all)")
    parser.add_argument("--force", action="store_true", help="Reprocess even if deep content exists")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent workers (default: 4)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed")
    args = parser.parse_args()

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    if args.sessions:
        sessions = [s for s in metadata if s["id"] in args.sessions]
    else:
        sessions = metadata

    print(f"Processing {len(sessions)} sessions with {args.workers} workers")
    if args.dry_run:
        for s in sessions:
            print(f"  Would process: {s['id']} - {s['title']}")
        return

    results = []
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_session, s, args.force): s for s in sessions}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            results.append(result)
            elapsed = time.time() - start_time
            status_icon = {"generated": "✅", "stub": "📝", "skipped": "⏭️", "error": "❌"}.get(result["status"], "?")
            extra = ""
            if result.get("has_transcript"):
                extra += " [transcript]"
            if result.get("code_blocks"):
                extra += f" [{result['code_blocks']} code blocks]"
            if result.get("error"):
                extra += f" ({result['error'][:60]})"
            print(f"[{i:03d}/{len(sessions)}] {status_icon} {result['id']}{extra} ({elapsed:.0f}s elapsed)", flush=True)

    # Summary
    generated = sum(1 for r in results if r["status"] == "generated")
    stubs = sum(1 for r in results if r["status"] == "stub")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    errors = sum(1 for r in results if r["status"] == "error")
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Done in {elapsed:.0f}s")
    print(f"  Generated: {generated}")
    print(f"  Stubs:     {stubs}")
    print(f"  Skipped:   {skipped}")
    print(f"  Errors:    {errors}")

    if errors:
        error_list = [r for r in results if r["status"] == "error"]
        print(f"\nFailed sessions:")
        for r in error_list:
            print(f"  {r['id']}: {r.get('error', 'unknown')}")

    # Save results log
    log_path = ROOT / "scripts/import-results.json"
    log_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nResults saved to {log_path}")


if __name__ == "__main__":
    main()
