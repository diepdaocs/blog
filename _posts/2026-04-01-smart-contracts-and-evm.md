---
layout: single
title: "Smart Contracts and the EVM: How Ethereum Actually Executes Code"
date: 2026-04-01 10:00:00 +0800
categories:
  - blockchain
tags:
  - smart-contracts
  - ethereum
  - evm
  - solidity
  - gas
---

This is Post 2 in the [Blockchain Series](/blockchain/2026/02/27/welcome-to-blockchain.html). The [previous post](/blockchain/2026/02/27/blockchain-introduction.html) covered blockchain fundamentals.

## Why Smart Contracts Matter

A smart contract is code stored on-chain that executes deterministically on every validating node. The same input must always produce the same state transition.

Core ideas:
- **State machine**: contracts map old state + transaction input → new state.
- **Determinism**: no hidden randomness, no local file/network access.
- **Economic metering**: computation costs gas.

## EVM Execution Model

Ethereum transactions either transfer ETH or call contract bytecode.

```
User signs transaction
  → node gossips transaction to mempool
  → validator includes it in a block
  → each node runs EVM bytecode
  → state root updates if execution succeeds
```

Important mechanics:
- **Stack machine** (256-bit words).
- **Storage** persists across transactions (expensive).
- **Memory** is transient per call (cheaper).
- **Calldata** is read-only function input.

## Gas, Fees, and Safety

Gas prevents denial-of-service. Every opcode has cost. If gas runs out, state changes revert (except gas spent).

Practical design rules:
1. Minimize storage writes.
2. Prefer pull-over-push payment patterns.
3. Validate inputs early and fail fast.
4. Use reentrancy guards on external calls.

## Minimal Secure Contract Pattern

```solidity
contract Vault {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient");
        balances[msg.sender] -= amount;
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "transfer failed");
    }
}
```

This follows checks-effects-interactions ordering.

## References

- Gavin Wood, *Ethereum: A Secure Decentralised Generalised Transaction Ledger (Yellow Paper)*: https://ethereum.github.io/yellowpaper/paper.pdf
- Ethereum docs (EVM, gas, execution): https://ethereum.org/en/developers/docs/
- Solidity docs: https://docs.soliditylang.org/

## Best Books

- Andreas M. Antonopoulos & Gavin Wood, *Mastering Ethereum*.
- Chris Dannen, *Introducing Ethereum and Solidity*.
- Camila Russo, *The Infinite Machine* (history/context).
