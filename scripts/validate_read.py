#!/usr/bin/env python3
"""Static integrity checks for SPACE-READ.

The validator is deliberately local and read-only. It must not contact SPACE Core
or any external service.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path}: {exc}")
        return None


manifest = load_json(ROOT / "manifest.json")
index = load_json(ROOT / "PUBLICATION_INDEX.json")
schema = load_json(ROOT / "schema/publication.schema.json")

if isinstance(manifest, dict):
    required = {"name", "schema_version", "status", "access_model", "write_back", "entrypoints"}
    missing = required - manifest.keys()
    if missing:
        fail(f"manifest missing keys: {sorted(missing)}")
    if manifest.get("name") != "SPACE-READ":
        fail("manifest.name must be SPACE-READ")
    if manifest.get("write_back") is not False:
        fail("manifest.write_back must be false")
    if manifest.get("access_model") != "read-only":
        fail("manifest.access_model must be read-only")

if not isinstance(index, dict) or not isinstance(index.get("items"), list):
    fail("PUBLICATION_INDEX.json must contain an items array")
else:
    ids: set[str] = set()
    for item in index["items"]:
        if not isinstance(item, dict):
            fail("publication index item must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str):
            fail("publication item has no string id")
        elif item_id in ids:
            fail(f"duplicate publication id: {item_id}")
        else:
            ids.add(item_id)
        path = item.get("path")
        if isinstance(path, str):
            target = ROOT / path
            if not target.is_file():
                fail(f"publication target does not exist: {path}")
        else:
            fail(f"publication {item_id!r} has no path")

if isinstance(schema, dict):
    if schema.get("type") != "object":
        fail("publication schema root must be an object")

# Detect common credential material. The documentation is allowed to mention
# credential concepts, but actual token-like values must not be present.
secret_patterns = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for pattern in secret_patterns:
        if pattern.search(text):
            fail(f"possible credential material detected in {path}")
            break

if ERRORS:
    print("SPACE-READ validation FAILED")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("SPACE-READ validation OK")
