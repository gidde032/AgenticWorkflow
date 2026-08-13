---
name: agentic-project-bootstrap
description: >-
  The day-one instantiation runbook for the whole human-directs-AI-agents
  workflow system. Use when starting a new project; when adopting this workflow
  on an existing project; for day-one setup; when standing up a spec, memory
  files, GitHub-backed planning and delivery, quality gates, a review cadence,
  and an evolution ledger together; when someone says "set up the workflow",
  "bootstrap this repo", "start a project the agentic way", or "instantiate the
  agentic workflow". This is the ROUTER — it sequences the sibling skills and
  gets out of the way. Do not trigger it for ordinary mid-project Issue, PR,
  documentation, or implementation work. Premise: the workflow is the product,
  as much as the code.
---

# Agentic Project Bootstrap

The instantiation runbook. In one session you stand up a **spec with phases,
a memory architecture, GitHub-backed planning and delivery, quality gates,
a review cadence, and an evolution ledger** — then hand off to the per-phase
loop and stay out of the way.

**The key promise:** a new project starts at the *end state* of a reference
project rather than deriving it, skipping ten documented workflow revisions of
trial and error. You inherit the matured loop, not the derivation.

These are **solo-maintainer defaults**, calibrated on one agent-heavy project
and extended through two documentation-and-GitHub migrations. They are not a
validated team-scale claim. Where this skill gives a number or default, preserve
its evidence boundary rather than upgrading it — see `examples.md`.

---

## The bootstrap sequence

A numbered runbook. A **CHECKPOINT** is a hard stop only when the human must
ratify a consequential decision or grant external-write authority. Once a
project profile, spec, and authorized action boundary have been ratified,
continue through mechanical setup without repeating approval requests. Stop
again only when evidence contradicts the approved profile, a new consequential
choice appears, or an external action falls outside the granted authority.
The checkpoint rationale lives in `agentic-collaboration-cadence`.

### Discovery gate — resolve product uncertainty before Step 0

If the product's problem, audience, scope, core workflow, build-vs-buy choice,
or visual direction is still materially open, route to
`agentic-product-discovery` first. Return here after the product-and-design
contract is ratified. Skip discovery when the user already supplies a coherent,
approved product contract; bootstrap should not reopen settled taste or scope.

### Step 0 — Ratify the project profile (10 questions max), then CHECKPOINT

Ask a short, bounded interview. Reuse answers supplied in a project-profile
file; do not ask the human to repeat them. Do not guess repository visibility,
licensing, public-release intent, or external-write authority.

- [ ] **Project goal** — one sentence: what it does and who uses it.
- [ ] **Stack and delivery target** — language, framework, runtime, packaging,
      hosting, or deployment target.
- [ ] **Maintainer model** — solo maintainer or contributors? This controls
      review, approval, and ownership defaults.
- [ ] **Repository identity** — GitHub owner/repository, default branch, and
      whether the remote already exists.
- [ ] **Visibility and public intent** — private, public, or remain private
      while performing a public-readiness audit.
- [ ] **License and release model** — chosen license; continuous, versioned, or
      one-shot delivery; anticipated first milestone or version.
- [ ] **Quality bar and definition of done** — prototype, production, or
      safety-critical, plus the observable conditions for completing work.
- [ ] **Cost sensitivity** — whether session or token spend is a live constraint.
- [ ] **Sensitive-data and compliance boundaries** — secrets, private content,
      generated artifacts, third-party assets, or data that cannot leave the
      machine.
- [ ] **Action authority and hard rules** — whether the agent may create Issues,
      labels, milestones, branches, commits, draft PRs, and repository
      configuration; identify actions that still require confirmation.

**CHECKPOINT:** return a compact project profile containing every answer,
assumption, and unresolved decision. The human ratifies the profile and
external-action boundary before repository or GitHub writes begin.

### Step 1 — Write the spec, then CHECKPOINT

Write the spec first. It is cheap — roughly 30 minutes and one round-trip on
the reference project (`examples.md` §3) — and becomes the canonical scope
reference reviewers cite. The full skeleton and phase-outline rules live in
`agentic-phase-workflow §1`; instantiate these sections:

- [ ] **Vision** — one paragraph: what it is, who it's for, success criteria.
- [ ] **Functional requirements** — FR-1, FR-2, … each a testable "the tool
      must …".
