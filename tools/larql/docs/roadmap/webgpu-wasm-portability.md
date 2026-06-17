<!--
SPDX-FileCopyrightText: larql-to-sparql contributors
SPDX-License-Identifier: AGPL-3.0-or-later
-->

# Portability Track: wasm32 + WebGPU

This document describes the **portability track** for the `metavacua/GeodesicLangModel` fork
of `larql-to-sparql`. It is additive to the canonical two-track philosophy (GPU track +
CPU track) documented in `ROADMAP.md` — it does not alter those tracks or the
"no GPU-only paths in core" constraint (C11).

---

## Motivation

The production goal is ***swarm categories*** (category-theoretical swarm language models):
specialist LMs compiled JIT from graph databases and deployed wherever they are needed —
browser, mobile, embedded, server. This requires LARQL to run in environments that are
closed to native OS I/O: browser sandboxes, WASI runtimes, and GPU-WebGPU compute contexts.

The canonical LARQL codebase is already well-positioned for this. The work here is to
make that positioning explicit, add a build gate that enforces it, and then extend outward
along the wasm target hierarchy.

---

## Wasm32 Stratification Model

Four strata, ordered from most to least restrictive:

| Stratum | Target | Primary runtime | I/O model |
|---------|--------|-----------------|-----------|
| **Compute** | `wasm32v1-none` | any wasm host, anywhere | no std, no I/O at all |
| **Browser** | `wasm32-unknown-unknown` | Firefox / Playwright (test), WebGPU browsers (prod) | JS glue; no direct OS I/O |
| **OS-like** | `wasm32-wasip1` | wasmer (preferred), wasmtime (upstream), pulley (no-Cranelift gap) | WASI P1 file/net primitives |
| **Emscripten** | `wasm32-unknown-emscripten` | Node.js (portable-std) or browser with MEMFS (full) | two distinct seams — see below |

Ubuntu x64 is the primary OS compile and runtime verification target for all wasm outputs.

### Emscripten Seam: Portable Std vs Full

`wasm32-unknown-emscripten` has two meaningfully different operating modes:

| Mode | Emscripten config | What it provides | Relation to other strata |
|------|------------------|-----------------|--------------------------|
| **Portable std** | minimal (`-sSTRICT` / no POSIX APIs) | `std::` shim (libc++); no filesystem, no POSIX | Sits between Compute and Browser — useful as a portability check: code that compiles here with no OS I/O deps is a short step from `wasm32-unknown-unknown` |
| **Full** | default (MEMFS + POSIX emulation) | emulated filesystem, POSIX stubs, Node.js integration | Closer to OS-like; highest emscripten overhead; deriving from WASI path is preferred |

The **portable std seam** is the important one for LARQL: it exposes whether a crate truly has
no OS I/O hidden behind `std::` types (e.g. `std::fs`, `std::net`), making it a compile-time
check that the Compute or Browser stratum is reachable. If a crate compiles to portable-std
emscripten without filesystem stubs, moving it to `wasm32-unknown-unknown` (add JS glue) or
`wasm32v1-none` (strip std) becomes mechanical.

**Full emscripten** (MEMFS + POSIX stubs) is lower priority: it papers over OS I/O rather than
eliminating it, making crates appear more portable than they are. Prefer the WASI path
(`wasm32-wasip1` + wasmer) where OS I/O is genuinely required — that path is explicit about
what OS primitives it uses.

The goal is to push each LARQL crate to the **most restrictive stratum** it can inhabit,
making the partition explicit:

| Crate | Target stratum | Blocker (if any) |
|-------|---------------|-----------------|
| `model-compute` (no features) | Compute (`wasm32v1-none`) | none — zero I/O deps |
| `model-compute --features wasm` (wasmi) | Compute (`wasm32v1-none`) | none — wasmi is pure Rust |
| `larql-core --no-default-features --features msgpack` | Compute | none — pure serde/thiserror |
| `larql-core` (default, with http) | Browser | reqwest → JS fetch (wasm32-unknown-unknown) |
| `larql-vindex` | Browser / OS | memmap2, libc, hf-hub → requires VindexStorage impl |
| `larql-lql`, `larql-models` | Browser / OS | depends on vindex |
| `larql-inference` | OS-like | tokio, tonic → wasm32-wasip1 + wasmer async |
| `larql-server` | OS-like | axum, tokio |
| `larql-cli` | **Split target** (see below) | bin must stay OS; lib can reach Browser |

