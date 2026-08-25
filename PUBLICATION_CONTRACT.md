# SPACE-READ — Publication Contract v1.0

## 1. Purpose

This contract defines what may enter the public SPACE-READ layer and how it must be identified, classified, verified and versioned.

SPACE-READ is a publication layer, not a second Core.

## 2. Publication classes

Every published object MUST belong to exactly one primary class:

- `axiom` — explicitly adopted architectural principle;
- `definition` — stable meaning of a term or object;
- `structure` — published topology, component or relation;
- `rule` — operational or architectural rule;
- `hypothesis` — proposition under investigation;
- `experiment` — reproducible experimental record;
- `verified_result` — result that passed the required verification scope;
- `rejected_result` — result rejected by validation;
- `open_question` — unresolved question retained for research;
- `history` — historical record whose publication is explicitly allowed.

A hypothesis MUST NOT be presented as a fact or verified result.

## 3. Required metadata

Each significant published object MUST provide:

- stable `id`;
- `class`;
- `title`;
- `status`;
- `schema_version`;
- `publication_version`;
- `published_at`;
- `provenance`;
- `scope`;
- `content` or a pointer to the published content;
- related objects where applicable.

## 4. Status values

- `draft` — prepared, not reviewed;
- `reviewed` — reviewed for publication;
- `verified` — verified within explicitly stated scope;
- `rejected` — rejected by validation;
- `deprecated` — historically published but no longer current.

Status is not a measure of absolute truth. It describes the state of publication and verification.

## 5. Provenance

`provenance` MUST distinguish:

1. where the material originated;
2. which version or commit was used;
3. what transformation, if any, was performed;
4. who or what reviewed it;
5. what verification scope was applied.

Private Core paths, credentials and sensitive internal details MUST NOT be exposed merely to provide provenance.

## 6. Versioning

Published history is append-only in meaning:

`v1 → v2 → v3`

A new publication supersedes an older one by explicit relation. Older records are not silently rewritten or deleted to hide previous states.

## 7. Promotion rule

The following distinction is mandatory:

`unknown ≠ true`

`hypothesis ≠ verified`

`proposal ≠ accepted change`

`published ≠ universal truth`

A local experiment becomes a stronger architectural statement only after the required evidence and scope are recorded.

## 8. Security boundary

Publication is one-way:

`SPACE Core → validation → SPACE-READ`

There is no publication operation that accepts commands from SPACE-READ and writes to Core.

## 9. External contributions

External humans and AI may submit proposals, analyses, corrections and independent replications through GitHub Issues, Pull Requests or forks. These are external evidence/proposals until explicitly reviewed and published.

No external contribution becomes canonical merely because it exists in GitHub.

## 10. Minimum acceptance checklist

Before publishing a significant object:

- [ ] class is explicit;
- [ ] status is explicit;
- [ ] provenance is recorded;
- [ ] version is recorded;
- [ ] sensitive data is removed;
- [ ] claim scope is explicit;
- [ ] hypotheses are separated from verified results;
- [ ] links and identifiers are valid;
- [ ] publication does not create a write path to Core.
