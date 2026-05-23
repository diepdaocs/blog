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

This is Post 5 in the [AI Series]({{ site.baseurl }}/ai/2026/02/27/welcome-to-ai.html). The [previous post]({{ site.baseurl }}/ai/2026/04/05/llm-systems-and-rag.html) covered LLM systems and RAG.

Agent systems are not just bigger prompts; they are control systems with feedback loops, external actions, and safety boundaries.

## 1) Agent Loop: Plan → Act → Observe → Adapt

A production agent typically:
1. decomposes a goal,
2. selects tools,
3. executes actions,
4. evaluates results,
5. retries, reroutes, or escalates.

This loop is where value appears—and where risk appears.

## 2) Core Architecture Blocks

- **Planner**: task decomposition and prioritization.
- **Executor**: function/tool invocation.
- **Memory**: short-term context + durable task state.
- **Evaluator/Critic**: correctness and policy checks.
- **Policy Engine**: permission and compliance decisions.

## 3) Failure Modes in the Wild

- Tool misuse from weak schema contracts.
- Infinite loops from weak termination conditions.
- Hallucinated tool outputs accepted as truth.
- Privilege escalation via prompt injection.

## 4) Non-Negotiable Safety Controls

- Least-privilege credentials per tool.
- Confirmation gates for irreversible actions.
- Sandboxed execution environments.
- Immutable audit logs and replayability.
- Output validation against typed schemas.
- Human handoff for high-impact decisions.

## 5) Evaluation for Agentic Systems

Measure:
- task completion rate,
- step efficiency,
- tool-call accuracy,
- policy violation rate,
- time-to-recovery after failure.

Agent quality is behavioral reliability over many trajectories, not one benchmark score.

## References

- ReAct paper: https://arxiv.org/abs/2210.03629
- Toolformer paper: https://arxiv.org/abs/2302.04761
- Anthropic engineering posts: https://www.anthropic.com/engineering
- OpenAI Agents guide: https://platform.openai.com/docs/guides/agents

## Best Books

- Chip Huyen, *AI Engineering*.
- Martin Kleppmann, *Designing Data-Intensive Applications*.
- Ronald T. Kneusel, *Practical Deep Learning*.