---

## larql-cli Split (Priority Focus)

`larql-cli` is the structural wedge that makes the wasm32 stratification explicit in
the codebase. It currently bundles three concerns that must be cleanly separated:

| Concern | Must live | Rationale |
|---------|-----------|-----------|
| Command logic (parse statement, call crate) | **inside wasm host** | Pure function: input → output |
| LQL executor, graph algorithms | **inside wasm host** | larql-core, larql-lql already wasm32-safe |
| File I/O (open vindex, read weights) | **outside wasm host** | mmap/libc/hf-hub; VindexStorage seam is the abstraction |
| Stdin/stdout/signal handling | **outside wasm host** | OS primitives |
| clap argument parsing | **outside wasm host** | depends on std::env, OS signals |
| HTTP fetch (hf:// URLs) | **outside wasm host** (native) / **JS fetch** (browser) | reqwest is gated by `http` feature; browser gets JS glue |

The target structure:

```
larql-cli/src/
├── lib.rs                  ← everything inside the wasm host
│   ├── execute(stmt, storage: &dyn VindexStorage) → Result<Rows>
│   ├── compile(vindex, output, fmt, storage: &dyn VindexStorage) → Result<()>
│   └── ...                 (all command logic; takes VindexStorage instead of paths)
├── bin/
│   └── larql.rs            ← OS entry point: parse clap args → open files → call lib
└── interface/
    ├── wasm.rs             ← #[wasm_bindgen] / WASI exports: bridge JS/host to lib fns
    └── native.rs           ← native OS IO: implement VindexStorage over real files
```

**Key principle**: wherever `larql-cli` currently takes a `&Path`, it should take a
`&dyn VindexStorage`. The OS native impl opens the file and wraps it; the in-memory
impl holds bytes loaded by the JS host; the WASI impl uses WASI file descriptors.

This refactor is purely additive — it does not change the binary behavior, only
introduces the `lib.rs` boundary that wasm targets need.

### Runtime targets per stratum

| Stratum | Target triple | Runtime | Test harness |
|---------|--------------|---------|--------------|
| Compute | `wasm32v1-none` | any wasm host; wasmi preferred | `cargo test --target wasm32-unknown-unknown` with wasmi runner |
| Browser | `wasm32-unknown-unknown` | Firefox (prod), Playwright (CI) | Playwright + wasm-pack test |
| OS-like | `wasm32-wasip1` | wasmer (preferred); wasmtime + pulley (no-Cranelift hosts) | `wasmer run larql.wasm -- infer ...` |
| Emscripten (portable std) | `wasm32-unknown-emscripten` | Node.js, minimal config | portability diagnostic: does lib.rs compile without filesystem stubs? |
| Emscripten (full) | `wasm32-unknown-emscripten` | Node.js or browser + MEMFS | lower priority; papers over OS I/O; prefer WASI path |

Ubuntu x64 is the **primary OS compile and CI verification target** for all strata.
macOS (Apple Silicon) is the primary native Metal target per the canonical ROADMAP.

**On runtimes**: wasmtime is used upstream in `larql-cli` (`wasm-jit` feature with
Cranelift). For hosts where Cranelift is absent (arm32, some embedded), pulley is the
intended gap-filler; wasmi remains the universal fallback (pure Rust, runs anywhere
including inside another wasm host). wasmer is the preferred WASI runtime for
`wasm32-wasip1` because it supports WASIX and faster AOT without requiring Cranelift.

---

## VindexStorage Seam (Already Shipped)

`VindexStorage` (shipped 2026-05-10, all 7 migration steps) is the storage seam:
a sealed, mmap-agnostic byte-handle trait where backends plug in. The in-browser
backend is a new `VindexStorage` impl that holds vindex bytes in a `Vec<u8>` or
JavaScript `ArrayBuffer`, with no filesystem access:

```rust
// New: browser/wasm backend — no mmap, no libc
struct InMemoryVindexStorage {
    data: Arc<[u8]>,
}

impl VindexStorage for InMemoryVindexStorage { ... }
```

This already has a trait slot. No architecture change needed; the in-memory impl is
a straightforward addition.

---

## wgpu Backend (Vulkan + WebGPU)

`larql-compute`'s `ComputeBackend` trait (`backend/mod.rs`) is the seam for GPU backends.
The existing Metal backend demonstrates the pattern. A `wgpu` backend:

- Uses [wgpu](https://github.com/gfx-rs/wgpu) (Vulkan, Metal, DX12, WebGPU — one API)
- Slots into the same `ComputeBackend` trait as the existing Metal backend
- Gives **Vulkan on Linux/Windows**, **WebGPU in browsers** with one implementation

Priority: wgpu is lower-risk than CUDA (no vendor lock) and enables WebGPU browsers
as a natural extension of the same code path.

CUDA: deferred. See [ianblenke/larql](https://github.com/ianblenke/larql) for existing
CUDA work; the fork direction is WebGPU-first, not CUDA-first. CUDA is behind Vulkan
and WebGPU in priority because it is GPU-only and OS-coupled in ways that wasm32
refactoring actively avoids.

---

## LARQL → MLC/TVM Adapter (Max GPU Coverage)

For GPU deployment outside the wgpu matrix (ROCm, older Metal, embedded GPU targets),
a LARQL → MLC/TVM adapter is the highest-leverage path:

```
larql compile --format mlc --output ./dist/specialist-mlc
mlc_llm serve ./dist/specialist-mlc
```

MLC/TVM compiles the vindex to optimized compute kernels for the target GPU, covering
the full matrix (CUDA, Metal, ROCm, Vulkan, WebGPU) without LARQL implementing each.
This is the `metavacua/mlc-llm` fork's primary role.

---

## WebLLM Front-End

`metavacua/web-llm` (fork) consumes MLC-compiled vindexes and runs them in the browser
using WebGPU. The LARQL pipeline ends with a browser-native specialist LM:

```
vindex → larql compile --format mlc → web-llm → browser (WebGPU)
```

This enables fully client-side swarm category operation: the specialist LM, its vindex,
and the coding agent harness all run inside the browser. Remote-KB and
attention-on-smartphone follow from the same wasm32 + WebGPU path.

---

## Implementation Order

| Step | Work | Gate |
|------|------|------|
| **W1** | Build gate: `wasm32-unknown-unknown` for compute-pure tier | `make wasm32-compute-tier-build` (see Makefile) |
| **W2** | `InMemoryVindexStorage` impl — `VindexStorage` browser backend | unit test: load vindex bytes from `Vec<u8>` |
| **W3** | `larql-cli` lib/bin/interface split — separate wasm32-compilable lib from OS bin | `cargo build -p larql-cli --lib --target wasm32-unknown-unknown` |
| **W4** | wasm32 WASI path — `larql-inference` on wasm32-wasip1 + wasmer | `wasmer run larql.wasm -- infer ...` |
| **W5** | wgpu `ComputeBackend` impl — Vulkan + WebGPU backend | Vulkan triangle smoke test on Linux |
| **W6** | LARQL → MLC/TVM adapter — `larql compile --format mlc` | `mlc_llm serve` loads compiled vindex |
| **W7** | WebLLM integration — load MLC vindex in browser | Playwright test: completion from browser |

W1 is the first concrete step — additive, non-breaking, mirrors the canonical ROADMAP's
C10/C11 "measure before you can enforce a track."

---

## Relation to Canonical ROADMAP

This portability track does not conflict with the canonical ROADMAP's two-track philosophy:

- **GPU track** (Metal baseline → competitive with ollama): unchanged; wgpu backend (W5) is additive to Metal, not a replacement
- **CPU track** (GPU-free sparse retrieval): unchanged; wasm32-unknown-unknown IS the ultimate CPU-track endpoint (universal, GPU-free, runs anywhere)
- **C11** ("no GPU-only paths in core"): wgpu/WebGPU is wasm32-compatible, so W5 respects C11 by design; MLC/TVM (W6) is external to core

The one-line pointer in `ROADMAP.md` marks this as a fork-specific track that does not
alter the upstream design contract.
