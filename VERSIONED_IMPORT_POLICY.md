# Versioned Import Policy

Date: 2026-07-01

This document defines how GuitarAlchemist repositories should consume shared `.github` workflows, composite actions, templates, rule packs, and policy inputs.

## Core rule

```text
Explicit imports beat implicit inheritance.
```

A repository must declare what it imports, where it imports it from, and which version or ref it uses.

Do not rely on silent organization-wide behavior.

## Why

GitHub does not provide rich, debuggable inheritance semantics for cross-repo policy.

If shared workflows or rule packs behave like hidden global state, it becomes unclear:

```text
which policy applied
which version applied
why a workflow changed behavior
which repo accepted the change
how to roll back safely
```

Therefore:

```text
No hidden inheritance.
No silent policy rollout.
No permanent @main consumption for stable cross-repo behavior.
```

## Allowed import classes

### Pilot imports

Allowed during experimentation:

```yaml
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@main
```

Constraints:

```text
advisory only
non-strict
artifact-only
no blocking
no auto-comments
explicitly marked as pilot
```

### Stable imports

Preferred once a shared block is proven:

```yaml
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@v1
```

or a pinned commit SHA for high-sensitivity workflows:

```yaml
uses: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@<commit-sha>
```

### Policy/rule imports

Policy semantics should be versioned separately from workflow mechanics.

Preferred direction:

```text
.github workflow/action = mechanism
Demerzel rule/policy pack = semantics
```

A consumer should be able to say:

```yaml
workflow_ref: GuitarAlchemist/.github/.github/workflows/methodology-guard.yml@v1
policy_ref: GuitarAlchemist/Demerzel/path/to/policy-pack@v1
mode: advisory
```

## Ownership split

```text
.github
  owns reusable workflow mechanics, composite actions, templates, adapters, and report upload.

Demerzel
  owns policy semantics, lifecycle states, promotion gates, review modes, and human decision rules.

TARS
  owns reasoning, triage interpretation, intent verification, and /teach learning artifacts.

IX
  owns metrics, scoring, drift baselines, false-positive rates, review-friction measurements, and usefulness scoring.
```

## Promotion from pilot to stable

A shared import may move from `@main` pilot to `@v1` stable only when:

```text
at least two real consumer repos have run it in advisory mode
false positives have been reviewed
multiline issue/PR bodies are confirmed in live workflows
a rollback path exists
owner scope is explicit
policy vs mechanism boundary is clear
version tag is created
```

## Bump policy

Consumers should update shared imports intentionally.

Recommended flow:

```text
1. Shared block publishes v1.
2. Consumer repo opens a PR bumping @main or old tag to @v1.
3. PR includes evidence from advisory runs.
4. Human approves high-impact bumps.
5. Rollback is possible by reverting the ref.
```

## Anti-patterns

```text
Permanent @main consumption for stable behavior.
Hidden org-wide workflow behavior.
Policy semantics embedded only inside .github workflows.
Markdown prose as an unversioned machine contract.
Labels/comments as the only lifecycle state.
Bulk updates across repos without pilot evidence.
```

## Current status

Methodology Guard is still a pilot.

Safe default:

```text
Keep pilots on @main only while non-strict, advisory, artifact-only.
Do not install in Demerzel until .github and tars artifacts are reviewed.
Do not create a stable @v1 until promotion gates are satisfied.
```

## Related

- `METHODOLOGY_GUARD.md`
- `ABSTRACTION_LIFECYCLE.md`
- `COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md`
- `ARCHITECTURE_AUDIT_RESPONSE_2026-07-01.md`
- `.github#28`
- `.github#30`
- `Demerzel#588`
- `Demerzel#592`
