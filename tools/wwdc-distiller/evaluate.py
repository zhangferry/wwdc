#!/usr/bin/env python3
"""Run retrieval and routing checks against realistic WWDC questions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

DISTILLER_DIR = Path(__file__).resolve().parent


def load_runtime(skill: Path):
    module_path = skill / "scripts" / "wwdc_runtime.py"
    spec = importlib.util.spec_from_file_location("wwdc_runtime_eval", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load runtime module: {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", default="skills/wwdc-notes", help="Runtime skill directory")
    args = parser.parse_args()
    skill = Path(args.skill).resolve()
    runtime = load_runtime(skill)
    cases = json.loads((DISTILLER_DIR / "evaluations" / "questions.json").read_text(encoding="utf-8"))
    passed = 0
    details = []
    for case in cases:
        routed, sessions, concepts = runtime.search_records(case["question"], 8)
        expected = set(case["expectedDomains"])
        routed_hit = bool(expected & set(routed))
        session_hit = any(expected & set(result["domains"]) for result in sessions)
        concept_hit = any(expected & set(result["domains"]) for result in concepts)
        source_hit = any(result.get("source", "").startswith("WWDC") for result in sessions)
        ok = routed_hit and (session_hit or concept_hit) and source_hit
        passed += int(ok)
        details.append(
            {
                "id": case["id"],
                "passed": ok,
                "expectedDomains": case["expectedDomains"],
                "routedDomains": routed,
                "topConcepts": [result["key"] for result in concepts[:3]],
                "topSources": [result["source"] for result in sessions[:3]],
            }
        )
    report = {"passed": passed, "total": len(cases), "score": round(passed / len(cases), 3), "cases": details}
    report_path = DISTILLER_DIR / "evaluations" / "latest-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
