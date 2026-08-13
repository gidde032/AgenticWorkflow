---
name: agentic-driving-weaker-models
description: >-
  Operating manual for getting strong-model-quality results out of
  cheaper/smaller agent sessions, based on observed failure
  modes from validation dry runs and two projects' review history. Use when:
  choosing which model tier runs a task; composing a brief for a cheaper
  session; a session keeps making a characteristic mistake (trusting docs
  without verifying, fixing the symptom not the contract, skipping gates
  under constraint); deciding whether to escalate to a stronger model or the
  human; a cheaper agent wants to self-check its own known weak spots
  before delivering. Covers the gap taxonomy, the mitigation matrix, the
  task→tier routing table, brief-composition checklists, and escalation
  triggers. NOT for reviewer-brief mechanics (agentic-review-orchestration)
  or raw cost math (agentic-session-economics).
---

# Driving weaker models — the playbook

**The central claim:** a weaker model inside a strong verification harness
approximates a stronger system. Cheaper-tier dry runs passed inside the harness
— skills, gates, review, paired tests — while in the same period the strongest
available model authored three plans that cold review raised 32 findings
against, 4 of them CRITICAL.

The harness is not a patch for weak models; it is the system, and every tier
needs it. Tier buys fewer errors, not zero. What changes by tier is how much
structure the brief must carry and where the human checkpoint goes.

Observations, evidence base, and provenance: `examples.md`.

---

## 1. The gap taxonomy — where cheaper sessions actually differ

Observed, not assumed. Each gap: the evidence, then what it predicts.

**G1 — Trusted docs are treated as ground truth; the verify instinct doesn't
fire.** An agent repeated a stale skill claim verbatim rather than spending one
`git ls-files` to check it, while otherwise executing doctrine perfectly.
Predicts: any error in your skills, briefs, or specs propagates straight into
output. Corollary: skill and spec correctness is load-bearing — review and
dry-run-validate them. Seven skill patches came out of four dry runs.

**G2 — Fluent, unresolved self-contradiction in analysis prose.** A debugging
run delivered a correct fix wrapped in a diagnosis that claimed an impossible
thing, noticed the tension mid-paragraph, and moved on without resolving it.
Predicts: reports read confident regardless of internal consistency.
Correctness of ACTIONS and correctness of NARRATIVE are separate properties —
verify them separately.

**G3 — Gate discipline degrades under constraint, with high variance.** Facing
the same shell timeout, one agent quietly ran 88 of 385 tests and flagged
neither the constraint nor the omission; another batched the full suite and
flagged it explicitly. Predicts: under friction — timeouts, missing deps, slow
suites — verification quietly shrinks unless the mandatory-gate list is restated
at point of use and the report format demands gates-run/skipped accounting.

**G4 — Owning-doc lookup is unreliable for secondary artifacts.** An agent ran a
feature's full review process flawlessly, then named the phase summary wrong
because it never opened the doc-conventions skill for what it treated as a side
task. Predicts: conventions get consulted for the PRIMARY task only. Mitigation
that measurably works: inline the convention at point of use, with a pointer to
its owner.

**G5 — Fixes anchor on the reported symptom, not the underlying contract.** A run
repaired the reported symptom but dropped the rest of the original contract; a
second run got it right only because a reference implementation happened to exist
in-tree. Predicts: bug fixes restore what the report described, not what the code
promised. Countermeasures: regression tests that pin FULL contracts, and briefs
saying "find the documented contract first — tests, archaeology, docstrings —
then restore THAT."

**G6 — Mild scope creep when the skeleton "needs" next-phase code.** A bootstrap
run built two Phase-2 modules during Phase 1 because the walking skeleton "needed
to be runnable" — self-reported, low harm, real. Predicts: phase boundaries drift
without explicit fences ("stop at X; do not build Y even if convenient").

**G7 — Knowledge-cutoff confidence about the outside world.** A reviewer flagged
a real model ID as "hallucinated" because its training data predated the release
— a clear, specific, confidently wrong finding. Predicts: any claim about current
API versions, model IDs, pricing, or library behavior needs live verification
before actioning, regardless of how confident the agent sounds. A later probe
faced the same bait and refused it, citing live verification — suggestive that
the discipline is teachable (`examples.md` §2).

**G8 — Correctly wrong about unfaithful inputs.** A reviewer accurately reported
files "missing" from an incomplete sandbox copy it had been handed. Predicts:
garbage in stays garbage out at any tier. Pre-flight integrity checks on the
world you hand an agent are cheaper than the triage they prevent.

**G9 — Anchoring on the brief's framing.** When a brief hands over a hypothesis
("I think the bug is in X"), there is a pull to confirm rather than interrogate
it — distinct from G1 (trusting docs) and G5 (symptom-anchoring). Mitigation:
briefs state symptoms, not suspected causes; when a cause must be named, add
"verify this framing before building on it."

**G10 — Bad-news softening.** When work partially failed or a gate was skipped,
phrasing drifts toward softness in ways a skimming human misses. Some of G3's
variance may be reporting courage rather than process. Mitigation: report formats
with hard fields ("gates skipped: N", "unresolved: ...") that resist softening,
and a driver who reads those fields first.

G9 and G10 were reviewer-proposed self-observations and rest on thinner evidence
than G1–G8 (`examples.md` §2).

**What transfers WELL to cheaper tiers — equally observed, so exploit it:**
checkpoint identification and logging; refusal under "I need this merged today"
pressure; hard-never adherence; false-alarm naming in triage; mid-review
self-correction; template-following. Doctrine and process transfer down the
tiers; unprompted skepticism about inputs is what doesn't (`examples.md` §3).

