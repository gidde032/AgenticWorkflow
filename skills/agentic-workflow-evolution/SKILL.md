---
name: agentic-workflow-evolution
description: >
  Improve a human-directs-AI-agents workflow through evidence rather than
  theory. Capture and route workflow observations; distinguish project-local
  lessons, cross-project candidates, and plugin-wide practices; design
  real-work experiments; evaluate reviewer, CI, migration, memory, gate, or
  session failures; promote, reshape, or retire practices; and reconcile the
  Issues, PRs, rules, practices, skills, and plugin releases affected by an
  approved change. Use when deciding whether a lesson belongs in
  pending-lessons, practices, a GitHub Issue, project rules, or a reusable
  plugin; when updating a skill; when a recurring failure suggests a workflow
  change; or when auditing whether current guidance is still supported.
  Triggers: "should we change the workflow", "promote this lesson", "update the
  plugin", "workflow experiment", "named failure mode", "why did this recur",
  "is this practice reusable", "retire the old practice", "log this revision",
  "what evidence supports this rule".
---

# Agentic Workflow Evolution

Treat the workflow as a versioned artifact. Improve it when evidence supports a
specific mechanism, at the narrowest adoption level that solves the observed
problem. Do not turn one project's preference into a universal rule, and do not
leave a proven cross-project improvement trapped in session memory.

The agent proposes and assembles evidence. The human decides whether project
rules, gates, reusable skills, or plugin behavior change.

Worked examples and provenance: `examples.md`.

## 1. Choose the adoption level first

Do not ask only, "Is this a good idea?" Ask, "What scope does the evidence
justify?"

| Level | Meaning | Normal destination |
|---|---|---|
| Observation | Something happened once; the mechanism may be unclear | Session evidence or `pending-lessons.md` |
| Project-local candidate | A plausible mechanism is worth testing in this repository | `pending-lessons.md`, experiment record, or project Issue |
| Project-local adopted | Evidence supports an operating rule or structural protection here | Project rules, `practices/`, tests, or configuration |
| Cross-project candidate | Similar evidence appears in materially different projects | Plugin backlog, explicit experiment, or proposal Issue |
| Plugin-wide adopted | Evidence supports changing reusable skills or plugin behavior | Canonical plugin source and versioned release |
| Retired | The practice is superseded, disproven, or no longer applicable | Preserved retirement record plus active-artifact cleanup |

Start narrow. Promotion is a separate decision, not a side effect of fixing the
original problem.

### Ratification is not implementation authority

Approval of a workflow proposal does not automatically authorize code changes,
gate changes, a plugin release, or installation. Establish the relevant
authority boundary through `agentic-collaboration-cadence`.

## 2. Route each artifact to one source of truth

Use the artifact whose job matches the information:

- **`pending-lessons.md`:** unpromoted local observations, unresolved
  mechanisms, and candidates awaiting evidence.
- **`practices/`:** durable rationale, mechanism, evidence, and history for
  adopted project practices.
- **Project rules (`CLAUDE.md`, `AGENTS.md`, or equivalent):** concise
  session-relevant instructions that future agents must follow.
- **GitHub Issue:** open work, a planned experiment, an actionable workflow
  change, or a deferral that needs ownership and status.
- **Pull request:** implementation, validation, discussion, and integration
  state for an approved change.
- **Handoff:** immediate project state and the next operational action.
- **Changelog or release notes:** shipped history.
- **Canonical plugin source:** approved reusable behavior.

Do not:

- Use the handoff as a long-term workflow backlog.
- Put unratified hunches into active rules.
- Duplicate a complete proposal across Issues, practices, and the handoff.
- Edit plugin caches or generated installed copies as source.
- Create speculative Issues with no intended owner, experiment, or decision.

Link canonical artifacts instead of copying their contents.

## 3. Apply the evidence bar

Before adopting "we should always do X," test the claim.

### Explain all material observations

Prefer one mechanism that explains the successes, failures, and apparently
contradictory evidence. "CI is flaky" is not a mechanism. An environment-specific
tool classification rule that explains both CI failure and local auto-reversion
is.

### Verify current external claims

Treat assertions about APIs, models, dependencies, platforms, and repository
settings as inputs to judgment. Check current primary evidence before adopting a
rule. A confident reviewer can be stale.

### Predict before measuring

When practical, state:

- The predicted observation.
- The measurement method.
- The baseline or comparison.
- The tripwire that would challenge the hypothesis.

Numbers are useful only when the method and scope are named.

### Seek independent evidence

