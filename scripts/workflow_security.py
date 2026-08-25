#!/usr/bin/env python3
"""Fail-closed security checks for GitHub Actions workflows."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


for path in sorted(WORKFLOWS.glob("*.y*ml")):
    text = path.read_text(encoding="utf-8")

    # A public read-only repository must never execute attacker-controlled
    # workflow definitions with write-capable credentials.
    if re.search(r"(?m)^\s*pull_request_target\s*:", text):
        fail(path, "pull_request_target is forbidden")
    if re.search(r"(?m)^\s*workflow_run\s*:", text):
        fail(path, "workflow_run is forbidden in the public read-only layer")
    if re.search(r"(?m)^\s*(contents|actions|checks|issues|pull-requests|id-token)\s*:\s*write\s*$", text):
        fail(path, "write-capable GitHub permission is forbidden")
    if re.search(r"(?m)^\s*permissions\s*:\s*$", text) and "contents: read" not in text:
        fail(path, "workflow must explicitly contain contents: read")
    if re.search(r"(?m)^\s*runs-on:\s*self-hosted", text):
        fail(path, "self-hosted runners are forbidden")

    # Third-party actions must be immutable commit references, not movable tags.
    for match in re.finditer(r"(?m)^\s*uses:\s*([^\s#]+)", text):
        ref = match.group(1).split("@", 1)[-1]
        if not re.fullmatch(r"[0-9a-fA-F]{40}", ref):
            fail(path, f"action is not pinned to a full commit SHA: {match.group(1)}")

    if "secrets." in text:
        fail(path, "repository secrets are forbidden in SPACE-READ CI")
    if re.search(r"(?i)curl[^\n|]*\|\s*(bash|sh)", text):
        fail(path, "remote shell execution is forbidden")
    if re.search(r"(?i)wget[^\n|]*\|\s*(bash|sh)", text):
        fail(path, "remote shell execution is forbidden")

if errors:
    print("WORKFLOW SECURITY FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)

print("WORKFLOW SECURITY OK")
