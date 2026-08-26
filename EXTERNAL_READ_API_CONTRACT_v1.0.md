# SPACE-READ — EXTERNAL READ API CONTRACT v1.0

STATUS: ARCHITECTURAL CONTRACT — API NOT YET DEPLOYED
DATE: 2026-08-26

## Purpose

Define the public API that exposes the already-existing SPACE-READ publication contract to external humans, LLMs, agents and research tools.

## Trust model

The external API is strictly read-only with respect to canonical SPACE.

Allowed:

`READ → ANALYZE → USE → PROPOSE`

Forbidden:

`WRITE_CORE / UPDATE_CORE / DELETE_CORE / MERGE_CORE / WRITE_BACK`

## Source

```text
SPACE Core
    ↓ controlled publication
validation
    ↓
SPACE-READ
    ↓
EXTERNAL READ API
```

The API reads the public publication layer. It does not read private Core directly.

## Minimal operations

```text
GET /manifest
GET /publications
GET /publications/{id}
GET /definitions/{id}
GET /structures/{id}
GET /experiments/{id}
GET /history/{id}
GET /search?q=...
GET /health
```

These endpoints are the network realization of the conceptual operations already defined by `AI_INTERFACE.md`.

## Response contract

Every significant object returned by the API must preserve:

```text
id
schema_version
publication_version
class
status
published_at
provenance
scope
content
relations
```

The API must never silently promote:

`UNKNOWN → TRUE`

`HYPOTHESIS → VERIFIED`

`PROPOSAL → ACCEPTED`

`PUBLICATION → UNIVERSAL TRUTH`

## Provenance

Public provenance may expose:

- source identity at the permitted abstraction level;
- source version/commit reference when safe;
- transformation/publication method;
- publication version;
- verification scope.

It must never expose Core credentials, private paths or private architectural details that are not explicitly approved for publication.

## No private Core route

The external API must not have:

- Core credentials;
- Core write credentials;
- network route to private Core services;
- filesystem access to private Core;
- arbitrary command execution;
- hidden callback/write-back capability.

## Proposal boundary

A proposal is external evidence, not an API mutation.

```text
EXTERNAL API
    ↓
PROPOSAL
    ↓
REVIEW / VALIDATION
    ↓
CONTROLLED PUBLICATION
    ↓
NEW PUBLICATION VERSION
```

## Caching and consistency

Responses should identify publication version and source snapshot/commit where available. Clients must not assume that a cached response is the current Core state.

## Error semantics

The API must distinguish at least:

`NOT_FOUND`
`NOT_PUBLIC`
`INVALID_QUERY`
`PUBLICATION_NOT_VERIFIED`
`TEMPORARILY_UNAVAILABLE`
`INTERNAL_ERROR`

No private error detail may leak internal credentials, paths or stack traces.

## Security invariant

`EXTERNAL_API_COMPROMISE ≠ SPACE_CORE_COMPROMISE`

This must be enforced by architecture, not by prompt or documentation alone.

## Relationship to existing contract

This document does not replace `AI_INTERFACE.md`, `PUBLICATION_CONTRACT.md`, `READ_ONLY_POLICY.md` or `SECURITY_ARCHITECTURE.md`. It defines the network layer that will implement their already-defined semantics.

## Implementation status

The current SPACE-READ manifest explicitly states that a network read API is not yet deployed. Therefore this document is a contract/implementation target, not a claim of an existing service.

## Verification gate

The API is not considered implemented until all of the following are demonstrated:

1. public read works;
2. publication metadata and provenance survive the API boundary;
3. unauthorized Core write attempts fail;
4. no Core credentials are reachable;
5. no private Core route is reachable;
6. schema/index validation passes;
7. recovery of the public publication set is reproducible;
8. adversarial write-back testing passes.
