# agent-feed

GitHub org webhook → Cloudflare Worker → `GET /feed` JSON. Lets pull-only LLM
observers (ChatGPT, Gemini, …) read recent ecosystem activity without polling
the GitHub API. Events kept 7 days, newest first, signal-only (issue/PR
lifecycle, comments, reviews, CI **failures**).

## Deploy (once, ~5 min)

```bash
cd agent-feed
npx wrangler kv namespace create FEED        # paste the id into wrangler.toml
npx wrangler secret put WEBHOOK_SECRET       # any strong random string
npx wrangler secret put FEED_TOKEN           # optional: protects GET /feed
npx wrangler deploy                          # note the workers.dev URL
```

## GitHub org webhook (once)

Org **GuitarAlchemist** → Settings → Webhooks → Add:

- Payload URL: `https://ga-agent-feed.<account>.workers.dev/webhook`
- Content type: `application/json`
- Secret: the `WEBHOOK_SECRET` value
- Events: *Let me select* → Issues, Pull requests, Issue comments,
  Pull request reviews, Workflow runs

## Wire ChatGPT

Custom GPT → Actions → import this schema (add an API key auth header
`Authorization: Bearer <FEED_TOKEN>` if you set one):

```yaml
openapi: 3.1.0
info: { title: GA agent feed, version: "1.0" }
servers: [{ url: https://ga-agent-feed.<account>.workers.dev }]
paths:
  /feed:
    get:
      operationId: getRecentActivity
      summary: Recent GitHub activity across the GuitarAlchemist org
      parameters:
        - { name: limit, in: query, schema: { type: integer, maximum: 40 } }
      responses:
        "200": { description: newest-first event list }
```

Any other pull-capable agent can consume the same endpoint.
