# Coupling, Decoupling, and Namespace Scoping Principles

Date: 2026-07-01

This document defines how GuitarAlchemist should think about coupling, decoupling, and nested scopes across GitHub workflows, issues, agents, rules, and state machines.

The guiding metaphor is C# namespaces and Russian dolls:

```text
Organization
  -> Repo
    -> Domain
      -> Workflow
        -> Rule pack
          -> Action
            -> Script
              -> Signal
```

Each inner scope may know just enough about its parent contract, but should not depend on unrelated siblings or hidden global state.

## Core thesis

```text
Good architecture is not maximum decoupling.
Good architecture is intentional coupling at the right abstraction boundary.
```

Too much coupling creates brittle workflows.

Too much decoupling creates generic blocks with no useful project semantics.

The goal is:

```text
high cohesion inside a scope
low accidental coupling across scopes
explicit contracts between scopes
```

## Namespace-style model

Use namespace-like naming for conceptual boundaries:

```text
GuitarAlchemist.GitHub.Methodology
GuitarAlchemist.GitHub.Methodology.Rules
GuitarAlchemist.GitHub.Methodology.Checker
GuitarAlchemist.GitHub.Methodology.Actions
GuitarAlchemist.GitHub.Methodology.Workflows
GuitarAlchemist.GitHub.Workflow.StateMachine
GuitarAlchemist.GitHub.Workflow.AttentionHeads
GuitarAlchemist.Demerzel.Policy
GuitarAlchemist.TARS.Teach
GuitarAlchemist.IX.Metrics
```

This gives every artifact a place, owner, and coupling expectation.

## Russian-doll scoping

Each nested level should expose a smaller, clearer contract than its parent.

```text
.github repository
  owns organization-wide methodology assets

methodology guard
  owns methodology section checks

rules.yml
  owns declarative rule lists

checker script
  owns deterministic validation mechanics

composite action
  owns execution packaging

reusable workflow
  owns cross-repo job interface

repo pilot workflow
  owns repo-specific adoption settings
```

## Coupling types

### Good coupling

```text
Workflow depends on composite action contract.
Composite action depends on checker CLI contract.
Checker depends on rules.yml schema.
TARS depends on methodology reports, not workflow internals.
Demerzel depends on state/rules signals, not GitHub YAML details.
```

### Bad coupling

```text
A repo workflow duplicates checker logic.
A label becomes the only source of truth.
A script hardcodes Demerzel policy names.
A GitHub workflow directly decides high-impact architecture transitions.
An attention head mutates issue state instead of emitting a signal.
A template assumes TARS-specific concepts in all repos.
```

## Scoping rules

### Rule 1 — Inner scopes should not know too much

Bad:

```text
check_methodology.py knows all repo names, issue numbers, agent lanes, and Demerzel policy rules.
```

Better:

```text
check_methodology.py validates text structure.
rules.yml defines required fields.
Demerzel evaluates policy.
TARS interprets learning signals.
IX computes metrics.
```

### Rule 2 — Outer scopes should not reach into internals

Bad:

```text
tars workflow calls a private function inside the checker script.
```

Better:

```text
tars workflow calls reusable workflow or composite action contract.
```

### Rule 3 — Derived state should stay derived

React/Jotai analogy:

```text
Do not store derived state as canonical source.
```

GitHub equivalent:

```text
Labels, comments, reports, and attention-head outputs are derived signals.
Issue body, central maps, evidence packets, and lifecycle state carry stronger truth.
```

### Rule 4 — Policy and mechanics should be separate

```text
Mechanics: parse issue body, run workflow, upload report.
Policy: decide whether missing evidence blocks a transition.
```

The Methodology Guard should report missing fields.
Demerzel should decide which missing fields become gates.

### Rule 5 — Stable contract beats clever integration

Prefer:

```text
JSON report contract
Markdown evidence packet
YAML rules config
named lifecycle states
small composite actions
```

Avoid:

```text
implicit conventions hidden in prompts
workflow-specific string parsing
large monolithic scripts
state encoded only in comments
```

## Coupling matrix

| Layer | May depend on | Should not depend on |
|---|---|---|
| rules.yml | methodology vocabulary | repo-specific issue numbers |
| checker script | rules.yml schema | Demerzel policy internals |
| composite action | checker CLI | repo workflows directly |
| reusable workflow | composite action | caller repo internals |
| repo workflow | reusable workflow | checker internals |
| attention heads | report/evidence contracts | workflow YAML details |
| rules engine | signals + lifecycle state | raw GitHub event quirks |
| Demerzel policy | rules/state/evidence contracts | parser implementation details |
| TARS /teach | learning artifacts | GitHub workflow implementation |
| IX metrics | event/report data | issue body formatting details |

## Namespace examples

### Methodology guard namespace

```text
GuitarAlchemist.GitHub.Methodology.Rules
  -> .github/methodology/rules.yml

GuitarAlchemist.GitHub.Methodology.Checker
  -> .github/scripts/check_methodology.py

GuitarAlchemist.GitHub.Methodology.Action
  -> .github/actions/methodology-guard/action.yml

GuitarAlchemist.GitHub.Methodology.Workflow
  -> .github/workflows/methodology-guard.yml
```

### Workflow intelligence namespace

```text
GuitarAlchemist.GitHub.Workflow.AttentionHeads.Value
GuitarAlchemist.GitHub.Workflow.AttentionHeads.Evidence
GuitarAlchemist.GitHub.Workflow.AttentionHeads.Review
GuitarAlchemist.GitHub.Workflow.AttentionHeads.Drift
```

### Governance namespace

```text
GuitarAlchemist.Demerzel.Policy.ObjectiveStack
GuitarAlchemist.Demerzel.Policy.ReviewModes
GuitarAlchemist.Demerzel.Lifecycle.IssueLifecycle
GuitarAlchemist.Demerzel.Lifecycle.PullRequestLifecycle
```

## Package boundary heuristic

A block deserves its own file, action, rule pack, or namespace when:

```text
it has a distinct owner
it changes for a distinct reason
it can be tested independently
it can be reused by two or more workflows
it produces a stable output contract
it hides implementation detail from callers
```

A block should stay inline when:

```text
it is used once
it has no stable contract yet
extracting it would hide important context
it is still exploratory
```

## Scoping by maturity

```text
rough idea
  -> issue comment or research note

repeated pattern
  -> template block

reused in two places
  -> helper script or composite action

cross-repo use
  -> reusable workflow

governance-critical
  -> Demerzel policy/rule pack

measurable/reported
  -> IX metric contract

teachable/repeated confusion
  -> TARS /teach lesson
```

## Anti-patterns

```text
Global everything
One workflow owns parsing, policy, state, labels, comments, and learning
Copy-paste workflow logic across repos
Labels treated as canonical truth
Rules hidden in prose only
Over-abstracting before a second use case
Under-abstracting after three repeated uses
Agent prompts depending on private implementation details
```

## Practical rule

Before extracting a block, ask:

```text
What contract will this block expose?
Who owns it?
What is allowed to depend on it?
What must not know it exists?
What signal proves the abstraction is useful?
```

## Related

- `WORKFLOW_COMPOSABILITY_PRINCIPLES.md`
- `REACT_STATE_MANAGEMENT_ANALOGY.md`
- `WORKFLOW_STATE_MACHINE.md`
- `METHODOLOGY_GUARD.md`
- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `.github#28`
- `.github#29`
- `Demerzel#588`
- `Demerzel#592`
