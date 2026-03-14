# SVE Skills

> Bounded, file-based executable contracts that govern agent behavior.

Skills are the operational backbone of Software Vibe Engineering. Each skill defines:
- **What it does** (the exact workflow)
- **What it does NOT own** (the explicit negative boundary)
- **When to trigger it**
- **What to report when done**

## Skill Anatomy

Every skill lives in its own directory with a `SKILL.md` file:

```
skills/
  slice-closeout/SKILL.md
  verification-ladder/SKILL.md
  memory-habit/SKILL.md
  proposal-maintainer/SKILL.md
  architecture-docs-maintainer/SKILL.md
  runtime-debugger/SKILL.md
  runtime-materialization/SKILL.md
  subagent-delegation/SKILL.md
  memory-protocol/SKILL.md
```

## Skill Categories

### Core Workflow Skills
| Skill | Scope | Purpose |
|-------|-------|----------|
| `slice-closeout` | General | Close every implementation slice with verification, docs, and reality gap |
| `verification-ladder` | General | Decide validation depth and report honest confidence |
| `proposal-maintainer` | General | Keep proposals concise, current, and linked to tasks |

### Memory Skills
| Skill | Scope | Purpose |
|-------|-------|----------|
| `memory-habit` | General | Mandatory bootstrap + session memory read/write via shared memory mesh |
| `memory-protocol` | General | Low-level memory operations, atomicity rules, and tagging |

### Documentation Skills
| Skill | Scope | Purpose |
|-------|-------|----------|
| `architecture-docs-maintainer` | Project-specific | Keep frontmatter, domains, status truth, and cross-links aligned |

### Runtime Skills
| Skill | Scope | Purpose |
|-------|-------|----------|
| `runtime-debugger` | General | Debug live runtime behavior (IPC, sockets, processes) |
| `runtime-materialization` | Project-specific | Materialize and validate runtime objects |

### Orchestration Skills
| Skill | Scope | Purpose |
|-------|-------|----------|
| `subagent-delegation` | General | Rules for spawning foreground/background sub-agents |

## How Skills Interlock

Skills reference each other to prevent scope creep:
- `slice-closeout` calls `verification-ladder` for confidence, `proposal-maintainer` for disposition
- `memory-habit` calls `subagent-delegation` for async memory writes
- `architecture-docs-maintainer` calls `proposal-maintainer` for generic proposal hygiene

## Creating Your Own Skills

Use the template in `skills/_template/SKILL.md` as a starting point.

Every skill MUST define:
1. A `name` and `description` header
2. A "This skill owns" list
3. A "This skill does not own" list
4. A workflow section
5. Output expectations

---

*Skills are living contracts. They evolve through the Reality Gap Loop.*
