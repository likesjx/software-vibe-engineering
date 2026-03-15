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
Semantic memory is externalized into a shared heuristic mesh across agents and sessions:
- **Cross-Conversation Recall** – Retrieve reality gaps from sessions ago
- **Token Optimization** – Query only load-bearing context, never dump the whole codebase

### 4. Bounded Skills (`SKILL.md`)
File-based executable contracts that define exact operational steps AND explicit negative boundaries (what the skill does NOT own). Prevents rogue agents from hallucinating sweeping refactors.

Core skills include:
- `slice-closeout` – Forces operational closure and disposition updates
- `verification-ladder` – Governs validation depth and confidence classification
- `muninn-memory-habit` – Mandatory bootstrap and context compression across sessions
- `proposal-maintainer` – Keeps architecture proposals current and linked to tasks
- `architecture-docs-maintainer` – Maintains frontmatter, domains, and doc cross-links
- `runtime-debugger` – Structured live-stack debugging when tests aren't enough
- `engine-check` – Validates repo health: required files, tool availability, test baselines

### 5. Verification Ladder: The Confidence Contract
Confidence is measurable, not heuristic. Every mutation must clear specific rungs:

| Rung | Description |
|------|-------------|
| `test-green` | Isolated unit/contract tests pass |
| `smoke-green` | Binary execution scripts validate against live sockets |
| `watched-live` | Physically observe materialized runtime and log output |

### 6. Workstream Isolation: Parallel Sub-Minds
Agents operate in completely sandboxed git worktrees. Multiple agents can build different services concurrently in the same repository, converging only when slices prove safe to merge.

### 7. The Reality Gap Loop
The self-tuning mechanism. At slice close-out, agents flag where human assumptions failed against machine reality. These gaps become new standing rules in the constitution. With every commit, the engine rewrites its own brain.

---

## Repository Structure

```
software-vibe-engineering/
├── README.md                        # This file – SVE philosophy and patterns
├── CONSTITUTION.md                  # Tool-agnostic agent governance rules
├── patterns/
│   ├── stateful-vibe-engineering.md # The core SVE pattern
│   ├── muninn-memory-mesh.md        # Externalized semantic memory
│   ├── verification-ladder.md       # Confidence measurement ladder
│   └── slice-closeout.md            # Operational closure protocol
├── skills/
│   ├── README.md                    # Skill registry and categories
│   ├── _template/SKILL.md           # Template for creating new skills
│   ├── slice-closeout/SKILL.md      # End-of-slice closure workflow
│   ├── verification-ladder/SKILL.md # Validation depth selection
│   ├── muninn-memory-habit/SKILL.md # Bootstrap and memory protocol
│   ├── proposal-maintainer/SKILL.md # Proposal hygiene and tracking
│   ├── architecture-docs-maintainer/SKILL.md
│   ├── runtime-debugger/SKILL.md    # Live-stack debugging
│   └── engine-check/SKILL.md        # Repo health validation
├── docs-structure/
│   ├── FRONTMATTER.md               # Document metadata guide
│   ├── PROPOSAL_TEMPLATE.md         # Architecture proposal template
│   └── TASK_SURFACE.md              # Task tracking guide
├── scripts/
│   └── secret-push-check.py         # Pre-push secret scanner
└── .githooks/
    └── pre-push                     # Git hook for secret scanning
```

---

## Quick Start

To adopt SVE in your own project:

1. **Read the Constitution** – Copy `CONSTITUTION.md` into your repo as `AGENTS.md`
2. **Install the skills** – Copy the `skills/` directory into your repo
3. **Set up doc structure** – Use `docs-structure/` templates for proposals and task tracking
4. **Configure git hooks** – Copy `.githooks/` and `scripts/` for secret scanning
5. **Bootstrap every session** – Agents must prove identity, directive, and continuity before writing

---

## The Standard

Stateful Vibe Engineering turns stochastic prediction into deterministic engineering. The chaos is bounded. The pipeline hums.

**THE ENGINE IS RUNNING.**

---

*© 2026 Software Vibe Engineering • Engineered by Jared & Antigravity*
