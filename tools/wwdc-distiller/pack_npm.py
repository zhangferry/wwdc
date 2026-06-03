#!/usr/bin/env python3
"""Create the npm package used to distribute the WWDC Notes skill."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


PACKAGE_NAME = "@zhangferry-dev/wwdc-notes"
SKILL_NAME = "wwdc-notes"


INSTALLER = """#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const packageRoot = path.resolve(__dirname, "..");
const skillSource = path.join(packageRoot, "skill", "wwdc-notes");

const targets = new Map([
  ["codex", path.join(os.homedir(), ".codex", "skills")],
  ["claude", path.join(os.homedir(), ".claude", "skills")],
]);

function usage() {
  console.log(`WWDC Notes skill installer

Usage:
  npx @zhangferry-dev/wwdc-notes install codex
  npx @zhangferry-dev/wwdc-notes install claude
  npx @zhangferry-dev/wwdc-notes install --target ~/.codex/skills

Commands:
  install [codex|claude]        Install to a known agent skills directory
  install --target <directory>  Install to a custom skills directory
`);
}

function expandHome(input) {
  if (input === "~") return os.homedir();
  if (input.startsWith("~/")) return path.join(os.homedir(), input.slice(2));
  return input;
}

function resolveTarget(args) {
  const targetFlag = args.indexOf("--target");
  if (targetFlag !== -1) {
    const value = args[targetFlag + 1];
    if (!value) throw new Error("missing value after --target");
    return path.resolve(expandHome(value));
  }

  const targetName = args[0] || "codex";
  if (targets.has(targetName)) return targets.get(targetName);
  return path.resolve(expandHome(targetName));
}

function install(args) {
  if (!fs.existsSync(skillSource)) {
    throw new Error(`package is missing skill payload: ${skillSource}`);
  }

  const skillsRoot = resolveTarget(args);
  const destination = path.join(skillsRoot, "wwdc-notes");
  fs.mkdirSync(skillsRoot, { recursive: true });
  fs.rmSync(destination, { recursive: true, force: true });
  fs.cpSync(skillSource, destination, {
    recursive: true,
    filter: (source) => !source.includes("__pycache__") && !source.endsWith(".pyc"),
  });
  console.log(`Installed WWDC Notes skill to ${destination}`);
}

const [command, ...args] = process.argv.slice(2);

try {
  if (!command || command === "--help" || command === "-h") {
    usage();
  } else if (command === "install") {
    install(args);
  } else {
    throw new Error(`unknown command: ${command}`);
  }
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
"""


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", default="skills/wwdc-notes", help="Runtime skill directory")
    parser.add_argument("--out", default=".dist/wwdc-notes-npm", help="npm package output directory")
    parser.add_argument("--version", help="Package version. Defaults to the root package version")
    args = parser.parse_args()

    root = Path.cwd()
    skill = Path(args.skill).expanduser()
    if not skill.is_absolute():
        skill = (root / skill).resolve()
    out = Path(args.out).expanduser()
    if not out.is_absolute():
        out = (root / out).resolve()

    if not (skill / "SKILL.md").is_file():
        parser.error(f"missing runtime skill: {skill}")

    root_package = json.loads((root / "package.json").read_text(encoding="utf-8"))
    version = args.version or root_package.get("version", "0.0.0")

    if out.exists():
        shutil.rmtree(out)
    (out / "bin").mkdir(parents=True)
    package_skill = out / "skill" / SKILL_NAME
    shutil.copytree(
        skill,
        package_skill,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

    installer = out / "bin" / "wwdc-notes.js"
    installer.write_text(INSTALLER, encoding="utf-8")
    installer.chmod(0o755)

    package_json = {
        "name": PACKAGE_NAME,
        "version": version,
        "type": "module",
        "description": "Install the WWDC Notes skill for Codex or Claude.",
        "license": "MIT",
        "publishConfig": {"access": "public"},
        "bin": {"wwdc-notes": "bin/wwdc-notes.js"},
        "files": ["bin", "skill", "README.md"],
        "keywords": ["wwdc", "codex-skill", "claude-skill", "apple", "swift", "swiftui"],
        "repository": {
            "type": "git",
            "url": "git+ssh://git@github.com/zhangferry/wwdc.git",
            "directory": ".dist/wwdc-notes-npm",
        },
    }
    write_json(out / "package.json", package_json)

    readme = f"""# WWDC Notes Skill

离线 WWDC 2020-2025 Apple 平台开发知识 skill。

## Install

```bash
npx {PACKAGE_NAME} install codex
```

或安装到 Claude：

```bash
npx {PACKAGE_NAME} install claude
```

自定义 skills 目录：

```bash
npx {PACKAGE_NAME} install --target ~/.codex/skills
```

安装后使用 `$wwdc-notes` 查询 Swift、SwiftUI、UIKit、AppKit、并发、Xcode、visionOS、Core ML 等 WWDC 知识。
"""
    (out / "README.md").write_text(readme, encoding="utf-8")

    print(f"Packed {PACKAGE_NAME}@{version} to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
