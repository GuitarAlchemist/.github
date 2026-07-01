# Methodology Guard

Date: 2026-07-01

The Methodology Guard checks GitHub issue and PR bodies for the minimum structure needed by the GuitarAlchemist operating model.

It is advisory by default.

## Current status

```text
pilot
non-strict
artifact-only
no auto-comments
no blocking
```

The guard is not yet an organization-wide policy authority.

## Purpose

```text
Reduce issue drift.
Surface missing business value.
Surface missing hierarchy.
Surface missing scope/boundary information.
Surface missing review mode and routing.
Keep PR evidence visible.
Avoid creating more human review prompts than necessary.
```

## Boundary rule

```text
.github = mechanism
Demerzel = policy
TARS = judgment / reasoning
IX = measurement
```

Therefore:

```text
Methodology Guard may report missing fields.
Demerzel decides which missing fields become policy gates.
TARS interprets methodology findings in triage/review reasoning.
IX measures false positives, review friction, and usefulness.
Human decides high-impact promotion or blocking behavior.
```

## Architecture

```text
rules.yml
  -> check_methodology.py
  -> composite action
  -> reusable workflow
  -> org workflow template
  -> optional per-repo pilot workflow
```

Files:

```text
.github/methodology/rules.yml
.github/scripts/check_methodology.py
.github/actions/methodology-guard/action.yml
.github/workflows/methodology-guard.yml
workflow-templates/methodology-guard.yml
workflow-templates/methodology-guard.properties.json
.github/workflows/methodology-guard-pilot.yml
.github/workflows/methodology-guard-self-test.yml
tests/methodology/*
```

## Versioning rule

Pilot consumers may use `@main` only while all of these are true:

```text
advisory
non-strict
artifact-only
no auto-comments
no blocking
explicitly marked as pilot
```

Stable consumers should use a version tag or pinned SHA:

```yaml
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@v1
```

or, for high-sensitivity consumers:

```yaml
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@<commit-sha>
```

Do not treat `@main` as stable behavior.

## Modes

### Advisory mode

```yaml
strict: false
```

Use for pilots and repo rollout.

### Strict mode

```yaml
strict: true
```

Use only after false positives are understood and Demerzel policy gates are explicit.

## Promotion gates

Do not promote Methodology Guard from pilot to stable org behavior until:

```text
live multiline issue/PR bodies are confirmed
false positives are reviewed
at least two repo pilots have produced artifacts
version tag exists
rollback path exists
policy/mechanism boundary is explicit
Demerzel owns any policy semantics
IX owns measurement criteria for usefulness/noise
```

## Recommended rollout

```text
1. .github pilot, advisory mode
2. tars pilot, advisory mode
3. Review artifacts and false positives
4. Create version tag only after pilot evidence
5. ix pilot, advisory mode, only after stable enough
6. Demerzel only after rules are stable and policy boundary is clarified
7. strict mode only for narrow, low-risk Demerzel-approved gates
```

## Consumer workflow — pilot only

Add this to a repo as `.github/workflows/methodology-guard.yml` while piloting:

```yaml
name: Methodology Guard

on:
  issues:
    types: [opened, edited, reopened]
  pull_request:
    types: [opened, edited, reopened, synchronize, ready_for_review]

permissions:
  contents: read
  issues: read
  pull-requests: read

concurrency:
  group: methodology-guard-${{ github.event_name }}-${{ github.event.issue.number || github.event.pull_request.number || github.run_id }}
  cancel-in-progress: true

jobs:
  issue-methodology:
    name: Issue methodology
    if: github.event_name == 'issues'
    uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@main
    with:
      kind: issue
      title: ${{ github.event.issue.title }}
      body: ${{ github.event.issue.body || '' }}
      strict: false

  pr-methodology:
    name: PR methodology
    if: github.event_name == 'pull_request'
    uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@main
    with:
      kind: pr
      title: ${{ github.event.pull_request.title }}
      body: ${{ github.event.pull_request.body || '' }}
      strict: false
```

Once promoted, replace `@main` with a version tag or SHA.

## Custom rules

Repos may provide a local rules file and pass it as `rules-path`.

If no file is provided, the action falls back to the central pilot checklist:

```text
.github/methodology/rules.yml
```

Important:

```text
This rules file is a mechanical checklist during pilot.
If rules become governance semantics, ownership should move to Demerzel.
```

## Current checks

Issues:

```text
summary
hierarchy
scope / boundary
business value
review mode
routing
non-goals
parent
children
related
namespace
owner scope
in scope
out of scope
allowed dependencies
forbidden dependencies
contract exposed
outcome
value hypothesis
who benefits
how we know it worked
risk if ignored
```

PRs:

```text
summary
linked issue
scope
boundary contract
business value
review mode
evidence
acceptance criteria
namespace affected
contract changed
expected dependencies touched
dependencies intentionally avoided
derived state kept derived
```

Research notes:

```text
[Research]
type:research
research note
```

Research notes bypass full structured readiness checks because they are intentionally not execution-ready.

## Outputs

```text
methodology-guard.md
methodology-guard.json
```

These are uploaded as workflow artifacts.

## Anti-spam rule

Do not auto-comment every finding at first.

Recommended progression:

```text
Phase 1: artifact only
Phase 2: batch digest
Phase 3: comments only for focused-review / decision-gate
Phase 4: strict blocking only for narrow stable cases
```

## Relationship to state machines

The guard currently detects missing methodology blocks.

Future evolution:

```text
missing block
-> attention head signal
-> TARS triage interpretation
-> IX usefulness/noise metrics
-> Demerzel policy transition recommendation
-> state machine state suggestion
```

Example:

```text
missing business value
-> Value Head signal
-> TARS explains why work is not ready
-> IX records whether this finding was useful
-> Demerzel may decide shaped cannot move to ready
-> safe default: keep shaping
```

## Non-goals

```text
Do not make .github the policy authority.
Do not block PRs until pilot evidence exists.
Do not auto-comment findings during pilot.
Do not treat @main imports as stable.
Do not mutate labels/issues from attention-head signals.
Do not hide raw evidence behind summary reports.
```

## Related

- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `OPERATING_GATES.md`
- `WORKFLOW_STATE_MACHINE.md`
- `REACT_STATE_MANAGEMENT_ANALOGY.md`
- `ENGINEERING_PRINCIPLES.md`
- `ARCHITECTURE_AUDIT_RESPONSE_2026-07-01.md`
- `.github#27`
- `.github#28`
- `.github#29`
- `.github#30`
- `Demerzel#588`
- `Demerzel#592`
