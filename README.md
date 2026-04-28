<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# GeodesicLangModel

Systematic experimental testing of the **Geometric Coherence Framework (GCF)** — the theory that LLMs operate as discrete geodesic graphs (vindex, via [LARQL](https://github.com/chrishayuk/larql)) approximating Riemannian semantic manifolds, where coherent inference corresponds to action-minimizing geodesic walks.

This repository is a research instrument: it designs, runs, logs, and analyzes falsifiable experiments testing both **inherited** claims (from established literature on geodesic language models) and **framework-distinctive** claims (novel synthesis or original observation).

The consolidated theoretical framework is in [`framework/geocoherence-framework.md`](framework/geocoherence-framework.md). The current version is **v0.2** (2026-04-28).

## Hypotheses Under Test

The framework distinguishes inherited claims from framework-distinctive claims to support honest attribution and to focus experimental effort on what is genuinely novel.

### Inherited from Literature (HL)

| ID | Statement | Source |
|----|-----------|--------|
| **HL1** | LLM hidden states reside on a smooth Riemannian semantic manifold approximable by tractable surfaces. | GeoGNN, GSS, RSLM |
| **HL2** | Coherent inference corresponds to geodesic trajectories on the semantic manifold (Geodesic Hypothesis). | STP (arXiv:2602.22617) |
| **HL3** | Geodesic structure arises from the Principle of Least Action under training dynamics. | STP |
| **HL4** | Departures from the manifold during operations produce systematic representation degradation ("semantic drift"). | GeoGNN (arXiv:2511.09042) |

### Framework-Distinctive (HF, Subject to Literature Verification)

| ID | Statement |
|----|-----------|
| **HF1** | The vindex (LARQL graph extraction) is the discrete operational object whose continuum limit is the semantic manifold. |
| **HF2** | Attention weights encode the local Riemannian metric; in current LLMs, this metric is fixed at training time. |
| **HF3** | Coherence requires alignment between FFN graph (manifold structure), attention metric, and residual position. |
| **HF4** | The manifold has three-zone density structure: dense interior (reliable inference), horizon region (refusal/confabulation), beyond-horizon (undecidable behavior). |
| **HF5** | LLMs can be reliably extended by suturing the dense interior to well-defined external graphs at proper interfaces preserving geodesic continuity. |
| **HF6** | Suturing to unbounded external graphs crosses a critical scale at which the system transitions from sub-Turing to Turing-complete (the "Turing catastrophe"). |
| **HF7** | For a given logical fragment L, valid inferences correspond to action-bounded walks; jointly-determinable observables correspond to commuting walk-pairs (Curry-Howard-Lambek extension). |

### Inherited Bounds (HB)

| ID | Statement | Source |
|----|-----------|--------|
| **HB1** | There exist true propositions about a model's knowledge that no finite token observation can decide. | Rosko (arXiv:2511.21296) |

## Experiment Classes (v0.2 Priority Order)

### Priority Classes

| Class | Target | Subdirectory |
|-------|--------|--------------|
| **H** | Action functional characterization (leverages STP loss as proxy) | `experiments/H_action_functional/` (to scaffold) |
| **C'** | Disorientation signature in agentic contexts | [`experiments/C_rag_navigation/`](experiments/C_rag_navigation/) |
| **I** | Suture engineering and Turing catastrophe onset | `experiments/I_suture_catastrophe/` (to scaffold) |
| **G** | Logic-walk correspondence | `experiments/G_logic_walk/` (to scaffold) |

### Deprioritized (Retained as Scaffolding)

| Class | Target | Reason |
|-------|--------|--------|
| **A** | Vindex round-trip fidelity | Substantially demonstrated by Hay |
| **B** | Surgical node insertion / deletion | Substantially demonstrated (Atlantis/Poseidon) |
| **D** | Temporal drift measurement | Subsumed into H and C' under three-zone framing |
| **E** | Curvature proxy measurement | Cross-validation work, lower priority |
| **F** | Incompleteness boundary mapping | Superseded by Class G |

See [`registry.md`](registry.md) for the running experiment index and [`EXPERIMENT_TEMPLATE.md`](EXPERIMENT_TEMPLATE.md) for the standard logging schema.

## Self-Applicable Instance

The framework's predictions about disorientation behavior apply to the agent maintaining this repository. A documented instance of the agent failing to discover its own prior actions (creating this very repository) is recorded in [`framework/disorientation-self-instance-20260428.md`](framework/disorientation-self-instance-20260428.md). This is observational evidence for HF3, HF4, and HB1 in a self-applicable form.

## Primary References

### Inherited Theoretical Foundations

- **STP** — Huang, H. et al. *Semantic Tube Prediction.* [arXiv:2602.22617](https://arxiv.org/abs/2602.22617). Formalizes Geodesic Hypothesis and least-action derivation.
- **Multi-step Latent Forecasting via STP** — [arXiv:2604.18464](https://arxiv.org/abs/2604.18464). Empirical refinement: trajectories are smooth curves, not straight lines.
- **GeoGNN** — [arXiv:2511.09042](https://arxiv.org/abs/2511.09042). Names "semantic drift"; log-exp manifold operations.
- **GSS** — [arXiv:2602.23665](https://arxiv.org/abs/2602.23665). Learned local Riemannian metrics; geodesic retrieval. Substantially overlaps with HF5.
- **RSLM** — [ResearchGate 399875145](https://www.researchgate.net/publication/399875145). Geodesic Policy Networks.

### Operational Substrate

- **LARQL** — [github.com/chrishayuk/larql](https://github.com/chrishayuk/larql). Vindex EXTRACT/WALK/INSERT/DELETE/PATCH/COMPILE.
- **Hay video series** — KV cache ([TYgCRPCAFhE](https://www.youtube.com/watch?v=TYgCRPCAFhE), [HJlWDSyDcD4](https://www.youtube.com/watch?v=HJlWDSyDcD4)) and LARQL inference ([8Ppw8254nLI](https://www.youtube.com/watch?v=8Ppw8254nLI)).

### Bounds and Validation

- **Rosko, M.** *Operational Incompleteness in LLMs.* [arXiv:2511.21296](https://arxiv.org/abs/2511.21296). Source for HB1.
- **Mabrok, M. et al.** *Curvature structure in transformer attention manifolds.* [arXiv:2603.22301](https://arxiv.org/abs/2603.22301). Empirical evidence for HF2.

See [`references/`](references/) for the maintained bibliography with full hypothesis cross-references.

## Licensing

This repository is **dual-licensed** and **[REUSE](https://reuse.software/)-compliant** (REUSE 3.x). License assignment is declared per-file via SPDX headers and `REUSE.toml`.

| License | Scope | SPDX Identifier |
|---------|-------|-----------------|
| **[CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt)** | *General default.* All creative works in the repository (prose, documentation, experiment logs, figures, prose-form data). | `CC-BY-SA-4.0` |
| **[AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt)** | *Specific override.* Software, and any data that corresponds to a program (i.e., data that is, or is known to encode, executable behavior). | `AGPL-3.0-or-later` |

### Licensing Rationale

A GitHub repository is a `schema.org/Collection` of `schema.org/CreativeWork` instances. CC-BY-SA-4.0 is the natural general license over creative works; AGPL-3.0-or-later is the specific license for the subclass of creative works that are software. There is a strict morphism CC-BY-SA-4.0 → GPL-family for compatibility purposes (per Creative Commons FAQ and FSF compatibility analysis), so this dual scheme is internally consistent.

**Software-vs-data classification rule:**

> Data that can be put in correspondence with a program is *precisely software* and is covered by **AGPL-3.0-or-later**. Data that cannot be, or is not known to be, in such correspondence is **CC-BY-SA-4.0** by default.

This follows the Curry-Howard-style view that programs and data are interconvertible under a known correspondence; the license tracks the correspondence, not the file extension. Per-file SPDX tags resolve all cases. Note: this rule is itself a small instance of the HF7 (logic-walk-measurement) correspondence applied at the level of authorial classification.

### Verifying License Compliance

```sh
pipx run reuse lint
```

A GitHub Actions workflow runs the same check on every push and pull request.
