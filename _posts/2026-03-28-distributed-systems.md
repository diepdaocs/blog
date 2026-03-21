---
layout: single
title: "Distributed Systems: When One Machine Is Not Enough"
date: 2026-01-11 10:00:00 +0800
permalink: /computer-science/2026/03/28/distributed-systems/
categories:
  - computer-science
tags:
  - distributed-systems
  - consistency
  - consensus
  - replication
  - cap-theorem
  - raft
---

This is Post 9 in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [previous post](/computer-science/2026/03/27/application-development/) covered building applications. Now we look at what happens when your app grows beyond one machine — **distributed systems**.

YouTube serves billions of videos. WhatsApp delivers messages to 2 billion users. Google processes hundreds of thousands of search queries every second. No single machine can do this. The solution is many machines working together — and that introduces a whole new class of hard problems.

---

<img src="/assets/images/arch-distributed-systems.svg" alt="Distributed Systems Overview" style="width:100%;max-width:860px;margin:1.5rem auto;display:block;border-radius:8px;">

## The Big Picture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                      Distributed Systems                                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Why distribute?                                                             ║
║   → More throughput than one machine                                         ║
║   → Survive machine failures (fault tolerance)                               ║
║   → Serve users globally with low latency                                    ║
║                                                                              ║
║  The hard problems:                                                          ║
║   → Partial failures: some machines die, others keep running                 ║
║   → Network delays: messages arrive late or out of order                     ║
║   → Consistency: different machines have different views of data             ║
║   → Coordination: getting machines to agree on anything                      ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Key Concepts                                                                ║
║                                                                              ║
║  CAP theorem    → Consistency, Availability, Partition-tolerance             ║
║  Consensus      → Raft algorithm, used in etcd, CockroachDB                  ║
║  Replication    → leader-follower, multi-leader, leaderless                  ║
║  Sharding       → partition data across machines                             ║
║  Caching        → Redis, CDN — serve fast from nearby                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Why Distributed Is Hard

On a single machine, everything is easy:
- One memory space — no question about who sees what
- If the machine crashes, everything stops — no partial failure
- Clock is shared — no ambiguity about order of events

On multiple machines:
- **Partial failures**: Server A crashes, B and C keep running. From B's perspective, is A dead? Or just slow? You can't tell.
- **Network unreliability**: a message from A to B might arrive late, arrive twice, or not arrive at all.
- **No global clock**: A's clock might be 100ms ahead of B's. Which event happened first?

These aren't implementation bugs — they're fundamental properties of distributed systems. Every design decision is navigating these constraints.

---

## 2. The CAP Theorem

In 2000, Eric Brewer stated what became the **CAP theorem**: in a distributed system, you can have at most two of three properties:

```
C — Consistency:         every read sees the most recent write
A — Availability:        every request gets a response (not an error)
P — Partition tolerance: system works even when network splits
```

In practice, **network partitions always happen** (cables fail, routers restart). So you must choose between C and A when a partition occurs.

### CP System (Consistent + Partition-tolerant)

When a partition happens, refuse to serve requests rather than return stale data.

```
Network partition occurs:
  Server A (primary):  has latest data
  Server B (replica):  can't reach A

  Client asks B for user balance
  B: "I can't guarantee I have the latest data → I refuse to answer (error)"
```

Examples: HBase, ZooKeeper, most relational databases. Good for: banking, inventory systems where stale data causes real harm.

### AP System (Available + Partition-tolerant)

When a partition happens, still serve requests but might return stale data.

```
Network partition occurs:
  Server A: updates user's balance to $150
  Server B: can't reach A, still thinks balance is $100

  Client asks B for balance
  B: "I'll return $100. It might be stale, but at least you get an answer."
```

Examples: DynamoDB (Eventual mode), Cassandra, DNS. Good for: shopping carts, social media likes, analytics — where small staleness is acceptable.

### Eventual Consistency

Most AP systems promise **eventual consistency**: if you stop writing, all replicas will eventually converge to the same value.

```
Time 0:  A=100 on all nodes
Time 1:  Write $50 to Node 1 → Node 1 has A=150
Time 2:  (propagation) → Node 2 gets the update → A=150
Time 3:  All nodes consistent: A=150
```

The window of inconsistency might be milliseconds or seconds. For most applications (social media, shopping recommendations), this is fine.

---

## 3. Replication — Copies for Safety

**Replication** keeps copies of data on multiple machines, so if one fails, others have the data.

### Leader-Follower (Primary-Replica)

One leader accepts all writes. Followers replicate the leader and serve reads.

```
Leader (primary):
  Accepts writes
  Replicates to followers asynchronously

Followers (replicas):
  Serve reads (possibly slightly stale)
  Promote to leader if leader fails
```

Used by PostgreSQL, MySQL, MongoDB, Redis.

**Synchronous replication**: wait for follower to confirm before acknowledging the write.
- Pro: no data loss if leader dies
- Con: every write is slower (must wait for network round-trip to follower)

**Asynchronous replication**: acknowledge immediately, replicate in background.
- Pro: fast writes
- Con: if leader dies before replication, the last few writes are lost

### Multi-Leader

Multiple nodes accept writes. Used when writes come from multiple geographic regions.

```
US datacenter (Leader 1) ←──sync──→ Asia datacenter (Leader 2)
   ↑ accepts US writes                    ↑ accepts Asia writes
```

**Problem**: what if both leaders accept a different write to the same record?

```
Leader 1: user changes name to "Alice"
Leader 2: user changes name to "Alicia"
(at same time, before sync)
→ conflict!
```

Conflicts must be resolved somehow: last-write-wins, merge, or show both to the user.

### Leaderless (Dynamo-style)

