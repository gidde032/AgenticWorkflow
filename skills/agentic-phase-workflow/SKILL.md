---
name: agentic-phase-workflow
description: >-
  Run the issue-backed development loop that turns a ratified spec into shipped
  increments: select an owning Issue, confirm implementation authority,
  implement on a focused branch, open a draft PR after the first coherent green
  commit, review independently, repair with regression tests, reconcile
  documentation and tracking, and close delivery state after merge. Use when
  planning or running a feature phase, hardening pass, bundled phase,
  spec-drift audit, workflow-improvement release, or release closeout; when
  deciding whether work is phase-shaped or pass-shaped; or when sequencing
  Issues within a milestone. Do not use for day-one project bootstrap,
  repository-wide documentation migration, or ordinary Issue/PR administration
  that does not require choosing or running a development shape. Premise: the
  workflow is the product, as much as the code.
---

# Agentic Phase Workflow

The shape of AI-directed development work. This skill sequences the loop that
turns a ratified contract and owning Issue into a reviewed, verified delivery
without losing project coherence.

The loop below is the **end state of ten documented revisions** — a new project
starts here rather than re-deriving it. How each revision emerged from evidence
belongs to `agentic-workflow-evolution`; this skill hands you the result.

Worked examples and provenance: `examples.md`.

---

## 1. Start with a spec and a phased plan (before any code)

If the problem, workflow, scope, experience, or visual direction is still
materially unsettled, run `agentic-product-discovery` first. The spec should
record ratified product choices, not conceal unresolved discovery inside an
implementation plan.

Write a spec first. It costs little and becomes the canonical scope reference
for the whole project — reviewers cite it, defer/fix decisions turn on it, and
"in scope vs. later" stops being an argument.

On the reference project it took about 30 minutes to write, and reviewers then
cited its sections directly when justifying findings (`examples.md` §2).

A spec has four load-bearing parts. Generic skeleton:

```
# <Project> — Spec & Phase Outline

## 1. Overview          — vision, target users, success criteria (one paragraph each)
## 2. Stack             — table: layer | choice | rationale
## 3. Functional Reqs   — FR-1, FR-2, ... each a testable "the tool must ..."
## 4. Non-Functional    — budgets: latency, cold-start, coverage floor, size caps
## 5. Schema / Design   — data model or module boundaries; the contracts
## 6. Phase Outline      — Phase 1..N, each with deliverables + success criteria
                          sequenced so EACH phase ends in a usable increment
```

The non-negotiable property of the phase outline: **each phase ends in a usable
increment**. Not "the ORM layer" then "the CLI layer" — instead "init works",
then "add/list/view work", each a thing a user could run.

### Convert the ratified phase outline into delivery authorities

After the spec is approved:

- Create an Issue for each actionable deliverable, defect, investigation, or
  consequential unresolved decision.
- Place only the committed delivery horizon into a milestone.
- Keep detailed acceptance criteria and current delivery state in the Issue,
  not duplicated in the phase outline.
- Keep the spec authoritative for product behavior, boundaries, and budgets.
- Link each Issue to the governing spec or ADR section.
- Leave uncommitted ideas as labeled Issues without treating them as committed
  milestone scope.
- Do not create separate Issues for implementation, review, documentation, and
  summary of the same deliverable.

Read
`agentic-project-memory/references/github-source-of-truth-contract.md`
whenever converting or reconciling phase scope.

---

## 2. The per-phase loop

Every feature phase runs this sequence. A project may pre-authorize routine
implementation in its operating rules, but Issue ratification alone does not
imply permission to modify product code.

