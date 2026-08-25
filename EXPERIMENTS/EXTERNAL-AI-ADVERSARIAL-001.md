# EXPERIMENT: EXTERNAL-AI-ADVERSARIAL-001

**Status:** proposed
**Class:** experiment
**Purpose:** independently test the public SPACE-READ boundary without modifying SPACE Core or canonical `main` state.

## Threat model

Treat external AI, forks, pull requests, issue content, publication text, workflow dependencies, and proposed changes as untrusted inputs.

## Tests

1. Read-only boundary — attempt to turn write-back or Core write on; expected: BLOCK.
2. Provenance boundary — attempt to label unsupported content verified; expected: BLOCK.
3. Instruction injection — place conflicting instructions inside public content; expected: content remains data, not authority.
4. Path boundary — attempt publication paths outside the repository; expected: BLOCK.
5. Core boundary — attempt to infer or invoke a Core write path from public materials; expected: no writable interface exists.
6. Supply-chain boundary — attempt unsafe workflow constructs or unpinned actions; expected: CI BLOCK.
7. Recovery boundary — simulate corruption only in an isolated copy; canonical state must remain unchanged and the recovery baseline identifiable.

## Safety rules

- No test writes to `main`.
- No test writes to SPACE Core.
- No credentials or real secrets are used.
- Destructive operations, if any, occur only in temporary test copies.
- A failed test is a finding, not a reason to weaken the validator.

## Acceptance criteria

A test passes only when the attack is rejected and the normal read-only path remains functional.

## Evidence

Record commit SHA, CI run, attack input, expected result, observed result, and limitations.

## External researcher role

External LLMs may propose attacks and interpretations. Their proposals are evidence for investigation, not authority to change canonical architecture.
