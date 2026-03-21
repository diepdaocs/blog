---
layout: single
title: "Data Structures: The Right Container for the Right Job"
date: 2026-01-07 10:00:00 +0800
permalink: /computer-science/2026/03/24/data-structures/
categories:
  - computer-science
tags:
  - data-structures
  - arrays
  - hash-tables
  - trees
  - graphs
  - linked-lists
---

This is Post 5 in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [previous post](/computer-science/2026/03/23/algorithms/) explained how to measure algorithm efficiency. Now we look at **data structures** — the containers that store data in ways that make algorithms fast.

The same algorithm on the wrong data structure can be 1000× slower than on the right one. Choosing wisely is one of the most practical skills in software engineering.

---

<img src="/assets/images/arch-data-structures.svg" alt="Data Structures Overview" style="width:100%;max-width:860px;margin:1.5rem auto;display:block;border-radius:8px;">

## The Big Picture

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    Data Structures: Trade-offs at a Glance                       ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  Structure       │ Access │ Search │ Insert │ Delete │ Best for                  ║
║  ────────────────┼────────┼────────┼────────┼────────┼────────────────────────   ║
║  Array           │  O(1)  │  O(n)  │  O(n)  │  O(n)  │ index by position         ║
║  Linked List     │  O(n)  │  O(n)  │  O(1)* │  O(1)* │ frequent insert/delete    ║
║  Hash Table      │  O(1)* │  O(1)* │  O(1)* │  O(1)* │ key-value lookup          ║
║  Binary Search T.│  O(log n) for all, if balanced    │ sorted data, range query  ║
║  Heap            │  O(1)  │  O(n)  │  O(log n)│ O(log n)│ min/max quickly        ║
║  Graph           │  O(1)  │  O(V+E)│  O(1)  │  O(E)  │ relationships             ║
║                                                                                  ║
║  * amortized or average                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Arrays — The Foundation

An **array** is a sequence of elements stored in **contiguous memory** — one right after another.

```
Index:  [0]  [1]  [2]  [3]  [4]
Value:  [10] [20] [30] [40] [50]
Memory: 1000 1004 1008 1012 1016  (each int = 4 bytes)
```

Because elements are contiguous, **random access is O(1)**: `arr[3]` takes one calculation: `base_address + 3 × element_size = 1000 + 12 = 1012`. Done.

**Strengths:**
- O(1) access by index
- Cache-friendly — elements sit next to each other in memory
- Simple and predictable

**Weaknesses:**
- Fixed size (in low-level languages) or expensive to resize
- Inserting/deleting in the middle: must shift all elements after → O(n)

```
Insert 15 at index 1:
Before: [10, 20, 30, 40, 50]
Shift:  [10, 20, 20, 30, 40, 50]  ← 20, 30, 40, 50 all moved right
Write:  [10, 15, 20, 30, 40, 50]  ← O(n) work
```

### Dynamic Arrays (Python lists, Java ArrayLists)

Dynamic arrays solve the fixed-size problem. When full, they allocate a new array ~2× the size and copy everything over.

```
Array is full (size 4):  [1, 2, 3, 4]
Append 5 → allocate new array of size 8 → copy → add 5
New array: [1, 2, 3, 4, 5, _, _, _]
```

Copying takes O(n), but it happens rarely (only when doubling). Amortized over many appends, each append costs O(1).

---

## 2. Linked Lists — Flexible Chains

A **linked list** stores elements as **nodes**, where each node holds a value and a pointer to the next node.

```
[10|→] → [20|→] → [30|→] → [40|null]
  head
```

Nodes can be scattered anywhere in memory — they don't have to be contiguous.

**Strengths:**
- O(1) insert or delete if you have a pointer to the node (just update pointers)
- No wasted space for empty slots

**Weaknesses:**
- O(n) to access element at index k (must follow pointers from head)
- Poor cache behaviour — nodes scattered in memory
- Extra memory for pointers

```
Insert 15 between 10 and 20:
1. Create new node [15|→]
2. Point 15's next → 20
3. Point 10's next → 15
Done! O(1) — no shifting.

[10|→] → [15|→] → [20|→] → [30|→] → [40|null]
```

**When to use:** when you need fast inserts/deletes and don't care about random access. Common in implementing queues, undo history, and music playlists.

---

## 3. Stacks and Queues

These are built on top of arrays or linked lists, with restricted operations.

### Stack — Last In, First Out (LIFO)

Like a stack of plates: you can only add or remove from the top.

```
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
pop()   → 3   (top removed)
pop()   → 2
```

Operations: `push` (add to top), `pop` (remove from top), `peek` (look at top).

