# Methodology Guard

Date: 2026-07-01

The Methodology Guard checks GitHub issue and PR bodies for the minimum structure needed by the GuitarAlchemist operating model.

It is advisory by default.

## Purpose

```text
Reduce issue drift.
Surface missing business value.
Surface missing hierarchy.
Surface missing review mode and routing.
Keep PR evidence visible.
Avoid creating more human review prompts than necessary.
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

Use only after false positives are understood.

## Recommended rollout

```text
1. .github pilot, advisory mode
2. tars pilot, advisory mode
3. ix pilot, advisory mode
4. Demerzel only after rules are stable
5. strict mode only for narrow, low-risk gates
```

## Consumer workflow

Add this to a repo as `.github/workflows/methodology-guard.yml`:

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

## Custom rules

Repos may provide a local rules file and pass it as `rules-path`.

If no file is provided, the action falls back to the central rules:

```text
.github/methodology/rules.yml
```

## Current checks

Issues:

```text
summary
hierarchy
business value
review mode
routing
non-goals
parent
children
related
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
business value
review mode
evidence
acceptance criteria
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
-> rules engine transition recommendation
-> state machine state suggestion
```

Example:

```text
missing business value
-> Value Head signal
-> cannot move from shaped to ready
-> safe default: keep shaping
```

## Related

- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `OPERATING_GATES.md`
- `WORKFLOW_STATE_MACHINE.md`
- `REACT_STATE_MANAGEMENT_ANALOGY.md`
- `.github#27`
- `.github#28`
- `.github#29`
