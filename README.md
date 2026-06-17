<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# GeodesicLangModel

Architectural hub for the **Geometric Coherence Framework (GCF)** research program and its production goal: **category-theoretical swarm language models** (or *swarm categories*) — specialist LMs compiled just-in-time from graph databases, operating as a coordinated ensemble of coding agents whose morphisms are formally tractable.

## The Core Pipeline

```
GitHub repo / graph DB
        ↓  graphify: repo → queryable knowledge graph
SPARQL store (Oxigraph)  ←→  RDF/OWL endpoints / Wikimedia dumps
        ↓  LARQL: graph → vindex (category-theoretical object)
    vindex
        ↙         ↘
decompile/query   compile/synthesize
   (LQL)            (mlc-llm / web-llm)
        ↘         ↙
  specialist LM  (JIT, on-demand)
        ↓
  swarm categories  (goose fork + tabby fork; each LM = categorical object)
        ↓  orientation layer
  open-deep-research + SPARQL/GraphQL/SQL synthesis
        ↑  (refinement loop)
```

The full round-trip: **production → distillation → decompilation → compilation → synthesis → refinement**

## Geometric Coherence Framework (GCF)

The theory that LLMs are discrete geodesic graphs approximating continuous Riemannian manifolds, where coherence depends on alignment between three structures:

1. The **FFN graph** (stored relational structure)
2. The **attention mechanism** (local metric / curvature encoding)
3. The **residual stream** (current positional state)

### Hypotheses Under Test

| ID | Statement |
|----|-----------|
| **H1** | LLM weights are isomorphic to a discrete geodesic graph (vindex) approximating a smooth Riemannian manifold. |
| **H2** | Attention weights encode the local metric distortion of the graph (discrete analog of the metric tensor field). |
| **H3** | Coherent reasoning requires alignment between FFN graph, attention curvature, and residual stream position. |
| **H4** | The frozen graph diverges progressively from world-state after training cutoff, producing coordinate misalignment, not just knowledge gaps. |
| **H5** | RAG injects correct facts but does not recalibrate attention navigation; reasoning over retrieved content fails systematically. |
| **H6** | Operational incompleteness bound (Rosko, [arXiv:2511.21296](https://arxiv.org/abs/2511.21296)): some true propositions about an LLM's knowledge cannot be decided by any finite token-observation sequence. |

## Research Constellation

### Cluster 1 — Theoretical Foundation (in this repo)

| Component | Location | Role |
|-----------|----------|------|
| LARQL toolchain | [`tools/larql/`](tools/larql/) | Core Rust + WASM toolchain; LLM weights → vindexes; LQL query/mutate; vindex = category-theoretical object |
| CategoricalReasoner | [`reasoning/`](reasoning/) | Java + SPARQL algorithms for categorical logic; morphism algorithms; vindexes are category-theoretical objects in this sense |
| Theory | [`theory/`](theory/) | LaTeX thesis + HTML proof pipeline; the GCF theoretical write-up |
| Subclass ontology | [`ontology/subclass/`](ontology/subclass/) | Subclass ontology scaffold |
| Experiments | [`experiments/`](experiments/) | Falsifiable experiment classes A–F against the GCF hypotheses |

### Cluster 2 — LARQL Pipeline Layer (sibling forks)

Toolchains for extending/reducing LARQL and realizing the round-trip. See [`RESEARCH_STACK.md`](RESEARCH_STACK.md).

graphify · Oxigraph · mlc-llm · web-llm · wasmspec · seaography · async-graphql · graphql-parser

### Cluster 3 — Coding Agent Harness (sibling forks)

See [`agents/`](agents/) for the integration design.

goose · tabby · web-llm · open-deep-research

## Experiment Classes

| Class | Target | Subdirectory |
|-------|--------|--------------|
| **A** | Vindex round-trip fidelity | [`experiments/A_vindex_roundtrip/`](experiments/A_vindex_roundtrip/) |
| **B** | Surgical node insertion / deletion | [`experiments/B_node_surgery/`](experiments/B_node_surgery/) |
| **C** | RAG navigation failure | [`experiments/C_rag_navigation/`](experiments/C_rag_navigation/) |
| **D** | Temporal drift measurement | [`experiments/D_temporal_drift/`](experiments/D_temporal_drift/) |
| **E** | Curvature proxy measurement | [`experiments/E_curvature_proxy/`](experiments/E_curvature_proxy/) |
| **F** | Incompleteness boundary mapping | [`experiments/F_incompleteness_boundary/`](experiments/F_incompleteness_boundary/) |

See [`EXPERIMENT_TEMPLATE.md`](EXPERIMENT_TEMPLATE.md) for the logging schema and [`registry.md`](registry.md) for the running index.

## Quick Start

```sh
# Clone with all submodules
git clone --recurse-submodules https://github.com/metavacua/GeodesicLangModel

# Build LARQL (requires Rust stable + nightly proc-macro support)
cd tools/larql
cargo build --release

# Run the LARQL REPL
./target/release/larql repl

# Run a Class A experiment
# See experiments/A_vindex_roundtrip/README.md for instructions
```

## Key Documents

| Document | Purpose |
|----------|---------|
| [`PIPELINE.md`](PIPELINE.md) | Full round-trip explained end-to-end |
| [`CONVERGENCE.md`](CONVERGENCE.md) | Mathematical bridge: CategoricalReasoner ↔ LARQL vindexes |
| [`DISCOVERIES.md`](DISCOVERIES.md) | Empirical observations from the SynthPlayground prototype series |
| [`RESEARCH_STACK.md`](RESEARCH_STACK.md) | Full constellation map with all sibling repos |
| [`AGENTS.md`](AGENTS.md) | Development guidance across all subsystems |

## References

- LARQL toolchain docs: [`tools/larql/docs/`](tools/larql/docs/)
- Rosko, M. *Operational Incompleteness in Large Language Models.* [arXiv:2511.21296](https://arxiv.org/abs/2511.21296)
- Mabrok, M. et al. *Curvature structure in transformer attention manifolds.* [arXiv:2603.22301](https://arxiv.org/abs/2603.22301)

See [`references/`](references/) for the maintained bibliography.

## Licensing

Dual-licensed, **[REUSE](https://reuse.software/)-compliant**:

| License | Scope |
|---------|-------|
| **CC-BY-SA-4.0** | Creative works: prose, documentation, experiment logs, figures |
| **AGPL-3.0-or-later** | Software and program-corresponding data |

```sh
pipx run reuse lint
```
