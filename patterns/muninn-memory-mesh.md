# Muninn Memory Mesh

> Externalized semantic memory that provides continuity across agents and sessions.

---

## The Problem: Amnesia

Every stateless LLM interaction resets cognitive velocity to zero. The agent forgets:
- What was decided and why
- What failed last time (reality gaps)
- The user's preferences and collaboration style
- The architectural state it's supposed to maintain

This is not a minor inconvenience. It is the **death of agentic productivity**.

## The Solution: Heuristic Context Mesh

The Muninn Memory Mesh externalizes agent memory into a shared, queryable database (MuninnDB) that all agents in the system can read from and write to.

### Core Capabilities

**Cross-Conversation Recall**
An agent can retrieve a reality gap discovered by a different agent three sessions ago and apply its learnings to the current task.

**Token Optimization**
Agents never dump an entire codebase into context. Instead, they query Muninn to retrieve only "load-bearing context" — the specific memories, decisions, and gaps that are relevant to the current slice.

**Decay and Activation**
MuninnDB implements cognitive memory dynamics: memories strengthen with use, fade when unused, and activate based on contextual relevance (Ebbinghaus decay, Hebbian strengthening, Bayesian confidence).

## The Bootstrap Sequence

At the start of every session, agents must:
1. **Recall Self** – `muninn_recall(identity, operating_posture)`
2. **Recall User** – `muninn_recall(user_preferences, collaboration_style)`
3. **Recall Topic** – `muninn_where_left_off` + `active_goal`
4. **Orient** – Summarize how the recalled context shapes the current plan

## Memory Write Protocol

- All memory writes are delegated to background sub-agents (main thread never blocks)
- One concept per memory, 1–3 sentences max
- Good: "active_incarnation is the primitive for session switching"
- Bad: A 500-word dump of everything that happened

## The Reality Gap Feed

Every reality gap discovered during a slice is written to Muninn. Over time, this creates a living record of where assumptions fail, which agents and future sessions can query to avoid repeating mistakes.

## Implementation

SVE uses [MuninnDB](https://github.com/scrypter/munnindb) as its memory mesh, connected via MCP, REST, and gRPC.
