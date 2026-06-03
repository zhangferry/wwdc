#!/usr/bin/env python3
"""Build or incrementally refresh the runtime WWDC skill package."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True

from wwdc_distiller_lib import (
    STATE_DIR,
    article_record,
    concept_records,
    domain_reference,
    overview_reference,
    overrides,
    read_json,
    taxonomy,
    write_json,
    write_jsonl,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to the wwdc-notes repository")
    parser.add_argument("--out", default="skills/wwdc-notes", help="Runtime skill output directory")
    parser.add_argument("--full", action="store_true", help="Rewrite every domain reference")
    parser.add_argument("--json", action="store_true", help="Print the change report as JSON")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    out = Path(args.out).expanduser()
    if not out.is_absolute():
        out = (source / out).resolve()
    content_dir = source / "src" / "content"
    if not content_dir.is_dir():
        parser.error(f"missing content directory: {content_dir}")

    domain_map = taxonomy()
    override_map = overrides()
    manual_sessions = override_map.get("sessions", {})
    previous_hashes = read_json(STATE_DIR / "source-hashes.json", {})
    sessions = []
    hashes = {}
    errors = []
    for path in sorted(content_dir.glob("wwdc*/*.md")):
        try:
            record, content_hash = article_record(path, domain_map, manual_sessions)
            sessions.append(record)
            hashes[record["source"]] = content_hash
        except Exception as error:
            errors.append({"path": str(path), "error": str(error)})
    if errors:
        print(json.dumps({"errors": errors}, ensure_ascii=False, indent=2))
        return 1

    sessions.sort(key=lambda session: (-session["year"], session["source"]))
    current_sources = set(hashes)
    previous_sources = set(previous_hashes)
    added = sorted(current_sources - previous_sources)
    removed = sorted(previous_sources - current_sources)
    changed = sorted(source_id for source_id in current_sources & previous_sources if hashes[source_id] != previous_hashes[source_id])
    unchanged = sorted(current_sources & previous_sources - set(changed))
    session_by_source = {session["source"]: session for session in sessions}
    previous_domains = read_json(STATE_DIR / "source-domains.json", {})
    affected = set()
    for source_id in added + changed:
        affected.update(session_by_source[source_id]["domains"])
    for source_id in removed + changed:
        affected.update(previous_domains.get(source_id, []))
    if args.full or not previous_hashes:
        affected = set(domain_map)

    report = {"added": added, "changed": changed, "removed": removed, "unchanged": len(unchanged), "affectedDomains": sorted(affected)}
    if previous_hashes and not args.full and not (added or changed or removed):
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else f"No source changes; {len(unchanged)} sessions unchanged.")
        return 0

    data_dir = out / "data"
    references_dir = out / "references"
    concepts = concept_records(sessions)
    write_jsonl(data_dir / "sessions.jsonl", sessions)
    write_jsonl(data_dir / "concepts.jsonl", concepts)
    write_json(data_dir / "domains.json", domain_map)
    years = [session["year"] for session in sessions]
    write_json(
        data_dir / "manifest.json",
        {
            "knowledgeVersion": datetime.now(timezone.utc).strftime("%Y.%m.%d"),
            "coverage": {"from": min(years), "to": max(years), "sessions": len(sessions)},
            "domains": {slug: sum(slug in session["domains"] for session in sessions) for slug in domain_map},
        },
    )

    references_dir.mkdir(parents=True, exist_ok=True)
    introductions = override_map.get("domainIntroductions", {})
    for slug in sorted(affected):
        (references_dir / f"{slug}.md").write_text(
            domain_reference(slug, domain_map[slug], sessions, concepts, introductions.get(slug, "")),
            encoding="utf-8",
        )
    (references_dir / "overview.md").write_text(overview_reference(domain_map, sessions), encoding="utf-8")

    write_json(STATE_DIR / "source-hashes.json", hashes)
    write_json(STATE_DIR / "source-domains.json", {session["source"]: session["domains"] for session in sessions})
    write_json(STATE_DIR / "last-report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else f"Distilled {len(sessions)} sessions; rewrote {len(affected)} domains; added={len(added)} changed={len(changed)} removed={len(removed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
