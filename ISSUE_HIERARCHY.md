# Cross-Repo Issue Hierarchy

This file records the current hierarchy across the GuitarAlchemist GitHub organization for AFK governance, TARS `/teach`, Streeling/Seldon learning, IX math/ML tooling, and Demerzel governance.

Date: 2026-07-01

## Top-level operating model

```text
.github   = organization cockpit, AFK boards, cross-repo process, scorecards
Demerzel  = governance, decision gates, review policies, objective stack
TARS      = agent runtime, second brain, `/teach`, Seldon bridge, intent verification
IX        = math/ML tooling, scoring, metrics, benchmarks, curriculum analytics
Streeling = curriculum/catalog/concept graph role, currently represented through TARS/IX issues
```

## AFK governance hierarchy

```text
.github#21 — Abstraction Wall and Evidence Ladder
  ├─ .github#22 — Verification Horizon and Human Intent Gates
  │   ├─ Demerzel#630 — Human Decision Gates for Architecture and Responsibility
  │   ├─ TARS#162 — Intent Verification Harness using IX and Demerzel Signals
  │   └─ TARS#163 — Review Mode Verdict for AFK Human Attention Routing
  ├─ .github#23 — AFK Agent Observability and Evidence Packets
  │   ├─ Demerzel#634 — Review Mode Router and Human Attention Budget
  │   └─ IX#216 — Human Attention Budget Metrics and Rubber-Stamp Detection
  ├─ .github#24 — AFK Effectiveness Baseline and Scorecard Implementation
  │   ├─ .github#20 — AFK workflow effectiveness scorecard
  │   ├─ IX#214 — Causal and Counterfactual Inference Toolkit for Governance Metrics
  │   └─ IX#216 — Human Attention Budget Metrics and Rubber-Stamp Detection
  ├─ .github#25 — AFK Pattern Registry and Anti-Pattern Memory
  └─ .github#26 — Anti-Goodhart Guardrails for AFK Metrics
      ├─ TARS#168 — /teach Capability Attestations for AI Agents
      ├─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum for /teach
      └─ IX#218 — PhD-Grade ML Math Tooling Backlog for Agentic Evaluation
```

## Demerzel governance hierarchy

```text
Demerzel#624 — Objective Stack and Metric Balance
  ├─ Demerzel#626 — Human Confirmation and Manual Review Protocol
  ├─ Demerzel#628 — Proposal Review and Correction Event Ledger
  ├─ Demerzel#630 — Human Decision Gates for Architecture and Responsibility
  ├─ Demerzel#632 — Anti-Rubber-Stamp Human Review Design [implemented by PR #636]
  └─ Demerzel#634 — Review Mode Router and Human Attention Budget [implemented by PR #636]
```

## TARS `/teach` and learning hierarchy

```text
TARS#90 — Second-Brain Harness
  ├─ TARS#95 — Seldon Teaching Engine as Research-to-Learning Bridge
  │   └─ TARS#164 — Interactive /teach Skill with Quiz, Teach-Back, and Mastery Checks
  │       ├─ TARS#165 — PR: /teach foundation merged
  │       ├─ TARS#166 — Add /teach Lesson Pack for Review Routing and Goodhart
  │       ├─ TARS#167 — Persist /teach Sessions into Second-Brain Learning State
  │       ├─ TARS#168 — /teach Capability Attestations for AI Agents
  │       └─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum for /teach
  └─ TARS#162 — Intent Verification Harness using IX and Demerzel Signals
      └─ TARS#163 — Review Mode Verdict for AFK Human Attention Routing
```

## IX math/ML/scoring hierarchy

```text
IX#214 — Causal and Counterfactual Inference Toolkit for Governance Metrics
IX#215 — Computational Argumentation and Deliberation Toolkit
IX#217 — Learning Mastery Metrics and Student Model for TARS /teach
  ├─ TARS#164 — /teach Skill
  ├─ TARS#167 — Persist /teach Sessions into Second-Brain Learning State
  └─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum for /teach
IX#216 — Human Attention Budget Metrics and Rubber-Stamp Detection
  ├─ Demerzel#632 — Anti-Rubber-Stamp Human Review Design
  ├─ Demerzel#634 — Review Mode Router and Human Attention Budget
  └─ TARS#163 — Review Mode Verdict for AFK Human Attention Routing
IX#218 — PhD-Grade ML Math Tooling Backlog for Agentic Evaluation
  ├─ TARS#168 — /teach Capability Attestations for AI Agents
  ├─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum for /teach
  ├─ IX#214 — Causal/Counterfactual Toolkit
  ├─ IX#215 — Argumentation Toolkit
  └─ IX#217 — Learning Mastery Metrics
```

## Streeling/Seldon curriculum hierarchy

```text
TARS#95 — Seldon Teaching Engine as Research-to-Learning Bridge
  ├─ TARS#164 — /teach Skill
  ├─ TARS#167 — Persist /teach Sessions into Second-Brain Learning State
  └─ IX#217 — Learning Mastery Metrics and Student Model

IX#209 — Streeling Research Registrar Support
  ├─ TARS#164 — /teach Skill
  ├─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum
  └─ IX#218 — PhD-Grade ML Math Tooling Backlog

IX#211 — GraphRAG-style Corpus Maps for Streeling and Second-Brain Retrieval
  ├─ TARS#169 — Streeling PhD-Grade Agentic AI Curriculum
  └─ IX#218 — PhD-Grade ML Math Tooling Backlog
```

## Rule for future issues

Every new cross-repo issue should include at least one of:

```text
Parent:
- owner/repo#number

Children:
- owner/repo#number

Related:
- owner/repo#number
```

Preferred hierarchy order:

```text
.github epic
  -> Demerzel governance epic/story
  -> TARS runtime/learning epic/story
  -> IX math/metric/tooling epic/story
  -> PR implementation
```

Do not rely only on issue titles for hierarchy. Add explicit issue comments or body links when relationships are cross-repo.
