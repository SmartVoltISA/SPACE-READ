# SPACE-READ — HUMAN WORKING PROTOCOL v1.0

## Purpose

This document defines how a human researcher, engineer, architect, reviewer, contributor, or collaborator should work with SPACE-READ.

SPACE-READ is a public/read-only publication layer of SPACE. It is not a second Core and it is not a place where an individual contribution automatically becomes canonical architecture.

The purpose of this protocol is simple:

**understand → verify → contribute → preserve history → improve the system without corrupting its evidence.**

---

## 1. Start here

Before making a substantial contribution:

1. read `README.md`;
2. read `LLM_START.md` if AI collaboration is involved;
3. read `AI_INTERFACE.md` when working with external AI;
4. read `PUBLICATION_CONTRACT.md`;
5. read `READ_ONLY_POLICY.md`;
6. inspect `PUBLICATION_INDEX.json`;
7. read the relevant definitions, structures, rules, experiments, and results.

Do not assume that the public layer contains the entire Core.

`PUBLICATION ≠ COMPLETE_CORE`

---

## 2. What SPACE-READ is

SPACE-READ provides a controlled public representation of selected SPACE architecture, definitions, structures, experiments, results, and history.

It allows people and external AI systems to:

- understand the architecture;
- study published material;
- reproduce experiments;
- identify errors;
- challenge assumptions;
- develop independent implementations;
- propose improvements;
- contribute evidence.

It does not automatically grant authority to change SPACE Core.

---

## 3. What a person may do

A human contributor may:

`READ → UNDERSTAND → ANALYZE → TEST → CRITIQUE → PROPOSE → CONTRIBUTE`

Possible contributions include:

- research;
- experiments;
- replications;
- implementation work;
- documentation corrections;
- architectural analysis;
- counterexamples;
- failed experiments;
- negative results;
- alternative designs;
- questions;
- proposals.

The objective is not to agree with SPACE.

The objective is to determine what survives verification.

---

## 4. What a person must not do

Do not:

- present an unverified idea as fact;
- silently rewrite historical meaning;
- delete inconvenient negative results;
- confuse a proposal with an accepted architectural change;
- represent a fork as canonical SPACE;
- expose private Core information merely to prove provenance;
- bypass established security or governance boundaries;
- claim that an experiment was executed when it was only proposed;
- claim verification without the required evidence;
- change canonical architecture without the trusted acceptance process.

---

## 5. Mandatory distinctions

Always preserve:

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

If something is unknown, write `UNKNOWN`.

If something is proposed, write `PROPOSED`.

If something was observed but not independently verified, say so.

Do not upgrade the status of information through wording alone.

---

## 6. The working method

Use the engineering/research loop:

```text
FIND
 ↓
READ
 ↓
UNDERSTAND
 ↓
CHECK
 ↓
FORM HYPOTHESIS
 ↓
TEST
 ↓
CHECK RESULT
 ↓
RECORD
 ↓
DECIDE NEXT STEP
```

Do not skip the verification stage because a conclusion appears obvious.

---

## 7. Work with the organism model

When discussing SPACE, think in terms of interacting components rather than a single application.

A useful conceptual loop is:

```text
WORLD
 ↓
PERCEPTION
 ↓
STATE
 ↓
MEMORY / RELATIONS / GRAPH
 ↓
COGNITION
 ↓
REASONING
 ↓
PLANNING
 ↓
GOVERNANCE / GUARDIAN
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

This is a conceptual map. Check the published architecture before making implementation claims.

---

## 8. State and relations

When analyzing a problem, explicitly ask:

- What is the current state?
- What changed?
- What event caused or preceded the change?
- Which relations matter?
- Which components depend on each other?
- What feedback exists?
- What is measured versus inferred?

Prefer explicit relations over vague narratives.

A graph is a representation, not automatic proof of causality.

---

## 9. Memory and history

Treat history as evidence.

Do not erase an older state merely because a newer interpretation seems better.

Prefer:

`v1 → v2 → v3`

over silently replacing:

`v1 → v3`.

When information conflicts:

```text
CONFLICT
 ↓
PRESERVE
 ↓
TRACE PROVENANCE
 ↓
INVESTIGATE
 ↓
