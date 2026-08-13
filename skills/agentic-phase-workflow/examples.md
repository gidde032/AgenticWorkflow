# Phase workflow — worked examples and provenance

Evidence behind the loop in `SKILL.md`. Read a section when you want the case
behind a rule, or when judging whether a shape fits your project.

The reference project is a Python CLI built across six feature phases and
several hardening releases. The GitHub authority split comes from two separate
documentation-and-GitHub migrations.

## Contents

1. The workflow is the product
2. What the spec bought
3. Hardening is a different shape
4. Bundled phases, two payoffs
5. The living spec
6. Workflow improvements before features
7. Provenance and maintenance

## 1. The workflow is the product

The governing claim, stated as the first thesis of the reference project's
retrospective:

> "The workflow is the product, as much as the code. Six phases of clean code
> came out of a repeatable loop — implement, review independently, fix with
> regression tests, summarize — not out of any single clever prompt."

The loop in `SKILL.md` is the end state of ten documented revisions — two
reviewers becoming three, parallel becoming serial, and so on. A new project can
start there rather than re-deriving it. How each revision emerged from evidence
is the domain of `agentic-workflow-evolution`; this skill hands over the result.

## 2. What the spec bought

The spec took, in the maintainer's words, "roughly 30 minutes / one round-trip
to produce... Practically negligible relative to the savings downstream."

Its observed value across the project:

> "Reviewers cited spec sections directly when justifying findings ('Phase 1
> spec says runs pending migrations on startup'). When in doubt about whether to
> fix something now vs. later, the spec's phase boundaries made the call."

Both halves matter. The spec was not merely documentation — it was the artifact
that made "in scope vs. later" a lookup instead of an argument, and gave
reviewers a contract to cite instead of an opinion to assert.

## 3. Hardening is a different shape

The distinction was named after a hardening release was run as though it were a
feature phase:

> "End-of-version hardening deserves its own structure. [The hardening release]
> wasn't a phase — it was a follow-up pass after [the release] shipped, with a
> different shape (dual-lens audit → plan with severity ranking → user-approved
> slice → execute → user-approved next slice). Phase-shaped work is for new
> features; pass-shaped work is for hardening. Don't conflate them."

The failure mode conflation produces: hardening work gets an Issue with
acceptance criteria written before the audit has found anything, so the audit's
actual findings either don't fit the Issue or get quietly dropped.

## 4. Bundled phases, two payoffs

One release bundled four features — undelete, stats, material merge, and a diff
redesign — into a single implementation phase and a single three-reviewer pass,
"saving three review cycles."

The second payoff was not anticipated:

> "The bundled review also caught cross-feature interactions (stats counting
> materials from deleted patterns after a merge) that single-feature reviews
> would have missed, because each reviewer held the full four-feature surface in
> context simultaneously."

That interaction — stats counting materials from patterns deleted by a different
feature in the same bundle — is invisible to a reviewer looking at either
feature alone.

**The precondition is load-bearing**, and it is the same property that produces
the benefit:

> "If they share surfaces, serial phases with per-phase reviews are safer — the
> cross-feature interaction risk is exactly what the bundled review is designed
> to exploit, not suppress."

When in doubt, go serial.

## 5. The living spec

> "A living spec is a feature, not a flaw. [A raised cold-start budget] is a
> concrete example... the spec grew toward reality with explicit rationale
> recorded inline ('the earlier target proved tight against real CI hardware and
> made the gate flaky') rather than fossilizing... and silently disagreeing with
> the code. Every audit cycle that produces DOCUMENT-class findings is also a
> spec backport cycle. A spec edited at end-of-version is a healthier artifact
> than a spec that's append-only."

The distinction that keeps this honest: the budget was raised *with the
rationale recorded next to the number*, through a human decision. That is a
living spec. Silently moving a target so a red gate turns green is not, and the
two look identical in a diff unless the rationale is present.

## 6. Workflow improvements before features

> "Workflow improvements before features is a legitimate release shape. [The
> version] began with a workflow-improvement batch on the rationale that tokens
> spent upfront on the workflow save more tokens downstream than tokens spent on
> features. The bet pays off after roughly 3–4 future doc updates and one phase's
> reviewer pass — about half a release's worth of work."

The payback figure is a recorded estimate from one project, not a measured
universal. It is precise enough to plan around and not precise enough to quote
as a benchmark.

## 7. Provenance and maintenance

The core implementation-review-repair loop and its feature, bundled, hardening,
spec-drift, and workflow-improvement shapes were derived from the reference
project's documented corpus.

The GitHub authority split was derived from one documentation-and-GitHub
migration and repeated on a second. The Issue-backed per-phase lifecycle
integrates that structure with the reference project's loop.

Update this skill when:

- A new *shape* of work appears, beyond feature phase, hardening pass, and
  workflow-improvement release.
- The per-phase invariants change.
- Repeated use on a project outside this pattern surfaces a step that does not
  generalize.
- A migrated project completes a full Issue → draft PR → independent review →
  merge → Issue/milestone synchronization phase.
- The distinction between product-slice ratification and implementation
  authorization proves too strict, or fails to prevent an unauthorized start.
- Conditional phase summaries either lose necessary rationale or consistently
  remove duplication.
- Bundled multi-Issue PRs prove too large, or preserve review quality at scale.

Do not fold review-briefing, verification, memory, cost, or cadence mechanics
into this skill — they belong to sibling skills. Keep this one focused on the
sequence and the choice of shape.
