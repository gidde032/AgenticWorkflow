# Project bootstrap — worked examples and provenance

Evidence behind the runbook in `SKILL.md`. Read a section when you want to know
how far a default generalizes, or why a step exists at all.

The reference project is a Python CLI built across six feature phases and
several hardening releases, maintained by one person working with agents. The
GitHub planning-and-delivery layer comes from two separate
documentation-and-GitHub migrations on other repositories.

## Contents

1. Why the workflow is the product
2. What a new project inherits
3. The spec is cheap
4. Gate numbers must be measured, not copied
5. The standing skeptic
6. The canonical checkpoint failure
7. Evidence boundaries for the right-sizing table
8. Provenance and maintenance

## 1. Why the workflow is the product

From the reference project's retrospective:

> "The workflow is the product, as much as the code. Six phases of clean code
> came out of a repeatable loop — implement, review independently, fix with
> regression tests, summarize — not out of any single clever prompt."
> — the maintainer

The claim being made is narrow and worth stating precisely: the output quality
came from the loop being repeatable, not from prompt craft. That is why this
skill is a runbook rather than a collection of prompts, and why it hands off to
sibling skills instead of restating them.

## 2. What a new project inherits

The reference project reached its final shape through ten documented workflow
revisions — each one a change made because something had gone wrong or proved
expensive. A project bootstrapped with this runbook starts at that end state
rather than deriving it.

That is the entire value proposition, and also its limit: you inherit a matured
loop calibrated on one project shape. Where a default does not fit your project,
the derivation that produced it is not available to you, so prefer measuring
your own reality over trusting the inherited number.

## 3. The spec is cheap

The reference project's spec took, in the maintainer's words, "roughly 30
minutes / one round-trip to produce... Practically negligible relative to the
savings downstream."

It became the canonical scope reference that reviewers cited for the rest of the
project's life. This is a single-project observation about one spec of moderate
size — not a general estimate — but the ratio is lopsided enough that writing
the spec first is rarely the wrong call.

## 4. Gate numbers must be measured, not copied

The first dry run of this skill on a fresh project copied a prior project's
cold-start budget as a guess, then had to flag the value `ASSUMED` because
nothing had been measured to support it.

An unmeasured gate is worse than no gate: it either passes trivially, teaching
the team the gate is meaningless, or fails on day one and poisons trust in every
other gate. Measure the walking skeleton, floor just below the measurement, and
ratchet later.

## 5. The standing skeptic

The skeptical-senior-engineer persona caught the highest-severity findings in
multiple phases on the reference project. That is why reviewer count is a
default with one non-negotiable slot rather than a free choice.

Full persona and lens mechanics live in `agentic-review-orchestration`; this
skill only instantiates the cadence on day one.

## 6. The canonical checkpoint failure

The failure mode Steps 0 and 1 exist to prevent: an autonomous agent implements
a taste-call the maintainer would have rejected, then pins it with a regression
test that makes it expensive to undo.

The regression test is what makes this costly. A bare wrong decision is cheap to
reverse; a wrong decision with a passing test asserting it is correct requires
unpicking the test, the fix, and the reviewer's approval of both. Surface the
decision, don't pin it.

## 7. Evidence boundaries for the right-sizing table

The three columns in the right-sizing table do not carry equal evidence.

**Solo, agent-heavy (the middle column)** is the calibrated one. Memory files,
gates, reviewer count, and the evolution ledger were all exercised across the
reference project's full lifetime. The GitHub planning-and-delivery row comes
from the two migrations rather than the reference project.

**Tiny project (down-scale)** is a reasoned reduction. Nothing about it was
separately validated, but it only ever removes structure, so the failure mode is
mild — you notice you needed something and add it.

**Team (up-scale)** is extrapolation throughout. The reference project never ran
multi-contributor, and no migration involved more than one maintainer.
Memory-file ownership conventions are the weakest cell in the table: who edits
which file, and how conflicts resolve, was never tested with more than one
person. Treat the whole column as a starting hypothesis and expect to revise it.

Implementation delegation in the middle column rests on lighter evidence than
its neighbors — bounded work packets with exclusive ownership were exercised,
but across fewer complete phases than the gates or reviewer rows.

## 8. Provenance and maintenance

The core development loop was derived from the reference project's documented
corpus. The GitHub-backed planning-and-delivery extension was derived from one
documentation-and-GitHub migration and repeated successfully on a second. Those
migrations support the solo-maintainer workflow and its reduced-checkpoint
execution model; they do not validate the team-scale extrapolations.

Update this skill when:

- The bootstrap sequence gains or loses a step.
- A project outside this pattern runs the runbook and surfaces a step that does
  not generalize.
- Team use validates or falsifies the up-scale column.
- A sibling skill is renamed and cross-references need re-pointing.
- GitHub changes observable ruleset or required-check behavior.
