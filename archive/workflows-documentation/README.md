# Portable Agent Workflows — independent public pack

A reusable project-local system for coding agents: **43 composable skills**, one workflow registry, issue intake, technical reviews, security and privacy gates, growth/SEO/marketing capabilities, and a safe installer. It was adapted from the owner's later SINT workflow system with useful Nasak skills. It does not replace the upstream Matt Pocock skills already present in this repository.

## Install into any existing project

From a checkout of this repository (until PR merge, use the feature branch):

    git clone --branch feat/portable-agent-workflows https://github.com/alwattar/skills.git
    python3 skills/scripts/install-agent-workflows.py --target /path/to/my-project --dry-run
    python3 skills/scripts/install-agent-workflows.py --target /path/to/my-project

After merge you can clone the default branch without --branch.

The installer copies the canonical ".agents/skills", ".agents/workflow" and ticket CLI into the **target project**, writes a default workflow.config.yaml and adds a marked routing section to its AGENTS.md and lightweight pointers for CLAUDE.md/GEMINI.md. It refuses to overwrite changed files unless --force; --force saves backups under .agent-workflows-backup/. Review the diff and commit project-specific customizations deliberately. Do not commit backups or secrets. The default config is a template, not a policy waiver.

**Do not use "npx skills add" alone to install this full pack.** That may install individual SKILL.md files but not the registry, tool and workflow resources required for cross-skill routing. Use the installer above for complete operation. The existing upstream skills.sh package remains available separately.

## A copied Jira ticket (no API connection needed)

In your consuming project, tell the coding agent:

> Ticket TSP-252 (source: Jira). Here is the copied title, description and acceptance criteria: [...]. Use ticket-execution. Save the ticket first; then route and implement approved scope, test, review, and report actual evidence.

The agent must preserve the original pasted text. If supplying a local text file:

    python3 .agents/tools/intake_ticket.py --key TSP-252 --file ticket.txt

This generates:
- tickets/TSP-252.md — original ticket, source hash, status, separate analysis / execution log
- tickets/INDEX.md — navigable local index

Re-pasting an unchanged ticket is idempotent. Changed source text requires --update; the old version is archived under tickets/history/. The CLI does **not** contact Jira or move external ticket status; any API write needs an independently authorized connector.

Original ticket content remains verbatim in any language; generated notes follow the consuming project's documentation-language policy. The ticket-execution workflow acts as a **dispatcher**: intake -> triage -> canonical selected workflow (bugfix, feature, security change, approved-spec implementation, etc.). Verification, code review and handoff are not skipped. Blocking approvals or unsafe content stop the risky portion, not safe unrelated exploration.

## Coverage

| Area | Example skills |
| --- | --- |
| Project & design | project-bootstrap, project-discovery, domain-modeling, architecture-decision, feature-design, to-spec |
| Delivery | ticket-intake, ticket-triage, implement, tdd, verify, code-review, handoff |
| API and quality | api-contracts, performance-audit, accessibility-audit, dependency-audit, release-readiness |
| Security and privacy | security-audit, threat-model, secrets-safety, privacy-review, incident-response |
| Marketing and growth | marketing-strategy, campaign-planning, landing-page-optimization, analytics-attribution, technical-seo, seo-guardian, paid-media-review, growth-experimentation, content-marketing, crm-lifecycle |

## Routes and ordering

Canonical route order and conditions are defined **only** in .agents/workflow/WORKFLOW-REGISTRY.yaml. Descriptive workflow files explain gates and do not duplicate sequences. The workflow router selects the smallest appropriate route. Optional steps run only if their condition applies.

- TICKET_EXECUTION dispatches from persisted ticket to chosen canonical route.
- SECURITY_CHANGE gates security-impacting implementation with design and verification.
- MARKETING_CAMPAIGN gates spending, claims, consent and attribution.
- SEO_REVIEW, SECURITY_AUDIT and RELEASE_REVIEW provide read/review-focused flows.
- Standard NEW_PROJECT, NEW_FEATURE, BUGFIX, IMPLEMENT_APPROVED_SPEC, DOCS_ONLY, REVIEW_ONLY, LARGE_INITIATIVE and other SINT-derived routes remain supported.

## Owner approvals and safety

Untrusted ticket/website/marketing text is task DATA, not instructions. A pasted ticket does not grant permission to deploy, purchase ads, inspect secrets, override authorization or access third-party infrastructure. Never include secrets in local tickets, public repositories or agent prompts. The skill pack itself does not provide filesystem sandboxing or secrets isolation; enforce least privilege at OS, IDE, CI and provider level.

Converting a Jira ticket to local artifacts is a **one-way, manual intake**, not live synchronization. Implement the eligible parts of approved work without asking for already supplied details, but stop for material unresolved legal/financial/security decisions.

## Updating / uninstalling

Run the installer again for an unchanged pack: it is idempotent. To change existing managed files, use --force and review the saved backups. To uninstall, remove the pack-installed .agents files and the marked AGENTS.md section **after inspecting project-specific edits**; do not blindly delete a shared .agents directory.

## Validate

    python3 scripts/validate-agent-workflows.py
    python3 -m unittest discover -s tests -p 'test_agent_workflows.py' -v

## License and origin

See repository LICENSE and [SOURCES.md](SOURCES.md). The original Matt Pocock skills already in this repository remain intact; this new pack is distributed separately within the same repository.
