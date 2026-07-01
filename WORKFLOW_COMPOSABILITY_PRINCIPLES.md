# Workflow Composability Principles

Date: 2026-07-01

This document captures the "Lego block" architecture for maintainable GitHub workflows.

## Core thesis

```text
Composable workflow systems are built from small blocks with explicit contracts.
```

Each block should do one thing, expose clear inputs/outputs, and be safe to reuse in different workflows.

## Why this matters

Large workflows become brittle when they mix:

```text
trigger logic
policy logic
state transitions
text parsing
business value checks
evidence reporting
side effects
comments
labels
agent prompts
```

The maintainable approach is to separate these concerns.

## Lego block stack

```text
Rules config
  -> declarative expected sections/fields

Checker script
  -> deterministic validation engine

Composite action
  -> reusable execution unit

Reusable workflow
  -> cross-repo job interface

Workflow template
  -> installable repo-level adapter

Pilot workflow
  -> repo-specific advisory adoption

Reports/artifacts
  -> durable outputs without notification spam

Attention heads
  -> derived signal extractors

Rules engine
  -> transition recommendations

State machine
  -> canonical lifecycle state

Demerzel policy
  -> governance boundaries

Human review
  -> final authority for high-impact decisions
```

## Design principle: single reason to change

Each layer should have one main reason to change.

```text
rules.yml changes when methodology expectations change
check_methodology.py changes when validation mechanics change
composite action changes when execution packaging changes
reusable workflow changes when GitHub job interface changes
workflow template changes when repo rollout policy changes
state machine changes when lifecycle semantics change
attention heads change when derived signal taxonomy changes
```

## Inputs and outputs

Every block should document:

```text
inputs
outputs
side effects
safe defaults
failure mode
review mode
owner
```

## Source of truth layering

```text
Issue/PR body      = intent, acceptance criteria, local context
Rules config       = methodology contract
Workflow reports   = derived diagnostics
Central maps       = cross-repo structure and value
State machine      = lifecycle state
Evidence packet    = review/audit proof
Memory             = operational lessons
```

Do not make labels or comments the only source of truth.

## Avoid hidden coupling

Bad:

```text
Workflow hardcodes sections, state names, labels, and policy decisions inline.
```

Better:

```text
Workflow calls a composite action.
Composite action calls a script.
Script reads rules.
Rules produce a report.
A later state machine consumes the report.
```

## Adoption levels

### Level 0 — Documentation only

Templates and docs describe expectations.

### Level 1 — Advisory artifact

Workflow emits a report artifact. No comments. No blocking.

### Level 2 — Digest

Findings are batched into a digest.

### Level 3 — Targeted comments

Only focused-review or decision-gate findings create comments.

### Level 4 — Strict checks

Only stable low-noise gates become blocking.

## React/Jotai analogy

```text
rules.yml                  = store configuration
issue/PR body              = source atoms
attention heads            = derived atoms/selectors
rules engine               = reducer / transition function
GitHub Actions             = effects
methodology reports        = devtools/audit snapshot
state machine              = canonical app state
```

## Good composable block checklist

```text
Small scope?
Clear input contract?
Clear output contract?
No hidden side effect?
Safe default?
Reusable from at least two workflows?
Test fixture exists?
Failure mode is visible?
Can be replaced without rewriting the whole system?
```

## Anti-patterns

```text
Copy-pasted workflow logic
Inline scripts with duplicated rules
Labels as hidden source of truth
Auto-comments for every warning
Strict blocking before false positives are known
One workflow doing parsing, policy, state, comments, and labels
No versioning strategy for reusable workflow calls
No fixtures for workflow behavior
```

## Recommended next refinements

```text
1. Keep methodology guard advisory.
2. Add state suggestion to report JSON.
3. Add attention-head signal objects.
4. Add small fixtures for each signal type.
5. Promote stable signals into rules engine checks.
6. Only later consider labels/comments/strict gates.
```

## Related

- `METHODOLOGY_GUARD.md`
- `WORKFLOW_STATE_MACHINE.md`
- `REACT_STATE_MANAGEMENT_ANALOGY.md`
- `OPERATING_GATES.md`
- `.github#28`
- `.github#29`
- `Demerzel#588`
- `Demerzel#592`
