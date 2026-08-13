---
name: agentic-review-orchestration
description: >-
  Run independent, contextless multi-agent review against an exact draft-PR
  diff and accepted Issue contract. Use after an implementation is integrated
  and locally green; before marking a PR ready; when running a release-hardening
  audit; when convergence across independent reviewers would improve confidence;
  when building isolated reviewer briefs; or when validating and triaging
  findings into approved repairs, linked deferral Issues, false alarms, and
  other terminal dispositions. Covers reviewer isolation, exact base/head
  targets, personas, orthogonal audit lenses, disposable-state verification,
  bounded evidence-oriented briefs, parallel versus serial review, provisional
  ledgers, human repair approval, and public-safe PR summaries. Do not use for
  implementation, ordinary PR administration, or reviewing work that does not
  yet have a coherent integrated target.
---

# Agentic Review Orchestration

**Independent, contextless multi-agent review.** Instead of one agent reviewing
its own work, spawn several fresh reviewers who never saw the implementation,
brief each narrowly, and treat *agreement between them* as your strongest
priority signal.

Worked examples and provenance: `examples.md`.
Reviewer brief template: `assets/reviewer-brief-template.md`.

## Vocabulary

- **Subagent** — a separate agent instance spawned for a bounded job, with its
  own context window.
- **Contextless reviewer** — a subagent given *only* a file list and a written
  brief. It never sees the implementation conversation, the other reviewers, or
  their output. Independence is the entire value.
- **Convergence** — two or more independent reviewers flagging the same issue.
  The strongest signal you get.
- **Triage** — you deciding which findings are real and how severe. Reviewer
  output is an *input to judgment*, never a verdict.
- **Lens** — a posture defined by *what surface it inspects* (spec, UX, CI).
- **Persona** — a posture defined by *who the reviewer pretends to be*.
- **Review target** — the exact base commit, head commit, owning Issue, accepted
  contracts, and allowed files a reviewer may inspect.
- **Provisional ledger** — local mutable memory holding unapproved
  candidate findings. Not an implementation plan, public documentation, or
  reviewer input.
- **Public-safe review summary** — the consolidated, verified account placed in
  the PR after removing private paths, internal continuity material, raw agent
  output, and unverified claims.
- **Interrupted reviewer** — one that timed out, hit a usage limit, or returned
  incomplete evidence. It does not fill a reviewer slot.

## The core mechanism

Reviewers inspect one frozen delivery target:

- exact base and head commits;
- the owning Issue and acceptance criteria;
- relevant spec and ADR sections;
- the exact changed-file manifest;
- surrounding code or tests needed to evaluate the diff;
- a focused persona or lens;
- explicit exclusions; and
- safe read-only or disposable verification commands.

They do **not** receive the implementation conversation, implementer packets or
reports, the handoff or session task file, migration profiles or disposition
ledgers, prior audits, the provisional ledger, PR discussion, or another
reviewer's report.

The orchestrator reads across reports only after every reviewer has returned.
Independence is a controlled evidence property, not merely a fresh chat window.

- **Convergent findings are high-confidence.** Two independent paths to the same
  bug beat one agent's confident opinion. On the reference project this caught
  the top bug in every phase (`examples.md` §1).
- **Divergent findings broaden coverage.** A UX-focused reviewer catches what the
  correctness-focused one missed. Divergence is the reason to run more than one.
- **Independence is fragile.** Pasting implementation rationale into a brief, or
  saying "reviewer B already found X," destroys the independent path that made
  convergence meaningful. Brief each reviewer separately. Don't tell a reviewer
  it is one of three.

## The two review shapes

Pick by the kind of work, not by taste.

### Shape A — three-reviewer pass for a substantive feature PR

Once the implementation is integrated, locally green, and represented by a draft
PR, run three contextless reviewers:

1. A skeptical senior engineer.
2. A specialist for the highest-risk product or architecture surface.
3. A specialist for the next-most-independent risk surface.

