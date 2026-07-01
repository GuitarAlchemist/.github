# AFK Workflow Runbook

## Purpose

This runbook defines the organization-level workflow for AFK/cloud-agent work across GuitarAlchemist repositories.

The goal is to increase delivery throughput without losing control of review quality, scope boundaries, safety gates, or product direction.

## Operating model

```text
Issue -> routing -> agent delegation -> PR -> review gate -> merge/hold/close -> post-merge retrospective
```

The workflow optimizes for small, reviewable, compounding changes.

## Board columns

Use the organization board definitions as the human-facing cockpit:

```text
Inbox
Ready
Delegated
PR Open
Needs Review
Needs Revision
Blocked
Done
```

Related board-definition issues:

- `GuitarAlchemist/.github#14` — TARS AFK Control Plane
- `GuitarAlchemist/.github#15` — Agent PR Review Queue
- `GuitarAlchemist/.github#16` — Guitar Alchemist Product Roadmap

## Agent roles

```text
Jules  = small docs/examples/state artifacts
Claude = review, split, architecture correction
Codex  = isolated second-opinion / test-only experiments
Human  = merge gate and priority owner
```

### Jules lane

Use Jules for:

- docs-only PRs;
- examples-only PRs;
- JSON/JSONL state artifacts;
- narrow dashboard/static HTML work;
- low-risk template/report additions.

Do not use Jules as the primary owner for:

- broad runtime refactors;
- GitHub Actions automation;
- security-sensitive workflow changes;
- large multi-file architecture changes;
- ambiguous product direction.

### Claude lane

Use Claude for:

- splitting oversized PRs;
- architecture critique;
- review of workflow/runtime changes;
- extracting narrower follow-up issues;
- explaining why a PR should be held.

### Codex lane

Use Codex sparingly for:

- isolated tests;
- second-opinion reviews;
- narrow implementation spikes;
- validation after Jules/Claude outputs.

## Delegation checklist

Before delegating an issue to an agent, confirm:

- the issue has a narrow scope;
- acceptance criteria are explicit;
- non-goals are listed;
- expected changed-file classes are clear;
- the target agent is appropriate;
- no active halt marker blocks AFK work;
- fanout limits are respected.

## Merge gate

A PR can be merged quickly only if all are true:

- scope is narrow;
- diff is easy to review;
- PR is mergeable;
- checks are green or intentionally non-applicable;
- Agent Blackbox/risk evidence is acceptable when present;
- no workflow/runtime/security-sensitive files were changed unexpectedly;
- the PR does not close a broader issue prematurely.

## Hold conditions

Hold or request revision if any are true:

- PR changes `.github/workflows/` without prior review;
- PR changes runtime code outside the issue scope;
- PR is non-mergeable;
- tests/checks fail;
- PR is a duplicate or superseded by another PR;
- PR attempts to auto-merge, auto-approve, or bypass human review;
- PR captures private prompts, secrets, raw logs, or unnecessary internal traces;
- PR is too broad to review from a phone.

## Fanout policy

Default fanout:

```text
1 active agent lane on the critical path
```

Increase fanout only when:

- the AFK board state is current;
- review queue is not overloaded;
- active work is independent;
- each agent has a distinct lane;
- each task can be merged or closed independently.

Recommended controlled fanout:

```text
Jules: one docs/artifacts task
Claude: one review/split task
Codex: one isolated validation task
```

## Post-merge retrospective

After every meaningful merge, capture a lightweight retrospective.

Related workflow issue:

- `GuitarAlchemist/.github#17` — Post-merge retrospective and compounding learning loop

Minimum report fields:

- repo;
- PR number;
- issue number;
- agent;
- merge SHA;
- scope class;
- review friction;
- what went well;
- what went poorly;
- follow-up issues;
- process adjustments;
- code/test adjustments;
- priority impact.

The retrospective should improve the next delegation cycle. It must not automatically change priorities without human confirmation.

## Current sequencing

Current AFK setup sequence:

```text
1. AFK state artifacts       -> done via GuitarAlchemist/tars#136 / PR #161
2. HTML AFK dashboard        -> active via GuitarAlchemist/tars#137
3. Post-merge retrospective  -> defined in GuitarAlchemist/.github#17
4. Watchdog automation       -> later, after dashboard and retrospective templates stabilize
5. Skill injection workflow  -> later, after split/review
```

## Safety principles

- Humans remain the merge gate.
- Labels and dashboards are advisory, not authority.
- No agent gets autonomous merge power.
- No auto-prioritization without human confirmation.
- Prefer boring docs/state artifacts before automation.
- Prefer reversible changes.
- Prefer small PRs that can be reviewed on a phone.

## Phone-first review rule

If a PR cannot be safely reviewed from a phone, it is not a fast-merge candidate.

It should move to one of:

```text
Needs Revision
Blocked
Needs Desktop Review
Superseded / Duplicate
```

## Done definition

A workflow item is done when:

- the PR is merged or intentionally closed;
- the linked issue is updated or closed;
- follow-up issues are created if needed;
- the post-merge learning loop has captured any meaningful lesson;
- the board status reflects reality.
