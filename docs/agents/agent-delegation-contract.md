# Agent delegation contract

This document defines the minimum contract for delegating GitHub issues to AI or human agents across GuitarAlchemist repositories.

The contract is intentionally portable. It can be used in issue bodies, issue comments, GitHub Projects fields, workflow inputs, local runner scripts, or provider-specific adapters.

## Principle

An issue is not agent-ready because it has an agent label. It is agent-ready when it has a bounded task contract, explicit review gates, and evidence requirements.

Agents may propose work. They do not own governance, risk escalation, HALT decisions, or merge authority.

## Delegation levels

| Level | Meaning | Allowed output |
|---|---|---|
| `observe` | Read, classify, summarize, or recommend. | Comment, report, triage note. |
| `draft` | Produce docs/specs/plans without code execution. | Markdown doc, issue split, PRD, checklist. |
| `patch` | Produce a bounded patch or branch. | Diff, branch, local test evidence. |
| `pr` | Open a PR with evidence. | Pull request, test log, risk notes. |
| `harvest` | Integrate or summarize completed work. | Review package, release notes, follow-up issues. |

`harvest` never means automatic merge. Merge remains governed by repo policy and human/Demerzel review.

## Worker classes

| Worker | Current role | Execution status |
|---|---|---|
| `human` | Final judgment, manual setup, review, merge authority. | Active. |
| `demerzel` | Governance, routing, policy, risk, HALT, batch control. | Active as process/governance layer. |
| `jules` | GitHub-native cloud coding worker that can open PRs. | Active when human `jules` label or API secret is available. |
| `claude` | Local/remote coding/review worker. | Routable; requires explicit adapter/runner for execution. |
| `codex` | Coding/patch/review worker. | Routable; requires explicit adapter/runner for execution. |
| `ollama` | Local cheap analysis, summaries, first-pass review. | Local execution only unless a runner is added. |
| `notebooklm` | Source-grounded research/synthesis workspace. | Manual/semi-manual write-back. |
| `gemini` | Large-context inspection/review or Google ecosystem worker. | Routable; requires explicit adapter/runner. |
| `augment` | IDE-assisted human-steered patching. | Human-in-the-loop only. |

## Required issue metadata

Every delegated issue should have either an `issue_meta` block or equivalent Project fields.

```yaml
issue_meta:
  level: task
  parent: "owner/repo#123"
  area: aiw|governance|product|runtime|music|rendering|research|infra|docs|evals|bot
  priority: P0|P1|P2|P3
  complexity: XS|S|M|L|XL
  risk: low|medium|high|critical
  afk:
    readiness: observe|draft|patch|pr|harvest|blocked
    max_autonomy: observe|draft|patch|pr|harvest
    reason: "why this autonomy is safe or blocked"
  routing:
    lane: explore|shape|loop|verify|govern
    preferred_workers:
      - human
      - jules
  status: ready
```

## Delegation block

Use this block when an issue is being staged for an agent.

```yaml
delegation:
  worker: jules|claude|codex|ollama|notebooklm|gemini|augment|human|demerzel
  mode: observe|draft|patch|pr|harvest
  trigger: manual-label|workflow-dispatch|local-runner|project-field|comment-command|manual
  allowed_paths:
    - docs/
    - scripts/
  non_goals:
    - no broad refactor
    - no secret changes
    - no governance bypass
  test_commands:
    - echo "docs-only"
  evidence_required:
    - diff_summary
    - validation_log
    - risk_notes
    - linked_issue
  stop_conditions:
    - missing_context
    - scope_expansion
    - failing_tests_without_progress
    - budget_exceeded
    - risk_escalation
    - halt_active
```

## Readiness checklist

Before moving an issue to `Ready for agent`, confirm:

- The issue has a single bounded outcome.
- The issue has explicit non-goals.
- Allowed files/directories are named where practical.
- Test or validation commands are named.
- The maximum autonomy mode is declared.
- Risk is declared.
- Stop conditions are declared.
- Required evidence is declared.
- Review state is declared.
- The worker has a real execution path.

If any of these are missing, route the issue to `shape`, not `loop`.

## Trigger rules

### Jules

Preferred trigger order:

1. Human-applied `jules` label.
2. Jules API workflow using `JULES_API_KEY` when configured.

`worker:jules` is routing metadata. It does not guarantee Jules pickup.

### Claude / Codex / Gemini

Use labels and Project fields for routing until a repo-specific adapter exists.

A safe adapter must declare:

- runner type;
- workspace isolation;
- allowed commands;
- secret policy;
- output collection;
- cancellation path;
- cost/budget tracking;
- review gates.

### Ollama

Use for local classification, summarization, and cheap review. Do not treat local model output as final authority.

### NotebookLM

Use for source-heavy research. Outputs must be copied/exported back to GitHub, Drive, or repo docs before they can influence a Demerzel decision.

## Project field mapping

| Project field | Source |
|---|---|
| `Preferred worker` | `delegation.worker` or `issue_meta.routing.preferred_workers` |
| `AFK readiness` | `issue_meta.afk.readiness` |
| `Status` | issue lifecycle state |
| `Agent batch` | queue/batch assignment |
| `Review state` | required human/governance review state |
| `Evidence` | PR, logs, report, artifact, or linked comment |

## Backpressure rules

- Do not fan out more PRs than can be reviewed.
- Keep architecture-heavy work to one active agent PR at a time.
- Batch related docs-only tasks only when file overlap is low.
- Stop delegation if PRs lack evidence.
- Stop delegation if agents touch files outside declared scope.
- Stop delegation if the review queue becomes the bottleneck.

## Minimal delegation comment

When staging an issue, use a short comment like:

```markdown
## Agent delegation

Prepared for: `jules`
Mode: `pr`
Trigger: human-applied `jules` label
Status: ready for agent

Constraints:
- Keep scope limited to the issue body.
- Do not change secrets, governance policy, or unrelated runtime code.
- Include validation evidence, risk notes, and linked issue in the PR.
- Stop if context is missing or scope expands.
```

## Acceptance criteria for agent outputs

An agent output is reviewable when it includes:

- a linked issue;
- a minimal scope summary;
- changed files list;
- validation evidence;
- risk notes;
- any unresolved questions;
- no secret leakage;
- no governance bypass;
- no broad refactor unless explicitly authorized.

## Relationship to Projects

GitHub Projects should show delegation state. They should not be the only source of truth.

The issue body or first coordination comment should remain sufficient for another maintainer to understand why a task was delegated, what the agent may do, and what evidence is required.
