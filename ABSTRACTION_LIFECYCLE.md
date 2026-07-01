# Abstraction Lifecycle Pipeline

Date: 2026-07-01

This document defines how GuitarAlchemist should collect, incubate, apply, evaluate, promote, and retire abstractions.

## Core thesis

```text
Abstractions should be earned, not guessed.
```

A useful abstraction usually emerges from repeated concrete work. The workflow should collect candidates automatically, incubate them safely, apply them in narrow contexts, and only promote them when they reduce friction without hiding important evidence.

## Why this matters

Without an abstraction lifecycle:

```text
patterns stay buried in issues and PRs
copy-paste spreads across repos
useful concepts never become reusable blocks
bad abstractions become permanent
agents over-generalize too early
humans lose visibility into why a block exists
```

With an abstraction lifecycle:

```text
repeated patterns are captured
weak abstractions stay in incubation
stable abstractions become templates/actions/rules
failed abstractions can be retired
TARS can teach recurring concepts
IX can measure usefulness
Demerzel can govern promotion gates
```

## Lifecycle

```text
observed
-> candidate
-> incubating
-> trial
-> promoted
-> applied
-> evaluated
-> generalized
-> retired | superseded
```

## State definitions

### observed

A pattern appears once in an issue, PR, retrospective, review, or conversation.

Examples:

```text
repeated missing business value
same review-mode confusion
same docs-only PR evidence format
same GitHub workflow shape
same TARS /teach misconception
```

### candidate

The pattern appears important enough to capture.

Required:

```text
source artifacts
repeated context or expected reuse
problem solved
scope boundary
```

### incubating

The abstraction is documented but not enforced.

Allowed forms:

```text
research note
template draft
example JSON
manual checklist
advisory report
```

### trial

The abstraction is used in one or two low-risk workflows or issues.

Required:

```text
pilot scope
safe default
rollback path
success signal
false-positive watch
```

### promoted

The abstraction becomes a reusable block.

Allowed forms:

```text
template
rules.yml entry
composite action
reusable workflow
attention head
state-machine transition
Demerzel policy rule
TARS /teach lesson
IX metric
```

### applied

The abstraction is installed or used across one or more repos/workflows.

Required:

```text
consumer list
version/reference
usage guide
owner
```

### evaluated

Usefulness is checked after real usage.

Signals:

```text
reduced review friction
fewer repeated comments
fewer missing sections
fewer false positives
clearer evidence packets
better review-mode routing
learning/memory reuse
```

### generalized

The abstraction proves useful across domains and is made more generic.

Gate:

```text
used successfully in at least two scopes
contract is stable
false positives are acceptable
business value is clear
```

### retired / superseded

The abstraction is removed, replaced, or downgraded.

Triggers:

```text
too noisy
unused
wrong abstraction boundary
hides important evidence
creates review friction
superseded by better block
```

## Automatic collection sources

```text
GitHub issues
GitHub PRs
methodology-guard reports
post-merge retrospectives
evidence packets
review comments
TARS /teach sessions
IX metrics
Demerzel policy decisions
MEMORY.md lessons
```

## Abstraction heads

These are specialized attention heads for abstraction management.

```text
Pattern Head
  detects repeated phrases, structures, missing blocks, review friction

Duplication Head
  detects repeated workflow YAML, templates, issue text, comments

Boundary Head
  detects unclear scope, hidden coupling, bad namespace placement

Promotion Head
  detects candidates that appear stable enough to become reusable blocks

Retirement Head
  detects abstractions that are noisy, unused, or harmful

Teaching Head
  detects concepts that should become /teach lessons

Metric Head
  detects abstractions that need IX usefulness metrics

Policy Head
  detects abstractions that need Demerzel gates or review modes
```

## Abstraction candidate contract

```json
{
  "abstraction_id": "",
  "name": "",
  "status": "observed | candidate | incubating | trial | promoted | applied | evaluated | generalized | retired | superseded",
  "namespace": "",
  "source_artifacts": [],
  "problem": "",
  "proposed_block_type": "template | rule | action | workflow | attention-head | state-transition | policy | teach-lesson | metric",
  "owner_scope": "",
  "allowed_dependencies": [],
  "forbidden_dependencies": [],
  "contract_exposed": "",
  "success_signal": "",
  "risk_if_wrong": "",
  "safe_default": "",
  "promotion_gate": "",
  "retirement_gate": ""
}
```

## Promotion gates

Do not promote an abstraction unless:

```text
problem is real
source artifacts exist
scope is explicit
owner is clear
contract is explicit
safe default exists
at least one fixture/example exists
business value is clear
review mode is appropriate
false-positive risk is acceptable
```

## Anti-premature-abstraction guardrails

```text
Do not extract after one occurrence unless risk is high.
Do not generalize before a second use case.
Do not enforce before advisory mode is tested.
Do not hide evidence behind a clean summary.
Do not turn every pattern into a workflow.
Do not promote a block without a retirement path.
```

## Application loop

```text
1. Observe pattern.
2. Capture candidate.
3. Incubate as docs/template/example.
4. Trial in low-risk scope.
5. Evaluate usefulness.
6. Promote if useful.
7. Apply wider.
8. Retire or refine if noisy.
9. Teach or memorize if recurring.
```

## Integration with current architecture

```text
Methodology Guard
  emits missing-section and boundary signals

Attention Heads
  detect repeated signals and candidate abstractions

Rules Engine
  evaluates candidate promotion/retirement gates

State Machine
  tracks abstraction lifecycle state

Demerzel
  governs high-impact promotions or policy gates

TARS
  turns recurring concepts into /teach lessons and memory

IX
  measures usefulness, friction, false positives, and reuse
```

## Minimal GitHub implementation

Start with docs and examples only:

```text
templates/abstraction-candidate-template.md
examples/abstractions/abstraction-registry.example.json
ABSTRACTION_LIFECYCLE.md
```

Later automation:

```text
abstraction-candidate report artifact
weekly abstraction digest
promotion recommendation
retirement recommendation
/teach lesson suggestion
```

## Related

- `WORKFLOW_COMPOSABILITY_PRINCIPLES.md`
- `COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md`
- `REACT_STATE_MANAGEMENT_ANALOGY.md`
- `WORKFLOW_STATE_MACHINE.md`
- `METHODOLOGY_GUARD.md`
- `.github#28`
- `.github#29`
- `Demerzel#588`
- `Demerzel#592`