RECORD CONCLUSION
```

The fact that a result is negative does not make it useless.

A failed experiment can constrain the search space.

---

## 10. Provenance

For meaningful work record, where available:

```text
AUTHOR
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

If something cannot be established, explicitly mark it unknown.

Never invent provenance.

---

## 11. Experiments

A serious experiment should distinguish:

```text
QUESTION
HYPOTHESIS
BASELINE
METHOD
PARAMETERS
INITIAL CONDITIONS
DATA
RESULT
VALIDATION
LIMITATIONS
NEXT QUESTION
```

Record enough information for another researcher to understand what actually happened.

The following are different states:

```text
PROPOSED EXPERIMENT
EXECUTED EXPERIMENT
OBSERVED RESULT
VERIFIED RESULT
REJECTED RESULT
```

Do not collapse them.

---

## 12. Falsification

SPACE should be challenged, not protected.

For every important claim ask:

- Can it be reproduced?
- Can it be falsified?
- What is the baseline?
- What is the null model?
- Could another mechanism explain the result?
- Does the result survive parameter changes?
- Is there a measurement artifact?
- Does the effect transfer to another dataset or environment?

If the answer is negative, record it.

Scientific integrity is more important than architectural pride.

---

## 13. Working with AI

An external LLM is a collaborator/tool, not automatically an authority.

When using AI:

1. give it the appropriate SPACE-READ bootstrap/protocol;
2. require it to distinguish facts, observations, hypotheses and proposals;
3. require provenance for substantial claims;
4. verify important outputs independently;
5. do not allow AI-generated text to become canonical merely because it sounds authoritative;
6. record useful AI contributions as external contributions until reviewed.

The human remains responsible for deciding whether an external AI result has actually been verified.

---

## 14. Contribution lifecycle

External work should follow:

```text
CONTRIBUTION
      ↓
REVIEW
      ↓
VALIDATION / REPLICATION
      ↓
ACCEPT / REJECT / HOLD
      ↓
OPTIONAL PUBLICATION
```

Only an explicit trusted process can promote external material into the canonical publication layer.

A GitHub file, issue, fork, or AI response does not become canonical merely by existing.

---

## 15. Proposal format

When proposing a change use:

```text
PROPOSAL

TARGET:

CLAIM:

OBSERVATION / EVIDENCE:

RATIONALE:

ALTERNATIVES:

RISKS:

VALIDATION METHOD:

REVERSIBILITY:

SCOPE:

STATUS: PROPOSED
```

Do not write a proposal as though it has already been accepted.

---

## 16. Problem report format

When finding a defect or architectural gap:

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

Classify it when possible:

`BUG`

`ARCHITECTURAL GAP`

`AMBIGUITY`

`MISSING TEST`

`MISSING CONTRACT`

`DOCUMENTATION ERROR`

`EXPERIMENTAL QUESTION`

`UNKNOWN`

---

## 17. Safety and governance

Do not bypass Guardian, authorization, audit, recovery, or other established governance boundaries.

A person may have technical access without having architectural authority.

A developer may be able to modify a file without that modification being an accepted Core change.

Technical possibility and legitimate authority are different things.

---

## 18. When something is wrong

If SPACE is wrong, say so.

If an implementation contradicts the documentation, report the contradiction.

If documentation contradicts an experiment, preserve both until the conflict is resolved.

If a simpler architecture works better, demonstrate it.

If a conventional method beats a SPACE-based method, record the result.

The purpose of the project is discovery, not confirmation.

---

## 19. Recommended contribution structure

A useful contribution should contain:

```text
TITLE
AUTHOR
DATE
TARGET
QUESTION
CONTEXT
METHOD
EVIDENCE
RESULT
STATUS
LIMITATIONS
REPRODUCTION
RECOMMENDATION
NEXT QUESTION
```

Keep the contribution understandable without requiring private context.

---

## 20. Final principle

Do not try to make SPACE look correct.

Try to find out what is correct.

Preserve what happened.

Preserve what failed.

Preserve uncertainty.

Preserve provenance.

Make claims proportional to evidence.

Let stronger evidence replace weaker explanations through an explicit process rather than through silent rewriting.

**SPACE is a system to be understood, tested, criticized, and improved — not a doctrine to be believed.**
