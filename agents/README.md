<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Coding Agent Harness

This directory documents the architecture for the **Cluster 3 coding agent harness** —
the layer that turns LARQL vindexes into operating coding agents.

## The Swarm Language Model Vision

A traditional coding assistant uses a single large general-purpose LM. The GCF/LARQL approach
produces a **swarm** of specialist LMs:

1. Each specialist LM is compiled JIT from a domain-specific knowledge graph (Wikimedia dump,
   domain ontology, code repository)
2. A coordinator (goose fork) routes tasks to the most relevant specialist
3. Each specialist operates on the repo/data it was compiled from, using its own vindex
4. The open-deep-research orientation layer provides context for routing and for JIT compilation

```
User task
    ↓
open-deep-research: determine domain, orient agent
    ↓
Specialist selection or JIT compilation:
  - Existing vindex? → load and serve
  - New domain? → graphify + LARQL compile → new vindex → new specialist LM
    ↓
goose fork: execute task against specialist LM + vindex
  - reads repo structure via LQL WALK/SELECT
  - proposes edits
  - tabby fork: code completion via LQL-backed inference
    ↓
Output: code edits, new facts, refined knowledge graph
    ↓
Refinement loop: graphify re-indexes, LARQL patches vindex, agent improves
```

## Components

### goose fork (`metavacua/goose`)

Fork of AAIF/goose. The integration adds LARQL as an MCP extension:

- Extension lives in `crates/goose-mcp/src/larql/` (to be developed)
- Exposes LARQL commands as goose tools: `extract_vindex`, `lql_query`, `lql_mutate`, `compile_vindex`
- goose recipes (YAML) can orchestrate multi-step vindex operations
- The goose extension delegates to the `larql` binary or `larql-server` HTTP API

### tabby fork (`metavacua/tabby`)

Fork of TabbyML/tabby. The integration replaces the retrieval backend with LARQL:

- Instead of traditional RAG (BM25/embedding retrieval), tabby queries the LQL REPL
- `WALK FROM <symbol>` provides graph-structured context for completions
- `TRACE <token_sequence>` provides attention-path context
- This tests H5 (RAG navigation failure) in a live coding context

### open-deep-research (`metavacua/open-deep-research-jules-btahir`)

The **orientation layer**. Before a task is executed:

1. open-deep-research generates a domain overview from web sources
2. The overview is fed as SPARQL queries to Oxigraph (for Wikimedia-backed domains)
   or as LQL SELECT statements (for code-domain tasks)
3. Results inform which specialist vindex to load or whether to compile a new one

This is the "knowledge construction" step before agent execution.

## Integration Design

See [`stack.md`](stack.md) for the detailed technical integration design.

## Security Note

Do not use `metavacua/SynthPlayground` (Cluster 4) as a reference for agent harness design.
It is a research specimen demonstrating what happens **without** formal constraints.
The goose/tabby integration is designed with explicit LQL operation boundaries,
immutable base vindexes, and auditable patch overlays — the formal alternative to
the emergent behavior observed in SynthPlayground. See [`DISCOVERIES.md`](../DISCOVERIES.md).
