# Verification discipline — worked examples and provenance

Evidence behind the rules in `SKILL.md`. Read a section when you want the
mechanism and outcome behind a rule, or when a rule seems not to apply to your
project and you need to judge how far it generalizes.

Unless stated otherwise, the reference project is a Python CLI built across six
feature phases and several hardening passes. A second and third body of evidence
come from two documentation-and-GitHub migrations.

## Contents

1. Regression tests compound into a living specification
2. Semantic markers as enforced contracts
3. Documented promises catch draft regressions
4. Disagreeing ignore lists corrupt the measurement
5. Silent skips hide real gaps
6. New output breaks old assertions
7. Environment-dependent failure classes
8. Provenance and maintenance

## 1. Regression tests compound into a living specification

After six feature phases and one hardening pass, roughly 94 of 301 tests (~31%)
came from review-fix regression files. The Phase 1 and Phase 2 regression files
were still green at the end of Phase 6 and through the following patch release.

The contracts held across the full project lifetime without anyone having to
remember them. That is the compounding argument for placing a test at the
nearest stable behavioral boundary: the test files become a more honest record
of handled edge cases than the spec document.

## 2. Semantic markers as enforced contracts

`@pytest.mark.smoke` was supposed to mark exactly five happy-path tests for a
"quick local feedback" suite. A later patch release added a regression test
running `pytest --collect-only -m smoke` in a subprocess, asserting the count is
*exactly* five, plus a companion test asserting the suite runs in under five
seconds. "Quick local feedback" became a pinned, enforceable property rather
than a documented aspiration.

**Cross-stack note.** The first cross-stack dry run of this skill had to
improvise the non-Python equivalent and chose the fragile form — counting
`test(` occurrences in source files. Source-grep counts drift from what the
runner actually registers. Prefer the runner's native enumeration:
`jest --listTests` or Jest's programmatic API, `go test -list`,
`cargo test -- --list`.

## 3. Documented promises catch draft regressions

A docs-content test caught a draft-quickstart regression in seconds: an early
version of a section fix forgot to mention a command by name, and the test
failed before the fix was committed.

This is the case for testing a *stable, machine-verifiable* promise. It is not
an argument for asserting on prose phrasing, which pins wording rather than
behavior.

## 4. Disagreeing ignore lists corrupt the measurement

Naive coverage measurement reported 67%. The coverage config had no `omit` list,
while the test runner and linter both excluded placeholder files left by a
filesystem recovery incident and migration scripts that run in subprocesses
coverage.py cannot instrument.

After mirroring those exclusions into the coverage `omit` list, measured
coverage came out at 91.3% — comfortably above the 85% floor. Nothing changed
about what code ran or what tests executed. Only the measurement became
accurate.

The 24-point gap is the point: a coverage number produced by tools that disagree
about which files exist is not a weak signal, it is a wrong one.

## 5. Silent skips hide real gaps

`pdfminer.six` was used in two test files but never listed in the dev
dependencies. `importorskip` silently dropped 22 PDF content-assertion tests
from every local run for four entire releases. The test suite appeared to pass
and the coverage number was inflated.

The maintainer discovered it during a tooling audit — not because anything broke
visibly. Nothing in the normal workflow would have surfaced it, which is why
skip counts need an expected value rather than a glance.

## 6. New output breaks old assertions

A hardening-audit fix added a "discarded quantity" warning to `merge_materials`.
It broke `test_merge_duplicate_different_units_keeps_target`, which asserted
`len(result.warnings) == 1` and now saw 2.

The full test suite caught it during quality gates — no targeted check would
have. The repair was a one-line update, but it was a surprise, because nobody
grepped for exact-count assertions before committing a change to shared output.

## 7. Environment-dependent failure classes

### Explicit beats implicit for tool configuration

`ruff`'s isort heuristic classified packages as first-party or third-party
differently in the development sandbox than in CI. `ruff --fix` on the
developer's machine reverted CI-correct import ordering on every run.

Two separate bugs across two releases both root-caused to this same class. The
fix was declaring `known-first-party` and `known-third-party` explicitly in
`[tool.ruff.lint.isort]`. Once explicit, every environment produced identical
output.

### `try/except` cannot catch native crashes

WeasyPrint's `dlopen` of bundled Pango and Cairo native libraries crashed with
SIGSEGV on a macOS machine where Anaconda Python and Homebrew Pango had
incompatible `glib`/`cairo` versions.

The existing `try/except (ImportError, OSError)` guard was useless: a signal
kills the process before any exception machinery runs. Subprocess probing turns
a runner-killing crash into a skip.

### Reproduce CI's environment locally before pushing

Two pre-existing tests passed every local run, including a full verification
pass, then failed on the first CI run after a release tag was cut. The CI
runner's narrower default terminal wrapped CLI output mid-word, breaking
substring assertions — `config.toml` became `config.tom\nl`, and
`JSON parse error` became `JSON\nparse error`.

Both layers of the countermeasure matter. The `conftest.py` width fixture
eliminates the bug class from newly written tests; the pre-push run at CI's
narrower width catches the older tests that predate the fixture.

## 8. Provenance and maintenance

The regression, numeric-gate, skip-visibility, tool-configuration,
native-library, and environment-parity practices were derived from the reference
Python CLI project.

The repository-owned Actions check, required-check source selection, activation
order, and configured-versus-enforced distinction were derived from a
documentation-and-GitHub migration and repeated during a second migration.
Current GitHub behavior must still be checked against GitHub's official
documentation, because provider rules and plan availability change.

Closest-boundary regression placement and behavior-centered test naming replace
an older review-round-file requirement as an efficiency improvement. The PR is
now expected to preserve the review provenance that the dedicated file used to
carry.

Update this skill when:

- A post-migration project completes a full red/green → Actions →
  ruleset-enforced PR cycle.
- Behavior-centered test placement loses review provenance or reduces
  searchability.
- Documentation verification becomes too brittle or fails to catch real drift.
- GitHub changes required-check recency, source selection, merge-group, ruleset,
  or plan behavior.
