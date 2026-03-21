---
layout: single
title: "Welcome to the Computer Science Series"
date: 2026-02-27 09:00:00 +0800
categories:
  - computer-science
tags:
  - introduction
  - algorithms
  - data-structures
  - databases
  - distributed-systems
  - machine-learning
  - software-engineering
---

Computer Science is one of the youngest engineering disciplines and one of the most consequential. In fewer than 80 years it has gone from vacuum tubes to language models that write poetry. Yet the core ideas — what can be computed, how efficiently, and at what cost — have remained remarkably stable.

This series is a structured journey through the entire field. Not a university syllabus, not a tutorial series — something in between. Each post goes deep on one area: the ideas behind it, the trade-offs that shaped it, and the intuition you need to apply it well.

Whether you are starting out or have been writing code for years, I hope this gives you a clearer map of the territory.

---

## The CS Landscape

Every layer of computing builds on the one below it. Here is the full stack, from physics to intelligence:

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI & Machine Learning                          │
│        Classical ML · Deep Learning · LLMs · Generative AI          │
├─────────────────────────────────────────────────────────────────────┤
│                       Distributed Systems                           │
│      Consistency · Replication · Consensus · Scalability            │
├─────────────────────────────────────────────────────────────────────┤
│                    Application Development                          │
│          Web · APIs · Mobile · Architecture Patterns                │
├─────────────────────────────────────────────────────────────────────┤
│                          Databases                                  │
│        Relational · NoSQL · Transactions · Query Engines            │
├─────────────────────────────────────────────────────────────────────┤
│                   Networks & Security                               │
│          TCP/IP · HTTP · TLS · DNS · Auth · Cryptography            │
├─────────────────────────────────────────────────────────────────────┤
│              Algorithms & Data Structures                           │
│      Sorting · Searching · Graphs · Trees · Complexity              │
├─────────────────────────────────────────────────────────────────────┤
│           Operating Systems & Systems Programming                   │
│      Processes · Memory · Concurrency · File Systems                │
├─────────────────────────────────────────────────────────────────────┤
│                  Computer Architecture                              │
│          CPU · Memory Hierarchy · Instruction Sets                  │
├─────────────────────────────────────────────────────────────────────┤
│                      Foundations                                    │
│       Bits & Bytes · Logic · Discrete Math · Computability          │
└─────────────────────────────────────────────────────────────────────┘

