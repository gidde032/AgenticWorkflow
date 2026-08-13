# Reference: What Goes Where

The single placement table for this workflow. Every artifact type maps to one
authority; the third column names the failure mode that authority is most often
degraded into.

| Content | Authority | Must not become |
|---|---|---|
| Approved product behavior, scope, boundaries, or numeric budgets | Spec | Backlog or session log |
| Accepted architecture decision and rationale | ADR | Implementation checklist |
| Planned feature, bug, investigation, deferred review finding, or unresolved decision | GitHub Issue | Session transcript |
| Committed release horizon | GitHub Milestone | General idea bucket |
| Implementation, review, verification, documentation accounting, and merge history | Pull request | Unbounded project plan |
| Current active Issue, branch, PR, blocker, and next command | `handoff.md` | Changelog or backlog |
| Current session's mechanical checklist | Optional gitignored `TASKS.md` | Durable project tracker |
| User-facing shipped history | Conditional `CHANGELOG.md` | Commit or PR dump |
| Multi-horizon future direction | Conditional `ROADMAP.md`, linked to Issues | Duplicate Issue tracker |
| Workflow rule an agent follows now | Operating-rules file | Rationale archive |
| Why a rule exists and what evidence supports it | Practices catalogue | Delivery-status authority |
| How the workflow evolved | Narrative/retrospective | Delivery-status authority |
| One-line mid-cycle lesson | `pending-lessons.md` | Backlog |
| Recurring question after its second occurrence | FAQ | Encyclopedia |
| Tooling failure mechanism and playbook | Practices catalogue | Handoff incident archive |
| Unresolved tooling remediation | GitHub Issue | Handoff note |
| Active tooling blocker | Handoff, linked to the Issue | Durable incident record |
| Multi-Issue or consequential phase synthesis | Optional immutable phase summary | Canonical delivery record |

---
