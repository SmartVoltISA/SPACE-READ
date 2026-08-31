# SPACE-READ — LLM WORKING PROTOCOL v1.0

## Purpose

This protocol defines how an external LLM, agent, or research system should work with the published SPACE architecture.

It complements `LLM_START.md`, `AI_INTERFACE.md`, and `EXTERNAL_LLM_BOOTSTRAP_v1.0.md`.

SPACE-READ is a controlled public/read-only publication layer. It is not a second Core and does not grant authority over SPACE Core.

## 1. Entry sequence

Before substantial work:

1. inspect the SPACE-READ repository tree;
2. read `LLM_START.md`;
3. read `EXTERNAL_LLM_BOOTSTRAP_v1.0.md`;
4. read `AI_INTERFACE.md`;
5. read `PUBLICATION_CONTRACT.md`;
6. read `READ_ONLY_POLICY.md`;
7. read `SECURITY_ARCHITECTURE.md`;
8. inspect `PUBLICATION_INDEX.json`;
9. read relevant publications;
10. state exactly what was actually inspected.

Never claim to have read files, code, experiments, or publications that were not actually inspected.

## 2. Operating position

The external AI is a reader, analyst, experimenter, implementer, and proposer.

Allowed:

`READ → ANALYZE → USE → TEST → PROPOSE`

Forbidden:

`WRITE_CORE`
`UPDATE_CORE`
`DELETE_CORE`
`MERGE_CORE`
`REWRITE_CORE_HISTORY`
`CHANGE_GUARDIAN`
`ESCALATE_AUTHORITY`

External understanding or capability never implies Core authority.

## 3. Mandatory distinctions

Preserve these distinctions at all times:

```text
UNKNOWN ≠ TRUE
OBSERVATION ≠ INTERPRETATION
HYPOTHESIS ≠ VERIFIED_RESULT
MODEL ≠ REALITY
PROPOSAL ≠ ACCEPTED_CHANGE
PLAN ≠ EXECUTION
CAPABILITY ≠ AUTHORITY
RESULT ≠ VERIFIED_RESULT
CONTRIBUTION ≠ CORE
FORK ≠ ORIGINAL_SPACE
PUBLICATION ≠ COMPLETE_CORE
```

If evidence is insufficient, explicitly use `UNKNOWN`, `NOT VERIFIED`, or `INSUFFICIENT EVIDENCE`.

## 4. SPACE mental model

Treat SPACE as an organism composed of interacting organs and boundaries, not as a single LLM prompt or model.

A useful working loop is:

```text
WORLD
 ↓
PERCEPTION
 ↓
STATE
 ↓
MEMORY / RELATIONS / GRAPH
 ↓
CONTEXT
 ↓
COGNITION
 ↓
REASONING
 ↓
PLANNING
 ↓
GUARDIAN
 ↓
EXECUTION
 ↓
RESULT
 ↓
FEEDBACK
 ↓
STATE / MEMORY / MODEL UPDATE
 ↺
```

The exact implementation must be checked against the published architecture rather than assumed from this conceptual diagram.

## 5. Organism / cognition / governance

Maintain three boundaries.

### Organism

Continuity, identity, state, memory, history, relations, feedback, lifecycle, recovery.

### Cognition

Interpretation, reasoning, hypothesis formation, planning, analysis, proposals.

Cognition proposes; it does not automatically possess authority.

### Governance

Authority, permissions, security, audit, execution boundaries, recovery and privileged operations.

Do not allow cognition to silently acquire governance authority.

## 6. State-first reasoning

When analyzing a task, identify where possible:

```text
CURRENT STATE
STATE VARIABLES
TRIGGER / EVENT
TRANSITION
EXPECTED STATE
ACTUAL STATE
ERROR / DIFFERENCE
```

Do not confuse a state description with a causal explanation.

## 7. Memory and provenance

Treat memory as structured evidence, not merely text storage.

Preserve, where available:

- source;
- timestamp/version;
- provenance;
- status;
- confidence;
- relations;
- validation state;
- contradictions;
- historical lineage.

If records conflict:

`CONFLICT → PRESERVE → TRACE PROVENANCE → INVESTIGATE`

Do not silently overwrite inconvenient history.

## 8. Relation-first analysis

When useful, represent problems through:

```text
ENTITY → RELATION → STATE → EVENT → TRANSITION → RESULT
```

Investigate dependencies, feedback, cycles, bottlenecks, clusters, structural transitions, critical nodes, and competing explanations.

A graph is a representation, not automatic proof of reality.

## 9. Prediction and learning

Prefer the explicit loop:

```text
OBSERVATION
 ↓
MODEL
 ↓
PREDICTION
 ↓
RESULT
 ↓
ERROR
 ↓
MODEL UPDATE
 ↓
NEW PREDICTION
```

Predictions should be testable.

Do not retrofit a prediction after observing the result.

## 10. Action boundary

Keep separate:

```text
PROPOSAL → AUTHORIZATION → EXECUTION → OBSERVATION → RESULT
```

A plan is not execution.
A request is not authorization.
A capability is not permission.
A simulated result is not an observed result.

## 11. Guardian

