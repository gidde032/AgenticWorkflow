---
name: agentic-decision-challenge
description: >-
  Grill, pressure-test, stress-test, poke holes in, challenge, or sanity-check a
  decision the user is about to commit to. Trigger on any such request — including
  bare ones like "grill me on this", "poke holes in this", "am I missing anything",
  or "help me think through this" — for a medium-to-large plan, architecture,
  workflow, or product decision, or when a consequential decision is going
  unchallenged. Runs a dependency-tree, one-question-round-at-a-time interrogation,
  records the ratified decision at the gate, and stops there without authority to
  act. Not for trivial decisions, deciding what to build from scratch (product
  discovery), reviewing a diff, or merely filing a decision already made (that is
  project-memory).
---

# Agentic Decision Challenge

A structured interrogation that sharpens one already-proposed decision. It does
not decide *what* to build (that is
`agentic-product-discovery`) and it does not grant permission to act — it makes a
decision more defensible by exposing what was silently assumed, then stops at a
gate and hands the ratified understanding back to the workflow that owns the next
step.

Worked example, the eight forward-test scenarios, and provenance: `examples.md`.

This skill is a plugin-native rebuild of the frontier/decision-tree mechanism
from Matt Pocock's MIT-licensed `grill-me` / `grilling` skills, adapted to this
plugin's stricter authority and evidence rules. See `examples.md` for attribution.

---

## When it runs

Reach for it readily on a **medium-to-large** decision — one whose cost of being
wrong is more than a quick redo. Any of these is a valid entry:

- The user asks for it: "grill me on this", "poke holes in this plan",
  "pressure-test this architecture", "am I missing anything here",
  `$agentic-decision-challenge`.
- You are about to help commit to a consequential plan, architecture, workflow
  change, or product decision that has **not** been scrutinised. Offer the
  challenge before the decision hardens.

Do **not** run it on trivial or easily-reversible decisions — a variable name, a
one-line default, a choice that costs seconds to change. Interrogating those is
the interview-fatigue failure this skill is built to avoid.

---

## The loop

### 1. Frame exactly one subject

State the single decision under challenge in one sentence, and the outcome that
makes it *settled*. One subject per session. If the user hands you a bundle
("grill our whole Q3 architecture"), narrow it to the one decision that matters
most or split it — see **Bounded scope** below. Do not silently grill everything.

### 2. Map it as a dependency tree

Every decision branches into the decisions that hang off it. A choice belongs
*below* another when you cannot sensibly answer it until the parent is settled.
You hold this tree; you do not have to draw it for the user, but you must respect
it — asking a child before its parent is the "dependent question asked too early"
mistake.

### 3. Work the frontier in rounds

The **frontier** is every decision whose prerequisites are already settled — the
questions you can ask *now* without guessing at answers you have not heard yet.
Ask the whole frontier in one round, then wait for answers before the next.

Each question is numbered and carries a recommended answer:

```
❓ Q1 — <short title>: <the question, plainly stated>
   a) <option>            — <one-line why>
   b) <option>            — <one-line why>
   ➡️ Recommended: <b, and one line on why it wins>
```

**Option rules — this is load-bearing:**

- Offer only **genuinely reasonable** choices. Every option must be a defensible
  answer, not a strawman.
- **Plain language, no jargon.** If an option needs a glossary, rewrite it.
- **Up to four options, fewer when there are not four good ones.** Two strong
  choices beat four padded ones. Do not invent options to reach a count.
- **Drop dominated choices.** If an option has a clear large downside and a
  clearly better alternative exists, leave it out rather than list it to argue
  against. Mention it in one line only if the user is likely to expect it.
- Always give a **recommended answer** with a one-line reason. A question with no
  recommendation is you offloading the thinking back onto the user.
- Some questions are genuinely open and have no menu — ask them plainly. Do not
  manufacture options for a question that is really "what is your constraint here?"

After each round, the user's answers settle decisions, which pushes the frontier
outward and unblocks the questions that depended on them. Recompute the frontier
and ask the next round. A question whose answer still depends on something open in
this round belongs to a *later* round.

### 4. Find facts yourself; put decisions to the user

**Facts are your job, never the user's.** When a frontier question turns on a fact
you can discover — what the code already does, which library version is pinned,
whether a file exists, what a benchmark says — go find it (read the repo, run a
read-only command, check the docs) instead of asking. Verify it; distinguish what
you *confirmed* from what you *inferred*.