**Used for:**
- Function call stack (when `f()` calls `g()`, `g` is pushed; when `g` returns, it's popped)
- Undo/redo in text editors
- Parsing expressions (matching parentheses)
- DFS graph traversal

### Queue — First In, First Out (FIFO)

Like a checkout line: first person in line is first served.

```
enqueue(A) → [A]
enqueue(B) → [A, B]
enqueue(C) → [A, B, C]
dequeue()  → A (front removed)
dequeue()  → B
```

Operations: `enqueue` (add to back), `dequeue` (remove from front).

**Used for:**
- BFS graph traversal
- Print queues, task queues
- Message queues between services (Kafka, RabbitMQ)

---

## 4. Hash Tables — O(1) Lookup Magic

A **hash table** (also called hash map or dictionary) stores key-value pairs with near-instant lookup.

```python
phone_book = {
    "Alice": "555-1234",
    "Bob":   "555-5678",
    "Carol": "555-9012"
}
phone_book["Alice"]  # O(1) lookup — instant!
```

### How It Works

1. Take the key ("Alice")
2. Run it through a **hash function** → get a number (e.g., 42)
3. Store the value at index 42 in an array
4. To look up: hash the key again, go to that index

```
hash("Alice") → 42 → array[42] = "555-1234"
hash("Bob")   → 17 → array[17] = "555-5678"
hash("Carol") → 91 → array[91] = "555-9012"

lookup("Alice") → hash → 42 → return array[42]  ← one step!
```

### Collisions

Two keys can hash to the same index — a **collision**. Solutions:

**Chaining**: each array slot holds a linked list of all keys that mapped there.

```
array[42] → [(Alice, 555-1234), (Dave, 555-0000)]  ← two keys collided at 42
```

**Open addressing**: if slot 42 is taken, try 43, 44, ... until empty.

A good hash function spreads keys evenly to minimize collisions. In practice, lookup is O(1) average.

### Real-World Use

Hash tables are everywhere:
- Python `dict` and `set`
- Database indexes on non-ordered columns
- Caches (URL → cached page)
- Counting word frequencies
- Detecting duplicates

---

## 5. Trees — Hierarchical Structure

A **tree** is a hierarchical structure with a root node, where each node has zero or more children.

```
         A          ← root
        / \
       B   C        ← children of A
      / \   \
     D   E   F      ← leaves (no children)
```

Trees model: file systems (folders within folders), HTML (DOM), company org charts, and much more.

### Binary Search Trees (BST)

A BST is a binary tree (each node has at most 2 children) with one rule: **left child < node < right child**.

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

This rule means **search is O(log n)** for a balanced tree:

```python
def search(node, target):
    if node is None: return None
    if target == node.value: return node
    if target < node.value:  return search(node.left,  target)
    else:                    return search(node.right, target)
```

At each step, you eliminate half the tree. After log₂(n) steps, you find it or confirm it's absent.

**Problem**: if you insert sorted data, the tree becomes a line:

```
1 → 2 → 3 → 4 → 5   (degenerate BST)
```

Now search is O(n), not O(log n). This is why self-balancing trees exist.

### Balanced Trees (AVL, Red-Black)

Self-balancing trees automatically rotate nodes to maintain balance after inserts and deletes. The result: **guaranteed O(log n)** for search, insert, and delete.

Red-black trees are used in Java's `TreeMap`, Python's `SortedList`, and many database index structures.

---

## 6. Heaps — Find the Min/Max Fast

A **heap** is a tree where every parent is ≤ its children (min-heap) or ≥ its children (max-heap). The root is always the minimum (or maximum).

```
Min-heap:
        1
       / \
      3   2
     / \ / \
    7  4 5  6
```

**Operations:**
- `find_min()`: O(1) — the root is always minimum
- `insert(x)`: O(log n) — add at bottom, bubble up
- `extract_min()`: O(log n) — remove root, restore heap property

**Used for:**
- Priority queues (process scheduling, Dijkstra's algorithm)
- Heap sort
- Finding the k smallest/largest elements

```python
import heapq
pq = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
heapq.heappop(pq)   # returns 1 — always the minimum
```

---

## 7. Graphs — Relationships Between Things

A **graph** is the most general structure: a set of nodes (vertices) with connections (edges).

```
Undirected graph:         Directed graph (digraph):
  A --- B                   A → B
  |     |                   ↑   ↓
  C --- D                   C ← D
```

Graphs represent: roads (cities connected by roads), social networks (people connected by friendships), dependencies (task A must happen before B), the internet (routers connected by links).

### Representing Graphs

**Adjacency list**: for each vertex, store a list of neighbors. Good for sparse graphs (few edges).

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

**Adjacency matrix**: a 2D array where `matrix[i][j] = 1` means there's an edge from i to j. Good for dense graphs (many edges), but O(V²) space.

```
     A  B  C  D
A  [ 0  1  1  0 ]
B  [ 1  0  0  1 ]
C  [ 1  0  0  1 ]
D  [ 0  1  1  0 ]
```

Graph algorithms (BFS, DFS, Dijkstra) were covered in the [Algorithms post](/computer-science/2026/03/23/algorithms/).

---

## 8. Choosing the Right Structure

| Problem                               | Best structure             |
|---------------------------------------|----------------------------|
| Access by integer index               | Array                      |
| Lookup by key                         | Hash table                 |
| LIFO (undo stack)                     | Stack                      |
| FIFO (task queue, BFS)                | Queue                      |
| Frequently insert/delete in middle    | Linked list                |
| Always need the minimum/maximum       | Heap                       |
| Sorted data, range queries            | Balanced BST               |
| Model relationships                   | Graph                      |
| Hierarchical data                     | Tree                       |

Real programs combine multiple structures. A web browser's tab history uses a stack. Its network request queue uses a queue. Its DNS cache uses a hash table. Its rendering tree uses, well, a tree.

---

## Summary

Data structures are not just CS theory — every line of code you write uses them. Python's `list` is a dynamic array. `dict` is a hash table. `set` is a hash table with no values. `heapq` is a heap.

Knowing what's underneath lets you:
- Choose the right tool (O(1) lookup vs O(n))
- Predict performance (why is this slow?)
- Debug unexpected behaviour (why is my dict using so much memory?)

```
Need fast access by key?         → hash table
Need sorted order?               → balanced BST
Need fast min/max?               → heap
Need to model relationships?     → graph
Need cache-friendly iteration?   → array
```

In the next post, we'll zoom out and look at **Networks & Security** — how computers talk to each other over the internet, and how we keep that communication safe.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)
