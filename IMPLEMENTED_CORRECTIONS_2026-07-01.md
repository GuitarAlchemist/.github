# Implemented Architecture Corrections

Date: 2026-07-01

## Summary

Architecture corrections were applied after external critique identified over-abstraction and `.github` policy ownership risk.

## Files changed in `.github`

```text
VERSIONED_IMPORT_POLICY.md
ABSTRACTION_LIFECYCLE.md
COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md
METHODOLOGY_GUARD.md
examples/abstractions/abstraction-registry.example.json
FABLE5_CORRECTION_REPORT_2026-07-01.md
```

## Files added to responsibility-owner repos

```text
Demerzel/docs/policy/workflow-policy-pack-contract.md
ix/docs/metrics/methodology-guard-usefulness-metrics.md
tars/docs/triage/methodology-guard-triage-reasoning.md
```

## Core corrected split

```text
.github   = mechanism
Demerzel  = policy
TARS      = judgment / reasoning
IX        = measurement
Human     = final authority
```

## Guardrails now encoded

```text
Explicit imports beat implicit inheritance.
@main is pilot-only, not stable behavior.
Abstraction lifecycle is a brake, not an accelerator.
No org-level promotion without concrete reuse evidence.
Methodology Guard remains advisory/non-strict/artifact-only.
.github must not become a second Demerzel.
```

## Remaining follow-ups

```text
Create version tag once pilot evidence exists.
Review Methodology Guard artifacts from .github and tars.
Decide whether IX should become next pilot after evidence review.
Use Demerzel policy pack contract before any strict gate.
Use IX metrics before promoting guard behavior.
Use TARS triage reasoning before human review escalation.
Return to GA product incident ga#493.
```
