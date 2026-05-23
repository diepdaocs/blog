---
layout: single
title: "MLOps and Evaluation: From Notebook Models to Reliable Production"
date: 2026-04-04 10:00:00 +0800
categories:
  - ai
tags:
  - mlops
  - evaluation
  - monitoring
  - deployment
---

This is Post 3 in the [AI Series]({{ site.baseurl }}/ai/2026/02/27/welcome-to-ai.html). The [previous post]({{ site.baseurl }}/ai/2026/02/27/learning-ml-andrew-ng.html) covered learning foundations.

Shipping ML is primarily an operations problem. Most failures are not model architecture failures; they are data quality, evaluation leakage, and runtime reliability failures.

## 1) The Production Lifecycle

1. Data contracts + ownership
2. Feature pipelines with reproducibility
3. Training with lineage and experiment tracking
4. Offline evaluation (incl. subgroup metrics)
5. Safe rollout (shadow/canary)
6. Monitoring + drift detection + retraining policy

## 2) Evaluation Beyond Accuracy

Use metrics aligned to business and risk:
- Precision/recall/F1 for imbalance.
- Calibration (Brier/expected calibration error).
- Ranking metrics when ordering matters.
- Latency, p95/p99, and cost-per-inference.
- KPI uplift and downstream operational impact.

## 3) Drift and Silent Failure

Models degrade when:
- feature distribution shifts,
- label definition changes,
- user behavior evolves,
- upstream data contracts break.

Treat monitoring as first-class product engineering, not a dashboard afterthought.

## 4) Rollout Safety Patterns

- Shadow mode before user impact.
- Canary with auto-rollback thresholds.
- Versioned features + model registry.
- Human-in-the-loop for high-stakes decisions.

## References

- Google, *Rules of ML*: https://developers.google.com/machine-learning/guides/rules-of-ml
- Sculley et al., *Hidden Technical Debt in ML Systems*: https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- Evidently docs: https://docs.evidentlyai.com/
- MLflow docs: https://mlflow.org/docs/latest/index.html

## Best Books

- Chip Huyen, *Designing Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.

Next: [LLM Systems and RAG: Building Useful AI Beyond Prompt Demos]({{ site.baseurl }}/ai/2026/04/05/llm-systems-and-rag.html).
