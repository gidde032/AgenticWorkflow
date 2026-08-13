---
name: agentic-implementation-orchestration
description: >-
  Orchestrate an approved Issue-backed implementation with a strongest-capability
  parent and bounded implementer agents. Use when decomposing an authorized
  feature or phase; mapping work packets to Issue acceptance criteria; deciding
  what the parent retains versus delegates; assigning exclusive files or modules;
  preserving unrelated work in a shared workspace; integrating changes into
  coherent commits; opening or updating a draft PR after local gates; or
  independently accepting delegated work before cold review. Covers dependency
  graphs, capability routing, ownership, concurrency, compact and full work
  packets, structured returns, escalation, integration, tracking impact, and
  parent-side verification. Do not use to decide product scope, treat Issue
  ratification as implementation authority, run cold review, or perform ordinary
  Issue/PR administration.
---

# Agentic Implementation Orchestration

The operating model is simple:

> The strongest available capability owns interpretation, decomposition, risk,
> integration, and acceptance. Other agents implement bounded work packets.

Delegation does not transfer accountability. An implementer's report is a lead;
the orchestrator verifies the actual workspace before accepting it.

Worked examples and provenance: `examples.md`.

---

## 1. Boundaries with the sibling skills

This skill owns the implementation manager layer:

- dependency-aware decomposition;
- retain-versus-delegate decisions;
- implementation work packets;
- exclusive file or module ownership;
- safe concurrency and integration order;
- structured implementer returns;
- parent-side acceptance of delegated work;
- mapping packets to the owning Issue and acceptance criteria;
- preserving the Issue/branch/PR relationship during implementation;
- parent-owned coherent commits and draft-PR updates; and
- preventing implementers from making unauthorized external GitHub changes.

Route adjacent mechanics to their owners:

| Need | Owning skill |
|---|---|
| Cheaper-model failure modes, brief hardening, escalation triggers | `agentic-driving-weaker-models` |
| Capability tiers, cost posture, session lifecycle | `agentic-session-economics` |
| Cold independent review after implementation is integrated | `agentic-review-orchestration` |
| Tests, quality gates, regression contracts, and repository-owned Actions evidence | `agentic-verification-discipline` |
| Human approval boundaries and slice size | `agentic-collaboration-cadence` |
| Issue-backed phase sequence, draft-PR timing, implementation approval, and feature-vs-hardening shape | `agentic-phase-workflow` |
| Durable planning, Issue/PR authority, handoff state, and documentation accounting | `agentic-project-memory` |

Implementation agents are **not contextless**. Give them the exact contract and
local context needed to implement their packet. Reviewers remain contextless:
they see the integrated files, specification, and review brief, but never the
implementation conversation or implementer reports.

An Issue defines durable desired work but does not necessarily authorize coding.
Before decomposition, confirm that the project's implementation-approval
checkpoint has been cleared or that its operating rules explicitly pre-authorize
the slice.

---

## 2. The orchestration loop

### Step 1 — Preflight the real workspace and delivery state

Before decomposing, verify rather than assume:

- project root, repository status, remotes, and current branch;
- unpublished commits and unrelated tracked or untracked changes;
- owning Issue, milestone, acceptance criteria, and current disposition;
- authoritative spec and ADR sections;
- whether implementation—not merely product scope—has been authorized;
- active branch and draft PR, or the approved point at which they will be created;
- relevant code and tests as they exist now;
- exact targeted and required gate commands;
- internal documentation that must remain unpublished; and
- available agent capabilities, concurrency, and workspace isolation.

If the handoff, Issue, spec, ADR, repository, or approval state disagree, stop
and resolve the contract. Do not ask an implementer to discover which source of
truth or authorization wins.

### Step 2 — Build a dependency graph

Break the approved slice into units with observable outputs. For each unit,
record inputs, interfaces, files, dependencies, acceptance criteria, and risk.
Keep cross-cutting integration work as an explicit parent-owned node.

Each packet maps to one or more acceptance criteria from the owning Issue. The
packet is not itself a new durable planning record.

Several packets may implement one Issue. Create another Issue only when a
separable deliverable, defect, investigation, or consequential decision must
survive independently—not because the parent decomposed implementation into
smaller assignments.

Record parent-owned integration, coherent commit construction, tracking updates,
and draft-PR maintenance as explicit dependency-graph nodes.

A packet is ready to delegate only when another capable agent can complete it
without inventing product behavior, architecture, or an interface used by a
sibling packet.

Choose the least machinery that satisfies the accepted contract. Do not add an
abstraction, configuration surface, or extension point without a concrete
current use or an explicitly required seam. Keep adjacent cleanup out of the
packet unless it is necessary for correctness or named in scope.

### Step 3 — Retain or delegate by risk

The orchestrator retains:

- unresolved product, architecture, schema, privacy, security, or migration
  decisions;
- confirmation that implementation authority has been granted;
- work spanning several subsystem contracts;
- ambiguous debugging without a known playbook;
- shared integration files, migrations, schemas, lockfiles, generated artifacts,
  and conflict-prone registries;
