#!/usr/bin/env python3
"""Install a standalone copy of the runtime WWDC Notes skill."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

DEFAULT_TARGETS = {
    "codex": Path.home() / ".codex" / "skills",
    "claude": Path.home() / ".claude" / "skills",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", default="skills/wwdc-notes", help="Runtime skill directory")
    parser.add_argument("--target", required=True, help="codex, claude, or a custom skills directory")
    args = parser.parse_args()
    skill = Path(args.skill).resolve()
    root = DEFAULT_TARGETS.get(args.target, Path(args.target).expanduser()).resolve()
    destination = root / "wwdc-notes"
    if destination == skill:
        parser.error("destination is the source skill directory")
    root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        skill,
        destination,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    print(f"Installed WWDC Notes skill to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
