---
name: engine-check
description: Use this skill to validate repo health before starting work. It checks that required files, tools, and services are present and functional. Run at session start or after major structural changes.
---

# Engine Check

Scope: General.

Use this skill to validate that an SVE-compliant repository has the required structural files, tools, and service connectivity before beginning work.

## What It Validates

1. **Required Files**: Constitution/protocol file exists, skill definitions are present, scripts are available
2. **Tool Availability**: python3, project-specific build tools
3. **Service Connectivity**: Muninn MCP bootstrap (if configured)
4. **Docs Structure**: Architecture docs hub, metadata anchors
5. **Test Baselines**: Project builds and tests pass at baseline

## When to Run

- At the start of a new session (after Muninn bootstrap)
- After major structural refactors
- Before declaring a slice complete (as part of slice-closeout)
- When onboarding a new agent to the repo

## Implementation

Run `scripts/engine-check.sh` from the repo root. The script will:
- Check for required SVE structural files
- Verify tool availability
- Run Muninn bootstrap gate
- Run docs metadata checks
- Run project build/test baselines

## Output Expectations

Report:

- PASS/FAIL for each check
- Total failure count
- Exit code 0 (all pass) or 1 (any failures)
