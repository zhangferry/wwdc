#!/usr/bin/env python3
"""Search the standalone WWDC knowledge index."""

from __future__ import annotations

import argparse
import json
import sys

sys.dont_write_bytecode = True

from wwdc_runtime import DATA_DIR, read_json, search_records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    routed, sessions, concepts = search_records(args.query, args.limit)
    if args.json:
        print(json.dumps({"domains": routed, "concepts": concepts, "sessions": sessions}, ensure_ascii=False, indent=2))
        return 0
    domain_map = read_json(DATA_DIR / "domains.json")
    print("领域:", "、".join(domain_map[slug]["label"] for slug in routed) or "未明确路由")
    if concepts:
        print("\n概念:")
        for concept in concepts[:3]:
            print(f"- {concept['title']}：{concept['summary']} 来源：" + "、".join(f"[{source}]" for source in concept["sources"][:4]))
    print("\nSession:")
    for session in sessions:
        print(f"\n[{session['source']}] {session['titleZh'] or session['title']} (score={session['score']})")
        print(session["summary"])
        print(session["videoUrl"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
