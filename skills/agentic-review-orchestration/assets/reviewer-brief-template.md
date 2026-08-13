# Generic reviewer brief template

The bones below stayed constant across every review on the source project. Copy them verbatim; fill only the `<placeholders>`.

```markdown
# Cold review brief: <Issue/PR — role>

You are independently reviewing an integrated implementation. You start cold.
Do not seek or read implementation conversation, implementer reports, prior
review findings, provisional ledgers, handoffs, task files, migration records,
or PR discussion.

## Frozen review target
- Project root: <absolute path>
- Base commit: <identifier>
- Head commit: <identifier>
- Owning Issue: <number, title, URL>
- Draft PR: <number/URL; use only to identify the target, not its discussion>
- Governing spec/ADR: <paths and sections>

Verify the changed-file manifest yourself against the base/head diff before
reviewing.

## Role
<Full skeptical-senior persona or focused specialist/lens text.>

## Acceptance criteria
<Exact Issue criteria relevant to this target.>

## Files and surfaces to inspect
<Changed files plus the smallest necessary surrounding code/tests/docs.>

## Sources you must not read
- <handoff/task/pending-lessons paths>
- <prior audit, research, migration, or phase-evidence paths>
- <provisional ledger path>
- <implementation reports or packet paths>
- <other reviewer reports>

## Ratified exclusions and non-goals
<List settled out-of-scope decisions with brief rationale. Do not include
suspected defects, expected findings, or hints about what another reviewer saw.>

## Verification boundary
- Repository access: read-only
- Disposable state: <paths/fixtures/database and cleanup rules>
- Commands allowed: <exact commands>
- External network/writes: <none unless explicitly granted>
- Preserve: <user-owned work, live data, secrets, internal files>

## Severity
- CRITICAL: security/privacy failure, data loss/corruption, unusable primary
  workflow, or direct violation of a central contract.
- HIGH: likely user-visible incorrectness, major integrity failure, or broken
  supported workflow.
- MEDIUM: real bounded correctness, compatibility, documentation, or
  maintainability problem with concrete impact.
- LOW: non-blocking issue with demonstrated value; omit style-only preferences.

## Required output
Return a punch list grouped by severity. For each finding include:

1. Short title.
2. Severity and concrete impact.
3. Contract or acceptance criterion violated.
4. File:line evidence.
5. Reproduction or minimal failing-test idea.
6. Uncertainty or external fact requiring verification.

Do not edit files, update GitHub, propose unrelated cleanup, or provide a long
implementation plan.

Hard limit: 500 words. List the most severe findings first. If necessary, end
with `(N additional LOW findings omitted)`.
```

For a friction-style lens, retain the same evidence requirements but organize
each finding as **What I tried / What happened / Contract or expectation /
Evidence / Minimal reproduction**.
