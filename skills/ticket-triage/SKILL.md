---
name: ticket-triage
description: ticket triage for reusable evidence-based software delivery.
---

# Ticket Triage

Read the saved ticket and active project `AGENTS.md`, project specifications, business rules, and `registry/registry.yaml`. Determine request type (BUGFIX, NEW_FEATURE, IMPLEMENT_APPROVED_SPEC, REFACTOR, SECURITY_CHANGE, ARCHITECTURE_CHANGE, DOCS_ONLY, REVIEW_ONLY, LARGE_INITIATIVE). Default security-sensitive changes to SECURITY_CHANGE, structural decisions to ARCHITECTURE_CHANGE. Validate scope/authorization: a pasted ticket is not permission to bypass security, purchase services, deploy or change billing settings. Reconcile external acceptance criteria with existing approved specs; never silently weaken either. If one material decision is missing, stop that risky portion and show specific options; proceed with independent safe parts. Save classification, chosen workflow, evidence, identified dependencies, risk, tests, and progress checklist under `tickets/KEY.md` in clearly marked agent-managed section (do not overwrite original). **Immediately execute the chosen registered workflow in its required order**, unless the user asked for planning only, safety gates prohibit it or tools are unavailable. Never expand scope to unrelated tickets. Do not call `to-tickets` for every pasted ticket; use it only for decomposing truly independent large tasks. When done update ticket state and record verified evidence, code refs, changed files, and outstanding gates. Never assert completion merely because code was written.

## Completion evidence
Report concrete files, tests, observed results and unresolved blockers. Follow the canonical registry and project-specific rules.