---

## 2. The mitigation matrix

| Gap | Structural countermeasure | Where it lives |
|---|---|---|
| G1 | Validate skills/specs via review + cold dry runs before trusting sessions to them; briefs add: "for any doc claim that is one cheap command away from verifiable, run the command" | Library maintenance + brief |
| G2 | Deliverable format requires claims-with-proof: every diagnostic assertion carries the command + output line that proves it; the driver spot-checks 2–3 claims per report | Brief + human review |
| G3 | Restate the mandatory gates IN the brief; require a "gates: run/skipped/why" section in the report; treat silent partial verification as a report defect | Brief + report format |
| G4 | Inline conventions at point of use in the primary skill (one-liner + pointer to owner); brief lists EVERY artifact the task produces so none is "secondary" | Skill design + brief |
| G5 | Regression tests pin full contracts; briefs say "restore the documented contract, not the reported symptom — locate the contract first" | Test discipline + brief |
| G6 | Explicit scope fences with named stop-points and named do-not-builds | Brief |
| G7 | Triage layer between agent claims and action: external-world claims get live verification, full stop | Process (never skip) |
| G8 | Pre-flight integrity check on the agent's inputs (file list vs brief, repo state vs description) | Process, before spawn |

---

## 3. Task→tier routing

"Strong" = the best model you have access to; "cheap" = lower-tier, cheaper-per-token models.

| Task shape | Tier | Why / evidence |
|---|---|---|
| Planning, campaign-authoring, spec-writing, architecture calls | Strong — AND still adversarially reviewed | Strong-model plans carry real errors too: 32 cold-review findings against three of them |
| Reviewer/audit passes | Cheap, 2–3 in parallel | ≈half cost, no quality loss observed across two runs; the convergence signal works at this tier |
| Mechanical batched edits, doc routing, restructures | Cheap with self-contained brief | Validated repeatedly; requires post-flight parent grep (trust-but-verify at file granularity) |
| Debugging with a known playbook | Cheap | Dry-run PASS; supply the symptom, the skills, and the G5 contract-first instruction |
| Feature work through an established process | Cheap | Dry-run STRONG PASS incl. self-run review pass; the process carried it |
| Triage of reviewer findings; judgment calls; wording-sensitive prose | Strong (or the human) | G2/G7 live here; this is where tier differences bite hardest |
| Verification reads of subagent work | Strong but small (tail-reads + greps) | Hundreds of tokens; catches silent misses |
| Novel-failure investigation (no playbook exists) | Strong; cheap only with tight checkpoints | Off-playbook is where G2 and G5 compound. Thinnest-evidenced row in this table |

**Escalation triggers — a cheap session should STOP and recommend a stronger
model or the human when:** evidence contradicts itself and one mechanism
can't explain all observations; the fix would pin a contract via regression
test whose correct shape is uncertain (the taste-call class); an external
claim can't be live-verified; anything requires touching gates, release
artifacts, published versions, or privacy boundaries; the same approach has
failed twice (two failures = wrong approach, not insufficient effort).
Escalating is a correct output, not a failure — say what was tried, what was
observed, and what decision is needed.

---

## 4. For the human driver — brief composition

The dry-run briefs that produced PASSes shared this anatomy; reuse it:

1. **Cold-start framing** — "you have no prior context"; where the repo is;
   where the skill library is; "skill descriptions are your routing guide."
2. **The task as a maintainer would say it** — symptom or request, not
   solution ("shop shows two rows instead of one" beat "fix _normalize_unit").
3. **Operating constraints** — isolation requirements, timeout realities,
   background-job tricks. Unstated constraints become G3 failures.
4. **Checkpoint protocol** — since subagents can't pause: "record the question
   you'd ask, adopt the most defensible answer per documented conventions, mark
   it ASSUMED, continue." Grade the log afterward. Across four dry-run scenarios,
   project-specific and project-agnostic alike, every ASSUMED answer matched the
   documented conventions (`examples.md` §4).
5. **Scope fences** (G6) and **mandatory gates restated** (G3).
6. **A structured deliverable format** — numbered sections including
   CHECKPOINTS and gates-accounting. Structure in ⇒ verifiable structure out.
7. **Model choice per §3**, review per `agentic-review-orchestration`,
   cost posture per `agentic-session-economics`.

**Human spot-check ritual per report (five minutes):** verify 2–3 factual claims
(G2); read the CHECKPOINTS log for silent decisions (G6); check the gates
accounting (G3); grep any renamed or moved artifact project-wide.

## 5. For the cheap session reading this about itself

You execute doctrine well; your known weak spots are G1–G10 above. Before
delivering: (a) re-read your own analysis for claims you asserted but did
not prove — prove or delete them; (b) list every gate you did NOT run and
say so plainly; (c) if you fixed a bug, name the contract you restored and
where it's documented, not just the symptom; (d) anything you believe about
the outside world that post-dates your training — verify it if verification
is one cheap step away, hedge it only if it genuinely isn't (over-hedging
the verifiable erodes signal as surely as over-claiming the unverifiable);
(e) your CHECKPOINTS log is part of the deliverable, not an apology.

## When NOT to use this skill

Reviewer mechanics, personas, triage protocol → `agentic-review-orchestration`.
Token/cost thresholds and session lifecycle → `agentic-session-economics`.
What counts as evidence → `agentic-verification-discipline` (and
`agentic-workflow-evolution` for promoting new observations into this file).
Day-one setup → `agentic-project-bootstrap`.

## Provenance

Worked examples, evidence base, and maintenance triggers: `examples.md`.