- reconciliation of mixed changes in files also containing user-owned work;
- Git staging, coherent commit construction, push, Issue updates, and draft-PR
  lifecycle unless explicitly delegated;
- tracking and documentation accounting;
- triage, final acceptance, merge, release, tag, publish, and deployment; and
- any decision that would be expensive to reverse.

Delegate bounded implementation when the contract and acceptance evidence are
clear. Use `agentic-session-economics` for the capability tier and
`agentic-driving-weaker-models` when the implementer is below the strongest
available tier.

If decomposition introduces a new judgment-sensitive choice, follow
`agentic-collaboration-cadence` and obtain human approval before spawning work.

Pre-authorized mechanical work may continue without repeated checkpoints.
Implementation stops only when a new consequential choice appears, evidence
contradicts the contract, or an action exceeds granted authority.

### Step 4 — Assign ownership and concurrency

Parallelize only work that is both dependency-independent and ownership-disjoint.

- Give each live agent exclusive ownership of named files or modules.
- Put overlapping surfaces, migrations, shared schemas, lockfiles, and central
  registries in serial order or keep them parent-owned.
- State forbidden files explicitly.
- In a shared workspace, assume edits are immediately visible to every agent.
- Do not let implementers commit, tag, publish, deploy, or rewrite user changes
  unless the packet explicitly grants that authority.
- Do not assign a file to an implementer when it already contains overlapping
  user-owned changes unless the packet explicitly describes how those changes
  will be preserved.
- When approved and user-owned changes share a file, keep integration
  parent-owned and use hunk-level inspection or partial staging to preserve
  commit boundaries (`examples.md` §1).
- Implementers do not stage or commit by default. Their filesystem edits remain
  visible to the parent for inspection and selective integration.
- Isolated worktrees may permit packet-local commits only when the packet grants
  that authority and the parent still owns final integration.
- Never let a packet publish internal handoffs, profiles, ledgers, or continuity
  documents merely to complete a PR record.

Two agents producing complementary edits to the same component are not parallel
work. The coordination cost and merge risk erase the apparent speedup.

### Step 5 — Choose a compact or full work packet

Use the full template in Section 3 for feature behavior, multi-file work,
debugging, migrations, risky integration, or any packet requiring meaningful
judgment.

A compact packet is allowed only when all of these are true:

- the change is mechanical or narrowly bounded;
- behavior and exact output are already specified;
- no new interface, schema, dependency, or product decision is possible;
- ownership is disjoint;
- one targeted verification command is sufficient; and
- no external GitHub write is required.

Regardless of size, every packet names the owning Issue or contract, allowed and
forbidden files, verification, and required return.

#### Compact template

```markdown
# Compact work packet: <ID — title>

- Owning Issue/criterion: <link and acceptance criterion>
- Objective: <one exact outcome>
- Allowed files: <exclusive list>
- Forbidden files: <list>
- Required edit: <deterministic instruction>
- Verification: `<exact command>`
- External writes: none
- Return: files changed, command/result, deviations or blockers
```

### Step 6 — Require implementer self-verification

Before returning, the implementer runs the packet's targeted tests and reports
every required gate as **run**, **skipped**, or **failed**, with evidence. A
quietly reduced test suite is a failed return contract.

The implementer also:

- provides red/green evidence for repaired defects when the packet owns that
  evidence;
- completes documentation-impact accounting for files in scope;
- reports expected Issue/PR tracking impact without changing GitHub unless the
  packet explicitly grants that authority;
- reports all files touched, including generated or incidental files; and
- states whether any user-owned or unrelated changes were encountered.

A quietly reduced test suite, unnamed skipped gate, bare "no docs needed," or
unauthorized Issue/PR update is a failed return contract.

### Step 7 — Audit the workspace, not the report

For each return, the orchestrator independently:

1. inspects repository status and the actual diff against the verified base;
2. identifies every file and hunk changed, including generated files;
3. confirms forbidden, unrelated, and user-owned changes were preserved;
4. traces each hunk to an Issue acceptance criterion, governing contract, or
   a necessary supporting change;
5. checks whether a materially smaller implementation preserves the same
   accepted behavior;
6. runs a focused acceptance command;
7. verifies claimed red/green evidence where proportionate;
8. searches project-wide for stale references after renames or moves;
9. performs tracking and documentation accounting; and
10. accepts, repairs, rebriefs, or rejects the packet explicitly.

Never assume a timed-out or interrupted agent made no changes. Inspect status,
diffs, generated artifacts, and running processes before retrying — partial
writes remain, and a replacement spawned from the original brief assumes a clean
base that no longer exists (`examples.md` §2).

### Step 8 — Integrate serially and advance the draft PR

Integrate in dependency order, then complete parent-owned seams.

For each coherent integrated state:

1. inspect and stage only the intended hunks;
2. run the relevant targeted and cross-component gates;
3. construct a focused parent-owned commit;
4. after the first coherent commit is locally green, push and open the draft PR
   when authorized;
