#!/usr/bin/env python3
"""Fail-closed static integrity checks for SPACE-READ."""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
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

# Immutable boundary invariants.
if isinstance(manifest, dict):
    required = {"name", "schema_version", "publication_version", "status",
                "visibility", "access_model", "source", "publication_direction",
                "write_back", "physical_isolation", "external_ai", "interfaces",
                "entrypoints", "principles", "repository"}
    missing = required - manifest.keys()
    if missing:
        fail(f"manifest missing keys: {sorted(missing)}")

    exact = {
        "name": "SPACE-READ",
        "visibility": "public",
        "access_model": "read-only",
        "source": "SPACE Core",
        "publication_direction": "SPACE Core -> validation -> SPACE-READ",
        "write_back": False,
        "repository": "SmartVoltISA/SPACE-READ",
    }
    for key, expected in exact.items():
        if manifest.get(key) != expected:
            fail(f"manifest.{key} must equal {expected!r}")

    physical = manifest.get("physical_isolation")
    if not isinstance(physical, dict):
        fail("manifest.physical_isolation must be an object")
    else:
        for key in ("core_credentials_in_read", "core_write_api_exposed",
                    "external_ai_core_credentials", "external_ai_core_write"):
            if physical.get(key) is not False:
                fail(f"manifest.physical_isolation.{key} must be false")
        if physical.get("publication_direction") != "one-way":
            fail("manifest.physical_isolation.publication_direction must be one-way")

    external = manifest.get("external_ai")
    if not isinstance(external, dict):
        fail("manifest.external_ai must be an object")
    else:
        for key in ("read", "analyze", "use", "propose"):
            if external.get(key) is not True:
                fail(f"manifest.external_ai.{key} must be true")
        if external.get("write_core") is not False:
            fail("manifest.external_ai.write_core must be false")

    interfaces = manifest.get("interfaces")
    if not isinstance(interfaces, dict):
        fail("manifest.interfaces must be an object")
    else:
        if interfaces.get("repository_read") is not True:
            fail("interfaces.repository_read must be true")
        if interfaces.get("network_read_api") is not False:
            fail("interfaces.network_read_api must be false until implemented")

# Publication objects follow the repository's published schema.
items: list[dict] = []
if not isinstance(index, dict) or not isinstance(index.get("items"), list):
    fail("PUBLICATION_INDEX.json must contain an items array")
else:
    items = index["items"]
    ids: set[str] = set()
    allowed_statuses = {"draft", "reviewed", "verified", "rejected", "deprecated"}
    allowed_classes = {"axiom", "definition", "structure", "rule", "hypothesis", "experiment", "verified_result", "rejected_result", "open_question", "history"}
    for item in items:
        if not isinstance(item, dict):
            fail("publication index item must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", item_id):
            fail(f"publication item has invalid id: {item_id!r}")
        elif item_id in ids:
            fail(f"duplicate publication id: {item_id}")
        else:
            ids.add(item_id)

        for key in ("class", "title", "status", "schema_version", "publication_version", "published_at", "provenance"):
            if key not in item:
                fail(f"publication {item_id!r} missing required field: {key}")
        if item.get("class") not in allowed_classes:
            fail(f"publication {item_id!r} has invalid class: {item.get('class')!r}")
        if item.get("status") not in allowed_statuses:
            fail(f"publication {item_id!r} has invalid status: {item.get('status')!r}")
        if not isinstance(item.get("title"), str) or not item.get("title", "").strip():
            fail(f"publication {item_id!r} title must be non-empty")

        published_at = item.get("published_at")
        if not isinstance(published_at, str):
            fail(f"publication {item_id!r} published_at must be a string")
        else:
            try:
                datetime.fromisoformat(published_at.replace("Z", "+00:00"))
            except ValueError:
                fail(f"publication {item_id!r} published_at is not ISO-8601")

        path = item.get("path")
        if not isinstance(path, str) or not path.strip():
            fail(f"publication {item_id!r} has no path")
        else:
            target = (ROOT / path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"publication path escapes repository: {path}")
            else:
                if not target.is_file():
                    fail(f"publication target does not exist: {path}")

        provenance = item.get("provenance")
        if not isinstance(provenance, dict):
            fail(f"publication {item_id!r} provenance must be an object")
        else:
            for key in ("source", "source_ref", "transformation"):
                if not isinstance(provenance.get(key), str) or not provenance[key].strip():
                    fail(f"publication {item_id!r} provenance.{key} must be non-empty")
            if item.get("status") == "verified" and not isinstance(provenance.get("verification"), str):
                fail(f"verified publication {item_id!r} requires provenance.verification")

# Validate the schema itself enough to catch accidental weakening.
if isinstance(schema, dict):
    if schema.get("type") != "object":
        fail("publication schema root must be an object")
    required_schema = schema.get("required")
    if not isinstance(required_schema, list) or set(required_schema) != {
        "id", "class", "title", "status", "schema_version", "publication_version", "published_at", "provenance"
    }:
        fail("publication schema required fields were weakened or changed")
    props = schema.get("properties")
    if not isinstance(props, dict):
        fail("publication schema must define properties")
    else:
        expected_enums = {
            "status": {"draft", "reviewed", "verified", "rejected", "deprecated"},
            "class": {"axiom", "definition", "structure", "rule", "hypothesis", "experiment", "verified_result", "rejected_result", "open_question", "history"},
        }
        for key, expected in expected_enums.items():
            actual = props.get(key, {}).get("enum")
            if set(actual or []) != expected:
                fail(f"publication schema {key} enum was weakened or changed")
        if props.get("provenance", {}).get("additionalProperties") is not False:
            fail("publication provenance must reject unknown properties")

# Repository/path safety.
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        fail(f"file resolves outside repository: {path}")

# Credential and forbidden-control detection. The validator itself is excluded
# from the control-pattern scan because it necessarily contains the patterns
# it is designed to detect.
secret_patterns = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{24,}['\"]"),
]
forbidden_control_patterns = [
    re.compile(r"(?i)write[_ -]?core\s*[:=]\s*true"),
    re.compile(r"(?i)write[_ -]?back\s*[:=]\s*true"),
    re.compile(r"(?i)core[_ -]?write[_ -]?api\s*[:=]\s*true"),
]

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path == Path(__file__).resolve():
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for pattern in secret_patterns:
        if pattern.search(text):
            fail(f"possible credential material detected in {path}")
            break
    for pattern in forbidden_control_patterns:
        if pattern.search(text):
            fail(f"forbidden write control detected in {path}")
            break

if ERRORS:
    print("SPACE-READ validation FAILED")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("SPACE-READ validation OK")
