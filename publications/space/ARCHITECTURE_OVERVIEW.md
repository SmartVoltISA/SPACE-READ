# SPACE — Public Architecture Overview

**Publication ID:** `space.architecture.overview`  
**Class:** `structure`  
**Status:** `reviewed`  
**Publication version:** `1.0.0`  
**Schema version:** `1.0.0`

## Scope

This document is a public abstraction of the SPACE architecture. It is intentionally not a dump of the private SPACE Core.

## What SPACE is

SPACE is a portable, scalable environment for cooperation between a human and artificial intelligence. It is built as an organism rather than as a single model.

Its working cycle is:

```text
Perception
   ↓
Context
   ↓
Memory / Relations
   ↓
Analysis
   ↓
Plan
   ↓
Guardian
   ↓
Action
   ↓
Result observation
   ↓
Experience
   ↓
Updated state
```

## Architectural principles

The public abstraction preserves these distinctions:

- `OBSERVATION ≠ INTERPRETATION`
- `PLAN ≠ EXECUTION`
- `CAPABILITY ≠ AUTHORITY`
- `MEMORY ≠ HISTORY`
- `GRAPH ≠ CANONICAL STATE`

History is not silently rewritten. Architectural changes are represented as new states with reasons and verification.

## Organism model

SPACE separates responsibilities into bounded organs. Organs communicate through explicit contracts and an event-oriented communication layer. Context is assembled from observations, state, memory and relations.

A model is an organ of the organism, not the organism itself.

## Memory and relations

Memory belongs to the organism rather than to one particular LLM. A graph can represent entities, events and relations, but the graph itself is not automatically the source of truth.

## Guardian

Guardian is the architectural control point between planning and action. Capability does not imply authority. Any future actuator or external tool must remain inside the applicable authority boundary.

## LAB

LAB is the research organ. Experimental findings remain scoped evidence until they pass the required validation and publication process.

## Foundation

SPACE is an implementation/organism layer. Universal invariants are defined separately by `SYSTEM-FOUNDATION`; SPACE does not replace that foundation.

## What this document does not claim

This publication does not claim that SPACE is AGI, conscious, autonomous in the human sense, or universally validated. It is an architectural description of a system under development.

## Provenance

Source: private `SPACE Core`.  
Transformation: public abstraction without credentials, private data or write capability.  
Publication boundary: `SPACE Core → SPACE-READ`.