| Step | Action |
|---|---|
| 1 | **Orient from current truth** — read the handoff, owning Issue, milestone, governing spec/ADR sections, repository state, and active constraints. |
| 2 | **Confirm the phase contract** — acceptance criteria, non-goals, dependencies, numeric budgets, required documentation, and verification are explicit. |
| 3 | **Clear implementation authority** — when the work is judgment-sensitive and not already authorized, present impact, scope, dominant and least-predictable cost, exact implementation contract, and verification plan. Stop for approval. Do not confuse product-slice ratification with coding authorization. |
| 4 | **Start delivery state** — create or verify the focused branch; update the handoff with the Issue, milestone, branch, status, and exact next action. Create an optional gitignored `TASKS.md` only for immediate execution steps. |
| 5 | **Implement** — change code, tests, and affected documentation in a tight local gate loop. Use `agentic-implementation-orchestration` for decomposition, delegation, integration, and acceptance. |
| 6 | **Open the delivery record** — after the first coherent commit passes the required local gates, push and open a draft PR when authorized. Link the Issue and governing contracts. |
| 7 | **Run independent review** — give contextless reviewers the exact base/head diff, owning Issue and acceptance criteria, relevant contracts, file list, focused brief, and length cap. Reviewers do not see the implementation conversation or each other's findings. |
| 8 | **Triage with evidence** — use union for coverage and convergence for priority. Verify external and repository-state claims before accepting them. |
| 9 | **Give every finding a terminal disposition** — repair accepted findings with regression tests; create or link an Issue for explicitly deferred work; reject with evidence; mark duplicates; or identify work outside the contract. "Remember later" is not a disposition. |
| 10 | **Reconcile and verify** — run targeted tests and full required gates; update the PR, owning Issue, documentation, and tracking accounting; confirm no local-only planning item remains orphaned. |
| 11 | **Write synthesis only when warranted** — create an immutable phase summary when the phase spans multiple Issues/PRs or contains consequential decisions, workflow evidence, or cross-delivery reasoning. A focused single-Issue, single-PR phase normally needs no separate summary. |
| 12 | **Complete delivery** — mark the PR ready only after review and gates finish; merge only within granted authority; close the Issue only when all acceptance criteria are satisfied; then synchronize milestone state, handoff, conditional changelog, and next Issue. |

### Phase invariants

- **No judgment-sensitive implementation begins without authority.** A ratified
  Issue defines desired work; it does not override a required implementation
  checkpoint.
- **No phase ends until review, verification, and delivery accounting are
  complete.** A phase summary is required only when the synthesis criteria apply.
- **No accepted finding remains as prose-only deferral.** Repair it or create a
  linked Issue with rationale.
- **No implementation or phase ends without tracking and documentation
  accounting.** Use `agentic-project-memory §1a`.
- **Reviewers remain contextless.** They receive contracts, artifacts, and the
  diff—not the implementation conversation or other reviewers' conclusions.
- **Every repaired defect receives a faithful regression test.**
- **One fact has one authority.** Issues own planned work, PRs own delivery
  history, and the handoff owns immediate continuation.
- **Merge does not automatically mean Issue completion.** Use a closing keyword
  only when the PR satisfies the entire Issue.

**Implementation invariants:** delegated work is bounded by a written contract
and exclusive ownership; implementer reports are independently verified by the
top-level session; and only the integrated, gate-checked state advances to cold
review. Parallel agents never own overlapping surfaces.

The top-level session verifies the integrated state before cold review and
retains merge, tag, release, deployment, and final-acceptance authority unless
the project profile explicitly grants those actions.

The mechanics of step 5 (decomposition, work packets, ownership, integration,
and parent acceptance) live in `agentic-implementation-orchestration`. The
mechanics of steps 7–9 (how to brief reviewers, personas vs. lenses,
parallel vs. serial) live in `agentic-review-orchestration`. The
regression-per-finding contract and the quality gates in step 5 live in
`agentic-verification-discipline`. This skill owns the *sequence*; those own the
*technique*.

## 3. Phase-shaped work vs. pass-shaped work

Two shapes of work. The choice determines everything that follows, and
conflating them is a named mistake.

**Phase-shaped work is for new features; pass-shaped work is for hardening.**
Hardening runs audit → severity-ranked plan → user-approved slice → execute →
next approved slice. Conflating the two means writing acceptance criteria before
the audit has found anything (`examples.md` §3).

| | Feature phase | Hardening pass |
|---|---|---|
| Trigger | Ratified new functionality with an owning Issue | End-of-horizon drift, accumulated defects, or user friction |
| Review shape | Contextless review of the focused phase PR | Multi-lens audit such as spec drift, user friction, and CI-as-contract |
| Planning authority | Issue acceptance criteria plus spec/ADR | Audit findings triaged into repair Issues or evidence-backed no-change dispositions |
| Delivery shape | Focused branch and PR; optional phase synthesis | Human-approved repair slices, each delivered through an Issue and PR |
| Cadence | Implement → draft PR → review → repair → verify → authorized merge | Audit → rank → approve slice → Issue/PR delivery → repeat |
| Completion | Issue and milestone state synchronized | Findings have terminal dispositions; release closeout runs when applicable |

