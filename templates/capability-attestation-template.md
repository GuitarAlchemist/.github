# Capability Attestation Template

Use this template to document a narrow AI agent/model/tool capability with evidence.

This is an internal engineering attestation, not an official external certification.

## Metadata

```yaml
attestation_id: ""
subject_agent: ""
model_id_or_tool_id: ""
version: ""
scope: ""
level: "observed | practiced | benchmarked | reviewed | trusted-scope | expired"
issued_at: ""
review_due: ""
status: "active | expired | revoked | superseded"
```

## Capability claim

The agent/model/tool can:
-

Within this scope:
-

It should not be used for:
-

## Evidence

Teach sessions:
-

Scenario results:
-

Benchmarks or evals:
-

Model/dataset/eval cards:
-

PRs or artifacts:
-

Human or agent review notes:
-

## Limitations

Known weaknesses:
-

Unverified assumptions:
-

Failure modes:
-

## Risk and review mode

Impact if wrong:
-

Reversibility:
-

Recommended review mode:
-

Human decision needed:
-

## Expiry / reassessment

Review due:
-

Reassess when:
-

Revocation triggers:
-

## Decision

Attestation decision:
- <!-- issue | deny | defer | expire | revoke -->

Reason:
-

Next step:
-

## Non-goals

- Do not claim legal, regulatory, ISO, or vendor certification.
- Do not treat benchmark rank as project readiness.
- Do not allow high-impact autonomous action from this artifact alone.