- [ ] **Non-functional budgets — AS NUMBERS.** Latency, cold-start, coverage
      floor, size caps. A budget without a number can't gate anything.
- [ ] **Design / schema** — the data model or module boundaries; the contracts.
- [ ] **Phase outline** — Phase 1..N, **each ending in a usable increment** (not
      "the ORM layer" then "the CLI layer" — instead "init works", then
      "add/list/view work").
- [ ] **Risks.**
- [ ] **Open questions** — features deferred to a later version, labeled.
- [ ] **Definition of done** — from Step 0's interview.

**CHECKPOINT:** the human reviews the spec, especially phase boundaries,
numeric budgets, deferred scope, and the definition of done. Do not create
GitHub planning artifacts from an unratified spec.

After approval, classify every actionable phase deliverable, defect, deferred
feature, and unresolved decision as an Issue candidate. The spec remains the
product contract; Issues become the executable work queue. Do not leave
actionable planning content only inside the spec.

### Step 2 — Instantiate the memory files (day-one set only)

Canonical templates live in `agentic-project-memory` — reference them, do not
duplicate here. Create only the day-one four; the catalogue, narrative, and FAQ
are created on **first use**, not day one (see "What NOT to do").

| File | One-line purpose | Template source |
|---|---|---|
| Operating-rules file (for example `CLAUDE.md`) | Compressed repository rules, source-of-truth boundaries, gates, and workflow commands; keep under about 200 lines | `agentic-project-memory §1` |
| State file (`handoff.md`) | Current state, active Issue, branch and PR, blockers, verified last action, and exact next command | `agentic-project-memory §1, §2` |
| `pending-lessons.md` | Temporary evidence-backed lessons awaiting promotion to the appropriate practice document | `agentic-project-memory §4a` |
| Ignore-file entries | Internal memory and optional active-session files added to `.gitignore` in the same commit in which they are created | `agentic-project-memory §8` |

Do not use `handoff.md`, `pending-lessons.md`, or a local task file as a second
backlog. Planned work belongs in GitHub Issues. A local `TASKS.md` is optional,
gitignored, and limited to the steps actively being executed in the current
session.

### Step 3 — Establish GitHub-backed planning and delivery

Follow the source-of-truth contract in
`agentic-project-memory/references/github-source-of-truth-contract.md`.

For a GitHub-hosted project:

- [ ] Verify the repository identity, default branch, visibility, license, and
      approved external-action boundary.
- [ ] Define a small initial label vocabulary. Start with `bug`, `enhancement`,
      `documentation`, `maintenance`, `investigation`, `needs-decision`,
      `ready`, and `blocked`; add project-specific labels only when they support
      a real filtering or routing need.
- [ ] Create the first milestone for the next committed delivery horizon.
- [ ] Convert ratified phase deliverables, defects, deferred features, and
      unresolved decisions into Issues with context, acceptance criteria,
      dependencies, and verification expectations.
- [ ] Create concise Issue templates and `.github/pull_request_template.md`.
- [ ] Use Issues as the durable backlog, milestones as committed release scope,
      and PRs as the implementation, review, verification, and delivery record.
- [ ] Create `CHANGELOG.md` only for a versioned project that needs curated
      user-facing release history.
- [ ] Create `ROADMAP.md` only when the project has multiple meaningful planning
      horizons. Keep it high-level and link every actionable entry to an Issue.
- [ ] Keep optional local `TASKS.md` limited to active-session execution steps.

Prefer one Issue per deliverable, defect, or consequential decision. Do not
create separate Issues for mechanical workflow stages such as implementation,
review, documentation reconciliation, and summary; represent those as
checklists within the owning Issue or PR.

If Step 0 already ratified these choices and authorized GitHub writes, execute
this step without another checkpoint. Stop only when repository evidence
contradicts the profile or a required decision remains unresolved.

### Step 4 — Define the gates (3–6), wire into tiers

Follow the "define-your-gates checklist" in `agentic-verification-discipline §5`.
For each gate, write three things: **command** + **numeric pass criterion** +
**change-requires-sign-off rule** (weakening a gate is never an autonomous agent
decision).

