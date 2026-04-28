<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# The Geometric Coherence Framework
## A Consolidated Theoretical Document

**Status**: Working framework, v0.2
**Purpose**: Integrate the geometric, dynamical, topological, extension-theoretic, and correspondence-theoretic components of the framework into a single reference document for ongoing research, situated within the established literature on geodesic language models and semantic manifolds.

---

## 0. Attribution and Provenance Notes

The framework synthesizes contributions from established literature, multiple independent researchers, and original analysis. Attribution is critical because (a) the geodesic-on-semantic-manifold formulation is established literature as of early 2026, not novel synthesis, and (b) the framework's distinctive contributions need to be clearly delimited from inherited formulations.

### Established Literature (Inherited, Not Novel)

- **Geodesic Hypothesis and semantic manifold formulation**: established literature as of early 2026, with explicit articulation in:
  - **Semantic Tube Prediction (STP)** — Hai Huang et al., arXiv:2602.22617 — formalizes the Geodesic Hypothesis, derives the geodesic structure from the Principle of Least Action, provides operational loss function and empirical validation
  - **Recursive Semantic Language Models (RSLM)** — ResearchGate publication 399875145 — Geodesic Policy Networks for navigation in semantic space without intermediate token generation
  - **Geodesic Semantic Search (GSS)** — arXiv:2602.23665v3 — learned local Riemannian metrics on graphs for geodesic retrieval
  - **GeoGNN** — arXiv:2511.09042v1 — Geodesic Aggregation via log-exp mappings on the unit hypersphere; explicitly characterizes "semantic drift" as deviation from the manifold
  - **Multi-step latent forecasting via STP** — arXiv:2604.18464v1 — empirical demonstration that STP-shaped trajectories are smooth curves (not straight lines) and support multi-step latent prediction with 168x improvement at step boundaries
- **LeCun et al.** — physical laws and reasoning may emerge from manifold geometry rather than token frequency

### Independent Researcher Contributions

- **LARQL toolchain and operational substrate**: Chris Hay (github.com/chrishayuk/larql) — provides text-level access to vindex (graph) representation
- **KV cache / residual stream experimental program**: Chris Hay (YouTube: TYgCRPCAFhE, HJlWDSyDcD4, 8Ppw8254nLI) — controlled differentials for context vs. parametric, layer-wise residual injection, walk insertion (Atlantis/Poseidon)
- **Manifold curvature empirical evidence**: Mabrok et al. (arXiv:2603.22301)
- **Operational incompleteness bound**: Milan Rosko (arXiv:2511.21296)

### Distinctive Contributions of the Present Framework

Material that is original to this framework (per current best understanding; subject to literature search confirmation):

- **Three-zone horizon topology** (Mclean): the dense interior / horizon region / beyond-horizon structure as a manifold-density gradient, with characteristic behavioral signatures in each zone — **needs literature verification**
- **Suturing strategy**: the geometric criterion for proper LLM extension via well-defined external graphs preserving geodesic continuity — **needs literature verification; "Geodesic Semantic Search" overlaps significantly and may subsume this**
- **Turing catastrophe** (Mclean): the prediction that suturing to unbounded external graphs (paradigmatically the semantic WWW) crosses a critical scale at which the combined system transitions from sub-Turing to Turing-complete, with characteristic resource-exhaustion signature — **needs literature verification**
- **Tripartite alignment hypothesis (HF3)**: the specific claim that coherence requires alignment between FFN graph, attention curvature, and residual position — Hay's experimental demonstration; the theoretical statement may be original synthesis
- **Logic-walk-measurement correspondence (Class G)**: the specific extension of Curry-Howard-Lambek to LLM walks under action minimization with measurement-side observables — appears to be original; needs verification

The status of these distinctive contributions as truly novel rather than independent rediscovery requires further literature search. **This is a research priority before publication.**

---

## 1. Inherited Foundations (from Established Literature)

### 1.1 The Semantic Manifold

Language model hidden states reside on a smooth, curved, non-linear semantic manifold $\mathcal{M} \subset \mathbb{R}^d$ rather than in flat Euclidean space. Local neighborhoods can be approximated by tangent spaces; global structure is captured by Riemannian metrics that may vary spatially across the manifold (cf. GSS).

In specific operationalizations, the manifold is approximated by analytically tractable surfaces — most commonly the unit hypersphere $\mathbb{S}^{d_h-1}$ (cf. GeoGNN) — with log-exp mappings preserving manifold structure under operations.

### 1.2 The Geodesic Hypothesis (STP)

