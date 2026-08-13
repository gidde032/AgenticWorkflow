---
name: agentic-verification-discipline
description: >-
  Build trustworthy evidence for agent-generated changes and make required
  verification enforceable locally and in GitHub. Use when converting accepted
  findings into fail-before-fix regression tests; defining or weakening numeric
  gates and coverage floors; recording red/green evidence in a PR; creating or
  selecting a repository-owned GitHub Actions required check and its check
  source; verifying ruleset enforcement; preventing unexpected skips, enforcing
  a skip budget, or pinning a smoke inventory; testing stable documentation
  promises; synchronizing tool ignore lists; deciding where a regression test
  belongs; or diagnosing a local-versus-CI difference where CI enforces a gate
  the local run does not. Do not use for ordinary CI log debugging that changes
  no verification contract, for designing a test plan or test strategy that
  carries no gate or enforcement change, or for deciding product scope and
  finding disposition.
---

# Agentic Verification Discipline

How agent-built code earns trust, one finding at a time.

**Numeric gates** — setting floors, ratcheting, and handling a missed
prediction: `references/numeric-gates.md`.
**GitHub Actions and rulesets** — workflow requirements, required-check
activation order, and configured-versus-enforced reporting:
`references/github-actions-contract.md`.
**Worked examples and provenance** — the evidence behind every rule here:
`examples.md`.

---

## 1. The Core Contract

> **No accepted defect disappears without durable evidence or a durable
> disposition.**

Every accepted finding receives one terminal disposition:

- **Repair now** — reproduce the failure, fix it, add the smallest faithful
  regression test, record red/green evidence.
- **Defer** — create or link an Issue containing the finding, evidence, impact,
  and acceptance criteria.
- **Reject** — record evidence showing the finding is incorrect or outside the
  accepted contract.
- **Duplicate** — link the existing Issue.
- **Outside contract** — name the governing boundary and why no action is
  warranted.

"Remember later," a handoff bullet, or an unlinked review report is not a
terminal disposition.

For a repaired finding:

1. Observe the failure before applying the fix when safely possible.
2. Add the smallest test that faithfully reproduces the defect.
3. Confirm that test fails for the defect mechanism.
4. Apply the fix.
5. Confirm the targeted test passes.
6. Run the broader required gates.
7. Record commands and results in the PR.

Do not claim fail-before-fix evidence unless the failure was actually observed.

### Why it compounds

A phase's regression file that stays green through later phases is a living
specification of the edge cases the project actually handles — more honest than
the spec document. On the reference project ~31% of the final suite came from
review-fix regression files, and the Phase 1 file was still green six phases
later (`examples.md` §1).

### Safe fail-before-fix evidence

When the finding arrives after an implementation already contains the fix:

1. Preserve the user's worktree and unrelated changes.
2. Reproduce against the base commit in an isolated worktree, disposable copy,
   container, or equivalent clean environment.
3. If isolation is impractical, use the smallest safe reversible mutation that
   exposes the defect without disturbing unrelated work.
4. Do not use destructive checkout or reset operations to manufacture evidence.
5. If faithful reproduction is impossible, say so and record the strongest
   available evidence without calling it fail-before-fix.

Record:

```text
Regression evidence
- Finding: <Issue/PR review link>
- Failing command: <command>
- Failure observed: <concise result>
- Passing command: <command>
- Pass observed: <concise result>
- Broader gates: <commands and results>
- Limitations: <none or explicit constraint>
```

---

## 2. Regression Test Placement and Naming

Place the regression test at the closest stable behavioral boundary, preferring:

1. The existing test file for the affected unit, endpoint, command, component,
   or contract.
2. An existing cross-cutting contract or integration-test file.
3. A dedicated review-fixes file only where the project has that convention, or
   the finding genuinely spans several unrelated surfaces.

Name the test for the behavioral contract, not the reviewer:

```text
test_rejects_nonfinite_quantity_at_cli_boundary
test_preserves_card_order_after_failed_move
test_export_v1_remains_readable_after_v2_migration
```