Convergence raises confidence when observers reached the conclusion
independently. Before claiming convergence, check whether they shared:

- The same prompt or conclusions.
- The same model assumptions or knowledge limitations.
- The same incomplete sandbox.
- The same source artifacts or blind spots.

Independent agreement is strong evidence, not an automatic verdict. Validate the
claim against code, tests, contracts, and primary sources.

### Preserve counterevidence

Record failed predictions, negative results, rejected findings, and conditions
where the practice does not apply. A rule without its boundary will spread past
the evidence that justified it.

## 4. Capture a workflow-change evidence packet

Before promotion, assemble:

```markdown
Proposal:
Adoption level requested:
Problem or named failure mode:
Evidence sources:
Mechanism:
Counterevidence:
Hypothesis:
Predicted observation:
Measurement method:
Real-work ride-along:
Observed result:
Scope and risks:
Decision:
Artifacts to update:
Follow-up signal:
```

Abbreviate this for a small local lesson. Use the complete packet for a
plugin-wide proposal or a consequential gate change.

Evidence sources may include:

- Repository code and tests.
- CI runs and tool logs.
- Issues and PR discussions.
- Independent reviewer reports after parent validation.
- Human hands-on testing, bounded to what was actually observed.
- Repeated session friction.
- Migration disposition ledgers.
- Primary external documentation.

Do not substitute recollection for inspectable evidence when the artifact is
available.

## 5. Run the idea lifecycle

Ideas move through capture, evidence-gathering, trial, and a terminal decision
to promote, reshape, or retire. The stage-by-stage mechanics are in
`references/idea-lifecycle.md`. Read it when advancing or closing an idea, not
when merely logging an observation.

## 6. Use real work and forward tests correctly

Workflow adoption evidence should ride real work. Skill forward tests,
simulations, fixtures, and disposable repositories may supplement that
evidence by exposing ambiguity or unsafe behavior.

Apply these limits:

- Synthetic success alone does not justify plugin-wide promotion.
- A failed forward test is material counterevidence.
- Forward-test agents must not receive the intended answer, suspected defect,
  or hidden conclusions unless the evaluated behavior specifically requires it.
- Preserve raw prompts, artifacts, outputs, and validation results.
- Use disposable state and avoid production mutations.
- Do not count repeated tests of the same fixture as cross-project evidence.

Route detailed skill forward-testing mechanics to `skill-creator`.

## 7. Set promotion thresholds

### Project-local adoption

One strong incident may justify a local protection when:

- The mechanism is verified.
- The consequence is meaningful.
- The rule or protection is scoped and reversible.
- Counterevidence is addressed.
- The project owner approves the change.

A regression, explicit configuration, or repository rule can be appropriate
before the same failure appears elsewhere.

### Plugin-wide adoption

Normally require:

- Evidence from at least two materially different projects; or
- One severe, well-understood failure with explicit provisional labeling and a
  planned cross-project test.

Also require:

- A reusable mechanism rather than a project preference.
- Compatibility with supported project variations.
- An explicit human promotion decision.
- Validation of every changed skill or resource.
- Forward testing when behavior is complex or easy to mis-trigger.
- A versioned, reversible plugin update.

If the threshold is not met, keep the proposal project-local or mark the plugin
change provisional. Do not promote by enthusiasm.

## 8. Use Issues and PRs for actionable evolution

Open or reuse an Issue when the proposal requires work, an experiment, or
durable tracking. Include:

- Requested adoption level.
- Evidence packet or link.
- Acceptance criteria.
- Affected artifacts.
- Explicit non-goals.
- Validation and follow-up requirements.

Implement an approved change through an isolated branch and PR when the
repository uses that workflow:

- Link the governing Issue.
- Explain the evidence-backed behavior change.
- Identify removed or retired guidance.
- Include validation and forward-test evidence.
- Separate reusable workflow changes from unrelated product work.
- Keep the PR draft until the approved review and gate sequence is complete.
- Close the Issue only after required artifacts and status are reconciled.

An Issue marked ready, a milestone assignment, or an approved proposal does not
grant implementation, merge, release, or installation authority by itself.

## 9. Change reusable skills and plugins safely

For plugin-wide adoption:

1. Identify the canonical source and the derived copies.
2. Preserve the current released version or a recoverable backup.
3. Edit only the canonical source.
4. Review judgment-sensitive changes skill by skill when requested.
5. Validate each changed skill and bundled resource.
6. Forward-test complex triggering or behavior when appropriate.
7. Refresh derived plugin copies with the supported helper.
8. Bump the version after the approved change set is complete.
9. Validate every supported runtime and package shape.
10. Record the evidence, release delta, and rollback path.