Any node can accept writes. A write succeeds if W nodes confirm. A read succeeds if R nodes respond. If W + R > N (total nodes), reads will always see at least one up-to-date copy.

Used by Cassandra, DynamoDB, Riak. Very available — no single point of failure.

---

## 4. Consensus — Agreeing on Anything

If multiple nodes can receive writes, how do they agree on who's the leader? Who wins a conflict? What's the definitive order of events?

This is the **consensus problem**: getting a group of nodes to agree on a value, even when some nodes fail.

Consensus turns out to be hard. The **FLP impossibility theorem** (1985) proved it's impossible to achieve consensus in an asynchronous system if even one node can fail. In practice, systems add timeouts and assumptions to work around this.

### Raft — How Most Systems Do It

**Raft** is the consensus algorithm used in etcd (Kubernetes' backbone), CockroachDB, TiKV, and Consul.

#### Leader Election

```
All nodes start as followers.
If a follower hears nothing from a leader for ~150ms, it becomes a candidate.
Candidate asks others for votes.
If it gets a majority, it becomes the leader.
Leader sends heartbeats to prevent re-elections.

Election example (3 nodes: A, B, C):
  1. Leader C crashes
  2. A and B both wait a random timeout (A waits 150ms, B waits 200ms)
  3. A times out first → becomes candidate, votes for itself (1/3)
  4. A requests votes from B → B votes for A (2/3) → A wins!
  5. A becomes new leader, sends heartbeats
```

The random timeout prevents both A and B from starting an election simultaneously.

#### Log Replication

Once a leader is elected, it replicates every write to followers before committing:

```
Client: "set x = 5"
Leader: 1. Append to own log: [set x = 5]
        2. Send to followers
        3. Wait for majority to confirm (2/3 nodes)
        4. Commit → apply to state machine
        5. Reply to client: "done"
```

If the leader crashes after commit but before telling the client, the client retries and gets "already done". Because the write is in the majority's logs, it won't be lost.

**Raft guarantees**: any committed write will survive any single machine failure (in a 3-node cluster). For tolerance of 2 failures: 5 nodes. For k failures: 2k+1 nodes.

---

## 5. Sharding — Splitting Data Across Machines

When data grows beyond what one machine can hold or one machine can write fast enough, you **shard** — partition data across multiple machines.

```
Shard by user_id:
  Shard 1: user_id % 3 == 0  (users 0, 3, 6, 9...)
  Shard 2: user_id % 3 == 1  (users 1, 4, 7, 10...)
  Shard 3: user_id % 3 == 2  (users 2, 5, 8, 11...)
```

Queries for one user go to one shard. Each shard handles 1/3 of the load.

**Problems with sharding:**
- **Cross-shard queries** (JOINs across shards) are very expensive — must query all shards
- **Rebalancing**: adding a new shard means moving lots of data
- **Hot spots**: if user_id 1 is 10× more active than others, Shard 1 is overloaded

**Consistent hashing** solves the rebalancing problem — when you add a shard, only a fraction of keys need to move.

---

## 6. Caching — Fast Data from Nearby

Not all load needs to hit the database. **Caching** stores frequently accessed data in a fast store (like Redis, in RAM).

```
Request: GET /api/product/123
  → Check Redis cache
     Hit:  return in < 1ms
     Miss: query database (50ms) → store in Redis → return
```

**Cache invalidation** is the hard part: when data changes in the database, you must update or remove the cached copy. Stale cache = users see old data.

```python
# After updating a product:
db.execute("UPDATE products SET price=99 WHERE id=123")
redis.delete("product:123")   # invalidate cache
# Next request will miss cache → fetch fresh from DB → re-cache
```

**CDN (Content Delivery Network)**: a global cache for static files (images, CSS, JS). User in Vietnam gets files from a nearby CDN edge in Singapore, not from a server in the US. 10ms vs 200ms.

---

## 7. The Reality: Trade-offs Everywhere

Distributed systems are a trade-off negotiation:

| Want                  | Trade-off                                              |
|-----------------------|--------------------------------------------------------|
| Strong consistency    | Higher latency (wait for majority), lower availability |
| High availability     | Possible stale reads, conflict resolution needed       |
| Low latency           | Async replication → possible data loss                 |
| Horizontal scale      | No cross-shard JOINs, complex rebalancing              |
| Global distribution   | Higher replication lag, conflict probability           |

The right design depends on what your system actually needs. A payment system needs strong consistency — stale data causes real financial harm. A social media "likes" counter doesn't — being off by a few likes for a second is fine.

---

## Famous Distributed System Disasters

Real incidents that show these problems are real:

- **GitHub, 2012**: MySQL failover left a replica as leader. Both old and new leader accepted writes. Conflicting data corrupted the database.
- **Amazon DynamoDB, 2011**: Metadata service overloaded → cascading failures across multiple AWS regions.
- **Cloudflare, 2019**: A BGP routing misconfiguration caused 15 minutes of partial internet outage globally.

Every large distributed system has failure stories. The goal isn't to prevent all failures — it's to design systems that fail gracefully and recover quickly.

---

## Summary

Distributed systems are hard because physical reality is hard:

```
Partial failures    → some nodes die; design for it
Network unreliability → messages are lost/delayed; handle it
No global clock    → order of events is ambiguous; track causality
CAP theorem         → choose consistency or availability during partitions
Raft consensus      → elect a leader, replicate a log, achieve agreement
Replication         → copies for fault tolerance and scale
Sharding            → split data for write scale
Caching             → serve fast from nearby; invalidate carefully
```

Building correct distributed systems requires thinking carefully about failure modes, not just the happy path. The best engineers design for failure — they ask "what happens when this network link goes down?" before shipping.

In the next post, we'll look at **Machine Learning** — how computers learn patterns from data instead of being explicitly programmed.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)
