<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Formalization: Mathematical Structures → Code Constructs

Reduction of `MATHEMATICAL_FOUNDATIONS.md` to implementation mappings.

| Mathematical structure | Code construct | Location |
|---|---|---|
| Riemannian manifold (M, g) | `VectorIndex { num_layers, hidden_size, gate_vectors, embeddings }` | `larql-vindex/src/index/core.rs` |
| `larql extract` | `weights → (M, g)` i.e. safetensors → vindex | `crates/larql-cli/src/commands/extraction/extract_index_cmd.rs` |
| Graph Laplacian `L_ε` on sampled points | `graph.json` (NetworkX node-link edges from `graphify update`) | `tools/graphify-to-vindex/graphify_to_vindexfile.py` |
| `L_ε → Δ_M` convergence (sample density → ∞) | `larql build Vindexfile && larql compile --base model` | `larql-cli/src/commands/extraction/compile_cmd/` |
| Functor `F: Diff → Ab` (homology / traversal) | `larql lql "WALK entity TOP k;"` | `larql-vindex/src/lql/` |
| Sheaf `𝒪_X` (local holomorphic sections) | `FeatureMeta { top_token, relation, target }` in `down_meta.bin` | `larql-vindex/src/index/types.rs` |
| Global section / sheaf cohomology `H^0` | `larql lql "SELECT * FROM vindex WHERE relation = r;"` | LQL query engine |
| Obstruction class `H^1` (non-global facts) | `INFER` edges (not directly compilable; require forward-pass gate) | `larql-vindex/src/lql/infer.rs` |
| Kähler triple `(J, g, ω)` | `larql extract --level all` → gate (ω) + attn (g) + FFN (J) | `extract_index_cmd.rs` |
| Gauss–Bonnet `∫κ dA = 2πχ(M)` | `larql dev circuit-discover --index vindex/` | `larql-cli/src/commands/dev/circuit_discover_cmd.rs` |
| Euler characteristic `χ = V - E + F` | `len(nodes) - len(links) + communities` from `graph.json` | graphify output |
| Branched covering (sheets over base) | specialist vindex per repo, each `FROM base-vindex` | `Vindexfile` + `larql build` |
| Chern class `c_1` (curvature of FFN bundle) | `larql compile --gate-scale 1.0 --alpha 0.3` | `compile_cmd/edge.rs::install_edge` |
| Categorical morphism | attention weight matrix `W_Q, W_K, W_V, W_O` | `attn_weights.bin` |
| Functor composition (layer stack) | forward pass through vindex layers | `larql-vindex/src/inference/forward.rs` |
| Natural transformation (between functors) | LQL `DESCRIBE entity` (all edges = full functor image at one object) | LQL DESCRIBE |
| ∞-morphism / swarm routing | goose coordinator querying N specialist vindexes via MCP | `crates/goose-mcp/` |
| `VindexStorage` (pullback seam for ∞-cat) | `StorageBackend` trait (mmap / in-memory / GPU-resident) | `larql-vindex/src/format/storage.rs` |
| CategoricalReasoner morphisms (LM/LK/LJ) | Java proof-tree algorithms = reference spec for LQL INFER | `reasoning/src/` |
| No-Contraction / No-Cloning (Girard 1987; Zizzi quant-ph/0611119) | Irreversibility of `larql compile` (non-unitary; information-lossy dimensional reduction) | `compile_cmd/` |
| Liar metatheorem / Zizzi entanglement `@` (non-idempotent) | Self-referential autoresearch loop: non-convergence (babelian) and paraconsistent convergence (non-babelian) are both metatheorems | `agents/autoresearch/` |
| Alexandroff compactification `V* = V ∪ {∞}` | Ideal fixed point: `∞` = fully-consistent oracle (H6; unreachable in V) and limit of contradiction profile (non-babelian; reachable) | DISCOVERIES.md |
| Babelian language (consistent, Tarski-hierarchical, plural) | Non-homoiconic API layers: Tabby → LQL → vindex (strict semantic ordering; decider at each boundary) | `agents/stack.md` |
| Non-babelian language (paraconsistent, singular, homoiconic) | Autoresearch loop: codebase (object language) = specialist LM (metalanguage); AMBIGUOUS edges = tolerated contradictions | `agents/autoresearch/` |

## Key Pipeline Equations

```
repo  →[graphify update]→  (V, E)        # discrete graph sample G_ε
G_ε   →[adapter]→          Vindexfile     # INSERT per edge
Vindexfile →[larql build]→  vindex/        # graph Laplacian embedded
vindex/ →[larql compile]→  model.safetensors  # Δ_M baked into weights
```

```
vindex = (M, g)  with
  gate_vectors  ↔  symplectic form ω      (Kähler)
  attn_weights  ↔  Riemannian metric g    (Kähler)
  FFN weights   ↔  complex structure J    (Kähler)
  down_meta     ↔  sheaf 𝒪_X sections    (holomorphic data)
```
