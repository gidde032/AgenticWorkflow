# Changelog

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
