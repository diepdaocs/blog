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

This is Post 3 in the [Blockchain Series]({{ site.baseurl }}/blockchain/2026/02/27/welcome-to-blockchain.html). The [previous post]({{ site.baseurl }}/blockchain/2026/04/01/smart-contracts-and-evm.html) covered smart contracts and the EVM.

DeFi protocols are financial systems made of code, incentives, and adversarial game theory. Good protocol design is not just "can it run", but "can it survive volatility, manipulation, and user panic".

## 1) AMMs and Price Formation

Constant-product AMMs use:

`x * y = k`

A swap changes reserves and implied price. Large trades relative to pool depth create slippage. LPs earn fees but carry impermanent loss risk.

Design implications:
- More liquidity lowers slippage.
- Fee tiers affect route choice and LP behavior.
- Oracle-dependent protocols should account for AMM price manipulation windows.

## 2) Lending: Collateral, Liquidations, Solvency

Lending protocols typically require over-collateralization.

Key controls:
- **LTV** (loan-to-value),
- **Liquidation threshold**,
- **Close factor**,
- **Liquidation bonus**,
- **Oracle staleness / heartbeat checks**.

Risk engine quality determines whether the system degrades gracefully or collapses during market stress.

## 3) Oracle Risk Is Protocol Risk

If your protocol reads manipulated or stale prices, all other safeguards are weakened.

Mitigations:
1. Decentralized oracle networks.
2. TWAP or medianization strategies.
3. Circuit breakers when deviation exceeds threshold.
4. Multi-source fallback logic.

## 4) Governance and Upgrade Risk

Even perfect contract logic can be compromised by governance capture.

Best practices:
- Timelocks on privileged actions.
- Multi-sig and role separation.
- Parameter bounds at contract level.
- Transparent on-chain governance logs.

## 5) Incident Response and Monitoring

Production DeFi needs:
- real-time health factor and liquidation dashboards,
- anomaly detection for oracle and liquidity shocks,
- runbooks for pause/degrade/recover,
- postmortem culture and parameter hardening.

## References

- Uniswap v2 whitepaper: https://uniswap.org/whitepaper.pdf
- Aave docs: https://docs.aave.com/
- Chainlink docs: https://docs.chain.link/
- Gauntlet research (risk frameworks): https://www.gauntlet.xyz/resources

## Best Books

- Campbell R. Harvey, Ashwin Ramachandran, Joey Santoro, *DeFi and the Future of Finance*.
- Andreas M. Antonopoulos, *Mastering Bitcoin*.
- Chris Burniske & Jack Tatar, *Cryptoassets*.

Next: [Blockchain Scalability: Layer 2 Rollups, Data Availability, and Trade-offs]({{ site.baseurl }}/blockchain/2026/04/03/blockchain-scalability-and-rollups.html).
