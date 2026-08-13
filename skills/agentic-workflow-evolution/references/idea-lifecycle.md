# 5. Run the idea lifecycle

Move each proposal through:

```text
Observed
  -> captured
  -> mechanism investigated
  -> adoption level selected
  -> experiment authorized
  -> tested during real work
  -> evidence reconciled
  -> adopted, provisional, reshaped, or retired
  -> affected artifacts updated
  -> follow-up signal monitored
```

### Observed and captured

Record the observation without prematurely writing a rule. Name the concrete
friction, artifact, and consequence.

### Mechanism investigated

Reproduce or inspect enough evidence to distinguish cause from coincidence.
Name a failure mode when it is characterizable.

### Adoption level selected

Choose the narrowest level supported. A project-specific architecture constraint
usually remains project-local even if it is important.

### Experiment authorized

If the experiment changes gates, budgets, operating rules, external state, or
plugin behavior, get the corresponding human approval. The experiment may ride
inside a broader authorization envelope.

### Tested during real work

Prefer a real phase, migration, review, or release where the proposed practice
has natural consequences. Do not build a contrived project and treat its success
as equivalent to production evidence.

### Evidence reconciled

Compare prediction with observation. Include counterevidence and costs. Do not
promote because the result was merely non-catastrophic.

### Decided

Use one terminal status:

- **Adopted:** evidence supports the requested level.
- **Provisional:** useful enough to continue testing, explicitly not final.
- **Reshaped:** evidence supports a narrower or different version.
- **Retired:** disproven, superseded, or not worth its cost.

Record the human decision and rationale.

### Artifacts reconciled

Update every active artifact that would otherwise contradict the decision.
Preserve historical context in the chronicle rather than leaving obsolete
instructions active.
