# Operating Gates

Date: 2026-07-01

This document defines lightweight gates for GuitarAlchemist issues, PRs, epics, and agentic work.

The goal is to improve quality without adding heavy bureaucracy.

## Gate 0 — Rough idea

Use when a thought is not ready for structured work.

Allowed missing fields:

```text
parent
business value
metric
review mode
```

Required fields:

```text
source/context
why it might matter
open questions
next clarification step
```

Exit condition:

```text
Converted to a structured issue or explicitly deferred.
```

## Gate 1 — Issue ready

An issue is ready for work when it has:

```text
clear outcome
parent or root reason
business value
success signal
risk if ignored
acceptance criteria
non-goals
routing lane
review mode
expected evidence
```

If any of these are missing, classify the issue as shaping/research, not ready for execution.

## Gate 2 — Delegation ready

An issue is ready for Jules/Claude/Codex when it has:

```text
narrow scope
explicit artifacts to change
non-goals
agent lane
stop condition
review expectation
```

Agent routing:

```text
Jules  = docs/examples/templates/evidence artifacts
Claude = critique, decomposition, architecture review support
Codex  = isolated validation/prototype/test fixture
Human  = architecture, value, priority, responsibility, high-impact decisions
```

## Gate 3 — PR ready for review

A PR is ready for review when it has:

```text
linked issue
scope summary
business value statement
evidence packet or evidence section
changed files summary
risk/reversibility note
review mode
checks or validation notes
follow-up issues if scope was split
```

## Gate 4 — PR ready to merge

A PR is ready to merge when:

```text
scope matches issue
review mode is appropriate
evidence is sufficient
no hidden high-impact changes
non-goals respected
risk is acceptable
follow-ups exist for remaining scope
```

Docs/examples/templates PRs may use `fast-review` if they are narrow and reversible.

Architecture, workflow, runtime, or governance boundary changes require at least `focused-review`, and often `decision-gate`.

## Gate 5 — Epic ready to close

An epic is ready to close when:

```text
implemented PRs are linked
merge commits are recorded
children are closed or intentionally deferred
business value outcome is reviewed
remaining gaps are captured as follow-ups
retrospective or learning artifact exists if useful
ISSUE_HIERARCHY.md is current
BUSINESS_VALUE_TREE.md is current
```

## Gate 6 — Learning captured

A completed meaningful work item should produce at least one of:

```text
retrospective
pattern
anti-pattern
/teach lesson or session
memory update
capability attestation update
evidence packet
```

## Blockers

Do not proceed to execution if:

```text
business value is unclear
scope is too broad
review mode is missing
expected evidence is missing
parent/child relationship is ambiguous
risk is high and no human decision question is stated
```

## Fast path

A small docs-only PR may proceed quickly if:

```text
scope is narrow
reversible
linked to an issue
business value is clear
evidence is visible
no workflow/runtime/governance boundary changes
```

## Anti-patterns

```text
large issue with no outcome
PR with no linked issue
benchmark with no project use case
lesson with no mastery check
metric with no anti-Goodhart guardrail
agent claim with no evidence
closed epic with no implementation evidence
```

## Related

- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `ISSUE_HIERARCHY.md`
- `BUSINESS_VALUE_TREE.md`
- `MEMORY.md`
- `.github#27`
