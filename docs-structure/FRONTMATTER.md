# Frontmatter & Document Tagging

A lightweight metadata strategy so proposals, tasks, and reference docs link together without turning markdown into ceremony.

## Why Frontmatter

Without structured metadata, the linking grammar between docs is social knowledge plus filename recognition. That breaks down as doc volume grows. Frontmatter solves three problems:

1. Cross-cutting concerns are easy to miss
2. Current truth and near-future design link inconsistently
3. Docs become harder to index over time

## Core Principle

Do **not** use frontmatter as a substitute for readable sections in the document body. Metadata helps find the right doc and understand its status quickly. The body carries the actual thinking.

## Minimum Frontmatter Block

Use this on all active architecture and process docs:

```yaml
---
title: "Human readable document title"
doc_type: proposal
domain: your-domain
status: accepted-current-slice
last_updated: 2026-03-12
tags:
  - relevant-tag-1
  - relevant-tag-2
related_docs:
  - OTHER_DOC.md
task_refs:
  - docs/task.md
---
```

## Doc Types

Use these as the controlled `doc_type` vocabulary:

| Type | Use For |
|------|--------|
| `status` | Living truth docs that reflect current system state |
| `reference` | Stable reference material |
| `proposal` | Near-future design intent |
| `seam` | Boundary docs between domains or proposals |
| `task-surface` | Active work tracking |
| `workflow` | Process and methodology docs |
| `historical` | Archived/superseded docs |

## Status Values

For **proposals and seams**:
- `proposed`
- `accepted-current-slice`
- `implemented`
- `superseded`
- `deferred`

For **status, reference, and workflow** docs:
- `active`
- `historical`

## Domains

Every doc declares exactly one primary `domain`. Cross-domain relevance goes in `tags` or `related_docs`, not multi-owner ambiguity.

Define your own domain vocabulary for your project. Examples:
- `runtime-sessions`
- `transport`
- `deployment`
- `workflow-docs` (for repo/process docs, not product architecture)

If a doc feels like it needs two primary domains, that is usually a seam warning worth naming explicitly.

## Proposal-Specific Fields

When the doc is a proposal, add:

```yaml
proposal_id: short-stable-id
implements: []
implemented_by: []
active_seams:
  - seam-name
source_of_truth_targets:
  - STATUS_DOC.md
```

## Tagging Strategy

Keep tags lightweight. Use three families:

1. **Domain-adjacent**: `sessions`, `routing`, `egress`
2. **Planning-shape**: `active-seam`, `current-slice`, `source-of-truth`
3. **Cross-cutting**: `security`, `observability`, `migration`

Rules:
- Prefer 3-6 tags per doc
- Avoid synonyms (`ops` and `operations` both existing)
- Don't encode primary domain in tags if it already exists in `domain`

## Cross-Linking Rules

Every active **proposal** links to:
- One primary status doc
- One task surface
- Adjacent proposals when relevant

Every **status doc** links to:
- Hot proposals or seams it summarizes
- The task surface for immediate work

## Rollout Advice

1. Define your controlled vocabularies first
2. Add frontmatter to highest-value docs first
3. Do **not** retrofit every historical doc in one pass
4. Let the schema prove useful on active docs before mass backfill
