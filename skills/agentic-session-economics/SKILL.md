---
name: agentic-session-economics
description: >
  Keep agent-session spend proportional to work delivered. Use this skill when:
  planning a new agentic workflow; noticing session costs feel disproportionate
  to output; deciding whether to full-read a large file or use a tail-read;
  weighing the cost consequences of a model tier; deciding when to start a
  fresh session; batching doc updates; setting up cost discipline before a
  project grows; fighting broken tooling in the agent layer. Triggers: "my
  usage is going fast", "why is this session so expensive", "which model should
  this subagent run on", "how do I keep costs down", "when should I
  start a fresh session", "how do I read large files efficiently", "token
  discipline". Defer tier *selection* for a given task to
  `agentic-driving-weaker-models`; this skill owns what a tier choice costs, not
  which tier fits the work. Not for API or product pricing questions.
---

# Agentic Session Economics

Keeping agent-session spend proportional to work delivered.

Worked examples, recorded costs, and provenance: `examples.md`.

## The problem, named honestly

Unmeasured file-loads and unscheduled doc updates silently dominate session
budgets — not the feature code, not the reviewer passes. On the reference
project, doc updates and gitignore checks consumed two sessions' worth of budget
before anyone measured why (`examples.md` §1).

**The general claim:** any artifact that grows monotonically — specs, practices
docs, retrospectives, transcripts — eventually crosses a cost threshold where the
workflow that built it stops being affordable. The response is some combination
of (a) read less of it, (b) push the expensive work to a cheaper tier, or
(c) batch the updates so the cost amortizes. Build the cost knobs in *before*
they are forced on you.

---

## Measure before acting

Before reading a file or starting a multi-step doc update, check the observable
proxies:

| Proxy | How to check | What it signals |
|---|---|---|
| File line count | `wc -l <file>` | >200 lines → consider tail-read; >400 → consider splitting |
| Re-reads of one file in a session | Count loads of the same path | Context isn't holding; the model is substituting re-reads for working memory |
| Compaction events | Harness notices or context-overflow warnings | Session is expensive to continue; a fresh start is likely cheaper |
| Subagent token reports | Whatever your platform surfaces | Reviewer or edit subagents dominating → restructure the brief or tier down |
| Sessions per release | Track against prior releases | Rising count means workflow cost is growing faster than output |

These work on any agent runtime; no platform-specific token meter is assumed.

---

## Capability-based model roles

Route by demonstrated capability and task shape, not by provider or a permanent
model-name hierarchy. A model can occupy different roles as the project changes.

| Role | Economic use | Typical work |
|---|---|---|
| **Orchestrator tier** | Spend where interpretation and reversibility matter most | Spec interpretation, decomposition, architecture, risk, triage, integration, acceptance |
| **Implementation tier** | Bounded reasoning against a frozen contract | Feature packets, targeted tests, local debugging with an established playbook |
| **Mechanical tier** | Deterministic, easily checked throughput | Exact-text edits, formatting, generated updates, doc routing |
| **Reviewer tier** | Independent bounded analysis where multiple perspectives beat one long context | Focused cold reviews and audits |

The strongest available model usually fills the orchestrator role, but that is a
runtime choice, not a vendor rule. Calibrate with actual gate results and escaped
defects. For decomposition and parent acceptance see
`agentic-implementation-orchestration`; for lower-tier failure modes and brief
hardening see `agentic-driving-weaker-models`.

---

## Standing rules

### Rule 1 — Files under ~200 lines: full-read is fine on the orchestrator tier

Reading a short file on the orchestrator tier is negligible cost. The threshold
is a line count, not a topic count — a 180-line file on a complex topic is still
fine to full-read.

### Rule 2 — Files over ~200 lines: tail-read + anchor-edit

*Tail-read* — reading only the bounded region you actually need, rather than
loading the whole body into context.

1. Get the line count first (`wc -l`).
2. Identify approximately where you need to work.
3. Use a bounded read of that region — e.g. `Read(file, offset=N, limit=80)`.
4. Find a unique anchor string near the edit point.
5. Apply the edit against that anchor.

Most agent edit tools require only that the file was read *once* in the
conversation, not that the whole body was loaded (`examples.md` §2). Check your
platform's semantics once, then exploit the boundary.

Files over ~400 lines with a regular update cadence should be split per-topic —
see Rule 7 and `agentic-project-memory` for the file-structure mechanics. The
cost rationale lives here: splitting two docs of ~480 and ~320 lines into 12
files averaging ~70 lines cut per-update read cost roughly 10x.

### Rule 3 — Multi-paragraph insertions or batched edits across large files: delegate to the mechanical tier

When one turn needs to insert a large block, or apply edits at multiple sites
across large files, spawn a mechanical-tier subagent with a self-contained brief:

