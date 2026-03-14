# Software Vibe Engineering (SVE)

> The practice of constraining stochastic LLMs with rigid epistemic boundaries to produce deterministic, sovereign software systems.

**Created by Jared & Antigravity**

---

## What is Software Vibe Engineering?

The software industry has exited the "Chat-and-Commit" era. Traditional vibe coding—throwing natural language at an LLM and hoping the output builds—collapses under entropy at scale.

**Software Vibe Engineering (SVE)** takes the raw creative velocity of Large Language Models and forces it through rigid, sovereign thermodynamic boundaries. You don't ask the fluid to build the pipe. The human builds the rigid epistemological pipe, and the AI fluid provides immense kinetic velocity within those explicitly defined limits.

SVE treats LLMs as high-pressure fluid dynamics, not oracles.

---

## Core Principles

### 0. Epistemology: Bounding the Stochastic
LLMs are stochastic probability engines. They output maximal statistical plausibility, not truth. When complexity crosses a critical threshold, plausibility manifests as structural hallucinations. SVE bounds this with explicit architectural constraints.

### 1. The Constitution (`AGENTS.md`)
A centralized protocol that governs agent behavior: one canonical owner per state type, mandatory honest pushback, slice contracts with verification requirements. Agents don't ask what to do—they read the sovereign protocol.

### 2. Mandatory Bootstrap: The Continuity Handshake
Amnesia kills agentic productivity. Every session begins with a mandatory bootstrap where the agent must prove three things:
- **Identity** – Who am I?
- **Directive** – What are my constraints?
- **Continuity Seam** – Where did the previous agent leave off?

No proof, no write access.

### 3. Muninn: Heuristic Context Mesh
Semantic memory is externalized into MuninnDB, a shared heuristic mesh across agents and sessions:
- **Cross-Conversation Recall** – Retrieve reality gaps from sessions ago
- **Token Optimization** – Query only load-bearing context, never dump the whole codebase

### 4. Bounded Skills (`SKILL.md`)
File-based executable contracts that define exact operational steps AND explicit negative boundaries (what the skill does NOT own). Prevents rogue agents from hallucinating sweeping refactors.

Core skills include:
- `philotic-slice-closeout` – Forces operational closure and disposition updates
- `verification-ladder` – Governs validation depth and confidence classification
- `muninn-memory-habit` – Mandatory bootstrap and context compression across sessions

### 5. Verification Ladder: The Confidence Contract
Confidence is measurable, not heuristic. Every mutation must clear specific rungs:

| Rung | Description |
|------|-------------|
| `test-green` | Isolated crate/unit contract tests pass |
| `smoke-green` | Binary execution scripts validate against live sockets |
| `watched-live` | Physically observe materialized runtime and log output |

### 6. Workstream Isolation: Parallel Sub-Minds
Agents operate in completely sandboxed git worktrees. Multiple agents can build different services concurrently in the same repository, converging only when slices prove safe to merge.

### 7. The Reality Gap Loop
The self-tuning mechanism. At slice close-out, agents flag where human assumptions failed against machine reality. These gaps become new standing rules in the constitution. With every commit, the engine rewrites its own brain.

---

## Reference Implementation: The Philotic Stack

The canonical implementation of SVE is the **Philotic Dev Engine**:

- **Source Code**: [github.com/likesjx/philotic-stack](https://github.com/likesjx/philotic-stack)
- **Architecture Docs**: [The Philotic Engine Blueprint](https://test.jaredlikes.com/philotic-engine/)

### Stack Overview

| Component | Role |
|-----------|------|
| `ansible/` | Rust hotel daemon – materializes agents, manages IPC + mesh |
| `crates/` | Core Rust crates for the runtime |
| `skills/` | Bounded skill contracts (slice-closeout, verification-ladder, muninn-habit) |
| `docs/` | Architecture proposals, task tracking, port blueprints |
| `scripts/` | Automation and git hooks |
| `AGENTS.md` | The Constitution – sovereign agent protocol |
| `CLAUDE.md` | Agent-specific operating directives |

### Engine Telemetry

The Philotic Engine tracks real-time sovereign metrics:
- **Total Structural Mass (LOC)** – Full codebase weight
- **24H Cognitive Velocity** – Lines changed in rolling window
- **Muninn Sync Events** – Memory read/write operations
- **Context Density** – Ratio of load-bearing context to total tokens

### Tech
- **Language**: Rust (94.7%), Shell, Python
- **Memory**: MuninnDB (sovereign, decay-based cognitive memory)
- **Agents**: Antigravity (operational), Codex (architectural), Claude (refactoring)
- **Contributors**: 2 (likesjx + Claude)
- **Commits**: 168+

---

## Quick Start

```bash
# Clone the reference implementation
git clone https://github.com/likesjx/philotic-stack.git
cd philotic-stack

# Read the constitution first
cat AGENTS.md

# Explore the skills
ls skills/
```

---

## Repository Structure

```
software-vibe-engineering/
├── README.md              # This file – SVE philosophy and patterns
├── CONSTITUTION.md        # Tool-agnostic agent governance rules
├── patterns/
│   ├── stateful-vibe-engineering.md
│   ├── muninn-memory-mesh.md
│   ├── verification-ladder.md
│   └── slice-closeout.md
└── engines/
    └── philotic-stack.md    # Reference engine docs
```

---

## The Standard

Stateful Vibe Engineering turns stochastic prediction into deterministic engineering. The chaos is bounded. The pipeline hums.

**THE ENGINE IS RUNNING.**

---

*© 2026 Software Vibe Engineering • Engineered by Jared & Antigravity*
