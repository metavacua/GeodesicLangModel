<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Agent Stack: Technical Integration Design

## goose fork — LARQL MCP Extension

### Extension location

`crates/goose-mcp/src/larql/` in `metavacua/goose`

### Tools exposed to the agent

```
extract_vindex(model_path: str, level: str) → vindex_path: str
lql_query(vindex_path: str, statement: str) → rows: list
lql_mutate(vindex_path: str, statement: str) → patch_path: str
compile_vindex(vindex_path: str, output_path: str, format: str) → str
load_graph(graph_path: str, vindex_path: str) → str
```

### Transport

The MCP extension calls the `larql` binary via stdio (for lightweight ops) or the
`larql-server` HTTP/gRPC API (for long-running extraction or compilation).

The server is started with: `larql serve --vindex-dir ./vindexes --port 8765`

### Example goose recipe

```yaml
# agents/recipes/compile-specialist.yaml
name: compile-specialist-lm
steps:
  - tool: extract_vindex
    args:
      model_path: "{{ inputs.model_path }}"
      level: "browse"
  - tool: load_graph
    args:
      graph_path: "{{ inputs.domain_graph }}"
      vindex_path: "{{ steps[0].vindex_path }}"
  - tool: compile_vindex
    args:
      vindex_path: "{{ steps[1].vindex_path }}"
      output_path: "{{ inputs.output_path }}"
      format: "mlc"
```

## tabby fork — LQL Retrieval Backend

### Integration point

tabby's retrieval interface (`crates/tabby-retrieval/` or equivalent) is extended with
an `LqlRetriever` that wraps the LARQL LQL executor:

```rust
struct LqlRetriever {
    vindex_path: PathBuf,
    client: LarqlClient,  // HTTP client to larql-server
}

impl Retriever for LqlRetriever {
    fn retrieve(&self, context: &CompletionContext) -> Vec<Snippet> {
        // Walk the FFN graph from the cursor symbol
        let rows = self.client.lql(
            &format!("USE VINDEX '{}'; WALK FROM '{}' DEPTH 2;",
                     self.vindex_path.display(),
                     context.current_symbol)
        );
        rows.into_iter().map(Snippet::from).collect()
    }
}
```

This tests **H5** (RAG navigation failure): the LQL WALK provides graph-structured
context that navigates the attention topology, not just bag-of-words retrieval.

## open-deep-research — Orientation Layer

### Role

Run before task assignment. Takes a user query, performs web research, produces
a structured domain summary. That summary is used to:

1. Select the appropriate specialist vindex (domain match)
2. Or trigger JIT compilation from a Wikimedia/SPARQL source if no vindex exists
3. Provide context to the goose recipe as `{{ inputs.domain_graph }}`

### Integration

open-deep-research outputs a structured report (Markdown + optional RDF/JSON-LD).
A lightweight adapter converts the report to SPARQL queries for Oxigraph, or
to LQL SELECT statements for an existing vindex.

```sh
# Orientation for a "Byzantine history" coding task
open-deep-research "Byzantine Empire administrative structure" \
  --format rdf \
  --output ./context/byzantine.ttl

# Load into Oxigraph
oxigraph load --file ./context/byzantine.ttl

# SPARQL → LARQL → specialist vindex
sparql "SELECT ?concept ?relation WHERE { ... }" \
  | larql extract-index --graph - --level inference \
    --output ./vindexes/specialist-byzantine
```

## web-llm — Browser Deployment

Specialist LMs compiled via mlc-llm can be deployed to the browser via web-llm:

```sh
# Compile specialist vindex to MLC format
larql build --vindex ./vindexes/specialist --format mlc --output ./dist/specialist-mlc

# web-llm loads the MLC model in the browser
# No server-side inference required
```

This enables fully client-side swarm LM operation for privacy-sensitive tasks.

## GraphQL-for-GitHub Adapter (Priority Integration)

The highest-priority near-term integration for the **codebase-as-LM** milestone:
a GraphQL-for-GitHub adapter that bridges GitHub's GraphQL API to the LARQL pipeline.

```
GitHub GraphQL API
    → adapter (seaography / async-graphql bridge)
    → RDF/graph representation (Oxigraph or LQL)
    → larql extract-index
    → vindex (the repo-as-LM)
```

This implements the core thesis in one concrete step: any GitHub repository becomes a
queryable knowledge graph, compiled to a vindex, serving as a specialist LM for the
agent operating on that repository. The graphify fork (`metavacua/graphify`) is a
candidate implementation of this same distillation step.

## mlc-llm — GPU Coverage Adapter

`metavacua/mlc-llm` (fork) serves as the **GPU-coverage adapter** in the stack:

```sh
# Compile vindex to MLC format for GPU-accelerated inference
larql build --vindex ./vindexes/specialist --format mlc --output ./dist/specialist-mlc

# mlc-llm loads and serves the compiled model on any supported GPU
```

mlc-llm/TVM provides the widest GPU coverage across Metal, CUDA, ROCm, and Vulkan —
making it the adapter that unlocks the full GPU matrix for compiled specialist LMs,
without LARQL itself needing to implement all GPU backends.

## web-llm — Browser Front-End

`metavacua/web-llm` (fork) is the **browser-side deployment front-end**:

```sh
# Deploy specialist LM (MLC-compiled) to browser via web-llm
# No server-side inference required; privacy-preserving for local corpora
```

web-llm consumes mlc-compiled models, runs them in WebGPU/WebAssembly, and exposes
an OpenAI-compatible API from inside the browser. The swarm runs client-side.

## Query Synthesis Summary

The four synthesis surfaces work together:

| Surface | Technology | Role |
|---------|-----------|------|
| SPARQL | Oxigraph | Knowledge graph queries (Wikimedia, domain ontologies) |
| LQL | larql-lql crate | Vindex queries and mutations |
| GraphQL | seaography / async-graphql + GitHub adapter | Codebase-as-LM (priority); API layer over vindex data for web UIs |
| SQL | (future) SeaORM via seaography | Relational views over vindex metadata |

Combined, these four surfaces allow the construction of specialist LMs from any
graph-structured knowledge source, with a unified query interface across the stack.
