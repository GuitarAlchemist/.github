# React State Management Analogy for GitHub Workflow States

Date: 2026-07-01

This document maps GitHub workflow state management to React state management concepts.

The analogy helps keep the GitHub methodology guard, state machines, rules engine, and attention heads understandable and maintainable.

## Core analogy

```text
React app state management
  ~=
GitHub workflow state management
```

In React, uncontrolled state duplication creates bugs, stale UI, and inconsistent derived views.

In GitHub workflows, uncontrolled state duplication creates stale issue bodies, stale labels, stale hierarchy maps, ambiguous PR status, and repeated human review friction.

## Mapping

```text
React component state
  -> local issue/PR fields, comments, labels

Global store / atoms
  -> central workflow state model

Actions / events
  -> GitHub events: issue opened, PR updated, review submitted, merge completed

Reducer
  -> rules engine deciding allowed or recommended transitions

Selectors
  -> attention heads extracting derived signals

Effects / middleware
  -> GitHub Actions, comments, artifacts, labels, digests

Derived state
  -> business value score, review mode, risk level, evidence completeness

State machine
  -> explicit lifecycle: shaped -> ready -> delegated -> pr-open -> review -> done

Devtools
  -> evidence packets, methodology reports, retrospectives, audit trail
```

## Jotai-style interpretation

Because GuitarAlchemist already prefers React + Jotai, the workflow can be understood as atoms and derived atoms.

```text
issueBodyAtom
labelsAtom
prStatusAtom
checksAtom
evidencePacketAtom
businessValueAtom
hierarchyLinksAtom
reviewModeAtom
```

Derived atoms:

```text
isIssueReadyAtom
missingEvidenceAtom
reviewModeSuggestionAtom
businessValueScoreAtom
verificationHorizonAtom
teachCandidateAtom
capabilityAttestationNeededAtom
```

Effects:

```text
writeMethodologyReport
uploadEvidencePacket
commentDigest
updateHierarchyMap
recommendTeachSession
```

## Important React lesson

```text
Do not store derived state as source of truth.
```

Applied to GitHub:

```text
Do not make labels the only source of truth.
Do not make comments the only source of truth.
Do not make central docs the only source of truth.
```

Use layered truth:

```text
Issue/PR body      = local intent and acceptance criteria
Labels             = routing/cache/index signal
Central maps       = cross-repo structure and value map
Evidence packets   = review/audit artifacts
Workflow reports   = derived diagnostics
```

## Reducer analogy

React reducer:

```text
(state, action) -> next_state
```

Workflow reducer:

```text
(current_lifecycle_state, github_event, rules, signals) -> transition_recommendation
```

Example:

```json
{
  "current_state": "shaped",
  "event": "issue.edited",
  "signals": ["business-value-present", "review-mode-present"],
  "missing": ["expected-evidence"],
  "recommended_state": "shaped",
  "blocked_transition": "ready",
  "safe_default": "keep shaping until expected evidence is defined"
}
```

## Selector / attention head analogy

React selector:

```text
selectVisibleTodos(state)
```

Workflow attention head:

```text
selectMissingEvidence(issue_or_pr)
selectReviewModeSuggestion(issue_or_pr)
selectBusinessValueGap(issue_or_pr)
selectTeachCandidate(issue_or_pr)
```

The head does not mutate state. It only emits a signal.

## Effect analogy

React effect:

```text
when state changes, synchronize with external system
```

GitHub workflow effect:

```text
when issue/PR changes, run guard, upload report, optionally comment/digest
```

## Practical design rule

```text
Events change state.
Rules validate transitions.
Attention heads derive signals.
Effects synchronize reports.
Humans decide high-impact tradeoffs.
```

## Anti-patterns

```text
Duplicating derived state manually everywhere
Using labels as canonical truth
Letting comments drift from central maps
Changing state without an event trail
Blocking work from noisy derived signals
Treating attention heads as authorities instead of advisors
```

## Recommended architecture

```text
GitHub event
-> normalized event
-> current lifecycle state
-> attention heads derive signals
-> rules engine evaluates transition
-> methodology report artifact
-> optional digest/comment
-> human review if required
-> learning/memory update if useful
```

## Related

- `WORKFLOW_STATE_MACHINE.md`
- `OPERATING_GATES.md`
- `PRODUCT_PROJECT_OPERATING_MODEL.md`
- `ISSUE_HIERARCHY.md`
- `BUSINESS_VALUE_TREE.md`
- `.github#29`
- `Demerzel#588`
- `Demerzel#592`
