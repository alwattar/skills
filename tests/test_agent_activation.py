"""Host discovery integration tests. No user-wide paths are touched."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "scripts/install-skills.py"
ACTIVATE = ROOT / "scripts/activate-agents.py"


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True)


class ActivationTests(unittest.TestCase):
    def test_codex_and_claude_use_same_skill_directory(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(0, run(INSTALL, "--target", d).returncode)
            args = ("--target", d, "--host", "codex", "--host", "claude-code")
            self.assertEqual(0, run(ACTIVATE, *args, "--dry-run").returncode)
            self.assertFalse((root / ".agents").exists())
            result = run(ACTIVATE, *args)
            self.assertEqual(0, result.returncode, result.stderr)
            codex = root / ".agents/skills/grill"
            claude = root / ".claude/skills/grill"
            self.assertTrue(codex.is_symlink())
            self.assertTrue(claude.is_symlink())
            self.assertEqual((root / "skills/grill").resolve(), codex.resolve())
            self.assertEqual(codex.resolve(), claude.resolve())
            self.assertEqual(0, run(ACTIVATE, *args).returncode)

    def test_foreign_skill_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(0, run(INSTALL, "--target", d).returncode)
            foreign = root / ".agents/skills/grill"
            foreign.mkdir(parents=True)
            (foreign / "SKILL.md").write_text("my own work")
            result = run(ACTIVATE, "--target", d, "--host", "codex")
            self.assertEqual(2, result.returncode)
            self.assertEqual("my own work", (foreign / "SKILL.md").read_text())
            self.assertFalse((root / ".agents/skills/verify").exists())

    def test_symlinked_discovery_parent_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(0, run(INSTALL, "--target", d).returncode)
            (root / "outside").mkdir()
            (root / ".agents").symlink_to(root / "outside", target_is_directory=True)
            result = run(ACTIVATE, "--target", d, "--host", "codex")
            self.assertEqual(2, result.returncode)
            self.assertFalse((root / "outside/skills").exists())


if __name__ == "__main__":
    unittest.main()
