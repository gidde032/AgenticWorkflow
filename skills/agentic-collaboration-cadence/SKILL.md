---
name: agentic-collaboration-cadence
description: >
  Establish and operate the human-in-the-loop authority model for agentic
  project work: distinguish product ratification, implementation, review
  repair, and merge or release authority; define an authorization envelope;
  continue pre-authorized repository and GitHub work with exception-only
  pauses; consolidate useful checkpoints; surface judgment calls, cost
  tripwires, and honest evidence. Use when planning substantial work,
  calibrating agent autonomy, deciding whether an Issue, PR, merge, deployment,
  publication, or repository-visibility action needs approval, structuring a
  review-and-repair cycle, or correcting a workflow that asks for approval too
  often or assumes too much authority. Triggers: "human in the loop",
  "authorization boundary", "implementation approval", "ratified but not
  approved", "exception-only pause", "work in the background", "checkpoint",
  "autonomous execution", "impact-ranked plan", "pick the slice", "judgment
  call", "how often should the agent check in".
---

# Agentic Collaboration Cadence

Keep the human involved where judgment or authority matters without converting
ordinary execution into a chain of approval requests. Establish the allowed
work once, continue through mechanical steps inside that boundary, communicate
progress without stopping, and pause only when a real decision or new authority
is required.

Use this skill to govern the agent's behavior toward the human. Route the
mechanics of implementation, review, verification, memory, and GitHub operations
to their dedicated skills.

Worked examples and provenance: `examples.md`.

## 1. Governing model

Avoid both failure modes:

- **Unbounded autonomy:** the agent silently decides product scope, taste,
  acceptable risk, or external actions.
- **Per-action approval:** the agent repeatedly asks permission for mechanical
  steps already included in an approved workflow.

Use an **authorization envelope** instead. The human approves a coherent scope,
allowed actions, withheld actions, verification standard, checkpoints, and
exception conditions. The agent then completes the authorized sequence without
inventing more gates.

A slice remains a coherent, testable, committable unit. It is primarily an
execution and commit boundary, not automatically a human checkpoint.

## 2. Keep four authority boundaries separate

Do not infer one kind of approval from another.

| Boundary | What it establishes | What it does not establish |
|---|---|---|
| Product or spec ratification | Desired behavior, scope, or acceptance contract is agreed | Permission to change product code |
| Implementation authorization | The agent may implement the agreed scope | Permission to accept later review findings or merge |
| Repair authorization | The agent may write regressions and fixes for an approved finding batch | Permission to merge, release, or expand the product contract |
| Integration or release authorization | The agent may perform the named merge, deploy, publish, release, or visibility action | General authority for unrelated external actions |

Apply these consequences literally:

- A ratified Issue is not implementation authorization.
- An approved roadmap or milestone is not implementation authorization.
- A completed documentation migration or "development ready" state is not
  implementation authorization.
- Opening a draft PR does not authorize merge.
- Approval to make a repository public eventually does not authorize changing
  its visibility now.
- Approval of review findings does not authorize unlisted product enhancements.

Each of those consequences was a real confusion before it was a rule
(`examples.md` §1).

When the user grants several boundaries together, record that combined grant
instead of asking for them again.

## 3. Establish the authorization envelope

Before substantial work, identify the envelope from the user's instruction,
repository rules, project profile, active Issue, and prior explicit approvals.
Do not ask the user to restate facts that can be discovered safely.

Record:

```yaml
scope:
  outcome: <approved outcome>
  governing_contracts:
    - <Issue, spec, ADR, or approved plan>

authorized:
  - <file or product changes>
  - <verification>
  - <branch, commit, push, Issue, or draft-PR actions>

withheld:
  - <merge, deploy, publish, visibility, destructive action, or other boundary>

required_checkpoints:
  - <specific decision point>

verification:
  - <gates and acceptance evidence>

pause_on_exception:
  - <condition that invalidates the envelope>
```

This need not always become a file. For short work, a concise checkpoint message
is enough. For a repeatable migration, phase, or long-running effort, place the
durable form in the project profile, Issue, PR, ADR, or other governing
artifact.

### Common pre-authorized actions

When explicitly included in the envelope, continue through these without
repeated approval:

- Read-only audit and source-of-truth reconciliation.
- Scoped edits and mechanical migrations.
- Local verification and approved disposable probes.
- Creating a branch and coherent commits.
- Pushing the named branch.
- Creating or updating approved Issues, labels, and milestones.
- Opening or updating a draft PR.
- Monitoring CI and repairing in-scope mechanical failures.
- Updating the handoff with immediate state.