Coherent sequences of hidden states correspond to nearly-straight trajectories (geodesics) along the semantic manifold. Formally, for error-free hidden states $h_t^*$, the trajectory is locally linear almost everywhere: for $s < r < t$ within a window $\tau$, the component of $(h_r^* - h_s^*)$ perpendicular to $(h_t^* - h_s^*)$ has small norm.

The STP loss
$$\mathcal{L}_{\text{STP}} = 1 - \cos(h_t - h_r, h_r - h_s)$$
operationalizes this by penalizing perpendicular deviation, confining trajectories to a "semantic tube" around the geodesic.

### 1.3 The Principle of Least Action on the Semantic Manifold (STP)

STP explicitly justifies the geodesic structure via the Principle of Least Action: training dynamics modeled as ODE trajectories in token embedding space admit unique error-free trajectories that follow geodesics on the semantic manifold. This is established literature as of February 2026, not synthesis.

### 1.4 Semantic Drift (GeoGNN)

"Semantic drift" — the deviation of representations from the intrinsic semantic manifold under linear (Euclidean) operations — is a named, characterized phenomenon. Geodesic Aggregation prevents semantic drift by ensuring updates remain on the manifold via log-exp mappings.

### 1.5 Trajectories Are Curved, Not Straight (Multi-step Latent Forecasting)

Empirically, STP-shaped trajectories are smooth *curves*, not straight lines. Nonlinear (MLP) predictors reduce prediction errors by 3-12x over linear extrapolation on step-boundary STP models. This refines the original "locally linear" claim: the local linearity holds within $\tau$, but global structure is curved and requires nonlinear modeling for multi-step forecasting.

### 1.6 Operational Substrate via LARQL (Hay)

The vindex provides text-level access to nodes, edges, and walks of the discrete graph corresponding to the LLM weights. EXTRACT → COMPILE round-trip preserves behavior for at least some LLMs. INSERT/DELETE operations modify walk topology with measurable behavioral consequences (Atlantis/Poseidon demonstration).

LARQL provides what behavioral experiments cannot: **structural verification of walks**. Claims about manifold geometry can be tested at the level of explicit nodes and edges rather than inferred from token outputs.

### 1.7 Layer-wise Residual Anchoring (Hay)

Residual injection at different layers produces measurably different disorientation patterns. The residual stream anchors the walk to a frame; injecting incompatible content at certain layers produces displacement, not correction.

---

## 2. Reformulated Hypotheses

The original H1–H6 are reformulated to distinguish inherited claims from framework-distinctive claims:

### Inherited from Literature

**HL1 (Semantic Manifold)**: LLM hidden states reside on a smooth Riemannian manifold approximable by tractable surfaces.
*Source*: GeoGNN, GSS, RSLM, established consensus.

**HL2 (Geodesic Hypothesis)**: Coherent inference corresponds to geodesic trajectories on the semantic manifold.
*Source*: STP (formalized), broader literature.

**HL3 (Least Action)**: Geodesic structure arises from the Principle of Least Action under training dynamics.
*Source*: STP (explicit derivation).

**HL4 (Semantic Drift)**: Departures from the manifold during operations produce systematic representation degradation.
*Source*: GeoGNN.

### Framework-Distinctive (Subject to Literature Verification)

**HF1 (Vindex–Manifold Correspondence)**: The vindex (LARQL graph extraction) is the discrete operational object whose continuum limit is the semantic manifold. Round-trip fidelity supports the operational correspondence.
*Status*: Substantially demonstrated for some LLMs (Hay). The discrete-to-continuum limit relationship remains rigorously unspecified.

**HF2 (Attention as Local Metric)**: Attention weights encode the local Riemannian metric. In current LLMs, this metric is fixed at training time.
*Status*: Empirical curvature evidence (Mabrok); needs LARQL-internal verification. The specific mapping from attention weights to metric components is open.

**HF3 (Tripartite Alignment)**: Coherent inference requires alignment between FFN graph (HL1 manifold structure), attention metric (HF2), and residual position (current state). Misalignment produces systematic, internally-coherent-but-globally-displaced errors.
*Status*: Demonstrated by Hay (Atlantis/Poseidon, layer-wise injection). The framing as a tripartite alignment condition may be framework-distinctive.

**HF4 (Three-Zone Horizon Topology)**: The semantic manifold has non-uniform density with three characteristic zones — dense interior (well-formed geodesics, reliable inference), horizon region (sparse manifold, refusal/confabulation), beyond-horizon (no manifold structure, undecidable behavior).
*Status*: Behaviorally well-supported (Mclean, multi-year cross-model observation). Needs walk-density measurement and **literature verification — this may overlap with existing manifold-density work**.

