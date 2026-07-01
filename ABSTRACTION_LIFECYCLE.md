# Abstraction Lifecycle Pipeline

Date: 2026-07-01

This document defines how GuitarAlchemist should collect, incubate, trial, evaluate, promote, apply, generalize, reject, quarantine, deprecate, and retire abstractions.

## Core thesis

```text
Abstractions should be earned, not guessed.
```

The abstraction lifecycle exists primarily as a brake against premature abstraction.

It must not become a process factory.

A useful abstraction usually emerges from repeated concrete work. The workflow should capture candidates, incubate them safely, apply them in narrow contexts, measure their usefulness, and only promote them when they reduce friction without hiding important evidence.

## Anti-usine-a-gaz rule

```text
The governance/process layer must not grow faster than the product/runtime layer it is supposed to help.
```

Therefore:

```text
No org-level promotion without concrete reuse evidence.
No blocking abstraction process before advisory evidence.
No new abstraction machinery unless it removes more friction than it adds.
```

## Ownership boundary

```text
.github   = mechanism, templates, reusable workflows, reports
Demerzel  = policy semantics, lifecycle gates, promotion/retirement authority
TARS      = reasoning, triage interpretation, /teach and second-brain learning
IX        = usefulness metrics, false positives, review friction, reuse scoring
Human     = final authority for high-impact promotions
```

`.github` may host this document while the process is being shaped, but governance semantics should migrate to Demerzel once stable.

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

With a disciplined lifecycle:

```text
repeated patterns are captured
weak abstractions stay in incubation
stable abstractions become templates/actions/rules
failed abstractions can be rejected, quarantined, retired, or superseded
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
-> evaluated
-> promoted
-> applied
-> generalized

alternative exits:
-> rejected
-> quarantined
-> deprecated
-> sunset
-> retired
-> superseded
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

Allowed action:

```text
capture note only
no extraction unless risk is high
```

### candidate

The pattern appears important enough to capture.

Required:

```text
source artifacts
repeated context or plausible reuse
problem solved
scope boundary
owner hypothesis
```

Allowed action:

```text
open candidate note or fill abstraction-candidate template
no enforcement
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

Required:

```text
safe default
non-goal list
retirement path
```

### trial

The abstraction is used in one or two low-risk workflows or issues.

Required:

```text
pilot scope
explicit import/version/ref
safe default
rollback path
success signal
false-positive watch
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
less copy-paste
```

IX should own the measurement model.

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

Promotion requires evidence.

Minimum gate:

```text
at least two real consumers
or one high-risk repeated failure
or explicit human decision that the value justifies early promotion
```

### applied

The abstraction is installed or used across one or more repos/workflows.

Required:

```text
consumer list
version/reference
usage guide
owner
rollback path
```

### generalized

The abstraction proves useful across domains and is made more generic.

Gate:

```text
used successfully in at least two scopes
contract is stable
false positives are acceptable
business value is clear
policy/mechanism boundary is explicit
```

### rejected

The abstraction is intentionally not pursued.

Required:

```text
rationale
source artifacts
what would change the decision
```

Purpose:

```text
avoid rediscovering and relitigating the same idea repeatedly
```

### quarantined

The abstraction caused harm, noise, false positives, or unclear behavior after trial/adoption.

Required:

```text
affected consumers
failure mode
rollback action
retest condition
```

### deprecated

The abstraction still exists but should not be adopted by new consumers.

Required:

```text
replacement path
sunset target
current consumers
```

### sunset

The abstraction is scheduled for removal.

Required:

```text
removal criteria
migration checklist
owner approval
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

Collection should create advisory artifacts only until a human approves promotion gates.

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

Safe default:

```text
Heads emit signals only.
They do not mutate issues, labels, policy state, or workflow behavior.
```

## Abstraction candidate contract

```json
{
  "abstraction_id": "",
  "name": "",
  "status": "observed | candidate | incubating | trial | evaluated | promoted | applied | generalized | rejected | quarantined | deprecated | sunset | retired | superseded",
  "namespace": "",
  "source_artifacts": [],
  "problem": "",
  "proposed_block_type": "template | rule | action | workflow | attention-head | state-transition | policy | teach-lesson | metric",
  "owner_scope": "",
  "allowed_dependencies": [],
  "forbidden_dependencies": [],
  "contract_exposed": "",
  "success_signal": "",
  "ix_metric": "",
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
policy/mechanism boundary is explicit
versioning plan exists
rollback path exists
```

Org-level reusable blocks require:

```text
at least two real consumer repos
or one high-risk repeated failure
or explicit human exception
```

## Anti-premature-abstraction guardrails

```text
Do not extract after one occurrence unless risk is high.
Do not generalize before a second use case.
Do not enforce before advisory mode is tested.
Do not hide evidence behind a clean summary.
Do not turn every pattern into a workflow.
Do not promote a block without a retirement path.
Do not use this lifecycle to justify more process than the work needs.
Do not let .github become policy authority.
```

## Application loop

```text
1. Observe pattern.
2. Capture candidate.
3. Incubate as docs/template/example.
4. Trial in low-risk scope.
5. Evaluate usefulness with IX-style signals.
6. Promote only if evidence supports it.
7. Apply wider through explicit versioned imports.
8. Retire, quarantine, or refine if noisy.
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
  owns policy semantics and high-impact promotion gates

TARS
  turns recurring concepts into /teach lessons and triage reasoning artifacts

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

Later automation, only after evidence:

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
- `VERSIONED_IMPORT_POLICY.md`
- `ARCHITECTURE_AUDIT_RESPONSE_2026-07-01.md`
- `.github#28`
- `.github#29`
- `.github#30`
- `Demerzel#588`
- `Demerzel#592`
