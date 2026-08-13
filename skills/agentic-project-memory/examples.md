# Project memory — worked examples and provenance

Evidence behind the memory architecture in `SKILL.md`. Read a section when you
want the case behind a rule, or when judging whether a threshold fits your
project.

The reference project is a Python CLI built across six feature phases and
several hardening releases. The GitHub source-of-truth split comes from two
documentation-and-GitHub migrations on other repositories.

## Contents

1. What writing the handoff actually does
2. Phase summaries force synthesis
3. The tooling-incident arc
4. Lessons compound backward
5. Machine memory versus in-repo files
6. Provenance and maintenance

## 1. What writing the handoff actually does

On when to write it:

> "Write the handoff at the **start** of each phase rather than at session end.
> Treat it as the contract for the upcoming phase. If I always know exactly what
> a fresh agent would need, I'm always working from the same vantage point as
> that agent, and the doc updates as naturally as the code does."
> — the maintainer

On what the act of writing surfaces:

> "The act of writing it surfaced two things I'd been carrying around in my head:
> the spec deviations and the soft-delete-history-blackout gap. Both should have
> been documented earlier; the handoff doc forced them into writing."
> — the maintainer

The second quote is the argument for the first. A handoff written at session end
is a summary of what happened. A handoff written at phase start is a contract,
and writing it exposes the things you were carrying implicitly — which is
precisely when they are still cheap to act on.

## 2. Phase summaries force synthesis

From the practices catalogue:

> "Writing [phase summaries] forced synthesis — the agent noted that drafting
> summaries 'surfaced half-formed views I didn't know I had.'"

This is why the summary criteria are about *consequence* rather than effort. A
summary of a single-Issue slice has nothing to synthesize; the Issue and PR
already hold the record. A summary spanning several Issues has to reconcile them,
and that reconciliation is the product.

## 3. The tooling-incident arc

A file-system bridge between the agent sandbox and the host workspace hit a POSIX
deadlock (EDEADLK) on rapidly-edited files. It happened three times:

1. **First occurrence.** Roughly 20,000 tokens of in-place recovery before a
   workaround was found. No post-mortem was written at the time.
2. **Second occurrence.** A documented playbook now existed and absorbed the
   incident in a fraction of the tokens.
3. **Third occurrence.** The cheapest resolution was discovered — asking the user
   to re-open the project folder, which issues fresh inodes and clears the
   deadlock project-wide for one user action. It was promoted to the first move
   in the playbook.

Each occurrence cost less than the last, because the post-mortem existed. The
third improved the playbook rather than merely consuming it. That arc is the
argument for treating workflow and tooling failures like production incidents:

> "The practice of writing post-mortems for workflow incidents (not just code
> bugs) is itself novel. Most coding workflows treat tooling friction as
> ephemeral; agentic workflows benefit from treating it as documentable."
> — the maintainer

## 4. Lessons compound backward

> "Catalogued lessons compound *backward* — applying a lesson via a structural
> fix (a fixture, an explicit config, a project-wide convention) propagates the
> lesson to every existing piece of code, not just future ones. The argument for
> keeping the catalog low-friction to add to is no longer just defensive ('write
> the lesson down'); it's offensive ('write the lesson down so the *next*
> structural fix you make can apply it backward to all prior code')."
> — the maintainer

**Worked example.** A lesson about test fragility under narrow terminal widths
was written into the catalogue mid-project. When a shared fixture was later added
to `conftest.py` to address it, every existing test in the suite gained the
protection retroactively — including tests from phases that predated the lesson
by months. Two tests that had been silently fragile were fixed without anyone
having to find them.

The implication for documentation discipline: write lessons down with low
friction, and write structural fixes alongside lessons rather than as separate
work. A catalogued lesson that sits unread still compounds forward, because
future agents benefit. A lesson that produces a structural fix also compounds
backward.

## 5. Machine memory versus in-repo files

Agent-platform memory panels and per-project files hold different things, and
mixing them makes both worse.

Cross-session facts about *you* — preferences, cost posture, collaboration style
— belong in the platform's memory layer, because they are true across every
project and reloading them per project wastes context. Project-specific facts —
file paths, schema invariants, active delivery state — belong in the state file
or the owning contract, because they are worthless outside this repository and
change on a different clock.

Keeping the split clean keeps the operating-rules file short and the platform
memory useful across projects. This was observed on one project and has not been
exercised across different agent platforms or team settings, so treat the
boundary as sensible rather than proven.

## 6. Provenance and maintenance

The four-file memory architecture, lessons pipeline, granularity guidance, and
workflow-evidence practices were derived from the reference project's documented
corpus. The GitHub source-of-truth split and the reduced handoff
responsibilities were derived from one documentation-and-GitHub migration and
repeated successfully on a second.

Update this skill when:

- A new memory-architecture pattern emerges and holds up on at least one project.
- The granularity thresholds prove wrong in practice.
- The FAQ second-time rule or the pending-lessons pattern is refined by evidence
  from a new project.
- A new-project bootstrap tests the GitHub authority split without a migration
  preceding it.
- Repeated use shows conditional phase summaries either lose necessary evidence
  or successfully remove duplication.
- GitHub changes Issue, milestone, PR, or ruleset behavior in a way that alters
  the contract.
