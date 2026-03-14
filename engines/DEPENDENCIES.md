# Philotic Stack Dependencies

External tools, services, and libraries that the Philotic Stack engine depends on. This is a direct audit of the codebase as of March 2026.

---

## Tier 1: SVE-Critical (Required for the Methodology)

These are dependencies that directly support the SVE workflow — memory, task management, and development orchestration.

### MuninnDB
- **What**: Cognitive semantic memory database. Stores "engrams" (memory traces) with decay, activation, and semantic search. Not a vector store or graph DB — a new class of memory-native storage.
- **Repo**: [scrypster/muninndb](https://github.com/scrypster/muninndb)
- **Role in SVE**: Powers the Muninn Memory Mesh pattern. Every agent session bootstraps by recalling context from Muninn. Session-start is gated on Muninn availability — if it's down, work stops.
- **Protocol**: MCP (Model Context Protocol) over HTTP, default `localhost:8750/mcp`
- **Key tools exposed**: `muninn_where_left_off`, `muninn_recall`, `muninn_remember`, `muninn_decide`
- **Ships as**: Single binary with embedded ONNX model for semantic search
- **Integration**: `scripts/muninn_mcp.py` (Python MCP client), `just session-start` gates on it

### just (justfile)
- **What**: Command runner (like make, but sane). Defines project-level recipes.
- **Repo**: [casey/just](https://github.com/casey/just)
- **Role in SVE**: The entire development workflow is orchestrated through `just` commands — build, test, smoke tests, session bootstrap, workstream management, deployment.
- **Key recipes**: `just session-start`, `just build`, `just check`, `just test`, `just engine-check`, `just workstream-start`, `just start-ansible`
- **Install**: `cargo install just` or `brew install just`

### Claude Code (claude.ai/code)
- **What**: AI coding agent from Anthropic
- **Role in SVE**: Primary agent that consumes CLAUDE.md and AGENTS.md standing protocols. The skills, memory habits, and proposal workflow are designed for Claude Code sessions.
- **Integration**: `CLAUDE.md` (session bootstrap), `AGENTS.md` (standing protocol), skills directory

---

## Tier 2: Runtime Infrastructure (Required for the Philotic Stack Specifically)

These are Rust ecosystem dependencies that power the distributed agent OS itself.

### Core Async Runtime
| Crate | Version | Purpose |
|-------|---------|---------|
| `tokio` | 1.42 | Async runtime (multi-thread, IPC, networking, timers) |
| `serde` / `serde_json` | 1.0 | Serialization — everything is JSON over IPC |
| `anyhow` | 1.0 | Error handling |
| `tracing` / `tracing-subscriber` | 0.1 / 0.3 | Structured logging and diagnostics |
| `clap` | 4.5 | CLI argument parsing |

### Networking & API
| Crate | Version | Purpose |
|-------|---------|---------|
| `reqwest` | 0.12 | HTTP client (model API calls, multipart, TLS) |
| `axum` | 0.7 | HTTP server framework (hotel daemon API, blob store) |
| `tower-http` | 0.5 | HTTP middleware (CORS, file serving, tracing) |
| `webrtc` | 0.17.1 | Peer-to-peer mesh communication between hotels |

### Storage & Crypto
| Crate | Version | Purpose |
|-------|---------|---------|
| `rusqlite` | 0.37 | SQLite — the Context Graph backing store (bundled) |
| `aes-gcm` | 0.10 | AES-256-GCM encryption for mesh beacons and vault |
| `sha2` | 0.10 | Hashing for content-addressed blob store |
| `hmac` | 0.12 | HMAC-PSK for mesh beacon authentication |
| `uuid` | 1.x | Identity for sessions, guests, messages |

### Other
| Crate | Version | Purpose |
|-------|---------|---------|
| `async-trait` | 0.1 | Async trait support (storage traits, client SDK) |
| `base64` | 0.22 | Encoding for mesh transport and blob payloads |
| `pulldown-cmark` | 0.13 | Markdown parsing (membrane gateway) |
| `bincode` | 1.3 | Binary serialization for mesh beacon messages |
| `hex` | 0.4 | Hex encoding utilities |
| `log` | 0.4 | Logging facade (mesh-core layer) |

---

## Tier 3: Development & Operations Tooling

### Rust Toolchain
- `cargo` — build system and package manager
- `cargo fmt` — code formatting
- `cargo test` — test runner
- Edition: 2024 (most crates), 2021 (tool-runner, ansible-mesh-core)

### Python 3
- Required for helper scripts: `muninn_mcp.py`, `docs-metadata-check.py`, `secret-push-check.py`
- No external Python packages needed (stdlib only: `urllib`, `json`, `argparse`, `subprocess`, `pathlib`)

### Ansible (deployment)
- Used for mesh node deployment to remote hosts
- Playbooks in `ansible/` directory
- `just ansible-deploy` runs `ansible-playbook deploy_mesh_node.yml`

### Git Worktrees
- Parallel workstream management uses `git worktree` for sibling checkouts
- Scripts: `codex-worktree.sh`, `codex-workstream.sh`
- Convention: one active implementation thread per worktree, one `codex/<slug>` branch per worktree

### Shell Utilities
- `pkill` — process management for local stack
- `bash` — all scripts are bash
- Standard Unix tools: `rm`, `ps`, `grep`, `cd`

---

## Tier 4: External Services (API Keys Required)

| Service | Purpose | Where Configured |
|---------|---------|-----------------|
| Google Gemini API | Primary LLM for agent cognitive loop | OAuth via `just gemini-oauth-start`, mesh-config.json |
| ElevenLabs API | Voice synthesis for model-router | mesh-config.json |
| Telegram Bot API | External user-facing gateway (membrane) | mesh-config.json, bot token |

---

## Configuration Files

| File | Purpose |
|------|---------|
| `mesh-config.json` | Hotel daemon configuration (guests, API keys, mesh peers) |
| `CLAUDE.md` | Session bootstrap instructions for Claude Code |
| `AGENTS.md` | Standing protocol for all coding agents |
| `justfile` | Development command recipes |
| `.githooks/` | Repo-local git hooks (secret scanning) |
