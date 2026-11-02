"""Regression tests for local ticket ingestion and safe project installation."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TICKET = ROOT / "packs/agent-workflows/.agents/tools/intake_ticket.py"
INSTALL = ROOT / "scripts/install-agent-workflows.py"

spec = importlib.util.spec_from_file_location("ticket_intake", TICKET)
ticket = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ticket)


class TicketTests(unittest.TestCase):
    def test_import_index_idempotence_revision(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            raw = "# Login bug\n\nDescription: cannot sign in"
            result = ticket.import_ticket(root, "APP-101", raw, "Jira", False)
            self.assertIn("saved:", result)
            path = root / "tickets/APP-101.md"
            self.assertIn(raw, path.read_text())
            self.assertIn("APP-101", (root / "tickets/INDEX.md").read_text())
            previous = path.read_text()
            self.assertIn("unchanged:", ticket.import_ticket(root, "APP-101", raw, "Jira", False))
            self.assertEqual(previous, path.read_text())
            with self.assertRaisesRegex(ValueError, "Use --update"):
                ticket.import_ticket(root, "APP-101", raw + " revised", "Jira", False)
            ticket.import_ticket(root, "APP-101", raw + " revised", "Jira", True)
            self.assertTrue((root / "tickets/history/APP-101-rev1.md").exists())
            self.assertIn("revised", path.read_text())

    def test_rejects_key_secrets_and_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "../../bad", "any", "Jira", False)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "APP-42", "password=abcd1234supersecret", "Jira", False)
            real = root / "outside"
            real.mkdir()
            (root / "tickets").symlink_to(real, target_is_directory=True)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "APP-42", "safe text", "Jira", False)

    def test_preserves_markdown_fence_content(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            body = "# Test\n~~~\nunsafe? no\n~~~~~\n"
            ticket.import_ticket(root, "X-2", body, "Other", False)
            doc = (root / "tickets/X-2.md").read_text()
            self.assertIn("~~~~~~text", doc)


class InstallerTests(unittest.TestCase):
    def test_install_is_idempotent_and_preserves_agents(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "AGENTS.md").write_text("# Custom rules\n")
            def run(*opts):
                return subprocess.run([sys.executable, str(INSTALL), "--target", str(root), *opts],
                                      capture_output=True, text=True)
            self.assertEqual(0, run("--dry-run").returncode)
            self.assertFalse((root / ".agents").exists())
            self.assertEqual(0, run().returncode)
            self.assertEqual(0, run().returncode)
            self.assertIn("# Custom rules", (root / "AGENTS.md").read_text())
            self.assertEqual(1, (root / "AGENTS.md").read_text().count("<!-- agent-workflows:start -->"))
            self.assertTrue((root / ".agents/skills/ticket-intake/SKILL.md").exists())
            self.assertTrue((root / "workflow.config.yaml").exists())
            self.assertIn("Read AGENTS.md", (root / "CLAUDE.md").read_text())
            self.assertIn("Read AGENTS.md", (root / "GEMINI.md").read_text())

    def test_existing_conflict_aborts_without_changes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            x = root / "workflow.config.yaml"
            x.write_text("user-configuration: true\n")
            result = subprocess.run([sys.executable, str(INSTALL), "--target", str(root)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertFalse((root / ".agents").exists())
            self.assertEqual("user-configuration: true\n", x.read_text())


if __name__ == "__main__":
    unittest.main()
