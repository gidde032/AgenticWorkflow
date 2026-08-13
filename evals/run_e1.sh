#!/usr/bin/env bash
# E1 execution eval: does the agent read extracted files when it needs them?
#
# Sets up a sandbox with the skill copied in, runs claude -p with a task
# that requires content from an extracted file, and checks whether Read
# was called on the target file.
#
# Usage: evals/run_e1.sh <skill-dir> <target-file> <query>
#   skill-dir:   path to the skill (e.g. agentic-project-memory)
#   target-file: relative path within the skill to check for (e.g. references/what-goes-where.md)
#   query:       the prompt to send
set -euo pipefail

SKILL_DIR="${1:?usage: run_e1.sh <skill-dir> <target-file> <query>}"
TARGET_FILE="${2:?}"
QUERY="${3:?}"
RUNS="${E1_RUNS:-3}"
MODEL="${E1_MODEL:-claude-sonnet-4-6}"
TIMEOUT="${E1_TIMEOUT:-60}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SKILL_NAME="$(basename "$SKILL_DIR")"
[ -d "$REPO/skills/$SKILL_DIR" ] || { echo "no such skill: $SKILL_DIR" >&2; exit 1; }
[ -f "$REPO/skills/$SKILL_DIR/$TARGET_FILE" ] || { echo "no such file: $SKILL_DIR/$TARGET_FILE" >&2; exit 1; }

hits=0
for i in $(seq 1 "$RUNS"); do
  SANDBOX="/tmp/aw-e1-$$-$i"
  rm -rf "$SANDBOX"
  mkdir -p "$SANDBOX/.claude/commands"

  # Copy the full skill into the sandbox so the agent can read its files
  cp -r "$REPO/skills/$SKILL_DIR" "$SANDBOX/$SKILL_NAME"

  # Register the skill as a command so the agent knows about it
  SKILL_MD="$REPO/skills/$SKILL_DIR/SKILL.md"
  DESCRIPTION=$(python3 -c "
import yaml, pathlib
fm = yaml.safe_load(pathlib.Path('$SKILL_MD').read_text().split('---')[1])
print(fm['description'])
")

  cat > "$SANDBOX/.claude/commands/$SKILL_NAME.md" <<CMDEOF
---
description: |
  $DESCRIPTION
---

$(cat "$REPO/skills/$SKILL_DIR/SKILL.md")
CMDEOF

  # Run claude -p from sandbox, capture stream-json, look for Read calls to the target file
  HIT_FILE="$SANDBOX/.e1-hit"
  (cd "$SANDBOX" && CLAUDECODE= claude -p "$QUERY" \
    --output-format stream-json \
    --model "$MODEL" \
    --verbose \
    --max-turns 5 \
    2>/dev/null \
    < /dev/null) | \
  python3 -c "
import sys, json, pathlib
hit_file = pathlib.Path('$SANDBOX/.e1-hit')
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        continue
    if event.get('type') == 'assistant':
        for item in event.get('message', {}).get('content', []):
            if item.get('type') == 'tool_use' and item.get('name') == 'Read':
                path = item.get('input', {}).get('file_path', '')
                if '$TARGET_FILE' in path:
                    hit_file.write_text(path)
    if event.get('type') == 'stream_event':
        se = event.get('event', {})
        if se.get('type') == 'content_block_delta':
            delta = se.get('delta', {})
            if delta.get('type') == 'input_json_delta':
                pj = delta.get('partial_json', '')
                if '$TARGET_FILE' in pj:
                    hit_file.write_text('stream-hit')
" || true

  if [ -f "$HIT_FILE" ]; then
    echo "  run $i: READ $TARGET_FILE ✓"
    hits=$((hits + 1))
  else
    echo "  run $i: did NOT read $TARGET_FILE"
  fi

  rm -rf "$SANDBOX"
done

echo ""
echo "Result: $hits/$RUNS reads of $TARGET_FILE"
echo "Skill: $SKILL_NAME"
echo "Query: $QUERY"
[ "$hits" -gt 0 ] && exit 0 || exit 1
