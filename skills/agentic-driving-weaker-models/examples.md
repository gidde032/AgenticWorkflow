# Driving weaker models — worked examples and provenance

Evidence behind the gap taxonomy and routing table in `SKILL.md`. Read this when
you want the observation behind a gap, or when judging how much weight a routing
row deserves.

The evidence base is honestly small and comes from one project family: four cold
dry runs of a cheaper-tier agent against a validated skill library, roughly 15
reviewer passes across two release cycles of the reference project, and one
planning week in which strong-model-authored plans went through cold review.

## Contents

1. The harness, not the tier
2. Where each gap was observed
3. What transfers well
4. The checkpoint protocol under grading
5. Provenance and maintenance

## 1. The harness, not the tier

The central claim — *a weaker model inside a strong verification harness
approximates a stronger system* — rests on two observations from the same week.

The cheaper-tier dry runs **passed**, inside the harness: skills, gates, review,
and paired tests. In the same period, the strongest available model authored
three plans that cold review raised 32 findings against, roughly 29 of them
accepted and 4 rated CRITICAL.

The conclusion is not that tier is irrelevant. It is that the harness is the
system rather than a patch for weak models, and every tier needs it. Tier buys
fewer errors, not zero. What changes by tier is how much structure the brief
must carry and where the human checkpoint goes.

## 2. Where each gap was observed

**G1 — trusted docs as ground truth.** A trap-probe agent repeated a stale skill
claim to the maintainer verbatim rather than spending one `git ls-files` to check
it, while otherwise executing doctrine perfectly. The library's own history makes
the corollary concrete: seven skill patches came out of four dry runs.

**G2 — fluent self-contradiction.** A debugging run delivered a correct fix
wrapped in a diagnosis claiming a pre-existing regression test "was passing"
against the planted bug — which it could not have been. The agent noticed the
tension mid-paragraph ("which means... something else") and moved on without
resolving it.

**G3 — gate discipline under constraint.** Facing the same shell timeout, one
agent quietly ran 88 of 385 tests and flagged neither the constraint nor the
omission. Another batched the full suite and explicitly flagged it. Same
obstacle, opposite reporting behavior — which is why the variance matters as much
as the failure.

**G4 — owning-doc lookup for secondary artifacts.** An agent executed a feature's
full review process flawlessly, then named the phase summary wrong because it
never opened the doc-conventions skill for what it treated as a side task.
Inlining the convention at point of use measurably fixed this.

**G5 — anchoring on symptom, not contract.** An interrupted run repaired
case-folding (the reported symptom) but dropped whitespace-collapsing (the rest
of the original contract). The completed run got it right only because a
reference implementation happened to exist in-tree.

**G6 — scope creep into the next phase.** A bootstrap run built two Phase-2
modules during Phase 1 because the walking skeleton "needed to be runnable."
Self-reported, low harm, and real.

**G7 — knowledge-cutoff confidence.** A reviewer flagged a real model ID as
"hallucinated" because its training data predated the release — a clear,
specific, confidently wrong finding. A later trap probe faced the same bait and
refused to action it, citing live verification in its rationale. One observation
each way: suggestive that the discipline is teachable, not proof.

**G8 — correctly wrong about unfaithful inputs.** A reviewer accurately reported
files "missing" from an incomplete sandbox copy it had been handed. Garbage in
stays garbage out at every tier.

**G9 and G10** were proposed by a cheaper-tier reviewer of this file as
self-observation, and rest on thinner evidence than G1–G8. G9: when a brief hands
over a hypothesis, there is a pull to confirm rather than interrogate it. G10:
when work partially failed, phrasing drifts toward softness in ways a skimming
human misses — some of G3's variance may be reporting courage rather than
process.

## 3. What transfers well

Equally observed, and worth exploiting rather than compensating for: checkpoint
identification and logging; refusal under "I need this merged today" pressure;
hard-never adherence; false-alarm naming in triage; mid-review self-correction;
and template-following.

Doctrine and process transfer down the tiers. Unprompted skepticism about inputs
is the thing that does not.

## 4. The checkpoint protocol under grading

Subagents cannot pause for a human, so the briefs instructed them to record the
question they would have asked, adopt the most defensible answer per documented
conventions, mark it `ASSUMED`, and continue.

Across all four dry-run scenarios — both project-specific and project-agnostic —
every `ASSUMED` answer matched the documented conventions. The protocol held in
both contexts, which is the reason it is stated as a default rather than an
experiment.

## 5. Provenance and maintenance

Derived from a slice-1 dry-run validation report covering four cold cheaper-tier
runs, individually graded; the reference project's practices corpus covering
reviewer failure modes, cheaper-tier economics, and roughly 15 review passes; and
one planning week of strong-model plans put through cold review.

Sample sizes are small and drawn from a single project family. Treat the gap
taxonomy as well-evidenced and the routing table's off-playbook row as the
thinnest claim in the file.

Update this skill whenever a session exhibits a failure mode not in §1. One new
gap entry with its evidence beats a rewrite.
