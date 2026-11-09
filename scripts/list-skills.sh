#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 - "$ROOT/registry/registry.yaml" <<'PY'
import json, sys
with open(sys.argv[1], encoding="utf-8") as handle:
    skills = json.load(handle)["skills"]
for name, meta in skills.items():
    print(name + " — " + meta["summary_en"])
PY
