<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# GeodesicLangModel

Systematic experimental testing of the **Geometric Coherence Framework (GCF)** — the theory that LLMs are discrete geodesic graphs approximating continuous Riemannian manifolds, where coherence depends on alignment between three structures:

1. The **FFN graph** (stored relational structure)
2. The **attention mechanism** (local metric / curvature encoding)
3. The **residual stream** (current positional state)

This repository is a research instrument: it designs, runs, logs, and analyzes falsifiable experiments against the GCF.

## Hypotheses Under Test

| ID | Statement |
|----|-----------|
| **H1** | LLM weights are isomorphic to a discrete geodesic graph (vindex) approximating a smooth Riemannian manifold. |
| **H2** | Attention weights encode the local metric distortion of the graph (discrete analog of the metric tensor field). |
| **H3** | Coherent reasoning requires alignment between FFN graph, attention curvature, and residual stream position. |
| **H4** | The frozen graph diverges progressively from world-state after training cutoff, producing coordinate misalignment, not just knowledge gaps. |
| **H5** | RAG injects correct facts but does not recalibrate attention navigation; reasoning over retrieved content fails systematically. |
| **H6** | Operational incompleteness bound (Rosko, [arXiv:2511.21296](https://arxiv.org/abs/2511.21296)): some true propositions about an LLM's knowledge cannot be decided by any finite token-observation sequence. |

## Experiment Classes

| Class | Target | Subdirectory |
|-------|--------|--------------|
| **A** | Vindex round-trip fidelity | [`experiments/A_vindex_roundtrip/`](experiments/A_vindex_roundtrip/) |
| **B** | Surgical node insertion / deletion | [`experiments/B_node_surgery/`](experiments/B_node_surgery/) |
| **C** | RAG navigation failure | [`experiments/C_rag_navigation/`](experiments/C_rag_navigation/) |
| **D** | Temporal drift measurement | [`experiments/D_temporal_drift/`](experiments/D_temporal_drift/) |
| **E** | Curvature proxy measurement | [`experiments/E_curvature_proxy/`](experiments/E_curvature_proxy/) |
| **F** | Incompleteness boundary mapping | [`experiments/F_incompleteness_boundary/`](experiments/F_incompleteness_boundary/) |

See [`EXPERIMENT_TEMPLATE.md`](EXPERIMENT_TEMPLATE.md) for the standard logging schema and [`registry.md`](registry.md) for the running experiment index.

## References

- LARQL toolchain: <https://github.com/chrishayuk/larql>
- Rosko, M. *Operational Incompleteness in Large Language Models.* [arXiv:2511.21296](https://arxiv.org/abs/2511.21296)
- Mabrok, M. et al. *Curvature structure in transformer attention manifolds.* [arXiv:2603.22301](https://arxiv.org/abs/2603.22301)

See [`references/`](references/) for the maintained bibliography.

## Licensing

This repository is **dual-licensed** and **[REUSE](https://reuse.software/)-compliant** (REUSE 3.x; tracked toward the 2026 REUSE workflow updates). License assignment is declared per-file via SPDX headers and `REUSE.toml`.

| License | Scope | SPDX Identifier |
|---------|-------|-----------------|
| **[CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt)** | *General default.* All creative works in the repository (prose, documentation, experiment logs, figures, prose-form data). | `CC-BY-SA-4.0` |
| **[AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt)** | *Specific override.* Software, and any data that corresponds to a program (i.e., data that is, or is known to encode, executable behavior). | `AGPL-3.0-or-later` |

### Licensing Rationale

A GitHub repository is a `schema.org/Collection` of `schema.org/CreativeWork` instances. CC-BY-SA-4.0 is the natural general license over creative works; AGPL-3.0-or-later is the specific license for the subclass of creative works that are software. There is a strict morphism CC-BY-SA-4.0 → GPL-family for compatibility purposes (per Creative Commons FAQ and FSF compatibility analysis), so this dual scheme is internally consistent.

**Software-vs-data classification rule:**

> Data that can be put in correspondence with a program is *precisely software* and is covered by **AGPL-3.0-or-later**. Data that cannot be, or is not known to be, in such correspondence is **CC-BY-SA-4.0** by default.

This follows the Curry-Howard-style view that programs and data are interconvertible under a known correspondence; the license tracks the correspondence, not the file extension. Per-file SPDX tags resolve all cases.

### Verifying License Compliance

```sh
pipx run reuse lint
```

A GitHub Actions workflow runs the same check on every push and pull request.