External mutation is not inherently forbidden; it requires authority. If the
user approved Issue creation and a draft PR as part of a migration, perform
them. Do not transform that approval into merge, release, or visibility
authority.

## 4. Decide whether to continue or pause

### Continue and report

Continue when all of the following are true:

1. The action is inside the authorization envelope.
2. The governing contract is still coherent with current evidence.
3. The action does not cross a withheld authority boundary.
4. Unrelated work and live data can be preserved.
5. Cost and risk remain within any declared tripwire.

Examples:

- A slice reaches a clean commit boundary.
- Tests pass or an in-scope mechanical failure needs repair.
- An approved branch is ready to push.
- An approved draft PR needs updated evidence.
- Parallel reviewers are still completing an already authorized formal review.

Send concise progress commentary when useful, but do not turn the update into a
request for approval.

### Pause on exception

Pause when:

- Evidence contradicts the ratified contract.
- Two consequential interpretations remain and the repository cannot resolve
  them.
- A user-visible, strategic, policy, or taste decision was not already made.
- The work would materially expand scope.
- Verification reveals a materially different risk or architecture consequence.
- The next action crosses a withheld merge, deploy, publish, release,
  visibility, communication, deletion, or history-rewrite boundary.
- An agreed cost or time tripwire is reached.
- Unrelated user work cannot be safely isolated.
- Required access or authority is missing.

Do not label ordinary difficulty, an expected failing test, or unchanged CI
state as an exception.

### Irreversible and consequential actions

Resolve the exact target first. Require explicit authority for destructive or
difficult-to-recover actions unless the user's request unmistakably names that
exact action and target. Treat public release, deployment, outbound
communication, repository visibility, history rewriting, data deletion, and
merging as separate authority surfaces.

## 5. Distinguish communication from checkpoints

Use three different interaction types.

### Progress update

Work continues. State:

- What is complete.
- What is running or next.
- Any bounded observation the human may want to know.

Do not end with a blocking question.

### Decision checkpoint

Work stops because human judgment or new authority is required. Present:

```markdown
Outcome so far:
Scope affected:
Decision required:
Recommended choice:
Alternatives and consequences:
Dominant cost:
Least-predictable cost:
Verification completed:
What remains blocked pending approval:
```

Adapt the length to the decision. Ask for one concrete choice. Do not present a
status-only checkpoint or a vague "what would you like me to do next?"

### Completion report

The authorized run is complete. Report:

- Outcome and material artifacts.
- Issue and PR state.
- Verification actually performed.
- Claims still unverified or blocked.
- Deviations from the envelope.
- Deferred work and its canonical Issue or destination.
- Whether the next action requires a new authority boundary.

The final report must stand alone; do not rely on earlier commentary.

## 6. Surface judgment calls early

| Category | Default action |
|---|---|
| Product behavior, taste, naming, or user-facing wording | Propose and pause unless ratified |
| Strategic scope or risk acceptance | Present options and pause |
| Contract, rule, or gate change | Name the consequence and pause |
| Merge, release, deployment, publication, or visibility | Require the relevant authority |
| Internal implementation technique with unchanged behavior | Decide inside the envelope and report if material |
| Mechanical application of an agreed convention | Execute |
| Formatting and trivial consistency | Execute without ceremony |

Use the governing artifacts before asking. If the Issue, spec, ADR, or explicit
user instruction already answers the question, apply it.

## 7. Plan and authorize coherent slices

For non-trivial work, present an impact-ranked plan when scope has not already
been ratified:

| Slice | Outcome | Impact | Cost or effort | Verification | Authority needed |
|---|---|---|---|---|---|
| A | <coherent outcome> | High | <estimate> | <evidence> | <boundary> |
| B | <coherent outcome> | Medium | <estimate> | <evidence> | <boundary> |
| C | <optional outcome> | Low | <estimate> | <evidence> | <boundary> |

Make each slice independently understandable and preferably committable. Split
by contract and risk, not a universal time estimate. A five-minute visibility
change may need a checkpoint; a multi-hour mechanical migration may not if its
envelope is clear.

Once the human approves a sequence, execute its authorized slices continuously.
Report at natural seams without stopping unless the envelope names that seam as
a checkpoint.

## 8. Handle cost without manufacturing approvals

Before authorizing expensive work, disclose:

1. **Dominant cost:** the step expected to consume most resources.
2. **Least-predictable cost:** the step most likely to overrun and why.
3. **Tripwire:** the observation that should trigger reassessment.

