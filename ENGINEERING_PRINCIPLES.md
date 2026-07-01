# Engineering Principles

Date: 2026-07-01

This is the compact operating rule set for GuitarAlchemist engineering work.

## Core split

```text
.github   = mechanism
Demerzel  = policy
TARS      = judgment / reasoning
IX        = measurement
Human     = final authority
```

## Principle 1 — Keep process smaller than product work

```text
The governance/process layer must not grow faster than the product/runtime layer it is supposed to help.
```

If a principle, template, rule, or workflow does not reduce real friction, do not promote it.

## Principle 2 — Explicit imports beat implicit inheritance

GitHub shared behavior must be declared explicitly.

```text
A repo declares what it imports, from where, at what version/ref, and in what mode.
```

Pilot behavior may use `@main` only when it is:

```text
advisory
non-strict
artifact-only
no auto-comments
no blocking
explicitly marked as pilot
```

Stable behavior should use a version tag or pinned SHA.

## Principle 3 — Abstractions must be earned

```text
No org-level promotion without concrete reuse evidence.
```

Promote only after:

```text
at least two real consumers
or one high-risk repeated failure
or explicit human exception
```

Otherwise keep the idea as a note, example, or local helper.

## Principle 4 — Mechanism and policy stay separate

```text
.github runs checks and emits artifacts.
Demerzel decides policy gates.
TARS explains intent/readiness.
IX measures usefulness/noise.
Humans approve high-impact changes.
```

Methodology Guard reports missing fields. It does not decide governance policy.

## Principle 5 — Derived state stays derived

Labels, comments, reports, and attention-head outputs are signals.

They are not canonical truth by themselves.

Prefer stable contracts:

```text
JSON report
Markdown evidence packet
versioned workflow ref
explicit owner
rollback path
```

Avoid hidden contracts:

```text
prompt-only conventions
commit-message parsing as state
labels as sole truth
silent org-wide behavior
```

## Principle 6 — Delete before generalizing

Before adding a new document, workflow, metric, or abstraction, ask:

```text
Can this be a section in an existing file?
Can this remain local to one repo?
Has the problem repeated?
Can we solve the concrete duplication first?
```

A document that is not consulted or used should be deleted, merged, or downgraded.

## Current safe defaults

```text
Methodology Guard stays pilot/advisory/artifact-only.
No hard blocking.
No mass issue mutation.
No auto-commenting every finding.
No Demerzel migration before pilot evidence.
Return to GA product work when meta-work is not removing current friction.
```

## First concrete abstraction candidate

The first serious candidate is not the abstraction lifecycle or Methodology Guard.

It is shared agent configuration deduplication, because duplication has already been observed across repos.

## Related

- `METHODOLOGY_GUARD.md`
- `reports/fable5/fable5-copy-paste-report-2026-07-01.md`
- `Demerzel/docs/policy/workflow-policy-pack-contract.md`
