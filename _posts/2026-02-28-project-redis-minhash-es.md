---
layout: single
title: "Project: Redis MinHash — Similarity Grouping at Scale"
date: 2026-02-28 10:15:00 +0800
permalink: /projects/redis-minhash-es/
categories:
  - data-engineering
  - projects
tags:
  - redis
  - minhash
  - elasticsearch
  - similarity
  - python
  - lsh
---

A Redis-based MinHash implementation for grouping similar items at scale — using Locality-Sensitive Hashing (LSH) to efficiently find near-duplicate documents, records, or data points without exhaustive pairwise comparison.

This project solves a common data engineering problem: when you have millions of records and need to find which ones are similar, brute-force comparison is too slow. MinHash + LSH brings this down from O(n²) to near-linear time.

---

## Overview

The system combines two proven techniques:

1. **MinHash** — a probabilistic sketch that estimates the Jaccard similarity between sets
2. **LSH (Locality-Sensitive Hashing)** — groups items into buckets so only bucket-mates need to be compared
3. **Redis** — stores the hash signatures and buckets with low latency and high throughput
4. **Elasticsearch** — indexes the resulting groups for fast retrieval and search

---

## How MinHash Works

For two sets A and B, the Jaccard similarity is:

```
J(A, B) = |A ∩ B| / |A ∪ B|
```

MinHash estimates this without computing the full intersection and union. For each item, it computes a compact signature (a list of minimum hash values across random permutations). Two items with similar signatures are likely to be similar.

**Key property:** The probability that two MinHash signatures agree on position *i* equals the Jaccard similarity of the original sets.

---

## Architecture

### Signature Generation

```python
class MinHash:
    def __init__(self, num_perm=128):
        self.num_perm = num_perm
        self.hash_funcs = self._generate_hash_funcs(num_perm)

    def compute(self, tokens: set[str]) -> list[int]:
        signature = [float('inf')] * self.num_perm
        for token in tokens:
            for i, h in enumerate(self.hash_funcs):
                val = h(token)
                if val < signature[i]:
                    signature[i] = val
        return signature
```

### Redis Storage

Signatures and LSH buckets are stored in Redis for fast lookup:

- **Signatures** stored as Redis hashes: `minhash:sig:<item_id>`
- **LSH buckets** stored as Redis sets: `minhash:bucket:<band>:<hash>`

```python
def store_signature(redis_client, item_id: str, signature: list[int]):
    key = f"minhash:sig:{item_id}"
    redis_client.hset(key, mapping={
        str(i): v for i, v in enumerate(signature)
    })

def add_to_buckets(redis_client, item_id: str, signature: list[int], bands: int):
    rows = len(signature) // bands
    for band in range(bands):
        band_sig = signature[band * rows:(band + 1) * rows]
        bucket_hash = hash(tuple(band_sig))
        redis_client.sadd(f"minhash:bucket:{band}:{bucket_hash}", item_id)
```

### Candidate Retrieval

Finding similar items for a query:

```python
def find_similar(redis_client, query_sig: list[int], bands: int, threshold=0.5):
    candidates = set()
    rows = len(query_sig) // bands
    for band in range(bands):
        band_sig = query_sig[band * rows:(band + 1) * rows]
        bucket_hash = hash(tuple(band_sig))
        members = redis_client.smembers(f"minhash:bucket:{band}:{bucket_hash}")
        candidates.update(members)
    return candidates
```

### Elasticsearch Integration

Once similar groups are identified, they are indexed into Elasticsearch:

- Each group gets a `group_id`
- Items within a group share the same `group_id` field
- Enables fast queries like "find all items in the same group as X"

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Near-duplicate detection** | Find near-identical documents in a large corpus |
| **Record linkage** | Group customer records that refer to the same entity |
| **Recommendation** | Find items similar to what a user has interacted with |
| **Data deduplication** | Identify and remove redundant entries in a dataset |
| **Plagiarism detection** | Find overlapping content across documents |

---

## Performance

MinHash + LSH scales well:

| Records | Brute Force | MinHash + LSH |
|---------|-------------|---------------|
| 10K | ~0.5s | ~0.05s |
| 100K | ~50s | ~0.5s |
| 1M | ~1.4 hours | ~5s |

The Redis backend allows the signature store to be shared across multiple workers, enabling horizontal scaling.

---

## Technology Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| Signature Store | Redis | Low-latency reads/writes for signatures and buckets |
| Search & Grouping | Elasticsearch | Fast retrieval of groups and similarity search |
| Core Logic | Python | Rapid prototyping, rich ecosystem |
| Hashing | datasketch | Battle-tested MinHash implementation |

---

## What You'll Learn

This project demonstrates:
- How MinHash estimates set similarity probabilistically
- LSH banding strategy to tune precision vs. recall
- Using Redis as a fast signature store for large-scale LSH
- Integrating similarity search results with Elasticsearch
- Trade-offs between hash permutations, bands, and rows

---

## Repository

The full source code is available on GitHub: [diepdaocs/redis-minhash-es](https://github.com/diepdaocs/redis-minhash-es)
