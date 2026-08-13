#!/usr/bin/env bash
# Smoke-test the migration validators against the bundled fixtures.
#
# Each case asserts an exit code, so a fixture that starts passing when it
# should fail is caught as loudly as one that starts failing. Run this after
# any change to the validators, the templates, or the ledger schema.
#
# Usage: scripts/run_fixtures.sh

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

F=assets/fixtures
S=scripts
pass=0
fail=0

expect() {
  local want="$1"; shift
  local label="$1"; shift
  "$@" >/dev/null 2>&1
  local got=$?
  if [ "$got" -eq "$want" ]; then
    printf '  ok    %s\n' "$label"
    pass=$((pass + 1))
  else
    printf '  FAIL  %s (expected exit %s, got %s)\n' "$label" "$want" "$got"
    fail=$((fail + 1))
  fi
}

echo "profile validation"
expect 0 "approved profile passes execute-mode validation" \
  python3 $S/validate_profile.py $F/profile.approved.valid.yaml
expect 0 "approved profile also passes draft validation" \
  python3 $S/validate_profile.py $F/profile.approved.valid.yaml --allow-unratified
expect 1 "unratified profile is rejected for execute mode" \
  python3 $S/validate_profile.py $F/profile.unratified.invalid-for-execute.yaml
expect 1 "placeholder token is caught in execute mode" \
  python3 $S/validate_profile.py $F/profile.unratified.invalid-for-execute.yaml
expect 1 "team maintainer_model is rejected" \
  python3 $S/validate_profile.py $F/profile.team-maintainer.rejected.yaml --allow-unratified

echo "disposition ledger validation"
expect 0 "pre-write ledger passes with a proposed issue title" \
  python3 $S/validate_disposition.py $F/ledger.pre-write.valid.yaml --pre-write
expect 1 "pre-write ledger is rejected at final: no real issue number" \
  python3 $S/validate_disposition.py $F/ledger.pre-write.valid.yaml
expect 0 "final ledger passes once issues exist" \
  python3 $S/validate_disposition.py $F/ledger.final.valid.yaml
expect 0 "draft ledger passes while a decision is outstanding" \
  python3 $S/validate_disposition.py $F/ledger.draft.awaiting-decision.yaml --allow-awaiting-decision
expect 1 "outstanding decision blocks strict validation" \
  python3 $S/validate_disposition.py $F/ledger.draft.awaiting-decision.yaml
expect 2 "mutually exclusive flags are refused" \
  python3 $S/validate_disposition.py $F/ledger.final.valid.yaml --allow-awaiting-decision --pre-write

echo "fingerprint verification"
expect 0 "recorded fingerprints match the fixture repository" \
  python3 $S/verify_fingerprints.py $F/ledger.final.valid.yaml --repository-root $F/repo
expect 1 "a stale fingerprint is detected" \
  python3 $S/verify_fingerprints.py $F/ledger.stale-fingerprint.invalid.yaml --repository-root $F/repo
expect 1 "an unreadable declared source is detected" \
  python3 $S/verify_fingerprints.py $F/ledger.final.valid.yaml --repository-root /nonexistent

printf '\n%s passed, %s failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
