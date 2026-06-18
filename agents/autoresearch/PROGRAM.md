<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Self-Referential Vindex Autoresearch

Autoresearch loop where the object of research is the codebase-as-language-model
pipeline that powers the loop itself.

Each iteration builds the specialist LM from the current codebase, measures how
much of the codebase's knowledge structure is encoded in the vindex, then proposes
improvements to encode more.

## Files

Editable:
- `tools/graphify-to-vindex/graphify_to_vindexfile.py` — adapter: controls which graphify edges enter the vindex and how they are normalised
- `agents/autoresearch/extra_inserts.vindexfile` — agent-editable static triples; supplement AST-derived edges with conceptual math↔code mappings
- `agents/autoresearch/PROGRAM.md` — this file; the program can refine its own instructions across iterations

Fixed:
- `FORMALIZATION.md` — target specification: the 19 math↔code mappings that define correct structure
- `MATHEMATICAL_FOUNDATIONS.md` — GCF theory; the manifold the vindex approximates
- `PIPELINE.md` — full round-trip documentation
- `CONVERGENCE.md` — CategoricalReasoner ↔ LARQL bridge

## Metric

Command: bash agents/autoresearch/run_experiment.sh
Regex: METRIC: ([\d.]+)
Goal: Maximize

## Constraints

time_budget_seconds: 7200

## Instructions

You are improving the pipeline that encodes the GeodesicLangModel codebase into a
specialist language model vindex. The pipeline is:

  codebase → graphify update → graph.json
           → adapter         → Vindexfile
           → extra_inserts   → Vindexfile (appended)
           → larql build     → vindex/

The metric is total_edges: the number of triples successfully ingested into the
vindex. More edges = denser knowledge graph = more of the codebase's categorical
structure is encoded in the LM weights.

Your two primary levers are:

1. **adapter** (`tools/graphify-to-vindex/graphify_to_vindexfile.py`):
   - Adjust `_sanitize()` to normalise entity names (e.g. collapse path variants,
     strip file extensions for conceptual entities)
   - Add relation type normalisation (e.g. map "invokes"/"calls"/"delegates_to"
     to a canonical relation)
   - Adjust confidence filtering to include INFERRED edges when they are
     semantically meaningful
   - Add pre/post-processing of the graph to derive composite edges graphify
     cannot produce from AST alone

2. **extra_inserts.vindexfile**:
   - Add conceptual triples that graphify cannot extract from source code
   - Seed with more rows from FORMALIZATION.md's math↔code table
   - Add cross-domain links: e.g. connecting CategoricalReasoner morphisms to
     LQL operations, or graphify communities to categorical objects

Before proposing changes, read FORMALIZATION.md in full. Each of its 19 rows is a
target triple the vindex should encode. Check which rows are already covered by
extra_inserts.vindexfile and which are missing — the missing ones are the highest-
value additions.

The loop is self-referential: the codebase being researched is compiled into the
specialist LM that will run the next iteration. Improvements to the pipeline
improve the researcher. This is a fixed-point iteration; convergence is not
guaranteed (see DISCOVERIES.md §H6).
