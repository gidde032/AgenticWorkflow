# Documentation Impact Contract Reference

Use this reference to decide which project documents a completed change must
refresh. Prefer the project's actual filenames; the names below are examples.

## Document-trigger matrix

This matrix answers *when* a surface needs refreshing. For *which* surface owns
a given fact, read `references/what-goes-where.md` first.

| Surface | Update when | Preserve while editing |
|---|---|---|
| GitHub Issue | Scope, acceptance criteria, dependency, disposition, or remaining work changes | Durable work authority |
| GitHub Milestone | Committed horizon or Issue membership changes | Ratified delivery scope |
| Pull request | Implementation, review, verification, documentation impact, or merge readiness changes | Delivery record |
| State (`handoff.md`) | Active Issue, branch, PR, blocker, verified state, or next command changes | Immediate continuity only |
| Optional `TASKS.md` | Current session's mechanical steps change | No durable history |
| Conditional `ROADMAP.md` | Multi-horizon direction changes | High-level, Issue-linked direction |
| Optional phase summary | A qualifying multi-Issue or consequential phase closes | Immutable synthesis |
| Operating rules | Durable commands, workflow rules, safety boundaries, source-of-truth map, or invariants change | Rules only |
| User documentation | Setup, commands, outputs, workflows, limitations, or visible behavior changes | Tested examples and truthful boundaries |
| Spec, ADR, API, or schema docs | Accepted scope, decision, interface, schema, budget, or architecture changes | Rationale and explicit deviations |
| Operations docs | Deployment, migration, recovery, monitoring, or incident procedure changes | Exact ordering and prerequisites |
| Conditional changelog/release notes | User-visible versioned change lands | Curated release language |
| Practices/narrative | Workflow evidence or workflow shape changes | Evidence and superseded history |

## Change-to-document prompts

Ask these against the actual diff or workspace, not the implementation report:

- Would a new user follow different setup or usage steps?
- Would a maintainer run a different command or diagnose a failure differently?
- Did scope, status, priority, a milestone, or the next step change?
- Did an interface, schema, budget, architecture decision, or supported behavior change?
- Did a durable agent instruction or quality gate change?
- Did files move or names change, creating stale paths or links?
- Does the release description now differ from what shipped?

## Verification menu

Choose checks proportional to the claim:

- Run documented commands in the documented order when practical.
- Test code snippets or examples that can silently drift.
- Grep project-wide for renamed or moved paths and retired terminology.
- Validate internal links, anchors, and referenced files.
- Pair stable user-facing promises with docs-content or smoke tests.
- Compare the owning Issue, milestone, PR, handoff, conditional roadmap,
  conditional changelog, and optional phase summary for contradictions.
- Confirm that secondary documents link to the authority instead of reproducing
  mutable status.
- Record any check that could not run and why; keep unverified text visibly
  provisional.

## Completion rule

Do not mark the work complete until the return includes the tracking and
documentation accounting below:

```text
Tracking impact
- Issue/milestone: <updated state and links, or none with reason>
- Pull request: <updated state and link, or not applicable>

Documentation impact
- Updated: <paths and why, or none>
- Reviewed; no change needed: <paths and why, or none>
- Verification: <checks and results, or explicit limitation>
```

Treat an omitted line, an unnamed authority or documentation surface, or an
unsupported freshness claim as incomplete work.
