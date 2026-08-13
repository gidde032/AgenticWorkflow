# GitHub Source-of-Truth Contract

Read this reference when creating, moving, deferring, completing, or reporting
planned work in a GitHub-hosted project.

## One fact, one authority

The artifact-to-authority map lives in `references/what-goes-where.md`. Read it
first; this file covers the contracts that map implies.

When the same status appears in more than one artifact:

1. Identify the authority from that table.
2. Update the authority first.
3. Replace secondary copies with a link and only the context needed by that
   document's audience.
4. Search for contradictory stale copies before declaring reconciliation
   complete.

## Issue contract

Create an Issue for an actionable deliverable, defect, investigation, deferred
review finding, or unresolved decision that must survive the current session.

Each Issue should contain:

- the problem or desired outcome;
- relevant context and links to the spec or ADR;
- observable acceptance criteria;
- dependencies or blockers;
- verification expectations;
- explicit non-goals when scope could expand; and
- milestone and labels when applicable.

Do not create separate Issues for implementation, review, documentation
reconciliation, and summary of the same deliverable. Keep those as a checklist
inside the owning Issue or PR.

Do not close an Issue merely because work started, a branch exists, or part of
the acceptance criteria landed.

## Milestone contract

A milestone represents a delivery horizon the maintainer currently intends to
complete. It is not a parking lot for every possible future idea.

- Assign Issues only after their inclusion in the horizon is ratified.
- Move an Issue when scope changes; do not duplicate it.
- Record meaningful deferral rationale in the Issue.
- Close the milestone only when its included Issues have terminal dispositions.
- Keep uncommitted ideas as labeled Issues without a committed milestone, or
  place them in an explicitly named exploratory horizon.

## Pull-request lifecycle

1. Select a ready Issue and create a focused branch.
2. Implement against the Issue acceptance criteria.
3. After the first coherent commit passes the local gates, push and open a draft
   PR when external-write authority has been granted.
4. Link the Issue, spec, and ADR as applicable.
5. Keep the PR current with verification and documentation accounting.
6. Run independent review before merge readiness.
7. Resolve accepted findings or create linked Issues for explicitly deferred
   work.
8. Mark ready only when the intended review and gates are complete.
9. Merge only within the granted authority.
10. Use `Closes #N` only when merge completes the entire Issue. Otherwise use a
    non-closing reference and update the Issue after merge.

The PR is the durable record of what changed and how it was verified. Do not
copy its full history into the handoff or a phase summary.

## Handoff synchronization

While work is active, `handoff.md` records:

- milestone and Issue;
- branch and PR;
- verified current state;
- active blockers;
- exact next action; and
- sanity-check commands.

After merge, replace the active entry with the next selected Issue or an
explicit waiting state. Keep at most a short link to the last completed
delivery.

## Conditional planning and release documents

Create `CHANGELOG.md` only when the project uses versioned releases or needs a
curated user-facing release history. Update it for user-visible shipped changes,
not every internal commit.

Create `ROADMAP.md` only when multiple future horizons benefit from a stable,
high-level explanation. Every actionable roadmap entry links to an Issue.
Status, assignee, acceptance criteria, and detailed task breakdown stay in the
Issue.

Keep optional `TASKS.md` gitignored and limited to the current session. Delete
or reset completed checklist items rather than preserving it as history.

## Review findings and deferred work

Every accepted review finding receives one terminal disposition:

- repaired in the current PR with verification;
- deferred to a linked Issue with rationale;
- rejected with evidence;
- duplicate of an existing Issue; or
- outside the project contract.

"Remember for later" is not a disposition.

## Public-safety boundary

Before writing an Issue or PR body, remove private paths, raw continuity notes,
credentials, personal data, unpublished profiles, and internal audit ledgers.
Private repositories may later become public, so write externally visible
GitHub artifacts to a public-safe standard unless the project profile says
otherwise.

## External-action boundary

Creating or changing repository visibility, licenses, Issues, milestones,
branches, PRs, rulesets, merges, tags, releases, deployment, or deletion
requires either explicit authorization for the action or a previously ratified
project profile that clearly grants it.

Routine writes within an approved boundary may continue without repeated
checkpoints. Stop when the requested action exceeds that boundary or evidence
contradicts the approved profile.

## Completion check

Before closing a slice or phase, verify:

- the Issue reflects current scope and disposition;
- milestone membership is correct;
- the PR links the Issue and records verification;
- accepted deferred findings have Issues;
- documentation accounting is present;
- the handoff names the active or next delivery state;
- conditional changelog or roadmap updates are complete; and
- no local-only planning item remains without a terminal disposition.
