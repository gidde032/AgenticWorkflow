# Session economics — worked examples and provenance

Evidence behind the rules in `SKILL.md`. Read a section when you want the
measurement behind a rule, or when deciding how far a number generalizes to your
own project.

The reference project is a Python CLI built across six feature phases and
several hardening passes. Its numbers are recorded project history, not
controlled benchmarks — treat them as order-of-magnitude evidence.

## Contents

1. The observation that started the practice
2. Tail-reads and edit-tool semantics
3. Delegating mechanical edits to a cheaper tier
4. Reviewer tier and brief quality
5. Verification granularity after a subagent restructure
6. Granularity as a cost lever
7. Fenced wrong paths in detail
8. Workflow improvements as an investment
9. Provenance and maintenance

## 1. The observation that started the practice

Mid-cycle, the maintainer interrupted a session:

> "the git repo is good, why are you killing my usage so fast? i didn't think
> that the doc updates and checking my gitignore changes would take 2 sessions
> worth of usage"

The diagnosis was straightforward. Two narrative docs had grown large enough
that each full read on the expensive tier consumed a non-trivial share of the
per-session budget, and the workflow updated both after *every* batch. Each
batch paid the full file-read cost twice, even when the actual edit was a few
lines.

Nothing about the feature work was expensive. The cost was entirely in unmeasured
file loads and unscheduled doc updates — which is why the rules in this skill
target reading and update cadence rather than implementation.

## 2. Tail-reads and edit-tool semantics

Most agent edit tools require only that a file was read at least once in the
conversation, not that the whole body was loaded into context. On the reference
project, the Edit tool required one read anywhere in the session to unlock edits
anywhere in the file.

That boundary is what makes tail-read plus anchor-edit work. Check your own
platform's semantics once, then exploit it.

## 3. Delegating mechanical edits to a cheaper tier

Across two runs — one 12-file documentation split, one multi-section
retrospective update costing roughly 117k tokens on the subagent side —
lower-class subagents executed mechanical edits at approximately half the token
cost of high-class, with no quality loss the maintainer could observe.

Two runs is not a controlled benchmark. The result is strong enough to act on
for mechanical work with exact anchors supplied, and weak enough that
judgment-sensitive prose deserves a spot check before you trust it.

## 4. Reviewer tier and brief quality

An end-of-version dual-lens audit ran on lower-class reviewer-tier subagents at
roughly half the previous release's token cost, with no measurable quality loss
in the maintainer's assessment.

The likely mechanism: each reviewer brief is self-contained — a fresh agent needs
the brief, the file paths, and a length cap, not conversation history. The
reasoning demand is bounded ("find bugs in these files against this rubric")
rather than open-ended, so reviewer quality tracks brief quality more closely
than it tracks model tier. That also makes reviewer tier selection independent of
the parent session's tier.

## 5. Verification granularity after a subagent restructure

A documentation-split subagent reported that every anchor match succeeded on the
first attempt. The report was accurate. A parent-side project-wide grep then
found four stale references the brief had never named — two in the operating-rules
file, two in the contributing guide.

Verification cost a few hundred tokens. A silent miss would have cost thousands
to diagnose later, after the stale paths had been copied forward.

The subagent's contract was "the anchors I was given matched." The parent's
contract is "nothing in the project is broken." Those are different claims, and
only the second one is what you actually need.

## 6. Granularity as a cost lever

Two narrative documents of roughly 480 and 320 lines were expensive to read on
the orchestrator tier. Split into 12 files averaging about 70 lines each,
per-update read cost fell roughly 10x, because a typical update then touched one
or two files instead of loading the whole corpus.

Total line count rose slightly — index files and per-file headers add about 5%.
The one-time restructuring cost was recovered within a single release.

The transferable point: when narrative artifacts pass the comfort threshold, the
response is not to write less. It is to change the granularity.

## 7. Fenced wrong paths in detail

**Fighting broken tooling in place.** A FUSE filesystem bridge between the agent
sandbox and the host workspace hit a POSIX deadlock on rapidly-edited files.
Roughly 20k tokens went into in-place recovery. The eventual cheapest fix was
asking the user to re-open the project folder — one user action plus one
reinstall, which cleared the deadlock project-wide by issuing fresh inodes.

The lesson is ordering: when tooling misbehaves, first isolate the workflow from
the broken layer, then debug. Debugging through a broken layer costs more than
stepping around it.

**Edit-spamming one file.** Each edit is a read-modify-write through the
filesystem bridge, and a rapid sequence of them contributed to the deadlock
above. Batch edits, or write the full new content in one pass.

**Per-batch narrative-doc updates.** See §1 — two sessions of budget consumed by
doc updates and gitignore checks.

## 8. Workflow improvements as an investment

Tokens spent upfront on workflow infrastructure saved more downstream than the
same tokens spent on features. The recorded estimate: the bet paid off after
roughly 3–4 future doc updates and one reviewer pass — about half a release's
work.

This is one project's estimate, not a measured curve. It is the rationale behind
scheduling a workflow-improvement pass at the start of a release rather than
deferring it until the cost becomes painful.

## 9. Provenance and maintenance

Derived from the reference project's documented corpus: its operating-rules
token-economics section, handoff notes on working efficiently, the workflow
retrospective's cost revision, and the practices catalogue entries covering FUSE
cost and edit-spamming.

Update this skill when:

- A new cost rule clears the promotion protocol (baseline → candidate → compare
  → sign-off).
- A new project produces a cost pattern the standing rules do not cover.
- Platform pricing or context-window behavior changes enough to move a threshold.

Do not update mid-release; batch to the end-of-release consolidation pass,
consistent with Rule 4.
