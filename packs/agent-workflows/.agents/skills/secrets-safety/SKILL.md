---
name: secrets-safety
description: Evidence-based secrets safety and prevention in software projects.
---

# Secrets Safety

Treat .env, system environment, local credentials, cloud tokens, private keys, database dumps, production analytics and personal identifiers as confidential. **Never print, ingest into model output, commit or copy sensitive values**. Inspect file paths/metadata without opening secrets unnecessarily; use redacted placeholders, secret scanners configured for minimal disclosure and repository .gitignore. Prefer short-lived scoped credentials, secret managers, least privilege, rotation and audit. On suspected exposure: stop propagation; notify owner; recommend revocation/rotation and repository history remediation without echoing values. An agent instruction file is not an OS security boundary: use sandbox permissions and scoped credentials as primary controls.

## Review output
List evidence, severity, affected boundary, verification and explicit open decisions. Obey project authorization and registered workflows.