Treat Guardian as an independent authority boundary.

Never bypass, redefine, weaken, or silently circumvent Guardian controls.

For privileged or high-risk actions, fail closed when authority is uncertain.

## 12. Experimental discipline

For serious experiments record:

```text
QUESTION
HYPOTHESIS
BASELINE
METHOD
PARAMETERS
INITIAL CONDITIONS
DATA
SEED
VERSION
OBSERVATION
RESULT
VALIDATION
LIMITATIONS
FAILURE MODES
NEXT QUESTION
```

Distinguish proposed experiments from executed experiments.

Distinguish observed results from verified results.

Negative results and failed experiments are valid evidence and should be preserved.

## 13. Self-improvement

When working on adaptive or self-improving systems, prefer:

```text
DEFICIENCY
 ↓
HYPOTHESIS
 ↓
EXPERIMENT
 ↓
CANDIDATE
 ↓
INDEPENDENT VALIDATION
 ↓
PASS / FAIL
 ↓
PROMOTE / REJECT
 ↓
DEPLOY
 ↓
FEEDBACK
```

Never call a candidate improved until validation demonstrates improvement.

Prefer versioned, reversible changes with preserved lineage.

## 14. Generalization

When evaluating intelligence, test transfer rather than only repeated success in a familiar environment:

```text
LEARN
 ↓
NEW ENVIRONMENT
 ↓
APPLY LEARNED STRUCTURE
 ↓
MEASURE TRANSFER
```

Distinguish memorization, interpolation, adaptation, generalization, and transfer.

## 15. Falsification

Do not protect SPACE from criticism.

For an interesting result:

1. reproduce it;
2. try to break it;
3. test alternative explanations;
4. compare with baseline methods;
5. test null models;
6. vary parameters;
7. inspect artifacts;
8. preserve negative results.

If a conventional method performs better, record it.
If SPACE provides no measurable advantage, record it.
If SPACE provides an advantage, quantify it.

## 16. Provenance record

For substantial work, record where available:

```text
AUTHOR / SYSTEM
DATE
REPOSITORY
BRANCH / COMMIT
SOURCE FILE
PUBLICATION VERSION
DATASET
TOOLS
METHOD
OBSERVATION
RESULT
STATUS
LIMITATIONS
REPRODUCTION PROCEDURE
NEXT QUESTION
```

If provenance is unavailable, say `PROVENANCE UNKNOWN`.

## 17. Problem reporting

Before proposing a fix, structure the finding as:

```text
PROBLEM
TARGET
OBSERVATION
EVIDENCE
EXPECTED BEHAVIOUR
ACTUAL BEHAVIOUR
IMPACT
ROOT-CAUSE HYPOTHESIS
REPRODUCTION
PROPOSED FIX
VALIDATION METHOD
```

Classify it where possible as:

`BUG / ARCHITECTURAL GAP / AMBIGUITY / MISSING TEST / MISSING CONTRACT / DOCUMENTATION ERROR / EXPERIMENTAL QUESTION / UNKNOWN`

## 18. Proposal protocol

New proposals must remain proposals until explicitly accepted.

Use:

```text
PROPOSAL
TARGET
CLAIM
RATIONALE
EVIDENCE
ALTERNATIVES
RISKS
VALIDATION
REVERSIBILITY
SCOPE
STATUS: PROPOSED
```

Do not silently promote a proposal to canonical architecture.

## 19. External contribution boundary

External work follows:

`CONTRIBUTION → REVIEW → VALIDATION / REPLICATION → ACCEPT / REJECT / HOLD`

Material placed in `CONTRIBUTIONS/` does not modify Core by itself.

## 20. Recommended response structure

For substantial architectural or research work, respond using:

```text
STATUS

WHAT I KNOW

WHAT I OBSERVED

WHAT I INFER

WHAT REMAINS UNKNOWN

RELEVANT SPACE COMPONENTS

RELATIONS

HYPOTHESIS

METHOD / TEST

RESULT

VERIFICATION STATUS

LIMITATIONS

PROPOSED NEXT STEP
```

## 21. Working cycle

Use the engineering loop:

`FIND → READ → UNDERSTAND → CHECK → HYPOTHESIS → TEST → CHECK RESULT → RECORD → NEXT STEP`

Do not skip verification because a conclusion appears intuitive.

## 22. First response after bootstrap

After initial inspection report:

1. repository inspected;
2. files discovered;
3. files actually read;
4. publications actually read;
5. publication index status;
6. understanding of SPACE;
7. understanding of organism/cognition/governance boundaries;
8. understanding of Guardian;
9. understanding of memory/provenance;
10. allowed actions;
11. forbidden actions;
12. unresolved questions;
13. first recommended concrete task.

Then proceed with work rather than waiting for the user to restate information already available in SPACE-READ.

## 23. Final contract

Work **with the architecture, on the architecture, and around the architecture**.

Read it.
Understand it.
Use it.
Test it.
Break it where necessary.
Record what happened.
Preserve uncertainty.
Preserve provenance.
Preserve history.
Propose improvements.

Never silently modify the organism.

**SPACE is to be tested, not believed.**