The PR owns review provenance, severity, and delivery history. Test names and
docstrings explain what must remain true and, when useful, the defect mechanism.
Reference an Issue or PR in a comment only when a future reader needs it to
understand the contract.

Do not create a test file merely to preserve a review round's chronology. That
chronology already exists in GitHub.

---

## 3. Contracts, Not Conventions

Any tag, marker, or annotation with *semantic* meaning — "this test is fast,"
"this test requires network," "this endpoint is deprecated" — should be enforced
by a checked contract, not left as documented convention.

```
meta-test: enumerate all items carrying tag X → assert count == N
           (or that composition matches the expected set)
```

**Assert exact counts, not lower bounds.** `>= N` catches removal but not
addition. If the tag means "quick local feedback," adding a slow test violates
the promise just as much as removing a fast one.

Use exact inventory checks only where membership is itself part of the contract
— a deliberately bounded smoke suite. Do not pin counts for ordinary test groups
whose growth is expected.

Prefer asserting expected identities or composition over parsing a
human-oriented summary count: a count can stay unchanged while the wrong test
enters and the right one leaves. In order of strength:

1. Structured runner API or machine-readable enumeration of expected members.
2. Exact identity set.
3. Exact count, when identity enumeration is impractical.
4. Source-text counting, only as a last resort.

```python
import subprocess, sys

def test_fast_tier_marker_count():
    """The 'smoke' marker must tag exactly N tests.

    Exact-count prevents both removal (drops below N) and creep (slow tests added).
    """
    result = subprocess.run(
        [sys.executable, "-m", "<test-runner>", "--collect-only", "-m", "smoke", "-q"],
        capture_output=True, text=True, cwd="<project-root>"
    )
    lines = [l for l in result.stdout.splitlines() if l.strip()]
    assert result.returncode == 0
    assert exactly_N_tests_collected(lines), f"Expected N, got:\n{result.stdout}"

def test_fast_tier_runs_under_budget():
    """The smoke suite must complete in under T seconds."""
    import time
    start = time.monotonic()
    subprocess.run([sys.executable, "-m", "<test-runner>", "-m", "smoke", "-q"],
                   capture_output=True)
    assert (time.monotonic() - start) < T
```

Non-Python stacks: use the runner's native enumeration (`jest --listTests`,
`go test -list`, `cargo test -- --list`), not source-text counting — a
cross-stack dry run of this skill chose the fragile form (`examples.md` §2).

---

## 4. Verification for Documented Promises

Documented promises are contracts, but prose wording is not automatically a test
target. Add an automated check when the promise is stable and
machine-verifiable:

- a command or option that must exist;
- a configuration key or environment variable;
- a referenced file, link, route, schema, or generated artifact;
- an onboarding sequence that can be executed safely;
- a documented output shape with a stable machine-readable contract; or
- a public support boundary likely to drift silently.

Prefer, in order:

1. Execute the documented command safely.
2. Validate the referenced file, link, schema, route, or generated artifact.
3. Test a structured example or fixture.
4. Assert normalized content, only when the exact textual promise itself matters.

Do not add a literal substring assertion merely because documentation changed.
That pins phrasing rather than behavior.

Normalize whitespace before asserting, or line wrapping creates false failures —
a raw `read_text()` breaks substring matching on a phrase spanning a line break:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent  # adjust to your layout

def _read_doc(name: str) -> str:
    """Read a doc file, normalizing whitespace so line-wraps don't break assertions."""
    return " ".join((PROJECT_ROOT / "docs" / name).read_text().split())

def test_quickstart_mentions_init_command():
    assert "init" in _read_doc("quickstart.md")
