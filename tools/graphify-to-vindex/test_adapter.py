#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 metavacua
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Smoke-test the graphify→Vindexfile adapter without external dependencies."""

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from graphify_to_vindexfile import convert, _sanitize

SAMPLE_GRAPH = {
    "directed": True,
    "multigraph": False,
    "graph": {},
    "nodes": [
        {"id": "src/main.rs#main", "label": "main", "file_type": "function"},
        {"id": "src/utils.rs#parse_args", "label": "parse_args", "file_type": "function"},
        {"id": "std::env", "label": "env", "file_type": "module"},
    ],
    "links": [
        {"source": "src/main.rs#main", "target": "src/utils.rs#parse_args",
         "relation": "calls", "confidence": "EXTRACTED"},
        {"source": "src/main.rs#main", "target": "std::env",
         "relation": "imports", "confidence": "EXTRACTED"},
        {"source": "src/utils.rs#parse_args", "target": "std::env",
         "relation": "uses", "confidence": "INFERRED"},
    ],
}


def test_basic_conversion():
    with tempfile.TemporaryDirectory() as tmp:
        graph_path = Path(tmp) / "graph.json"
        out_path = Path(tmp) / "Vindexfile"
        graph_path.write_text(json.dumps(SAMPLE_GRAPH))

        count = convert(str(graph_path), str(out_path), "hf://chrishayuk/gemma-3-4b-it-vindex", "EXTRACTED")
        assert count == 2, f"Expected 2 EXTRACTED edges, got {count}"

        text = out_path.read_text()
        assert text.startswith("FROM hf://chrishayuk/gemma-3-4b-it-vindex"), "Missing FROM"
        assert 'INSERT ("src/main.rs#main", "calls", "src/utils.rs#parse_args")' in text
        assert 'INSERT ("src/main.rs#main", "imports", "std::env")' in text
        assert "INFERRED" not in text
        print("PASS: test_basic_conversion")


def test_min_confidence_inferred():
    with tempfile.TemporaryDirectory() as tmp:
        graph_path = Path(tmp) / "graph.json"
        out_path = Path(tmp) / "Vindexfile"
        graph_path.write_text(json.dumps(SAMPLE_GRAPH))

        count = convert(str(graph_path), str(out_path), "hf://chrishayuk/base", "INFERRED")
        assert count == 3, f"Expected 3 edges at INFERRED+, got {count}"
        print("PASS: test_min_confidence_inferred")


def test_sanitize():
    assert _sanitize('foo"bar') == "foo'bar"
    assert _sanitize("foo,bar") == "foo;bar"
    assert _sanitize("normal_id") == "normal_id"
    print("PASS: test_sanitize")


def test_stdout(capsys=None):
    with tempfile.TemporaryDirectory() as tmp:
        graph_path = Path(tmp) / "graph.json"
        graph_path.write_text(json.dumps(SAMPLE_GRAPH))
        count = convert(str(graph_path), "-", "hf://base", "AMBIGUOUS")
        assert count == 3
        print("PASS: test_stdout")


if __name__ == "__main__":
    test_sanitize()
    test_basic_conversion()
    test_min_confidence_inferred()
    test_stdout()
    print("\nAll tests passed.")
