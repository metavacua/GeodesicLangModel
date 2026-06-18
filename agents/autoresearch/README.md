<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Self-Referential Vindex Autoresearch

An autoresearch loop whose **research object is the pipeline that powers the loop
itself** — the codebase-as-language-model stack.

## What it does

Each iteration:

```
codebase → graphify update → graph.json        # distil codebase → knowledge graph
         → adapter         → Vindexfile        # graph edges → vindex build spec
         → extra_inserts   → Vindexfile        # agent-editable conceptual triples
         → larql build     → vindex/           # graph Laplacian embedded
         → metric          → METRIC: N         # total edges ingested
```

The nca autoresearch agent proposes edits to the adapter or `extra_inserts.vindexfile`,
re-runs the experiment, and keeps the change if `N` increases.

## The self-referential structure

The specialist LM compiled from this codebase is the same LM that runs the next
iteration of the research loop. At iteration 0 the base model (Gemma 3 4B-IT vindex)
runs the loop. From iteration 1 onward the specialist built from the previous
iteration runs the next.

```
iteration 0:  base_model        researches GeodesicLangModel  → specialist_v1
iteration 1:  specialist_v1     researches GeodesicLangModel  → specialist_v2
iteration N:  specialist_vN     researches GeodesicLangModel  → specialist_v(N+1)
```

Each `specialist_vN → specialist_v(N+1)` is a morphism in the category of vindexes.
The autoresearch loop traces a path through that category.

## The bootstrap problem

The specialist cannot run the loop until it exists, and it does not exist until the
loop has run at least once. Solution:

1. Run iteration 0 with the base model (or any OpenAI-compatible endpoint).
2. After `larql compile` produces `specialist_v1.safetensors`, load it into Ollama
   or llama.cpp and point `nca --api-base` at that endpoint.
3. Run subsequent iterations against the specialist.

```bash
# Iteration 0 (base model via Tabby or Ollama)
nca autoresearch agents/autoresearch/PROGRAM.md

# Iterations 1+ (specialist endpoint)
AUTORESEARCH_BASE_MODEL=local://path/to/specialist_v1.safetensors \
nca --api-base http://localhost:11434/v1 autoresearch agents/autoresearch/PROGRAM.md
```

## Metric: edge count and Euler characteristic

`run_experiment.sh` reports two quantities:

| Quantity | Formula | Connection to GCF |
|---|---|---|
| `total_edges` | `graphify_edges + extra_edges` | Knowledge density in vindex |
| `euler_chi` | `V − E + communities` | Gauss-Bonnet χ(M) = ∫κ dA / 2π |

The **primary metric** (`METRIC: N`) is `total_edges` — this is what nca autoresearch
optimises. Euler characteristic is reported for interpretability; a decreasing χ with
increasing E indicates the graph is filling in the manifold (less topological "gap").

## H6 connection: why the loop does not converge

By H6 (Operational Incompleteness, Rosko 2025), there exist Π⁰₂ facts about the
vindex that the vindex itself cannot derive. Concretely:

- Each iteration's specialist LM reveals new structural relationships in the codebase.
- Those relationships generate new edges in the next Vindexfile.
- The new edges change the specialist, which reveals further new relationships.
- The loop never reaches a fixed point where no new edges can be added.

The trajectory of `(total_edges, euler_chi)` across iterations is an empirical test
of the GCF convergence claim. Non-convergence is predicted; any apparent stall is a
candidate for investigation (pruned region of the manifold, not a genuine fixed point).

This is the formal, constrained version of what the SynthPlayground prototype
demonstrated informally: an agent researching its own codebase asymptotically
approaches but never fully represents itself. See `DISCOVERIES.md`.

## Files

| File | Role |
|---|---|
| `PROGRAM.md` | nca `ResearchProgram` config (Markdown format) |
| `run_experiment.sh` | Experiment runner: full pipeline → `METRIC: N` |
| `extra_inserts.vindexfile` | Agent-editable conceptual triples (seeds from FORMALIZATION.md) |

## Running

```bash
# Prerequisites: nca installed, graphify installed, larql in PATH (or skip build step)
cd /path/to/GeodesicLangModel
nca autoresearch agents/autoresearch/PROGRAM.md

# Dry run (no larql required — metric from edge counts only):
bash agents/autoresearch/run_experiment.sh
```

Artifacts go to `.autoresearch/` (gitignored): `graph.json`, `Vindexfile`, `vindex/`.
