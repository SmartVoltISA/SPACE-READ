#!/usr/bin/env python3
"""Static integrity checks for SPACE-READ.

This validator is local and read-only. It must not contact SPACE Core or any
external service. A failure is fail-closed: the publication is not considered
valid unless every invariant below passes.
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

# ---- Immutable publication boundary ----
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

# ---- Publication index ----
items: list[dict] = []
if not isinstance(index, dict) or not isinstance(index.get("items"), list):
    fail("PUBLICATION_INDEX.json must contain an items array")
else:
    items = index["items"]
    ids: set[str] = set()
    allowed_statuses = {"draft", "reviewed", "verified", "rejected", "deprecated"}
    allowed_kinds = {"architecture", "definition", "axiom", "hypothesis", "experiment", "result", "policy", "protocol"}
    for item in items:
        if not isinstance(item, dict):
            fail("publication index item must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id.strip():
            fail("publication item has no non-empty string id")
        elif item_id in ids:
            fail(f"duplicate publication id: {item_id}")
        else:
            ids.add(item_id)

        path = item.get("path")
        if not isinstance(path, str) or not path.strip():
            fail(f"publication {item_id!r} has no path")
            continue
        target = (ROOT / path).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            fail(f"publication path escapes repository: {path}")
            continue
        if not target.is_file():
            fail(f"publication target does not exist: {path}")

        status = item.get("status")
        if status not in allowed_statuses:
            fail(f"publication {item_id!r} has invalid status: {status!r}")
        kind = item.get("kind")
        if kind not in allowed_kinds:
            fail(f"publication {item_id!r} has invalid kind: {kind!r}")

        provenance = item.get("provenance")
        if not isinstance(provenance, dict):
            fail(f"publication {item_id!r} missing provenance object")
        else:
            for key in ("source", "source_ref", "published_at", "published_by"):
                if not isinstance(provenance.get(key), str) or not provenance[key].strip():
                    fail(f"publication {item_id!r} provenance.{key} must be non-empty")

        # A public index may describe proposals, but proposals cannot masquerade
        # as verified facts.
        if status == "verified" and kind in {"hypothesis", "result"}:
            verification = item.get("verification")
            if not isinstance(verification, dict):
                fail(f"verified publication {item_id!r} requires verification metadata")

# ---- Schema sanity ----
if isinstance(schema, dict):
    if schema.get("type") != "object":
        fail("publication schema root must be an object")
    properties = schema.get("properties")
    required_schema = schema.get("required")
    if not isinstance(properties, dict):
        fail("publication schema must define properties")
    if not isinstance(required_schema, list) or not required_schema:
        fail("publication schema must define required fields")

# ---- Repository path safety ----
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        resolved = path.resolve()
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"file resolves outside repository: {path}")

# ---- Credential and dangerous-control detection ----
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
    for pattern in forbidden_control_patterns:
        if pattern.search(text):
            fail(f"forbidden write control detected in {path}")
            break

# ---- Fail closed ----
if ERRORS:
    print("SPACE-READ validation FAILED")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("SPACE-READ validation OK")
