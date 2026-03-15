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

AI-powered music theory and guitar learning platform built with .NET 10 and React.

- Chord analysis, scale exploration, voice leading, harmonic analysis
- Connected to ix ML tools for chord clustering, spectral analysis, and progression classification
- MCP server exposing 50+ music theory tools

### [Demerzel](https://github.com/GuitarAlchemist/Demerzel) — Agent Governance

Constitutional governance framework for AI agents — Asimov's Laws of Robotics, personas, alignment policies, multi-valued logic, cross-repo communication, and self-improving governance.

- **Asimov constitution** (Articles 0-5: Zeroth Law, First-Third Laws, Separation of Understanding/Goals, Consequence Invariance)
- **Default constitution** (Articles 1-11: Truthfulness, Transparency, Reversibility, Proportionality, and more)
- **7 personas** — Demerzel (governance coordinator), Seldon (knowledge transfer), skeptical-auditor, kaizen-optimizer, reflective-architect, system-integrator, default
- **9 policies** — alignment, rollback, self-modification, Kaizen (PDCA + waste + 5 Whys), reconnaissance, scientific objectivity, Streeling (knowledge transfer), governance audit, autonomous loops (Ralph Loop governance + agentic patterns catalog)
- **Galactic Protocol** — 6 contract schemas for cross-repo governance communication with crisp/fuzzy channel separation
- **Governance meta-compounding** — self-improving governance with promotion protocol, confidence calibration, semantic routing, evolution tracking
- **11 Claude Code skills** — `/demerzel` command with subcommands: audit, recon, directive, promote, evolve, teach, loop, patterns, confidence, harvest

> Named after [Eto Demerzel](https://asimov.fandom.com/wiki/R._Daneel_Olivaw) — the robot who guided humanity for 20,000 years through the application of the Zeroth Law.

## Knowledge Base (NotebookLM)

Research notebooks powering the ecosystem's institutional memory:

| Notebook | Topics | Link |
|----------|--------|------|
| **Compound the Compounding** | Meta-compounding, DSL evolution, grammar governance, promotion staircase, CompoundCore architecture | [Open](https://notebooklm.google.com/notebook/b9f51708-11cf-4618-ae4d-6981c9e02891) |
| **Probabilistic Grammars & Constrained LLM Reasoning** | Constrained decoding, PCFGs, neuro-symbolic AI, formal verification, TARS grammars | [Open](https://notebooklm.google.com/notebook/6b810c22-dcc3-45dd-a0f3-2e7921de5863) |
| **Semantic Event Routing Architecture** | Multi-agent orchestration, bounded fuzziness, confidence protocols, embedding-based routing, OPTIC-K | [Open](https://notebooklm.google.com/notebook/c9470f2a-a97a-4d94-a38d-a1fb22b99bf8) |

These notebooks are indexed by Demerzel's Streeling knowledge framework and harvested daily by Seldon for curriculum updates.

## MCP Federation

The repositories connect through the [Model Context Protocol](https://modelcontextprotocol.io/), forming a federated agent ecosystem governed by Demerzel:

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
     ┌────────────────────────────────┐
     │  Asimov Laws · Galactic Protocol  │
     │  Kaizen · Streeling · Ralph Loops │
     │  7 Personas · 9 Policies          │
     │  Governance Meta-Compounding      │
     └────────────────────────────────┘
```

## Built With

**Rust** · **F#** · **.NET 10** · **React** · **WGPU** · **Claude Code** · **MCP** · **NotebookLM**
