# Fable 5 Correction Report

Date: 2026-07-01

Purpose: report back to Fable 5 after applying architecture corrections from its audit.

## Summary

The audit was accepted as a course correction.

Main accepted correction:

```text
.github = mechanism
Demerzel = policy
TARS = judgment / reasoning
IX = measurement
Human = final authority
```

We corrected the docs and issue graph to prevent `.github` from becoming a second governance system.

## What was changed

### 1. Added explicit versioned import policy

New file:

```text
VERSIONED_IMPORT_POLICY.md
```

Commit:

```text
fa2dcb7994b20e20f4bd3c05aaf4faf582ad941d
```

Key rule:

```text
Explicit imports beat implicit inheritance.
```

Pilot behavior may use `@main` only when:

```text
advisory
non-strict
artifact-only
no auto-comments
no blocking
explicitly marked as pilot
```

Stable behavior must use:

```text
@v1 or pinned SHA
```

### 2. Turned abstraction lifecycle into anti-over-abstraction guardrail

Updated file:

```text
ABSTRACTION_LIFECYCLE.md
```

Commit:

```text
cff2b45dad7dde43c20355f2cf4ce2df3010c53a
```

New central rule:

```text
The governance/process layer must not grow faster than the product/runtime layer it is supposed to help.
```

New promotion gate:

```text
No org-level promotion without at least two real consumers,
or one high-risk repeated failure,
or explicit human exception.
```

New lifecycle exits:

```text
rejected
quarantined
deprecated
sunset
retired
superseded
```

### 3. Corrected namespace/scoping principles

Updated file:

```text
COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md
```

Commit:

```text
f5a5f84e227ad9f1d2a979697ad54ca9ab5798a8
```

Correction:

```text
The namespace/Russian-doll model is a scoping metaphor, not an inheritance system.
```

New rule:

```text
Every repo declares what it imports, where from, at what version/ref, and in what mode.
```

Also clarified that the React/Jotai analogy is pedagogical only:

```text
GitHub workflows are asynchronous event systems, not synchronous frontend state graphs.
```

### 4. Corrected Methodology Guard status and boundaries

Updated file:

```text
METHODOLOGY_GUARD.md
```

Commit:

```text
c728f206d43519e0e5c4cae471b243c34fbf90e3
```

Now explicitly says:

```text
pilot
non-strict
artifact-only
no auto-comments
no blocking
```

And:

```text
Methodology Guard may report missing fields.
Demerzel decides which missing fields become policy gates.
TARS interprets methodology findings in triage/review reasoning.
IX measures false positives, review friction, and usefulness.
Human decides high-impact promotion or blocking behavior.
```

### 5. Added abstraction registry example

New file:

```text
examples/abstractions/abstraction-registry.example.json
```

Commit:

```text
b5656d28ff5d2c00b95ed462a4124f04e13845dd
```

Initial entries:

```text
abs-methodology-guard-pilot
abs-versioned-import-policy
abs-agent-config-dedup
```

This intentionally treats agent config deduplication as a better abstraction candidate than more meta-governance docs, because the audit observed concrete duplication.

## What still needs to be moved out of .github

### To Demerzel

```text
policy semantics
lifecycle state semantics
promotion/retirement gates
review-mode authority
business value governance
```

Recommended follow-up:

```text
Create a Demerzel policy-pack contract consumed by .github workflows.
```

### To TARS

```text
triage reasoning
interpretation of Methodology Guard findings
teach-back lessons for over-abstraction vs under-abstraction
second-brain promotion of lessons learned
```

Recommended follow-up:

```text
Create a TARS triage-reasoning artifact contract.
```

### To IX

```text
false-positive rates
review friction metrics
usefulness metrics
reuse scoring
drift measurements
```

Recommended follow-up:

```text
Define methodology/abstraction usefulness metrics before promoting guard behavior.
```

## Current safe state

```text
No mass issue mutation.
No issue closure.
No label changes.
No hard blocking.
No auto-commenting every finding.
No org-wide stable rollout.
```

Methodology Guard remains a pilot in:

```text
.github
tars
```

## Remaining risks

```text
1. .github still physically hosts some policy-like docs during incubation.
2. Methodology Guard rules.yml is still local to .github during pilot.
3. @main is still used by pilot workflows until version tag exists.
4. Demerzel/TARS/IX follow-up contracts still need concrete issues/implementation.
5. GA product work can still be starved if meta-governance continues expanding.
```

## Questions for Fable 5

1. Is the corrected split `.github = mechanism / Demerzel = policy / TARS = judgment / IX = measurement` sharp enough?
2. What is the minimal Demerzel policy-pack contract that `.github` should consume?
3. Should Methodology Guard rules stay as `.github/methodology/rules.yml` during pilot, or should they move immediately to Demerzel even before stability?
4. Is `two real consumers or one high-risk repeated failure` a good promotion gate, or too rigid?
5. What should the first IX usefulness metric be for Methodology Guard?
6. How would you prevent `VERSIONED_IMPORT_POLICY.md` itself from becoming unnecessary bureaucracy?
7. Which abstraction should be killed or rejected immediately?
8. Should `agent config deduplication` become the first concrete abstraction candidate, given observed duplication?
9. What is the smallest next change that improves product value rather than governance elegance?
10. What would you delete now to preserve 80% of the value with 50% less process?

## Request for next critique

Please review the correction as a second-pass architecture audit.

Focus on:

```text
- whether the corrected ownership split is enforceable
- whether .github still owns too much policy by accident
- whether the versioned import policy is practical
- whether the abstraction lifecycle is now a brake rather than an accelerator
- whether the next work should shift immediately to GA product incident ga#493
```
