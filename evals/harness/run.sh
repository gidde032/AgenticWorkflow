#!/usr/bin/env bash
# Routing-eval runner for this plugin. Use this instead of calling run_eval
# directly -- it applies three corrections the raw harness does not:
#
#   1. Serial runs. Concurrent runs of one query register identically-described
#      command files; an agent may invoke a sibling run's name and be scored a
#      miss, collapsing the measured rate toward 1/num_concurrent. (Observed:
#      a literal control invocation scored 0.2 instead of 1.0.)
#   2. Preamble tolerance. The upstream detector scores an immediate miss if the
#      first tool call is not Skill/Read, so a TodoWrite or Bash preamble reads
#      as a false negative. Patched in evals/harness/scripts/run_eval.py.
#   3. Sandbox isolation. Running with cwd set to this repository lets the agent
#      explore the real skills and read prior eval output. Runs execute in an
#      empty sandbox containing only .claude/.
#   4. Pinned model. `claude -p` otherwise inherits ~/.claude/settings.json's
#      `model`. A model that is unset/unavailable makes every run fail with no
#      tool calls, which scores as a clean 0.0 -- indistinguishable from a
#      description that does not route. Pin it so results are reproducible.
#      Override with EVAL_MODEL=<id>.
#
# Usage: evals/harness/run.sh <skill-name> [extra run_eval args...]
set -euo pipefail

SKILL="${1:?usage: run.sh <skill-name> [args...]}"; shift || true
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SANDBOX="${EVAL_SANDBOX:-/tmp/aw-eval-sandbox}"
MODEL="${EVAL_MODEL:-claude-sonnet-4-6}"
TIMEOUT="${EVAL_TIMEOUT:-20}"

SKILL_DIR="$REPO/skills/$SKILL"
[ -d "$SKILL_DIR" ] || { echo "no such skill: $SKILL" >&2; exit 1; }
EVALSET="$REPO/evals/$SKILL/eval-set.json"
[ -f "$EVALSET" ] || { echo "no eval set: $EVALSET" >&2; exit 1; }

rm -rf "$SANDBOX"; mkdir -p "$SANDBOX/.claude"

cd "$SANDBOX"
PYTHONPATH="$REPO/evals/harness" python3 -m scripts.run_eval \
  --eval-set "$EVALSET" \
  --skill-path "$SKILL_DIR" \
  --runs-per-query 5 \
  --timeout "$TIMEOUT" \
  --model "$MODEL" \
  "$@"