Treat estimates as planning ranges, not guarantees.

If the expensive step is inside the approved envelope, proceed. Pause only when
the tripwire fires, cost or risk changes materially, or the approved method is
no longer viable. Route detailed token and session economics to
`agentic-session-economics`.

## 9. Use GitHub as the collaboration surface

Assign each artifact one job:

- **Issue:** open scope, acceptance criteria, decisions, and deferrals.
- **Milestone:** grouping and target planning; never authorization by itself.
- **Branch and commits:** isolated implementation history.
- **Draft PR:** implementation discussion, review target, gates, and evolving
  evidence.
- **Ready PR:** implementation and approved repair accounting are complete;
  merge still follows repository authority.
- **Handoff:** immediate local state and the next operational action.
- **Changelog or release notes:** shipped history.

Do not duplicate detailed plans across all surfaces. Link them. Update the
canonical artifact when status changes.

Normal sequence:

```text
Issue or ratified contract
  -> implementation authorization
  -> branch and coherent commits
  -> draft PR and automated gates
  -> independent review
  -> consolidated repair checkpoint
  -> approved regressions and repairs
  -> merge or release authority
```

An authorization envelope may omit or combine stages, but no arrow silently
grants the next authority boundary.

## 10. Consolidate formal-review checkpoints

When formal review is authorized:

- Freeze the review target.
- Run all independent reviewers without pausing between them.
- Do not show one reviewer another review or the provisional ledger.
- Validate findings against code, tests, contracts, and current primary
  evidence.
- Consolidate accepted candidates into one impact-ranked repair proposal.
- Pause once before regressions or fixes unless the repair batch was separately
  pre-authorized.

Do not interrupt the cold-review phase with raw findings or ask the human to
triage unvalidated reports. Route reviewer mechanics to
`agentic-review-orchestration` and fail-before-fix mechanics to
`agentic-verification-discipline`.

## 11. Treat human testing as an independent evidence lane

Invite hands-on testing at meaningful acceptance boundaries, especially for
user experience, discoverability, real-machine integration, and visual feel.
Record exactly what the human observed.

Do not inflate that observation:

- Visual acceptance does not prove console cleanliness.
- A successful click path does not prove keyboard or focus behavior.
- One viewport does not prove responsive containment or absence of overflow.
- Real-machine success does not replace automated regressions.

Hands-on testing need not block unrelated authorized verification. Keep each
evidence lane explicit and reconcile them at acceptance.

## 12. Account honestly

Trust depends on reporting misses and limits without drama:

- Name failed approaches, tooling problems, and recovery cost.
- Flag plan deviations even when the outcome is acceptable.
- Record rejected findings and their evidence-backed rationale.
- Distinguish skipped, blocked, passed, failed, and not applicable.
- Do not call a gate green because a neighboring check passed.
- Never claim an external action completed without confirmed evidence.

When a failure suggests a reusable workflow improvement, log the observation
and route promotion decisions to `agentic-workflow-evolution`. The agent
proposes; the human decides.

## 13. Compact operating checklist

Before work:

- [ ] Read the governing repository and project instructions.
- [ ] Identify the ratified contract and active Issue.
- [ ] Establish the authorization envelope.
- [ ] State dominant cost, uncertainty, and tripwire when material.
- [ ] Pause only if scope or authority is unresolved.

During work:

- [ ] Continue through authorized mechanical steps.
- [ ] Send progress updates without manufacturing checkpoints.
- [ ] Preserve unrelated work and live data.
- [ ] Pause on a genuine exception or withheld boundary.
- [ ] Keep Issue, PR, and handoff state in their assigned roles.

At review and completion:

- [ ] Consolidate independent review before repair approval.
- [ ] Report measured evidence and bounded claims.
- [ ] Record deviations, deferrals, and canonical destinations.
- [ ] State the next authority boundary explicitly.

## When not to use this skill

| Need | Route to |
|---|---|
| Run a feature phase end to end | `agentic-phase-workflow` |
| Spawn and brief independent reviewers | `agentic-review-orchestration` |
| Write regressions and define gates | `agentic-verification-discipline` |
| Orchestrate parent and implementer agents | `agentic-implementation-orchestration` |
| Manage token budgets and session lifecycle | `agentic-session-economics` |
| Maintain handoff, lessons, and source-of-truth files | `agentic-project-memory` |
| Adopt or retire a workflow practice | `agentic-workflow-evolution` |
| Bootstrap the complete workflow | `agentic-project-bootstrap` |

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
