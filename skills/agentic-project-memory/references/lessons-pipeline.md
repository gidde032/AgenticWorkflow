# 4. The Lessons Pipeline

The lessons pipeline is:
`pending-lessons.md` → verified consolidation → catalogue, narrative, FAQ,
operating rule, or remediation Issue.

The scratch file is not a backlog. If an entry describes actionable product or
workflow work, create or link an Issue during consolidation. Keep only the
lesson or rationale in the destination practice document.

### 4a. Pending-Lessons Scratch File

One gitignored file at the project root (`pending-lessons.md`). During a release
cycle, append one-line bullets here instead of opening the destination doc.

**The section structure is the forcing function.** Organizing the file with one
section per destination doc means writing an entry requires deciding which
section it belongs to — which in turn clarifies the lesson even before
consolidation.

**The consolidation pass is also a signal filter.** Entries that do not survive
it were rarely worth writing into the destination document in the first place,
so the scratch file tends to produce higher-signal destination entries than
real-time editing would.

The scaffolding lives in `references/memory-file-templates.md`.

At release or milestone close, run one bounded consolidation pass. Use the
lowest capable tier that can preserve meaning and quotations reliably, or keep
the pass parent-owned when delegation adds overhead.

For each entry:

1. Verify the claim against the repository, delivery record, or incident evidence.
2. Route the durable lesson to its owning document.
3. Create or link an Issue if actionable work remains.
4. Preserve quotations verbatim.
5. Remove the scratch entry only after verifying its destination.
6. Finish with a project-wide search for distinctive text from the migrated entries.

### 4b. FAQ — Second-Time Rule

Create `project-FAQ.md` (gitignored) at the project root.

**Add an entry the second time a question recurs across sessions — not the
first.** Once is a one-off; twice is a pattern worth canonical-referencing.

Format: `## Q: ...` header followed by a one-paragraph answer. Cross-link to
deeper explanations in the catalogue, narrative, or state file rather than
duplicating content here. If an answer grows past a paragraph, it probably
belongs in the catalogue instead.

The FAQ is an index, not an encyclopedia. Its scaffolding lives in
`references/memory-file-templates.md`.

### 4c. Once-Per-Release Batching

Update the catalogue and narrative **once per release**, not once per batch
within a release. Each touch pays the file-load cost; batching amortizes it.
Mid-release additions go to `pending-lessons.md`; the bounded consolidation
pass routes them at release end.

See `agentic-session-economics` for the cost rationale and model-mixing details.

---
