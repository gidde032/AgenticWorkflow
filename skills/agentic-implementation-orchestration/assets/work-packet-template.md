# 3. Implementation work-packet template

```markdown
# Work packet: <ID — short title>

## Objective
<One observable outcome.>

## Delivery state
- Project root: <absolute path>
- Owning Issue: <number, title, URL>
- Milestone: <name or none>
- Branch/worktree: <identifier>
- Draft PR: <number/URL or not opened>
- Implementation authority: <approved source or explicit pre-authorization>

## Verified starting state
- Relevant current behavior: <verified fact>
- Base commit or comparison point: <identifier>
- Existing user/unrelated changes: <paths and preservation rule>

## Owning contract
- Issue acceptance criteria implemented by this packet: <exact subset>
- Spec/ADR sections: <paths and sections>
- Interfaces that must remain stable: <list>

## Ownership
- Allowed files/modules: <exclusive list>
- Forbidden files/modules: <explicit list>
- Dependencies or preceding packets: <IDs or none>
- Parent-owned integration surfaces: <list>

## Version-control and external-write authority
- Stage/commit permission: <none unless explicitly granted>
- Push permission: <none unless explicitly granted>
- Issue/PR update permission: <none unless explicitly granted>
- Internal documents that must remain unpublished: <paths>

## Required implementation
- <bounded requirement>

## Minimality constraints
- Smallest acceptable solution: <least machinery needed>
- New abstractions/configuration permitted only when: <current use or required seam>
- Adjacent cleanup allowed: <explicit list or none>

## Acceptance criteria
- [ ] <observable criterion>

## Verification
- Required fail-before-fix evidence: <command/method or not applicable>
- Targeted commands: `<exact commands>`
- Required gates: `<exact commands or named project gates>`
- Expected skips or environment limitations: <explicit set or none>

## Tracking impact
- Issue state change expected: <proposal or none>
- PR update expected: <proposal or none>
- Parent-owned external actions: <list>

## Documentation impact
- Documentation map: <path>
- Expected surfaces: <specific paths or none with rationale>
- Required freshness checks: `<commands, examples, links, paths, or claim checks>`

## Non-goals
- <named scope fence>

## Stop and escalate when
- A contract or authorization is missing or contradictory.
- Work requires a forbidden file or new cross-packet interface.
- User-owned changes overlap required edits without a preservation plan.
- The same approach fails twice.
- A privacy, security, migration, release, or external-world claim is uncertain.
- A GitHub or other external write appears necessary but is not granted.

## Required return
1. Files and hunks changed.
2. Issue criteria and contract implemented.
3. Commands run and exact results.
4. Gates skipped or failed, with reasons.
5. Red/green evidence and limitations.
6. Documentation impact accounting.
7. Proposed tracking impact; external writes actually performed, if any.
8. Minimality accounting.
9. Deviations, assumptions, unrelated changes encountered, and unresolved risks.
```

For a lower-capability implementer, append the brief-hardening instructions from
`agentic-driving-weaker-models`: contract-first fixes, explicit scope fences,
mandatory gate accounting, proof for diagnostic claims, and live verification
of unstable external facts.

---
