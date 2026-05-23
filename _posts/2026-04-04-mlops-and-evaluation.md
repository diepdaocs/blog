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

This is Post 2 in the [AI Series](/ai/2026/02/27/welcome-to-ai/). The [previous post](/ai/2026/02/27/learning-ml-andrew-ng/) covered the learning journey and foundations.

## The Real Problem: Reliability, Not Demos

A model that looks great in a notebook often fails in production because:
- data distribution shifts,
- labels arrive late,
- business constraints are ignored.

## Production ML Lifecycle

1. Data contracts and feature definitions
2. Reproducible training pipeline
3. Offline evaluation with leakage checks
4. Online rollout with guardrails (canary, shadow)
5. Monitoring and retraining triggers

## Metrics That Matter

Beyond accuracy:
- Precision/recall/F1 (imbalance)
- Calibration (probability quality)
- Latency and throughput SLOs
- Drift metrics (feature + prediction drift)
- Business KPI lift

## References

- Google, *Rules of Machine Learning*: https://developers.google.com/machine-learning/guides/rules-of-ml
- Google, *Hidden Technical Debt in ML Systems*: https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- Evidently AI docs (monitoring): https://docs.evidentlyai.com/

## Best Books

- Chip Huyen, *Designing Machine Learning Systems*.
- Mark Treveil & Alok Shukla et al., *Introducing MLOps*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
