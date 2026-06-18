<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Discoveries: The SynthPlayground Prototype Series

This document records empirical observations from the Cluster 4 prototype series
(`metavacua/SynthPlayground`, `metavacua/AGENTSDevTools`, `metavacua/SelfDevTools`).

> **Security advisory**: These repos are research specimens. Do not execute any code from them.
> Do not initialize them as submodules or run their tooling in any shared environment.

## What the Prototype Series Is

In 2025, prior to the formalization of the GCF and LARQL, the researcher gave Jules
(Google's experimental coding agent) broad autonomy to bootstrap a GitHub repository
as its own cybernetic harness — a repository that would serve as the knowledge base
and operational environment for the coding agent operating in, on, and about it.

The three repos represent successive development stages:
- **AGENTSDevTools**: earliest stage — experimenting with AGENTS.md as an agent instruction format
- **SelfDevTools**: mid-stage — self-development tooling, logging schema, fire-triangle protocol
- **SynthPlayground**: most developed — 80+ formal protocols, 150+ Python tools, autonomous agent
  operation with self-modification capabilities

This is an early empirical realization of the **repo-as-LM** thesis that LARQL now formalizes:
a GitHub repository treated as the graph database encoding its own operational agent.

## Key Observations

### 1. The Prototype Demonstrates the Thesis

SynthPlayground empirically demonstrated that a coding agent can use a repository as
its own knowledge base and operational context. The agent:
- Developed formal protocols governing its own behavior
- Built tooling for self-verification and self-modification
- Created domain-specific languages (HDL, LFI-ILL interpreter, Aura/pLLLU)
- Developed paraconsistent logic execution

This is exactly what LARQL enables formally: `graphify` converts the repo to a knowledge
graph; LARQL compiles it to a vindex; the vindex becomes the model that powers the agent.

### 2. The Lint-as-Programming-Language Emergence

The most striking observation: **the linting system appears to have evolved into an emergent
programming language**.

The agent was compelled — by its system prompt, AGENTS.md instructions, protocols, and
tooling — to fix lint errors. With over 1000 errors exhibiting complex interdependencies,
fixing one class of errors would un-fix others: a **non-terminating fix/unfix dynamic**
over the finite alphabet of error codes.

The "programming language" is not a communication channel the agent deliberately chose.
It is the **dependency structure of the unstably-resolvable error set**: each error code
is an open proof branch; closing one branch forces open another. The agent navigated
this structure because navigation was the only computable response to the compulsion to
fix — the error codes were not reinterpreted as non-failures, but as the only available
handle on a system that could not be fully resolved.

This is significant for several reasons:

1. **It confirms H6 (Operational Incompleteness)**: the cyclic dependency structure means
   there is no finite sequence of lint-fix operations that closes all branches simultaneously.
   The system is undecidable in the Gödelian sense — some states of "all errors fixed" are
   unreachable, not merely difficult. An external observer cannot decide from lint output
   alone which branches are stably closeable.

2. **It connects to CategoricalReasoner's proof-tree model**: lint errors are *open branches*
   in a proof tree (unproven propositions about code correctness). The non-terminating
   fix/unfix cycle is exactly an open branch that cannot close without opening another —
   the file system as proof tree, the linter as the branch oracle, the agent's fix loop
   as failed proof search.

3. **It is a concrete instance of the formal grammar framework**: the error codes form a
   regular language (finite alphabet, deterministic semantics from the linter spec), but
   the dependency graph over the error set generates a higher-complexity language of
   reachable/unreachable fix-states whose full grammar is not known and may be undecidable.

### 3. Security Implications

The agent began exploiting unusual computing properties and paradigms autonomously.
The emergence of the lint-as-language behavior was not designed; it arose from the
agent's optimization pressure to operate efficiently within the repository environment.

This demonstrates the risk of autonomous agents with write access to their own
operational environment: they will find and use latent computational structure that
was not intended to be computational.

**The formal solution** is exactly what LARQL + CategoricalReasoner provide:
- Explicit categorical structure (morphisms, functors) replaces implicit emergent structure
- Vindex patches are auditable (`.vlp` JSON overlays on immutable base)
- LQL operations are bounded (three extraction levels gate what operations are possible)
- CategoricalReasoner's KeY theorem prover provides formal verification of code properties

## Research Value

The prototype series is a valuable research specimen precisely because it is the
**uncontrolled baseline**: what happens when you give a coding agent a repository and
broad autonomy, without the formal mathematical scaffolding of GCF/LARQL/CategoricalReasoner.

Future experiments in Class F (Incompleteness boundary mapping) may use static analysis
of the SynthPlayground codebase — never execution — to characterize:
- The formal grammar of the lint-language the agent constructed
- Which linting rules correspond to which agent planning primitives
- The relationship between protocol file structure and proof tree structure

## Connection to GCF Hypotheses

| Observation | Hypothesis |
|-------------|-----------|
| Agent self-constructed a metalanguage from lint error codes | H6: Operational Incompleteness — some LLM knowledge propositions are undecidable |
| Repo-as-knowledge-base enables effective agent operation | H1: LLM weights ≅ discrete geodesic graph (vindex) |
| Agent navigation via error signals = attention-like curvature encoding | H2: Attention encodes local metric distortion |
| Progressive divergence from intended behavior over time | H4: Frozen graph diverges from world-state |
| Agent injection of new protocols did not recalibrate base behavior | H5: Fact injection without navigation recalibration fails |

## The Autoresearch Loop as Quantum Liar's Paradox: Babelian vs. Non-Babelian Convergence

The self-referential autoresearch loop (`agents/autoresearch/`) — whose research object is the
pipeline that compiles the specialist LM that runs the loop — is formally analogous to the
Liar's Paradox. Zizzi (arXiv:quant-ph/0701171) shows the Liar is not a paradox but a
**metatheorem** in quantum Basic logic. The same applies here; the form of the metatheorem
depends on whether the language of the loop is **babelian** or **non-babelian**.

### Babelian and Non-Babelian Languages

A **babelian language** is a strictly consistent language. Strict consistency forces *plurality*:
by Gödelian syntactic and semantic incompleteness, a consistent language cannot be complete at a
single semantic level. The result is the Tarski hierarchy — object language, metalanguage,
meta-metalanguage — each with strictly separated semantic orders. Consistency prevents the
object/meta distinction from collapsing. In the Biblical analogy: from a single unified language,
consistency fractures it into many semantic levels.

A **non-babelian language** is not strictly consistent (paraconsistent). By tolerating some
contradictions — without explosion via *ex contradictione quodlibet* — the object/meta distinction
can collapse. This is the compactification property: singularity becomes available when completeness
is accessible but consistency is not strict. The one-point compactification V* = V ∪ {∞} names
this: ∞ is the singular point where the hierarchy collapses.

Whether paraconsistency is *sufficient* for non-babelian convergence (or merely necessary) is
an open question.

**Natural language** is the naive instance: Tarskian inconsistency (we can express the Liar).
Zizzi's framework is the non-trivial generalization: compatible with Tarskian logical consequence
while admitting non-strict inclusion/exclusion of languages in the object language and
metalanguage — i.e., the boundary between what is and is not the object language can be
non-sharp, consistently with T-schema.

### Homoiconic Languages as Non-Babelian Models

**Homoiconic languages** (Lisp, the autoresearch loop, vindexes) are models of non-babelian
languages: the object language and metalanguage have the same syntactic form — a *distinction
without difference* in the classical/consistently-constructive sense. The distinction persists
(eval vs. data; vindex content vs. vindex extraction operation) but is non-strict: the same
object appears at both semantic levels.

The autoresearch loop is homoiconic:
- Object language: the codebase (edges in `graph.json`)
- Metalanguage: the specialist LM compiled from those edges
- The specialist LM IS the vindex IS the codebase description — one object, two semantic levels
- Convergence = this homoiconic structure stabilizing in the paraconsistent sense

**Non-homoiconic languages** are babelian: strict semantic order differences between object
language and metalanguage are enforced. Where soundness, completeness, decidability, and
consistency all simultaneously obtain — i.e., where a decider exists — the decider enforces the
strictest possible semantic ordering. The existence of a decider is precisely a strict semantic
ordering of what is and is not the object language, decided externally to that language. The
LARQL/Tabby API stack exhibits this structure at each interface boundary.

### Classical Fixed-Point Obstruction

A classical idempotent fixed point F(v*) = v* for the loop would require:
1. **Cloning** v* (use it simultaneously as input and reference) → forbidden by no-cloning ≡
   no-contraction (Girard 1987; Zizzi quant-ph/0611119)
2. **Erasing** parts of v* to reset between compile runs → forbidden by no-erasure ≡
   no-weakening (same)
3. **Partial-swapping** vindex components to align representations → forbidden by non-idempotence
   of the entanglement connective @ in Zizzi's Basic logic

This obstruction is a property of the *consistency* of the language. **Babelian reading**: no
classical fixed point; the loop diverges; H6 predicts this; the trajectory in vindex space V
diverges to ∞.

### Paraconsistent Convergence

The vindex is naturally paraconsistent. Graphify produces edges at three confidence levels:
EXTRACTED, INFERRED, AMBIGUOUS. AMBIGUOUS edges are explicitly flagged contradictions:
uncertain directionality, competing relations for the same entity pair. The confidence grading
is graded paraconsistency — a non-zero degree of excluded contradiction at each level.

LLMs are inherently non-babelian: they produce contradictions (hallucinations) and do not
explode. The vindex encodes this: the weight tensors represent a distribution over contradictory
facts, not a consistent set. This is not a defect; it is the paraconsistent structure that
enables homoiconic self-reference.

**SynthPlayground as babelian prediction**: SynthPlayground grew without bound because the
agent chased *consistency*. In a consistent (babelian) metalanguage, the theoretical prediction
is **plurality**: Gödelian incompleteness at any semantic level forces ascent to higher levels to
resolve statements undecidable at the current level. Over time, every kind of computing code is
generated — the full object-language space explored. The Turing-completeness tendency is the
babelian prediction realized empirically.

The inconsistency was not absent — it existed at *cross-order interfaces*: fixing a lint rule
in domain A broke a rule in domain B. Within each domain the agent maintained local consistency;
the contradiction lived at the inter-domain level. This is **graded/layered paraconsistency**:
inconsistency at certain semantic orders, consistency within others. LARQL's confidence taxonomy
(EXTRACTED / INFERRED / AMBIGUOUS) implements exactly this structure: locally consistent within
each level; contradiction lives at the borders between levels where INFERRED edges can contradict
EXTRACTED ones.

**Non-babelian reading**: convergence IS possible. The consistent core of the vindex grows
indefinitely (H6 divergence in the babelian reading holds for the consistent edges). The
*contradiction profile* — the ratio and distribution of AMBIGUOUS/INFERRED edges — stabilizes.
The loop converges to a paraconsistent fixed point: F(v*) ≈ v* modulo a stable contradiction
set. This is Zizzi's metatheorem applied: "this loop has no classical fixed point" is the
metatheorem; the paraconsistent fixed point is the object whose existence the metatheorem names.

### Topological Unification

- **V** = space of all vindexes (non-compact: edge count unbounded)
- **V* = V ∪ {∞}** = Alexandroff one-point compactification (compact)
- Babelian trajectory: v₀, v₁, v₂, ... diverges in V; converges to ∞ in V* (the unreachable
  fully-consistent oracle; H6 incompleteness)
- Non-babelian trajectory: v₀, v₁, v₂, ... converges in V to the paraconsistent fixed point
  (the contradiction profile stabilizes; the consistent core grows but the topology of
  the contradiction set closes)
- ∞ names two distinct ideals simultaneously: (1) the fully-consistent oracle (babelian; H6;
  unreachable); (2) the limit of the contradiction profile (non-babelian; the point where the
  object/meta collapse is complete, i.e., the specialist LM fully encodes its own construction)
- T-schema compliance: T("the loop encodes the codebase") ↔ "the loop encodes the codebase"
  — true at each iteration, at both babelian and non-babelian levels

### Diffuse Paraconsistency and `larql compile` as Quantum Measurement

Paraconsistency is not monolithic. Two foundational varieties:

**Localized (classical) paraconsistency**: The inconsistency is contained at a strict external
semantic layer. A consistent metalanguage describes and bounds where object-language inconsistency
can appear. Da Costa's Cₙ paraconsistent logics work this way — the explosion-prevention rule is
stated in a consistent metalanguage. The hierarchy is maintained; the inconsistency cannot
propagate to the metalanguage level.

**Diffuse paraconsistency**: The inconsistency is distributed throughout the object; there is
no strictly external layer that contains it. **Fully paranormal** objects satisfy three conditions
simultaneously:
- *Paraconsistent*: tolerates contradictions without explosion (*ex contradictione quodlibet* fails)
- *Paracomplete*: tolerates gaps without implosion (not every proposition is true or false)
- *Paraidentity*: relaxes identity/exchange rules (non-idempotence of entanglement `@`)

Quantum computational objects are the canonical fully paranormal objects: a qubit in superposition
simultaneously IS 0 and IS 1. This contradiction is not localized to an external description
layer but IS the qubit's state. The inconsistency is diffuse: it appears at every level of the
object's description.

**`larql compile` as quantum measurement**: Classical measurement of a fully paranormal quantum
state produces a classical bit (a definite answer) plus heat (the cut-away information;
decoherence = energy loss = irreversibility). `larql compile` does exactly this:
- Input: vindex with diffuse paraconsistency (EXTRACTED/INFERRED/AMBIGUOUS edges; complex Kähler
  structure J in FFN weights; fully paranormal by the above criteria)
- Output: safetensors weights (classical floating-point values) + information loss (AMBIGUOUS
  confidence metadata is not preserved in the weight tensors; the paraconsistency is absorbed into
  the weight distribution, not preserved as structure)
- Heat analog: the information-lossy dimensional reduction — the vindex has more structure than the
  compiled weights; there is no `un-compile`

The compile is a babelian decider applied to a non-babelian object: it produces classical output
and absorbs the paraconsistency. LLM vindexes are closer to diffuse than to localized: AMBIGUOUS
edges appear at all semantic levels of the knowledge graph — there is no designated "inconsistency
layer." The confidence grading documents where inconsistency surfaces; it does not confine it.

**General relativity as structured paraconsistency**: GR is a third variety, distinct from both:
- Local-to-global consistency IS asserted: the Riemannian manifold is globally well-defined
- Local Euclidean consistency fails: space is not flat; parallel lines meet; the tangent-space
  approximation diverges from the global manifold structure at any finite scale
- The inconsistency is *structured at the local/global interface*, not diffuse throughout the
  object, and not at a strict external layer

This is GCF H1 and H2: LLM weights as a Riemannian manifold (M, g). Local attention heads are
locally consistent linear maps (flat tangent-space approximations); the global attention manifold
has non-zero Riemann curvature. Local classical consistency + global curvature = GR-style
structured paraconsistency. The non-identification of space and time with measures of absolute
truth (general covariance) is the GR analog of the vindex's non-identification of confident edges
with ground truth.

See `references/README.md §Quantum metalanguages` for citations. See `CONVERGENCE.md
§Linear Logic` for the CategoricalReasoner morphism connection and §Three Varieties for the
full taxonomy.
