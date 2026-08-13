# 5. Numeric Gates — Predicted Before Measured

Gates exist to *catch regressions*, not to memorialize whatever the meter reads today.

### Setting a gate

1. **State the number explicitly**, with method: "best of 5 runs," "85th percentile in CI," "floor measured after excluding inert files."
2. **Record the rationale inline** — next to the config line that sets the gate, not just in a commit message.
3. **Set headroom**: floor = measured value - reasonable buffer. A gate at 91% measured coverage should floor at 85%, not 90.9%, so legitimate uncovered defensive branches don't trigger false failures.

### Gate-change protocol

Weakening a required gate always requires explicit human approval.

Present:

- the current value and measurement method;
- observed results across representative environments;
- why the existing value is unreliable or no longer represents the contract;
- the proposed value;
- effect on user risk and defect detection;
- alternatives considered; and
- the Issue or decision record that will preserve the rationale.

After approval, update the spec or ADR, local gate configuration, GitHub Actions
workflow, required-check documentation, and rationale in the same delivery
boundary.

Strengthening a gate may proceed only when the project already meets it
reliably and the approved workflow permits autonomous ratcheting. Otherwise,
surface it as a proposal too.

Never make a red gate green by silently changing its target, exclusions,
measurement method, or test population.

**Worked example (a Python CLI project):** The startup-time budget was raised from 300 ms to 600 ms in v0.1.2, with rationale recorded directly in the spec: "the earlier 300 ms target proved tight against real CI hardware and made the gate flaky." The gate wasn't fossilized at an unreachable value; it was updated deliberately, with the decision visible to any future reader. This is what "living gates" look like — route to the `agentic-phase-workflow` skill for the parallel "living spec" concept.

### Define-your-gates checklist for a new project

Pick 3–6 gates. Write each as: **command** + **pass criterion** + **owner-signed change rule**.

| Gate | Example command | Pass criterion | Change rule |
|---|---|---|---|
| Format | `<formatter> --check src tests` | Exit 0 | Auto-fix at commit via pre-commit; CI gate-only |
| Lint | `<linter> check src tests` | Exit 0 | Same as format |
| Types | `<type-checker> src` | Exit 0 | Explicit maintainer approval to suppress |
| Tests + coverage | `<test-runner> --cov=src --cov-fail-under=N` | N% floor | Raise only with new uncovered code; lower only with sign-off + rationale |
| Smoke tier inventory | Meta-test asserting marker count | Exact count == N | Change count deliberately, update meta-test in same commit |
| Domain budget (startup time, response latency, etc.) | Best-of-5 shell timing | Under T ms/s | Raise with recorded rationale; lower when architecture improves |

### Three-tier gate placement

Route gates to the tier that matches their latency and audience:

| Tier | Trigger | What runs | Characteristic |
|---|---|---|---|
| Commit | `git commit` | Format auto-fix, basic lint auto-fix | Sub-second; fixes persist on contributor's filesystem |
| Push | `git push` | Full test suite, narrow-terminal check | 30–60s; catches regressions before they reach the team |
| CI | PR / tag | All of the above + type-check + coverage + publish pipeline | 2+ min; canonical gate; runs against a clean environment |

**Key insight:** auto-fixing in CI's ephemeral filesystem is a no-op. Auto-fix
belongs at commit time, where the result persists, or through a deliberately
selected integration that commits fixes back to the branch. CI should be
gate-only.

**Worked example (a Python CLI project):** `ruff format` + `ruff
check --fix` ran at commit time; `pytest` at `COLUMNS=80` ran at push time; lint,
type-check, and `pytest` with coverage ran at CI. Same hooks, three different
latencies, three different signals.
