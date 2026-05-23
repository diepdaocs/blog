---
layout: single
title: "Market Microstructure: How Trades Actually Happen"
date: 2026-03-18 09:00:00 +0800
permalink: /finance/2026/03/18/market-microstructure/
categories:
  - finance
tags:
  - market-microstructure
  - trading
  - order-book
  - execution
---

Market microstructure is the study of how buyers and sellers interact, how prices form, and how orders become trades. For engineers, this is where system behavior directly changes financial outcomes.

## Core Concepts

- **Order types**: market, limit, stop, iceberg.
- **Order book**: bid/ask levels with price-time priority.
- **Spread**: ask minus bid; a key transaction cost.
- **Liquidity**: how much can be traded without moving price.
- **Slippage**: difference between expected and executed price.

## Why Engineers Should Care

- Matching-engine latency changes fill quality.
- Queue position affects execution probability.
- Throttling and retries can create accidental duplicate orders.
- Timestamp precision is critical for post-trade analysis.

## Practical System Design Notes

- Use immutable execution events.
- Keep clock synchronization explicit (NTP/PTP strategy).
- Separate market-data ingestion from order-routing paths.
- Build replay tooling for execution incident investigation.

## References

- [BIS: Market Microstructure](https://www.bis.org/publ/work331.htm)
- [SEC: Market Structure Overview](https://www.sec.gov/marketstructure)
- [CFA Institute: Market Microstructure Basics](https://www.cfainstitute.org/insights)

## Best Books to Read

- *Trading and Exchanges* — Larry Harris
- *Algorithmic Trading and DMA* — Barry Johnson
- *Market Microstructure Theory* — Maureen O'Hara
