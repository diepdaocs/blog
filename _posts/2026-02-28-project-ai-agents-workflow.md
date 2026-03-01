---
layout: single
title: "Project: AI & Agents Workflow — Text-to-SQL, Text-to-Dashboard"
date: 2026-02-28 10:05:00 +0800
permalink: /projects/ai-agents-workflow/
categories:
  - ai
  - projects
tags:
  - llm
  - generative-ai
  - a2a-protocol
  - text-to-sql
  - agents
  - natural-language
---

An AI agents system that lets traders create and modify dashboards using natural language — powered by Text-to-SQL and Text-to-Dashboard agents communicating via the A2A protocol.

The vision: a trader types "show me PnL by desk for the last week" into a chat window, and a dashboard materializes. They say "break it down by currency pair," and the dashboard updates. No tickets, no waiting for developers.

---

## Overview

This project builds a multi-agent system where specialized AI agents collaborate to transform natural language into working trading dashboards. It demonstrates:

1. **Text2SQL Agent** — converts natural language to SQL queries against a ClickHouse trading database
2. **Text2Dashboard Agent** — takes query results and generates dashboard configurations
3. **A2A Protocol** — agent-to-agent communication for orchestrating the workflow
4. **Chat Interface** — conversational UI for traders to iteratively refine dashboards

---

## Architecture

<img src="/assets/images/arch-ai-agents.svg" alt="AI Agents Workflow Architecture" style="width:100%;max-width:820px;margin:1rem auto;display:block;border-radius:8px;">

### Agent Roles

**Orchestrator Agent**
- Receives natural language input from the chat interface
- Determines which agents to invoke and in what order
- Manages conversation context and multi-turn refinement
- Routes A2A messages between agents

**Text2SQL Agent**
- Understands the ClickHouse schema (trades, risk metrics, positions)
- Converts natural language to valid SQL queries
- Validates queries for safety (no mutations, resource limits)
- Handles ambiguity by asking clarifying questions

**Text2Dashboard Agent**
- Takes SQL query results and generates dashboard configurations
- Supports chart types: line, bar, heatmap, table, time-series
- Adapts layout to data shape (single metric vs. multi-dimensional)
- Generates responsive dashboard JSON consumed by the React renderer

**Schema Agent**
- Provides schema context to other agents
- Maps business terms ("PnL," "desk," "portfolio") to table columns
- Maintains a glossary of trading terminology

---

## A2A Protocol

The Agent-to-Agent (A2A) protocol defines how agents communicate:

```json
{
  "from": "orchestrator",
  "to": "text2sql",
  "type": "request",
  "payload": {
    "intent": "query",
    "natural_language": "Show me PnL by desk for last week",
    "context": {
      "user_role": "fx_trader",
      "desk": "fx_spot",
      "previous_queries": []
    }
  }
}
```

Key features:
- **Typed messages** — request, response, clarification, error
- **Context propagation** — conversation history travels with each message
- **Agent discovery** — agents register capabilities, orchestrator routes accordingly
- **Fallback chains** — if one agent can't handle a request, it's routed to the next

---

## Chat Interface

The chat window is embedded in the trading dashboard, providing a conversational experience:

**Example conversation:**

> **Trader:** Show me today's PnL for the FX desk
>
> **Agent:** Here's the FX desk PnL for today. Total: +$1.2M. Top contributors: EUR/USD (+$450K), GBP/USD (+$280K).
>
> *[Dashboard appears with bar chart of PnL by currency pair]*
>
> **Trader:** Break it down by trader
>
> **Agent:** Updated — showing PnL by trader within the FX desk.
>
> *[Dashboard updates to show grouped bar chart: traders × currency pairs]*
>
> **Trader:** Add a time-series of cumulative PnL for the top 3 pairs
>
> **Agent:** Added a time-series panel below the bar chart.

The chat maintains context across turns, so traders can iteratively refine their dashboards without starting over.

---

## Per-Desk Customization

Different trading desks have different vocabulary, metrics, and dashboard preferences:

| Desk | Key Metrics | Default Views |
|------|-------------|---------------|
| **FX Spot** | PnL, position, spread | Currency pair heatmap, PnL waterfall |
| **Rates** | DV01, duration, yield | Tenor ladder, yield curve, PnL attribution |
| **Options** | Greeks, vol surface | Greeks panel, vol smile, PnL decomposition |
| **Credit** | Spread, default prob | Credit spread curve, issuer exposure |

The agents are context-aware — when an FX trader says "show my exposure," the system knows to show currency pair positions, not bond durations.

---

## Technology Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| LLM | Claude / GPT-4 | Natural language understanding |
| Agent Framework | Python, custom | Lightweight A2A orchestration |
| Backend | FastAPI | Async API endpoints |
| Database | ClickHouse | Fast analytical queries on trade data |
| Dashboard | React | Dynamic chart rendering |
| Communication | WebSocket | Real-time chat and dashboard updates |

---

## What You'll Learn

This project demonstrates:
- How to build a multi-agent system with clear agent responsibilities
- The A2A protocol for agent-to-agent communication
- Text-to-SQL techniques for financial databases
- Natural language interfaces for non-technical users
- Iterative dashboard creation through conversational AI

---

## Repository

The full source code is available on GitHub: [diepdaocs/agentic-risk-dashboard](https://github.com/diepdaocs/agentic-risk-dashboard)
