# Cross-Repo Business Value Tree

Date: 2026-07-01

This document maps the GuitarAlchemist issue hierarchy to business value.

The issue tree explains dependency and ownership. The business value tree explains why the work matters.

## North-star value

```text
Increase useful, safe, reviewable, compounding progress across GuitarAlchemist, TARS, IX, and Demerzel while reducing human decision fatigue.
```

## Core business outcomes

```text
1. Ship more useful work with less review friction.
2. Preserve human judgment for high-value architecture and governance decisions.
3. Build reusable agentic infrastructure instead of one-off automation.
4. Turn project knowledge into durable learning assets.
5. Improve agent reliability through evidence, benchmarks, and scoped attestations.
6. Reduce rework by capturing patterns, anti-patterns, and post-merge lessons.
7. Create an inspectable path from idea -> issue -> agent work -> PR -> evidence -> learning.
```

## Value streams

### 1. AFK execution value

Primary value:

```text
Reduce decision latency and keep work moving while the maintainer is away.
```

Issues:

- `.github#14` — TARS AFK Control Plane
- `.github#15` — Agent PR Review Queue
- `.github#18` — AFK workflow runbook
- `.github#20` — AFK effectiveness scorecard
- `.github#24` — AFK scorecard implementation

Business value:

- faster issue-to-PR flow;
- clearer delegation to Jules/Claude/Codex;
- fewer ambiguous review states;
- measurable throughput and review friction;
- safer batching of low-risk work.

Representative metrics:

```text
issue_to_pr_latency
pr_review_latency
safe_docs_prs_merged
blocked_prs_identified
human_prompts_per_week
review_friction_score
```

## 2. Governance value

Primary value:

```text
Avoid unsafe or low-quality automation by preserving human authority where it matters.
```

Issues:

- `Demerzel#624` — Objective Stack and Metric Balance
- `Demerzel#626` — Human Confirmation and Manual Review Protocol
- `Demerzel#628` — Proposal Review and Correction Event Ledger
- `Demerzel#630` — Human Decision Gates
- `Demerzel#632` — Anti-Rubber-Stamp Human Review
- `Demerzel#634` — Review Mode Router

Business value:

- protects architecture decisions from shallow automation;
- prevents human rubber-stamping;
- keeps approval prompts meaningful;
- creates traceable correction history;
- balances metrics against real project value.

Representative metrics:

```text
approval_without_change_rate
outcome_changed_by_human_rate
unnecessary_prompt_rate
decision_gate_count
correction_event_count
repeated_pattern_failure_count
```

## 3. Evidence and observability value

Primary value:

```text
Make agent work inspectable enough that the maintainer can trust, reject, or redirect it quickly.
```

Issues:

- `.github#21` — Abstraction Wall and Evidence Ladder
- `.github#22` — Verification Horizon and Human Intent Gates
- `.github#23` — Evidence Packets
- `TARS#162` — Intent Verification Harness
- `TARS#163` — Review Mode Verdict
- `IX#216` — Human Attention Metrics

Business value:

- fewer hidden assumptions;
- better review packets;
- faster diagnosis of unclear PRs;
- reduced risk of accepting work from summaries alone;
- better routing of review modes.

Representative metrics:

```text
evidence_packet_completeness
verification_horizon_exceeded_count
intent_verdict_confidence
scope_mismatch_count
review_mode_accuracy
```

## 4. Learning and knowledge-compounding value

Primary value:

```text
Convert project activity into reusable understanding for both the human maintainer and AI agents.
```

Issues:

- `TARS#90` — Second-Brain Harness
- `TARS#95` — Seldon Teaching Engine
- `TARS#164` — /teach Skill
- `TARS#166` — /teach Lesson Pack
- `TARS#167` — Persist /teach Sessions
- `TARS#169` — Streeling PhD-Grade Curriculum
- `IX#217` — Learning Mastery Metrics

Business value:

- reduces repeated explanation cost;
- turns difficult concepts into teachable modules;
- helps the maintainer make better architecture decisions;
- makes agent learning inspectable;
- creates a durable training curriculum for future project work.

Representative metrics:

```text
concept_mastery_delta
misconception_recurrence
teach_back_quality
scenario_transfer_score
spaced_review_due_count
lesson_reuse_count
```

## 5. Agent capability value

Primary value:

```text
Know which agents can be trusted for which narrow tasks, with evidence and expiry.
```

Issues:

- `TARS#168` — /teach Capability Attestations
- `IX#218` — PhD-Grade ML Math Tooling Backlog
- `IX#214` — Causal and Counterfactual Toolkit
- `IX#215` — Computational Argumentation Toolkit
- `IX#217` — Learning Mastery Metrics

Business value:

- avoids over-trusting a general model;
- allows safe reuse of proven agent skills;
- separates benchmark evidence from project readiness;
- makes agent capability drift visible;
- supports narrow trusted-scope automation.

Representative metrics:

```text
attestation_scope_count
attestation_expiry_count
scenario_pass_rate
benchmark_reproducibility_score
capability_drift_count
human_review_required_rate
```

## 6. Product and platform value

Primary value:

```text
Make GuitarAlchemist more likely to ship as a coherent product instead of a collection of experiments.
```

Issues:

- `.github#16` — Guitar Alchemist Product Roadmap
- TARS/IX/Demerzel governance and learning issues as enabling infrastructure

Business value:

- clearer product priorities;
- better architecture decisions;
- reusable assets and patterns;
- reduced experimental sprawl;
- improved path from research to playable/usable features.

Representative metrics:

```text
roadmap_item_progress
architecture_decision_quality
rework_rate
asset_reuse_count
feature_readiness_score
```

## Business value hierarchy

```text
North Star
  -> AFK execution value
  -> Governance value
  -> Evidence/observability value
  -> Learning/knowledge-compounding value
  -> Agent capability value
  -> Product/platform value
```

## Required business-value block for future issues

Every important issue should include:

```text
## Business value

Outcome:
-

Value hypothesis:
-

Who benefits:
-

How we know it worked:
-

Risk if ignored:
-
```

## Business value review rule

Before expanding a large issue tree, ask:

```text
Does this issue directly improve throughput, quality, safety, learning, capability evidence, or product progress?
```

If not, it should be deferred, narrowed, or reframed.

## Non-goals

- Do not optimize for issue count.
- Do not optimize for PR count alone.
- Do not treat learning metrics as business value unless they improve decisions or outcomes.
- Do not add governance process that increases friction without improving decision quality.
