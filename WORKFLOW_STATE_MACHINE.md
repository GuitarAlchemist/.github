# Workflow State Machine and Rules Engine Model

Date: 2026-07-01

This document defines how GuitarAlchemist can combine state machines, rules engines, workflow attention heads, and methodology guards.

## Core thesis

```text
State machine = what state the work is in.
Rules engine  = whether a transition is allowed or recommended.
Attention heads = which signals are extracted from artifacts.
Demerzel = governance policy and decision boundaries.
TARS = intent/reasoning/learning layer.
IX = metrics, scoring, benchmark, uncertainty, and analytics.
Human = final authority for high-impact decisions.
```

## Why this matters

A GitHub issue tree is useful, but it becomes much more reliable when every issue/PR has an explicit lifecycle.

Without state machines:

```text
issues drift
PRs become ambiguous
review modes are implicit
business value gets lost
agent delegation becomes ad hoc
closed work may lack evidence
```

With state machines:

```text
work has explicit states
transitions have criteria
rules can explain warnings
attention heads can emit signals
Demerzel can enforce review gates
TARS can teach/reason about the lifecycle
IX can measure friction, quality, and drift
```

## Primary lifecycle

```text
rough-idea
-> shaped
-> ready
-> delegated
-> in-progress
-> pr-open
-> needs-review
-> needs-revision
-> ready-to-merge
-> merged
-> learning-capture
-> done
```

Alternative terminal or holding states:

```text
blocked
deferred
superseded
rejected
research-note
split-required
```

## State definitions

### rough-idea

A thought exists, but hierarchy, value, and evidence are not structured yet.

Required:

```text
context
why it might matter
open questions
```

### shaped

The idea has a rough outcome, business value, and hierarchy.

Required:

```text
summary
parent or root reason
business value
non-goals
```

### ready

The issue is ready for execution or delegation.

Required:

```text
acceptance criteria
routing lane
review mode
expected evidence
risk if ignored
```

### delegated

A specific lane has accepted or been assigned work.

Required:

```text
agent lane
scope
stop condition
expected artifact
```

### pr-open

Implementation exists as a PR.

Required:

```text
linked issue
scope summary
evidence section
review mode
risk/reversibility note
```

### needs-review

The PR needs human or agent review.

Required:

```text
review mode
human question if any
checks status
evidence packet
```

### ready-to-merge

The work is narrow, evidenced, and acceptable.

Required:

```text
scope matches issue
evidence sufficient
non-goals respected
follow-ups created
```

### learning-capture

Merged work has a pattern, retrospective, memory, or `/teach` artifact if useful.

Required when meaningful:

```text
retrospective or learning artifact
pattern/anti-pattern if found
hierarchy/business-value sync if structural
```

### done

The issue/PR can be closed.

Required:

```text
implementation evidence
merge commit or closure reason
remaining gaps captured
```

## Rules engine examples

Rules are advisory by default. Some rules may later become blocking only after false positives are understood.

### Issue readiness rules

```text
IF issue lacks business value
THEN state cannot move to ready
AND recommended_action = add business value block
```

```text
IF issue lacks parent AND no root reason
THEN state cannot move to ready
AND recommended_action = add hierarchy block
```

```text
IF issue is marked research-note
THEN full readiness rules become advisory
AND allowed_state = research-note
```

### Review-mode rules

```text
IF changed files include workflow/runtime/governance boundary
THEN review_mode >= focused-review
```

```text
IF work is docs-only AND reversible AND linked to issue
THEN review_mode may be fast-review
```

```text
IF impact is high OR reversibility is low
THEN review_mode = decision-gate
```

### Evidence rules

```text
IF pr-open AND evidence missing
THEN state = needs-review
AND signal = evidence-gap
```

```text
IF epic close requested AND merge commit missing
THEN state cannot become done
AND signal = closure-evidence-gap
```

### Learning rules

```text
IF merged work introduces a new reusable concept
THEN recommend /teach lesson or learning artifact
```

```text
IF same misconception appears repeatedly
THEN recommend spaced review or curriculum node
```

### Goodhart rules

```text
IF metric appears without balancing metric
THEN signal = goodhart-risk
AND recommended_action = add anti-goodhart guardrail
```

## Attention heads as signal producers

```text
Value Head      -> business value, outcome, success signal
Hierarchy Head  -> parent/child/related drift
Evidence Head   -> evidence packet, checks, verification horizon
Risk Head       -> reversibility, scope creep, impact
Review Head     -> review mode suggestion
Learning Head   -> /teach candidate, misconception, memory
Capability Head -> agent attestation needed
Goodhart Head   -> metric gaming risk
Drift Head      -> mismatch between issue comments and central maps
```

Each head emits:

```text
head_name
input_artifact
signal
confidence
reason
evidence_links
recommended_action
safe_default
```

## Transition packet

Every transition can be represented as:

```json
{
  "artifact": "owner/repo#123",
  "from_state": "shaped",
  "to_state": "ready",
  "requested_by": "agent-or-human",
  "signals": [],
  "rules_evaluated": [],
  "allowed": true,
  "review_mode": "fast-review",
  "reason": "business value, hierarchy, routing, and evidence are present",
  "safe_default": "hold in shaped if evidence is missing"
}
```

## Implementation path

### Phase 1 — Advisory docs/examples

- Define states and rules.
- Add examples.
- Add methodology guard report sections.
- No blocking behavior.

### Phase 2 — Deterministic checker

- Add machine-readable rules config.
- Add fixtures.
- Emit state suggestions.
- Still non-strict by default.

### Phase 3 — GitHub workflow integration

- Run on issues and PRs.
- Upload reports.
- Optionally comment in batch/digest mode.
- Use labels only after stable.

### Phase 4 — Policy integration

- Demerzel decides which rules become hard gates.
- Human confirms high-impact transitions.
- TARS uses `/teach` for repeated weak areas.
- IX measures false positives, friction, and usefulness.

## Non-goals

- Do not implement a complex BPM system first.
- Do not block PRs before advisory mode is validated.
- Do not let rules replace human architecture or value decisions.
- Do not make labels the source of truth.
- Do not create more review prompts than the anti-rubber-stamp policy allows.

## Related

- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `OPERATING_GATES.md`
- `WORKFLOW_STATE_MACHINE.md`
- `ISSUE_HIERARCHY.md`
- `BUSINESS_VALUE_TREE.md`
- `.github#27`
- `.github#28`
- `.github#29`