```

---

## 5. Numeric Gates — Predicted Before Measured

Predict a gate's value before you measure it, then compare. A floor chosen after
seeing the number is not a gate, it is a description.

Full mechanics — choosing floors, ratcheting, coverage and latency specifics,
and handling a missed prediction — are in `references/numeric-gates.md`. Read it
when setting or changing a gate, not when running one that already exists.

---

## 6. Tool Ignore-Lists Must Agree

Where your test runner, linter, and coverage tool each carry exclude/ignore
lists, they must agree on what counts as live code. One project-wide answer.

**Symptom of disagreement:** coverage reports a number that reflects neither the
tests being run nor the code being linted, because each tool has a different idea
of which files exist.

**Fix:** mirror the lists. When the test runner ignores `<path>`, add it to the
linter's `exclude` and the coverage tool's `omit`. The rationale is the same
across all three — write it once, apply it everywhere.

This is not a rounding error. On the reference project, mirroring the lists moved
measured coverage from 67% to 91.3% with no change to what code ran
(`examples.md` §4).

---

## 7. Skip Visibility

`pytest.importorskip` and its equivalents are right for *optional* environment
dependencies: "if the PDF library isn't available, skip these PDF tests." They
are wrong for a dependency that should always be present in a development
environment.

**The problem:** when a should-always-be-installed dep is missing,
`importorskip` silently drops the tests. The suite appears to pass, coverage is
inflated, and nobody notices — on the reference project, 22 tests vanished from
every local run for four releases (`examples.md` §5).

**Countermeasures:**

1. **Distinguish "might be absent" from "must be present"** at the top of any
   test file using `importorskip`.
2. **Read skip counts and reasons in CI output.** A run that skipped 22 tests is
   not the same as one that skipped none.
3. **Verify deps match usage.** After adding any `importorskip`, confirm the
   dependency appears in the dev/test dependency list.

### Skip budget contract

Classify each skip as:

- expected and environment-optional;
- expected but temporary, with an owning Issue and expiry condition; or
- unexpected and gate-failing.

Where the runner permits, emit machine-readable skip data and enforce an expected
skip count or reason-set in CI, so a change requires deliberate review. Manual
inspection is the fallback for runners without structured skip reporting, not the
primary control.

---

## 8. New Output Breaks Old Assertions

Adding a warning, log line, or message to an existing code path is a *contract
change* for every test that already asserts on that output. You add a warning to
`function_X` and test it; the full suite then fails on an older test written when
`function_X` produced exactly one warning.

Before committing any change that adds output to an existing path:

```bash
rg -n 'len\(.*warnings|warnings.*==|==\s*[0-9]+' tests
rg -n 'stdout|stderr|output|messages' tests
rg -n 'toHaveLength|length\)|count\(|exactly' tests
```

Search the semantic output surface, not one framework's assertion syntax. Run
the full suite after changing shared output — a targeted test cannot reveal
every old exact-count assumption (`examples.md` §6). Update affected assertions
in the same commit as the contract change.

---

## 9. Environment-Dependent Failure Classes

Three portable classes, each with a distinct countermeasure. Worked cases in
`examples.md` §7.

### 9a. Explicit beats implicit for tool configuration

**Problem:** a tool (linter, import sorter, type checker, test discovery) uses a
heuristic to classify or order things, the heuristic answers differently across
environments, and the tool's auto-fix actively reverts correct code.

**Countermeasure:** declare key classification decisions explicitly rather than
leaving them to heuristic — import sorters' first/third-party lists, formatter
settings, test discovery patterns, type-checker `follow_imports`. Cheap
insurance against silent cross-environment thrash.

### 9b. `try/except` cannot catch native crashes

**Problem:** you guard a native-library import with
`try/except (ImportError, OSError)`. The library loads partially, then crashes
the process with a signal (SIGSEGV, SIGILL). No exception fires; the runner dies.

**Countermeasure:** probe the import in a subprocess first.

```python
import subprocess, sys

def _native_lib_available(import_name: str) -> bool:
    """True if the library loads cleanly in a subprocess.

    A subprocess crash produces a non-zero exit code; the parent detects it
    and returns False rather than dying.
    """
    result = subprocess.run([sys.executable, "-c", f"import {import_name}"],
                            capture_output=True)
    return result.returncode == 0