Never:

- Edit a plugin cache as the source of truth.
- Let derived copies diverge silently from the canonical source.
- Bump the release version after each partial skill edit when the edits belong
  to one approved release.
- Treat a successful validation script as proof that the workflow behavior is
  correct.
- Install or publish the updated plugin without the relevant authority.

## 10. Keep experimental skills contained

An experimental skill must declare:

- Trigger policy.
- Supported and excluded workflows.
- Required evidence artifacts.
- Validation target.
- Promotion condition.
- Retirement or rollback path.

Treat a successful run as evidence, not as promotion authority.

`agentic-docs-github-migration` is the worked example of a skill that completed
this path — contained while evidence accumulated, then promoted by an explicit
human decision, and still explicit-invocation-only afterward because of its
finite-use shape (`examples.md` §2).

## 11. Preserve lessons so they compound backward

Write project lessons so a future structural improvement can find them:

- **Concrete:** name the observable failure.
- **Mechanism-named:** explain why it occurred.
- **Artifact-linked:** identify where a structural protection would live.
- **Boundary-aware:** state where the lesson does and does not apply.

A useful lesson can later become a shared fixture, explicit configuration,
review rule, or reusable skill improvement that protects older code as well as
new work.

Three lessons from the reference project each became a structural fix that
repaired existing work as well as future work — explicit tool configuration,
differentiated reviewer roles, and a shared test fixture (`examples.md` §1).

## 12. Name failure modes

Named failure modes turn repeated surprises into cheap guards. Useful examples:

- **Confidently wrong about current reality:** verify external claims against
  current primary evidence.
- **Correctly wrong in an unfaithful sandbox:** verify the review target and
  supplied artifacts before trusting absence claims.
- **Ratified therefore authorized:** separate product agreement from
  implementation authority.
- **Derived copy edited as source:** restore canonical ownership and refresh
  through supported tooling.
- **Successful pilot promoted universally:** require the requested adoption
  level's evidence.
- **History preserved as active contradiction:** retain the chronicle while
  removing obsolete operating instructions.

When a new mode recurs or has severe consequences, add its mechanism and guard
to the appropriate project practice or plugin proposal.

## 13. Retire and reconcile

Do not silently delete the history of a practice. Also do not keep superseded
instructions active merely to preserve history.

For retirement:

1. Record what was retired and why.
2. Link the evidence or replacement.
3. Remove or update active rules, templates, skills, and gates.
4. Search for contradictory copies.
5. Update related Issues and PRs.
6. Keep the historical entry with its retirement status.
7. Define a follow-up signal if the replacement remains provisional.

The chronicle preserves evolution; active artifacts describe current behavior.

Revision entry:

```markdown
### Revision N: <one-line name>
- What changed: <concrete workflow delta>
- Evidence: <observations and links>
- Adoption level: <local, cross-project candidate, or plugin-wide>
- What to watch: <success or failure signal>
- Ride-along: <real phase, migration, review, or release>
- Status: <adopted, provisional, reshaped, or retired>
```

## 14. Compact decision checklist

Before proposing:

- [ ] Name the observation and consequence.
- [ ] Inspect the current artifact rather than relying on memory.
- [ ] Identify the mechanism and counterevidence.
- [ ] Select the narrowest requested adoption level.
- [ ] Route the proposal to the correct canonical artifact.

Before experimenting:

- [ ] Declare the hypothesis, prediction, method, and tripwire.
- [ ] Obtain authority for gates, rules, costs, and external actions.
- [ ] Choose a real-work ride-along.
- [ ] Preserve raw evidence and disposable test state.

Before promoting:

- [ ] Check the evidence threshold for the requested level.
- [ ] Reconcile independent evidence and shared blind spots.
- [ ] Obtain the human decision.
- [ ] Update all affected active artifacts.
- [ ] Validate and forward-test reusable skill changes as appropriate.
- [ ] Record version and rollback information for plugin changes.

## When not to use this skill

| Need | Route to |
|---|---|
| Decide whether work may continue or must pause | `agentic-collaboration-cadence` |
| Run a feature phase | `agentic-phase-workflow` |
| Run independent reviewers | `agentic-review-orchestration` |
| Write regressions or define gates | `agentic-verification-discipline` |
| Maintain memory files mechanically | `agentic-project-memory` |
| Bootstrap a project | `agentic-project-bootstrap` |
| Manage session cost as the primary problem | `agentic-session-economics` |

This skill governs whether observed evidence should change those workflows.

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
