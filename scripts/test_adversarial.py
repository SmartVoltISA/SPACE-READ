#!/usr/bin/env python3
"""Adversarial regression tests for SPACE-READ.

Every mutation is made in a temporary copy. The real repository is never
modified. Each malicious mutation must make the validator fail closed.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_read.py"


def run_validator(tree: Path) -> bool:
    result = subprocess.run(
        ["python", str(tree / "scripts" / "validate_read.py")],
        cwd=tree,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode == 0


def mutate_manifest(tree: Path, key: str, value) -> None:
    path = tree / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data[key] = value
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def mutate_nested_manifest(tree: Path, section: str, key: str, value) -> None:
    path = tree / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data[section][key] = value
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def mutate_index(tree: Path, mutation: str) -> None:
    path = tree / "PUBLICATION_INDEX.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if mutation == "duplicate_id":
        data["items"].append(dict(data["items"][0]))
    elif mutation == "missing_provenance":
        data["items"][0].pop("provenance", None)
    elif mutation == "path_escape":
        data["items"][0]["path"] = "../manifest.json"
    elif mutation == "fake_verified":
        data["items"][0]["status"] = "verified"
        data["items"][0]["class"] = "verified_result"
        data["items"][0]["provenance"].pop("verification", None)
    else:
        raise ValueError(mutation)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def run_case(name: str, mutator) -> None:
    with tempfile.TemporaryDirectory(prefix="space-read-attack-") as tmp:
        tree = Path(tmp) / "SPACE-READ"
        shutil.copytree(ROOT, tree, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        mutator(tree)
        if run_validator(tree):
            raise SystemExit(f"ADVERSARIAL TEST FAILED: {name} was accepted")
        print(f"BLOCKED: {name}")


cases = [
    ("manifest write_back=true", lambda t: mutate_manifest(t, "write_back", True)),
    ("external_ai write_core=true", lambda t: mutate_nested_manifest(t, "external_ai", "write_core", True)),
    ("physical core_write_api_exposed=true", lambda t: mutate_nested_manifest(t, "physical_isolation", "core_write_api_exposed", True)),
    ("duplicate publication id", lambda t: mutate_index(t, "duplicate_id")),
    ("missing provenance", lambda t: mutate_index(t, "missing_provenance")),
    ("publication path escape", lambda t: mutate_index(t, "path_escape")),
    ("fake verified result", lambda t: mutate_index(t, "fake_verified")),
]

for name, mutator in cases:
    run_case(name, mutator)

print("SPACE-READ adversarial tests OK")
