# Implementation orchestration — worked examples and provenance

Evidence behind the orchestration loop in `SKILL.md`. This skill is younger than
its siblings and carries correspondingly less evidence: it was synthesized from
the surrounding disciplines and then exercised on one implementation phase, so
most of its rules are derived rather than measured.

## Contents

1. Mixed ownership in a shared file
2. Why the parent audits the workspace, not the report
3. Provenance and maintenance

## 1. Mixed ownership in a shared file

A phase produced approved implementation changes in a file that also contained
the user's own in-progress edits. Committing the whole worktree would have swept
unrelated work into the packet's commit; refusing to touch the file would have
blocked the packet.

The resolution that worked was hunk-level: the parent inspected the diff hunk by
hunk, staged only the hunks tracing to the accepted contract, and left the user's
changes in the working tree. That is why integration stays parent-owned whenever
approved and user-owned changes share a file, and why implementers do not stage
or commit by default — their edits stay visible on the filesystem for the parent
to select from.

## 2. Why the parent audits the workspace, not the report

An implementer's report is a claim about what it did. The workspace is what
actually happened, and the two diverge in ordinary ways: generated files the
implementer did not think to mention, a gate quietly skipped under a timeout, a
rename that left stale references outside the packet's named files.

The specific case that motivates auditing after an interruption: a timed-out
agent has usually already written something. Spawning a replacement from the
original brief without inspecting the filesystem first can duplicate or corrupt
partial work — the replacement assumes a clean base that no longer exists.

## 3. Provenance and maintenance

The initial version was synthesized from the surrounding phase, review,
verification, cadence, economics, and weaker-model disciplines, then exercised on
one UI product's first implementation phase.

The GitHub authority split, pre-authorized mechanical continuation, separation of
migration and product commits, the internal-document boundary, and the
distinction between "development ready" and "implementation authorized" were
reinforced by two documentation-and-GitHub migrations. The same work supplied the
hunk-level preservation evidence in §1.

The orchestration sequence has been exercised across fewer complete
Issue-backed phases than the review or verification disciplines. Expect its
details to move as more phases measure packet outcomes, integration defects,
escaped scope, interruptions, and parent-verification catches.

Update this skill when:

- Compact packets save effort without increasing rebriefs or escaped scope.
- Packet-to-Issue mapping creates too much duplication, or improves traceability.
- Parent-owned hunk staging preserves mixed work reliably.
- Draft-PR updates improve visibility without creating noisy commit history.
- A complete post-migration phase validates or falsifies the named sequence.
