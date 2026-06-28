# Agent delegation comment template

Use this comment when staging a GitHub issue for an AI or human worker.

Keep the comment short enough to remain readable in the issue thread. Longer rationale belongs in the issue body, linked docs, or follow-up comments.

```markdown
## Agent delegation

Prepared for: `<worker>`
Mode: `<observe|draft|patch|pr|harvest>`
Trigger: `<manual-label|workflow-dispatch|local-runner|project-field|comment-command|manual>`
Status: `<shaping|ready|ready-for-agent|agent-running|blocked>`

### Scope

Outcome:
- <single bounded outcome>

Allowed paths:
- `<path/>`

Non-goals:
- <no broad refactor>
- <no secret changes>
- <no governance bypass>

### Validation

Expected validation:
- `<command or docs-only check>`

Evidence required:
- diff summary
- validation log or explanation
- risk notes
- linked issue/PR

### Stop conditions

Stop and report back if:
- required context is missing;
- scope expands beyond this issue;
- tests fail without clear progress;
- a secret, credential, or private token would be needed;
- the change touches governance, HALT, security, or release policy unexpectedly.

### Review gate

This delegation does not grant merge authority. Output must be reviewed under repository policy and Demerzel/human review gates.
```

## Worker-specific notes

### Jules

Use this when the issue is ready for a human-applied `jules` label or an API-backed Jules workflow.

Recommended values:

```text
Prepared for: `jules`
Mode: `pr`
Trigger: `manual-label`
Status: `ready-for-agent`
```

### Claude / Codex / Gemini

Use this for routing until a repo-specific adapter exists.

Recommended values:

```text
Prepared for: `claude|codex|gemini`
Mode: `draft|patch|pr`
Trigger: `manual|local-runner|workflow-dispatch`
Status: `ready`
```

### Ollama

Use for local classification, summaries, and cheap review passes.

Recommended values:

```text
Prepared for: `ollama`
Mode: `observe|draft`
Trigger: `local-runner`
Status: `ready`
```

### NotebookLM

Use for source-heavy research. Require write-back into GitHub before relying on the output.

Recommended values:

```text
Prepared for: `notebooklm`
Mode: `observe|draft`
Trigger: `manual`
Status: `ready`
```
