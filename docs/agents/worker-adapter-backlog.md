# Worker adapter backlog

This document tracks the gap between routing an issue to a worker and actually executing that worker safely.

The organization can already express intent through issue metadata, labels, Project fields, and delegation comments. Execution requires a worker-specific adapter or a manual process.

## Adapter status

| Worker | Routing ready | Execution ready | Current trigger | Gap |
|---|---:|---:|---|---|
| `human` | yes | yes | manual | none |
| `demerzel` | yes | partial | process / comments / issues | executable governance runner is separate work |
| `jules` | yes | partial | human `jules` label or `JULES_API_KEY` workflow | Demerzel secret access or manual label path |
| `claude` | yes | no | manual/local | adapter contract and runner needed |
| `codex` | yes | no | manual/local | adapter contract and runner needed |
| `ollama` | yes | local only | local-runner | repo-local script/workflow needed |
| `notebooklm` | yes | manual only | manual | export/write-back process needed |
| `gemini` | yes | no | manual/local | adapter contract and runner needed |
| `augment` | yes | human-in-loop | IDE | no autonomous runner; template only |

## Adapter requirements

A worker adapter must define:

- invocation mechanism;
- workspace isolation;
- input contract;
- allowed commands;
- secret policy;
- cost/budget policy;
- timeout/cancellation path;
- output artifact format;
- PR/comment/write-back behavior;
- review gates;
- HALT behavior.

## Priority order

### P0 — Jules operational path

Goal: make Demerzel able to delegate to Jules reliably.

Options:

1. Add `Demerzel` access to the organization-level `JULES_API_KEY` secret.
2. Recreate `JULES_API_KEY` as a Demerzel repository secret.
3. Use the human-applied `jules` label path as the reliable fallback.

Do not rely on API-applied `jules` labels as the trigger.

### P1 — Local/Ollama observe runner

Goal: local cheap classification and issue shaping.

Inputs:

- issue title/body;
- labels;
- linked docs;
- desired worker lane.

Outputs:

- routing recommendation;
- risk estimate;
- missing metadata checklist;
- suggested delegation comment.

### P1 — Claude/Codex manual dispatch contract

Goal: make manual Claude/Codex runs consistent before automating them.

Outputs must include:

- changed files list;
- diff summary;
- validation evidence;
- risk notes;
- unresolved questions;
- linked issue.

### P2 — NotebookLM research write-back

Goal: make source-heavy research usable by Demerzel.

Required write-back:

- source bundle link;
- synthesis summary;
- citations or source references;
- decision impact;
- recommended follow-up issues.

### P2 — Gemini large-context review

Goal: large-context review of docs, policies, or architecture decisions.

Required output:

- issue-linked review comment;
- contradictions found;
- missing assumptions;
- risk notes;
- suggested edits.

## Issue split candidates

Create repo-local issues when ready:

- `[Task][AIW] Restore Jules API delegation for Demerzel`
- `[Task][AIW] Add local Ollama issue-shaping runner`
- `[Task][AIW] Define Claude manual dispatch adapter`
- `[Task][AIW] Define Codex manual dispatch adapter`
- `[Task][AIW] Add NotebookLM research write-back template`
- `[Task][AIW] Add Gemini large-context review template`

## Non-goals

- No automatic merge.
- No secret exfiltration or secret printing.
- No broad cross-repo write automation without explicit review gates.
- No provider-specific lock-in where a portable contract is enough.