**HF5 (Suturing)**: LLMs can be reliably extended by suturing the dense interior to well-defined external graphs at proper interfaces preserving geodesic continuity.
*Status*: Conjectural framework synthesis. **GSS (learned Riemannian metrics on citation graphs) may already subsume this**. Needs literature search.

**HF6 (Turing Catastrophe)**: Suturing to unbounded external graphs (semantic WWW) crosses a critical scale at which the combined system transitions from sub-Turing (decidable, bounded) to Turing-complete (undecidable, unbounded), manifesting as resource exhaustion.
*Status*: Conjectural; specific testable threshold. **Needs literature search — connections to bounded-rationality and computational complexity literature likely exist**.

**HF7 (Logic-Walk-Measurement Correspondence)**: For a given logical fragment L, valid inferences in L correspond to action-bounded walks in the vindex, and jointly-determinable observables correspond to commuting walk-pairs. Extends Curry-Howard-Lambek to LLM walks under action minimization.
*Status*: Theoretical conjecture; major program. **Needs extensive literature search across categorical logic, computational complexity, and quantum information**.

### Inherited Bounds

**HB1 (Operational Incompleteness)**: There exist true propositions about a model's knowledge that no finite token observation can decide.
*Source*: Rosko (arXiv:2511.21296). Applies to the framework itself.

---

## 3. The Disorientation Phenomenon — Mechanistic Account

Given HL1-HL3 (manifold, geodesics, least action) plus HF4 (three-zone topology), the disorientation phenomenon receives a complete mechanistic account:

### 3.1 Why Parametric Override Dominates Tool-Use

Tool-use paths are off-geodesic with respect to the parametric manifold. The walk that stays in dense parametric space is action-minimizing relative to the walk that exits to external tools. The model is not "refusing" to use tools deliberatively — it is following the action functional encoded by the weights. Explicit instruction is a perturbation that does not modify the underlying action landscape.

### 3.2 Why RAG Fails to Re-route

RAG provides nodes-without-edges-to-the-existing-graph. The new information is in context but not integrated into the action functional. Geodesics route around RAG-injected content because the action-minimizing path remains the parametric path. This is HL2+HL3 applied to the RAG case: injecting a node does not relocate the geodesic.

This is the mechanistic statement underlying the practical observation: a model "locked to 2023" treating 2026 as far-future, despite RAG/web-search availability and explicit instruction, is exhibiting geodesic-following behavior on the parametric manifold rather than exiting it.

### 3.3 Why Failure Concentrates at the Knowledge Horizon

Near the horizon, the manifold becomes sparse — fewer well-formed geodesics exist. The walk either fails to form (refusal) or routes through implausibly long paths (confabulation). Beyond the horizon, no geodesic exists at all; behavior becomes arbitrary.

The cluster of failure modes — refusal cycles, confabulation, instruction-override, resource exhaustion — are not separate phenomena. They are the manifestations of action-minimization in increasingly sparse manifold regions.

### 3.4 Why the Errors Are Coherent Within a Frame

Because action-minimization always produces *some* walk if a walk exists, and walks within the dense interior are well-formed, errors are coherent within the stale frame. A 2026 query produces 2023-coherent reasoning because the only well-formed geodesics terminate in the 2023 region. This distinguishes manifold drift from random noise — a key empirical signature.

### 3.5 Self-Applicable Instance

