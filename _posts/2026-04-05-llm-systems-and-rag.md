---
layout: single
title: "LLM Systems and RAG: Building Useful AI Beyond Prompt Demos"
date: 2026-04-05 10:00:00 +0800
categories:
  - ai
tags:
  - llm
  - rag
  - embeddings
  - vector-database
  - agents
---

This is Post 4 in the [AI Series]({{ site.baseurl }}/ai/2026/02/27/welcome-to-ai.html). The [previous post]({{ site.baseurl }}/ai/2026/04/04/mlops-and-evaluation.html) covered MLOps and evaluation.

RAG became the default architecture because base models are general but not naturally grounded in proprietary or rapidly changing knowledge.

## 1) Canonical RAG Pipeline

1. Ingest and normalize documents.
2. Chunk with overlap tuned to use case.
3. Generate embeddings.
4. Index in vector DB with metadata.
5. Retrieve + rerank.
6. Compose grounded prompt and generate.
7. Enforce citation/attribution in output.

## 2) Design Decisions That Actually Move Quality

- Chunk strategy (semantic vs fixed length).
- Metadata design (time, source, permission scope).
- Hybrid retrieval (sparse + dense).
- Reranking quality vs latency budget.
- Prompt template with explicit abstention behavior.

## 3) Evaluation Framework

Evaluate with task-specific sets:
- Retrieval hit rate / nDCG.
- Faithfulness and groundedness.
- Hallucination rate.
- Citation correctness.
- End-to-end latency and cost.

No eval set means no engineering signal.

## 4) Guardrails for Real Deployments

- Structured outputs (JSON schema).
- Tool permissions and sandboxed actions.
- PII and compliance filters.
- Fallback behavior when confidence is low.

## References

- Lewis et al., RAG paper: https://arxiv.org/abs/2005.11401
- OpenAI Cookbook: https://cookbook.openai.com/
- LangChain RAG concepts: https://python.langchain.com/docs/concepts/rag/
- LlamaIndex docs: https://docs.llamaindex.ai/

## Best Books

- Jurafsky & Martin, *Speech and Language Processing*.
- Chip Huyen, *AI Engineering*.
- O'Reilly, *Designing Large Language Model Applications*.

Next: [AI Agents in Production: Planning, Tool Use, and Safety Boundaries]({{ site.baseurl }}/ai/2026/04/06/ai-agents-tool-use.html).
