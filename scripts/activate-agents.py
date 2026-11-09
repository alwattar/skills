#!/usr/bin/env python3
"""Safely expose the canonical skill library in Codex and Claude Code discovery paths."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DISCOVERY = {
    "codex": Path(".agents/skills"),
    "claude-code": Path(".claude/skills"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Existing project directory for project scope")
    parser.add_argument("--host", action="append", choices=sorted(DISCOVERY), required=True)
    parser.add_argument("--scope", choices=("project", "user"), default="project")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        target = Path(args.target).resolve()
        if args.scope == "project" and not target.is_dir():
            raise ValueError("Project target must exist")
        source = (ROOT if args.scope == "user" else target) / "skills"
        registry_file = (ROOT if args.scope == "user" else target) / "registry/registry.yaml"
        if not registry_file.is_file() or not source.is_dir():
            raise ValueError("Install the unified skills first, or use user scope from a checked-out source repository")
        entries = json.loads(registry_file.read_text(encoding="utf-8"))["skills"]
        root = Path.home() if args.scope == "user" else target
        plan = []
        for host in sorted(set(args.host)):
            directory = root / DISCOVERY[host]
            if directory.is_symlink():
                raise ValueError(f"Refusing symlinked skill discovery directory: {directory}")
            for name in entries:
                src = source / name
                if not src.is_dir() or not (src / "SKILL.md").is_file() or src.is_symlink():
                    raise ValueError(f"Missing or unsafe source skill: {src}")
                destination = directory / name
                link_value = os.path.relpath(src, directory)
                if destination.is_symlink():
                    if os.readlink(destination) != link_value:
                        raise ValueError(f"Foreign symlink at {destination}, refusing replacement")
                    plan.append(("existing", destination, link_value))
                elif destination.exists():
                    raise ValueError(f"User-owned skill exists at {destination}, refusing replacement")
                else:
                    plan.append(("create", destination, link_value))
        if args.dry_run:
            for action, path, value in plan:
                print(f"{action}: {path} -> {value}")
            return 0
        for action, path, value in plan:
            if action == "create":
                path.parent.mkdir(parents=True, exist_ok=True)
                path.symlink_to(value, target_is_directory=True)
        print(f"Activated {len(entries)} skills for {len(set(args.host))} host(s), scope={args.scope}")
        print("Restart the selected agent sessions to refresh skill discovery.")
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print("Activation blocked:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
