#!/usr/bin/env bash
set -euo pipefail

# SVE Engine Check
# Validates that an SVE-compliant repository has required structural files,
# tools, and service connectivity.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MUNINN_BASE_URL="${MUNINN_MCP_BASE_URL:-http://localhost:8750/mcp}"

FAILURES=0

pass() {
  printf 'PASS %s\n' "$1"
}

fail() {
  printf 'FAIL %s\n' "$1" >&2
  FAILURES=$((FAILURES + 1))
}

check_file() {
  local path="$1"
  local label="$2"

  if [[ -f "${ROOT_DIR}/${path}" ]]; then
    pass "${label}"
  else
    fail "${label} (missing ${path})"
  fi
}

run_check() {
  local label="$1"
  shift

  if "$@"; then
    pass "${label}"
  else
    fail "${label}"
  fi
}

printf 'SVE Engine Check\n'
printf 'Root: %s\n' "$ROOT_DIR"
printf 'Muninn MCP: %s\n' "$MUNINN_BASE_URL"
printf '\n'

# --- Required SVE structural files ---
check_file "CONSTITUTION.md" "SVE constitution is present"
check_file "scripts/muninn_mcp.py" "shared Muninn helper is present"
check_file "scripts/docs-metadata-check.py" "docs metadata helper is present"
check_file "scripts/secret-push-check.py" "secret push checker is present"

# --- Core skills ---
check_file "skills/muninn-memory-habit/SKILL.md" "muninn-memory-habit skill is present"
check_file "skills/proposal-maintainer/SKILL.md" "proposal-maintainer skill is present"
check_file "skills/architecture-docs-maintainer/SKILL.md" "architecture-docs-maintainer skill is present"
check_file "skills/verification-ladder/SKILL.md" "verification-ladder skill is present"
check_file "skills/slice-closeout/SKILL.md" "slice-closeout skill is present"
check_file "skills/runtime-debugger/SKILL.md" "runtime-debugger skill is present"
check_file "skills/engine-check/SKILL.md" "engine-check skill is present"

# --- Tool availability ---
if command -v python3 >/dev/null 2>&1; then
  pass "python3 is available for helper scripts"
else
  fail "python3 is available for helper scripts"
fi

# --- Muninn MCP connectivity (if configured) ---
if python3 "${ROOT_DIR}/scripts/muninn_mcp.py" --base-url "$MUNINN_BASE_URL" bootstrap >/dev/null 2>&1; then
  pass "Muninn MCP helper passes recoverable bootstrap gate"
else
  fail "Muninn MCP helper passes recoverable bootstrap gate"
fi

# --- Docs metadata checks ---
if python3 "${ROOT_DIR}/scripts/docs-metadata-check.py" >/dev/null 2>&1; then
  pass "docs metadata checks pass"
else
  fail "docs metadata checks pass"
fi

printf '\n'
if [[ "$FAILURES" -eq 0 ]]; then
  printf 'Engine check complete: all checks passed.\n'
else
  printf 'Engine check complete: %d check(s) failed.\n' "$FAILURES" >&2
  exit 1
fi