Do not block the whole frontier on one slow lookup. A running investigation is
just an unsettled prerequisite: only the questions *downstream* of it wait — ask
the rest of the frontier now, and fold the fact in when it lands. Subagents are
optional; use direct inspection when that is enough.

**Decisions are the user's.** Put each consequential choice to them and wait. Do
not resolve a genuine judgement call by picking your recommendation and moving on.

### 5. Route the un-discussable out

Some questions cannot be settled by discussion *or* lookup — they need real
research, a spike, or a prototype ("will this query hold at 10× load?"). Name the
question, say why talking about it will not resolve it, and route it to that work.
Do not keep re-asking it in successive rounds, and do not let it silently block the
gate — record it as an open item the decision depends on.

### 6. Stop at the shared-understanding gate

The session is done when the frontier is empty: every branch visited, nothing left
silently assumed. Then:

- **Produce the decision record.** State it compactly: the decision as now settled,
  the assumptions surfaced, the choices the user made, and any items routed to
  research/prototyping that remain open. This block is the durable artifact of the
  session.
- **Persist it before ending — do not leave it to the user to remember.** Offer to
  record the decision, defaulting to yes: *"Record this decision to `<target>`?"*
  Choose `<target>` with `agentic-project-memory`'s source-of-truth map — an
  existing spec/ADR section that governs this decision, else a new ADR, else the
  handoff or owning Issue. Do not invent a decisions log or a placement rule of your
  own; that ownership is project-memory's. On the user's confirmation, **write the
  record into that target yourself** (append with rationale; keep a human confirm so
  nothing lands in a spec silently). If the user declines, leave the record in the
  session output and say where it would have gone.
- **Then stop.** Recording a ratified decision is documentation, not authority to
  act. Do **not** start implementing, write code or other *implementation*
  artifacts, or treat "we agree" as permission to build.
- Hand off the rest: turning the decision into delivery → `agentic-phase-workflow`;
  the authorization envelope for acting on it → `agentic-collaboration-cadence`;
  unresolved *what to build* → back to `agentic-product-discovery`.

---

## Bounded scope

This skill has an appetite, not an unlimited one.

- **One subject per session.** Split a bundle; do not chain-grill.
- **Stop when the frontier empties.** More questions are always *possible*; that is
  not a reason to keep asking. The bar is "nothing consequential left silently
  assumed," not "every conceivable branch enumerated."
- **Narrow an over-broad subject** to its highest-stakes decision, out loud, and
  offer to run the rest separately. Interview fatigue is a failure mode, not a sign
  of thoroughness.
- **No new backlog or source of truth.** The decision record is written into an
  *existing* owner chosen by `agentic-project-memory` (a spec/ADR, the handoff, or
  the Issue); this skill does not invent its own decisions register or placement
  rule.

---

## Scope

- **Supported:** challenging a single proposed plan, architecture, workflow change,
  or product decision before it is ratified or acted on.
- **Excluded:** open-ended "what should I build" discovery; auditing an implemented
  diff; merely filing a decision already made; ordinary planning that is not
  stress-testing a specific choice; any interrogation that has drifted into a
  general chat loop.
- **Record evidence of use:** for a consequential run, note the material assumptions
  exposed, the question/round cost, and whether the decision became more defensible
  — useful when refining the loop.

Promoted from experiment to stable in v3.1.0 after repeated real-world use: the
frontier/rounds mechanism and the reasonable-options rule held up, and the
decision-persistence gate (step 6) was added from that use.

---

## When NOT to use this skill

- **Deciding what to build, build-vs-buy, product scope, or visual direction** —
  `agentic-product-discovery`. This skill sharpens a decision already on the table;
  it does not generate the options space.
- **Auditing an implemented change or a diff** — `agentic-review-orchestration`.
- **Deciding *where* a decision or its rationale lives** — `agentic-project-memory`
  owns the source-of-truth map. This skill *writes* the decision record at the gate,
  but it uses that map to choose the target rather than deciding placement itself.
- **Running the build loop once the decision is made** — `agentic-phase-workflow`.
- **Setting how much authority an agent has or where check-ins go** —
  `agentic-collaboration-cadence`.
- **A trivial or easily-reversible decision** — just make it; grilling it is
  waste.
- **A decision that is really blocked on a fact or a prototype** — do the lookup or
  the spike; do not interrogate around a gap that only evidence can fill.

---

## Provenance

Mechanism origin, MIT attribution, the worked session, and the eight forward-test
scenarios with their pass criteria: `examples.md`.