- [ ] Pick 3–6 gates (format, lint, type-check, tests+coverage floor, any perf
      budget from the spec's non-functional section).
- [ ] Set each numeric budget by MEASURING the walking skeleton (or current
      reality, on an existing project), then ratchet later — never copy another
      project's numbers (`examples.md` §4).
- [ ] Record each gate's rationale **inline** next to the config line.
- [ ] Wire into whatever tiers exist — local hook (commit/push) and/or CI —
      per the three-tier placement table. Auto-fix belongs at commit time, not
      in CI's ephemeral filesystem. Use the ecosystem's hook manager (Python:
      `pre-commit`; Node: husky + lint-staged; anywhere: `core.hooksPath` +
      scripts) — the tier model is portable, the wiring tool is not.
- [ ] Include a **fast smoke tier from the start**, with a **checked inventory**:
      a regression test that asserts the exact smoke-test count, so "quick
      feedback suite" is a contract, not a convention.

#### GitHub Actions and ruleset order

Stand up the repository-owned Actions check and its ruleset by following
`agentic-verification-discipline/references/github-actions-contract.md` — it owns
workflow requirements, the required-check activation order, and the
configured-versus-enforced reporting format. Do not require a status check before
it has run successfully at least once.

Two defaults are bootstrap's own decision, not verification mechanics:

- [ ] For a solo-maintainer repository, default to requiring a PR with zero
      approving reviews, the repository-owned status check, blocked force
      pushes, and restricted branch deletion.
- [ ] Require review approvals only when the maintainer model or risk profile
      supports them.

### Step 5 — Set implementation orchestration

Derive operating rules and the current work-packet template from
`agentic-implementation-orchestration`; derive capability routing from
`agentic-session-economics`.

- [ ] Name the project's **orchestrator, implementation, and mechanical
      capability tiers** from observed ability, not provider names.
- [ ] Set the default ownership rule: one live agent owns each named file or
      module; overlapping surfaces run serially or remain parent-owned.
- [ ] Keep publishing, deployment, integration, merge, tagging, and final
      acceptance with the top-level session unless the approved project profile
      grants them.
- [ ] Instantiate the current work-packet template from
      `agentic-implementation-orchestration`; do not preserve a second copy here.
- [ ] Populate it with the owning Issue, branch, allowed files, governing
      spec/ADR, acceptance criteria, required gates, documentation impact, and
      escalation conditions.

### Step 6 — Set the review cadence

Derive the specifics from `agentic-review-orchestration`; instantiate here:

- [ ] **Reviewer count: default 3, with a standing skeptical senior engineer**
      always in the mix — non-negotiable; this persona caught the
      highest-severity findings in multiple phases (`examples.md` §5).
- [ ] **Seed a persona library by stack** — pick rotating specialists named
      after the surfaces at risk (web app → frontend/accessibility, API-contract,
      auth/security, data-model; data pipeline → schema-integrity, idempotency,
      cost/perf, observability; CLI/library → packaging, UX-surface, dependency;
      plus a testing/CI specialist whenever pipeline config changes).
- [ ] **End-of-version audit lenses:** start with **spec-drift + user-friction**.
      Add a **CI-as-contract** lens once infrastructure accumulates — not day one.
- [ ] **Create the project's brief-templates file NOW**, filling the generic
      reviewer-brief template from `agentic-review-orchestration` with this
      project's root path and stack, so Phase 1's reviews are fill-in-the-blanks.
- [ ] Reviewer briefs cite the owning Issue and its acceptance criteria, the
      relevant spec or ADR, and the exact base/head diff.
- [ ] Independent review happens before the PR is marked ready for merge.
- [ ] Every accepted finding is either repaired with verification or deferred
      to a linked Issue with rationale before the phase closes.
- [ ] Documentation drift is reviewed as part of the normal review contract;
      do not add a separate documentation reviewer unless the change warrants it.

### Step 7 — Open the evolution ledger

Per `agentic-workflow-evolution §4, §8`:

- [ ] **Empty revisions log** — append-only; the first real workflow change
      becomes "Revision 1".
- [ ] **Starter open-questions ledger** — an empty append-only list. Record a
      question the first time the project makes a workflow choice it cannot yet
      justify with evidence. Each entry stays OPEN until a real phase answers
      it; `agentic-workflow-evolution` owns the promotion bar.

### Step 8 — Start the first issue-backed delivery slice

- [ ] Confirm that every ratified first-horizon deliverable or unresolved
      decision has an owning Issue.
- [ ] Select the first `ready` Issue and create a focused branch.
- [ ] Use the Issue acceptance criteria to instantiate the first work packet.
- [ ] After the first coherent commit passes the local gates, push the branch
      and open a draft PR when Step 0 granted that authority.
- [ ] Link the PR to the Issue. Use an automatic closing keyword only when
      merging the PR will genuinely complete the entire Issue.
- [ ] Record the active Issue, branch, draft PR, verification state, and exact
      next command in `handoff.md`.
- [ ] If useful, create a gitignored `TASKS.md` containing only the immediate
      session checklist. Do not copy the project backlog into it.
- [ ] Hand off to `agentic-phase-workflow §2`.

---

## Adoption on an EXISTING project

Same target end state, different on-ramp. Do NOT write the spec from imagination —
write it from reality.

Adoption introduces the workflow around current reality. A repository-wide
documentation and GitHub migration is a distinct operation, not part of it — do
not trigger one merely because an agent finds stale documentation mid-project.

`agentic-docs-github-migration` never fires on its own; only when the user names
it. So when the inventory below shows a solo-maintained repository with
substantial existing documentation and little or no GitHub governance, say so and
offer `$agentic-docs-github-migration profile` before continuing. That is the one
case where bootstrap is the wrong on-ramp, and the user cannot learn it unless
this skill says so.

Before modifying an existing project:

- inventory current documentation, local planning files, Issues, PRs,
  milestones, branches, unpublished commits, and worktree changes;
- preserve unrelated and unpublished work;
- give every discovered planning or audit item a terminal disposition:
  completed with evidence, retained as authoritative documentation, converted
  to an Issue, merged with an existing Issue, or explicitly rejected with
  rationale;
- do not combine unrelated product changes with workflow-adoption changes; and
- do not delete or rewrite stale planning files until their contents have been
  reconciled and, when requested, backed up.

1. **Run a spec-drift-style audit FIRST.** Before writing the spec, spawn a
   contextless reviewer to read the existing code and produce the spec's factual
   backbone (per the audit shape in `agentic-review-orchestration` and the
   living-spec discipline in `agentic-phase-workflow §5`). Where the code and any
   existing docs disagree, document the deviation as **ACCEPTED** — don't fight
   it. The spec grows toward reality with rationale recorded inline.
2. **Seed the failure catalogue from history.** Instead of an empty catalogue,
   mine the bug tracker and git log for recurring failure classes and name them
   as lessons (mechanics in `agentic-project-memory`, evidence bar in
   `agentic-workflow-evolution §1`).
3. **Introduce gates at current-reality levels, then ratchet.** Measure the
   project's *actual* current coverage/latency and floor the gate just below it;
   raise later. **Never claim a floor the project doesn't currently meet** — a
   red gate on day one poisons trust in every gate.

---

## Right-sizing table

The middle column is the calibrated default. Scale down for a smaller project,
up for a team.

| Dimension | Tiny project (down-scale) | Solo, agent-heavy (default) | Team (up-scale) |
|---|---|---|---|
| Spec | Vision + FRs + budgets only | Full 7-section spec | Full spec + owned sign-off |
| Memory files | Handoff + pending-lessons only | All four day-one; catalogue/narrative/FAQ on first use | Add ownership conventions — who edits which file |
| Gates | Regression-per-fix + one smoke tier | 3–6 numeric gates across 3 tiers | Same, plus branch-protection enforcement |
| GitHub planning and delivery | Issues as needed, one stable CI workflow, focused PRs | Issues as backlog, milestones as committed horizon, draft PR after first green commit, solo ruleset defaults | Ownership labels, required human approvals, CODEOWNERS or equivalent |
| Implementation delegation | Parent implements and self-verifies | Bounded work packets with exclusive ownership; parent integrates and accepts | Isolated branches/worktrees plus owned integration |
| Reviewers | 1 skeptic | 3 with standing skeptic | 3 agents + human reviewers as full slots |
| Evolution ledger | Skip until 2nd revision | Revisions log + open-questions | Shared ledger; revision authorship recorded |

**Down-scale floor:** even the smallest GitHub-hosted project keeps a ratified
scope contract, measurable gates, regression-per-fix, one durable location for
planned work, and a traceable delivery record.

**Up-scale boundary:** the team column is reasoned extension, not tested
practice — this workflow was built and exercised by a solo maintainer. Adopt it
as a starting point and expect to revise it, particularly memory-file ownership.
`examples.md` §7 states what evidence sits behind each column.

---

## First-session exit criteria

Bootstrap is complete only when all applicable items are measurably true:

- [ ] The spec exists and the Step 1 checkpoint is cleared.
- [ ] The project's source-of-truth map is recorded in its operating rules.
- [ ] Day-one memory files exist and internal files are ignored as intended.
- [ ] Repository identity, visibility, license, and public-readiness intent are
      recorded without unresolved assumptions.
- [ ] Initial labels, the first milestone, and first-horizon Issues exist, or an
      exact external-access blocker and continuation command are documented.
- [ ] Local gates run green, or an existing-project deficit has a truthful,
      issue-backed ratchet plan.
- [ ] The GitHub Actions workflow has produced the intended stable check, or its
      first-run dependency is explicitly documented.
- [ ] Any branch ruleset is reported as configured and separately verified for
      actual enforcement.
- [ ] Implementation and reviewer brief templates are instantiated from their
      owning skills.
- [ ] The first ready Issue, branch, and draft PR exist when authorized and
      applicable.
- [ ] `handoff.md` names the active Issue, branch, PR, verified state, and exact
      next command.
- [ ] `CHANGELOG.md` and `ROADMAP.md` exist only when their project-profile
      conditions apply.

---

## What NOT to do at bootstrap

- **Don't pre-create the catalogue, narrative, or FAQ.** They earn existence
  through use: the catalogue on the first practice worth documenting, the
  narrative on the first workflow revision, the FAQ on the **second** time a
  question recurs. Pre-creating them means maintaining empty scaffolding and
  paying its read cost for nothing.
- **Don't copy another project's project-SPECIFIC skills.** A runbook whose facts
  weren't verified against *this* repo is worse than none — it asserts file paths,
  commands, and gate values that are wrong here, and a confidently-wrong doc costs
  more than an absent one. A project-specific skill library is something you
  build **later**, once the project has real history to encode — not something
  to clone on day one.
- **Don't set gates you can't measure.** A budget with no number and no command
  is decoration. If you can't run it and read a pass/fail, it isn't a gate.
- **Don't skip the human checkpoints.** Steps 0 and 1 gate everything downstream.
  The canonical failure is an autonomous agent implementing a taste-call the
  maintainer would have rejected, then pinning it with a regression test that
  makes it expensive to undo (`examples.md` §6). Surface; don't pin.
- **Don't maintain parallel backlogs.** GitHub Issues own actionable planned
  work. `ROADMAP.md`, the spec, `handoff.md`, and optional `TASKS.md` may point
  to Issues but must not silently recreate their queue.
- **Don't require a status check before it exists.** Run the repository-owned
  workflow first, confirm its exact check identity, and then configure the
  ruleset.
- **Don't confuse configured with enforced.** Report provider or repository-plan
  limitations explicitly.
- **Don't close Issues early.** Close on merge only when the PR satisfies the
  whole Issue; otherwise update or split the remaining work.
- **Don't change visibility, licensing, merge, publish, deploy, tag, or delete
  without authority.** These remain consequential external actions even when
  the surrounding bootstrap has been approved.
- **Don't silently turn normal project work into a repository migration.**
  Migration requires an explicit trigger and a complete audit/disposition pass.

---

## When NOT to use this skill

This skill is the router; once the system is stood up, the work lives in the
siblings. Route out when you are past day one:

| If you're… | Go to… |
|---|---|
| Figuring out what to build, comparing alternatives, or refining product/visual direction | `agentic-product-discovery` |
| Running the per-phase loop, or asking "phase or hardening pass?" | `agentic-phase-workflow` |
| Decomposing, briefing, assigning, integrating, or accepting implementer work | `agentic-implementation-orchestration` |
| Hardening briefs for a lower-capability agent or deciding when it must escalate | `agentic-driving-weaker-models` |
| Briefing/triaging reviewers, choosing personas or lenses | `agentic-review-orchestration` |
| Writing regression tests, defining gates, contracts-not-conventions | `agentic-verification-discipline` |
| Maintaining handoffs, lessons pipeline, doc granularity | `agentic-project-memory` |
| Managing token/cost, model mixing, session lifecycle | `agentic-session-economics` |
| Deciding when to pause for the human, slicing work | `agentic-collaboration-cadence` |
| Turning a hunch into an adopted practice; the evidence bar | `agentic-workflow-evolution` |

Come back here only when standing up the whole system on a **new or newly-adopted**
project.

---

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