```

Each layer depends on everything below it. A distributed system that ignores network fundamentals will fail in subtle ways. A machine learning model trained without understanding data structures will be impossibly slow. The goal of this series is to understand each layer deeply enough that the one above it makes sense.

---

## What Each Layer Is About

### Foundations — Bits, Logic & Computability

Everything a computer does reduces to manipulating ones and zeros. This layer covers how information is represented in binary, how logic gates compute with electricity, and — most profoundly — what computation itself means.

Alan Turing's 1936 paper introduced the Turing machine and proved that some problems are fundamentally undecidable: no algorithm can solve them, ever, regardless of hardware. Church and Turing showed that all sufficiently powerful computational models are equivalent. These results set the outer boundary of what computers can do.

Discrete mathematics — boolean logic, set theory, graph theory, combinatorics, probability — is the language in which CS ideas are expressed. You cannot reason about algorithms without it.

**Key questions:** What can be computed? What can't? How do we encode information? How does logic become electricity?

---

### Computer Architecture — How CPUs Actually Work

A CPU is a machine that fetches instructions from memory, decodes them, executes them, and writes results back. Understanding this loop — and the optimisations layered on top of it (pipelining, out-of-order execution, branch prediction, speculative execution) — explains why code that looks equivalent can run at wildly different speeds.

The memory hierarchy is equally critical. Registers are fast but tiny. L1 cache is small but close. RAM is large but slow. SSD is vast but enormously slower. Every algorithm you write is implicitly a negotiation with this hierarchy. Cache-friendly code can outperform mathematically-optimal-but-cache-hostile code by 10–100×.

**Key questions:** How does a CPU execute a program? Why does data locality matter? What are SIMD, branch prediction, and speculative execution?

---

### Operating Systems & Systems Programming

The OS is the software that manages hardware on behalf of all other programs. It abstracts physical memory into virtual address spaces (so programs can't corrupt each other), manages processes and threads, schedules CPU time, and handles I/O.

Systems programming means working close to the OS — managing memory manually, writing concurrent code, understanding how system calls work, and reasoning about undefined behaviour. Languages like C and Rust operate at this level. Understanding it makes you a better programmer even if you spend most of your time in Python or JavaScript.

Concurrency is the hardest part: race conditions, deadlocks, and memory visibility bugs are notoriously difficult to reproduce and debug. The concepts here — locks, semaphores, atomics, memory ordering — appear again when we get to distributed systems, where the same problems re-emerge at a larger scale.

**Key questions:** How does virtual memory work? What happens when you call `malloc`? What is a context switch? How do threads share state safely?

---

### Algorithms & Data Structures

This is the heart of the discipline. Algorithms are precise recipes for computation; data structures are the containers that make algorithms efficient.

Complexity analysis — Big O notation — gives us a language for comparing algorithms independent of hardware. Knowing that quicksort is O(n log n) average and O(n²) worst case, and understanding *why*, tells you when to use it and when to reach for something else.

The canonical data structures — arrays, linked lists, stacks, queues, hash tables, trees, heaps, graphs — are not arbitrary. Each is a trade-off between insertion cost, lookup cost, deletion cost, and memory usage. Choosing the wrong one can turn an O(n log n) algorithm into an O(n²) one without changing a single line of logic.

Graphs deserve special attention: an enormous class of real-world problems (shortest paths, dependency resolution, social networks, recommendation systems) are graph problems in disguise. BFS, DFS, Dijkstra, topological sort, and minimum spanning trees are tools that come up constantly.

**Key questions:** What is time and space complexity? When do I use a hash table vs a tree? How do I find the shortest path in a graph? What makes an algorithm correct?

---

### Networks & Security

The internet is a collection of networks that agree to speak the same language: TCP/IP. Understanding how packets are routed across the globe, how TCP provides reliable delivery over an unreliable medium, how DNS translates names to addresses, and how TLS secures connections — this knowledge is essential for anyone building anything that communicates.

Security is not a feature you add at the end. It is a discipline of threat modelling, defence in depth, and thinking adversarially. Cryptographic primitives (AES, RSA, ECDH, SHA-256) are the building blocks. TLS, JWT, OAuth, and certificate authorities are the structures built from them. SQL injection, XSS, CSRF, and supply chain attacks are the failure modes.

**Key questions:** How does a TCP connection work? What happens during a TLS handshake? How does public-key cryptography work? What is an OAuth flow?

---

### Databases

Databases are specialised programs for storing and querying data reliably at scale. The relational model — tables, foreign keys, SQL — has dominated for 50 years because it makes strong guarantees and has a clean mathematical foundation (relational algebra).

ACID transactions (Atomicity, Consistency, Isolation, Durability) are what distinguish a database from a file. Understanding how databases implement these properties — write-ahead logging, B-tree indexes, MVCC (Multi-Version Concurrency Control), two-phase locking — demystifies the magic and explains the performance characteristics.

NoSQL databases (document stores, key-value stores, column-family stores, graph databases) trade some of these guarantees for different trade-offs: horizontal scalability, flexible schemas, or specialised query models. Knowing when to reach for each is a core engineering skill.

Query optimisation — indexes, query plans, statistics — is where databases get deep. A missing index can make a query 1000× slower. Understanding execution plans is one of the highest-leverage debugging skills for application developers.

**Key questions:** How does a B-tree index work? What is MVCC? When should I use NoSQL? How do I read a query execution plan?

---

### Application Development

Application development is where most engineers spend most of their time — but "just building apps" conceals enormous complexity. REST, GraphQL, and gRPC are not equivalent; choosing between them requires understanding trade-offs in coupling, performance, and developer experience.

Architecture patterns — MVC, event-driven, CQRS, hexagonal — are solutions to recurring structural problems. Design patterns (factories, observers, strategies, decorators) are solutions to recurring code-level problems. Neither is a silver bullet, but understanding them gives you a vocabulary for discussing and comparing designs.

Software engineering practice — clean code, testing (unit, integration, end-to-end), CI/CD pipelines, code review, refactoring — is what separates software that works once from software that works for years. Technical debt is real and compounds like financial debt.

**Key questions:** How do I design a clean API? What makes code testable? When should I refactor vs rewrite? How do I make a CI/CD pipeline reliable?

---

### Distributed Systems

A distributed system is a collection of machines that cooperate to achieve a common goal — and that fail independently. This combination (cooperation + independent failure) is what makes distributed systems so hard.

The CAP theorem says that in the presence of a network partition, you must choose between consistency (every read sees the latest write) and availability (every request gets a response). Real systems navigate this with nuanced consistency models: strong consistency, eventual consistency, causal consistency, read-your-writes.

Consensus — getting a group of nodes to agree on a value even when some nodes fail — is foundational. Paxos and Raft are the canonical algorithms. They underlie etcd, ZooKeeper, and the coordination layers of almost every large distributed system.

Scaling strategies — sharding, replication, caching, load balancing — each introduce trade-offs. Sharding distributes data but makes cross-shard queries hard. Replication increases read throughput but requires synchronisation. Caching speeds reads but introduces consistency complexity.

**Key questions:** What is the CAP theorem? How does Raft achieve consensus? How do I design for horizontal scale? What is eventual consistency in practice?

---

### AI & Machine Learning

Machine learning is the technology that allows computers to learn patterns from data rather than having them programmed explicitly. Classical ML — linear regression, decision trees, SVMs, gradient boosting — remains highly effective for structured data and interpretable models.

Deep learning extends this with neural networks composed of many layers. Convolutional networks (CNNs) recognise images; recurrent networks (RNNs, LSTMs) process sequences; transformers process sequences with attention mechanisms and have become the dominant architecture for language tasks.

Large Language Models (LLMs) like GPT-4 and Claude are transformers trained on massive text corpora. They demonstrate in-context learning (following instructions from a prompt), few-shot learning, and emergent capabilities that were not anticipated from smaller models. Understanding how they work — tokenisation, attention, pretraining, RLHF fine-tuning, inference — is now essential for any engineer building AI-powered products.

**Key questions:** What is gradient descent? How does backpropagation work? What makes a transformer different from an RNN? How do LLMs generate text?

---

## The Series Roadmap

The posts will go deep on each layer, in order from the bottom up. This is not the only valid order — but it ensures that when I introduce a concept, the ideas it depends on have already been covered.

<div class="projects-grid" style="margin-top: 1rem;">

  <a href="/computer-science/2026/03/16/introduction-to-computer-science/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">0. Introduction to Computer Science: From Bits to AI</h2>
      <p class="project-card__excerpt">A high-level map of the entire CS landscape — hardware, software, networks, and AI — before we go deep on any one layer.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">overview</span>
        <span class="project-card__tag">foundations</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/16/bits-and-bytes/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">1. Bits & Bytes: How Computers Encode, Transmit, and Decode Everything</h2>
      <p class="project-card__excerpt">How numbers, text, audio, images, and video are encoded as bits — and how all of it travels across the internet and arrives at your screen.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">bits</span>
        <span class="project-card__tag">encoding</span>
        <span class="project-card__tag">networking</span>
        <span class="project-card__tag">tcp-ip</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/21/computer-architecture/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">2. Computer Architecture: Inside the CPU</h2>
      <p class="project-card__excerpt">The fetch-decode-execute cycle, pipelining, branch prediction, out-of-order execution, the memory hierarchy, and why cache misses hurt so much.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">cpu</span>
        <span class="project-card__tag">architecture</span>
        <span class="project-card__tag">cache</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/22/operating-systems/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">3. Operating Systems: The Software That Runs Everything Else</h2>
      <p class="project-card__excerpt">Processes, threads, virtual memory, the file system, system calls, and the concurrency primitives that every application depends on.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">os</span>
        <span class="project-card__tag">processes</span>
        <span class="project-card__tag">memory</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/23/algorithms/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">4. Algorithms: Thinking About Efficiency</h2>
      <p class="project-card__excerpt">Complexity analysis, sorting, searching, divide and conquer, dynamic programming, greedy algorithms, and how to reason about correctness.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">algorithms</span>
        <span class="project-card__tag">complexity</span>
        <span class="project-card__tag">dynamic-programming</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/24/data-structures/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">5. Data Structures: The Right Container for the Right Job</h2>
      <p class="project-card__excerpt">Arrays, linked lists, hash tables, trees, heaps, and graphs — the trade-offs behind each, and the real problems they solve.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">data-structures</span>
        <span class="project-card__tag">hash-tables</span>
        <span class="project-card__tag">graphs</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/25/networks-and-security/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">6. Networks & Security: How the Internet Works and How to Protect It</h2>
      <p class="project-card__excerpt">TCP/IP, DNS, TLS, HTTP/2 and HTTP/3, cryptographic primitives, common attack vectors, and how authentication and authorisation really work.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">networking</span>
        <span class="project-card__tag">security</span>
        <span class="project-card__tag">cryptography</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/26/databases/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">7. Databases: Storing and Querying Data at Scale</h2>
      <p class="project-card__excerpt">The relational model, ACID transactions, B-tree indexes, MVCC, query optimisation, and when to reach for NoSQL instead.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">databases</span>
        <span class="project-card__tag">sql</span>
        <span class="project-card__tag">nosql</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/27/application-development/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">8. Application Development: Building Software That Lasts</h2>
      <p class="project-card__excerpt">API design, architecture patterns, software engineering practices, testing strategies, CI/CD, and the craft of writing maintainable code.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">software-engineering</span>
        <span class="project-card__tag">api-design</span>
        <span class="project-card__tag">testing</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/28/distributed-systems/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">9. Distributed Systems: When One Machine Is Not Enough</h2>
      <p class="project-card__excerpt">CAP theorem, consistency models, consensus algorithms (Raft, Paxos), replication, sharding, caching, and the real meaning of "five nines" reliability.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">distributed-systems</span>
        <span class="project-card__tag">consistency</span>
        <span class="project-card__tag">consensus</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/29/machine-learning/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">10. Machine Learning: Teaching Computers to Learn</h2>
      <p class="project-card__excerpt">Supervised and unsupervised learning, gradient descent, decision trees, SVMs, ensemble methods, and when classical ML beats deep learning.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">machine-learning</span>
        <span class="project-card__tag">gradient-descent</span>
        <span class="project-card__tag">decision-trees</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/30/deep-learning/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">11. Deep Learning: Neural Networks and the Transformer Revolution</h2>
      <p class="project-card__excerpt">Backpropagation, CNNs, RNNs, the attention mechanism, transformers, pretraining, fine-tuning, and why scale changed everything.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">deep-learning</span>
        <span class="project-card__tag">transformers</span>
        <span class="project-card__tag">attention</span>
      </div>
    </div>
  </a>

  <a href="/computer-science/2026/03/31/large-language-models/" class="project-card">
    <div class="project-card__body">
      <h2 class="project-card__title">12. Large Language Models: How AI Understands and Generates Language</h2>
      <p class="project-card__excerpt">Tokenisation, the transformer architecture in depth, pretraining on internet-scale data, RLHF, inference, prompting, and what LLMs can and cannot do.</p>
      <div class="project-card__tags">
        <span class="project-card__tag">llm</span>
        <span class="project-card__tag">generative-ai</span>
        <span class="project-card__tag">rlhf</span>
      </div>
    </div>
  </a>

</div>

---

## A Note on Prerequisites

I assume you can read code — examples will be in Python, Go, or pseudocode. I do not assume a CS degree. Where I introduce mathematical notation I will explain it. My goal is to build intuition first, formalism second.

The best way to read this series is actively. When I describe an algorithm, try to implement it. When I describe a system, try to draw it. When I make a claim about performance, try to measure it.

Computer Science rewards curiosity more than memorisation. The questions matter as much as the answers.

---

*This series is a living document. Posts will be added as I write them. The structure above is the plan — reality will diverge from plans, and that is fine.*
