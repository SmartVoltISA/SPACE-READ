# SPACE-READ — External Contributions

This directory is the public workspace for material created by people, external LLMs and independent researchers while working with the published SPACE architecture.

## Purpose

`SPACE-READ` publishes the controlled public view of SPACE.

`CONTRIBUTIONS/` stores external work **about or around SPACE**. It is not part of SPACE Core and must never be interpreted as canonical Core state.

A contribution may contain:

- research notes;
- working journals;
- independent analyses;
- replications;
- experiments;
- critiques and counterexamples;
- implementation notes;
- proposals;
- questions;
- failed attempts and negative results.

## Boundary

```text
SPACE CORE
    |
    | controlled publication
    v
SPACE-READ
    |
    +---- official published material
    |
    +---- CONTRIBUTIONS/
             |
             +---- human
             +---- external AI
             +---- researcher
             +---- independent implementation
```

`CONTRIBUTIONS/` does not write back to SPACE Core.

A contribution is not automatically an accepted change, canonical fact, or new SPACE state.

## Required distinction

Always preserve:

`UNKNOWN != TRUE`

`HYPOTHESIS != VERIFIED`

`PROPOSAL != ACCEPTED CHANGE`

`CONTRIBUTION != CORE`

`FORK != ORIGINAL SPACE`

## Recommended contribution record

Each substantial contribution should identify:

- author or system;
- contribution type;
- date;
- SPACE publication/version used;
- target object or question;
- claim or objective;
- evidence;
- method;
- observed result;
- limitations;
- provenance;
- status;
- next step.

Use `CONTRIBUTION_TEMPLATE.md` as the starting point.

## Review

External material may be submitted by pull request or another explicitly supported review mechanism.

The normal path is:

`CONTRIBUTION -> REVIEW -> VALIDATION / REPLICATION -> ACCEPT / REJECT / HOLD`

Only an explicit trusted publication process can promote material into the official published layer. Nothing in this directory grants write access to SPACE Core.

## Security

Never put credentials, API keys, private keys, passwords, secrets, confidential documents or unnecessary personal data into this directory.

The contribution workspace is deliberately separated from the canonical organism.
