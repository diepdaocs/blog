---
layout: single
title: "Project: @diepdao/aicli — API Docs CLI for AI Copilots"
date: 2026-03-14 10:00:00 +0800
permalink: /projects/aicli-npm-tool/
categories:
  - ai
  - projects
tags:
  - cli
  - npm
  - developer-tools
  - copilot
  - claude
  - open-source
  - api-docs
  - kafka
  - redis
  - clickhouse
---

A global npm CLI that gives AI copilots (GitHub Copilot, Claude, Cursor) instant access to the latest API documentation for any open-source tool — Kafka, Redis, ClickHouse, and more — without hallucination, without stale training data.

Inspired by [@aisuite/chub](https://github.com/andrewyng/context-hub), `@diepdao/aicli` follows the same philosophy: fetch live, accurate docs on demand, and hand them to your AI agent in a structured format it can immediately use.

GitHub: *(link coming soon)*

---

## The Problem

AI copilots are trained on snapshots. By the time you're using them, their knowledge of `kafka-js@2.x`, `ClickHouse HTTP API v24`, or `redis@5` may already be outdated. The copilot confidently generates code that calls APIs that no longer exist, with parameters that have been renamed, against endpoints that have moved.

The fix isn't a bigger model — it's **retrieval at prompt time**.

---

## What `aicli` Does

```bash
npm install -g @diepdao/aicli

aicli help                          # show available commands and topics
aicli search kafka                  # find available doc topics for kafka
aicli get kafka/producer --lang js  # fetch producer API docs (JavaScript)
aicli get redis/commands            # fetch Redis command reference
aicli get clickhouse/http-api       # fetch ClickHouse HTTP API docs
```

The copilot runs these commands, gets the current docs as structured text, and uses them to generate accurate code — no guessing, no hallucination.

---

## How It Works

### Architecture

<img src="/assets/images/arch-aicli.svg" alt="@diepdao/aicli Architecture" style="width:100%;max-width:820px;margin:1rem auto;display:block;border-radius:8px;">

The CLI has three layers:

1. **Registry** — an index of known tools and their doc topics (`kafka/producer`, `redis/commands`, etc.)
2. **Fetcher** — pulls documentation from official sources (GitHub, official docs sites), parses and normalises it
3. **Formatter** — outputs clean Markdown to stdout so it fits directly into a copilot context window

---

## Project Structure

```
aicli/
├── bin/
│   └── aicli.js          # CLI entry point (shebang, commander setup)
├── src/
│   commands/
│   ├── search.js         # aicli search <tool>
│   ├── get.js            # aicli get <tool/topic>
│   └── help.js           # aicli help
│   ├── registry/
│   │   └── index.json    # tool → topics → source URL mapping
│   ├── fetcher/
│   │   ├── http.js       # HTTP doc fetcher
│   │   ├── github.js     # GitHub README / docs fetcher
│   │   └── cache.js      # local TTL cache (~/.aicli/cache/)
│   └── formatter/
│       └── markdown.js   # normalise to Markdown for LLM context
├── SKILL.md              # Claude / Copilot skill descriptor
├── package.json
└── README.md
```

---

## Building It

### 1. Scaffold the package

```bash
mkdir aicli && cd aicli
npm init -y
npm install commander axios cheerio marked
npm install --save-dev jest
```

`package.json` key fields:

```json
{
  "name": "@diepdao/aicli",
  "version": "1.0.0",
  "bin": {
    "aicli": "./bin/aicli.js"
  },
  "files": ["bin", "src", "SKILL.md"],
  "engines": { "node": ">=18" }
}
```

### 2. CLI entry point

```js
// bin/aicli.js
#!/usr/bin/env node
import { program } from 'commander';
import { searchCommand } from '../src/commands/search.js';
import { getCommand }    from '../src/commands/get.js';
import { helpCommand }   from '../src/commands/help.js';

program
  .name('aicli')
  .description('Fetch latest API docs for open-source tools — built for AI copilots')
  .version('1.0.0');

program
  .command('search <tool>')
  .description('List available doc topics for a tool')
  .action(searchCommand);

program
  .command('get <topic>')
  .description('Fetch docs for a topic (e.g. kafka/producer)')
  .option('--lang <lang>', 'language variant (js, py, java, go)', 'js')
  .option('--no-cache', 'bypass local cache')
  .action(getCommand);

program
  .command('help [topic]')
  .description('Show usage guide or explain a topic')
  .action(helpCommand);

program.parse();
```

### 3. Doc registry

```json
// src/registry/index.json
{
  "kafka": {
    "producer":  "https://kafka.js.org/docs/producing",
    "consumer":  "https://kafka.js.org/docs/consuming",
    "admin":     "https://kafka.js.org/docs/admin"
  },
  "redis": {
    "commands":  "https://redis.io/commands/",
    "streams":   "https://redis.io/docs/data-types/streams/",
    "pubsub":    "https://redis.io/docs/manual/pubsub/"
  },
  "clickhouse": {
    "http-api":  "https://clickhouse.com/docs/en/interfaces/http",
    "sql":       "https://clickhouse.com/docs/en/sql-reference",
    "client-js": "https://clickhouse.com/docs/en/integrations/javascript"
  }
}
```

### 4. Fetcher with local cache

```js
// src/fetcher/cache.js
import fs from 'fs';
import path from 'path';
import os from 'os';

const CACHE_DIR = path.join(os.homedir(), '.aicli', 'cache');
const TTL_MS = 24 * 60 * 60 * 1000; // 24 hours

export function readCache(key) {
  const file = path.join(CACHE_DIR, encodeURIComponent(key) + '.json');
  if (!fs.existsSync(file)) return null;
  const { ts, content } = JSON.parse(fs.readFileSync(file, 'utf8'));
  return Date.now() - ts < TTL_MS ? content : null;
}

export function writeCache(key, content) {
  fs.mkdirSync(CACHE_DIR, { recursive: true });
  const file = path.join(CACHE_DIR, encodeURIComponent(key) + '.json');
  fs.writeFileSync(file, JSON.stringify({ ts: Date.now(), content }));
}
```

```js
// src/fetcher/http.js
import axios from 'axios';
import * as cheerio from 'cheerio';
import { readCache, writeCache } from './cache.js';

export async function fetchDocs(url, { noCache = false } = {}) {
  if (!noCache) {
    const cached = readCache(url);
    if (cached) return cached;
  }

  const { data } = await axios.get(url, {
    headers: { 'User-Agent': 'aicli/1.0 (AI copilot doc fetcher)' },
    timeout: 10_000,
  });

  const $ = cheerio.load(data);
  // strip nav, footer, ads — keep main content
  $('nav, footer, header, script, style, .sidebar').remove();
  const text = $('main, article, .content, body').first().text().trim();

  writeCache(url, text);
  return text;
}
```

### 5. The `get` command

```js
// src/commands/get.js
import registry from '../registry/index.json' assert { type: 'json' };
import { fetchDocs } from '../fetcher/http.js';

export async function getCommand(topic, opts) {
  const [tool, subtopic] = topic.split('/');

  if (!registry[tool]) {
    console.error(`Unknown tool: ${tool}. Run 'aicli search' to see available tools.`);
    process.exit(1);
  }

  const url = registry[tool][subtopic];
  if (!url) {
    console.error(`Unknown topic '${subtopic}' for ${tool}.`);
    console.log(`Available: ${Object.keys(registry[tool]).join(', ')}`);
    process.exit(1);
  }

  console.log(`# ${tool} / ${subtopic}\nSource: ${url}\n`);
  const docs = await fetchDocs(url, { noCache: !opts.cache });
  console.log(docs);
}
```

---

## SKILL.md — Integrating with Claude and Copilot

This file tells the AI agent how and when to use `aicli`. Place it at `~/.claude/skills/aicli/SKILL.md` for Claude Code, or reference it in your Copilot workspace instructions.

```markdown
# aicli — API Documentation Fetcher