Do not invoke this for a tiny mechanical change where review overhead exceeds
the risk; route that through normal parent verification and required gates.

An interrupted reviewer does not occupy a slot. Rerun that role fresh without
exposing provisional findings or completed reports.

- **One is ALWAYS a skeptical senior engineer.** Non-negotiable — this persona
  caught the highest-severity findings in multiple phases (`examples.md` §2).
- **The other two are rotating domain specialists**, chosen by what the phase
  touched.
- **Three is the default, not a floor to exceed.** Three stays legible to one
  orchestrator at triage; adding reviewers past that has no evidence behind it.

Add a **documentation-drift overlay** when the PR changes behavior, scope,
interfaces, commands, configuration, architecture, operations, release promises,
or workflow rules. Assign it to an existing specialist; do not add a fourth
reviewer for documentation alone. Give that reviewer the exact diff, relevant
repository-visible documentation, the governing spec and ADRs, the Issue
acceptance criteria, the documentation map, and the implementation's
documentation accounting.

Do not hand a cold reviewer `handoff.md`, `TASKS.md`, pending lessons, migration
ledgers, or phase evidence merely because they mention project status. The parent
verifies internal handoff consistency separately.

Require concrete contradictions, stale paths, unsupported promises, or missing
updates — not general suggestions to improve wording.

### Shape B — end-of-version multi-lens audit

At the end of a release cycle (not a feature phase), spawn reviewers by
**orthogonal lens** rather than persona:

| Lens | Question | Sources |
|---|---|---|
| **Spec drift** | Does implementation match accepted contracts and repository-visible claims? | Code, tests, config, spec, ADRs, Issues, milestones, conditional roadmap/changelog, README, relevant docs |
| **User friction / adversarial user** | What happens when a real person follows the supported workflow cold? | Public docs, packaged or deployed entry points, disposable test data |
| **CI as contract** | Do PR and release pipelines enforce the gates they claim? | Workflow files, required-check configuration, PR checks, release configuration, local-equivalent commands |

The handoff is current continuity, not delivery-history authority. Do not make it
a cold-review input unless the handoff architecture is itself the subject.

**Grow the lens count with the infrastructure.** Two lenses were the default
until CI complexity accumulated and a third caught a release-pipeline gap two
prior audits had missed, for about a third more tokens (`examples.md` §3). Each
lens should correspond to a surface that can drift independently — which is also
why lenses are rarely redundant (`examples.md` §4).

## Parallel versus serial review

**Default: run independent reviewers in parallel.** When reviewers inspect the
same frozen target with independent personas or orthogonal lenses, dispatch them
without sharing findings and collect all reports before triage. Do not pause for
human review between independent reviewers — the meaningful checkpoint comes
after consolidated evidence validation.

**Serial review is a different evidence shape.** Use it only when the human asks
for reviewer-by-reviewer checkpoints, the next reviewer's scope genuinely depends
on a previous decision, or a safety or access constraint prevents parallelism.

If a later reviewer sees an earlier report, that is a layered or meta-review, not
an independent reviewer. Do not count its agreement as convergence.

**Meta-review** may inspect completed reports for contradictions, missing
evidence, or triage errors. Label the role explicitly and keep its findings out
of independent convergence counts.

## Building your persona library

One **constant** plus **rotating specialists** chosen by what the work touched.

**The constant: skeptical senior engineer.** Posture: assume the implementation
is incomplete somewhere. Look for design flaws masked by passing tests, missing
edge cases, leaky abstractions, code that satisfies the spec *literally* but
misses its intent, unhandled error paths, and naming that will confuse a future
reader. Push back on confident-looking code that hasn't been stress-tested.

Give the skeptic a **minimality overlay**: trace changed hunks to the accepted
contract; identify machinery with no concrete current use; name the exact
removable lines or abstraction; describe a materially smaller implementation
preserving the contract; avoid requesting unrelated cleanup.