- Exact text to insert — you write it, the subagent does not draft it.
- Exact anchor strings for each edit site.
- File paths, with line counts where known.
- Style notes ("match the existing register; factual not narrative; no trailing
  summaries").
- Explicit out-of-scope items ("do not touch section X").

Then verify on the orchestrator tier with a small tail-read per touched file —
see "Trust-but-verify at the right granularity."

The working model: **orchestrator thinks, mechanical tier types, orchestrator
verifies.** Mechanical-tier subagents ran these edits at roughly half the token
cost with no observed quality loss (`examples.md` §3). Spot-check
judgment-sensitive prose rather than assuming that result transfers to it.

### Rule 4 — Batch narrative-doc updates to once per release

Each touch of a narrative doc pays the full file-load cost; batching amortizes it
across everything accumulated during the release.

Mid-release, write new lessons to a scratch file, not the destination doc. At
end-of-release, one subagent pass routes them all and clears the scratch file.
The mechanism lives in `agentic-project-memory`; this rule owns the cost
rationale.

### Rule 5 — Reviewer subagents default below the orchestrator tier

Reviewer quality is more sensitive to brief quality than to model tier, because
the reasoning demand is bounded — "find bugs in these files against this rubric"
rather than open-ended. Each brief is self-contained, so reviewer tier selection
is independent of the parent session's tier.

Dual-lens audits at reviewer tier ran at roughly half the orchestrator-tier cost
with no measurable quality loss (`examples.md` §4). Confirm on your own project
before lowering the tier on a high-stakes review; the mechanics are in
`agentic-review-orchestration`.

### Rule 6 — Bounded feature implementation may use the implementation tier; integration stays orchestrator-owned

When product behavior, interfaces, allowed files, and acceptance commands are
already fixed, an implementation-tier agent can own the bounded packet. The
orchestrator keeps decomposition, overlapping surfaces, independent acceptance,
cross-component gates, and final integration.

A vague feature request is not an implementation packet. Resolve it before
tiering down.

Use the work-packet and acceptance loop in
`agentic-implementation-orchestration`, and `agentic-driving-weaker-models` when
the implementer needs extra scope fences, contract-first guidance, or
gate-accounting structure.

---

## Trust-but-verify at the right granularity

A subagent reporting "all anchor matches succeeded first attempt" is being honest
about what it did. It guarantees only that the anchors *named in the brief* were
updated — not that no stale references remain.

After any subagent-driven restructure that renames or moves things:

1. Run a project-wide grep for the old name, path, or reference.
2. Verify the output with a small tail-read — not a full re-read — of each
   touched file.

A "clean" doc-split subagent report still left four stale references that a
parent-side grep caught for a few hundred tokens (`examples.md` §5).

**Verification must sit at a granularity that catches what the subagent's
contract doesn't cover.** Its contract is "the anchors I was given matched."
Yours is "nothing in the project is broken."

---

## Session lifecycle — when to start fresh

Fresh sessions at workflow boundaries beat long threads:

- Compaction cost grows with conversation length — each turn re-encodes a growing
  context window. (*Compaction*: the automatic summarization a runtime applies as
  the context window approaches its limit.)
- Fresh-session warm-up cost is *bounded* by your rules file plus state file. Keep
  each under ~200 lines and warm-up is cheap and fixed. See
  `agentic-project-memory`.

**Three proactive triggers for suggesting a fresh session:**

1. The conversation has already compacted at least once.
2. The active task has shifted to a clearly different surface — you just shipped
   a release and are about to start feature work.
3. You are re-reading the same files because context isn't holding.

Frame it as a recommendation with rationale — name the boundary, the cost trend,
and the bounded warm-up — then let the human decide. Don't insist.

---

## Granularity as a cost lever

Doc cost is a function of file granularity, not project size:

- Under ~200 lines: keep as a monolith.
- Between ~200 and ~400: monitor; split when updates start feeling expensive.
- Over ~400 with regular updates: split into per-topic files.

Splitting is roughly a 5% one-time line increase for a ~10x per-update read
reduction (`examples.md` §6). When narrative artifacts outgrow the threshold, the
response is not to write less — it is to change the granularity. Split mechanics
live in `agentic-project-memory`; this section owns the cost rationale.

---

## Fenced wrong paths

Learn the pattern, not the specific paths. Recorded costs in `examples.md` §7.

| Wrong path | Cost / consequence | Right move |
|---|---|---|
| Fighting broken tooling in place | ~20k tokens on one filesystem deadlock | Isolate the workflow from the broken layer first, then debug |
| Per-batch narrative-doc updates | Two sessions of budget on doc updates alone | Batch to once per release; scratch file mid-release |
| Full-reading large files "to be safe" | File-load cost × every read in the session | Measure the line count first, then tail-read + anchor |
| Skipping post-flight verification | Four stale references survived a "clean" doc split | Project-wide grep for the old name after any rename |
| Edit-spamming one file | Each edit is a read-modify-write through the filesystem bridge | Batch edits; write full new content in one pass |

---

## Workflow improvements as an investment

Tokens spent upfront on workflow infrastructure save more downstream than the
same tokens spent on features. One recorded estimate puts the payback at roughly
3–4 future doc updates plus one reviewer pass — about half a release's work
(`examples.md` §8).

That is the rationale for a "workflow improvements before features" release
shape. Full treatment lives in `agentic-phase-workflow`; this section owns the
cost math.

---

## Promotion protocol for new cost rules

New cost rules meet the same evidence bar as any other workflow practice:

1. **Baseline** — measure current cost before applying the rule (line counts,
   session counts, token reports where available).
2. **Candidate** — apply for one release and observe.
3. **Compare** — did cost drop without quality loss?
4. **Human sign-off** — present the comparison; the maintainer decides.

Full promotion mechanics live in `agentic-workflow-evolution`.

---

## When NOT to use this skill

| Situation | Route to |
|---|---|
| Setting up the multi-reviewer pass and choosing reviewer tiers | `agentic-review-orchestration` |
| Decomposing implementation, assigning ownership, accepting delegated code | `agentic-implementation-orchestration` |
| Hardening a lower-capability brief or applying its escalation triggers | `agentic-driving-weaker-models` |
| Regression tests paired with reviewer findings | `agentic-verification-discipline` |
| File structure of memory docs, scratch files, handoffs | `agentic-project-memory` |
| Human-in-the-loop checkpoints and slice cadence | `agentic-collaboration-cadence` |
| Phase vs. hardening-pass shape, living spec | `agentic-phase-workflow` |
| Turning a cost hunch into an adopted practice | `agentic-workflow-evolution` |
| Day-one project setup including cost infrastructure | `agentic-project-bootstrap` |
