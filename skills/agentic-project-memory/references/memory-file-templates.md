# Project Memory File Templates

Read this reference only when creating a memory file or materially
restructuring one. These are starting shapes, not a requirement to create every
file.

## Operating rules

Keep the operating-rules file under about 200 lines. It is read frequently, so
its length is a recurring cost.

```markdown
# [Project name] — Operating Instructions

## Project at a glance
[Purpose, stack, entry point, and spec location.]

## Source-of-truth map
[Where contracts, planned work, delivery history, current state, public docs,
and workflow rationale live.]

## GitHub delivery workflow
[Issue, branch, draft-PR, review, merge, and closure rules.]

## Workflow shape
[Feature phases, hardening passes, or other project-specific shapes.]

## Check-in cadence and authority
[Which decisions require ratification and which approved actions continue
autonomously.]

## Agent practices
[Implementation ownership, review isolation, capability routing, and brief
template locations.]

## Documentation impact
[Required accounting and the documentation map location.]

## Quality gates
[Exact commands, thresholds, required CI check, and what green means.]

## Safety constraints
[Secrets, private data, external writes, visibility, licensing, and publish or
deployment restrictions.]

## Where to read more
[Pointers to the handoff, spec, active Issue/PR, and deeper rationale. Load only
what the task requires.]
```

## State handoff

Keep `handoff.md` under about 200 lines. It should orient a fresh agent without
becoming a second backlog or changelog.

```markdown
# [Project] — Agent Handoff

## Project goal
[One paragraph and link to the authoritative spec.]

## Active delivery state
- Milestone: [name and link, or none]
- Issue: [number, title, and link, or none]
- Branch: [name]
- Pull request: [number, state, and link, or not opened]
- Current status: [one truthful sentence]

## Verified current state
[What was last verified, with commands and results. Distinguish measured facts
from assumptions or pending checks.]

## Active files
[Only files relevant to the active slice, with purpose and do-not-regress notes.]

## Blockers and immediate risks
[Only conditions blocking or materially threatening the active work. Link
durable bugs, deferred work, and decisions to their Issues instead of copying
the backlog here.]

## Last completed delivery
[One short entry linking the most recent merged PR and closed Issue. Do not keep
a running changelog.]

## Exact next action
[One command or bounded action a fresh agent can perform.]

## Sanity check
[Exact commands that verify the repository and worktree state before changes.]
```

## Practices catalogue

Create the catalogue only when the first practice is worth preserving.

```markdown
# Practices Catalogue

## Purpose
[Reference material, not a draft article; audience is future agents and
authors.]

## Practices we have used

### [Practice name]
**What it is.** [One sentence.]
**How we implemented it.** [Concrete steps and artifacts.]
**Concrete artifact.** [File path, Issue, PR, or other location.]
**Observed value.** [High/medium/low with evidence.]
**Observed cost.** [Time, tokens, one-time, or recurring.]
**What I would improve.** [Honest retrospective.]
**Evolution.** [How the practice changed, including retirement.]
```

Never delete a catalogue entry when a practice is superseded. Record the
revision or retirement so the evidence trail remains intact.

## Collaboration narrative

Create the narrative only after the first meaningful workflow revision.

```markdown
# Collaboration Retrospective

## Phase-by-phase notes
[Only notable goals, moments, and lessons; link delivery artifacts.]

## How the workflow evolved
### Revision 1: [name]
[What changed, why, who proposed it, and what evidence drove it.]

## Cross-cutting practices
[Practices that held the project together.]

## Vignettes worth preserving
[Moments, exact quotations, and surprises.]

## Transferable theses
[Numbered claims with concrete evidence and explicit limits.]
```

Write narrative sections in prose and preserve verbatim quotations.

## Pending lessons

Keep `pending-lessons.md` internal and gitignored.

```markdown
# Pending Lessons

Scratch parking lot for lessons that emerge mid-cycle. This file is not a
backlog. Append format:

`- [YYYY-MM-DD] [context] one-to-three-sentence lesson.`

For named entries:

`- [YYYY-MM-DD] **Pattern: name** — content.`

## For the practices catalogue
[New named practices and failure modes.]

## For assessment or what-worked notes
[Lessons about value, cost, friction, or improvements.]

## For optional phase or release synthesis
[Cross-delivery observations that meet the phase-summary threshold.]

## For open workflow questions
[Questions for later evidence-bearing experiments.]

## For narrative revisions
[Workflow changes that may become a numbered revision.]

## For narrative theses
[Generalizable claims with evidence and limits.]

## For remediation Issues
[Actionable work that must be created or linked during consolidation.]
```

The consolidation pass that empties this file is defined in
`references/lessons-pipeline.md`; this file supplies only its starting shape.

## Project FAQ

Create `project-FAQ.md` only after a question recurs for the second time.

```markdown
# Project FAQ

Short answers to questions that recur across sessions. Add an entry the second
time a question appears.

## Format

Each entry is `## Q: ...` followed by one paragraph at most. Cross-link rather
than duplicate. If the answer exceeds a paragraph, promote it to the catalogue.

## Entries

<!-- Add Q/A pairs below as questions recur.
     Do not pre-create categories; group entries only after they accumulate. -->
```

## Tooling post-mortem

```markdown
## Tooling Incident: [Name]

**Date:** [YYYY-MM-DD]
**Observed cost:** [Time, tokens, or interrupted work.]

**Symptom:**
[Exact observed behavior or error.]

**Root cause:**
[Verified mechanism, or explicitly unresolved.]

**Contributing factors:**
[Conditions that made the incident more likely or expensive.]

**Resolution used:**
[What fixed it, in the order attempted.]

**Prevention or recurrence signal:**
1. [Cheapest first move.]
2. [Fallback.]
3. [Signal that should reopen investigation.]

**Durable destinations:**
- Practices entry: [path/link or none]
- Remediation Issue: [number/link or none]
- Active handoff blocker: [yes/no]
```