Aesthetic preferences, generic "too complex" claims, and speculative future
maintenance concerns are not valid findings without concrete present impact.

**The rotation: pick specialists by surface at risk.**

| Project type | Likely rotating specialists |
|---|---|
| Web app | Frontend/accessibility, API-contract, auth/security, data-model/migration |
| Data pipeline | Schema/data-integrity, idempotency/retry, cost/performance, observability |
| CLI / library | Packaging/distribution, UX/interface-surface, dependency/compat |
| Any | + testing/CI specialist whenever test or pipeline config changed |

**Rotate personas across cycles so blind spots don't compound.** Prompts drift
toward sameness — by the third phase on the reference project, two reviewer
prompts had converged enough to produce overlapping focus (`examples.md` §5).
That looks like convergence but isn't: the reviewers agreed because they were
asked the same question.

**Lens library** (Shape B):

- **Spec drift** — compare code, tests, configuration, spec, ADRs, Issue
  acceptance criteria, milestone membership, repository-visible documentation,
  and conditional roadmap/changelog. Concrete contradictions only.
- **User-friction / adversarial-user** — role-play a first-time user with a name.
  Run the real entry points from the docs. Produce a friction log: "I tried X, I
  expected Y, I saw Z."
- **CI as contract** — verify the repository-owned Actions workflow runs the
  canonical gate, the required check has the expected name and source, PR and
  release paths agree, and configured rules are not mistaken for observed
  enforcement.

## Briefing discipline

- **Brief like a smart colleague who walked in cold.** State the goal, hand over
  exact files, define the severity rubric, cap the length. Synthesis across
  findings is *your* job at triage, not theirs.
- **Heavy out-of-scope sections, with reasons.** Name everything already deferred
  or triaged with a one-line why. Cheapest lever available: it stops reviewers
  re-raising decided items and stops you dismissing them.
- **Require proof for minimality findings.** Reject "too complex" unless the
  reviewer identifies removable machinery and a narrower equivalent.
- **Freeze and verify the target.** Record base/head and run a base-to-head
  changed-file query before dispatch. If the branch moves during review, review
  the additional diff separately or restart against the new frozen head.
- **Separate parent orientation from reviewer inputs.** The parent may read the
  handoff, operating rules, and implementation reports. Cold reviewers may not.
- **Exclusions must not leak answers.** Name ratified non-goals and declined
  scope; do not seed suspected findings or relay what another agent believes.
- **Use disposable state for probes.** Never review backup, restore, migration,
  export, destructive, or privacy behavior against live user data.
- **No reviewer writes.** Reviewers do not edit code, update the PR, create
  Issues, or modify the provisional ledger.
- **Public-safe output is a parent responsibility.** Raw reports stay local until
  claims are verified and consolidated.

**Pre-flight sandbox integrity check — run before every spawn.** Verify the world
the reviewer will inspect is the real one. A reviewer handed an incomplete temp
sandbox will file accurate reports about a world that doesn't exist, and you pay
for them at triage (`examples.md` §6). Confirm:

- base and head resolve to the intended commits;
- the changed-file manifest matches the brief;
- every named contract and file exists;
- prohibited continuity and prior-review material is absent from a copied
  sandbox;
- disposable fixtures are isolated from live state; and
- the reviewer has no accidental write or external-action authority.

## Triage and approval protocol

Do not open or update the provisional ledger until all independent reviewers have
completed. An interrupted reviewer is rerun fresh first.

Then the parent:

1. Normalizes duplicate findings without erasing independent provenance.
2. Identifies convergence only among genuinely independent reviewers.
3. Verifies file:line evidence against the frozen head.
4. Reproduces behavior with disposable probes when proportionate.
5. Verifies external claims against current primary sources.
6. Recalibrates severity from concrete impact, not reviewer confidence.
7. Rejects false alarms with evidence.
8. Produces an impact-ranked candidate batch.
9. **Stops for human approval** before writing regression tests, implementing
   repairs, or turning judgment-sensitive candidates into new work.

