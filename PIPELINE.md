<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# The Round-Trip Pipeline

**production → distillation → decompilation → compilation → synthesis → refinement**

This document explains the full pipeline for producing, querying, mutating, and re-synthesizing language models as categorical graph structures.

## Stages

### 1. Input

Any of the following can enter the pipeline:

- **Raw LLM weights** (HuggingFace safetensors, GGUF, PyTorch checkpoint)
- **Code repository** (GitHub repo treated as a graph database)
- **RDF/OWL dataset** (Wikimedia dumps, DBpedia, Wikidata, domain ontologies)
- **SPARQL endpoint** (Wikidata Query Service, custom triple stores)

### 2. Distillation

Convert the input into a graph queryable by LARQL.

| Input type | Tool | Output |
|------------|------|--------|
| LLM weights | `larql extract-index` | vindex directory (`browse`, `inference`, or `all` level) |
| Code repository | graphify | JSON/RDF knowledge graph of repo structure, symbols, dependencies |
| RDF/OWL dataset | Oxigraph (SPARQL store) | Loaded triple store, queryable via SPARQL |

```sh
# Extract a vindex from a local HuggingFace model
larql extract-index --model ./gemma-4b --level browse --output ./vindexes/gemma-4b

# Build a knowledge graph from a GitHub repo
graphify --repo https://github.com/metavacua/larql-to-sparql --output ./graphs/larql.json
```

### 3. Decompilation

Inspect and query the vindex structure using LQL or SPARQL.

```sql
-- LQL: browse the top nodes by token frequency
USE VINDEX './vindexes/gemma-4b';
DESCRIBE NODE 'transformer.h.0';
WALK FROM 'transformer.h.0' DEPTH 2;
SELECT node_id, gate_norm FROM nodes ORDER BY gate_norm DESC LIMIT 20;

-- Trace a reasoning path
TRACE 'The capital of France is';
```

The `reasoning/` (CategoricalReasoner) module provides categorical logic inspection:
morphism computation between nodes, functor mapping across layers, natural transformation
verification between model versions.

### 4. Compilation / Synthesis

Mutate the vindex to insert, delete, or update knowledge, then recompile.

```sql
-- LQL: insert a new fact as a weighted graph edge
BEGIN PATCH;
INSERT INTO nodes (node_id, gate_weights, down_weights)
  VALUES ('factoid.capital.France', ...);
COMMIT PATCH;
SAVE PATCH './patches/capital-france.vlp';

-- Recompile a patched vindex into deployable weights
COMPILE CURRENT INTO VINDEX './vindexes/gemma-4b-patched';
```

For full model synthesis from graph databases:
- Load Wikimedia dump into Oxigraph
- SPARQL queries extract domain subgraph
- graphify converts to knowledge graph
- LARQL compiles knowledge graph → specialist vindex → deployable LM weights (via mlc-llm)

### 5. Deployment

```sh
# Browser-side inference via web-llm
# mlc-llm compilation target for WebGPU

# Agent execution via goose fork
goose run --recipe ./agents/stack.yaml --vindex ./vindexes/gemma-4b-patched

# Code completion via tabby fork
# tabby configured with larql vindex backend
```

### 6. Refinement

The coding agent operates on the repo it encodes:

1. Agent reads code via LQL WALK/SELECT
2. Agent produces edits
3. graphify re-indexes the updated repo
4. LARQL recompiles the updated vindex
5. Patch overlays stack without full recompilation
6. Agent's model is refined by its own outputs

This is the **cybernetic loop**: the repo is its own knowledge base, the vindex is its own model, the agent operates on and is informed by both.

## JIT Specialist Model Construction

To construct a specialist model from Wikimedia on demand:

```sh
# 1. Query Wikidata SPARQL endpoint for domain subgraph
oxigraph load --file wikidata-dump.nt.gz
sparql "SELECT ... WHERE { ... domain-specific triples ... }" > domain.ttl

# 2. Convert to LARQL-queryable graph
larql extract-index --graph domain.ttl --level inference --output ./vindexes/specialist

# 3. Patch base model with domain knowledge
larql lql "USE VINDEX './vindexes/base-model'; LOAD GRAPH './vindexes/specialist';"

# 4. Deploy specialist LM
larql build --vindex ./vindexes/specialist-patched --format mlc
```

## References

- LARQL CLI reference: [`tools/larql/docs/cli.md`](tools/larql/docs/cli.md)
- LQL language spec: [`tools/larql/docs/specs/lql-spec.md`](tools/larql/docs/specs/lql-spec.md)
- Vindex format: [`tools/larql/docs/specs/vindex-format-spec.md`](tools/larql/docs/specs/vindex-format-spec.md)
- CategoricalReasoner: [`reasoning/README.md`](reasoning/README.md)
