---
name: muninn-memory-habit
description: HIGH PRIORITY. Use this skill at the START of EVERY session to retrieve project context and during the session to store decisions. It is the mandatory bootstrap mechanism for continuity and the engine for project optimization. Retrieve before meaningful work, write back important decisions, and use revealed gaps to improve repo-local protocols.
---

# Muninn Memory Habit

Use this skill when Muninn is part of the active workflow.

## Goal

Treat Muninn as a working memory habit, not a ceremonial sidecar.

The objective is to test whether regular retrieval and write-back improve:
- continuity
- personalization
- design recall
- context compression

When Muninn MCP is configured and reachable, this habit is the MANDATORY BOOTSTRAP STEP defined in the project constitution. It is not an optional flourish.

## The Bootstrap Sequence

At the start of every session (before responding to the user):
1.  **Bootstrap Muninn**: run `python3 scripts/muninn_mcp.py bootstrap`
2.  **If bootstrap fails**: alert the user/operator immediately and do not continue without explicit approval
3.  **Recall Self**: `muninn_recall(identity, operating_posture)`
4.  **Recall User**: `muninn_recall(user_preferences, collaboration_style)`
5.  **Recall Topic**: `muninn_where_left_off` + `muninn_recall(active_goal, architecture_decisions)`
6.  **Orient**: Summarize how the recalled context shapes your plan for the current turn.

## Failure Rule

If the shared helper or Muninn MCP is unavailable or cannot be recovered automatically:

- say so immediately
- do not imply memory retrieval occurred
- pause and require explicit approval before proceeding without Muninn
- if approval is granted, say clearly that you are continuing on observed repo/runtime truth only

## Memory Triad

Prefer organizing memory around three questions:

1. Who am I?
- agent identity
- stable operating style
- collaboration posture

2. Who am I talking to?
- user preferences
- collaboration fit
- recurring needs or dislikes

3. What matters about this topic right now?
- active goals
- architecture decisions
- unresolved seams
- relevant facts or constraints

## Default Habit

Good (atomic, one concept):
- "User prefers terse status updates over narrative"
- "The routing layer uses correlation IDs, not request IDs"

Bad (too dense):
- "The system has three kinds with multiple tiers and complex IPC..."

## What to Store

One concept. One memory.

Good candidates:
- a single architectural decision and its one-sentence rationale
- a single user preference
- a single gotcha or risk
- a single "do not do X" rule

Avoid:
- summaries of whole proposals (the proposal file already exists)
- long verbatim logs
- anything that duplicates what's in a committed doc

## Retrieval and Projection

When Muninn returns relevant memory, treat it as projected context, not absolute truth.

- summarize it succinctly
- use it to shape the answer or plan
- keep a distinction between:
  - recalled memory
  - current observed repo/runtime truth

If recalled memory conflicts with current code or docs, trust current observed truth and note the mismatch.

## Suggested Workflow

1. Determine whether the turn is meaningful enough for retrieval.
2. Retrieve along the triad:
- self
- user
- topic
3. Use the recalled memory to shape planning or explanation.
4. After the turn, write back any durable learning.

## The Optimization Loop

Use memory to proactively improve the repository:

1.  **Identify Protocol Gaps**: If a memory surfaces a recurring error, do not just fix the code.
2.  **Evaluate Protocol**: Check if the constitution or a SKILL.md needs a new rule to prevent the error.
3.  **Update Repo**: Apply the improvement to the local markdown documentation.
4.  **Note the Optimization**: Store the update as a new memory.

## Honesty Rule

Do not claim Muninn improved continuity unless retrieval actually influenced the turn.

If Muninn was not consulted, say so.
If Muninn returned irrelevant memory, say so.
If the habit is too heavy, say so.
If Muninn was unavailable, say so immediately and note whether the user approved continuing without it.

The experiment is about whether the memory helps, not about pretending it helped.
