# Report for Fable 5 — Architecture Corrections Applied

Date: 2026-07-01

## Final correction (second pass, 2026-07-01)

The first-pass correction below over-materialized the fix: it answered "too many process docs" with more process docs. The second pass applied the "delete 50% of the process" recommendation:

```text
- VERSIONED_IMPORT_POLICY.md, ABSTRACTION_LIFECYCLE.md, and
  COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md were merged into a single
  compact ENGINEERING_PRINCIPLES.md and deleted.
- examples/abstractions/abstraction-registry.example.json was deleted
  (no registry before real reuse evidence).
- ix/docs/metrics/methodology-guard-usefulness-metrics.md and
  tars/docs/triage/methodology-guard-triage-reasoning.md were deleted
  (IX measures only after real data; TARS reasons only after real reasoning).
- Demerzel/docs/policy/workflow-policy-pack-contract.md survives as a
  draft contract, activated only after pilot evidence.
- Methodology Guard stays pilot/advisory/artifact-only.
```

File references in the historical body below describe documents that no longer exist as standalone files; their surviving content lives in `ENGINEERING_PRINCIPLES.md`.

Recommended next work: return to GA product incident `ga#493`.

You identified the core risk correctly: the governance/process layer was starting to grow faster than the product/runtime layer it is supposed to help.

I applied a corrective pass.

## Accepted split

```text
.github   = mechanism
Demerzel  = policy
TARS      = judgment / reasoning
IX        = measurement
Human     = final authority
```

## Corrections implemented

### 1. Versioned imports instead of implicit inheritance

Added:

```text
VERSIONED_IMPORT_POLICY.md
```

Rule:

```text
Explicit imports beat implicit inheritance.
```

`@main` is now explicitly pilot-only:

```text
advisory
non-strict
artifact-only
no auto-comments
no blocking
explicitly marked as pilot
```

Stable imports must become:

```text
@v1 or pinned SHA
```

### 2. Abstraction lifecycle is now a brake, not a process accelerator

Updated:

```text
ABSTRACTION_LIFECYCLE.md
```

New central guardrail:

```text
The governance/process layer must not grow faster than the product/runtime layer it is supposed to help.
```

Promotion now requires:

```text
at least two real consumers
or one high-risk repeated failure
or explicit human exception
```

Lifecycle now includes negative/exit states:

```text
rejected
quarantined
deprecated
sunset
retired
superseded
```

### 3. Namespace model corrected

Updated:

```text
COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md
```

Correction:

```text
The namespace/Russian-doll model is a scoping metaphor, not an inheritance system.
```

Also clarified:

```text
React/Jotai analogy is pedagogical only.
GitHub workflows are asynchronous event systems, not synchronous frontend state graphs.
```

### 4. Methodology Guard downgraded/clarified as pilot

Updated:

```text
METHODOLOGY_GUARD.md
```

It now explicitly says:

```text
pilot
non-strict
artifact-only
no auto-comments
no blocking
```

And clarifies:

```text
Methodology Guard reports missing fields.
Demerzel decides policy gates.
TARS interprets findings.
IX measures usefulness/noise.
Human decides high-impact promotions or blocking.
```

### 5. Abstraction registry example added

Added:

```text
examples/abstractions/abstraction-registry.example.json
```

Initial candidates:

```text
abs-methodology-guard-pilot
abs-versioned-import-policy
abs-agent-config-dedup
```

The agent config dedup candidate was included because your audit identified concrete duplication across repos.

### 6. Responsibility-owner artifacts added outside .github

Added in Demerzel:

```text
docs/policy/workflow-policy-pack-contract.md
```

Added in IX:

```text
docs/metrics/methodology-guard-usefulness-metrics.md
```

Added in TARS:

```text
docs/triage/methodology-guard-triage-reasoning.md
```

This is meant to prevent `.github` from becoming policy authority.

## Current safe state

```text
No mass issue mutation.
No issue closure.
No label changes.
No hard blocking.
No auto-commenting every finding.
No org-wide stable rollout.
```

## Still fragile

```text
1. .github still physically hosts several policy-like docs during incubation.
2. rules.yml still lives in .github during Methodology Guard pilot.
3. @main is still used by pilots until enough evidence exists for @v1.
4. Demerzel/TARS/IX contracts are drafts, not enforced.
5. GA product work can still be starved if meta-governance continues expanding.
```

## Questions for your second-pass review

1. Is the ownership split now sharp enough?
2. Should Methodology Guard rules move to Demerzel immediately, or stay in .github during pilot?
3. Is `two consumers or one high-risk repeated failure` a good promotion rule?
4. Is the versioned import policy practical, or too bureaucratic?
5. What would you delete now to reduce process by 50% while preserving 80% of the value?
6. Should `agent config deduplication` be the first real abstraction candidate?
7. What is the minimal Demerzel policy-pack contract that .github should consume?
8. What is the first IX metric that should gate Methodology Guard promotion?
9. Should the next work shift immediately to GA product incident `ga#493`?
10. Where does `.github` still accidentally act as a god-repo?
