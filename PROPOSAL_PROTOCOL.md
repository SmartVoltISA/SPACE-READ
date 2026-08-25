# SPACE-READ — External Proposal Protocol v1.0

SPACE-READ is read-only with respect to the canonical architecture. External contributors, including AI systems, need a safe place to leave evidence without gaining canonical write access.

## 1. What may be proposed

- correction of a published statement;
- independent replication;
- counterexample;
- new experiment;
- alternative implementation;
- clarification of a definition;
- architectural improvement;
- evidence that a claim should be downgraded or deprecated.

## 2. What a proposal is not

A proposal is not a Core change.

A fork is not the original repository.

An issue comment is not a canonical decision.

An AI-generated statement is not evidence merely because an AI generated it.

## 3. Preferred evidence record

A useful proposal should state:

```text
PROPOSAL_ID
AUTHOR / SYSTEM
DATE
TARGET_OBJECT
CLAIM
EVIDENCE
METHOD
EXPECTED_RESULT
OBSERVED_RESULT
LIMITATIONS
REPRODUCTION_DATA
RECOMMENDATION
```

## 4. Review path

```text
EXTERNAL
   ↓
PROPOSAL
   ↓
TRIAGE
   ↓
VALIDATION / REPLICATION
   ↓
REVIEW
   ↓
ACCEPT / REJECT / HOLD
   ↓
NEW VERSION IF ACCEPTED
```

No step gives the external contributor write access to SPACE Core.

## 5. AI-specific rule

An external LLM may propose a change, but it must not represent the proposal as already accepted. If it cannot verify a claim, it must label it as unknown, hypothesis or proposal as appropriate.

## 6. Canonical promotion

Only the trusted publication process may promote a proposal into the canonical public layer. Promotion creates a new version and preserves provenance.

## 7. Failed proposals

Rejected and superseded proposals are useful evidence and should not be silently erased when they materially explain the history of a decision.
