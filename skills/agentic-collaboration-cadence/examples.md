# Collaboration cadence — worked examples and provenance

Evidence behind the authority model in `SKILL.md`. This skill carries fewer
worked examples than its siblings because most of its rules are boundary
definitions rather than empirical claims — but the three authority failures
below are what forced the boundaries apart.

## Contents

1. Three authority confusions, observed
2. Why impact-ranked plans exist
3. Provenance and maintenance

## 1. Three authority confusions, observed

The four-boundary table exists because these three were each conflated in real
work, and each conflation cost something.

**"Development ready" read as implementation authorization.** A product had been
ratified and its documentation migration completed, leaving the project in a
state everyone described as ready for development. An agent treated that state
as permission to change product code. Ratifying *what* should be built and
authorizing *someone to build it now* are separate grants, and the gap between
them is where taste decisions get made silently.

**Review completion read as repair authorization.** Independent reviews finished
and produced accepted findings. Acting on them directly — writing regressions and
fixes — skips the one checkpoint where a human can rank impact and reject a
finding. The fix was consolidating all reviewers into a single repair-approval
checkpoint rather than pausing after each reviewer.

**Approved-eventually read as approved-now.** Approval to make a repository
public *at some point* is not authority to change its visibility today.
Irreversible actions need the exact action and target named.

## 2. Why impact-ranked plans exist

On the reference project, presenting impact-ranked choices prevented autonomous
taste decisions: the human picked the slice, so the agent never had to guess
which of several defensible directions was wanted. Costly reviewer passes
justified the explicit planning overhead — a wasted review cycle costs far more
than the plan that would have avoided it.

Honest deviation accounting improved trust independently of outcome quality.
Reporting a failed approach and its recovery cost made the successful reports
credible.

## 3. Provenance and maintenance

The original cadence was derived from the reference project: impact-ranked
choices prevented autonomous taste decisions, costly reviewer passes justified
explicit planning, and honest deviation accounting improved trust.

The authorization-envelope revision adds evidence from two later project
workflows:

- Two documentation migrations showed that an explicitly approved
  audit-to-draft-PR sequence can proceed with exception-only pauses.
- A UI product's second phase showed that product ratification and
  "development ready" status must not be confused with implementation
  authorization.
- That product's formal review showed that independent reviews should complete
  before one consolidated repair-approval checkpoint.

Treat these as observed workflow evidence, not permission to erase project-level
rules.

Update this skill when another project reveals a distinct authority failure,
exception-only execution exceeds its boundary, or a checkpoint shape proves
consistently wasteful or insufficient. Preserve the distinction between progress
communication and permission.
