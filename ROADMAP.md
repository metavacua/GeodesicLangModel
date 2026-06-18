<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# GeodesicLangModel Roadmap

Strategic roadmap for the GCF research program and its production goal:
***swarm categories*** (category-theoretical swarm language models).

This document points to the canonical roadmaps for each subsystem.

---

## Core Toolchain: LARQL

The primary development roadmap lives in the LARQL subtree:

- **Canonical two-track roadmap**: [`tools/larql/ROADMAP.md`](tools/larql/ROADMAP.md)
  — GPU track (Metal → competitive with ollama/llama.cpp) + CPU track (GPU-free sparse
  retrieval on consumer hardware). Architecture rule: "no GPU-only paths in core."

- **Portability track** (fork-specific): [`tools/larql/docs/roadmap/webgpu-wasm-portability.md`](tools/larql/docs/roadmap/webgpu-wasm-portability.md)
  — wasm32 stratification, larql-cli split, VindexStorage browser backend, wgpu/WebGPU,
  LARQL→MLC/TVM adapter, WebLLM front-end. Additive; does not alter the canonical two-track.

---

## Near-Term Milestones (Fork Direction)

### 1. wasm32 compute-tier build gate (W1)

First concrete portability step. Verifies that the already-wasm-ready compute-pure tier
compiles to `wasm32-unknown-unknown`:

```sh
make wasm32-compute-tier-build
```

Non-breaking, additive. Mirrors the canonical ROADMAP's C10/C11 "measure before enforcing."

### 2. GraphQL-for-GitHub adapter (codebase-as-LM)

Bridges GitHub's GraphQL API to the LARQL pipeline:
`GitHub repo → GraphQL query → RDF graph → larql extract-index → vindex`

This is the primary implementation step for the **repo-as-LM** thesis: any GitHub
repository becomes a specialist LM for the agent operating on it.

See [`agents/stack.md`](agents/stack.md) for the integration design.

### 3. larql-cli lib/bin/interface split (W3)

Separates `larql-cli` into three layers:
- `lib.rs` — command logic that lives **inside the wasm host**; takes `&dyn VindexStorage` instead of `&Path`
- `bin/larql.rs` — thin OS entry point; wires clap args + file I/O to lib functions
- `interface/` — wasm host exports (`#[wasm_bindgen]` / WASI exports) vs native OS interface

The key refactor: replace `&Path` args with `&dyn VindexStorage` throughout `lib.rs`.
The OS native impl opens files; the in-memory impl holds bytes from the JS/WASI host;
the result is a clean seam between inside-wasm and outside-wasm code.

Milestone: `cargo build -p larql-cli --lib --target wasm32-unknown-unknown` succeeds.
Runtime test targets: Firefox/Playwright (browser stratum), wasmer (WASI stratum).

### 4. Tabby integration (near-term harness)

`metavacua/tabby` as the coding harness: LQL-backed completions replace BM25/embedding
retrieval. Tests H5 (RAG navigation failure) in a live coding workflow.

See [`agents/README.md`](agents/README.md) and [`agents/stack.md`](agents/stack.md).

### 5. VindexStorage browser backend (W2)

`InMemoryVindexStorage`: a `VindexStorage` impl backed by `Vec<u8>` or JS `ArrayBuffer`.
Plugs into the already-shipped `VindexStorage` trait; no architecture change needed.
Enables vindex loading in browser and wasm32 contexts.

---

## Longer-Term (Fork Direction)

| Milestone | Document |
|-----------|---------|
| wgpu backend (Vulkan + WebGPU) | [portability track](tools/larql/docs/roadmap/webgpu-wasm-portability.md#wgpu-backend-vulkan--webgpu) |
| LARQL → MLC/TVM adapter | [portability track](tools/larql/docs/roadmap/webgpu-wasm-portability.md#larql--mlctvm-adapter-max-gpu-coverage) |
| WebLLM front-end integration | [portability track](tools/larql/docs/roadmap/webgpu-wasm-portability.md#webllm-front-end) |
| wasm32-wasip1 + wasmer path | [portability track](tools/larql/docs/roadmap/webgpu-wasm-portability.md#implementation-order) |
| CategoricalReasoner → Rust migration | [`CONVERGENCE.md`](CONVERGENCE.md) |
| Class A experiments: vindex round-trip | [`experiments/A_vindex_roundtrip/`](experiments/A_vindex_roundtrip/) |
| Class F experiments: incompleteness boundary | [`experiments/F_incompleteness_boundary/`](experiments/F_incompleteness_boundary/) |

---

## Research Horizon

The ultimate aim: a **swarm category** — a small category whose objects are vindexes and
whose morphisms are trainable transformations between specialist LMs, verifiable by
CategoricalReasoner's KeY theorem prover. The swarm operates on the repositories it
encodes; the round-trip is:

> production → distillation → decompilation → compilation → synthesis → refinement

See [`PIPELINE.md`](PIPELINE.md) for the full end-to-end description.
