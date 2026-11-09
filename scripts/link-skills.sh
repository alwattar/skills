#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"
for skill in "$ROOT"/skills/*/SKILL.md; do
  [ -f "$skill" ] || continue
  source="$(dirname "$skill")"
  name="$(basename "$source")"
  dest="$DEST/$name"
  if [ -L "$dest" ]; then
    if [ "$(readlink "$dest")" != "$source" ]; then
      echo "skip foreign symlink: $dest" >&2
      continue
    fi
  elif [ -e "$dest" ]; then
    echo "skip existing user skill: $dest" >&2
    continue
  fi
  ln -sfn "$source" "$dest"
  echo "linked $name"
done
echo "For workflows, also load registry/registry.yaml and project policies."
