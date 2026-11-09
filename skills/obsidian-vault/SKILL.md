---
name: obsidian-vault
description: Safely search, link and organize a user-specified Obsidian knowledge vault.
---

# Obsidian Vault

## Select the vault

Use an explicit vault path provided by the user, or a project-owned configuration value such as `knowledge.vault_path` in `workflow.config.yaml`. Do **not** assume a developer's absolute disk path or search the user's home directory to discover private notes.

If the vault path is missing, request it before reading or writing vault files. The user's vault content may be private; never ingest an entire vault without a scoped reason.

## Read and organize

- Search only the authorized path and requested notes using filenames or bounded content queries.
- Preserve Obsidian `[[wikilinks]]` and existing note naming conventions; do not assume all vaults are flat or use Title Case.
- Suggest index notes and backlinks when they materially improve navigation.
- For creating or editing notes, preserve unrelated data, use previews when appropriate, and respect the requested scope.
- Identify link collisions, duplicate titles and broken references without inventing files.
- Never sync a vault to a remote provider or public repository without explicit permission.

**Output:** note references, proposed/verified edits and links.
**Next:** `doc-sync` for recorded organizational decisions, or `verify` for link integrity.
