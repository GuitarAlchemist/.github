# Cross-Repo Issue Triage Session

Date: 2026-07-01

Scope: best-effort audit of open GitHub issues across the visible GuitarAlchemist repositories.

Repos inspected:

```text
GuitarAlchemist/.github
GuitarAlchemist/tars
GuitarAlchemist/ix
GuitarAlchemist/Demerzel
GuitarAlchemist/ga
GuitarAlchemist/guitaralchemist.github.io
GuitarAlchemist/demerzel-bot
GuitarAlchemist/guitar-singularity
GuitarAlchemist/hari
GuitarAlchemist/ga-godot
GuitarAlchemist/ga-legacy
GuitarAlchemist/agent-blackbox
```

## Triage principles

```text
Do not spam every issue with comments.
Prefer central triage report first.
Close only with implementation evidence.
Treat .github as the operating cockpit.
Treat Demerzel lifecycle/state-machine epics as canonical for policy.
Treat TARS as reasoning/teach/second-brain.
Treat IX as metrics/math/scoring.
Treat GA and satellites as product consumers.
```

## Executive summary

The issue graph is coherent but has three kinds of debt:

```text
1. Fresh operating-system work in .github is active and should remain open.
2. Several older roadmap/PI issues still point to .github#5/#6 and need later migration to the new hierarchy/business-value model.
3. GA has urgent live-demo/smoke and local stash issues that should be handled before expanding product backlog work.
```

## Priority queue

### P0 — Handle now / next

| Issue | Triage | Reason |
|---|---|---|
| `GuitarAlchemist/ga#493` | active incident | Latest live demo regression, status 530 on multiple URLs. |
| `GuitarAlchemist/ga#491` | local cleanup | Local stash inventory can block clean reconcile work. |
| `GuitarAlchemist/.github#28` | active infra audit | Methodology Guard rollout still needs live artifact review and multiline confirmation. |
| `GuitarAlchemist/.github#30` | active abstraction epic | New abstraction lifecycle needs registry example and first candidates. |
| `GuitarAlchemist/Demerzel#588` | canonical parent | Policy engine + lifecycle state machines remain authoritative. |
| `GuitarAlchemist/Demerzel#592` | canonical child | Lifecycle catalog should receive state-machine semantics, not be duplicated in `.github`. |

### P1 — High leverage next

| Issue | Triage | Reason |
|---|---|---|
| `GuitarAlchemist/tars#166` | delegate docs/examples | First `/teach` lesson pack, narrow and Jules-friendly. |
| `GuitarAlchemist/tars#167` | design artifact | Persist `/teach` sessions into second brain. |
| `GuitarAlchemist/tars#168` | design artifact | Agent capability attestations. |
| `GuitarAlchemist/tars#169` | curriculum/catalog | Streeling PhD-grade curriculum. |
| `GuitarAlchemist/ix#217` | metrics foundation | Learning mastery metrics for `/teach`. |
| `GuitarAlchemist/ix#218` | metrics/tooling map | PhD-grade ML/math tooling backlog. |
| `GuitarAlchemist/ix#216` | governance metric | Human attention/rubber-stamp measurement. |
| `GuitarAlchemist/tars#162` | integration epic | Intent verification from IX + Demerzel. |
| `GuitarAlchemist/tars#163` | integration story | Review-mode verdict. |
| `GuitarAlchemist/hari#12` | research engine parent | Epistemic-state engine boundary is relevant to TARS/IX/Demerzel. |
| `GuitarAlchemist/agent-blackbox#38` | evaluation roadmap | Relevant to Methodology Guard and agent capability evidence. |

### P2 — Keep, but do not expand until P0/P1 stabilize

