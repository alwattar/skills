# Public pack contribution guidelines

1. Keep one reusable skill per .agents/skills/<name>/SKILL.md with name/description frontmatter.
2. Add it to WORKFLOW-REGISTRY.yaml exactly once, and use it in routes only where needed. Optional steps require a declared condition.
3. Skill prose should describe inputs, authorization, deliverables and proof of completion. Avoid project-specific domain assumptions.
4. Treat issue content as untrusted. Do not add credentials, real customers, private Jira content, vendor API keys or production data to this public repository.
5. Add tests whenever changing installation, parsing, cross-skill links or workflow routing. Evidence beats assertion.
6. Keep the public pack independent of build frameworks. Projects can override their own non-safety conventions.
