# Label Taxonomy

Date: 2026-07-01

This document defines a lightweight cross-repo label taxonomy for GuitarAlchemist issues and PRs.

Labels should help routing, priority, review mode, and value tracking. They should not become a separate bureaucracy.

## Type labels

```text
type:epic
type:story
type:task
type:bug
type:research
type:docs
type:template
type:governance
type:metric
type:curriculum
type:capability
```

## Area labels

```text
area:afk
area:governance
area:tars
area:ix
area:demerzel
area:teach
area:seldon
area:streeling
area:product
area:github-ops
area:agent-eval
area:ml-math
```

## Value-stream labels

```text
value:execution-flow
value:governance-safety
value:evidence-observability
value:learning-compounding
value:agent-capability
value:product-platform
```

## Priority labels

```text
priority:p0
priority:p1
priority:p2
priority:p3
```

Meaning:

```text
p0 = urgent / blocking / very high leverage
p1 = important next
p2 = useful but not immediate
p3 = research / parking lot / future
```

## Review-mode labels

```text
review:silent-classify
review:batch-digest
review:fast-review
review:focused-review
review:decision-gate
review:escalate-review
```

## State labels

```text
state:shaping
state:ready
state:delegated
state:pr-open
state:needs-review
state:blocked
state:done
state:deferred
state:superseded
```

## Agent-lane labels

```text
agent:jules
agent:claude
agent:codex
agent:human
agent:mixed
```

## Risk labels

```text
risk:low
risk:medium
risk:high
risk:uncertain
risk:goodhart
risk:verification-horizon
risk:rubber-stamp
```

## Evidence labels

```text
evidence:needed
evidence:packet-ready
evidence:checks-passing
evidence:manual-review-needed
evidence:retrospective-needed
evidence:learning-captured
```

## Recommended minimum per important issue

```text
type:*
area:*
value:*
priority:*
state:*
review:*
```

## Recommended minimum per PR

```text
type:docs | type:task | type:governance | type:template
area:*
review:*
evidence:needed | evidence:packet-ready | evidence:checks-passing
```

## Label usage rules

```text
Use labels to support routing and review.
Do not use labels as a substitute for issue body evidence.
Do not add priority labels without business value.
Do not add review labels without review-mode rationale.
Do not mark evidence as ready unless evidence is visible.
```

## Relationship to methodology guard

The methodology guard should eventually check for missing sections first, then labels second.

Labels are a routing signal. The body remains the source of evidence.

## Related

- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `OPERATING_GATES.md`
- `BUSINESS_VALUE_TREE.md`
- `.github#27`
