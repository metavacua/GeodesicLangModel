#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 metavacua
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Convert graphify graph.json to a LARQL Vindexfile.

graphify outputs a NetworkX node-link JSON with nodes and links (edges).
LARQL Vindexfiles accept INSERT ("entity", "relation", "target") triples.
This script bridges them.

Usage:
    python graphify_to_vindexfile.py graph.json -o Vindexfile
    python graphify_to_vindexfile.py graph.json --base hf://chrishayuk/gemma-3-4b-it-vindex
    python graphify_to_vindexfile.py graph.json --min-confidence INFERRED -o -

The LARQL Vindexfile parser splits on commas and strips outer quotes but does
not handle escaped inner quotes, so we sanitize values by replacing " and ,
with safe equivalents before writing.
"""

import json
import sys
import argparse
from pathlib import Path


_CONFIDENCE_RANK = {"EXTRACTED": 2, "INFERRED": 1, "AMBIGUOUS": 0}


def _sanitize(s: str) -> str:
    """Sanitize a string for safe embedding in a Vindexfile triple.

    The LARQL parser splits on commas and strips outer double-quotes without
    unescaping, so we replace both characters rather than try to escape them.
    """
    return s.replace('"', "'").replace(",", ";")


def convert(
    graph_path: str,
    output_path: str,
    base_vindex: str,
    min_confidence: str,
) -> int:
    """Convert graph.json to a Vindexfile. Returns the number of edges written."""
    with open(graph_path, encoding="utf-8") as f:
        graph = json.load(f)

    min_rank = _CONFIDENCE_RANK.get(min_confidence.upper(), 0)
    links = graph.get("links", [])

    lines = [f"FROM {base_vindex}", ""]

    count = 0
    for link in links:
        source = _sanitize(str(link.get("source", "")).strip())
        target = _sanitize(str(link.get("target", "")).strip())
        relation = _sanitize(str(link.get("relation", "related_to")).strip())
        confidence = str(link.get("confidence", "EXTRACTED")).upper()

        if not source or not target or not relation:
            continue
        if _CONFIDENCE_RANK.get(confidence, 0) < min_rank:
            continue

        lines.append(f'INSERT ("{source}", "{relation}", "{target}")')
        count += 1

    content = "\n".join(lines) + "\n"

    if output_path == "-":
        sys.stdout.write(content)
    else:
        Path(output_path).write_text(content, encoding="utf-8")

    return count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert graphify graph.json to a LARQL Vindexfile",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("graph_json", help="Path to graphify graph.json")
    parser.add_argument(
        "-o", "--output",
        default="-",
        help="Output path (default: stdout, use '-' for stdout)",
    )
    parser.add_argument(
        "--base",
        default="hf://chrishayuk/gemma-3-4b-it-vindex",
        help="Base vindex for FROM directive (default: %(default)s)",
    )
    parser.add_argument(
        "--min-confidence",
        default="EXTRACTED",
        choices=["EXTRACTED", "INFERRED", "AMBIGUOUS"],
        help="Minimum confidence level of edges to include (default: %(default)s)",
    )
    args = parser.parse_args()

    count = convert(args.graph_json, args.output, args.base, args.min_confidence)
    print(f"# Wrote {count} INSERT statements", file=sys.stderr)


if __name__ == "__main__":
    main()
