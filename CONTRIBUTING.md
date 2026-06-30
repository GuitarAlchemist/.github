# Contributing to Guitar Alchemist

Thanks for your interest. This file is an organization default and applies across
`GuitarAlchemist` repositories. Individual repos may add their own
`CONTRIBUTING.md` or developer docs (for example, `ga` has a detailed
`CLAUDE.md` / `AGENTS.md`); when a repo-specific document exists, it wins for
that repo.

## Operating principles

This is a working lab for **agentic engineering**, so a few principles shape how
we work:

- **GitHub is the control plane.** Issues, labels, PRs, checks, and comments are
  the shared operational record.
- **Work is bounded.** A good task has scope, non-goals, allowed paths, test
  commands, evidence requirements, and stop conditions.
- **Evidence beats confidence.** A useful contribution includes diffs, tests,
  logs, and a link back to its issue.
- **Small batches win.** Thin vertical slices over big-bang changes. Don't open
  more work than can be reviewed.
- **Governance is separate from execution.** Anyone — human or agent — can
  propose changes; review decides what advances.

## Before you start

1. **Find or open an issue.** Use the org issue templates (`Epic`, `Story`,
   `Task`, `Agent-ready task`). Non-trivial work should be backed by an issue,
   not a Project-only card.
2. **Add metadata.** Important issues carry an `issue_meta` block — see
   [`docs/issue-meta.schema.md`](docs/issue-meta.schema.md). Labels mirror those
   fields — see [`docs/label-taxonomy.md`](docs/label-taxonomy.md).
3. **Link the hierarchy.** Reference the parent (`PI → Epic → Story → Task →
   Subtask`) and the org roadmap
   ([`.github#5`](https://github.com/GuitarAlchemist/.github/issues/5)) where
   relevant.

## Making changes

- **Branch** off the repository's default branch. Keep branches focused on one
  issue.
- **Tracer-bullet first.** For a non-trivial feature, build the smallest
  end-to-end slice that touches every layer, verify it, then expand. Decompose
  vertically (a thin slice through all layers), not horizontally (one layer at a
  time).
- **Commits** follow [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, …).
- **Verify before claiming success.** Run the repository's build, tests, and
  linters, and include the evidence.

## Pull requests

A reviewable PR includes:

- a **linked issue**;
- a **minimal scope summary** and the **list of changed files**;
- **validation evidence** (build/test/lint output, screenshots for UI);
- **risk notes** and any unresolved questions;
- **no secrets**, no governance bypass, and no broad refactor unless explicitly
  authorized.

These are the same acceptance criteria we apply to agent-generated PRs — they
make review fast for everyone.

## Contributing as (or with) an AI agent

This organization delegates work to AI workers under an explicit contract. If you
are operating an agent, or staging an issue for one, follow:

- [`docs/agents/agent-delegation-contract.md`](docs/agents/agent-delegation-contract.md)
  — delegation levels, worker classes, readiness checklist, stop conditions.

Agents may propose work. They do not own governance, risk escalation, or merge
authority.

## Code of conduct

By participating you agree to abide by our
[Code of Conduct](CODE_OF_CONDUCT.md).

## Security

Never post secrets in issues, PRs, or commits. To report a vulnerability, see
[`SECURITY.md`](SECURITY.md).

## Questions

Open a [GitHub Discussion](https://github.com/orgs/GuitarAlchemist/discussions)
or contact spareilleux@gmail.com.
