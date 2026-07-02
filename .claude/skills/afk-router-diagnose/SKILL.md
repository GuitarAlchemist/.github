---
name: afk-router-diagnose
description: Diagnose GuitarAlchemist AFK routing, Claude Code, Jules, Agent Blackbox, submodule, and post-merge smoke failures before editing workflows.
---

# AFK Router Diagnose

Use this skill before patching GitHub Actions or agent-routing behavior in GuitarAlchemist repositories.

## Scope

Apply this skill when investigating:

- `Claude` or `Claude Code Review` workflow failures.
- `Agent Blackbox` verdicts, especially `Verdict: fail`.
- `Auto-Update Demerzel Submodule` failures.
- `post-merge-smoke` reports against `demos.guitaralchemist.com`.
- Duplicate agent-created issues or PRs around the same root cause.
- Changes under `.github/workflows/**`, `.claude/**`, `AGENTS.md`, `CLAUDE.md`, or agent governance files.

## First classify the failure

Before editing files, classify the failure as one of:

1. **Repo workflow bug** — YAML step ordering, missing checkout, wrong path, bad shell command, bad GitHub CLI query, insufficient permissions declared in the workflow.
2. **Human secret or permission action** — missing organization/repository secret, expired OAuth token, unavailable deployment tunnel, branch protection, or org policy.
3. **Expected guardrail** — Agent Blackbox failing because an autonomous PR touched protected workflow/governance paths.
4. **Local infrastructure outage** — `demos.guitaralchemist.com` or Cloudflare 52x/530 caused by the operator's local machine or tunnel being offline.
5. **Duplicate work** — multiple issues or PRs report the same regression, smoke failure, or agent task.

Do not patch until the classification is explicit in the PR body or issue comment.

## Claude / Claude Code Review failures

Check for these causes first:

- Repository checkout missing before `anthropics/claude-code-action`.
- Empty or unavailable `CLAUDE_CODE_OAUTH_TOKEN`.
- Missing `contents`, `pull-requests`, or `issues` permissions for the intended operation.
- Branch/ref mismatch caused by a reused `claude/*` branch.
- Failure in env validation before model/tool execution.

Patch workflow YAML only for repo workflow bugs. If the root cause is an org secret, token, or permission outside the repo, request human action and do not create workaround code.

## Agent Blackbox fail verdicts

A fail verdict is blocking by default. Inspect the reason before proposing a merge.

Common expected fail:

- A Claude/Jules/Codex PR touched `.github/workflows/**` or governance/agent files.
- The diff is small and intentional, but the path is protected.

Required response:

- State that human review is required.
- Summarize changed protected files.
- Explain whether the failure is expected guardrail or real defect.
- Never auto-merge or recommend auto-merge for workflow/governance changes.

## Auto-Update Demerzel Submodule failures

Check the failing step:

- `Checkout with submodules` fails: suspect submodule URL, credentials, branch/ref, or access permissions.
- `Update submodule` fails: inspect target SHA/ref and submodule state.
- `Auto-commit small update` fails: suspect dirty working tree, Git identity, branch protection, or push permission.
- `Create PR for large update` fails: suspect `gh` auth, token scopes, duplicate branch/PR, or branch naming conflict.

Prefer PR-based updates over direct pushes to protected branches.

## Post-merge smoke failures

For `demos.guitaralchemist.com`:

- Treat Cloudflare 502, 503, 504, 52x, and 530 as likely infrastructure-down unless there is evidence of an application regression.
- A local tunnel or powered-off operator machine is human-only action.
- Do not open repeated regression issues for the same outage.
- Keep one canonical issue if tracking is useful; close duplicates with a short explanation.

Real regressions include:

- HTTP 200 with missing expected marker.
- Persistent 404/asset route failure not explained by tunnel outage.
- Reproducible app error after infrastructure is healthy.

## Duplicate triage

When multiple issues/PRs share the same root cause:

- Pick the oldest or most complete item as canonical.
- Close newer duplicates with links to the canonical item.
- Preserve evidence in the canonical item.
- Do not close an active PR until confirming its changes are already merged or superseded.

## PR requirements

For any PR produced after this diagnosis, include:

- Failure classification.
- Evidence: workflow name, run ID if available, failing step, and affected repo.
- Files changed.
- Whether human action is required.
- Rollback plan.

## Hard rules

- Do not directly push to `main`.
- Do not auto-merge workflow or governance changes.
- Do not invent or expose secrets.
- Do not bypass Agent Blackbox.
- Do not treat local tunnel downtime as product regression.
- Ask for human action when the fix requires organization secrets, OAuth setup, billing, or external infrastructure.