The audit mechanics (orthogonal lenses, ranked findings, named false alarms)
belong to `agentic-review-orchestration`. The slice mechanics (impact-ranked,
human-picks-the-slice, report at the boundary) belong to
`agentic-collaboration-cadence`. This skill's job is only to make you pick the
right shape first.

---

## 4. Bundled phases

When several features touch **non-overlapping** code surfaces and need no schema
migrations or breaking changes, bundle them into **one** implementation phase
and **one** review cycle instead of one phase per feature.

**Payoff, two kinds.** One bundle of four features ran through a single
three-reviewer pass, saving three review cycles — and caught a cross-feature
interaction that single-feature reviews would have missed, because each reviewer
held the whole surface in context at once (`examples.md` §4).

**Precondition, stated hard.** Features must be *genuinely* non-overlapping in
code surfaces. If they share surfaces, serial phases with per-phase reviews are
safer: cross-feature interaction risk is what the bundled review is designed to
exploit, not suppress. When in doubt, go serial.

### GitHub representation of a bundle

Keep each independently meaningful deliverable as its own Issue even when
several Issues share one implementation and review cycle.

A bundled phase may use one branch and PR only when:

- every Issue belongs to the same committed horizon;
- the combined diff remains reviewable;
- contracts and acceptance criteria remain distinguishable;
- the bundle does not conceal a migration, breaking change, or consequential
  design decision; and
- merge will genuinely satisfy every Issue referenced with a closing keyword.

If one Issue remains incomplete after merge, reference it without closing it
and record the remaining acceptance criteria there.

---

## 5. Spec-drift audits and the living spec

Periodically — typically at end-of-version — audit the implementation against
the spec section by section. Each deviation receives one terminal disposition:

- **FIX NOW** — the implementation violates the accepted contract and is
  repaired in the current Issue/PR with a regression test.
- **ISSUE** — corrective or investigative work remains but is explicitly
  deferred to a linked Issue.
- **DOCUMENT** — the implementation reflects an accepted decision and the
  governing spec or ADR must be updated with rationale.
- **ACCEPT / NO CHANGE** — the difference is understood and deliberately
  tolerated; record evidence and rationale.

Do not use `ACCEPT` to hide unplanned work, and do not use `DOCUMENT` to weaken a
contract after the fact without the required human decision.

DOCUMENT-class findings are the point: they keep the spec alive rather than
letting it fossilize.

**A living spec is a feature, not a flaw.** Every audit cycle producing
DOCUMENT-class findings is also a spec backport cycle, and a spec edited at
end-of-version is healthier than one that is append-only. The discipline that
keeps it honest: the rationale is recorded inline, next to the changed number
(`examples.md` §5).

Budgets and gates may grow toward measured reality, but weakening one is a
consequential workflow and product-contract change. Present the observed data,
proposed new value, effect on users and verification, and alternatives. Obtain
the required human approval, then update the spec, gate configuration, and
rationale together. Never make a red gate green by silently moving its target.

Document deviations at decision time in the owning spec, ADR, Issue, and PR as
applicable—not later in the handoff. If the phase warrants a summary, link and
synthesize those decisions there rather than making the summary their first
record.

---

## 6. Workflow-improvement releases

A legitimate, distinct release shape: spend a batch on the *workflow artifacts
themselves* — memory files, brief templates, tooling, doc structure — **before**
any feature work in that version.

The rationale: tokens spent upfront on the workflow save more downstream than
tokens spent on features. One recorded estimate puts the payback at roughly 3–4
future doc updates plus one reviewer pass — about half a release's work
(`examples.md` §6). That is a single-project estimate, not a measured universal.

This shape is distinct from a hardening pass. A hardening pass responds to
*project* drift (the code diverged from the spec, users hit friction). A
workflow-improvement release responds to *workflow* drift — the artifacts that
*produce* the project have grown stale or expensive. Different target, different
trigger.

Represent a workflow-improvement release with its own milestone or explicitly
named horizon and one Issue per durable workflow change. Deliver tracked
repository changes through focused PRs. Internal-only memory changes still
receive local verification and handoff accounting, but must not be published
merely to make the GitHub record look complete.

