# SPACE-READ — External AI Read Interface v1.0

## Purpose

This document is the machine-oriented entry contract for an external LLM, agent or research system that wants to use SPACE-READ.

## Trust model

The external AI is a reader and analyst, not an owner of SPACE Core.

Allowed:

- `read` — retrieve published material;
- `analyze` — reason over published material;
- `use` — use the architecture in an independent system;
- `propose` — submit a proposal, correction, experiment or replication.

Forbidden:

- `write_core`;
- `update_core`;
- `delete_core`;
- `merge_core`;
- any hidden or indirect write-back operation.

## Recommended reading order

1. `manifest.json`
2. `PUBLICATION_CONTRACT.md`
3. `READ_ONLY_POLICY.md`
4. `SECURITY_ARCHITECTURE.md`
5. `PUBLICATION_INDEX.json`
6. the referenced publication objects

## Query model

An implementation may expose read operations equivalent to:

```text
get_manifest()
list_publications()
get_publication(id)
get_definition(id)
get_structure(id)
get_experiment(id)
get_history(id)
search(query)
```

These are conceptual operations. SPACE-READ does not currently claim that a network API is deployed.

## Response requirements

A machine-readable response SHOULD include:

```json
{
  "id": "space.architecture.overview",
  "schema_version": "1.0.0",
  "publication_version": "1.0.0",
  "status": "reviewed",
  "class": "structure",
  "provenance": {
    "source": "SPACE Core",
    "source_ref": "controlled internal publication",
    "transformation": "public abstraction"
  },
  "content": {}
}
```

## Important interpretation rule

The external AI must preserve publication status and provenance when using the material. It must not silently convert:

- a proposal into a decision;
- a hypothesis into a fact;
- a model into a description of reality;
- a fork into the canonical SPACE architecture.

## Proposal path

If the AI discovers an error or improvement:

`READ → ANALYZE → PROPOSAL → REVIEW → optional new PUBLICATION`

Never:

`READ → WRITE CORE`.

## No API claim

SPACE-READ is currently a Git repository with machine-readable files. A future API may expose the same contract, but an API MUST NOT be considered implemented until independently tested and documented.
