---
layout: single
title: "Blockchain From First Principles: Cryptography, Consensus, and the Trustless Ledger"
date: 2026-02-27 10:00:00 +0800
categories:
  - blockchain
tags:
  - cryptography
  - hashing
  - merkle-tree
  - consensus
  - bitcoin
  - distributed-systems
---

Most introductions to blockchain start with Bitcoin or Ethereum and work backwards. This one goes the other direction — starting from the fundamental computer science concepts and building up to a full picture of how a trustless, immutable ledger emerges from them.

By the end of this post you'll understand not just *what* blockchain is, but *why* it works.

---

## 1. Cryptography — The Foundation of Trust

Blockchain doesn't introduce new cryptography. It assembles well-understood primitives into a system with remarkable properties.

The two most important primitives are:

### Public-Key Cryptography (Asymmetric Encryption)

Each participant in a blockchain network has a **key pair**:
- A **private key** — known only to the owner, never shared
- A **public key** — derived from the private key, shared freely

The relationship is asymmetric: you can derive the public key from the private key, but not the reverse. This asymmetry is the foundation of digital ownership.

**Digital signatures** use this pair to prove authenticity. When you sign a transaction with your private key, anyone can verify the signature using your public key — proving the transaction came from you, without ever learning your private key.

```
sign(transaction, private_key)   → signature
verify(transaction, signature, public_key) → true / false
```

This replaces the need for a trusted third party (like a bank) to vouch for identity. Cryptographic proof substitutes for institutional trust.

### Elliptic Curve Cryptography (ECC)

Bitcoin and Ethereum use **secp256k1**, a specific elliptic curve. ECC achieves the same security as RSA with much smaller key sizes — a 256-bit ECC key is roughly equivalent to a 3072-bit RSA key. This matters for a system where every node stores every transaction.

---

## 2. Hashing — Fingerprinting Data

A **cryptographic hash function** takes an input of any size and produces a fixed-size output (the hash or digest). The properties that matter for blockchain:

| Property | Meaning |
|---|---|
| **Deterministic** | Same input always produces the same hash |
| **Fixed size** | Any input → 256-bit output (for SHA-256) |
| **Avalanche effect** | Changing one bit in the input changes ~50% of the output |
| **Pre-image resistance** | Given a hash, you cannot recover the input |
| **Collision resistance** | It's computationally infeasible to find two inputs with the same hash |

```
SHA-256("Hello") = 185f8db32921bd46d35...
SHA-256("hello") = 2cf24dba5fb0a30e26e8...  ← completely different
```

Hashes serve as **tamper-evident fingerprints**. If anyone modifies a block's data, its hash changes entirely — and since each block references the previous block's hash, the change propagates forward, breaking the entire chain. More on this shortly.

Bitcoin uses **double SHA-256** (`SHA-256(SHA-256(data))`). Ethereum uses **Keccak-256**.

---

## 3. Merkle Trees — Efficient Transaction Verification

A block can contain thousands of transactions. How do you efficiently prove that a specific transaction is included in a block without downloading every transaction?

Enter the **Merkle tree**, invented by Ralph Merkle in 1979.

### How It's Built

1. Hash each transaction individually: `H(tx1)`, `H(tx2)`, `H(tx3)`, `H(tx4)`
2. Pair adjacent hashes and hash them together: `H(H(tx1) + H(tx2))`, `H(H(tx3) + H(tx4))`
3. Repeat until a single hash remains — the **Merkle root**

```
                  [Merkle Root]
                 /             \
          [H(tx1+tx2)]    [H(tx3+tx4)]
           /       \        /       \
        H(tx1)  H(tx2)  H(tx3)  H(tx4)
```

The Merkle root is stored in the block header. It's a single 32-byte fingerprint that represents *all* transactions in the block.

### Why It Matters

To prove that `tx3` is in a block, you only need to provide:
- `H(tx4)` (the sibling)
- `H(H(tx1) + H(tx2))` (the uncle)
- The Merkle root from the block header

That's a **Merkle proof** — logarithmic in size (`O(log n)`) rather than requiring all transactions. This enables **SPV (Simplified Payment Verification)**, allowing lightweight clients (like mobile wallets) to verify transactions without downloading the full blockchain.

---

## 4. Transactions — Expressing Intent

A transaction is a signed instruction to transfer value or execute logic.

In Bitcoin, a transaction contains:
- **Inputs** — references to unspent outputs (UTXOs) being consumed
- **Outputs** — new UTXOs being created (recipients and amounts)
- **Signatures** — proving the sender owns the inputs

```
Transaction {
  inputs: [{ prev_tx_hash, output_index, signature }],
  outputs: [{ recipient_public_key_hash, amount }],
  fee: inputs_total - outputs_total
}
```

Miners are incentivised to include transactions with higher fees. Unconfirmed transactions sit in the **mempool** (memory pool) waiting to be picked up.

In Ethereum, transactions also carry a `data` field — this is how smart contracts are invoked. A transaction can trigger arbitrary computation on the EVM (Ethereum Virtual Machine), not just value transfer.

---

## 5. Blocks — Packaging Transactions

A **block** is a container that groups transactions together and links to the previous block.

```
Block {
  header: {
    previous_block_hash,   ← links to parent block
    merkle_root,           ← fingerprint of all transactions
    timestamp,
    difficulty_target,
    nonce                  ← the number miners search for
  },
  transactions: [tx1, tx2, tx3, ...]
}
```