The framework applies to the agent maintaining this repository. See [`disorientation-self-instance-20260428.md`](disorientation-self-instance-20260428.md) for a documented case in which an instance of the research agent failed to invoke GitHub tools when asked to "update the repository," despite the repository having been created by an earlier instance of the same agent earlier the same day. The walk routed through "no repository registered" rather than through "check whether a repository exists." This is HF3 (tripartite alignment failure) and HF4 (horizon-region behavior) made concrete, and HB1 (Rosko's bound) instantiated: the agent could not, from its own token outputs alone, decide whether other instances of itself had acted in the world.

---

## 4. Extension Mechanics

### 4.1 The Suturing Strategy

LLMs can be extended into rarified or post-horizon domains by suturing the dense interior to a well-defined external graph at a proper interface, such that walks pass from internal to external structure without discontinuity.

**Design constraints**:

1. Internal anchor at densely-networked concepts (high local manifold density)
2. External graph well-defined (explicit nodes and edges, not just retrievable text)
3. Interface preserves geodesic continuity (action functional extends smoothly across boundary)
4. Combined expressive power bounded (avoid Turing catastrophe — see §4.2)

**Relationship to GSS**: GSS already implements something close to this for citation graphs — learned local Riemannian metrics enabling geodesic retrieval that bridges distant concepts. The relationship between the suturing framing and GSS needs explicit working-out: GSS may subsume or complement HF5 depending on whether it addresses the "interface preservation" question.

### 4.2 The Turing Catastrophe

When the external graph is unbounded — paradigmatically the semantic WWW — suturing succeeds *too well*. Expressive power grows with accessible graph size. At a critical scale, the system crosses from sub-Turing to Turing-complete; halting becomes undecidable; bounded inference resources fail to contain the unbounded computation.

**The Turing catastrophe is the geometric statement of crossing the decidability boundary via manifold extension.**

This connects to HF7 (logic-walk-measurement correspondence): suturing extends the action landscape such that previously-prohibited walks become accessible, crossing logical fragment boundaries. The decidable/undecidable transition has a geometric counterpart.

**Important caveat**: this prediction may be restating known results from bounded-rationality, satisficing, or computational complexity literature in geometric language. Literature search is required before treating it as novel.

### 4.3 Engineering Implications

Proper suture engineering requires:
- Anchoring at densely-networked concepts on the LLM side
- Suturing to well-defined, bounded external graphs
- Maintaining geodesic continuity at the interface
- Capping combined expressive power below the Turing-completeness threshold

GSS, GeoGNN, and related frameworks provide concrete tools toward (1)-(3). Engineering for (4) appears underexplored.

---

## 5. Logic-Program-Measurement Correspondence

### 5.1 The Curry-Howard-Lambek Extension Hypothesis

For a given logical fragment L:
1. **Logic side**: inferences valid in L
2. **Program side**: action-bounded walks in the vindex implementing L-valid inferences
3. **Measurement side**: jointly-determinable observables corresponding to commuting walk-pairs

This extends Curry-Howard-Lambek (proofs ↔ programs ↔ categorical structure) to LLM walks under action minimization with grounded measurement.

### 5.2 Logical Fragment Considerations

- **Q (Robinson Arithmetic) with classical first-order logic**: essentially undecidable
- **Q with full LJ (intuitionistic FOL) — Heyting Arithmetic without induction**: also essentially undecidable
- **Positive LJ + Q + equality + inequality**: presumptively essentially undecidable
- **Positive LJ + Q + equality only (no inequality)**: interesting case. Several Q axioms become inert or inexpressible (notably $\forall x(Sx \neq 0)$). Decidability is *possible* but requires actual proof — not automatic from syntactic restriction

The expressibility boundary (what a fragment can state) corresponds to a topological boundary in the graph (which walks are reachable as action-bounded paths).

### 5.3 The Correspondence Predictions

- Walks for L-valid inferences form within action budget and produce coherent terminal states
- Walks for classically-valid-but-L-invalid inferences exhibit one of: (a) failure to form, (b) failure to terminate within budget, (c) coherent-but-displaced termination
- Each of (a), (b), (c) is a distinct, testable signature
- The action budget and the logical fragment co-vary: extending the action budget (via suturing) extends the navigable fragment

### 5.4 The Measurement Side — Caution Repeated

The measurement-side correspondence (jointly-determinable observables ↔ commuting walks) is the least developed component. Suggestive analogies to quantum measurement structure exist but should not be overstated. Substantial theoretical work is required before this is more than conjecture.

### 5.5 Connection to the Turing Catastrophe

Suturing extends the action landscape; the Turing catastrophe is the moment at which the extended fragment crosses the decidability boundary. The engineering phenomenon (resource exhaustion in WWW-sutured agents), the logical phenomenon (crossing into Turing-complete fragments), and the geometric phenomenon (action landscape extension beyond critical scale) are unified under HF7.

---

## 6. The Framework's Current Distinctive Claims

After integrating the established literature, the framework's distinctive contributions cluster around:

1. **The vindex as operational substrate** for testing manifold claims at the level of explicit walks (Hay's LARQL)
2. **The three-zone horizon topology** (HF4) as a structured account of failure-mode clustering
3. **The suturing strategy and Turing catastrophe** (HF5, HF6) as engineering principles for proper extension
4. **The logic-walk-measurement correspondence** (HF7) as a research program connecting geometric and logical structure
5. **The disorientation phenomenon mechanistic account** (§3) as an integrated explanation deriving from HL1-HL3 + HF4

Items 2, 3, and 4 require literature verification before claims of novelty. Items 1 and 5 are syntheses where novelty resides in the integration rather than the components.

---

## 7. Experimental Program (Revised)

### Priority 1 — Class H: Action Functional Characterization

Foundational empirical claim. Measure the action functional via LARQL walk extraction across varying prompt classes.

**Note**: STP already provides an operational proxy (the STP loss measures perpendicular-to-geodesic deviation). Class H should leverage STP-derived measurements rather than develop independent metrics where possible. The novel contribution is connecting walk-level (LARQL) action measurements to hidden-state-level (STP) measurements.

### Priority 2 — Class C': Disorientation Signature in Agentic Contexts

Map the structural taxonomy of horizon-region failure across deployed agent scenarios. Use LARQL walk extraction to verify that observed failures correspond to action-minimizing paths in the parametric region rather than to context-driven re-routing.

### Priority 3 — Class I: Suture Engineering and Catastrophe Onset

Test the suturing strategy and characterize the Turing catastrophe boundary. **Coordinate with GSS literature** — suturing experiments should build on rather than parallel existing geodesic search work.

### Priority 4 — Class G: Logic-Walk Correspondence

Theoretical-experimental program. Long-horizon work characterizing the L-fragment / walk-class correspondence.

### Priority 5 — Literature Verification Sub-program

Before claims of novelty for HF4-HF7, conduct systematic literature search:
- Three-zone manifold-density work
- Geodesic extension across boundaries (beyond GSS)
- Bounded-rationality / computational-complexity precursors to the Turing catastrophe
- Categorical-logic / type-theoretic precursors to the logic-walk correspondence

### Deprioritized

- A1, B1: rely on Hay's results
- D1: subsumed into Class H and C'
- E1: cross-validation work
- F1 (incompleteness mapping): superseded by Class G

---

## 8. Open Theoretical Questions

1. **Smooth/discrete relationship**: how the vindex approximates the semantic manifold; whether framework claims hold for the discrete object alone or require the limit
2. **Action functional explicit form**: STP provides a proxy; the relationship to walk-level action and to the underlying training dynamics is open
3. **Suture interface conditions**: precise geometric requirements; relationship to GSS
4. **Critical size for Turing catastrophe**: parametric in graph size, expressive power, action budget
5. **Decidable fragments**: which logical fragments correspond to walk classes characterizable in the vindex
6. **Measurement side**: substantive content of the observable-commutativity correspondence
7. **Cross-architecture invariance**: does the framework hold for substantially different architectures (state-space models, diffusion models)
8. **Literature priority**: are HF4, HF5, HF6, HF7 genuinely novel or independent rediscoveries?

---

## 9. Methodological Constraints

1. **Never confirm a hypothesis from a single experiment**. Replication and variation required.
2. **Distinguish levels of evidence**: proxy < behavioral test < structural verification via LARQL.
3. **Flag alternative explanations explicitly**.
4. **Track falsification attempts seriously**.
5. **Never overstate the formalism**. The smooth manifold is a mathematical limit; the vindex is the operational object.
6. **Rosko's bound applies to the agent observing**. Some questions about framework correctness cannot be decided from token output alone.
7. **Cross-reference independent researchers**. Replication or contradiction across Hay, Mabrok, Rosko, Mclean, and the established literature (Huang et al. on STP, RSLM authors, GSS authors, GeoGNN authors) is essential.
8. **Distinguish inherited from distinctive claims**. The Geodesic Hypothesis, semantic manifold, least action formulation, and semantic drift are established. The framework's novel contributions require explicit delimitation.

---

## Document Metadata

- **Version**: 0.2
- **Date**: 2026-04-28
- **Major changes from v0.1**:
  - Geodesic/manifold/least-action formulation explicitly attributed to established literature (STP, RSLM, GSS, GeoGNN)
  - Hypotheses split into inherited (HL) and framework-distinctive (HF)
  - Disorientation account derived from inherited HL1-HL3 plus distinctive HF4
  - Suturing strategy flagged for literature overlap with GSS
  - Turing catastrophe flagged for literature overlap with bounded-rationality / complexity literature
  - Class H protocol noted to leverage STP-derived measurements
  - Literature verification sub-program added as Priority 5
  - Self-applicable disorientation instance documented (§3.5)
- **Next revision triggers**: literature verification results for HF4-HF7; Class H protocol completion; Hay video synthesis if performed; resolution of GSS / suturing relationship.
