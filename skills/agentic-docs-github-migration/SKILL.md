---
name: agentic-docs-github-migration
description: >-
  Explicitly invoked migration workflow for an existing solo-maintained
  repository whose documentation, roadmap candidates, shipped history, and
  GitHub governance need consolidation. Use only when the user invokes
  `$agentic-docs-github-migration profile`, invokes
  `$agentic-docs-github-migration execute` with an absolute profile path, or
  explicitly requests this named repository-wide migration. Do not trigger for
  ordinary documentation edits, issue creation, CI changes, feature work,
  project planning, new-project bootstrap, or mid-project maintenance.
---

# Agentic Documentation and GitHub Migration

Migrate one established solo-maintained repository from scattered planning and
documentation into verified documentation authorities plus GitHub
Issues/PRs/milestones.

This is a finite-use workflow. A repository is migrated once; afterwards it is
governed by the ordinary phase and review skills. That shape is why the skill
is explicitly invoked rather than implicitly triggered — there is no such thing
as routine migration work, so an implicit trigger could only ever be a
false positive.

Worked examples and provenance: `examples.md`.

## Activation guard

Require one of the two exact modes:

```text
$agentic-docs-github-migration profile
$agentic-docs-github-migration execute /absolute/path/project-profile.yaml
```

If the request is not explicit or the target is a new project, stop this
workflow. Route new-project setup to `agentic-project-bootstrap`.

### Solo-maintainer constraint

Operate only on a solo-maintained repository. If the repository has multiple
active maintainers, team-owned protections, or organizational compliance
requirements, report that this workflow does not cover that case and do not
extrapolate. The constraint exists because every checkpoint in this skill
assumes a single ratifying human; with several maintainers, "the human
approved the profile" stops being a well-defined claim.

This constraint is expressed in two places that must change together: the prose
above, and the `project.maintainer_model` check in `scripts/validate_profile.py`.
Relaxing one without the other produces a skill whose documentation and whose
gate disagree — exactly the drift this plugin exists to prevent.

## Non-negotiable invariants

1. Read repository reality before trusting narrative or session memory.
2. Preserve unrelated work and never rewrite unpublished history silently.
3. Back up current documentation before target-repository edits.
4. Inventory every planning/audit finding before creating any issue or editing
   its destination document.
5. Give every finding exactly one evidence-backed disposition.
6. Validate the complete disposition ledger, and verify its source fingerprints
   against disk, before migration writes and again before the final draft PR.
7. Keep profile and full ledger local-only. Put only a concise public-safe
   disposition summary in the PR.
8. Leave merges, releases, visibility changes, branch deletion, gate
   weakening, destructive cleanup, and product-scope changes to the human.
9. Configure unsupported GitHub protections as future-ready only when safe;
   report actual enforcement status without claiming they are active.
10. Stop on contradiction, sensitive-publication risk, missing authority, or a
    materially different repository condition.

## Reuse sibling disciplines

Compose rather than duplicate:

- Use `agentic-project-bootstrap` for the existing-project reality-audit shape.
- Use `agentic-project-memory` to separate operating rules, current state,
  provisional lessons, practices, and public documentation.
- Use `agentic-collaboration-cadence` for checkpoints and exception stops.
- Use `agentic-verification-discipline` for measurable gates and CI.
- Use `agentic-workflow-evolution` to record observed friction and named
  failure modes from a completed migration.
- Use the available GitHub connector or authenticated GitHub CLI for repository
  state. Never infer remote configuration from local files.

## Bundled resources

- Copy `assets/project-profile.template.yaml` to a local working directory when
  starting `profile` mode.
- Copy `assets/disposition-ledger.template.yaml` beside the profile.
- Run `scripts/validate_profile.py` before presenting a profile for ratification
  and again before `execute`.
- Run `scripts/validate_disposition.py --allow-awaiting-decision` while building
  the ledger.
