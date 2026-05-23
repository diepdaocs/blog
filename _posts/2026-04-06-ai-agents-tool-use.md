---
layout: single
title: "AI Agents in Production: Planning, Tool Use, and Safety Boundaries"
date: 2026-04-06 10:00:00 +0800
categories:
  - ai
tags:
  - ai-agents
  - tool-use
  - planning
  - safety
---

This is Post 5 in the [AI Series](/ai/2026/02/27/welcome-to-ai.html). The [previous post](/ai/2026/04/05/llm-systems-and-rag.html) covered LLM system design and RAG.

## What Makes an Agent Different

A chatbot answers once. An agent loops:
- plans,
- chooses tools,
- executes,
- checks results,
- retries or escalates.

## Production Agent Architecture

- **Planner**: decomposes goals into steps.
- **Executor**: calls APIs/tools.
- **Memory**: persists relevant state.
- **Evaluator**: checks correctness and policy compliance.

## Safety Boundaries

Essential controls:
1. Least-privilege credentials
2. Action confirmation for irreversible operations
3. Sandboxed tool execution
4. Immutable audit logs
5. Policy-based deny lists

## References

- ReAct prompting paper: https://arxiv.org/abs/2210.03629
- Toolformer paper: https://arxiv.org/abs/2302.04761
- Anthropic agentic patterns (engineering notes): https://www.anthropic.com/engineering

## Best Books

- Ronald T. Kneusel, *Practical Deep Learning* (deployment mindset).
- Martin Kleppmann, *Designing Data-Intensive Applications* (systems thinking).
- Chip Huyen, *AI Engineering*.
