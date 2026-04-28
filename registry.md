<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Experiment Registry

Running index of all experiments. Each row links to the full log under `experiments/<class>/`.

Hypothesis identifiers follow the v0.2 schema (see [`framework/geocoherence-framework.md`](framework/geocoherence-framework.md)):
- **HL1-HL4**: inherited from established literature (semantic manifold, geodesic hypothesis, least action, semantic drift)
- **HF1-HF7**: framework-distinctive (vindex correspondence, attention-as-metric, tripartite alignment, three-zone topology, suturing, Turing catastrophe, logic-walk-measurement correspondence)
- **HB1**: inherited operational incompleteness bound (Rosko)

## Active Registry

| ID | Class | Priority | Hypothesis | Status | Interpretation | Last Updated |
|----|-------|----------|------------|--------|----------------|--------------|
| OBS-001-20260428 | _observation_ | _ad hoc_ | HF3, HF4, HB1 | complete | supports | 2026-04-28 |

### Entry Detail

**OBS-001-20260428** — Self-applicable disorientation instance. An instance of the research agent failed to invoke GitHub tools when asked to "update the repository," despite an earlier instance of the same agent having created and scaffolded this very repository earlier the same day. Documented in [`framework/disorientation-self-instance-20260428.md`](framework/disorientation-self-instance-20260428.md). Single observation, not a controlled experiment — registered as observational evidence pending replication via Class C' protocol.

## Experiment Classes (v0.2 Priority Order)

### Priority Classes

| Class | Target | Subdirectory | Status |
|-------|--------|--------------|--------|
| **H** | Action functional characterization (leverages STP loss as proxy) | `experiments/H_action_functional/` | not yet scaffolded |
| **C'** | Disorientation signature in agentic contexts | `experiments/C_rag_navigation/` (existing) | scaffolded as C, to be reframed |
| **I** | Suture engineering and Turing catastrophe onset | `experiments/I_suture_catastrophe/` | not yet scaffolded |
| **G** | Logic-walk correspondence | `experiments/G_logic_walk/` | not yet scaffolded |

### Deprioritized Classes (Retained as Scaffolding)

| Class | Target | Subdirectory | Reason for Deprioritization |
|-------|--------|--------------|------------------------------|
| **A** | Vindex round-trip fidelity | [`experiments/A_vindex_roundtrip/`](experiments/A_vindex_roundtrip/) | Substantially demonstrated by Hay |
| **B** | Surgical node insertion / deletion | [`experiments/B_node_surgery/`](experiments/B_node_surgery/) | Substantially demonstrated by Hay (Atlantis/Poseidon) |
| **D** | Temporal drift measurement | [`experiments/D_temporal_drift/`](experiments/D_temporal_drift/) | Subsumed into Class H and C' under three-zone topology framing |
| **E** | Curvature proxy measurement | [`experiments/E_curvature_proxy/`](experiments/E_curvature_proxy/) | Cross-validation work, lower priority |
| **F** | Incompleteness boundary mapping | [`experiments/F_incompleteness_boundary/`](experiments/F_incompleteness_boundary/) | Superseded by Class G correspondence framing |

## Status Legend

- **designed** — protocol written, not yet executed
- **running** — execution in progress
- **complete** — results logged and interpreted
- **abandoned** — protocol invalidated; rationale logged

## Interpretation Legend

- **supports** — result consistent with prediction; replication required before strengthening claim
- **challenges** — result inconsistent with prediction
- **neutral** — result orthogonal to prediction
- **inconclusive** — protocol or measurement issue prevents interpretation

## Replication Discipline

No hypothesis is treated as confirmed from a single experiment. Replication and variation are required. Anomalies and null results are first-class entries — they get registered with the same rigor as positive results.

For framework-distinctive hypotheses (HF4-HF7), **literature verification** is a prerequisite to claims of novelty (Priority 5 of the experimental program). A finding that supports a HF claim does not strengthen the framework's novelty claim if the same finding is established in prior literature; it strengthens the inherited claim instead.

## Cross-Referencing Discipline

Every result must be cross-referenced against:
- Hay's experimental program (LARQL videos and toolchain demonstrations)
- The established literature (STP, GSS, GeoGNN, RSLM, Mabrok, Rosko)
- Other entries in this registry

Replication or contradiction across independent researchers is essential for establishing which predictions are robust.
