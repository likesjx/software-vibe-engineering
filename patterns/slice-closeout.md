# Slice Close-Out

> Every implementation slice must be explicitly closed with verification, documentation, and a reality gap note.

---

## What is a Slice?

A slice is the smallest coherent unit of implementation work. It is not a feature, not a sprint, not a PR. It is a single bounded change that can be verified, committed, and documented independently.

## The Close-Out Protocol

Every slice must produce all five artifacts before it is considered complete:

### 1. Proposal/Spec Update
Update the relevant architecture proposal disposition. If the slice changes behavior, the spec must reflect it.

### 2. Smallest Coherent Code Change
No multi-concern sprawl. One slice, one concern. If you find yourself touching unrelated files, you've exceeded the slice boundary.

### 3. Verification
Run the appropriate rung of the verification ladder:
- `test-green` at minimum
- `smoke-green` if IPC/networking is involved
- `watched-live` if concurrency/supervision is involved

### 4. Descriptive Commit and Push
The commit message is part of the system's historical record. It must describe what changed, why, and at what verification level.

### 5. Reality Gap Note
Document what was missed or harder than expected. This is not optional. Every slice teaches the system something about the gap between assumptions and reality.

## The Seam Statement

After close-out, the agent must state the **next seam**: what the next agent (or next session) should pick up. This feeds directly into the bootstrap protocol's continuity requirement.

## Task Tracking

Update `docs/task.md` (or equivalent) with:
- Completed work
- Real follow-ups (not aspirational wish lists)
- Any unresolved questions or risks

## Implementation

In the Philotic Stack, slice close-out is enforced via the `philotic-slice-closeout` skill in `skills/philotic-slice-closeout/SKILL.md`.

---

*Pattern defined by Jared & Antigravity, March 2026.*
