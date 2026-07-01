// agent-feed — GitHub org webhook receiver + JSON feed for LLM observers.
//
// POST /webhook  : GitHub org webhook target (HMAC-verified, WEBHOOK_SECRET).
// GET  /feed     : last N events, newest first (Bearer FEED_TOKEN if set).
//
// Storage: one KV entry per event, 7-day TTL, reverse-chronological keys so
// a prefix list returns newest first without an index.

const EVENT_TTL_SECONDS = 7 * 24 * 3600;
const MAX_FEED_LIMIT = 40;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method === "POST" && url.pathname === "/webhook") {
      return handleWebhook(request, env);
    }
    if (request.method === "GET" && url.pathname === "/feed") {
      return handleFeed(request, env, url);
    }
    return json({ usage: "POST /webhook (GitHub), GET /feed?limit=N" }, 404);
  },
};

async function handleWebhook(request, env) {
  const body = await request.text();
  const signature = request.headers.get("X-Hub-Signature-256");
  if (!(await verifySignature(env.WEBHOOK_SECRET, body, signature))) {
    return json({ error: "bad signature" }, 401);
  }

  const eventType = request.headers.get("X-GitHub-Event") || "unknown";
  const deliveryId = request.headers.get("X-GitHub-Delivery") || crypto.randomUUID();
  let payload;
  try {
    payload = JSON.parse(body);
  } catch {
    return json({ error: "bad json" }, 400);
  }

  const summary = summarize(eventType, payload);
  if (!summary) return json({ ok: true, stored: false });

  const record = {
    ts: new Date().toISOString(),
    repo: payload.repository?.full_name ?? payload.organization?.login ?? null,
    actor: payload.sender?.login ?? null,
    ...summary,
  };

  // Reverse-sortable key: newest events list first under the evt: prefix.
  const seq = String(1e13 - Date.now()).padStart(13, "0");
  await env.FEED.put(`evt:${seq}:${deliveryId}`, JSON.stringify(record), {
    expirationTtl: EVENT_TTL_SECONDS,
  });
  return json({ ok: true, stored: true });
}

async function handleFeed(request, env, url) {
  if (env.FEED_TOKEN) {
    const auth = request.headers.get("Authorization") || "";
    if (auth !== `Bearer ${env.FEED_TOKEN}`) {
      return json({ error: "unauthorized" }, 401);
    }
  }
  const limit = Math.min(
    Math.max(parseInt(url.searchParams.get("limit") || "25", 10) || 25, 1),
    MAX_FEED_LIMIT,
  );
  const list = await env.FEED.list({ prefix: "evt:", limit });
  const events = [];
  for (const key of list.keys) {
    const value = await env.FEED.get(key.name, "json");
    if (value) events.push(value);
  }
  return json({ count: events.length, events });
}

// Only signal, not firehose: issue/PR lifecycle, comments, reviews, CI failures.
function summarize(eventType, p) {
  switch (eventType) {
    case "issues": {
      if (!["opened", "closed", "reopened", "labeled"].includes(p.action)) return null;
      return {
        type: "issue",
        action: p.action,
        number: p.issue.number,
        title: p.issue.title,
        label: p.label?.name,
        url: p.issue.html_url,
      };
    }
    case "pull_request": {
      if (!["opened", "closed", "reopened", "ready_for_review"].includes(p.action)) return null;
      const action =
        p.action === "closed" ? (p.pull_request.merged ? "merged" : "closed") : p.action;
      return {
        type: "pr",
        action,
        number: p.number,
        title: p.pull_request.title,
        url: p.pull_request.html_url,
      };
    }
    case "issue_comment": {
      if (p.action !== "created") return null;
      return {
        type: "comment",
        number: p.issue.number,
        title: p.issue.title,
        snippet: (p.comment.body || "").slice(0, 200),
        url: p.comment.html_url,
      };
    }
    case "pull_request_review": {
      if (p.action !== "submitted") return null;
      return {
        type: "review",
        state: p.review.state,
        number: p.pull_request.number,
        title: p.pull_request.title,
        url: p.review.html_url,
      };
    }
    case "workflow_run": {
      if (p.action !== "completed") return null;
      if (p.workflow_run.conclusion !== "failure") return null;
      return {
        type: "ci",
        workflow: p.workflow_run.name,
        conclusion: p.workflow_run.conclusion,
        branch: p.workflow_run.head_branch,
        url: p.workflow_run.html_url,
      };
    }
    default:
      return null;
  }
}

async function verifySignature(secret, body, signature) {
  if (!secret || !signature || !signature.startsWith("sha256=")) return false;
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const mac = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(body));
  const expected =
    "sha256=" +
    [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, "0")).join("");
  if (expected.length !== signature.length) return false;
  let diff = 0;
  for (let i = 0; i < expected.length; i++) {
    diff |= expected.charCodeAt(i) ^ signature.charCodeAt(i);
  }
  return diff === 0;
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj, null, 2), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}
