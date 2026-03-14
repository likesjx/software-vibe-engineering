# Verification Ladder

> Confidence is not a heuristic. It is a measurable ladder.

---

## The Problem

In traditional vibe coding, "it works" means "I ran it once and it didn't crash." This is not verification. This is hope.

When agents self-report confidence without a measurable standard, they hallucinate certainty the same way they hallucinate code.

## The Ladder

Every mutation to the system must clear specific rungs:

| Rung | Name | Standard | When to Use |
|------|------|----------|-------------|
| 1 | `test-green` | Isolated crate/unit contract tests pass | Every code change |
| 2 | `smoke-green` | Binary execution scripts validate against live sockets | Changes to IPC, networking, routing |
| 3 | `watched-live` | Human or agent physically observes materialized runtime and log output | Concurrency, supervision, environment behavior |

## Decision Rules

**Climb the ladder** when the change affects:
- Inter-process communication (IPC)
- Networking or socket behavior
- Concurrency or parallelism
- Supervision trees
- Routing or delivery
- Materialization of runtime objects
- Environment behavior or configuration

**Stay at current rung** when the change is:
- Pure refactoring with no behavioral change
- Documentation only
- Test-only changes

## Output Expectations

At slice close-out, the agent must report:
1. Which rungs were run
2. What passed
3. What remains unverified
4. The **highest honest confidence level** achieved

The key word is "honest." An agent that claims `watched-live` when it only achieved `test-green` is in violation of the constitution.

## Implementation

In the Philotic Stack, the verification ladder is enforced via the `verification-ladder` skill in `skills/verification-ladder/SKILL.md`.

---

*Pattern defined by Jared & Antigravity, March 2026.*
