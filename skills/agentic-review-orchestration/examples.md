# Review orchestration — worked examples and provenance

Evidence behind the mechanics in `SKILL.md`. Read a section when you want the
case behind a rule, or when deciding whether a default transfers to your review.

The reference project is a Python CLI built across six feature phases. A second
body of evidence comes from the first formal review run on a separate UI product
after a documentation-and-GitHub migration.

## Contents

1. Convergence catches the top bug
2. Where the standing skeptic came from
3. Why lens count grows with infrastructure
4. Non-redundant lenses
5. Persona rotation and prompt drift
6. Correctly wrong about an unfaithful sandbox
7. Reviewer tier economics
8. The user as a full reviewer slot
9. Provenance and maintenance

## 1. Convergence catches the top bug

Across six feature phases, the multi-reviewer pass caught the highest-priority
bug in every phase. In one, both reviewers independently found that the `init`
command used a raw schema-create instead of the migration framework — a defect
that would have broken every future migration.

Neither reviewer was told about the other. Convergence flagged it as the #1
priority without the orchestrator having to adjudicate severity, which is the
whole point: two independent paths to the same defect is materially stronger
evidence than one confident opinion.

As the orchestrating agent put it:

> "Convergent findings — when both agents catch the same issue — are the
> strongest signal that something is genuinely high-priority, because the agents
> arrived from independent paths."

## 2. Where the standing skeptic came from

The rule came directly from the maintainer, mid-project:

> "instead of 2 reviewers, from now on, spawn 3 subagents, and make one of the
> reviewers for each phase take on the personality of a skeptical senior
> engineer, who pushes back on sections of code he feels unsatisfied with or
> uncertain about."

The reviewer count evolved from two to three at that moment, and the skeptic
persona went on to catch the single highest-severity bug in multiple phases.
Three reviewers stayed legible to a single orchestrator at triage time; four was
never tried, so the default is three rather than "more."

## 3. Why lens count grows with infrastructure

Two lenses — spec-drift and user-friction — were the default for two releases. A
third, CI-as-contract, became the new default once CI complexity accumulated: it
caught a release-pipeline gap that had survived two prior two-lens audits.

The extra lens cost roughly a third more audit tokens, which was cheap because
all lenses run on cheaper-tier subagents.

The generalizable lesson is not "use three lenses." It is that as a project's
infrastructure grows, the audit surface should grow to match, and each lens
should correspond to a surface that can drift independently.

## 4. Non-redundant lenses

A two-lens audit converged on exactly one bug and was otherwise entirely
non-redundant. The spec-drift lens found a spec promise that had gone
unimplemented for six releases. The friction lens found a command that dropped a
confused user into a bare usage screen.

Neither lens could have produced the other's findings. That is the evidence for
choosing lenses by *surface that can drift independently* rather than by
severity or seniority.

## 5. Persona rotation and prompt drift

The rotation rule exists because of an observed failure:

> "Reviewer prompts have drifted toward sameness. By Phase 3, the two reviewer
> prompts looked similar enough that the agents had overlapping focus."

Overlapping focus looks like convergence but is not — the reviewers agreed
because they were asked the same question, not because they found the same
defect by independent paths. Sameness kills coverage and inflates confidence at
the same time.

The reference project's specialist library was packaging/distribution,
testing/CI, LLM-API-integration, data-integrity, and UX/CLI-surface. Each phase
pulled the two whose surface it touched — an API phase pulled LLM-integration
plus a privacy specialist. Derive your own the same way: name the specialist
after the surface at risk.

## 6. Correctly wrong about an unfaithful sandbox

In a late phase, a packaging reviewer reported that the license file, config,
and docs were "missing." The report was scrupulously accurate — about the
incomplete temp sandbox it had been handed, into which only changed source files
had been synced. All three files existed in the real repository.

Triage caught it, but only after writing up three "false positives" that were
not false. They were correct reports of an incomplete world.

A one-line pre-flight `ls` against the brief's file list would have prevented
the entire round. This is why sandbox integrity is checked before every spawn
rather than treated as an occasional concern.

## 7. Reviewer tier economics

Running the audit lenses on a cheaper model tier cost roughly half, with no
quality loss observed across two runs. Cheaper-tier reviewers were even observed
self-correcting mid-review — downgrading their own findings after re-reading — a
posture previously seen only on the expensive tier.

Two informal data points is not a controlled benchmark. It is enough to make
cheaper-tier the default for routine audits, and not enough to justify it for a
security-sensitive surface or a high-stakes release without checking the output
quality yourself.

## 8. The user as a full reviewer slot

Hands-on testing by the maintainer caught real bugs in three separate cases that
sandboxed reviewers missed: an environment and native-library failure, a
critical setup bug reproduced by following the quickstart, and an output-path
bug.

All three shared a property — they depended on the real machine, the real
install, or the real filesystem. A sandboxed reviewer cannot reach them by
reading a diff, which is why a human running the actual commands occupies a full
reviewer slot rather than serving as a sanity check.

## 9. Provenance and maintenance

The independent multi-reviewer mechanism, standing skeptic, persona rotation,
hardening lenses, and reviewer-economics observations were derived from the
reference project.

The first formal review on a separate UI product subsequently validated a
three-reviewer cold pass with strict isolation: exact changed-file verification,
governing contracts and exclusions, a severity rubric, file:line evidence,
minimal failing-test ideas, disposable probes, a 500-word cap, a
provisional-ledger boundary, and an explicit approval stop before repairs.

The GitHub draft-PR target, public-safe PR consolidation, Issue-backed
deferrals, and PR-readiness boundary come from the documentation-and-GitHub
migration workflow.

Update this skill when:

- A complete Issue → draft PR → three cold reviewers → approved repair →
  ready-for-merge cycle validates the integrated workflow.
- Excluding handoffs and PR discussion either deprives reviewers of necessary
  contract information or improves independence as intended.
- Parallel background review reduces checkpoints without lowering quality.
- Public-safe consolidation loses useful evidence.
- A meta-review proves useful but is mistakenly counted as independent
  convergence.
- Four reviewers work well, structured returns are adopted, or cheaper-tier
  reviewers show a quality loss under a real benchmark.

Do not delete superseded guidance; record the evolution.
