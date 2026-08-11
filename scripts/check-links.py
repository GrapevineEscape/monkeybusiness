#!/usr/bin/env python3
"""Validate the documentation cross-reference web.

This repository is a "mindflow" of interlinked Markdown planning docs. The one
thing worth checking automatically is that every relative link between docs
actually resolves, so the web of cross-references stays trustworthy as it grows.

Only relative links are checked. External URLs (http/https/mailto/tel) and
pure in-page anchors (#section) are ignored, so the check is deterministic and
runs fully offline. Uses the Python standard library only -- no dependencies.

Exit code: 0 when every relative link resolves, 1 when any are broken.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

# [text](target) and ![alt](target). Captures the raw target (may include a
# trailing "title" and/or #fragment, which we strip below).
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "//")


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(out.stdout.strip())


def tracked_markdown(root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [root / line for line in out.stdout.splitlines() if line]


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    # Drop an optional link title: [text](path "Title") / (path 'Title')
    for quote in ('"', "'"):
        idx = target.find(f" {quote}")
        if idx != -1:
            target = target[:idx].strip()
    return target


def is_external(target: str) -> bool:
    return target.startswith(EXTERNAL_PREFIXES)


def resolve(root: Path, md_file: Path, target: str) -> Path:
    # Strip any #fragment; anchors aren't validated (repo uses none today).
    path_part = target.split("#", 1)[0]
    if path_part.startswith("/"):
        return root / path_part.lstrip("/")
    return (md_file.parent / path_part).resolve()


def main() -> int:
    root = repo_root()
    files = tracked_markdown(root)

    broken: list[tuple[Path, str]] = []
    checked = 0

    for md_file in files:
        text = md_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = clean_target(match.group(1))
            if not target or target.startswith("#") or is_external(target):
                continue
            checked += 1
            dest = resolve(root, md_file, target)
            if not dest.exists():
                broken.append((md_file.relative_to(root), target))

    print(f"Checked {checked} relative links across {len(files)} Markdown files.")
    if broken:
        print(f"\n{len(broken)} broken link(s) found:\n")
        for src, target in broken:
            print(f"  [BROKEN] {src} -> {target}")
        return 1

    print("All relative links resolve. Documentation web is healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
