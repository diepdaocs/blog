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

This is Post 3 in the [AI Series](/ai/2026/02/27/welcome-to-ai/). The [previous post](/ai/2026/04/04/mlops-and-evaluation/) covered MLOps and evaluation.

## Why RAG Became Default

LLMs are strong general reasoners but weak on private, current, or domain-specific facts. Retrieval-Augmented Generation (RAG) solves this by injecting grounded context at inference time.

## RAG Pipeline

1. Chunk and clean source documents
2. Create embeddings
3. Index in vector database
4. Retrieve top-k relevant chunks
5. Re-rank / filter
6. Generate answer with citations

## Design Pitfalls

- Overly large chunks reduce precision.
- Missing metadata hurts filtering.
- No eval set means no measurable quality.
- Ignoring latency budgets kills UX.

## Practical Guardrails

- Structured output schemas
- Tool calling with explicit permissions
- Citation enforcement
- Human escalation for high-stakes tasks

## References

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*: https://arxiv.org/abs/2005.11401
- OpenAI cookbook (RAG patterns): https://cookbook.openai.com/
- LangChain docs (retrieval architecture): https://python.langchain.com/docs/concepts/rag/

## Best Books

- Jurafsky & Martin, *Speech and Language Processing* (latest draft).
- Chip Huyen, *AI Engineering*.
- Building LLM apps community playbooks by O'Reilly (practitioner references).
