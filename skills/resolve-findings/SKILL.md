---
name: resolve-findings
description: Triage, resolve and record design review findings and approvals.
---
# Resolve Findings

**Use when:** design, human or security reviews produce actionable findings.

1. Read the design, review artifacts, original constraints, owner decisions and evidence.
2. Classify each finding: ACCEPTED, REJECTED, DEFERRED, UNRESOLVED; include rationale, impact, source and proposed follow-up.
3. Update the design only for accepted changes. Do not silently weaken an invariant or acceptance criterion.
4. Ask the owner before material security, architecture, payments or production decisions. Do not treat silence as approval.
5. Re-run an independent review when material, high-risk changes require it and fresh-context delegation exists.

**Output:** findings ledger, design revision, change summary, unresolved blockers and approval evidence.
**Next:** `architecture-decision` for material choices, `to-spec` for approved work.
