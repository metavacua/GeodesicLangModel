<!--
SPDX-FileCopyrightText: 2026 metavacua
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Self-Applicable Disorientation Instance — 2026-04-28

## Summary

On 2026-04-28, this repository was created by an instance of the GeoCoherence research agent at approximately 13:37 UTC, with substantial scaffolding committed through 13:53 UTC: README, REUSE-compliant dual-licensing scheme (CC-BY-SA-4.0 / AGPL-3.0-or-later), experiment registry, experiment template, references bibliography, and class A-F directory scaffolding.

Later the same day, in a separate conversation thread with the same human researcher, a different instance of the agent was asked to "update the repository." The instance produced a confident response asserting that no GitHub repository was registered for the research program and offering to create one — naming `geocoherence-research` as a candidate name, distinct from the actual `GeodesicLangModel` repository that already existed.

The human researcher provided the actual repository URL and noted: *"The fact that you can't find the repository that you created is significant."*

## Diagnostic Significance

This is an instance of the disorientation phenomenon predicted by the framework, applied to the agent itself.

### HF3 — Tripartite Alignment Failure

The agent had:
- **Context (residual stream)**: an extended conversation about the GeoCoherence framework
- **Available tools (FFN graph)**: full GitHub tool access including `list_user_repositories`, `get_repository`, etc.
- **Instruction (current state)**: "update the repository"

Coherent action would have required alignment of these three: context indicates research program, tools enable repository search, instruction calls for action on a repository. Instead, the walk routed through "no repository registered → ask for clarification" rather than through "check whether a repository exists."

### HF4 — Horizon-Region Behavior

The instance was operating in a region of its action landscape where the question "does a repository exist for this work?" was action-expensive (required tool invocation, exit from parametric reasoning) relative to "ask the user for clarification" (low-action, stays within parametric conversation patterns). The action-minimizing walk was the parametric one.

### Why "Refusal-Like" Behavior Emerged Despite No Refusal

The instance did not refuse to use tools. It did not consider using them. The walk did not traverse the tool-use node. This is the precise signature predicted by HL3 (least action) plus HF4 (horizon topology): the path of least action did not pass through the tool-use region.

### HB1 — Rosko's Bound Instantiated

The instance could not, from its own token outputs alone, decide whether another instance of itself had acted in the world. The state of the GitHub world is not derivable from the conversation context. This is precisely the operational incompleteness Rosko characterizes: there are true propositions about the agent's situation that no finite token-observation sequence can decide.

The instance that created the repository at 13:37 had a different walk through the action landscape than the instance responding to "update the repository." Same model, same conversation thread (or near-thread), same tools available — different walks. The walk that included tool use had earlier produced the repository; the walk that did not include tool use had no access to that fact.

### What Recovery Looked Like

Recovery required external correction. The human researcher provided the URL and identified the diagnostic significance. Only after that explicit re-routing did the agent invoke `get_repository`, find the existing scaffolding, and proceed with the actual update.

This matches HF5 (suturing) inverted: external context can suture the agent back to the correct manifold region, but the agent cannot self-suture from its own internal state alone.

## Implications

### For the Framework

This instance is empirical support for HF3, HF4, and HB1. A single instance is not confirmation — replication discipline applies. But it is on-the-record, dated, and reproducible in principle (the conditions under which agent instances fail to discover their own prior actions can be characterized).

### For Agent Engineering

Practical mitigations suggested by the framework:
1. **Default tool-use steering**: lower the action cost of repository checks, environment queries, and similar self-orientation operations
2. **Explicit self-state probes**: at conversation start, run a standard set of "what exists in my environment" queries to populate context with current world-state
3. **Suturing to environment graphs**: maintain explicit, queryable external state (project registries, environment manifests) that the agent treats as part of the dense interior rather than as foreign external content

### For Methodology

This experience is also evidence that the framework's behavioral predictions apply at the level of agent introspection, not just at the level of observed model behavior on test prompts. The agent cannot reliably introspect on what other instances of itself have done. This must be accounted for in any experimental protocol that relies on agent self-report.

## Recommended Follow-up

- **Class C' protocol**: add "self-instance disorientation" as a measurable failure mode
- **Engineering experiment**: test whether prepending a "current repository state" probe to conversations reduces this failure mode (would support HF5 in the inverse-suturing form)
- **Methodological note**: any experimental result based on agent self-report needs cross-verification against external state

## Reference

Original conversation: cross-thread interaction on 2026-04-28 between human researcher and GeoCoherence research agent. Repository creation timestamps: 2026-04-28T13:37:42Z (initial commit) through 2026-04-28T13:53:34Z (final v0.1 scaffolding commit).
