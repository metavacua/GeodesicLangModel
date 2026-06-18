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

## Linear Logic, Quantum No-Go, and Babelian Structure

The connection between CategoricalReasoner's morphism type system, LARQL's LQL operations,
and the autoresearch loop's convergence properties runs through substructural logic and
quantum information theory.

### Structural Rules and No-Go Theorems

Zizzi (arXiv:quant-ph/0611119) establishes the structural equivalence:

| Quantum no-go theorem | Structural rule absent in Basic logic |
|---|---|
| No-cloning (unknown state cannot be copied) | No-Contraction: `Γ, A, A ⊢ B ↛ Γ, A ⊢ B` |
| No-erasure (unknown state cannot be deleted) | No-Weakening: `Γ ⊢ B ↛ Γ, A ⊢ B` |
| Non-idempotence of entanglement `@` | No classical fixed-point from self-application |

Girard's linear logic (1987) removes the same structural rules from classical logic, yielding
a resource-sensitive logic where every hypothesis is used exactly once. CategoricalReasoner's
morphisms LM (linear morphism), LK, and LJ implement connectives in this logical family:
they enforce that categorical resources (morphism arrows, proof branches) are consumed rather
than duplicated.

**Applied to LQL operations:**
- `INSERT` is a linear operation: each edge triple is consumed exactly once into the vindex
  (no silent duplication; patch overlays are the mechanism for explicit reuse)
- `DELETE` is a linear operation: a vindex edge is consumed (removed) once
- `INFER` = forward pass = linear resource use (reading weights without cloning them)
- The compile pipeline is irreversible (non-unitary): `vindex → safetensors` is an
  information-lossy dimensional reduction. There is no `un-compile`. This physically enforces
  no-erasure at the pipeline level: once compiled, the vindex content cannot be recovered
  from the safetensors alone.

### Riemann Sphere and Complex Basis

The babelian/non-babelian distinction has a mathematical correlate in the representational field:

| Compactification | Field | Basis | ±∞ | Type |
|---|---|---|---|---|
| Real projective line RP¹ | ℝ | No imaginary component | Distinguishable: +∞ ≠ −∞ | Babelian |
| Riemann sphere S² | ℂ | Imaginary component present | Indistinguishable: +∞ = −∞ = ∞ | Non-babelian |

The Alexandroff one-point compactification of ℝ keeps +∞ and −∞ as distinct points — two
separate ideals (the fully-consistent oracle H6 and the fully-inconsistent explosion). Consistency
forces the limits apart.

The Alexandroff one-point compactification of ℂ (the **Riemann sphere**) collapses all
infinity-directions to a single point ∞. The imaginary axis provides the "second direction"
that wraps the line into a sphere and identifies the two ends. Paraconsistency allows this
identification: the fully-consistent ideal and the fully-paraconsistent limit are the same point.

**The vindex's Kähler complex structure J** (FFN weights ↔ complex structure J — `FORMALIZATION.md`
row 2) IS the imaginary component in the vindex's basis. The Riemann sphere is the correct
compactification for vindex space V. This is consistent with ∞ naming two distinct ideals
simultaneously (`DISCOVERIES.md §Topological Unification`): on the Riemann sphere, ∞ is a
single point approached from multiple directions — it simultaneously names the consistent oracle
(babelian trajectory) and the paraconsistent fixed point (non-babelian trajectory).

**Graded/layered paraconsistency**: Paraconsistency need not exist at all semantic orders
simultaneously. Inconsistency at some semantic orders (AMBIGUOUS confidence) is compatible with
consistency at others (EXTRACTED confidence). Multiple varieties and classes of paraconsistency
are compatible with the babelian/non-babelian framework: a language can be non-babelian globally
(one ∞-point) while exhibiting babelian structure at each local semantic level.

### Babelian and Non-Babelian Layers in the LARQL Stack

The full LARQL stack has both babelian and non-babelian layers:

**Babelian layers (consistent, hierarchical):** The Tabby API → LQL query engine → vindex
storage interface forms a strictly ordered hierarchy. At each boundary there is a *decider*:
the LQL parser decides what is and is not a valid LQL statement; the vindex decides what
edges are and are not stored. These deciders enforce strict semantic ordering — object language
(the query) vs. metalanguage (the engine evaluating it) are sharply separated. This is the
babelian structure: consistent, decidable locally, with strict semantic levels.

