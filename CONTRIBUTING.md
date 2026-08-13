# Contributing

Thanks for your interest. This plugin is a **solo-maintained** set of skills for
human-directs-agents development, and — importantly — its own repository runs the
workflow the skills describe. Contributions are welcome; they're evaluated the
same way the plugin asks every project to evaluate change: **on evidence, not
theory.**

## The premise

The plugin's own `agentic-workflow-evolution` skill sets the bar: a workflow
change earns its place through repeated, real-world evidence, not because it
sounds right. When you propose a change, the first question will be *"what lived
failure or recurring pattern does this fix?"* — so lead with that.

## How to propose a change

1. **Open an Issue first.** Use the templates:
   - **Bug** — a skill, script, or documented behavior doesn't work as described.
   - **Enhancement** — a new skill or an improvement, with the evidence for it.
   - **Investigation** — an open question to research before it's actionable.
   - **Needs decision** — a consequential choice the maintainer must ratify.
2. **Wait for direction on non-trivial work.** New skills and behavior changes
   are design decisions; a quick Issue discussion saves a wasted PR.
3. **Branch, implement, open a draft PR.** Draft after your first coherent green
   commit; the PR template lists what's expected. Mark ready only once it's been
   reviewed.
4. **Bring evidence.** For scripts: red→green test output. For skills: routing or
   execution eval results (`evals/`), or the concrete example that motivated the
   change.

## Local checks

- **Migration validators** (only if you touch `agentic-docs-github-migration`):
  ```
  bash skills/agentic-docs-github-migration/scripts/run_fixtures.sh
  ```
  Requires Python 3.10+ and `pyyaml`. This is the check CI enforces.
- **Skill hygiene:** every `SKILL.md` stays under 500 lines; every sibling and
  `references/`/`assets/`/`scripts/` pointer must resolve.

## Scope

This plugin models a **single ratifying maintainer**. It can be adapted to teams,
but PRs that assume multi-maintainer governance, org compliance, or team review
as a built-in aren't in scope — see the "Model" section of the README.

## Conduct

Be direct, be reasonably polite, bring evidence. Disagreement about the workflow is expected and
welcome, that's how it improves.
