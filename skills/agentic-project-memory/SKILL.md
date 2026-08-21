---
name: agentic-project-memory
description: >-
  Maintain durable project memory and assign each kind of information to one
  authoritative location across sessions, agents, GitHub Issues, milestones,
  pull requests, and source-of-truth repository documentation. Use when creating or updating a
  handoff; deciding whether information belongs in an Issue, PR, spec, roadmap,
  changelog, task file, practices catalogue, retrospective, FAQ, or pending
  lessons; deciding where a deferred idea is recorded; reconciling
  documentation drift; reconciling which documents a completed phase must update;
  preserving session continuity; documenting tooling failures; splitting an
  oversized internal document; or defining documentation-impact accounting.
  Do not use for ordinary GitHub Issue or PR operations that do not affect
  project memory or source-of-truth boundaries, or for writing ordinary
  reference documentation -- a README, API docs, docstrings -- that carries no
  source-of-truth status.
---

# Agentic Project Memory

The portable architecture for keeping a project coherent across sessions,
agents, GitHub delivery cycles, and releases. It separates immediate state,
durable planning, delivery history, public documentation, and workflow
rationale so that no agent must reread several overlapping documents to
discover what is true.

Worked examples and provenance: `examples.md`.

---

## When NOT to use this skill

| If you need… | Go to… |
|---|---|
| Cost and model-mixing strategy | `agentic-session-economics` |
| How to run review passes | `agentic-review-orchestration` |
| Regression tests and quality gates | `agentic-verification-discipline` |
| Human checkpoints and slice cadence | `agentic-collaboration-cadence` |
| Phase structure and living spec | `agentic-phase-workflow` |
| Day-one instantiation on a new project | `agentic-project-bootstrap` |
| Creating, editing, or triaging an ordinary Issue or PR without changing memory boundaries | Use the available GitHub tooling directly |
| Performing a repository-wide documentation and GitHub migration | Use the explicit migration workflow when it has been deliberately invoked; do not infer migration from normal project work |
| Configuring Actions checks or diagnosing CI failures | `agentic-verification-discipline` or the relevant GitHub CI workflow |

---

## 1. The Four-File Memory Architecture and GitHub Delivery Layer

Most projects collapse operating rules, current state, planning, delivery
history, rationale, and narrative into one or two documents. That makes every
update expensive and creates contradictory status claims.

Keep the four memory responsibilities separate, then place actionable planning
and delivery state in GitHub. GitHub is not a fifth memory file: it is the
external planning and delivery layer to which the memory files point.

### The Four Files

| Memory surface | Audience | Content | Update cadence |
|---|---|---|---|
| **Operating rules** | Agent loading the project this session | Current workflow rules, commands, invariants, source-of-truth map, and safety boundaries | Only when a durable rule or command changes |
| **State (`handoff.md`)** | Next fresh agent or session | Active Issue, milestone, branch, PR, blockers, verified state, and exact next command | Whenever active delivery state or the next command changes |
| **Catalogue** | Future agent or human needing rationale | Why a rule exists, with evidence, observed cost, value, and failure modes | When a practice crystallizes |
| **Narrative** | Long-arc reviewers or future writing | How the workflow evolved, what changed, and why | When workflow shape changes |

### The external source-of-truth split

Read `references/github-source-of-truth-contract.md` whenever work creates,
moves, defers, completes, or reports planned work.

The governing rule is **one fact, one authority**:

