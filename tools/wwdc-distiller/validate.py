#!/usr/bin/env python3
"""Validate a generated runtime WWDC Notes skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from wwdc_distiller_lib import read_json, read_jsonl, taxonomy


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", default="skills/wwdc-notes", help="Runtime skill directory")
    args = parser.parse_args()
    skill = Path(args.skill).resolve()
    data_dir = skill / "data"
    references_dir = skill / "references"
    errors = []
    domain_map = taxonomy()
    sessions = read_jsonl(data_dir / "sessions.jsonl")
    concepts = read_jsonl(data_dir / "concepts.jsonl")
    manifest = read_json(data_dir / "manifest.json", {})
    domains_runtime = read_json(data_dir / "domains.json", {})
    sources = [session.get("source", "") for session in sessions]

    if not (skill / "SKILL.md").exists():
        errors.append("missing SKILL.md")
    if not sessions:
        errors.append("sessions.jsonl is empty")
    if not concepts:
        errors.append("concepts.jsonl is empty")
    if len(sources) != len(set(sources)):
        errors.append("sessions.jsonl contains duplicate source IDs")
    if manifest.get("coverage", {}).get("sessions") != len(sessions):
        errors.append("manifest session count is stale")
    if set(domains_runtime) != set(domain_map):
        errors.append("runtime domains.json differs from distiller taxonomy")
    forbidden_manifest = {"sourceRepository", "sourceCommit", "lastUpdate"}
    leaked = sorted(forbidden_manifest & set(manifest))
    if leaked:
        errors.append(f"manifest exposes distiller-only keys: {leaked}")
    for source in sources:
        if not re.fullmatch(r"WWDC\d{2}-.+", source):
            errors.append(f"invalid source ID: {source}")
    for session in sessions:
        unknown = sorted(set(session.get("domains", [])) - set(domain_map))
        if unknown:
            errors.append(f"{session['source']} has unknown domains: {unknown}")
        if "contentHash" in session:
            errors.append(f"{session['source']} exposes contentHash")
        expected_url_prefix = f"https://developer.apple.com/videos/play/wwdc{session['year']}/"
        if not str(session.get("videoUrl", "")).startswith(expected_url_prefix):
            errors.append(f"{session['source']} has invalid videoUrl: {session.get('videoUrl')}")
        if not session.get("summary"):
            errors.append(f"{session['source']} has no summary")
    for concept in concepts:
        if not concept.get("sources"):
            errors.append(f"{concept.get('key', '<unknown>')} has no sources")
    for slug in domain_map:
        path = references_dir / f"{slug}.md"
        if not path.exists():
            errors.append(f"missing reference: {path.name}")
    if not (references_dir / "overview.md").exists():
        errors.append("missing reference: overview.md")
    for path in [skill / "SKILL.md", references_dir / "overview.md"]:
        if path.exists() and any(term in path.read_text(encoding="utf-8") for term in ["维护", "原始仓库", "sourceRepository", "update.py", "distill.py"]):
            errors.append(f"{path.relative_to(skill)} leaks maintenance wording")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(sessions)} sessions, {len(concepts)} concepts, {len(domain_map)} domains.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
