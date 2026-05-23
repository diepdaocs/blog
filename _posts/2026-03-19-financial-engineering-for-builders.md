---
layout: single
title: "Financial Engineering for Builders: Pricing, Curves, and Risk"
date: 2026-03-19 09:00:00 +0800
permalink: /finance/2026/03/19/financial-engineering-for-builders/
categories:
  - finance
tags:
  - financial-engineering
  - pricing
  - quantitative-finance
  - risk
---

Financial engineering in production is the discipline of turning models into reliable, explainable, and testable systems.

## Core Building Blocks

- **Discounting** and present value
- **Curves** (OIS, LIBOR fallback/term benchmarks, credit curves)
- **Volatility surfaces** for options
- **Sensitivities** (DV01, delta, gamma, vega)
- **Scenario and stress engines**

## Engineering Priorities

- Deterministic valuation runs for reproducibility.
- Version everything: models, market data, conventions.
- Explainability: contribution analysis by trade and factor.
- Fast incremental recalculation after trade events.

## Common Failure Modes

- Hidden convention mismatches (day count, calendars).
- Mixing stale and live market snapshots.
- Non-idempotent risk aggregation jobs.

## References

- [ISDA: Risk and Initial Margin](https://www.isda.org/category/risk/)
- [Bank of England: Yield Curves and Discounting](https://www.bankofengland.co.uk/)
- [CME Education: Options Greeks](https://www.cmegroup.com/education.html)

## Best Books to Read

- *Options, Futures, and Other Derivatives* — John C. Hull
- *Paul Wilmott Introduces Quantitative Finance* — Paul Wilmott
- *Interest Rate Markets* — Siddhartha Jha