- Specs and ADRs own approved product and architecture contracts. (`agentic-decision-challenge`
  may write a ratified decision record into one of these targets at its gate; it
  defers *placement* to this skill's source-of-truth map.)
- GitHub Issues own actionable planned work, bugs, deferred findings, and
  unresolved decisions.
- Milestones own committed delivery horizons.
- Pull requests own implementation, review, verification, and merge history.
- `CHANGELOG.md` owns curated user-facing shipped history when the project uses
  versioned releases.
- `ROADMAP.md` may summarize multiple future horizons, but every actionable
  entry links to an Issue.
- `handoff.md` owns only immediate continuity: active Issue, branch, PR,
  blockers, verified state, and next command.
- Optional `TASKS.md` owns only the current session's execution checklist and
  remains gitignored.
- Practices and retrospective documents own evidence and rationale, not backlog
  status.

When two artifacts appear to own the same fact, choose the authority above and
replace the other copy with a link or concise context.

### Memory file templates

Read `references/memory-file-templates.md` when creating a new memory file or
materially restructuring an existing one. Do not load it for ordinary handoff
updates.

The templates are starting shapes, not additional required files. Instantiate
only the files justified by the project's current workflow.

---

## 1a. Documentation and Tracking Impact Contract

Do not let documentation or delivery-state freshness depend on an optional
cleanup step. Before an implementation packet, slice, phase, PR, or release is
called complete:

1. Identify the owning Issue, milestone, branch, and PR, when applicable.
2. Inspect the project's source-of-truth map.
3. Classify what changed: behavior, scope/status, interfaces, commands/config,
   architecture, operations, workflow rules, release promises, or planning
   state.
4. Update each affected authority in the same work boundary. Do not copy the
   same status into multiple documents.
5. Verify commands, examples, links, paths, Issue/PR relationships, and contract
   claims at the cheapest faithful level.
6. Return explicit tracking and documentation accounting:

```text
Tracking impact
- Issue/milestone: <updated state and links, or none with reason>
- Pull request: <updated state and link, or not applicable>

Documentation impact
- Updated: <paths and why, or none>
- Reviewed; no change needed: <paths and why, or none>
- Verification: <checks and results, or explicit limitation>
```

A bare "no docs needed" or "Issue updated" is not accounting. Name the surfaces
reviewed and why they changed or remained correct.

Read `references/github-source-of-truth-contract.md` when work affects planned
or delivered scope. Read `references/documentation-impact-contract.md` when it
affects user behavior, project status, interfaces, commands, configuration,
architecture, operations, releases, or workflow rules.

---

## 2. Handoff Document Discipline

The handoff is the current-state contract between sessions. Update it whenever
the active Issue, milestone, branch, PR, blocker, verified state, or exact next
action changes. It must orient a fresh agent without becoming a second backlog
or changelog.

Write the handoff early enough that it can guide the active slice, then keep it
current as evidence changes. At session close, ensure it points to the exact
next action rather than summarizing the conversation.

**Write the handoff at the start of each phase, not at session end.** Treat it
as the contract for the upcoming phase: if you always know what a fresh agent
would need, you are working from that agent's vantage point and the document
updates as naturally as the code does.

Writing it also surfaces what you have been carrying implicitly — on the
reference project, drafting one exposed two undocumented gaps that should have
been written down earlier (`examples.md` §1).

### Handoff update checklist

- [ ] Active milestone and Issue are linked, or explicitly none.
- [ ] Branch and PR state match GitHub and local Git.
- [ ] Current state distinguishes verified evidence from assumptions.
- [ ] Active files contain only the current slice.
- [ ] Blockers and immediate risks are current; durable work links to Issues.
- [ ] Last completed delivery links to the most recent merged PR/closed Issue.
- [ ] Exact next action names one command or bounded operation.
- [ ] Sanity-check commands are current.
- [ ] No roadmap, general bug backlog, or running changelog has accumulated.

---

## 3. Phase Summaries

A phase summary is optional synthesis, not the canonical delivery record.
GitHub Issues and PRs already own implementation, review, verification, and
closure history.

Create an immutable phase summary when a phase:

- spans multiple Issues or PRs;
- resolves consequential design or architecture decisions;
- produces workflow-experiment evidence worth preserving;
- contains accepted-versus-deferred reasoning that would otherwise be difficult
  to reconstruct; or
- closes a named release horizon needing internal synthesis.

For a focused single-Issue, single-PR slice, the Issue, PR, documentation
accounting, and updated handoff are normally sufficient.

When a summary is warranted, write it after implementation, review, repairs,
and verification. Link the milestone, Issues, and PRs rather than reproducing
their full timelines. Never retroactively rewrite a closed summary; add a dated
correction note when necessary.

### Sections

1. **Goal and horizon**
2. **Delivered outcomes** — links to Issues and merged PRs
3. **Consequential findings and corrections**
4. **Accepted, deferred, and rejected decisions** — deferred actionable work
   must link to an Issue
5. **Workflow evidence and lessons**
6. **Verification and remaining limitations**

### Naming convention

`phase-N.md` for early sequential phases. When the project moves past the initial
phase sequence, use `phase-X-Y.md` where X = version number and Y = chronological
number within that version (e.g., `phase-2-1.md` for v0.2's first feature phase).
This keeps summaries grouped by version in directory listings.

### What phase summaries are for

- **Memory consolidation**: writing forces synthesis of half-formed views
- **Cross-delivery synthesis**: connect several Issues or PRs without duplicating
  their individual timelines
- **Decision rationale**: make future "why didn't we do X?" questions answerable
  without rereading conversation history

---

## 4. The Lessons Pipeline

A lesson enters as a provisional observation and only becomes a practice once
evidence supports it. The stage definitions, promotion criteria, and worked
examples are in `references/lessons-pipeline.md`. Read it when you are moving a
lesson between stages or deciding whether one has earned promotion.

## 5. Tooling Post-Mortems

Treat workflow and tooling failures like production incidents. When something
goes wrong with the environment (not the project code) and burns meaningful
time, write it up.

Most workflows treat tooling friction as ephemeral. Treating it as documentable
is what makes the second occurrence cheap: one filesystem-deadlock incident cost
~20k tokens the first time, a fraction of that the second time once a playbook
existed, and produced a cheaper first move on the third (`examples.md` §3).

The post-mortem template lives in `references/memory-file-templates.md`.

Store the durable mechanism and playbook in the practices catalogue. If
remediation remains, create or link an Issue. Mention the incident in the
handoff only while it actively blocks or threatens the current slice.

The goal is that the next agent encountering the symptom finds the playbook
quickly without turning the handoff into an incident archive.

---

## 6. Lessons Compound Backward

The practices catalogue is not an archive of past pain. It is leverage for future
structural fixes.

Applying a lesson through a structural fix — a fixture, an explicit config, a
project-wide convention — propagates it to every *existing* piece of code, not
just future code. One catalogued lesson about terminal-width fragility became a
`conftest.py` fixture that retroactively repaired tests written months earlier
(`examples.md` §4).

So the argument for keeping the catalogue low-friction is not only defensive
("write the lesson down"). It is offensive: write it down so the next structural
fix can apply it backward across all prior code. Write lessons with low friction
into the scratch file, and write structural fixes alongside lessons rather than
as separate work.

---

## 7. Granularity Management

Doc cost is a function of file granularity, not project size.

### The threshold

| File size | Recommendation |
|---|---|
| Under ~200 lines | Full read is fine; keep as monolith |
| 200–400 lines with occasional updates | Monitor; monolith still acceptable |
| Over ~400 lines with regular updates | Split per-topic with an index file |

### How to split

1. Create a directory with the same base name as the file
2. Create `index.md` with a navigation block pointing to each sub-file
3. Move each top-level section to its own file, preserving section numbering
4. Update all cross-references to point at the per-file locations
5. Verify with a project-wide grep for the old file name

Cost summary in one line: roughly +5% lines one-time, roughly 10x per-update
read-cost reduction. The full cost math lives in `agentic-session-economics`
("Granularity as a cost lever") — that skill owns the numbers; this one owns the
split mechanics above.

### Post-split verification

After any subagent-driven restructure that renames or moves files, the parent
runs `grep` for the old file name across the project as a separate verification
step. Do not rely on the subagent's "anchor matches succeeded" report — that
confirms the anchors named in the brief were updated, not that no stale
references remain elsewhere.

---

## 8. Hygiene Rules

### Classify documentation visibility deliberately

At bootstrap, classify every project-memory document as either:

- **Repository-visible** — safe and useful to contributors or users; tracked in
  Git; or
- **Internal continuity** — contains session details, private paths, unpublished
  plans, agent notes, profiles, ledgers, or sensitive context; ignored in the
  same commit in which it is created.

Do not assume every operating-rules file must be private, and do not assume it
is safe to publish. Decide from its contents and the approved project profile.

Migration profiles, complete disposition ledgers, raw continuity notes, and
private audit evidence remain local-only. Only a deliberately written
public-safe summary belongs in an Issue or PR.

Public documentation such as `README.md`, `CONTRIBUTING.md`, `LICENSE`,
conditional `CHANGELOG.md`, and conditional `ROADMAP.md` remains tracked.

**Never delete catalogue entries, even when superseded.** Add a note that
the practice was revised, but keep the original entry. The article series (or
any future reader) wants the evolution, not just the final state. From the
corpus:

> "Don't delete earlier entries — the article wants the evolution, not just the
> final state."

**Verbatim quote preservation.** When the narrative doubles as writing source
material, preserve quotes exactly. Paraphrasing loses the texture that makes
a quote quotable. Use block-quote formatting with attribution when capturing
something worth reproducing.

**Machine memory vs. in-repo files.** Cross-session facts about the user —
preferences, cost posture, collaboration style — belong in the agent platform's
memory layer. Project-specific facts — file paths, schema invariants, active
delivery state — belong in the state file or the owning contract. The split keeps
the operating-rules file short and the platform memory useful across projects
(`examples.md` §5).

---

## 9. Day-One Minimal Memory Set

Before implementation begins, establish:

1. **Operating rules** — project goal, source-of-truth map, workflow shape,
   gates, safety constraints, and authority boundary.
2. **Handoff skeleton** — active delivery fields, verified state, next action,
   and sanity checks.
3. **Empty `pending-lessons.md`** — internal scratch scaffolding only.
4. **Visibility and ignore decisions** — internal files ignored immediately;
   repository-visible files tracked intentionally.

GitHub repository structure, initial Issues, milestone, CI, and the first draft
PR are sequenced by `agentic-project-bootstrap`; they are not additional memory
files.

Do not create the catalogue, narrative, FAQ, changelog, roadmap, or phase-summary
directory without a present need:

- Catalogue: first practice worth preserving.
- Narrative: first meaningful workflow revision.
- FAQ: second recurrence of a question.
- `CHANGELOG.md`: versioned project needing curated release history.
- `ROADMAP.md`: multiple meaningful planning horizons.
- Phase summaries: a phase meeting the synthesis criteria in Section 3.

**Full instantiation checklist lives in `agentic-project-bootstrap`.** Point
there for the step-by-step setup procedure.

---

## Reference: What Goes Where

The full placement table — every artifact type mapped to its single
authoritative location — is in `references/what-goes-where.md`. Read it whenever
you are unsure where a piece of information belongs; that lookup is the most
common reason to consult this skill at all.

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
