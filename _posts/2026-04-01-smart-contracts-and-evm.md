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

This is Post 2 in the [Blockchain Series]({{ site.baseurl }}/blockchain/2026/02/27/welcome-to-blockchain.html). The [previous post]({{ site.baseurl }}/blockchain/2026/02/27/blockchain-introduction.html) covered cryptography, consensus, and the trustless ledger.

Smart contracts are not "magic legal contracts". They are deterministic programs executed by a global, adversarially replicated computer. If your logic is wrong, the network will execute the wrong logic *perfectly*.

---

## 1) The Contract Mental Model: A Persistent State Machine

At core, a smart contract is:

`new_state = f(old_state, input)`

Where:
- `old_state` is on-chain storage,
- `input` is calldata from a transaction,
- `f` is EVM bytecode,
- `new_state` must be reproducible by every validator.

This is why determinism is non-negotiable: contracts cannot read your local clock, fetch random web APIs, or depend on host machine behavior.

## 2) How a Transaction Becomes State

```text
User signs tx
→ tx enters mempool
→ proposer/validator includes tx in block
→ all full nodes execute same bytecode
→ if valid, global state root changes
```

If one node computes a different result, that node is wrong and falls out of consensus.

## 3) EVM Internals That Matter in Real Design

- **Stack**: 256-bit word stack machine (opcode-level execution).
- **Memory**: transient per-call workspace (cheap, cleared after call).
- **Storage**: persistent key-value store (expensive and state-rent sensitive).
- **Calldata**: immutable input payload from caller (cheap to read).
- **Logs/Events**: indexable outputs for off-chain consumers.

Most gas optimization comes down to reducing expensive storage writes and unnecessary external calls.

## 4) Gas, Fees, and Failure Modes

Gas is Ethereum's anti-abuse metering system.

- Every opcode has a gas cost.
- Sender sets gas limit and fee parameters.
- Out-of-gas reverts state changes in the call frame.
- Gas spent is still paid, even on revert.

Common production failures:
1. Underestimating gas in loops over unbounded arrays.
2. Writing storage repeatedly instead of caching in memory.
3. Designing admin or payout flows that become too expensive under high state growth.

## 5) Security Patterns You Should Treat as Defaults

- **Checks → Effects → Interactions** ordering.
- **Pull payment** over push payment.
- **Reentrancy guard** on sensitive paths.
- **Access control** with explicit roles.
- **Pause/circuit breaker** for emergency response.
- **Invariant-focused tests** (not just happy path unit tests).

```solidity
contract Vault {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient");
        balances[msg.sender] -= amount; // Effects first
        (bool ok, ) = msg.sender.call{value: amount}(""); // Interaction after
        require(ok, "transfer failed");
    }
}
```

## 6) Build Workflow for Serious Teams

1. Model protocol invariants before coding.
2. Implement minimal surface area contracts.
3. Add fuzzing + property tests.
4. Run static analyzers and symbolic checks.
5. Audit before mainnet deployment.
6. Ship with monitoring + incident runbooks.

## References

- Ethereum docs (EVM, execution, gas): https://ethereum.org/en/developers/docs/
- Solidity docs: https://docs.soliditylang.org/
- Gavin Wood, *Ethereum Yellow Paper*: https://ethereum.github.io/yellowpaper/paper.pdf
- ConsenSys Smart Contract Best Practices: https://consensysdiligence.github.io/smart-contract-best-practices/

## Best Books

- Andreas M. Antonopoulos & Gavin Wood, *Mastering Ethereum*.
- Chris Dannen, *Introducing Ethereum and Solidity*.
- Narayanan et al., *Bitcoin and Cryptocurrency Technologies* (foundations).

Next: [DeFi Protocol Design: AMMs, Lending, and On-Chain Risk]({{ site.baseurl }}/blockchain/2026/04/02/defi-protocol-design.html).
