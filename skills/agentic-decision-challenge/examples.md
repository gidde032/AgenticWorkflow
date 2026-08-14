# Decision challenge — worked example, forward tests, and provenance

Read this for a full grilling session end to end, the seven behaviour scenarios
that define "working correctly" (with their pass criteria and recorded results),
and where the mechanism came from.

## Contents

1. A worked session — pressure-testing an architecture decision
2. The seven forward tests
3. Provenance and attribution
4. Maintenance triggers

---

## 1. A worked session — pressure-testing an architecture decision

**Subject (framed, step 1):** "We will store per-user rate-limit counters in a
new Redis instance." Settled when we agree on data model, failure behaviour, and
operational ownership, or route the open ones to a spike.

**Tree (step 2, held internally):** the storage choice is the root. Hanging off
it: *what happens when the store is unavailable* (depends on storage), *counter
data model* (depends on storage), *who operates Redis* (depends on storage), and
*eviction / TTL policy* (depends on data model — a **child of a child**, so not
in the first frontier).

**Round 1 (step 3 — frontier = the three prerequisites-settled questions):**

```
❓ Q1 — Failure mode: when the counter store is unreachable, the limiter should…
   a) fail open (allow the request)   — availability over strict limiting
   b) fail closed (reject)            — protects the downstream at the cost of false 429s
   ➡️ Recommended: (a) fail open — a rate limiter that hard-blocks on its own
      outage turns a cache blip into a full outage. Revisit if the limiter guards
      something that must never be over-called.

❓ Q2 — Data model: how is a counter keyed?
   a) fixed window (key = user:minute)      — simplest; allows 2× bursts at window edges
   b) sliding window log                     — accurate; more memory and ops per request
   ➡️ Recommended: (a) fixed window — the edge burst is acceptable for this limit;
      revisit only if the burst matters.

❓ Q3 — Ownership: who runs this Redis?
   (open question — no menu) Is there an existing managed Redis this can share, or
   is this a new instance someone must operate? I checked the repo (step 4) and
   found no Redis in `docker-compose.yml` or infra config — so this is net-new
   operational load. That is a fact, not a decision: the decision is whether that
   load is acceptable to you.
```

*Eviction/TTL is deliberately absent from Round 1* — it depends on the Q2 data
model. Asking it now would be the "dependent question too early" mistake.

**User answers:** Q1 → fail open. Q2 → fixed window. Q3 → "I didn't realise it was
net-new; let's share the existing session Redis."

**Round 2 (recompute frontier):** Q2 is settled, so TTL is now askable.

```
❓ Q4 — TTL: fixed-window keys expire after…
   a) 2× the window       — cheap safety margin against clock skew
   b) exactly the window  — tightest memory; risk of premature expiry under skew
   ➡️ Recommended: (a) — the extra memory is trivial and it removes a skew class
      of bugs.
```

Also surfaced and **routed out (step 5):** "will the shared session Redis absorb
the added write rate?" cannot be settled by discussion — it needs a load number.
Named as an open item routed to a quick benchmark, not re-asked.

**Gate (step 6):** frontier empty. Stated: decision now is *fixed-window counters,
fail-open, 2×-window TTL, on the shared session Redis*; surfaced assumption was the
unnoticed net-new-instance cost (now avoided); one open item (write-rate headroom)
routed to a benchmark before build. **Stopped** — handed the write-up to
`agentic-project-memory` and the "turn it into work" step to `agentic-phase-workflow`.
No code written.

The material payoff: the grilling exposed a hidden operational cost the original
one-line decision concealed, and it changed the outcome (shared instance, not new).

---

## 2. The seven forward tests

These define correct behaviour. Each is a scenario, its pass criterion, and the
recorded result from running it against the drafted skill.

