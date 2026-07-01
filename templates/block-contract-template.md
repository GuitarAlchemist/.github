# Block Contract Template

Use this template when extracting a reusable workflow, action, script, rule pack, attention head, or state-machine component.

## Metadata

```yaml
namespace: ""
block_name: ""
owner_scope: ""
maturity: "rough | repeated | reusable | cross-repo | governance-critical"
version: ""
```

## Purpose

What single job does this block do?
-

Why should it exist as a separate block?
-

## Inputs

```yaml
inputs:
  - name: ""
    required: true
    type: ""
    description: ""
```

## Outputs

```yaml
outputs:
  - name: ""
    type: ""
    description: ""
```

## Side effects

Expected side effects:
-

Side effects intentionally avoided:
-

## Dependencies

Allowed dependencies:
-

Dependencies intentionally avoided:
-

## Boundary

This block may know about:
-

This block must not know about:
-

Callers may depend on:
-

Callers must not depend on:
-

## Failure mode

What happens when it fails?
-

Safe default:
-

## Test fixtures

Pass examples:
-

Expected warning examples:
-

Expected failure examples:
-

## Review mode

Recommended review mode:
-

Reason:
-

## Extraction justification

- [ ] distinct owner
- [ ] distinct reason to change
- [ ] reusable from at least two workflows or likely future workflows
- [ ] testable independently
- [ ] stable output contract
- [ ] hides implementation detail from callers

## Non-goals

-
