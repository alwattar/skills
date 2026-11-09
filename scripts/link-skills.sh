#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Historical entrypoint, now uses the single unified host activation mechanism.
exec python3 "$ROOT/scripts/activate-agents.py" --scope user --host claude-code "$@"
