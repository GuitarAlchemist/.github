# Product and Project Operating Model

Date: 2026-07-01

This document adapts product management, project management, requirements, software quality, and AI governance standards to the GuitarAlchemist cross-repo GitHub operating model.

## Purpose

Make the issue tree cleaner, more effective, and easier to govern.

The goal is not to copy a heavyweight framework. The goal is to adopt the smallest useful control surface from established standards.

## Standards and reference families

```text
PMI / PMBOK / portfolio-program-project standards
ISO 21502 project management guidance
PRINCE2 business justification, stage control, lessons, roles, tolerances
Scrum Product Goal, Product Backlog, Sprint Goal, Definition of Done
IIBA BABOK business analysis and value delivery
ISO/IEC/IEEE 29148 requirements engineering
ISO/IEC 25010 product quality model
ISO/IEC 42001 AI management system
```

## Operating principles

```text
1. Every issue must explain why it matters.
2. Every structural issue must have hierarchy links.
3. Every project branch must have a value hypothesis.
4. Every implementation PR must have evidence.
5. Every high-impact decision must have a decision gate.
6. Every completed epic must produce a learning artifact.
7. Every metric must be paired with an anti-Goodhart guardrail.
8. Every AI capability must be scoped, evidenced, and time-bound.
```

## Recommended hierarchy

```text
North Star
  -> Product Goal
    -> Value Stream
      -> Outcome
        -> Initiative / Epic
          -> Capability / Feature / Governance Asset
            -> Story / Task
              -> PR
                -> Evidence Packet
                  -> Retrospective / Learning Artifact
```

## GitHub artifact mapping

```text
North Star                = BUSINESS_VALUE_TREE.md
Product Goal             = product-goal issue or roadmap issue
Value Stream             = business value section
Outcome                  = measurable issue outcome
Initiative / Epic        = GitHub epic issue
Capability / Feature     = child issue
Story / Task             = narrow actionable issue
PR                       = implementation artifact
Evidence Packet          = PR review/evidence comment or file
Retrospective            = post-merge retrospective artifact
Learning Artifact        = /teach session, pattern, anti-pattern, or memory update
```

## Issue readiness checklist

An issue is ready only if it has:

```text
clear outcome
business value
parent or explicit reason for being root
related issues
success metric or acceptance signal
risk if ignored
non-goals
routing lane
expected evidence
review mode
```

## Business value block

```markdown
## Business value

Outcome:
-

Value hypothesis:
-

Who benefits:
-

How we know it worked:
-

Risk if ignored:
-
```

## Product goal block

Use this for product-facing or platform-facing epics.

```markdown
## Product goal

Future state:
-

Users / stakeholders:
-

Value delivered:
-

Boundary:
-

Current gap:
-

Measure of progress:
-
```

## Requirements block

Use this when an issue changes behavior, contract, architecture, workflow, or acceptance criteria.

```markdown
## Requirements

Functional requirements:
-

Quality requirements:
-

Constraints:
-

Assumptions:
-

Acceptance criteria:
-

Verification method:
-
```

## Evidence block

Use this for PRs and completed issues.

```markdown
## Evidence

Changed files:
-

Checks:
-

Manual review notes:
-

Risks:
-

Rollback / reversibility:
-

Linked PR / commit:
-
```

## Review mode block

```markdown
## Review mode

Mode:
- silent-classify | batch-digest | fast-review | focused-review | decision-gate | escalate-review

Reason:
-

Human question, if any:
-

Safe default:
-
```

## Stage-gate model

Inspired by project management stage control and product discovery/delivery loops.

```text
0. Capture
   idea, source, context

1. Shape
   outcome, business value, hierarchy, non-goals

2. Validate
   requirements, risks, evidence needed, review mode

3. Delegate
   Jules / Claude / Codex / Human

4. Deliver
   PR, evidence packet, checks

5. Review
   review mode, human question, decision gate if needed

6. Learn
   retrospective, pattern/anti-pattern, /teach artifact if useful

7. Sync
   ISSUE_HIERARCHY.md, BUSINESS_VALUE_TREE.md, MEMORY.md if needed
```

## Portfolio lanes

```text
Product / GA runtime
AFK execution
Governance / Demerzel
TARS runtime and second brain
Teach / Seldon / Streeling
IX math, metrics, and benchmarks
Agent capability attestations
Research backlog
```

## Metrics model

Avoid single-metric optimization. Track a balanced set:

```text
Value        = outcome progress, product readiness, user/stakeholder value
Flow         = issue-to-PR latency, review latency, blocked work
Quality      = defect/rework rate, Definition of Done, acceptance criteria met
Learning     = mastery delta, repeated misconception rate, retrospective reuse
Governance   = review-mode accuracy, decision-gate quality, prompt usefulness
Capability   = attestation scope, evidence quality, benchmark reproducibility
Risk         = uncertainty, reversibility, impact, verification horizon exceeded
```

## Minimum useful templates

```text
Issue Template        = hierarchy + business value + requirements + routing
PR Template           = scope + evidence + review mode + risks + rollback
Epic Review Template  = value delivered + children status + remaining gap
Retrospective Template = what changed + friction + pattern + follow-up
Capability Template   = scope + evidence + benchmark + limitations + expiry
```

## Anti-Goodhart controls

```text
Do not optimize for issue count.
Do not optimize for PR count alone.
Do not optimize for approval speed alone.
Do not treat a benchmark score as project readiness.
Do not treat a learning score as decision authority.
Do not merge governance changes without review-mode justification.
```

## Lightweight adoption plan

### Step 1 — No new bureaucracy

Use comments before changing templates.

### Step 2 — Add templates only after repeated use

If a block is used three times successfully, promote it to a template.

### Step 3 — Automate checks later

A future agent can detect missing blocks:

```text
missing_parent
missing_business_value
missing_metric
missing_risk
missing_non_goals
missing_review_mode
missing_evidence
```

### Step 4 — Keep human authority

The system may classify and recommend. The maintainer decides high-impact priorities, architecture, product boundaries, and value tradeoffs.

## Decision rule

Before creating or expanding an issue, ask:

```text
Does this improve product value, delivery flow, review quality, learning, capability evidence, or governance safety?
```

If not, narrow it, defer it, or convert it into a research note.

## Related artifacts

- `MEMORY.md`
- `ISSUE_HIERARCHY.md`
- `BUSINESS_VALUE_TREE.md`
- `.github#27` Cross-Repo Issue Hierarchy Sync Protocol
