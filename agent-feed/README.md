# agent-feed

Signal-only JSON feed of recent org activity (issue/PR lifecycle, comments,
reviews, CI failures) for pull-only LLM observers (ChatGPT, Gemini, …).

## Variant A — GitHub Actions poller (ACTIVE, zero infra)

[`.github/workflows/agent-feed.yml`](../.github/workflows/agent-feed.yml)
refreshes every 15 min and force-pushes a single-commit data branch:

```text
https://raw.githubusercontent.com/GuitarAlchemist/.github/agent-feed-data/feed.json
```

Shape: `{ generated_at, count, events: [{ts, repo, actor, type, ...}] }`,
newest first, max 60 events, CI events are failures only.

### Wire ChatGPT

- **On demand**: Custom GPT → Actions → import the schema below, or just ask
  ChatGPT (with browsing) to read the URL.
- **Monitoring**: ChatGPT Tasks → "every morning, fetch this URL and notify me
  only if there are CI failures, agent-opened PRs, or ready-for-agent issues;
  report as risk + recommended action per item."

```yaml
openapi: 3.1.0
info: { title: GA agent feed, version: "1.0" }
servers: [{ url: https://raw.githubusercontent.com }]
paths:
  /GuitarAlchemist/.github/agent-feed-data/feed.json:
    get:
      operationId: getRecentActivity
      summary: Recent GitHub activity across the GuitarAlchemist org
      responses:
        "200": { description: newest-first event list }
```

## Variant B — Cloudflare Worker webhook (optional upgrade, sub-minute)

`worker.js` + `wrangler.toml` here: org webhook → HMAC-verified receiver → KV
(7-day TTL) → `GET /feed`. Same event schema. Deploy only if 15-min freshness
stops being enough:

```bash
npx wrangler kv namespace create FEED        # id → wrangler.toml
npx wrangler secret put WEBHOOK_SECRET
npx wrangler secret put FEED_TOKEN           # optional read gate
npx wrangler deploy
```

Then add the org webhook (Issues, Pull requests, Issue comments, PR reviews,
Workflow runs → `https://<worker>/webhook`, content type JSON, the secret).
