<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# AGENTS.md

Development guidance for the GeodesicLangModel research constellation.

## Repository structure

```
geodesiclangmodel/
├── tools/larql/        git subtree ← metavacua/larql-to-sparql (Rust + WASM)
├── reasoning/          git submodule ← metavacua/CategoricalReasoner (Java + SPARQL)
├── theory/             git submodule ← metavacua/Theory (LaTeX thesis)
├── ontology/subclass/  git submodule ← metavacua/subclass (ontology scaffold)
├── experiments/        Falsifiable experiment classes A–F
├── agents/             Coding agent harness design docs
└── references/         Bibliography
```

Each subcomponent has its own development guidance:

- **LARQL**: [`tools/larql/AGENTS.md`](tools/larql/AGENTS.md)
- **CategoricalReasoner**: [`reasoning/AGENTS.md`](reasoning/AGENTS.md)

## Getting started

```sh
# Clone with submodules
git clone --recurse-submodules https://github.com/metavacua/GeodesicLangModel

# If already cloned without --recurse-submodules:
git submodule update --init --recursive

# subclass main branch is empty; active work is in candidate branches:
git -C ontology/subclass checkout <branch-name>
```

## Build requirements

| Subsystem | Requirements |
|-----------|-------------|
| `tools/larql/` | Rust stable + nightly (proc-macros), optional Metal GPU (Apple Silicon) |
| `reasoning/` | Java 25, Maven |
| `theory/` | pdflatex / XeLaTeX (optional) |
| Root | `pipx run reuse lint` for license compliance |

## Technology direction

**Rust + WASM** is the target platform for all computation. This means:

- `tools/larql/` is the primary execution environment
- `reasoning/` (Java) serves as the **reference specification** for categorical logic algorithms; implementations migrate to Rust as they mature
- The `model-compute` crate in `tools/larql/crates/` already uses the WebAssembly backend for portable, arm32-safe compute kernels
- Oxigraph (Rust SPARQL store) is the target for SPARQL execution, complementing CategoricalReasoner's Java/Jena SPARQL execution

## Submodule workflow

```sh
# Update all submodules to their latest pinned commits
git submodule update --remote --merge

# Sync larql subtree from upstream
git subtree pull --prefix=tools/larql \
  http://local_proxy@127.0.0.1/git/metavacua/larql-to-sparql main --squash
```

## Coding agent harness forks

`metavacua/goose` and `metavacua/tabby` are **independent development forks** — not upstream contribution forks. They do not require DCO sign-off. Development on these forks adds LARQL/LQL integration. See [`agents/stack.md`](agents/stack.md) for design.

## Security advisory: Cluster 4 repos

`metavacua/SynthPlayground`, `metavacua/AGENTSDevTools`, and `metavacua/SelfDevTools` are research specimens from an earlier autonomous-agent experiment. **Do not execute code from these repos.** See [`DISCOVERIES.md`](DISCOVERIES.md) for context.

## License compliance

```sh
pipx run reuse lint
```

REUSE.toml enforces dual-licensing (CC-BY-SA-4.0 for docs, AGPL-3.0-or-later for software). Submodule directories carry their own REUSE configs; the root lint does not enforce inside them.