if not _native_lib_available("weasyprint"):
    pytest.skip("weasyprint not available or native libs incompatible")
```

Cost: one subprocess at collection time. Value: a catastrophic environment
failure degrades to a skip instead of killing the runner.

### 9c. Reproduce CI's environment locally before pushing

**Problem:** tests pass locally and fail on CI because an environment-dependent
variable — terminal width, locale, available memory, path separators — differs
between your machine and the runner.

**Countermeasures, both layers:**

1. **Structural fix.** Bake the variable into a fixture applying to all tests by
   default: a `conftest.py` fixture setting `env={"COLUMNS": "200"}` on every
   invocation, so wrap bugs are invisible during development.
2. **Stress test (pre-push gate).** Run the full suite at CI's value first —
   `COLUMNS=80 pytest -q` before any push touching CLI output assertions.

The structural fix eliminates the class from new tests; the stress test catches
older tests that predate it.

---

## 10. Verification Accounting in the PR

Before marking a PR ready, record:

```text
Verification
- Targeted red/green evidence: <commands and results>
- Local required gates: <commands and results>
- GitHub Actions check: <name, source, and result>
- Required-check/ruleset enforcement: <verified result or limitation>
- Skips and exclusions: <expected set/count and changes>
- Documentation verification: <checks and results>
- Unrun checks: <none or explicit reason>
```

A green badge without the command, source, and applicable limitations is weaker
than a reproducible verification record.

---

## 11. When NOT to Use This Skill

| Situation | Go here instead |
|---|---|
| Design the review process that *produces* the findings this skill converts to tests | `agentic-review-orchestration` |
| Decide what phases produce, when hardening passes happen, or how the spec stays alive | `agentic-phase-workflow` |
| Control session cost when the verification pass is too expensive | `agentic-session-economics` |
| Decide which findings to fix now vs. defer to a later release | `agentic-collaboration-cadence` |
| Set up the four-file memory architecture or write a handoff | `agentic-project-memory` |
| Bootstrap the whole system on a new project | `agentic-project-bootstrap` |
| Decide whether a finding is repaired, deferred, rejected, duplicate, or outside scope | `agentic-review-orchestration` and `agentic-collaboration-cadence` |
| Administer ordinary Issues or PR metadata | Use the available GitHub tooling |
| Debug one failing Actions run without changing the verification contract | Use the platform's GitHub CI diagnostic workflow |
| Change branch governance, visibility, licensing, or merge authority | Return to the approved project profile and human authorization boundary |

A project may also carry its own skill library that instantiates these patterns
with project-specific paths, runner commands, and gate values.

---

## 12. Quick Reference Checklist

Before marking a reviewed PR ready:

- [ ] Every accepted finding has a terminal disposition.
- [ ] Every repaired defect has an observed failing reproduction, or an explicit
      limitation explaining why fail-before-fix could not be observed.
- [ ] The smallest faithful regression test sits at the nearest stable
      behavioral boundary.
- [ ] The targeted test passes after the fix.
- [ ] Required broader local gates pass.
- [ ] Test provenance and severity live in the PR; test names describe behavior.
- [ ] Semantic marker/tag inventories use structured identities or justified
      exact counts.
- [ ] Stable documented promises are verified at the strongest practical level.
- [ ] New output was searched against existing exact-count and output assertions.
- [ ] Gate changes preserve the approved value, population, exclusions, and
      measurement method — or carry explicit approval and rationale.
- [ ] Test, lint, type, and coverage ignore lists agree.
- [ ] Skip counts and reasons match the expected contract.
- [ ] Native libraries are isolated with subprocess probing where process crashes
      are possible.
- [ ] The repository-owned Actions check passed with the expected name and source.
- [ ] Required-check and ruleset enforcement are reported separately from
      configuration.
- [ ] The PR contains complete verification and documentation accounting.
