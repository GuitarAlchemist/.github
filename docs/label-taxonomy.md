# Label Taxonomy

This document defines the standardized label groups and their values used across the Guitar Alchemist organization.

## Label Groups

### Priority
`priority:P0` / `priority:P1` / `priority:P2` / `priority:P3`

### Risk
`risk:low` / `risk:medium` / `risk:high`

### Complexity
`complexity:XS` / `complexity:S` / `complexity:M` / `complexity:L` / `complexity:XL`

### Area
`area:runtime` / `area:research` / `area:governance` / `area:product` / `area:docs` / `area:infra`

### AFK (Away From Keyboard)
`afk:ready` / `afk:candidate` / `afk:blocked`

### Routing
`routing:shape` / `routing:loop` / `routing:fix` / `routing:docs` / `routing:research` / `routing:infra`

### Worker
`worker:jules` / `worker:claude-code` / `worker:ollama-local` / `worker:human-review`

---

## Usage Guidelines

- Labels should be applied by the triage router or by human maintainers.
- The `afk:*` labels indicate the state of an issue for autonomous agent pickup.
- The `worker:*` labels are used to assign or prefer specific agents or humans for a task.
- These labels are intended to mirror the values found in the `issue_meta` block for easy filtering in the GitHub UI.
