# Guitar Alchemist

**AI-native tools for music, machine learning, and agent governance.**

We build composable systems where AI agents operate under principled governance — combining music theory, ML algorithms, neuro-symbolic reasoning, and constitutional alignment into a federated ecosystem.

## Repositories

### [ix](https://github.com/GuitarAlchemist/ix) — Machine Forge

Rust workspace (32+ crates) of composable ML and math algorithms exposed as Claude Code skills via MCP.

- Optimization (SGD, Adam, PSO, simulated annealing), search (A\*, MCTS, minimax), neural networks (trainable transformers with GPU attention)
- Chaos theory, topology, game theory, signal processing, adversarial ML, category theory
- GPU compute via WGPU, DAG pipeline orchestration, embedded cache
- **36 MCP tools** available to AI agents

### [tars](https://github.com/GuitarAlchemist/tars) — Thinking, Acting, Reasoning System

Self-improving AI agent framework in F# combining neuro-symbolic reasoning, multi-agent orchestration, and probabilistic grammars.

- Closed-loop evolution pipeline: grammar weighting, pattern promotion, metacognition
- Multi-agent orchestration with belief graphs and memory
- 800+ tests passing

### [ga](https://github.com/GuitarAlchemist/ga) — Guitar Alchemist

AI-powered music theory and guitar learning platform built with .NET 9 and React.

- Chord analysis, scale exploration, voice leading, harmonic analysis
- Connected to ix ML tools for chord clustering, spectral analysis, and progression classification
- MCP server exposing 50+ music theory tools

### [Demerzel](https://github.com/GuitarAlchemist/Demerzel) — Agent Governance

Reusable governance framework for AI agents — constitutions, personas, alignment policies, and multi-valued logic.

- 11-article constitution defining behavioral boundaries
- 12 agent personas with structured capability profiles
- Tetravalent logic (True / False / Unknown / Contradictory)
- Behavioral tests and thought experiments

> Named after [Eto Demerzel](https://asimov.fandom.com/wiki/R._Daneel_Olivaw) — the guardian who shapes policy without wielding direct power.

## MCP Federation

The repositories connect through the [Model Context Protocol](https://modelcontextprotocol.io/), forming a federated agent ecosystem:

```
┌─────────────────────────────────────────────────┐
│                  Claude Code                     │
│              (orchestration layer)               │
└──────┬──────────────┬──────────────┬─────────────┘
       │              │              │
  ┌────▼────┐   ┌─────▼─────┐  ┌────▼────┐
  │   ix    │   │   tars    │  │   ga    │
  │  Rust   │   │    F#     │  │  C#/.NET│
  │ 36 tools│   │ reasoning │  │ 50+tools│
  └────┬────┘   └─────┬─────┘  └────┬────┘
       │              │              │
       └──────────────▼──────────────┘
              Demerzel Governance
            (constitutions, personas,
             tetravalent logic)
```

## Built With

**Rust** · **F#** · **.NET 9** · **React** · **WGPU** · **Claude Code** · **MCP**
