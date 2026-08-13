# Workflow evolution — worked examples and provenance

Evidence behind the rules in `SKILL.md`. This skill has fewer worked examples
than its siblings by design: it governs how evidence is judged, so its own
claims are deliberately thin and its thresholds are argued rather than measured.

## Contents

1. Lessons that compounded backward
2. A contained skill that completed the path
3. Provenance and maintenance

## 1. Lessons that compounded backward

Three lessons from the reference project each became a structural protection
that repaired existing work, not just future work:

- **An environment-dependent import-classification failure became explicit tool
  configuration.** A linter's first-party/third-party heuristic answered
  differently in CI than locally. Declaring the classification explicitly fixed
  every file at once, including files written before anyone noticed the problem.
- **Reviewer prompt sameness became differentiated reviewer roles.** Two
  reviewer briefs had drifted close enough to produce overlapping focus. Naming
  distinct personas restored coverage across all subsequent reviews.
- **A test-fragility lesson became a shared fixture.** A lesson about tests
  breaking under narrow terminal widths, written mid-project, later became a
  `conftest.py` fixture — which retroactively protected every existing test,
  including two that had been silently fragile for months.

The pattern worth generalizing: a lesson recorded with its *mechanism* and its
*artifact location* can later be discharged as a structural fix. A lesson
recorded only as advice cannot. This is why the capture format in §11 asks for
both.

## 2. A contained skill that completed the path

`agentic-docs-github-migration` is the worked example of the containment path in
§10. It was held as an explicitly-invoked, contained skill while its evidence
accumulated across two real migrations, then promoted by an explicit human
decision.

One detail is easy to misread: it remains explicit-invocation-only *after*
promotion. Containment was never the reason for that restriction — its
finite-use shape was. A skill that performs a one-time repository-wide operation
should not fire on inference, regardless of how well validated it is.

## 3. Provenance and maintenance

The evidence-first foundation comes from the reference project's documented
workflow: environment-dependent CI behavior, stale reviewer assertions, reviewer
prompt sameness, numbered revisions, and backward-compounding test lessons.

Later evidence from two documentation-and-GitHub migrations refined the adoption
model:

- Documentation and GitHub migrations can run as a repeatable, evidence-backed
  workflow with exception-only pauses.
- Ratification and development readiness do not imply implementation authority.
- Cold review reinforced independent evidence, parent validation, and one
  consolidated repair-approval boundary.

Update this skill when a new project changes the evidence threshold, a contained
skill completes or fails its promotion test, or a plugin release reveals a
source, validation, versioning, or rollback failure.

Preserve the epistemic labels — observation, candidate, provisional, adopted,
retired. They are this skill's core vocabulary, not hedging.
