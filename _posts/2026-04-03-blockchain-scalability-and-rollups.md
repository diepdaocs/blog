---
layout: single
title: "Blockchain Scalability: Layer 2 Rollups, Data Availability, and Trade-offs"
date: 2026-04-03 10:00:00 +0800
categories:
  - blockchain
tags:
  - layer2
  - rollups
  - scalability
  - data-availability
---

This is Post 4 in the [Blockchain Series](/blockchain/2026/02/27/welcome-to-blockchain/). The [previous post](/blockchain/2026/04/02/defi-protocol-design/) covered DeFi protocol design.

## Why Layer 2 Exists

Base layers optimize decentralization and security, but throughput is limited. Layer 2 systems move execution off-chain while inheriting L1 settlement.

## Rollup Types

- **Optimistic rollups**: assume valid by default; fraud proofs during challenge windows.
- **ZK rollups**: validity proofs (SNARK/STARK) submitted to L1.

## Data Availability (DA)

State validity is not enough; users need transaction data to reconstruct state.

DA approaches:
- Post calldata/data blobs on Ethereum.
- Validium/volition (trade-offs in DA trust).
- Modular DA layers for high throughput.

## Choosing the Right Architecture

- Need fastest finality and high security assumptions? → ZK rollup.
- Need EVM compatibility with mature tooling? → Often optimistic first.
- Need lowest costs for consumer apps? → Hybrid with strong DA guarantees.

## References

- Ethereum rollup-centric roadmap notes: https://ethereum-magicians.org/
- OP Stack docs: https://docs.optimism.io/
- zkSync docs: https://docs.zksync.io/
- Arbitrum docs: https://docs.arbitrum.io/

## Best Books

- Alex Xu, *System Design Interview* (scalability mindset, complementary).
- Narayanan et al., *Bitcoin and Cryptocurrency Technologies*.
- Andreas M. Antonopoulos & Gavin Wood, *Mastering Ethereum*.