5. link the owning Issue and governing contracts;
6. update the draft PR with later coherent commits and verification evidence;
7. keep internal continuity documents unpublished; and
8. update the handoff with the actual Issue, branch, PR, verified state, and next
   action.

After all packets are accepted, run the full required gates. Only the integrated,
gate-checked state advances to independent cold review.

Do not mark the PR ready merely because all implementers returned. Parent
acceptance, integrated verification, documentation accounting, and cold review
still govern readiness.

---

## 3. Implementation work-packet template

The full packet template lives in `assets/work-packet-template.md`. Read it when
you are about to brief an implementer — it is a form to fill, not reasoning you
need resident while planning.

A compact packet may omit Minimality constraints, Non-goals, and Documentation
impact when the work touches one file and one contract. Everything else is
required, because each remaining field is what an isolated implementer cannot
reconstruct from the repository alone.

## 4. Capability routing

Roles are based on observed capability, not vendor or product names:

| Role | Suitable work | Must not own by default |
|---|---|---|
| Orchestrator tier | Interpretation, decomposition, judgment, integration, acceptance | Large mechanical batches that do not need its judgment |
| Implementation tier | Bounded feature work against a frozen contract; targeted tests and local debugging | New product behavior, architecture, cross-cutting contracts, final acceptance |
| Mechanical tier | Deterministic edits, formatting, generated updates, exact-text routing | Ambiguous code changes or judgment-sensitive prose |
| Reviewer tier | Independent bounded audit with a focused rubric | Implementation conversation or final triage authority |

The same model may fill different roles on different projects. Calibrate against
actual results and gates; do not hard-code "strong" or "cheap" to a provider.

---

## 5. Parent acceptance checklist

- [ ] Implementation authority—not only Issue ratification—was verified.
- [ ] Repository, branch, base commit, and existing user changes were inspected.
- [ ] Every packet mapped to specific Issue acceptance criteria.
- [ ] Every packet had one owner, allowed files, forbidden files, and non-goals.
- [ ] Compact packets met every compact-packet eligibility rule.
- [ ] Parallel packets were dependency-independent and ownership-disjoint.
- [ ] Implementer returns accounted for gates, red/green evidence, documentation,
      tracking impact, and external writes.
- [ ] Actual status and diffs were inspected independently of reports.
- [ ] Every changed hunk traces to the accepted contract.
- [ ] Unrelated and user-owned changes were preserved.
- [ ] No materially smaller implementation preserves the same behavior.
- [ ] Focused acceptance checks passed for each packet.
- [ ] Coherent commits contain only intended hunks.
- [ ] Draft PR timing, Issue linkage, and internal-document visibility are correct.
- [ ] Cross-component and full required gates pass on the integrated state.
- [ ] Handoff state matches the real Issue, branch, PR, and next action.
- [ ] Cold reviewers receive only the integrated diff, Issue criteria, contracts,
      and review brief—not implementation history or implementer reports.

---

## 6. Failure patterns

- **Delegating the decision, not the work.** If an agent must decide what the
  product should do, the packet is not ready.
- **Parallelizing a shared surface.** File collisions are a visible symptom;
  incompatible assumptions can survive a clean merge.
- **Accepting a green self-report.** The parent must inspect and rerun a small,
  independent acceptance check.
- **Giving implementation history to reviewers.** It anchors them on the chosen
  approach and destroys the cold-review control.
- **Retrying after interruption without auditing state.** Partial writes remain.
- **Using a stronger model as a substitute for a contract.** Higher capability
  lowers error probability; it does not resolve unspecified behavior.
- **Building for hypothetical reuse.** A single-use abstraction, configuration
  surface, or extension point adds cost without satisfying more of the current
  contract.
- **Turning implementation into cleanup.** Unrelated refactors make the diff
  harder to verify and consume scope that the packet never authorized.
- **Treating Issue ratification as coding authority.** Desired scope and
  permission to implement can be separate checkpoints.
- **Creating one Issue per work packet.** Packets are temporary implementation
  decomposition; Issues are durable deliverables and decisions.
- **Letting implementers administer GitHub.** External tracking remains
  parent-owned unless explicitly granted.
- **Opening a draft PR from an incoherent or locally red state.** Open it after
  the first coherent green commit.
- **Committing the whole shared worktree.** Inspect and stage intended hunks so
  user-owned and unrelated work do not enter the packet commit.
- **Publishing continuity documents.** A private repository may later become
  public; keep internal memory out of the PR.
- **Equating implementer completion with PR readiness.** Integrated gates and
  cold review still remain.

## When NOT to use this skill

- The product or UX is still being discovered; use
  `agentic-product-discovery` to resolve and ratify the contract first.
- The task is one tiny, low-risk edit where delegation costs more than direct
  implementation.
- You are running the independent reviewer pass; use
  `agentic-review-orchestration`.
- You need model-specific failure mitigation or raw cost decisions; use
  `agentic-driving-weaker-models` or `agentic-session-economics`.

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
