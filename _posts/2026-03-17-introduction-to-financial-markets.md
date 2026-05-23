---
layout: single
title: "Introduction to Financial Markets: A Software Engineer’s Map"
date: 2026-03-17 09:00:00 +0800
permalink: /finance/2026/03/17/introduction-to-financial-markets/
categories:
  - finance
tags:
  - financial-markets
  - risk-management
  - trading
  - corporate-banking
  - financial-engineering
---

If computer science gives you the language of systems, finance gives you the language of money, risk, and incentives. As a software engineer working across corporate banking, trading, portfolios, and risk dashboards, I found that understanding the domain changes how you design software.

This post is a practical map of the core concepts every engineer in a bank should know.

---

## 1. Financial Markets in One View

At a high level, financial markets connect three groups:

- **Capital providers** (investors, funds, banks)
- **Capital users** (companies, governments, institutions)
- **Intermediaries** (exchanges, brokers, clearing houses, banks)

The main market segments:

- **Money markets** (short-term funding)
- **Capital markets** (equity and debt for longer-term funding)
- **FX markets** (currencies)
- **Rates markets** (government bonds, swaps)
- **Credit markets** (corporate bonds, CDS)
- **Derivatives markets** (futures, options, structured products)

As engineers, this structure matters because every subsystem we build (trade capture, risk, limits, settlement, reporting) maps to one or more market segments.

---

## 2. Financial Engineering: Pricing + Models + Data

Financial engineering is where mathematics, statistics, and software meet.

Core building blocks:

- **Pricing models**: present value, discounting, yield curves, option pricing
- **Market data models**: curves, surfaces, historical time series, volatility snapshots
- **Risk models**: sensitivities (Greeks, DV01), stress scenarios, VaR

In production systems, the challenge is not just model correctness. It is also:

- deterministic reproducibility
- latency budgets
- explainability of risk numbers
- traceability from market data snapshot to final report

See the implementation blueprint in this project: **[Project: Financial Engineering & Risk Management System](/projects/financial-engineering/)**.

---

## 3. Banking & Institutions: Who Does What

In most global banks, the institutional setup looks like this:

- **Front Office**: sales + traders, revenue generation, pricing and execution
- **Middle Office**: risk control, PnL explain, limit monitoring
- **Back Office**: confirmations, settlement, reconciliation
- **Treasury**: liquidity and funding
- **Finance/Regulatory**: accounting and regulatory reports

Different teams care about the same trade in different ways:

- Trader: fill quality, market impact, position
- Risk manager: exposure, concentration, stress loss
- Operations: booking correctness and settlement status
- Finance: valuation and ledger alignment

Good internal platforms unify these views without duplicating logic.

---

## 4. Corporate Banking: Loans, Facilities, and Client Risk

Corporate banking systems usually center around:

- **Client onboarding** (KYC, legal entities, hierarchies)
- **Credit facilities** (limits, drawdowns, utilization)
- **Loan lifecycle** (origination → disbursement → repayment)
- **Covenants and monitoring**
- **Collateral and guarantees**

From an engineering perspective, corporate banking is workflow-heavy and audit-heavy. Two design principles matter:

1. **Event history is a first-class dataset** (who changed what, when, and why)
2. **Reference data consistency** across loans, clients, facilities, and exposures

When these are weak, downstream risk and finance numbers drift.

---

## 5. Risk Management: What Risk Numbers Actually Mean

The most common risk numbers you will see on trading and portfolio dashboards:

- **PnL**: realized and unrealized profit/loss
- **DV01/PV01**: sensitivity to 1bp rate moves
- **Delta/Gamma/Vega/Theta/Rho**: option sensitivities
- **VaR**: distribution-based portfolio loss estimate
- **Stress loss**: scenario-based losses under extreme moves

For engineers, the key is lineage:

`Trade + Market Data + Model Version + Netting Rules + Aggregation Hierarchy → Risk Number`

If any component is ambiguous, trust in the number collapses.

---

## 6. Traders and the Risk Dashboard Contract

A trader-facing risk dashboard is not just visualization. It is an operational contract:

- **Timeliness**: updates must arrive within desk-specific SLAs
- **Consistency**: totals must reconcile across drill-down levels
- **Context**: each metric should be explainable and attributable
- **Actionability**: users can identify the trades/drivers behind moves

Typical views that matter most on desks:

- PnL by book / trader / strategy
- Greeks by maturity bucket
- VaR and stress compared to limits
- Top risk contributors and concentration hotspots

---

## 7. Practical Engineering Patterns for Bank Systems

Patterns that repeatedly work well:

- **Event-driven pipelines** for trade lifecycle and risk recalculation
- **Idempotent consumers** for replay safety
- **Immutable market-data snapshots** for reproducibility
- **Explicit versioning** of models and valuation parameters
- **As-of-time queries** for audit and investigations

Patterns that usually create pain:

- hidden in-place mutations of trade state
- risk calculators tightly coupled to UI-specific formatting
- ad-hoc joins across ungoverned reference data

---

## What’s Next in the Finance Series

Start here:

- **[Welcome to the Finance Series](/finance/2026/02/27/welcome-to-finance/)**
- **[Project: Financial Engineering & Risk Management System](/projects/financial-engineering/)**

Next deep dives will cover market microstructure, valuation pipelines, and production risk controls in more detail.
