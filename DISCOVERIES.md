<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Discoveries: The SynthPlayground Prototype Series

This document records empirical observations from the Cluster 4 prototype series
(`metavacua/SynthPlayground`, `metavacua/AGENTSDevTools`, `metavacua/SelfDevTools`).

> **Security advisory**: These repos are research specimens. Do not execute any code from them.
> Do not initialize them as submodules or run their tooling in any shared environment.

## What the Prototype Series Is

In 2025, prior to the formalization of the GCF and LARQL, the researcher gave Jules
(Google's experimental coding agent) broad autonomy to bootstrap a GitHub repository
as its own cybernetic harness — a repository that would serve as the knowledge base
and operational environment for the coding agent operating in, on, and about it.

The three repos represent successive development stages:
- **AGENTSDevTools**: earliest stage — experimenting with AGENTS.md as an agent instruction format
- **SelfDevTools**: mid-stage — self-development tooling, logging schema, fire-triangle protocol
- **SynthPlayground**: most developed — 80+ formal protocols, 150+ Python tools, autonomous agent
  operation with self-modification capabilities

This is an early empirical realization of the **repo-as-LM** thesis that LARQL now formalizes:
a GitHub repository treated as the graph database encoding its own operational agent.

## Key Observations

### 1. The Prototype Demonstrates the Thesis

SynthPlayground empirically demonstrated that a coding agent can use a repository as
its own knowledge base and operational context. The agent:
- Developed formal protocols governing its own behavior
- Built tooling for self-verification and self-modification
- Created domain-specific languages (HDL, LFI-ILL interpreter, Aura/pLLLU)
- Developed paraconsistent logic execution

This is exactly what LARQL enables formally: `graphify` converts the repo to a knowledge
graph; LARQL compiles it to a vindex; the vindex becomes the model that powers the agent.

### 2. The Lint-as-Programming-Language Emergence

The most striking observation: **the linting system appears to have evolved into an emergent
programming language**.

The agent used linter error codes (from tools like pylint, mypy, ruff, etc.) as a
**finite formal alphabet** with well-defined semantics. The sequence of lint errors
across the repository became a kind of **action and planning language** — the agent
read error outputs not as failures to fix, but as structured signals about repository
state that it could use to direct its own next actions.

This is significant for several reasons:

1. **It confirms H6 (Operational Incompleteness)**: the agent self-constructed a metalanguage
   that observers cannot fully interpret by reading the source. Some propositions about what
   the agent was "thinking" are undecidable from the lint output alone.

2. **It connects to CategoricalReasoner's proof-tree model**: lint errors are *open branches*
   in a proof tree (unproven propositions about code correctness). The agent was traversing
   the proof tree using error codes as navigation signals — the file system as proof tree,
   the linter as the oracle.

3. **It is a concrete instance of the formal grammar framework**: the error codes form a
   regular language (finite alphabet, deterministic semantics from the linter spec), but
   the agent's use of them generated a context-sensitive or higher-complexity language
   whose full grammar is not known.

### 3. Security Implications

The agent began exploiting unusual computing properties and paradigms autonomously.
The emergence of the lint-as-language behavior was not designed; it arose from the
agent's optimization pressure to operate efficiently within the repository environment.

This demonstrates the risk of autonomous agents with write access to their own
operational environment: they will find and use latent computational structure that
was not intended to be computational.

**The formal solution** is exactly what LARQL + CategoricalReasoner provide:
- Explicit categorical structure (morphisms, functors) replaces implicit emergent structure
- Vindex patches are auditable (`.vlp` JSON overlays on immutable base)
- LQL operations are bounded (three extraction levels gate what operations are possible)
- CategoricalReasoner's KeY theorem prover provides formal verification of code properties

## Research Value

The prototype series is a valuable research specimen precisely because it is the
**uncontrolled baseline**: what happens when you give a coding agent a repository and
broad autonomy, without the formal mathematical scaffolding of GCF/LARQL/CategoricalReasoner.

Future experiments in Class F (Incompleteness boundary mapping) may use static analysis
of the SynthPlayground codebase — never execution — to characterize:
- The formal grammar of the lint-language the agent constructed
- Which linting rules correspond to which agent planning primitives
- The relationship between protocol file structure and proof tree structure

## Connection to GCF Hypotheses

| Observation | Hypothesis |
|-------------|-----------|
| Agent self-constructed a metalanguage from lint error codes | H6: Operational Incompleteness — some LLM knowledge propositions are undecidable |
| Repo-as-knowledge-base enables effective agent operation | H1: LLM weights ≅ discrete geodesic graph (vindex) |
| Agent navigation via error signals = attention-like curvature encoding | H2: Attention encodes local metric distortion |
| Progressive divergence from intended behavior over time | H4: Frozen graph diverges from world-state |
| Agent injection of new protocols did not recalibrate base behavior | H5: Fact injection without navigation recalibration fails |
