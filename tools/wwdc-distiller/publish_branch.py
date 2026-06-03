#!/usr/bin/env python3
"""Publish the runtime skill as a lightweight git branch."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def copy_skill(skill: Path, target: Path) -> None:
    for child in skill.iterdir():
        destination = target / child.name
        if child.is_dir():
            shutil.copytree(
                child,
                destination,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
        else:
            shutil.copy2(child, destination)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", default="skills/wwdc-notes", help="Runtime skill directory")
    parser.add_argument("--branch", default="skill", help="Git branch to update")
    parser.add_argument("--remote", default="origin", help="Git remote to push")
    args = parser.parse_args()

    root = Path.cwd()
    skill = Path(args.skill).expanduser()
    if not skill.is_absolute():
        skill = (root / skill).resolve()
    if not (skill / "SKILL.md").is_file():
        parser.error(f"missing runtime skill: {skill}")

    head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=root, text=True).strip()
    remote_url = subprocess.check_output(
        ["git", "remote", "get-url", args.remote],
        cwd=root,
        text=True,
    ).strip()
    with tempfile.TemporaryDirectory(prefix="wwdc-notes-skill-branch-") as temp:
        worktree = Path(temp)
        run(["git", "init", "-q"], worktree)
        run(["git", "checkout", "--orphan", args.branch], worktree)
        copy_skill(skill, worktree)
        (worktree / "README.md").write_text(
            "# WWDC Notes Skill\n\n"
            "Install with:\n\n"
            "```bash\n"
            "npx skills add zhangferry/wwdc#skill\n"
            "```\n\n"
            "This branch contains only the standalone runtime skill payload.\n",
            encoding="utf-8",
        )
        run(["git", "add", "-A"], worktree)
        run(
            [
                "git",
                "commit",
                "-q",
                "-m",
                f"Publish WWDC Notes skill from {head}",
            ],
            worktree,
        )
        run(["git", "remote", "add", args.remote, remote_url], worktree)
        run(["git", "push", args.remote, f"{args.branch}:{args.branch}", "--force"], worktree)

    print(f"Published {skill} to {args.remote}/{args.branch}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
