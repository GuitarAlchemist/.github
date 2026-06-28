# Issue Meta Schema

This document defines the standard `issue_meta` YAML block structure used across the Guitar Alchemist organization for cross-repo triage and automated processing.

## Schema Definition

The `issue_meta` block should be included in the issue description, typically at the top or within a designated section.

```yaml
issue_meta:
  level: # Required. One of: pi, epic, story, task, subtask
  parent: # Optional. Format: owner/repo#number or null
  area: # Required. One of: runtime, research, governance, product, docs, infra
  priority: # Required. One of: P0, P1, P2, P3
  complexity: # Required. One of: XS, S, M, L, XL
  risk: # Required. One of: low, medium, high
  afk:
    readiness: # Required. One of: ready, candidate, blocked
    max_autonomy: # Required. One of: none, draft, pr, comment_only
    reason: # Required. String explaining the autonomy level or readiness state.
  budget:
    tier: # Required. One of: free-local, paid-allowed, cloud-required
    max_cost_usd: # Required. Number
    max_runner_minutes: # Required. Number
  routing:
    lane: # Required. One of: shape, loop, fix, docs, research, infra
    preferred_workers: # Optional. List of worker identifiers (e.g., [jules, claude-code-local])
  evidence_required: # Required. List of strings (e.g., [unit_tests, screenshots])
  status: # Required. One of: ready, blocked, needs_review, done
```

## Field Details

### `level`
The hierarchy level of the issue.
- `pi`: Program Increment or very large initiative.
- `epic`: Large feature or theme.
- `story`: User-facing feature or significant technical piece.
- `task`: Discrete unit of work.
- `subtask`: Smallest unit of work, usually part of a task.

### `parent`
Reference to the parent issue. Must be a full GitHub issue reference (e.g., `GuitarAlchemist/Demerzel#475`) or `null` if it's a top-level issue.

### `area`
The functional area of the codebase or project.
- `runtime`: Core execution logic.
- `research`: Exploratory work.
- `governance`: Policy, standards, and organization.
- `product`: Feature definition and UX.
- `docs`: Documentation.
- `infra`: Infrastructure and CI/CD.

### `priority`
Business or technical urgency.
- `P0`: Critical / Blocker.
- `P1`: High priority.
- `P2`: Medium priority.
- `P3`: Low priority.

### `complexity`
Estimated effort.
- `XS`, `S`, `M`, `L`, `XL` (T-shirt sizes).

### `risk`
Potential for negative impact or uncertainty.
- `low`, `medium`, `high`.

### `afk` (Away From Keyboard)
Parameters for autonomous agent execution.
- `readiness`: Whether the issue is ready for an agent to pick up.
- `max_autonomy`: The maximum level of authority granted to the agent (e.g., `pr` means it can open a PR but not merge).
- `reason`: Explanation for the current readiness/autonomy status.

### `budget`
Resource constraints for the task.
- `tier`: Cost category.
- `max_cost_usd`: Maximum dollar amount allowed for LLM/API usage.
- `max_runner_minutes`: Maximum CI/CD runner time.

### `routing`
Triage and assignment hints.
- `lane`: The processing pipeline this issue belongs to.
- `preferred_workers`: List of agents or humans preferred for this task.

### `evidence_required`
A list of artifacts that must be provided to consider the task complete (e.g., `template_inventory`, `label_taxonomy`).

### `status`
Current lifecycle state of the issue.

---

## Migration Notes

To adopt this standard across the organization, the following steps should be taken for **TARS**, **IX**, **Demerzel**, **GA**, and **Hari**:

1.  **Template Update**: Copy the standardized `.github/ISSUE_TEMPLATE/*.yml` files from the `profile` repository to each repo.
2.  **Label Sync**: Ensure all repositories have the labels defined in `docs/label-taxonomy.md`.
3.  **Retroactive Meta**: For active Epics and Stories, add the `issue_meta` block to the issue description.
4.  **Router Integration**: Once the triage router is implemented (Demerzel #475), ensure it is configured to watch these repositories.
5.  **Training**: Ensure both human contributors and AI agents are aware of the new `issue_meta` block and its importance for autonomous workflows.
