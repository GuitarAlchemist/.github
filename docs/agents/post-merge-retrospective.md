# Post-Merge Retrospective Loop

## Purpose

This document defines the lightweight compounding loop used after AFK/cloud-agent PRs are merged.

The goal is not to create bureaucracy. The goal is to turn every merge into better future delegation, faster review, safer automation, and clearer prioritization.

## Loop

```text
merge -> retrospective -> notes -> follow-up issues -> process/code adjustments -> reprioritization -> better next delegation
```

## When to write a retrospective

Write a post-merge retrospective when any of the following are true:

- an agent-authored PR was merged;
- a PR closed a workflow or governance issue;
- the PR changed AFK process, board state, review policy, or agent routing;
- review friction was medium or high;
- the PR revealed missing tests, missing docs, or unclear ownership;
- the PR was safe and repeatable enough to become a pattern.

Skip the retrospective for trivial typo-only changes unless there is a reusable lesson.

## Required fields

Each retrospective should capture:

- repository;
- PR number;
- issue number;
- agent or author lane;
- merge SHA;
- scope class;
- risk before merge;
- review friction;
- what went well;
- what went poorly;
- defects found before merge;
- defects found after merge;
- follow-up issues;
- process adjustments;
- code/test adjustments;
- priority impact.

## Scope classes

Use one or more of:

```text
docs
examples
state-artifact
workflow
runtime
test
refactor
governance
product
```

## Review friction scale

```text
none    = obvious phone-safe merge
low     = small review needed, no ambiguity
medium  = required careful review or one correction
high    = broad diff, failing checks, workflow/runtime risk, or unclear ownership
blocked = unsafe, duplicate, non-mergeable, or missing prerequisite
```

## Output locations

Recommended artifact locations:

```text
docs/agents/post-merge-retrospective.md
templates/agents/post-merge-retrospective.md
examples/agents/post-merge/tars-161-afk-state-artifacts.md
examples/agents/post-merge-index.example.json
```

Repo-specific projects may mirror these under their own `governance/agents/post-merge/` directory once automation exists.

## How retrospectives feed the system

Retrospectives should produce at most three concrete outcomes:

1. **Follow-up issue** — when work remains or a defect/risk was discovered.
2. **Process adjustment** — when routing, fanout, labels, board state, or review gates should change.
3. **Code/test adjustment** — when the repo needs stronger validation, tests, templates, or schemas.

Do not create noisy follow-ups for every observation. Prefer fewer, higher-signal actions.

## Priority impact

Retrospectives may recommend priority changes, but they do not change priorities automatically.

Priority changes require human confirmation.

Suggested values:

```text
none
raise-priority
lower-priority
block-until-fixed
split-before-continuing
promote-to-pattern
```

## Automation policy

First pass is manual/docs-only.

Later automation may trigger on merged PRs, but must follow these rules:

- no auto-prioritization;
- no auto-merge;
- no private prompt/log capture;
- no spam comments on every PR event;
- no workflow automation until the AFK dashboard and watchdog model are stable;
- human remains the merge and priority gate.

## Phone-first rule

A useful retrospective must be readable from a phone.

If it cannot be skimmed quickly, it is too long. Move detailed evidence into links and keep the lessons concise.

## Template

Use `templates/agents/post-merge-retrospective.md`.
