#!/usr/bin/env python3
"""SVE docs metadata checker.

Scans docs/architecture/ for markdown files with YAML frontmatter and
validates that required metadata keys are present. This is a generalized
version that discovers docs dynamically rather than hardcoding file paths.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# Minimum frontmatter keys required for any architecture doc
BASE_KEYS = {
    "title",
    "doc_type",
    "status",
    "last_updated",
}

# Additional keys expected for proposal docs
PROPOSAL_KEYS = BASE_KEYS | {
    "domain",
    "tags",
    "related_docs",
    "task_refs",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        raise ValueError("missing closing frontmatter delimiter")
    data: dict[str, str] = {}
    for raw_line in lines[1:end_idx]:
        if not raw_line.strip():
            continue
        if raw_line.startswith("  ") or raw_line.startswith("- "):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    docs_dir = ROOT / "docs" / "architecture"
    if not docs_dir.is_dir():
        print("docs/architecture/ not found - skipping metadata checks")
        return 0

    failures: list[str] = []
    checked = 0

    for md_file in sorted(docs_dir.glob("**/*.md")):
        rel_path = md_file.relative_to(ROOT)
        try:
            frontmatter = parse_frontmatter(md_file)
        except ValueError:
            # File has no frontmatter - skip silently
            continue

        checked += 1
        name = md_file.name.upper()
        required = PROPOSAL_KEYS if "PROPOSAL" in name else BASE_KEYS
        missing = sorted(required - set(frontmatter))
        if missing:
            failures.append(f"{rel_path}: missing frontmatter keys: {', '.join(missing)}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print(f"docs metadata checks passed ({checked} docs checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