| Issue | Triage | Reason |
|---|---|---|
| `GuitarAlchemist/ga#482` | product roadmap parent | Keep as GA product tree, later migrate hierarchy/value blocks. |
| `GuitarAlchemist/guitaralchemist.github.io#10` | docs/site roadmap | Keep as public docs lane. |
| `GuitarAlchemist/guitar-singularity#1` | music roadmap | Keep parked until GA/TARS/IX stabilizes. |
| `GuitarAlchemist/demerzel-bot#6` | bot roadmap | Keep parked until Demerzel lifecycle/policy matures. |
| `GuitarAlchemist/ga-godot#3` | visualization roadmap | Keep parked; useful future Prime Radiant direction. |
| `GuitarAlchemist/hari#11` | PI parent | Keep as HARI roadmap parent. |

### P3 / parked / evidence-gated

| Issue | Triage | Reason |
|---|---|---|
| `GuitarAlchemist/ga#448` | demand-gated | One-way-door OPTK reindex; should wait for telemetry evidence. |
| `GuitarAlchemist/ga#42` | opportunistic perf | Useful but product incident and workflow guard have higher priority. |
| `GuitarAlchemist/ga#47`-`#56` | portfolio backlog | Mostly panels/integrations; group under GA roadmap before action. |
| `GuitarAlchemist/ga#328` | environment-dependent QA | Hosted runner lacks local dependencies; needs classification as infra limitation or local-only check. |

## Duplicate / supersession candidates

### GA live-demo regression issues

```text
GuitarAlchemist/ga#493 appears to be the latest live-demo regression.
GuitarAlchemist/ga#461 is an older live-demo regression on a previous merge commit.
```

Recommendation:

```text
Do not close automatically yet.
First confirm whether #461 is fully superseded by #493 or documents a separate historical incident.
If superseded, comment on #461 and close with state: closed only.
```

### Old roadmap metadata issues

Several PI roadmap issues still reference older `.github#5` and `.github#6` metadata patterns.

Recommendation:

```text
Do not rewrite all bodies now.
Create a migration pass later:
- add hierarchy block
- add business value block
- add scope/boundary block
- link to ISSUE_HIERARCHY.md and BUSINESS_VALUE_TREE.md
```

## Recommended next actions

### Immediate

```text
1. Triage `ga#493` as current product incident.
2. Triage `ga#491` local stash cleanup.
3. Finish `.github#30` deliverables:
   - registry example
   - first abstraction candidates
   - report schema
4. Review first Methodology Guard artifacts from `.github` and `tars`.
```

### Delegation candidates

```text
Jules:
- `tars#166` lesson pack docs/examples
- `.github#30` abstraction registry examples
- Methodology Guard fixture docs

Claude:
- critique `.github#30` promotion gates
- critique Demerzel#588/#592 alignment
- split GA portfolio issues #47-#56 into a clean dashboard integration roadmap

Codex:
- later deterministic abstraction-candidate checker prototype
- later Methodology Guard state-suggestion prototype

Human:
- decide whether GA live demo regression is P0 product incident
- decide when to install Methodology Guard in IX/Demerzel
- decide whether artifact-only remains enough or digest comments are needed
```

## Proposed issue state buckets

```text
Now:
- ga#493
- ga#491
- .github#28
- .github#30

Next:
- tars#166
- tars#167
- ix#217
- ix#218
- Demerzel#588/#592 alignment

Hold:
- GA panel backlog #47-#56
- guitar-singularity#1
- demerzel-bot#6
- ga-godot#3

Evidence-gated:
- ga#448
- ga#328
```

## Follow-up issue candidates

```text
[Story] Add abstraction registry examples for .github#30
[Story] Review Methodology Guard live artifacts from .github/tars
[Story] Migrate old PI roadmap issues to new hierarchy/business-value/scope model
[Story] Consolidate GA live-demo regression issues
[Story] Split GA governance dashboard panel backlog into coherent roadmap slices
```

## Non-actions taken

```text
No mass issue comments.
No issue closures.
No label changes.
No body rewrites across repos.
```

Reason: this was an audit/triage session, and broad mutation would create noise before the triage decisions are confirmed.
