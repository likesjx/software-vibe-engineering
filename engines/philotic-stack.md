# Philotic Stack Engine

> The canonical reference implementation of Software Vibe Engineering.

---

## Overview

The Philotic Stack is a sovereign multi-agent development engine built in Rust. It is the first and reference implementation of the SVE specification.

- **Repository**: [github.com/likesjx/philotic-stack](https://github.com/likesjx/philotic-stack)
- **Architecture Blueprint**: [test.jaredlikes.com/philotic-engine](https://test.jaredlikes.com/philotic-engine/)
- **Language**: Rust (94.7%), Shell (3.0%), Python (1.6%)
- **Commits**: 168+
- **Contributors**: likesjx (human supervisor) + Claude (refactoring agent)

## Architecture

| Directory | Purpose |
|-----------|----------|
| `ansible/` | The "hotel daemon" – Rust runtime that materializes guest agents and manages IPC + mesh communication |
| `crates/` | Core Rust crates powering the runtime |
| `skills/` | Bounded skill contracts (`philotic-slice-closeout`, `verification-ladder`, `muninn-memory-habit`) |
| `docs/` | Architecture proposals, task tracking, port blueprints |
| `scripts/` | Automation, git hooks, deployment helpers |
| `.githooks/` | Deterministic pre-push hooks |
| `AGENTS.md` | The Constitution – sovereign agent protocol |
| `CLAUDE.md` | Agent-specific operating directives |

## Sovereign Agents

The Philotic Stack currently runs three named agents:

| Agent | Role | Contribution |
|-------|------|--------------|
| **Antigravity** | Operational Agent | 14 verifications, 1 deploy |
| **Codex** | Architectural Agent | 12 proposals, 4 core slices |
| **Claude** | Refactoring Generalist | ~3.2k LOC scaffolding |

## Memory Integration

The stack uses [MuninnDB](https://github.com/scrypter/munnindb) as its heuristic context mesh:
- Cross-conversation recall across all agents
- Token-optimized "load-bearing context" retrieval
- Connected via MCP, REST, and gRPC

## Live Telemetry

The engine tracks real-time metrics:
- **Total Structural Mass**: ~288,874 LOC
- **24H Cognitive Velocity**: ~7,927 lines/day
- **Muninn Sync Events**: 173
- **Context Density**: 92.4%

## Quick Start

```bash
git clone https://github.com/likesjx/philotic-stack.git
cd philotic-stack

# Read the constitution
cat AGENTS.md

# Explore skills
ls skills/

# Review architecture
cat docs/
```

## Relationship to SVE

The Philotic Stack is **one implementation** of SVE. The patterns documented in this repository (`software-vibe-engineering`) are tool-agnostic and can be implemented with different runtimes, languages, and memory systems. Philotic Stack proves the patterns work at scale in Rust with MuninnDB.

---

*Engine built by Jared & Antigravity, March 2026.*
