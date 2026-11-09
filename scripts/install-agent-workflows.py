#!/usr/bin/env python3
"""Compatibility wrapper: prefer install-skills.py for the unified architecture."""
from pathlib import Path
import runpy
if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("install-skills.py")), run_name="__main__")