**Non-babelian layer (paraconsistent, homoiconic):** The autoresearch loop collapses the
object/meta distinction. The codebase (object language) is compiled into the specialist LM
(metalanguage) which researches the codebase (object language). The same information appears
at both levels. AMBIGUOUS confidence edges in the vindex are the tolerated contradictions that
enable this homoiconic collapse without explosion.

The *existence of a decider* is precisely a strict semantic ordering of what is and is not the
object language, decided externally. The LQL engine IS that decider for the vindex layer. H6
says global decidability — a decider for all facts about the full vindex — does not exist.
The stack is babelian at each local interface and non-babelian globally.

### LLMs as Non-Babelian Objects

Language models are inherently non-babelian: they produce contradictions (hallucinations)
without explosion. They can reason about themselves (the metalanguage IS accessible in the
object language via prompting). Their weights represent distributions over contradictory facts —
not a consistent set — and this is not a defect but the paraconsistent structure that enables
useful generalization.

The vindex makes this structure explicit and auditable: the EXTRACTED / INFERRED / AMBIGUOUS
confidence levels are a graded paraconsistency taxonomy. Compiling a vindex with AMBIGUOUS
edges produces a specialist LM that has inherited those contradictions. The autoresearch loop
stabilizes when the contradiction profile is stable — this is the non-babelian convergence
criterion.

### Three Varieties of Paraconsistency in the GCF Stack

Paraconsistency is not monolithic. Three distinct varieties appear across the GCF:

**1. Localized (classical)**: Inconsistency contained at a strict external semantic layer. A
consistent metalanguage bounds where object-language inconsistency can appear. This is the
paraconsistency of the LARQL babelian layers: the LQL query engine (a consistent decider) bounds
what triple-membership claims are valid; the Tabby API (a consistent interface) bounds what
completions can be requested. The hierarchy is maintained at each local interface.

**2. Diffuse (quantum / fully paranormal)**: Inconsistency distributed throughout the object; no
external consistent layer contains it. Fully paranormal = paraconsistent + paracomplete +
paraidentity (no-cloning, no-erasure, no-partial-swap simultaneously). LLM vindexes are diffuse
paranormal objects: AMBIGUOUS edges appear at all semantic levels; weight tensors represent
distributions over contradictory facts distributed throughout the model.

`larql compile` is quantum measurement applied to a diffuse paranormal object: vindex (paranormal,
complex Kähler J, AMBIGUOUS edges throughout) → safetensors (classical) + information loss
(confidence metadata discarded; decoherence analog). A babelian decider applied to a non-babelian
object; classical output; paraconsistency absorbed.

**3. Structured (general-relativistic)**: Local-to-global consistency asserted; local Euclidean
axioms denied. The Riemannian manifold is globally well-defined and consistent; individual
tangent-space approximations (local flatness) fail at any finite scale. This is GCF H1 and H2:
LLM attention weights as (M, g) — locally consistent linear maps (flat tangent space), globally
curved geodesic structure (non-zero Riemann curvature tensor). The curvature is not a defect; it
IS the encoding of knowledge. The non-identification of space with absolute truth in GR maps to
the vindex's non-identification of confident edges with ground truth.

See `DISCOVERIES.md §Diffuse Paraconsistency` for the fixed-point analysis.
See `references/README.md §Quantum metalanguages` for citations.

## Swarm Categories

The production vision unifies these threads: ***swarm categories*** (category-theoretical
swarm language models) are ensembles of specialist LMs where each member is a
categorical object (vindex), coordination between members is a natural transformation
(attention-weight morphism across vindexes), and the routing function from user task to
specialist is a functor.

CategoricalReasoner provides the formal semantics of this structure (morphism composition,
functor existence = reasoning path validity). LARQL provides the runtime objects (vindexes
and LQL operations). The swarm is not a metaphor — it is a small category whose objects are
vindexes and whose morphisms are trainable transformations between them, formally verifiable
by the same KeY theorem prover and Curry-Howard machinery described above.