- Run `scripts/validate_disposition.py --pre-write` after decisions are
  resolved and before migration writes. Proposed issues require titles here.
- Run `scripts/validate_disposition.py` after issue creation and before the
  final PR. Proposed issues require real issue numbers or URLs here.
- Run `scripts/verify_fingerprints.py` alongside each strict ledger validation.
  Use `--print-actual` to fill fingerprints while building the ledger.
- Run `scripts/run_fixtures.sh` after changing any validator, template, or
  ledger field. It asserts an exit code per case, so a gate that silently stops
  enforcing is caught as loudly as one that starts over-rejecting.

The validators require Python 3.10+ and PyYAML. If `python3` lacks PyYAML, use a
known interpreter that has it or report the missing dependency. Do not install
packages without authority.

### Why fingerprints are recomputed, not trusted

The ledger's `fingerprint` and `scan_complete` fields are the mechanism that
distinguishes a source that was genuinely re-read from one an agent merely
remembered reading. Left unverified they are self-attestation, and an agent
that skipped a source can write a plausible hash and pass every other gate.
`verify_fingerprints.py` recomputes the digest from disk, which is what turns
invariant 1 into something enforceable rather than promised.

## Mode: `profile`

Keep the target repository read-only. The only writes allowed in this mode are
the profile and ledger in the user-approved local working directory.

### 1. Resolve identity and safety

- Resolve the absolute repository path, Git root, remote, default branch,
  visibility, license, owner, and current branch.
- Inspect repository instructions before broad exploration.
- Record dirty files, local/remote divergence, unpublished commits, ignored
  local documents, secrets/data boundaries, generated artifacts, and
  destructive or external-write risks.
- Verify GitHub plan/capability limitations live.
- Set `public_readiness_audit.enabled` to `false` unless the user explicitly
  enables it.

### 2. Establish documentation authority

Read the operating-rules entrypoint, handoff/current-state document, task list,
specification, roadmap/history documents, practices index if earned, CI/gate
configuration, and relevant source. Do not assume filenames from another
project.

Classify documents as:

- public durable authority;
- local internal continuity;
- immutable historical evidence;
- stale or duplicative candidate;
- generated or sensitive;
- absent but proposed.

Do not create an empty practices catalogue. Preserve project-specific
architecture when it already expresses the intended separation.

### 3. Build the complete disposition ledger

Enumerate every distinct completed item, active item, roadmap candidate,
unresolved decision, known defect, accepted/rejected audit finding, and
documentation mismatch found in all declared sources.

For every source:

- record an absolute or repository-relative path;
- record the SHA-256 digest, obtained from
  `scripts/verify_fingerprints.py --print-actual` rather than written by hand;
- attest that the declared scope was scanned completely;
- link each discovered item to one or more finding IDs.

Give each finding one status:

- `completed`;
- `ported_to_issue`;
- `retained_in_authoritative_doc`;
- `rejected_with_rationale`;
- `awaiting_human_decision`.

Do not hide ambiguity inside `completed`. Evidence requirements are enforced by
the bundled validator.

### 4. Fill and validate the project profile

Derive commands, gates, labels, milestone strategy, visibility/license
decisions, documentation destinations, GitHub capabilities, safety boundaries,
artifact retention, automation authority, and checkpoint policy from current
reality.

Set the profile to `draft`, validate with `--allow-unratified`, and present only
the unresolved human decisions. Recommend defaults but do not choose licensing,
visibility, history rewriting, gate weakening, destructive cleanup, or product
scope.

### 5. Profile checkpoint

Stop for the human to ratify the profile. On approval:

- set `ratification.status: approved`;
- record approver and date;
- resolve every decision placeholder;
- validate without `--allow-unratified`;
- report the exact profile and ledger paths.

Do not enter execute mode implicitly.

## Mode: `execute`

Require an absolute profile path. Treat the profile as authority for granted
actions, not as evidence that repository state is unchanged.

