---
layout: single
title: "DeFi Protocol Design: AMMs, Lending, and On-Chain Risk"
date: 2026-04-02 10:00:00 +0800
categories:
  - blockchain
tags:
  - defi
  - amm
  - lending
  - risk
  - tokenomics
---

This is Post 3 in the [Blockchain Series](/blockchain/2026/02/27/welcome-to-blockchain.html). The [previous post](/blockchain/2026/04/01/smart-contracts-and-evm.html) covered smart contracts and the EVM.

## AMMs: Market Making in Code

The canonical constant-product AMM uses:

`x * y = k`

Where `x` and `y` are token reserves. A swap changes reserves and implied price. Deeper liquidity means lower slippage.

## Lending Protocol Basics

Lending markets depend on over-collateralization:
- Supply collateral.
- Borrow below collateral factor.
- Liquidation triggers if health factor drops.

Critical parameters:
- Loan-to-value (LTV)
- Liquidation threshold
- Liquidation bonus
- Oracle heartbeat/staleness checks

## Risk Surfaces

Top failure modes in DeFi:
1. **Smart contract bugs**
2. **Oracle manipulation**
3. **Liquidity crunches**
4. **Governance capture**

Engineering mitigations:
- Timelocks + multi-sig for upgrades
- Circuit breakers / pause guardians
- Formal verification for core math
- Real-time risk monitoring dashboards

## References

- Uniswap v2 whitepaper: https://uniswap.org/whitepaper.pdf
- Aave docs: https://docs.aave.com/
- Chainlink docs (oracle architecture): https://docs.chain.link/

## Best Books

- Campbell R. Harvey, Ashwin Ramachandran, Joey Santoro, *DeFi and the Future of Finance*.
- Andreas M. Antonopoulos, *Mastering Bitcoin* (for transaction and security foundations).
- Linda Xie et al., *DeFi Developer Road Map* (community resource/book-length guide).