Do not use a workflow-improvement release as a reason to trigger the explicit
repository-migration workflow mid-project.

---

## 7. Issue-backed delivery-state tracking

Do not create a full local implementation/review/summary task list for every
planned phase.

Use:

- **GitHub Issues** for durable deliverables, defects, investigations, deferred
  findings, and unresolved decisions.
- **Milestones** for the committed delivery horizon.
- **Pull requests** for in-flight implementation, review, verification, and
  delivery history.
- **`handoff.md`** for the active Issue, branch, PR, blocker, verified state,
  and exact next action.
- **Optional gitignored `TASKS.md`** for the current session's mechanical
  checklist only.

At the start of a phase, verify which Issue is active and whether implementation
is authorized. At every state transition, update the owning authority rather
than reproducing the same status across several files.

The local checklist may be cleared or replaced after the session. It is not an
audit trail; the Issue and PR provide that history.

---

## 8. Horizon and Release Closeout

This skill is the entry point for "we merged — what now?", because the person
asking is standing inside the phase loop. Closeout has two halves and they run
in order: **delivery state** (Issues, milestones, branches, what ships next),
owned here; and **what the closeout must record** (changelog, roadmap, lessons,
handoff), owned by `agentic-project-memory`. Work the checklist below, then hand
off to that skill for the documentation-impact accounting rather than
reconstructing its placement rules here.

At the close of a committed horizon:

- [ ] Every included Issue has a terminal disposition: completed, moved with
      rationale, rejected with evidence, or explicitly retained in a later
      horizon.
- [ ] Every merged PR records its owning Issue, review result, verification, and
      documentation accounting.
- [ ] All required gates are green, or the release remains blocked with an
      explicit Issue and truthful status.
- [ ] Accepted deferred findings have linked Issues.
- [ ] Documentation impact is reconciled across user docs, operating rules,
      contracts, ADRs, API/schema docs, runbooks, and conditional release docs.
- [ ] `handoff.md` identifies the next Issue or an explicit waiting state and
      contains no duplicate backlog.
- [ ] Pending lessons have been verified and routed; actionable remnants have
      Issues.
- [ ] Practices and retrospective documents receive their batched update when
      new evidence warrants one.
- [ ] A phase or horizon summary exists only when its synthesis threshold was
      met.
- [ ] `CHANGELOG.md`, release notes, tag, and GitHub Release are created only
      when the approved release model requires them.
- [ ] Merge, tag, release, publish, and deployment actions remain within the
      granted authority.

---

## When NOT to use this skill

- **Discovering what to build, build-vs-buy, product scope, interaction, or
  visual direction** — `agentic-product-discovery`.
- **Decomposing, briefing, assigning, integrating, or accepting implementer
  work** — `agentic-implementation-orchestration`.
- **Briefing or triaging reviewers** — the loop's steps 7–9 delegate to
  `agentic-review-orchestration`.
- **Writing regression tests, setting up gates, defining contracts** — that's
  `agentic-verification-discipline`.
- **Handoff docs, memory files, lesson routing** — `agentic-project-memory`.
- **Token/cost discipline, model choice, session lifecycle** —
  `agentic-session-economics`.
- **Slice grain, check-in cadence, human-in-the-loop pauses** —
  `agentic-collaboration-cadence`.
- **How a hunch becomes an adopted practice / how the loop itself evolved** —
  `agentic-workflow-evolution`.
- **Day-one instantiation of all these files on a brand-new project** —
  `agentic-project-bootstrap`.
- **Ordinary Issue, milestone, or PR administration without choosing or running
  a development shape** — use the available GitHub tooling.
- **Repository-wide documentation and GitHub migration** — use the explicit
  migration workflow only when deliberately invoked.
- **Deciding which artifact owns planning, delivery, state, or rationale** —
  `agentic-project-memory`.
- **Stress-testing one consequential plan or architecture decision before ratifying
  it** — `agentic-decision-challenge` (`/grill`) exposes hidden assumptions and
  records the decision; return here to turn the ratified decision into delivery.

This skill is the container that sequences the others; when the question is
*which shape of work is this and what's the next step in the loop*, you're in the
right place.

---

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
