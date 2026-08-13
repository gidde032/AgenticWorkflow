# Docs and GitHub migration — worked examples and provenance

Evidence behind the migration workflow in `SKILL.md`. This skill was promoted
out of an experiments directory after completing the containment path described
in `agentic-workflow-evolution` §10, so its provenance is worth stating plainly.

## Contents

1. What validated this workflow
2. Why the ledger is fingerprinted
3. Why the checkpoint budget is three
4. Provenance and maintenance

## 1. What validated this workflow

Two completed real-repository migrations, on separate solo-maintained projects,
each taking a repository with scattered planning documents and little GitHub
governance to consolidated documentation authorities plus Issues, milestones,
and a draft PR.

The first established the shape: reality-audit before trusting narrative,
complete inventory before any write, one evidence-backed disposition per
finding, and a local-only ledger with a public-safe summary in the PR. The
second repeated it without discovering a new phase, which is the observation
that moved the skill from contained experiment to promoted workflow — a
repeatable run, not a successful one.

Both were solo-maintained. That is the origin of the solo-maintainer constraint
rather than a conservative guess: no multi-maintainer repository has been
migrated with this workflow, so nothing is known about how its checkpoints
behave when "the human approved the profile" has more than one possible
referent.

## 2. Why the ledger is fingerprinted

The failure this defends against is an agent that reports having read a source
it only remembered reading. Every other gate in the ledger can be satisfied by a
plausible-looking entry — a finding ID, a status, a rationale — written from
recollection.

Recomputing the SHA-256 from disk is what turns invariant 1 ("read repository
reality before trusting narrative or session memory") from a promise into
something enforceable. An agent that skipped a source can write a convincing
digest; it cannot write one that matches the file.

## 3. Why the checkpoint budget is three

Migration is long and almost entirely mechanical once the profile is ratified.
An agent that checkpoints at every reversible step converts a bounded operation
into an approval queue, and the human stops reading the checkpoints carefully —
which defeats the two that actually matter.

The three that survive are the ones where a wrong answer is expensive:
ratifying the profile (before any write), an exceptional prerequisite (where
repository state contradicts the plan), and the final draft-PR review (before
anything becomes public). Everything else was pre-authorized by the ratified
profile.

## 4. Provenance and maintenance

Validated by two completed real-repository migrations on separate
solo-maintained projects, plus the bundled validator fixtures
(`scripts/run_fixtures.sh`, 14 cases) which assert an exact exit code per case,
so a gate that silently stops enforcing fails as loudly as one that starts
over-rejecting.

This skill was developed in a contained experiments directory and promoted by an
explicit human decision once the second migration completed. It remains
explicit-invocation-only after promotion — not because it is unproven, but
because its finite-use shape means an implicit trigger could only ever be a
false positive.

Update this skill when:

- A migration encounters a repository condition the profile schema cannot
  express.
- A validator gate proves either too strict to complete a real migration, or too
  loose to catch a skipped source.
- GitHub changes Issue, milestone, ruleset, or required-check behavior in a way
  that alters what `execute` mode can configure.
- A multi-maintainer case is deliberately attempted, which requires revisiting
  the solo-maintainer constraint in both the prose and
  `scripts/validate_profile.py` together.

Record observed friction and named failure modes from a completed migration
through `agentic-workflow-evolution`, not here.