The critical field is `previous_block_hash`. Each block cryptographically commits to its parent, forming a **chain**. If you alter any transaction in block 500, the block's hash changes, which invalidates block 501's `previous_block_hash`, which invalidates block 502, and so on.

To tamper with history, you'd need to recompute every subsequent block — faster than the entire honest network is building new ones. This is computationally prohibitive, and exactly why the chain's length matters.

---

## 6. Consensus Protocols — Agreeing Without a Central Authority

This is where blockchain gets genuinely interesting. In a distributed network with no central server, how do thousands of nodes agree on which block comes next?

This is the **consensus problem**, and it's harder than it sounds. Nodes may be slow, offline, or malicious. The network must reach agreement despite all of this — what distributed systems researchers call the **Byzantine Generals Problem**.

### Proof of Work (PoW) — Bitcoin

Miners compete to find a `nonce` such that:

```
SHA-256(SHA-256(block_header + nonce)) < difficulty_target
```

There's no shortcut — you just try billions of nonces until one works. This is computationally expensive by design. The first miner to find a valid nonce broadcasts the block and claims the **block reward** (newly minted coins + transaction fees).

**Why this achieves consensus:**
- Finding a valid block requires massive real-world energy expenditure
- The longest chain (most accumulated work) is accepted as canonical
- Attacking the network requires outpacing the entire honest network's hash rate — the famous **51% attack** threshold

The difficulty adjusts automatically so that a new block is found roughly every 10 minutes (Bitcoin), regardless of how much total mining power exists.

**Trade-offs:** Secure and battle-tested, but energy-intensive and slow (~7 transactions per second for Bitcoin).

### Proof of Stake (PoS) — Ethereum (post-Merge)

Instead of competing with computation, validators are chosen to propose blocks in proportion to the **stake** (ETH) they've locked up as collateral.

- Validators are randomly selected, weighted by stake
- If they behave honestly, they earn rewards
- If they try to cheat, their stake is **slashed** (destroyed)

Economic incentive replaces computational work. The threat of losing your stake is what makes dishonesty irrational.

**Trade-offs:** Far more energy-efficient than PoW, faster finality, but introduces different trust assumptions around stake concentration.

### Other Mechanisms

- **DPoS (Delegated PoS)** — token holders vote for a small set of delegates (used by EOS, TRON)
- **PBFT (Practical Byzantine Fault Tolerance)** — used in permissioned blockchains (Hyperledger); deterministic finality, suited for smaller validator sets
- **PoA (Proof of Authority)** — validators are known, trusted entities; fast but not decentralised

---

## 7. How Trustlessness Emerges

"Trustless" doesn't mean you trust nobody. It means you don't need to trust *any specific party* — instead, you trust the **protocol and the mathematics**.

Here's how each component contributes:

| Component | What it eliminates |
|---|---|
| Public-key cryptography | Need to trust identity verification to a third party |
| Digital signatures | Need to trust that instructions came from the right person |
| Hashing | Need to trust that data hasn't been tampered with |
| Merkle trees | Need to trust a full node when verifying a transaction |
| Consensus protocol | Need to trust a central authority to order transactions |
| Chain of hashes | Need to trust that history hasn't been rewritten |

The result: two parties who have never met, in different countries, can exchange value — with finality, and without a bank, lawyer, or any intermediary. The rules are enforced by code and cryptography, not by institutions.

---

## 8. The Immutable Ledger

Bring it all together and you get the **immutable ledger** — blockchain's defining property.

Every confirmed transaction is:

1. **Signed** by the sender's private key (authenticity)
2. **Hashed** and included in a Merkle tree (integrity)
3. **Packed into a block** that references all previous blocks (ordering)
4. **Accepted by consensus** across thousands of independent nodes (decentralisation)

To rewrite a transaction confirmed 6 blocks deep in Bitcoin, an attacker would need to:
- Recompute the altered block's proof of work
- Recompute every subsequent block's proof of work
- Do all of this faster than the entire honest network keeps adding new blocks
- Sustain this for long enough to build a longer chain that nodes accept

With Bitcoin's current hash rate, this is not just difficult — it's economically irrational. The cost of the attack exceeds the value of anything you could gain from it.

This is why "6 confirmations" is considered final for large Bitcoin transactions. Not because it's mathematically impossible to reverse — but because the probability drops to effectively zero, and the cost rises to effectively infinity.

---

## Putting It All Together

```
Cryptography  →  proves ownership and authenticity
Hashing       →  creates tamper-evident fingerprints
Merkle Trees  →  summarises thousands of transactions efficiently
Transactions  →  express intent, signed and verified
Blocks        →  chain transactions together with cryptographic links
Consensus     →  thousands of nodes agree without trusting each other
               =
         Immutable, Trustless, Distributed Ledger
```

Each piece is necessary. Remove cryptography and you can't prove ownership. Remove consensus and you get competing versions of history. Remove the chain of hashes and history can be quietly rewritten.

The elegance of blockchain is that none of these components are new — cryptographic hashing and Merkle trees predate Bitcoin by decades. What Satoshi Nakamoto did was assemble them into a system where trustlessness emerges from the combination. That's the insight worth understanding.

In the next post, we'll go deeper into smart contracts — what they are, how the EVM executes them, and what "code is law" actually means in practice.