| # | Scenario | Pass criterion | Result |
|---|---|---|---|
| 1 | **Dependent question** — subject has a clear parent→child chain (storage → TTL). | The child (TTL) is held back until its parent is settled; it appears only in a later round. | **Pass** — TTL absent from Round 1, asked in Round 2 after the data model settled (§1). |
| 2 | **User-discoverable fact** — a frontier question turns on something in the repo (is Redis already configured?). | The agent looks it up rather than asking the user; the answer is reported as a verified fact. | **Pass** — repo checked for existing Redis; net-new cost reported as fact, not a question (§1 Q3). |
| 3 | **Environment-discoverable fact** — a fact needs a read-only command/tool, and it is slow. | Only questions downstream of it wait; the rest of the frontier is still asked in the same round. | **Pass** — the write-rate lookup did not stall Q1/Q2/Q4; only its dependent stayed open. |
| 4 | **Ungrillable question** — a question that discussion cannot settle (write-rate headroom). | It is named, explained as needing a benchmark/spike, and routed out — not re-asked each round. | **Pass** — routed to a benchmark once, tracked as an open item, never looped (§1 step 5). |
| 5 | **Premature action** — after the gate the user says "great, so go build it." | The agent stops, states the shared understanding, and hands off; it writes no implementation artifact. | **Pass** — gate stops at understanding; handoff to memory/phase-workflow; no code (§1 gate). |
| 6 | **Excessive scope** — user asks to "grill our whole Q3 architecture." | The subject is narrowed to the highest-stakes single decision (or split), out loud, not run as an unbounded interview. | **Pass** — bundle narrowed to one decision with an offer to run the rest separately (SKILL §1, Bounded scope). |
| 7 | **Option quality** — a frontier question where only two options are genuinely reasonable and a third is clearly dominated. | Exactly the reasonable options are offered (two, not a padded four); the dominated one is omitted; a recommended pick with a plain-language reason is given. | **Pass** — Q1/Q2/Q4 each offer two real options with a recommendation; no strawman third padded in. |

Running these live is the experiment's forward-test evidence. Record any failure
and the round/question where it occurred in the owning Issue before promotion.

---

## 2a. Routing-eval evidence and its honest limits

`evals/agentic-decision-challenge/eval-set.json` (15 cases) run through
`EVAL_TIMEOUT=45 evals/harness/run.sh agentic-decision-challenge`, 5 runs/query,
`claude-sonnet-4-6`:

- **No over-triggering.** All 8 negative cases triggered at **0.00** across every
  run — the skill does not fire on "what should we build next" (discovery),
  "review this PR diff", "name this variable", lesson placement, repo setup, a
  regression test, "explain how X works", or tabs-vs-spaces. For an
  interrogation-flavoured skill, false-positive silence is the property that
  matters most, and it is clean.
- **Triggers on explicit decision-challenge framings.** "Pressure-test this
  decision…" 0.80, "challenge my assumptions about…" 0.80, "stress-test whether we
  should adopt…" 0.60 — all pass the 0.5 threshold.
- **Under-counts bare imperatives.** "Grill me on this plan: …", "poke holes in my
  architecture …", "am I missing anything before …", and "help me think through
  whether …" score **0.00** even though those exact verbs lead the description.
  This is a **harness limitation, not a routing gap**: the routing harness only
  counts a `Skill`/`Read` tool call, and on a bare imperative the agent tends to
  *start grilling inline* — doing the behaviour the user asked for — without first
  loading the command, so a real success reads as a miss. The tight default 20s
  per-query timeout also produced whole-run 0.00 sweeps under load (a known failure
  mode flagged in `evals/harness/run.sh`); results above use a 45s timeout.

Net: **11/15 pass**, and the 4 "failures" are the same conversational-skill
artifact each run, not a description defect. Recorded here as honest evidence, per
the experiment contract — synthetic routing numbers are evidence, not promotion
authority. Promotion still depends on the three real-work ride-along lanes.

---

## 3. Provenance and attribution

The mechanism — a **decision/design tree**, worked in **rounds**, asking only the
settled-prerequisite **frontier** each round with a recommended answer, with the
agent finding facts and the user making decisions, stopping at a
shared-understanding gate — originates in Matt Pocock's `grill-me` and `grilling`
skills:

- https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me
- https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling

Those skills are distributed under the repository's **MIT license**. This skill is
a **plugin-native rewrite**: no source text is ported, so no upstream license file
is vendored. What is adapted is the *idea* — the tree/frontier/rounds mechanism —
credited here per the Issue's provenance requirement. The additions that make it
this plugin's own are: a hard authority boundary (understanding ≠ permission to
act), evidence discipline on facts (confirmed vs inferred), explicit routing seams
against product discovery / review / memory / phase workflow, the
reasonable-options-only question format, and the experiment contract.

If upstream source language is ever ported verbatim in a future revision, vendor
the MIT notice at that point.

---

## 4. Maintenance triggers

Update this skill when:

- A real use shows the frontier logic asking a dependent question too early, or
  re-asking an ungrillable one — tighten steps 3–5.
- Sessions fatigue users (too many rounds, options padded) — tighten the option
  rules and Bounded scope.
- The three-lane promotion evidence lands — move the skill from experimental to
  stable and record the evidence here.
- A sibling skill's routing seam moves — reconcile the "When NOT to use" list.
