---
layout: single
title: "Project: Financial Engineering & Risk Management System"
date: 2026-02-28 10:00:00 +0800
permalink: /projects/financial-engineering/
categories:
  - finance
  - projects
tags:
  - trading
  - risk-management
  - clickhouse
  - kafka
  - java
  - order-book
  - real-time
---

Building a complete simulation trading and risk management system from scratch — the kind that powers real trading desks.

This project demonstrates the full lifecycle: from order entry and trade matching to real-time risk calculation and dashboard delivery. It's designed to mirror the systems I've worked on at Standard Chartered Bank, simplified for demonstration but architecturally faithful.

---

## Overview

The system has two main subsystems:

1. **Trading System** — an order book engine that accepts orders, matches trades, and stores executions in ClickHouse
2. **Risk System** — a real-time risk engine that computes PnL, Greeks, and other risk metrics, pushing updates to dashboards via an event queue

Both systems support multiple asset classes: FX, bonds, equities, options, and derivatives.

---

## Architecture

<img src="/assets/images/arch-finance.svg" alt="Trading & Risk Management System Architecture" style="width:100%;max-width:820px;margin:1rem auto;display:block;border-radius:8px;">

### Trading System

**Order Book Engine**
- Limit order book with price-time priority matching
- Supports market, limit, and stop orders
- Multi-asset: each instrument maintains its own order book

**Trade Matching**
- Continuous matching for equities and FX
- Auction matching for derivatives
- Partial fills and order amendments

**Trade Storage**
- ClickHouse as the columnar store for high-throughput trade ingestion
- Designed for time-series queries: trade history, blotter views, aggregation by desk/portfolio

### Risk System

**Risk Engine**
- Real-time computation triggered by trade events
- Calculates per-trade and per-portfolio risk metrics
- Supports different calculation profiles per trading desk

**Risk Metrics**
- **PnL** — Mark-to-market, realized vs unrealized
- **DV01** — Dollar value of a basis point (interest rate sensitivity)
- **Greeks** — Delta, gamma, theta, vega, rho for options
- **VaR** — Value at Risk for portfolio-level risk monitoring

**Limits Framework**
- Per-desk risk limits (e.g., max notional, max DV01)
- Per-portfolio limits
- Breach alerting and pre-trade limit checks

**Event Pipeline**
- Trade booked → event published to queue
- Risk engine consumes event, calculates risk
- Risk numbers stored in ClickHouse
- Dashboard receives notification to refresh

---

## Multi-Asset Coverage

| Asset Class | Instruments | Key Risk Metrics |
|-------------|-------------|-----------------|
| **FX** | Spot, forwards, swaps | PnL, delta, DV01 |
| **Bonds** | Government, corporate | PnL, DV01, duration, convexity |
| **Equities** | Stocks, ETFs | PnL, delta, beta |
| **Options** | Vanilla calls/puts | PnL, delta, gamma, theta, vega |
| **Derivatives** | Futures, swaps | PnL, DV01, Greeks |

Each trading desk sees only the risk metrics relevant to their book. An FX desk sees DV01 and spot delta. An options desk sees the full Greeks panel. The dashboard is configurable per desk.

---

## Technology Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| Core Engine | Java | Low-latency, strong concurrency |
| Message Queue | Kafka | High-throughput event streaming |
| Time-Series DB | ClickHouse | Columnar storage, fast aggregation |
| Caching | Hazelcast | In-memory grid for hot risk data |
| Dashboard | React | Real-time UI with WebSocket updates |

---

## Trading Desk Dashboards

Different desks have different views:

**FX Desk**
- Live FX rates and spot positions
- DV01 exposure by currency pair
- PnL by book, intraday and cumulative

**Rates Desk**
- Bond portfolio duration and convexity
- DV01 ladder by tenor bucket
- Yield curve shifts and PnL attribution

**Options Desk**
- Full Greeks dashboard: delta, gamma, theta, vega
- Volatility surface and skew
- PnL decomposition by Greek

---

## What You'll Learn

This project demonstrates:
- How order books work and how trades are matched
- Real-time risk calculation patterns used in investment banks
- ClickHouse schema design for financial time-series data
- Event-driven architecture for low-latency risk systems
- How trading desks consume risk data differently

---

## Repository

*Coming soon — the GitHub repository with full source code, setup instructions, and sample data.*
