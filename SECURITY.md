# Security Policy

Guitar Alchemist is a multi-repository laboratory for building software with AI
agents in the loop. Security here covers two surfaces at once: **conventional
software** (code, dependencies, web surfaces) and **agentic infrastructure** (AI
workers, MCP servers, automation runners, and the GitHub control plane itself).

This policy is an organization default and applies to every repository under
`GuitarAlchemist` unless that repository publishes its own `SECURITY.md`.

## Reporting a vulnerability

Please report security issues **privately**. Do not open a public issue,
discussion, or pull request for a suspected vulnerability.

Preferred channels, in order:

1. **GitHub private vulnerability reporting** — on the affected repository, go to
   the **Security** tab → **Report a vulnerability** (GitHub Security
   Advisories). This keeps the report private and attached to the repo.
2. **Email** — if private reporting is unavailable, contact
   **spareilleux@gmail.com** with `SECURITY` in the subject line.

Please include, where you can:

- the affected repository, branch, commit, or URL;
- a description of the issue and its impact;
- reproduction steps or a proof of concept;
- relevant logs, requests, or screenshots (with secrets redacted).

## What to expect

This is a small, actively-maintained lab, not a 24/7 security operation.
Best-effort targets:

- acknowledgement within **5 business days**;
- an initial assessment and severity triage shortly after;
- coordinated disclosure once a fix or mitigation is available.

We welcome good-faith security research. If you avoid privacy violations, data
destruction, and service disruption, and give us reasonable time to respond, we
will not pursue action against you for your research.

## Scope

In scope:

- source code across `GuitarAlchemist` repositories;
- public web/demo surfaces (e.g. the demo site and component demos);
- CI/CD workflows, GitHub Actions, and automation runners;
- MCP servers, agent adapters, and tool integrations operated by this org.

Out of scope:

- third-party services and dependencies (report those upstream);
- findings that require a compromised maintainer machine or stolen credentials;
- volumetric denial-of-service and social engineering of maintainers.

## Agent- and MCP-specific security

Because this organization runs AI workers and Model Context Protocol (MCP)
servers as part of normal development, the threat model is broader than a typical
repository. We are especially interested in reports about:

- **MCP servers as attack surface** — every tool adapter is a trust boundary.
  Missing permission limits, secret leakage, unaudited tool calls, or over-broad
  write access.
- **Prompt injection** — content in issues, PRs, comments, CI logs, or fetched
  web data that manipulates an agent into actions a maintainer would not expect
  (scope escalation, secret exfiltration, governance bypass).
- **Secret handling** — secrets committed to issues, PRs, logs, or artifacts;
  tokens scoped more broadly than needed; secrets reachable by an agent runner.
- **Governance bypass** — automation paths that could merge, escalate
  privileges, or change policy files without the human/Demerzel review gates the
  organization requires.

## Secrets hygiene (for everyone, including agents)

- Never put credentials, tokens, private hostnames, or personal data in issues,
  PRs, comments, or commits.
- Treat anything posted to GitHub as effectively public and permanent.
- Agent-generated changes must not introduce secrets and must not weaken review
  gates. See the [agent delegation contract](docs/agents/agent-delegation-contract.md).

## Supported versions

Development is rolling. Security fixes target the **default branch** of each
repository. There are no long-lived maintenance branches unless a repository
states otherwise.
