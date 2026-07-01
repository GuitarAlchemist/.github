# Architecture Audit Response

Date: 2026-07-01

Source: external model critique session, captured as corrective architecture input.

## Executive takeaway

The audit is useful because it identifies the central risk of the current operating system work:

```text
The governance/process layer may grow faster than the product/runtime layer it is supposed to help.
```

This report converts the critique into concrete architecture corrections.

## Accepted corrections

### 1. .github must remain mechanism, not policy owner

Rule:

```text
.github = mechanism
Demerzel = policy
TARS = judgment/reasoning
IX = metrics
```

Implication:

```text
.github may host reusable workflows, composite actions, templates, and adapters.
.github should not become the canonical owner of policy semantics.
```

Policy-like artifacts created in `.github` should either:

```text
1. remain explicitly advisory, or
2. be migrated/synced into Demerzel when they become governance semantics.
```

### 2. Explicit imports beat implicit inheritance

The namespace/Russian-doll model is useful pedagogically, but GitHub does not provide rich inheritance semantics.

Rule:

```text
Every repo should explicitly declare what workflow/action/rule pack it imports and at what version.
```

Avoid:

```text
silent inheritance
unversioned org-wide behavior
hidden policy resolution
```

Prefer:

```text
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@v1
rules_ref: GuitarAlchemist/Demerzel/...@v1
```

### 3. Methodology Guard should stay pilot/advisory until proven

The guard is useful, but it should not be treated as an org standard until artifacts from `.github` and `tars` have been reviewed.

Current safe rule:

```text
artifact-only
non-strict
no auto-comments
no blocking
```

Promotion gates:

```text
- live multiline bodies confirmed
- false positives reviewed
- at least two repo pilots observed
- version tag available
- ownership split clarified between .github and Demerzel
```

### 4. Abstraction lifecycle is useful only as a brake, not acceleration

The abstraction pipeline must prevent premature abstraction, not create more process.

Rule:

```text
No org-level promotion without concrete reuse evidence.
```

Suggested gate:

```text
promote to org reusable block only after at least two real consumers or one high-risk repeated failure.
```

### 5. Under-abstraction in agent/config/workflow setup is real

Observed duplication candidates:

```text
- skills configuration across repos
- auto-compact / agent settings across repos
- auth / @claude / cost-safety conventions
- daily snapshot workflows in GA
```

These are better candidates for reusable blocks than additional meta-governance docs.

## Boundary corrections

### .github

Owns:

```text
workflow adapters
composite actions
repo templates
report artifacts
mechanical checks
installation templates
```

Should not own long-term:

```text
policy semantics
promotion/retirement authority
human decision gates
business value theory
lifecycle truth
```

### Demerzel

Owns:

```text
policy semantics
review modes
state-machine semantics
business value governance
promotion/retirement gates
human decision gates
```

### TARS

Owns:

```text
triage reasoning
intent verification
teach-back and learning artifacts
interpretive summaries
second-brain promotion
```

### IX

Owns:

```text
scores
metrics
drift baselines
false-positive rates
review-friction metrics
reuse/usefulness measurements
```

## Hidden coupling risks to track

```text
1. Markdown and commit-message contracts without schemas.
2. .github becoming a god repo.
3. Unpinned shared agent/model/prompt behavior across repos.
4. Temporal coupling among GA daily snapshots.
5. Budget/auth split between demerzel-bot and TARS.
```

## Corrective backlog

### P0

```text
- Keep Methodology Guard non-strict.
- Do not install in Demerzel until .github/tars artifacts are reviewed.
- Add versioning plan for reusable workflows/actions.
- Add explicit import policy: no silent inheritance.
```

### P1

```text
- Create a contract for .github consuming Demerzel policy/rules.
- Move policy semantics out of .github docs once stable.
- Identify duplicated agent/skills/config snippets across repos.
- Create reusable action/template for shared agent config only after second confirmed consumer.
```

### P2

```text
- Create IX metrics for abstraction usefulness.
- Add TARS /teach lesson for over-abstraction vs under-abstraction.
- Add Demerzel promotion gates for workflow abstractions.
```

## Simplified architecture after audit

```text
.github
  = how checks/workflows run

Demerzel
  = what policies/states mean

TARS
  = why a triage/recommendation makes sense

IX
  = how well it worked

Human
  = whether high-impact changes proceed
```

## Things to explicitly not do

```text
Do not make the abstraction lifecycle a blocking process.
Do not let .github become policy authority.
Do not spread @main reusable workflows without version tags forever.
Do not auto-comment every methodology finding.
Do not generalize React/Jotai semantics beyond pedagogical use.
Do not treat labels/comments as canonical state.
Do not create a second governance stack parallel to Demerzel.
```

## Decision

This audit should be treated as a course correction.

Immediate implementation principle:

```text
Shrink policy ownership in .github.
Strengthen versioned mechanical contracts in .github.
Move governance semantics toward Demerzel.
Move interpretation toward TARS.
Move scoring toward IX.
```

## Related

- `.github#28`
- `.github#30`
- `.github#31`
- `Demerzel#588`
- `Demerzel#592`
- `TARS#162`
- `TARS#163`
- `IX#216`
- `IX#217`
- `IX#218`
