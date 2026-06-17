<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Research Stack

Full map of the GeodesicLangModel research constellation.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GeodesicLangModel (this repo)                    │
│                                                                     │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────┐  ┌──────────┐  │
│  │ tools/larql │  │  reasoning/  │  │  theory/  │  │ ontology/│  │
│  │ (subtree)   │  │ (submodule)  │  │(submodule)│  │ subclass │  │
│  │ Rust + WASM │  │ Java + SPARQL│  │   LaTeX   │  │(submodule│  │
│  └──────┬──────┘  └──────┬───────┘  └─────┬─────┘  └──────────┘  │
│         │                │                 │                        │
│         └────────────────┴─────────────────┘                       │
│                          │                                          │
│              ┌───────────▼───────────┐                             │
│              │     experiments/      │                             │
│              │    (classes A–F)      │                             │
│              └───────────────────────┘                             │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼──────┐   ┌──────▼──────┐   ┌─────▼──────┐
    │ Cluster 2 │   │  Cluster 3  │   │ Cluster 4  │
    │  Pipeline │   │ Agent Harness│   │ Specimens  │
    └────┬──────┘   └──────┬──────┘   └────────────┘
         │                 │
  ┌──────▼──────────┐  ┌───▼────────────────────────┐
  │ graphify        │  │ goose (fork)               │
  │ Oxigraph        │  │ tabby (fork)               │
  │ mlc-llm (fork)  │  │ web-llm (fork)             │
  │ web-llm (fork)  │  │ open-deep-research (fork)  │
  │ wasmspec (fork) │  └────────────────────────────┘
  │ seaography (fork│
  │ async-graphql   │
  │ graphql-parser  │
  └─────────────────┘
```

## Cluster 1 — Theoretical Foundation

These components live inside this repository.

| Component | Integration | GitHub | Role |
|-----------|------------|--------|------|
| larql-to-sparql | git subtree → `tools/larql/` | [metavacua/larql-to-sparql](https://github.com/metavacua/larql-to-sparql) | Core Rust + WASM toolchain; LLM weights → vindexes; LQL query/mutate |
| CategoricalReasoner | git submodule → `reasoning/` | [metavacua/CategoricalReasoner](https://github.com/metavacua/CategoricalReasoner) | Java + SPARQL categorical logic; morphism algorithms; vindexes are categorical objects |
| Theory | git submodule → `theory/` | [metavacua/Theory](https://github.com/metavacua/Theory) | LaTeX thesis + HTML proof pipeline for GCF |
| subclass | git submodule → `ontology/subclass/` | [metavacua/subclass](https://github.com/metavacua/subclass) | Subclass ontology scaffold (main=empty; candidate branches active) |

## Cluster 2 — LARQL Pipeline Layer

Sibling forks for extending/reducing LARQL and realizing the round-trip. Documented here; not merged into this repo.

| Repo | GitHub | Role in round-trip |
|------|--------|-------------------|
| graphify | [metavacua/graphify](https://github.com/metavacua/graphify) *(planned fork of safishamsi/graphify)* | **Distillation**: GitHub repo → queryable knowledge graph; key step for repo → LARQL vindex → LM |
| Oxigraph | [metavacua/oxigraph](https://github.com/metavacua/oxigraph) *(planned fork of oxigraph/oxigraph)* | **SPARQL store**: Rust RDF triple store + SPARQL engine; SPARQL synthesis leg; bridge from CategoricalReasoner's SPARQL execution to Rust pipeline |
| mlc-llm | [metavacua/mlc-llm](https://github.com/metavacua/mlc-llm) | **Production/Synthesis**: ML compilation engine; compile vindexes → deployable LMs |
| web-llm | [metavacua/web-llm](https://github.com/metavacua/web-llm) | **Deployment**: in-browser inference; browser-side vindex round-trip experiments |
| wasmspec | [metavacua/wasmspec](https://github.com/metavacua/wasmspec) | **Compute kernel**: WebAssembly spec; backs `model-compute` crate in larql (universal, arm32-safe) |
| seaography | [metavacua/seaography](https://github.com/metavacua/seaography) | **Query interface**: SeaORM → GraphQL bridge; part of LQL/GraphQL synthesis layer |
| async-graphql | [metavacua/async-graphql](https://github.com/metavacua/async-graphql) | **Query interface**: high-performance GraphQL server library |
| graphql-parser | [metavacua/graphql-parser](https://github.com/metavacua/graphql-parser) | **Query interface**: Rust GraphQL parser; LARQL dependency |

**Note on graphify**: transforms GitHub repositories into queryable knowledge graphs. This implements the core insight that a GitHub repo is a graph database — graphify is the distillation step before LARQL compiles the graph to a vindex.

**Note on Oxigraph**: needs to be forked into the metavacua namespace (`oxigraph/oxigraph`). Provides the SPARQL execution layer that connects CategoricalReasoner's SPARQL operations to the Rust pipeline.

## Cluster 3 — Coding Agent Harness Layer

Sibling forks for orientation, knowledge construction, and agent execution. These are independent development forks, not upstream contribution forks.

| Repo | GitHub | Role |
|------|--------|------|
| goose | [metavacua/goose](https://github.com/metavacua/goose) | AI agent framework (fork of AAIF/goose); extended with LARQL tools via MCP extension (`crates/goose-mcp/`) |
| tabby | [metavacua/tabby](https://github.com/metavacua/tabby) | Self-hosted coding assistant (fork of TabbyML/tabby); LARQL-backed completions from vindex |
| web-llm | [metavacua/web-llm](https://github.com/metavacua/web-llm) | *(also in Cluster 2)* browser-side deployment of JIT-compiled specialist LMs for agents |
| open-deep-research | [metavacua/open-deep-research-jules-btahir](https://github.com/metavacua/open-deep-research-jules-btahir) | **Orientation + knowledge construction**: deep research from web/docs; combined with SPARQL/LARQL/GraphQL/SQL synthesis to construct specialist LMs from Wikimedia dumps JIT |

See [`agents/`](agents/) for the integration design.

## Cluster 4 — Historical Prototype Series (Research Specimens)

Empirical prototypes from the pre-LARQL phase of the research program. **Do not execute code from these repos.**

| Repo | GitHub | Stage | Notes |
|------|--------|-------|-------|
| SynthPlayground | [metavacua/SynthPlayground](https://github.com/metavacua/SynthPlayground) | Most developed | Jules-bootstrapped cybernetic harness; primary empirical demonstration of repo-as-LM thesis; suspected emergent lint-language; suspected subtle malware from autonomous agent operation |
| AGENTSDevTools | [metavacua/AGENTSDevTools](https://github.com/metavacua/AGENTSDevTools) | Earliest | AGENTS.md format experiments |
| SelfDevTools | [metavacua/SelfDevTools](https://github.com/metavacua/SelfDevTools) | Mid-stage | Self-development tool experimentation |

See [`DISCOVERIES.md`](DISCOVERIES.md) for research observations from these repos.

## Supporting / Reference

| Repo | GitHub | Notes |
|------|--------|-------|
| latex-thesis-template | [metavacua/latex-thesis-template](https://github.com/metavacua/latex-thesis-template) | LaTeX template used by `theory/` |
| open-deep-research | [metavacua/open-deep-research-jules-btahir](https://github.com/metavacua/open-deep-research-jules-btahir) | See Cluster 3 |