## When to use
Use `aicli` whenever you need current API documentation for an open-source
tool. Prefer this over relying on training knowledge for:
- Library APIs that change between versions (Kafka, Redis, ClickHouse, etc.)
- HTTP interfaces and SDK methods
- Configuration options and connection parameters

## Install
npm install -g @diepdao/aicli

## Commands

### Discover available topics
aicli search <tool>
# Example: aicli search kafka

### Fetch documentation
aicli get <tool>/<topic> [--lang <js|py|java|go>]
# Example: aicli get kafka/producer --lang js
# Example: aicli get redis/commands
# Example: aicli get clickhouse/http-api

### General help
aicli help

## Workflow
1. Run `aicli search <tool>` to see what topics are available
2. Run `aicli get <tool>/<topic>` to fetch the docs
3. Use the fetched docs as context to write accurate, up-to-date code
4. Docs are cached locally for 24h — pass --no-cache to force refresh
```

---

## Publishing to npm

### 1. Test locally first

```bash
npm link           # installs aicli globally from local source
aicli help
aicli search kafka
aicli get kafka/producer
```

### 2. Publish

```bash
npm login          # authenticate with your npm account
npm publish --access public
```

After publish:

```bash
npm install -g @diepdao/aicli
aicli help
```

### 3. CI with GitHub Actions

```yaml
# .github/workflows/publish.yml
name: Publish to npm

on:
  push:
    tags: ['v*']

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          registry-url: 'https://registry.npmjs.org'
      - run: npm ci
      - run: npm test
      - run: npm publish --access public
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

Tag a release to trigger it:

```bash
git tag v1.0.0 && git push --tags
```

---

## Extending the Registry

Adding a new tool is a one-line registry edit plus an optional custom fetcher if the source isn't plain HTML:

```json
"elasticsearch": {
  "search-api": "https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html",
  "index-api":  "https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html"
}
```

For tools whose docs live on GitHub (READMEs, wikis), the `github.js` fetcher uses the raw API:

```js
// src/fetcher/github.js
export async function fetchGithubDocs(owner, repo, path = 'README.md') {
  const url = `https://raw.githubusercontent.com/${owner}/${repo}/HEAD/${path}`;
  return fetchDocs(url);
}
```

---

## Comparison: `aicli` vs `@aisuite/chub`

| Feature | `@aisuite/chub` | `@diepdao/aicli` |
|---|---|---|
| Focus | OpenAI, commercial AI APIs | Open-source infra (Kafka, Redis, ClickHouse…) |
| Language filter | `--lang py\|js` | `--lang js\|py\|java\|go` |
| Cache | None mentioned | Local 24h TTL cache |
| SKILL.md | Supported | Supported |
| Registry | Curated AI APIs | Extensible JSON registry |
| Auth required | No | No |

Both tools follow the same core idea: **pull docs at runtime, not from training weights**.

---

## What's Next

- Add more tools to the registry: PostgreSQL, MongoDB, Elasticsearch, gRPC
- Support versioned docs (`aicli get kafka/producer@2.x`)
- Add a `--json` output flag for programmatic consumption
- MCP (Model Context Protocol) server mode — expose `aicli` as an MCP tool so Claude Desktop can call it directly
- Community-contributed registry entries via pull requests
