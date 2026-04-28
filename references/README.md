<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# References

Maintained bibliography for the Geometric Coherence Framework research program.

The framework distinguishes **inherited** claims (established in published literature) from **framework-distinctive** claims (novel synthesis or original observation). References are organized accordingly. See [`framework/geocoherence-framework.md`](../framework/geocoherence-framework.md) for the consolidated theoretical document.

## Inherited Theoretical Foundations

### Geodesic Hypothesis and Semantic Manifolds

- **Huang, H. et al.** *Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA.* arXiv:2602.22617.
  <https://arxiv.org/abs/2602.22617>
  Formalizes the Geodesic Hypothesis. Derives the geodesic structure from the Principle of Least Action via ODE training dynamics. Provides operational STP loss $\mathcal{L}_{\text{STP}} = 1 - \cos(h_t - h_r, h_r - h_s)$. Empirical claim: 16x data efficiency improvement on NL-RX-SYNTH. **Source for HL2, HL3.**

- **Multi-step Latent Forecasting in LLM Reasoning Trajectories via STP.** arXiv:2604.18464.
  <https://arxiv.org/abs/2604.18464>
  Empirical refinement of HL2: STP-shaped trajectories are smooth *curves*, not straight lines. Step-boundary STP achieves 168x improvement in multi-step latent prediction over frozen baselines. Establishes that local linearity (within window $\tau$) coexists with global curvature. **Refines HL2.**

- **GeoGNN: Geodesic Aggregation for Graph Neural Networks.** arXiv:2511.09042.
  <https://arxiv.org/abs/2511.09042>
  Names and characterizes "semantic drift" as deviation from the intrinsic semantic manifold under linear (Euclidean) operations. Implements log-exp mappings on the unit hypersphere $\mathbb{S}^{d_h-1}$ to preserve manifold structure during message passing. **Source for HL1, HL4.**

- **Geodesic Semantic Search (GSS).** arXiv:2602.23665v3.
  <https://arxiv.org/abs/2602.23665>
  Learned local Riemannian metrics on citation graphs. MetricGAT architecture jointly learns embeddings and node-specific metric tensors $\mathbf{G}_i = \mathbf{L}_i \mathbf{L}_i^\top + \epsilon \mathbf{I}_d$. Bridge Recovery Guarantee (Theorem 5) for retrieval across distant concepts. **Bears on HL1; substantially overlaps with HF5 (suturing) — relationship needs explicit working-out.**

- **Recursive Semantic Language Models (RSLM): From Geometric Theory to Experimental Validation.** ResearchGate publication 399875145, January 2026.
  <https://www.researchgate.net/publication/399875145>
  Geodesic Policy Networks for navigation in semantic space without intermediate token generation. Hybrid frozen-LLM + trainable policy network architecture. **Bears on HL1, HL2.**

### Operational Incompleteness

- **Rosko, M.** *Operational Incompleteness in Large Language Models.* arXiv:2511.21296.
  <https://arxiv.org/abs/2511.21296>
  Structural incompleteness bound: there exist true propositions about an LLM's knowledge that no finite token-observation sequence can decide. Defines $\Delta_0$ Heyting Arithmetic realizability structure. **Source for HB1.**

### Empirical Curvature Validation

- **Mabrok, M. et al.** *Curvature structure in transformer attention manifolds.* arXiv:2603.22301.
  <https://arxiv.org/abs/2603.22301>
  Empirical evidence relevant to attention-as-curvature claims. **Bears on HF2.**

## Independent Researcher Contributions

### LARQL Toolchain

- **Hay, C.** *Language-graph extraction, walking, and recompilation toolchain.*
  <https://github.com/chrishayuk/larql>
  Operationalizes the vindex decomposition (EXTRACT / WALK / INSERT / DELETE / PATCH / COMPILE). Provides text-level access to discrete graph corresponding to LLM weights. Substantially demonstrates HF1 (round-trip fidelity) for at least some LLMs. **Operational substrate for HF1, foundational for all experimental classes.**

### KV Cache and Residual Stream Experimental Program

- **Hay, C.** *KV Cache and Residual Stream — Part 1.*
  <https://www.youtube.com/watch?v=TYgCRPCAFhE>
  Detailed breakdown of KV cache structure and residual stream behavior under controlled experimental conditions.

- **Hay, C.** *KV Cache and Residual Stream — Part 2.*
  <https://www.youtube.com/watch?v=HJlWDSyDcD4>
  Continued analysis of context-as-input vs. parametric-information differential. Layer-wise residual injection experiments. Empirically supports HF3 (tripartite alignment) and HF4 (horizon disorientation).

- **Hay, C.** *LARQL Inference and Knowledge Insertion Demonstration.*
  <https://www.youtube.com/watch?v=8Ppw8254nLI>
  Demonstrates querying via LARQL, layer/feature representation as graph nodes and relations, and the Atlantis/Poseidon insertion experiment showing walk topology modification. **Substantially demonstrates HF1 and HF3.**

## Framework-Distinctive (Subject to Literature Verification)

The framework's distinctive contributions (HF4 three-zone topology, HF5 suturing, HF6 Turing catastrophe, HF7 logic-walk-measurement correspondence) are documented in [`framework/geocoherence-framework.md`](../framework/geocoherence-framework.md). Literature verification searches for these are tracked under Priority 5 of the experimental program.

## Adding Entries

When a new reference is added, also note:

1. Which hypothesis (HL1-HL4, HF1-HF7, HB1) it bears on.
2. Whether it provides theoretical grounding, empirical support, or independent replication.
3. Whether its findings replicate, contradict, or extend prior entries.
4. For framework-distinctive claims: whether it constitutes a precursor that would require the claim to be reframed as inherited rather than novel.
