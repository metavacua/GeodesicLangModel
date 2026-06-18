#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 metavacua
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# One iteration of the self-referential autoresearch loop:
#
#   codebase → graphify update → graph.json
#           → adapter          → Vindexfile
#           → extra_inserts    → Vindexfile (appended)
#           → larql build      → vindex/
#           → metrics          → METRIC: N
#
# The metric N is the total edge count ingested. Maximising N means the vindex
# encodes more of the codebase's structure. The Euler characteristic
# χ = V − E + communities is also reported; it tracks topology, not just volume.
#
# Usage:
#   bash agents/autoresearch/run_experiment.sh
#
# Env vars:
#   AUTORESEARCH_BASE_MODEL      default: hf://chrishayuk/gemma-3-4b-it-vindex
#   AUTORESEARCH_MIN_CONFIDENCE  default: EXTRACTED

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORK_DIR="${REPO_ROOT}/.autoresearch"
# graphify update writes to <dir>/graphify-out/graph.json by default
GRAPH_JSON="${REPO_ROOT}/graphify-out/graph.json"
VINDEXFILE="${WORK_DIR}/Vindexfile"
VINDEX_DIR="${WORK_DIR}/vindex"
BASE_MODEL="${AUTORESEARCH_BASE_MODEL:-hf://chrishayuk/gemma-3-4b-it-vindex}"
MIN_CONF="${AUTORESEARCH_MIN_CONFIDENCE:-EXTRACTED}"
EXTRA="${REPO_ROOT}/agents/autoresearch/extra_inserts.vindexfile"

mkdir -p "${WORK_DIR}"

log() { echo "[autoresearch] $*" >&2; }

# ── 1. graphify update ────────────────────────────────────────────────────────
log "Step 1: graphify update → graphify-out/graph.json"
if command -v graphify &>/dev/null; then
    graphify update "${REPO_ROOT}" 2>&1 >&2 \
        || log "graphify exited non-zero; continuing with whatever graph.json exists"
else
    log "graphify not in PATH; using existing graphify-out/graph.json"
fi

if [[ ! -f "${GRAPH_JSON}" ]]; then
    log "ERROR: ${GRAPH_JSON} not found. Run 'graphify update .' from the repo root first."
    exit 1
fi

# ── 2. adapter → Vindexfile ───────────────────────────────────────────────────
log "Step 2: adapter → Vindexfile"
ADAPTER_STDERR=$(python3 "${REPO_ROOT}/tools/graphify-to-vindex/graphify_to_vindexfile.py" \
    "${GRAPH_JSON}" \
    --output "${VINDEXFILE}" \
    --base "${BASE_MODEL}" \
    --min-confidence "${MIN_CONF}" 2>&1)
log "${ADAPTER_STDERR}"
EDGE_COUNT=$(printf '%s\n' "${ADAPTER_STDERR}" | grep -oP '(?<=# Wrote )\d+' || echo 0)

# ── 3. append extra_inserts.vindexfile ────────────────────────────────────────
EXTRA_COUNT=0
if [[ -f "${EXTRA}" ]]; then
    log "Step 3: appending extra_inserts.vindexfile"
    EXTRA_COUNT=$(grep -c '^INSERT' "${EXTRA}" || true)
    grep -v '^#' "${EXTRA}" | grep -v '^[[:space:]]*$' >> "${VINDEXFILE}" || true
    log "Appended ${EXTRA_COUNT} extra INSERT statements"
fi
TOTAL_EDGES=$(( EDGE_COUNT + EXTRA_COUNT ))

# ── 4. larql build → vindex ───────────────────────────────────────────────────
log "Step 4: larql build → vindex"
if command -v larql &>/dev/null; then
    rm -rf "${VINDEX_DIR}"
    larql build "${VINDEXFILE}" --output "${VINDEX_DIR}" 2>&1 >&2
    log "larql build complete → ${VINDEX_DIR}"
else
    log "larql not in PATH; skipping build (metric derived from edge counts only)"
fi

# ── 5. graph metrics ──────────────────────────────────────────────────────────
NODE_COUNT=$(python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    g = json.load(f)
print(len(g.get('nodes', [])))" "${GRAPH_JSON}" 2>/dev/null || echo 0)

COMMUNITY_COUNT=$(python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    g = json.load(f)
communities = {n.get('community', 0) for n in g.get('nodes', [])}
print(len(communities))" "${GRAPH_JSON}" 2>/dev/null || echo 1)

EULER_CHI=$(( NODE_COUNT - TOTAL_EDGES + COMMUNITY_COUNT ))

# ── 6. report ─────────────────────────────────────────────────────────────────
printf '\n=== Vindex Metrics ===\n'
printf 'nodes:           %s\n' "${NODE_COUNT}"
printf 'graphify_edges:  %s\n' "${EDGE_COUNT}"
printf 'extra_edges:     %s\n' "${EXTRA_COUNT}"
printf 'total_edges:     %s\n' "${TOTAL_EDGES}"
printf 'communities:     %s\n' "${COMMUNITY_COUNT}"
printf 'euler_chi:       %s\n' "${EULER_CHI}"
printf '\nMETRIC: %s\n' "${TOTAL_EDGES}"
