<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Convergence: CategoricalReasoner ↔ LARQL

Both `CategoricalReasoner` (`reasoning/`) and `larql-to-sparql` (`tools/larql/`) are converging toward the same mathematical objects from different directions. This document makes that convergence explicit.

## What a Vindex Is, Categorically

A LARQL vindex is a **directed weighted graph** extracted from transformer weights. In category-theoretical terms:

| Vindex component | Category-theoretical interpretation |
|-----------------|--------------------------------------|
| Token embeddings | Objects in a category **V** |
| Attention weight matrix (layer *l*) | A morphism family **Hom(V, V)** encoding local metric distortion |
| FFN gate/down matrices | A functor **F_l : V → V** (feature routing per layer) |
| Residual stream | An identity morphism **id_V** (positional state accumulator) |
| Layer stack | A natural transformation between successive functors **F_l ⇒ F_{l+1}** |
| Full model | A **monoidal category** where tensor product = attention ⊗ FFN composition |

This maps exactly to CategoricalReasoner's formalism: CategoricalReasoner models formal logics (LM, LK, LJ, LDJ, linear logic) as categories, defines morphisms between them, and verifies logical entailment as functor existence. A trained LLM **is** a large monoidal category of this type, and a vindex is its explicit representation.

## Shared Operations

| CategoricalReasoner concept | LQL equivalent |
|-----------------------------|---------------|
| Morphism composition | `WALK` traversal across attention edges |
| Functor application | `INFER` (forward pass through FFN graph) |
| Natural transformation | `DIFF` between two vindexes (version comparison) |
| Object identity | `DESCRIBE NODE` (inspect embedding coordinates) |
| Limit / colimit | `SELECT ... GROUP BY` aggregation over node neighborhoods |
| Subobject | `INSERT` / `DELETE` (patch overlay = subobject of the base vindex) |
| Proof search | `TRACE` (reasoning path tracing through the geodesic graph) |

## Semantic Web Convergence

Both projects consume semantic web graphs:

- **CategoricalReasoner**: ingests RDF/OWL graphs via Apache Jena and Oxigraph, executes SPARQL queries against external endpoints, emits categorical structures as RDF output
- **LARQL**: can ingest graph databases directly (`larql extract-index --graph domain.ttl`), uses the same RDF triple representation for knowledge graph vindexes

**Oxigraph** (Rust SPARQL/RDF engine) is the shared execution target:
- Replaces Jena's SPARQL execution in CategoricalReasoner's Rust migration path
- Provides the SPARQL synthesis leg in the LARQL pipeline
- All three tools — LARQL, Oxigraph, CategoricalReasoner — converge on Turtle/N-Triples as the interchange format

## Technology Convergence Path

CategoricalReasoner's Java implementations are the **reference specifications**. Migration to Rust proceeds as each algorithm is needed in the LARQL execution pipeline:

| Algorithm | CategoricalReasoner (Java/Maven) | Migration target (Rust/Cargo) |
|-----------|----------------------------------|-------------------------------|
| Morphism composition | `src/main/java/.../Morphism.java` | `larql-core` graph algorithms |
| Logic modeling (LM, LK, LJ) | `src/main/java/.../Logic*.java` | `larql-inference` trace module |
| SPARQL execution | Apache Jena | Oxigraph (`sparql_client` feature) |
| Semantic validation | KeY theorem prover + OWL-API | `larql-vindex` invariant checks |
| RDF output | Java RDF4J | `model-compute` or `larql-vindex` |

## The Curry-Howard Dimension

CategoricalReasoner's AGENTS.md describes its file system as a **proof tree**: open branches (docs, CC-BY-SA) transform to closed branches (code, AGPL) via the CC-BY-SA → GPL morphism.

This is the same morphism that the GeodesicLangModel dual-license scheme uses, and it is itself an instance of the Curry-Howard correspondence:

- Open branch (proposition) = undecided hypothesis
- Closed branch (proof) = compiled executable
- The vindex = the proof object (a completed derivation of the model's knowledge graph)
- `COMPILE` = proof normalization (reducing the derivation to normal form)
- `INSERT/DELETE` patches = proof edits (axiom additions/removals)

H6 (Operational Incompleteness) is the statement that no finite token-observation sequence can decide all propositions about an LLM's knowledge — i.e., the proof system is incomplete in the Gödelian sense.
