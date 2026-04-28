<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Experiment Template

Copy this file into the appropriate `experiments/<class>/` subdirectory and rename it `<class>-<number>-<YYYYMMDD>.md`.

---

## EXPERIMENT ID
`<CLASS>-<NUMBER>-<YYYYMMDD>` (e.g. `H-001-20260428`)

## Status
`designed` | `running` | `complete` | `abandoned`

## Hypothesis Targeted

State which of HL1-HL4, HF1-HF7, or HB1 (or a derived hypothesis) is being tested. State precisely what would confirm vs. falsify it.

**Inherited (HL) vs. Framework-Distinctive (HF)**: explicitly classify. If HL, the experiment validates the inherited claim against the LARQL operational substrate or specific model. If HF, the experiment tests a claim that is candidate-novel and subject to literature verification.

## Literature Precursor Check

For HF-class hypotheses: has a systematic literature search been performed for prior work on this claim? Cite any precursors. If the claim is found in prior literature, reframe the experiment as testing the inherited form rather than asserting novelty.

## Experimental Conditions

- **Baseline:** behavior of unmodified model on the test task.
- **Intervention:** what changes (vindex patch, RAG injection, prompt modification, suturing operation, etc.).
- **Control:** what is held constant to isolate the variable of interest.

## Measurement

Operational definition. Prefer quantitative metrics:

- **Geometric/topological metrics**: walk length and divergence (LARQL), STP loss (perpendicular-to-geodesic deviation), curvature proxies, manifold-distance measures.
- **Behavioral metrics**: token-match rate, perplexity delta, reasoning-chain coherence.
- **Failure-mode classification**: random vs. systematic displaced-coherence; refusal vs. confabulation vs. instruction-override vs. resource exhaustion.
- **Cross-level metrics**: connecting hidden-state-level (STP) measurements to walk-level (LARQL) measurements.

## Prediction

Precise prediction the framework makes. State:

- What a positive result looks like.
- What a null result looks like.
- What would falsify the hypothesis.
- For HF claims: what would distinguish a positive result from a result already established in inherited literature.

## Toolchain

LARQL operations used (EXTRACT, WALK, INSERT, DELETE, PATCH, COMPILE), STP-derived measurements if applicable, model APIs, datasets, evaluation harness.

## Result

Quantitative outcome. Tables, plots, references to artifacts in this directory.

## Interpretation

`supports` | `challenges` | `neutral` | `inconclusive` — and why.

State at least one **alternative interpretation** that does not require the framework. For HF claims: state whether the result, if positive, would still be explainable under the inherited HL claims alone (without requiring the HF extension).

## Anomalies

Unexpected observations, including null results, instability patterns, and any indication of self-applicable disorientation in the agent running the experiment.

## Replication Status

- Independent replications attempted: N
- Cross-references to prior work: Hay (LARQL/videos), STP, GSS, GeoGNN, RSLM, Mabrok, Rosko, other registry entries.

## Next Steps

Follow-up experiments, replications, refinements, or deprioritization.

## Incompleteness Note

If applicable: which aspects of this result fall under HB1's operational-incompleteness bound (i.e., cannot be decided from finite token-observation alone). Note especially any cases where the experiment relies on agent self-report — agent self-report is subject to the bound and requires external state verification.