After approval, every candidate receives one terminal disposition: repaired in
the current PR with fail-before-fix evidence; deferred to a linked Issue with
rationale and acceptance criteria; rejected with evidence; duplicate of an
existing Issue; or outside the accepted contract.

The provisional ledger stays local. Only a verified public-safe consolidation
belongs in the PR — remove private paths, raw reviewer text, internal continuity
details, unsupported severity claims, and unpublished project information.

### Named failure modes

- **Confidently wrong about the world.** A reviewer asserts a false or stale
  external fact. Verify API, library, and provider claims against primary sources.
- **Correctly wrong about an unfaithful sandbox.** The reviewer accurately reports
  an incomplete copied world. Preflight the target and manifest.
- **Contaminated convergence.** A reviewer saw another report, the ledger,
  implementation rationale, or a seeded finding. Its agreement is not independent.
- **Interrupted slot inflation.** A timed-out report counted as a completed
  reviewer. Rerun the role fresh.
- **Severity inheritance.** The parent preserves a reviewer's severity without
  validating actual impact.
- **Ledger-to-plan jump.** Candidates trigger fixes or new scope before the human
  approves the batch.
- **Live-state probing.** Verification modifies or exposes real user data instead
  of disposable fixtures.

## Model-tier economics for reviewers

**Default reviewers to a cheaper tier.** Audit lenses on a cheaper tier cost
roughly half with no observed quality loss (`examples.md` §7). **Raise the tier**
for high-stakes releases, security-sensitive surfaces, or when a cheaper run
produced muddy, low-signal reports.

Do not reduce reviewer count by exposing one reviewer's report to another and
calling it equivalent. If cost forces fewer independent reviewers, state the
reduced confidence explicitly. Running reviewers in parallel cuts wall-clock time
without adding checkpoints; cost and reviewer count stay separate decisions.

Deeper cost and model-mixing strategy: `agentic-session-economics`.

## User-as-reviewer

**A real human running the actual commands is a reviewer** — a full slot with
their own brief, not a sanity check. Hands-on maintainer testing caught real bugs
in three separate cases that sandboxed reviewers missed, each depending on the
real machine, install, or filesystem (`examples.md` §8).

The **adversarial-user / friction-log lens** is the synthetic proxy. Use it when
a real human tester isn't available — but prefer the human when you can get one.

## PR readiness after review

Keep the PR in draft until:

- every intended independent reviewer completed;
- the parent validated and triaged the reports;
- the human approved the repair/disposition batch when required;
- approved repairs have regression evidence;
- deferred findings have linked Issues;
- full required gates and repository-owned Actions pass;
- documentation and tracking accounting are complete; and
- the PR contains a public-safe review summary.

Reviewer completion alone does not make the PR ready.

## When NOT to use this skill

| If you need to… | Go to… |
|---|---|
| Fix findings and lock them in, rather than generate them | `agentic-verification-discipline` |
| Decide the development loop — phases vs. hardening passes, living specs | `agentic-phase-workflow` |
| Manage human checkpoints and slice cadence | `agentic-collaboration-cadence` |
| Control the cost of the whole workflow, not just reviewer tier | `agentic-session-economics` |
| Turn a review hunch into an adopted practice | `agentic-workflow-evolution` |
| Store reviewer briefs, false-alarm lists, and handoffs across sessions | `agentic-project-memory` |
| Stand up this whole system on a new project | `agentic-project-bootstrap` |
| Reach a stable base/head target the implementation doesn't yet have | `agentic-implementation-orchestration` |
| Administer normal PR metadata or comments | Use the available GitHub tooling |
| Review migration inventory completeness | Use the explicitly invoked migration workflow |

A project may also carry its own project-specific skill library alongside these
portable ones.
