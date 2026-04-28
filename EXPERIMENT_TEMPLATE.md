<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Experiment Template

Copy this file into the appropriate `experiments/<class>/` subdirectory and rename it `<class>-<number>-<YYYYMMDD>.md`.

---

## EXPERIMENT ID
`<CLASS>-<NUMBER>-<YYYYMMDD>` (e.g. `A-001-20260428`)

## Status
`designed` | `running` | `complete` | `abandoned`

## Hypothesis Targeted
Which of H1–H6 (or derived hypothesis) is being tested. State precisely what would confirm vs. falsify it.

## Experimental Conditions
- **Baseline:** behavior of unmodified model on the test task.
- **Intervention:** what changes (vindex patch, RAG injection, prompt modification, etc.).
- **Control:** what is held constant to isolate the variable of interest.

## Measurement
Operational definition. Prefer quantitative metrics:
- Geometric metrics (manifold-distance proxies, curvature proxies, walk divergence).
- Behavioral metrics (token-match rate, perplexity delta, reasoning-chain coherence).
- Failure-mode classification (random vs. systematic displaced-coherence).

## Prediction
Precise prediction the framework makes. State:
- What a positive result looks like.
- What a null result looks like.
- What would falsify the hypothesis.

## Toolchain
LARQL operations used (EXTRACT, WALK, INSERT, DELETE, PATCH, COMPILE), model APIs, datasets, evaluation harness.

## Result
Quantitative outcome. Tables, plots, references to artifacts in this directory.

## Interpretation
`supports` | `challenges` | `neutral` | `inconclusive` — and why.

State at least one **alternative interpretation** that does not require the full GCF framework.

## Anomalies
Unexpected observations, including null results and instability patterns.

## Replication Status
- Independent replications attempted: N
- Cross-references to prior work (Hay / Rosko / Mabrok / others).

## Next Steps
Follow-up experiments, replications, or refinements.

## Incompleteness Note
If applicable: which aspects of this result fall under H6's operational-incompleteness bound (i.e., cannot be decided from finite token-observation alone).
