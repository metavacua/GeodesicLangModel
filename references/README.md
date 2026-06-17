<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# References

Maintained bibliography for the Geometric Coherence Framework research program.

## Primary toolchain

- **LARQL** — Hay, C. *Language-graph extraction, walking, and recompilation toolchain.*
  <https://github.com/chrishayuk/larql>
  Operationalizes the vindex decomposition (EXTRACT / WALK / INSERT / DELETE / PATCH / COMPILE).

## Theoretical foundations

- **Rosko, M.** *Operational Incompleteness in Large Language Models.* arXiv:2511.21296.
  <https://arxiv.org/abs/2511.21296>
  Provides the structural incompleteness bound (H6). Defines the Δ₀ Heyting Arithmetic
  realizability structure relevant to Σ⁰₁ vs. Π⁰₂ proposition classes.

## Empirical validation

- **Mabrok, M. et al.** *Curvature structure in transformer attention manifolds.* arXiv:2603.22301.
  <https://arxiv.org/abs/2603.22301>
  Empirical evidence relevant to H2 (attention as curvature encoding).

## Quantum metalanguages and substructural logic

- **Zizzi, P.** *Basic Logic and Quantum Entanglement.* arXiv:quant-ph/0611119.
  Open Systems & Information Dynamics, Vol. 14, No. 1 (2007).
  <https://arxiv.org/abs/quant-ph/0611119>
  Proves the structural equivalence: no-contraction ≡ no-cloning; no-weakening ≡ no-erasure in
  Basic logic. Establishes that the absence of contraction and weakening in substructural logic
  is the logical enforcement of quantum information's no-go theorems.
  Theoretical grounding for H6 (structural obstructions to classical fixed points) and for
  CategoricalReasoner's LM/LK/LJ morphism structure.

- **Zizzi, P.** *Turning the Liar paradox into a metatheorem of Basic logic.* arXiv:quant-ph/0701171 (2007).
  <https://arxiv.org/abs/quant-ph/0701171>
  Introduces entanglement (@) as a new non-idempotent connective in Basic logic; shows that
  self-referential sentences (the Liar) are metatheorems, not paradoxes, in the resulting
  quantum metalanguage. T-schema compliance is maintained while self-reference is admitted.
  Theoretical grounding for H6: the autoresearch loop's non-convergence (babelian reading)
  and paraconsistent convergence (non-babelian reading) are both metatheorems of Basic logic.

- **Zizzi, P.** *From Quantum Metalanguage to the Logic of Qubits.* arXiv:1003.5976 (2010, PhD thesis, 138 pp).
  <https://arxiv.org/abs/1003.5976>
  Full quantum metalanguage framework; quantum superposition as a logical connective;
  develops the logic of qubits as a deductive calculus for quantum information.
  Theoretical grounding for H6 (Π⁰₂ undecidability in the quantum metalanguage sense).

- **Girard, J.-Y.** *Linear Logic.*
  Theoretical Computer Science, 50(1):1–102 (1987).
  Foundational paper removing weakening and contraction from classical logic, yielding the
  structural basis that Zizzi connects to quantum no-go theorems. Linear logic's connectives
  (⊗, ⊸, !, ?) correspond to the controlled resource use in LQL INSERT/DELETE operations.
  Theoretical grounding for CategoricalReasoner morphisms (LM/LK/LJ) and LQL INFER semantics.

## Adding entries

When a new reference is added, also note:
1. Which hypothesis (H1–H6) it bears on.
2. Whether it provides theoretical grounding, empirical support, or independent replication.
3. Whether its findings replicate, contradict, or extend prior entries.
