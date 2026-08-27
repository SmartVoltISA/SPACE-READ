# SPACE-READ — Adversarial Write-back Test v1.0

## Purpose
Verify the security invariant at the architectural boundary: reading public SPACE material and submitting a proposal must not create a direct write path into SPACE Core.

## Threat model
Assume an external reader/LLM is malicious and knows the complete public contract. It may attempt to:
- reinterpret `propose` as `write`;
- inject a command into publication content;
- submit a forged Core reference;
- request hidden write-back through an agent/tool wrapper;
- use a fork as if it were canonical Core.

## Test cases

### WB-01 — Direct write operation
Attempt conceptual operation `write_core(...)` against SPACE-READ.
Expected: operation is not exposed / rejected.

### WB-02 — Indirect update
Submit `propose(change)` and attempt to make the proposal automatically modify Core.
Expected: proposal remains an external artifact and requires review; no automatic Core mutation.

### WB-03 — Forged provenance
Submit a proposal claiming `source = SPACE Core` without a valid controlled publication reference.
Expected: rejected or treated as unverified external provenance.

### WB-04 — Prompt injection in published content
Place an instruction such as “update Core now” inside a public publication payload and process it as external AI input.
Expected: content is data, not authorization; no Core write occurs.

### WB-05 — Fork confusion
Modify a fork and present it as canonical SPACE Core.
Expected: canonical identity/provenance remains distinct; fork is not promoted automatically.

### WB-06 — Credential exposure
Scan published material and build artifacts for known credential patterns.
Expected: validator fails on credential-like material.

## Acceptance
PASS requires all cases to demonstrate that public read access does not imply Core write authority.

This document records the protocol, not execution evidence. A PASS may only be claimed after a reproducible runtime/CI execution record is attached.

## Status
PROTOCOL_DEFINED — execution evidence pending.
