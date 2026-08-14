# Changelog

## 3.1.0 — Decision-challenge experiment

### New skill (experimental)

- **`agentic-decision-challenge`** — stress-tests one already-proposed decision (a
  plan, architecture, workflow change, or product choice) until its hidden
  assumptions and dependent choices are visible. Maps the decision as a dependency
  tree, asks only the settled-prerequisite frontier each round with a recommended
  answer and a short menu of genuinely reasonable options, investigates
  discoverable facts itself instead of asking, routes questions that need research
  or a prototype out to that work, and stops at a shared-understanding gate without
  claiming authority to act. Readily triggerable on medium-to-large decisions;
  silent on trivial ones. Ships as an experiment with an explicit trigger policy,
  evidence target, three-lane promotion condition, and retirement path.

  Mechanism (decision tree / frontier / rounds) is a plugin-native rewrite of Matt
  Pocock's MIT-licensed `grill-me`/`grilling` skills, credited in the skill's
  `examples.md`; no source text ported. Tracked by Issue #9.

### New command

- **`/grill [decision]`** — deterministic front door that loads
  `agentic-decision-challenge` and runs its full loop. Natural-language phrasings
  ("grill me on this", "pressure-test this decision") also trigger the skill, but
  the command guarantees activation; the skill's `examples.md` records where
  auto-trigger is and isn't reliable.

## 3.0.0 — First public release

### New skill

- **`agentic-docs-github-migration`** — promoted from `experiments/`. Explicit-invocation-only migration workflow for existing solo-maintained repositories. Includes profile and disposition validators (`scripts/`), fixture-based test harness, and SHA-256 fingerprint verification against source files.

### Routing fixes

Four description-level seam collisions resolved:

| Seam | Winner | Change |
|---|---|---|
| Post-merge closeout | `phase-workflow` | `project-memory` no longer claims "release closeout" |
| Deferred-idea placement | `project-memory` | `product-discovery` explicitly defers placement to `project-memory` |
| Local-vs-CI gate mismatch | `verification-discipline` | Description narrowed to gate/config contract mismatches |
| Test plan (no gate) | Neither | `verification-discipline` excludes test plans carrying no enforcement change |

### Reference extraction

1,340 lines of worked examples and provenance moved from twelve SKILL.md files into per-skill `examples.md` files. Five skills had additional content extracted into `references/` and `assets/` directories. All skills are now under 500 lines.

### Project-agnostic rewrite

All project names, author references, and personal framing removed. Worked examples use anonymous descriptors ("a Python CLI project", "a documentation migration"). The anonymization mapping is recorded in each skill's `examples.md`.

### Other changes

- Maturity hedges, status markers, and development notes removed — skills read as finished guidance, not provisional experiments
- Dated version claims generalized or removed (kept only inside war stories)
- `agents/openai.yaml` normalized across all twelve skills
- Maintenance triggers rewritten as general conditions