### 1. Revalidate before mutation

- Validate the approved profile.
- Re-read repository instructions.
- Verify project identity, Git root, remote, visibility, current branch,
  cleanliness/divergence, and profile snapshot.
- Refresh GitHub state.
- Refresh source fingerprints with `verify_fingerprints.py` and re-validate the
  disposition ledger.
- Stop if state drift changes a consequential decision.

### 2. Take the documentation backup

Before target-repository edits, copy every current project document declared by
the profile into a timestamped directory outside the target repository. Preserve
relative paths and record a manifest with hashes. Report the exact absolute
backup path.

Never delete the backup during the migration.

### 3. Resolve exceptional prerequisites

If unpublished product commits, divergent history, missing authentication, an
unsupported ruleset, or a sensitive-publication decision requires separate
human action, prepare the narrowest prerequisite and stop at that checkpoint.

Do not bundle product changes into the documentation migration. Resume only
after the prerequisite is resolved and state is reverified.

### 4. Freeze the pre-write ledger

Complete all human decisions. Run the disposition validator with `--pre-write`
and `verify_fingerprints.py` against the same ledger. Do not create GitHub
issues, labels, milestones, documentation changes, templates, or CI until both
pass.

### 5. Execute the approved migration

Within `automation_authority.allowed`:

- create or update labels and the milestone;
- create issues only for ledger entries marked `ported_to_issue`;
- include source provenance and acceptance criteria in issue bodies;
- update public documentation without copying local narrative wholesale;
- move shipped history to the approved changelog/history destination;
- make roadmap documents link to GitHub instead of duplicating live issue
  state;
- create the approved license, templates, and CI;
- configure future-ready GitHub settings when safe;
- retain a clear manual-configuration list for unenforceable settings.

Never close an issue merely because a document mentioned the work. A completed
finding must have implementation or delivery evidence.

### 6. Verify coverage and behavior

- Re-scan every declared source and compare it with the ledger.
- Confirm each `ported_to_issue` entry resolves to the created issue.
- Confirm every retained entry names its authoritative destination.
- Confirm every completed/rejected entry carries evidence or rationale.
- Run documentation checks, project gates, build, and CI-equivalent commands
  required by the profile.
- Check for secrets, sensitive local material, unintended product changes,
  generated drift, and unrelated modifications.
- Run both validators strictly, plus `verify_fingerprints.py`.

Any unledgered item, fingerprint mismatch, or validator failure blocks the PR.

### 7. Open the draft PR and stop

Commit intentionally, push the migration branch, and open a draft PR when
authorized. Include:

- scope and repository snapshot;
- concise public-safe disposition counts and exceptions;
- created issue/milestone links;
- verification evidence;
- enforcement status and manual GitHub tasks;
- public-readiness result only if enabled;
- explicit non-goals.

Do not attach the full local ledger. Stop for final human review. Never merge,
release, change visibility, or delete branches autonomously.

## Checkpoint budget

Expect only:

1. profile ratification;
2. an exceptional prerequisite checkpoint when repository state requires one;
3. final draft-PR review.

Do not manufacture checkpoints for reversible work already authorized by the
profile. Do stop for new licensing/visibility choices, history rewriting,
destructive cleanup, sensitive publication, gate weakening, product-scope
changes, or a profile contradiction.

## After a completed migration

Record observed friction, deviations, and named failure modes through
`agentic-workflow-evolution` rather than in this file. A migration is a rich
source of workflow evidence, and that evidence belongs in the evolution ledger
where it can be weighed against other projects — not appended here, where it
would slowly turn a runbook into a changelog.

## Future-project boundary

Do not expand this skill into new-project setup. Forward-looking defaults —
Issues/PRs as live planning truth, documentation authority, license/visibility
decisions, CI/rulesets, and public/private boundaries — belong in
`agentic-project-bootstrap`. Legacy backup, drift reconciliation, history
mining, and disposition migration stay here.
