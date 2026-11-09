"""Regression tests for project-local intake, safe installation and unified skill routing."""
from pathlib import Path
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TICKET = ROOT / "tools/intake_ticket.py"
INSTALL = ROOT / "scripts/install-skills.py"
VALIDATE = ROOT / "scripts/validate-skills.py"
GUIDES = ROOT / "scripts/generate-docs.py"

spec = importlib.util.spec_from_file_location("ticket_intake", TICKET)
ticket = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ticket)


def command(script, *opts):
    return subprocess.run([sys.executable, str(script), *opts], capture_output=True, text=True)


class TicketTests(unittest.TestCase):
    def test_import_idempotency_revision_and_index(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            raw = "# Login bug\n\nDescription: cannot sign in"
            self.assertIn("saved:", ticket.import_ticket(root, "APP-101", raw, "Jira", False))
            self.assertIn(raw, (root / "tickets/APP-101.md").read_text())
            previous = (root / "tickets/APP-101.md").read_text()
            self.assertIn("unchanged:", ticket.import_ticket(root, "APP-101", raw, "Jira", False))
            self.assertEqual(previous, (root / "tickets/APP-101.md").read_text())
            with self.assertRaisesRegex(ValueError, "Use --update"):
                ticket.import_ticket(root, "APP-101", raw + " revised", "Jira", False)
            ticket.import_ticket(root, "APP-101", raw + " revised", "Jira", True)
            self.assertTrue((root / "tickets/history/APP-101-rev1.md").exists())

    def test_rejects_path_traversal_secrets_and_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "../../bad", "any", "Jira", False)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "APP-42", "password=abcd1234supersecret", "Jira", False)
            external = root / "outside"
            external.mkdir()
            (root / "tickets").symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                ticket.import_ticket(root, "APP-42", "safe text", "Jira", False)

    def test_preserves_fenced_ticket_text(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ticket.import_ticket(root, "X-2", "# Test\n~~~\ncontent\n~~~~~", "Other", False)
            self.assertIn("~~~~~~text", (root / "tickets/X-2.md").read_text())


class InstallerTests(unittest.TestCase):
    def test_dry_run_idempotency_and_project_settings(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text("# Local project rules\n")
            (root / "workflow.config.yaml").write_text("project_override: true\n")
            self.assertEqual(0, command(INSTALL, "--target", temp, "--dry-run").returncode)
            self.assertFalse((root / "skills").exists())
            self.assertEqual(0, command(INSTALL, "--target", temp).returncode)
            self.assertEqual(0, command(INSTALL, "--target", temp).returncode)
            self.assertIn("# Local project rules", (root / "AGENTS.md").read_text())
            self.assertEqual(1, (root / "AGENTS.md").read_text().count("<!-- unified-skills:start -->"))
            self.assertEqual("project_override: true\n", (root / "workflow.config.yaml").read_text())
            self.assertTrue((root / "skills/review-design/README.ar.md").exists())
            self.assertTrue((root / "registry/registry.yaml").exists())
            self.assertTrue((root / ".agent-skills-lock.json").exists())

    def test_unowned_existing_file_aborts_without_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            conflict = root / "skills/grill/SKILL.md"
            conflict.parent.mkdir(parents=True)
            conflict.write_text("user-owned content")
            proc = command(INSTALL, "--target", temp)
            self.assertEqual(2, proc.returncode, proc.stdout + proc.stderr)
            self.assertFalse((root / "registry").exists())
            self.assertEqual("user-owned content", conflict.read_text())

    def test_modified_managed_file_needs_force_and_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertEqual(0, command(INSTALL, "--target", temp).returncode)
            target = root / "skills/grill/SKILL.md"
            target.write_text("local modifications")
            proc = command(INSTALL, "--target", temp)
            self.assertEqual(2, proc.returncode)
            self.assertEqual("local modifications", target.read_text())
            self.assertEqual(0, command(INSTALL, "--target", temp, "--force").returncode)
            backups = list((root / ".agent-skills-backup").rglob("SKILL.md"))
            self.assertTrue(backups)
            self.assertEqual("local modifications", backups[0].read_text())

    def test_legacy_install_stops_safely(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / ".agents/workflow"
            folder.mkdir(parents=True)
            (folder / "WORKFLOW-REGISTRY.yaml").write_text("legacy")
            self.assertEqual(2, command(INSTALL, "--target", temp).returncode)
            self.assertFalse((root / "skills").exists())


class RegistryTests(unittest.TestCase):
    def test_canonical_registry_and_security_order(self):
        proc = command(VALIDATE)
        self.assertEqual(0, proc.returncode, proc.stdout + proc.stderr)

    def test_bilingual_guides_synchronized(self):
        proc = command(GUIDES, "--check")
        self.assertEqual(0, proc.returncode, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
