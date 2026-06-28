# GitHub Projects operating model

This document defines how GuitarAlchemist GitHub Projects should be fleshed out so the organization has an operational portfolio view across repositories.

Issues remain the source of truth. GitHub Projects provide portfolio views, fields, sequencing, prioritization, review/backpressure visibility, and agent-delegation tracking.

## Current anchors

- `GuitarAlchemist/.github#5` — organization roadmap and repository hierarchy.
- `GuitarAlchemist/.github#6` — portable issue metadata standard.
- `GuitarAlchemist/.github#9` — AIW / Jules / AFK coordination rollup.
- `GuitarAlchemist/Demerzel#473` — AI Workforce roadmap and issue hierarchy.
- `GuitarAlchemist/Demerzel#475` — cross-repo issue triage router.

## Recommended Projects

### 1. Organization Portfolio

Purpose: maintainer-level view of all major streams across GuitarAlchemist.

Suggested views:

1. **Roadmap** — group by `Area`, sort by `Priority`.
2. **Now / Next / Later** — group by `Time horizon`.
3. **By repository** — group by `Repository`.
4. **Risk & review** — filter `Risk = high|critical` or `Review state != not-needed`.
5. **Agent work** — filter `Preferred worker` contains an AI worker.
6. **Blocked** — filter `Status = Blocked`.

### 2. AI Workforce / Demerzel

Purpose: operating board for Jules / Claude / Codex / local-worker coordination.

Suggested views:

1. **AIW Roadmap** — PI → epic → story → task.
2. **Jules batches** — group by `Agent batch`.
3. **AFK readiness** — group by `AFK readiness`.
4. **Worker routing** — group by `Preferred worker`.
5. **Review pressure** — group by `Review state`.
6. **Risk gates** — filter high/critical or governance-touching issues.

### 3. Product / Guitar Alchemist

Purpose: product-facing roadmap for music theory, fretboard, WebGPU, visualization, demos, and public site work.

Suggested views:

1. **Product roadmap** — group by product area.
2. **Demos** — demo-ready issues and public surfaces.
3. **Rendering / WebGPU** — graphics-heavy work.
4. **Music theory engine** — scale/chord/progression/data work.
5. **Performance** — FPS, latency, bundle size, rendering improvements.

### 4. Research / Runtime

Purpose: research and runtime board across TARS, IX, Hari, and supporting repos.

Suggested views:

1. **Runtime roadmap** — TARS / IX / Hari initiatives.
2. **Research queue** — ideas not yet shaped.
3. **Ready for implementation** — shaped tasks with tests/non-goals.
4. **Agent-ready** — issues that may be delegated after readiness gates.

## Core Project fields

Use these fields consistently across Projects.

| Field | Type | Suggested values |
|---|---|---|
| `Area` | single select | `aiw`, `governance`, `product`, `runtime`, `music`, `rendering`, `research`, `infra`, `docs`, `evals`, `bot` |
| `Repository` | single select/text | `Demerzel`, `ga`, `tars`, `ix`, `hari`, `agent-blackbox`, `demerzel-bot`, `.github`, `guitaralchemist.github.io` |
| `Level` | single select | `PI`, `Epic`, `Story`, `Task`, `Subtask` |
| `Parent` | text | `owner/repo#123` |
| `Priority` | single select | `P0`, `P1`, `P2`, `P3` |
| `Complexity` | single select | `XS`, `S`, `M`, `L`, `XL` |
| `Risk` | single select | `low`, `medium`, `high`, `critical` |
| `Status` | single select | `Inbox`, `Shaping`, `Ready`, `Ready for agent`, `Agent running`, `PR open`, `Review`, `Blocked`, `Done`, `Parked` |
| `Time horizon` | single select | `Now`, `Next`, `Later`, `Someday`, `Parked` |
| `AFK readiness` | single select | `none`, `observe`, `draft`, `patch`, `pr`, `harvest`, `blocked` |
| `Preferred worker` | multi select | `human`, `demerzel`, `jules`, `claude`, `codex`, `ollama`, `notebooklm`, `gemini`, `augment` |
| `Agent batch` | single select | `batch-1`, `batch-2`, `later`, `blocked`, `not-agent-work` |
| `Review state` | single select | `not-needed`, `needs-human`, `needs-adversarial-review`, `needs-governance`, `approved`, `changes-requested` |
| `Blocked reason` | text | short human-readable blocker |
| `Evidence` | text | links to PR, logs, report, doc, artifact |

## Status mapping

Recommended status transitions:

```text
Inbox
  -> Shaping
  -> Ready
  -> Ready for agent
  -> Agent running
  -> PR open
  -> Review
  -> Done
```

Blocked work may move to `Blocked` from any state. Work that is intentionally deferred moves to `Parked`.

## AIW/Jules batch mapping

Use this in the AI Workforce / Demerzel Project:

| Batch | Issues | Project values |
|---|---|---|
| Batch 1 | `Demerzel#463`, `#465`, `#467` | `Agent batch = batch-1`, `Status = Ready for agent`, `Preferred worker = jules`, `Review state = needs-human` |
| Batch 2 | `Demerzel#459`, `#461`, `#471` | `Agent batch = batch-2`, `Status = Ready`, `Preferred worker = jules`, `Review state = needs-human` |
| Later | `Demerzel#457`, `#455`, `#469`, `#473`, `#475` | `Agent batch = later`, `Status = Ready`, `Preferred worker = jules|human`, `Review state = needs-human` |

Do not move Batch 2 to `Ready for agent` until Batch 1 PRs have reviewable evidence.

## Product board seed

Initial product streams:

- Fretboard intelligence
- Music theory data and scale/chord/progression systems
- WebGPU / Three.js / PixiJS rendering
- Guitar model / strings / materials / animation
- Hand pose and performance assistance
- Public demos and website
- Sound / strumming / synthesis experiments

## Research/runtime board seed

Initial runtime streams:

- TARS V2 agentic runtime
- TARS cloud-agent observability
- IX scoring / blast-radius / algorithmic primitives
- Hari high-uncertainty recommendations
- Cross-repo memory and research loops
- MCP / A2A surfaces
- Agent-ready issue factory

## Maintenance rules

- Every Project item should link to a GitHub issue or PR when possible.
- Large free-form notes should become issues, not Project-only cards.
- `Priority`, `Risk`, `Status`, and `Time horizon` should be filled for P0/P1 items.
- `AFK readiness`, `Preferred worker`, and `Agent batch` should be filled for agent-delegated work.
- Do not treat Project fields as stronger than repo policy; Demerzel governance still wins.

## Manual setup checklist

Because Project automation is not available through the current connector, set this up manually in GitHub UI:

1. Create or update the four Projects above.
2. Add the core fields listed in this document.
3. Add saved views for each Project.
4. Add `.github#5`, `.github#6`, `.github#9`, `Demerzel#473`, and `Demerzel#475` to the Organization Portfolio.
5. Add the AIW/Jules issues to the AI Workforce / Demerzel Project.
6. Add active `ga` / product issues to Product / Guitar Alchemist.
7. Add active `tars`, `ix`, and `hari` issues to Research / Runtime.
8. Review once per week and keep Project-only notes to a minimum.
