---
layout: single
title: "Introduction to Computer Science: From Bits to Generative AI"
date: 2026-03-16 09:00:00 +0800
categories:
  - computer-science
tags:
  - introduction
  - bits-and-bytes
  - algorithms
  - data-structures
  - machine-learning
  - generative-ai
  - search
  - networking
---

This is the first deep-dive post in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). Whether you're just starting out or looking to consolidate your mental model of the field, this post gives you a map of the entire landscape — from the smallest unit of data a computer understands, all the way up to systems that can write code and generate images.

The structure below is inspired by Stanford's [CS101: Introduction to Computing Principles](https://online.stanford.edu/courses/soe-ycscs101-computer-science-101) — one of the best overviews of the field for any level of experience.

---

## 1. Bits & Bytes — The Language of Machines

Everything a computer does reduces down to **bits**: a value that is either `0` or `1`. That's it. Every video, every message, every running program is ultimately a long sequence of these two states, stored in transistors on a chip.

- **1 bit** = a single `0` or `1`
- **1 byte** = 8 bits → can represent 256 distinct values (0–255)
- **1 kilobyte (KB)** ≈ 1,000 bytes, **1 megabyte (MB)** ≈ 1 million bytes, and so on

Numbers are stored in **binary** (base-2). Text is encoded using standards like **ASCII** or **UTF-8**, which map characters to numbers. Images are grids of pixels, each pixel a triplet of numbers for red, green, and blue. Sound is a stream of amplitude samples over time.

The key insight: **everything is data, and all data is numbers, and all numbers are bits**. Once you internalize this, the rest of computer science starts to make sense.

---

## 2. Hardware — The Physical Machine

Software runs on hardware. Understanding the physical machine demystifies a lot of what feels like magic.

The key components:

- **CPU (Central Processing Unit)** — the brain. Executes instructions billions of times per second. Modern CPUs have multiple cores, each able to run tasks in parallel.
- **RAM (Memory)** — fast, temporary storage the CPU uses while working. Loses data when powered off.
- **Disk / SSD** — slow but persistent storage. Data survives reboots.
- **GPU (Graphics Processing Unit)** — originally for rendering graphics, now essential for training machine learning models due to its ability to run thousands of operations in parallel.
- **Network interface** — the hardware that connects you to the internet.

The speed hierarchy matters: CPU registers → CPU cache → RAM → SSD → network. Every step is orders of magnitude slower than the previous. Good software is designed around this hierarchy.

---

## 3. How Software Works — Programs, Compilers & the Runtime

A **program** is a set of instructions that tell the CPU what to do. You write those instructions in a high-level language (Python, Java, JavaScript, C), and they get translated down to machine code — the binary instructions the CPU actually understands.

This translation happens via:

- **Compilers** — transform the entire source code into machine code before running (e.g. C, Rust, Go)
- **Interpreters** — read and execute code line by line at runtime (e.g. Python, Ruby)
- **JIT (Just-in-Time) compilers** — a hybrid that compiles code at runtime for speed (e.g. Java's JVM, JavaScript's V8 engine)

Key concepts: variables, functions, loops, conditionals, and recursion. These are the building blocks that every program — from a web app to a machine learning model — is made from.

---

## 4. Data Structures — Organizing Information

Data structures define **how data is stored and organized** in memory. The choice of data structure directly impacts the performance of your program.

The essential ones:

| Structure | Best For | Key Operation Cost |
|---|---|---|
| **Array** | Index-based access | O(1) read, O(n) insert |
| **Linked List** | Frequent insertions/deletions | O(1) insert, O(n) search |
| **Hash Map** | Key-value lookups | O(1) average get/set |
| **Tree** | Hierarchical data, sorted data | O(log n) search |
| **Graph** | Relationships & connections | Varies |
| **Stack / Queue** | Order-dependent processing | O(1) push/pop |

Every database, file system, compiler, and operating system is built on these primitives. Learning them is non-negotiable for any serious engineer.

---

## 5. Algorithms — Solving Problems Efficiently

An **algorithm** is a step-by-step procedure for solving a problem. Two algorithms can produce the same result but differ dramatically in how long they take or how much memory they use.

This is measured with **Big O notation** — a way to describe how an algorithm's time or space requirements grow as the input size grows.

Core algorithm categories:

- **Sorting** — arranging data in order. QuickSort and MergeSort are O(n log n). BubbleSort is O(n²) and too slow for real use.
- **Searching** — finding an element. Linear search is O(n); binary search on sorted data is O(log n).
- **Recursion & Divide-and-Conquer** — breaking a problem into smaller instances of itself (e.g. MergeSort, binary search trees).
- **Dynamic Programming** — caching intermediate results to avoid redundant computation (e.g. shortest paths, sequence alignment).
- **Greedy Algorithms** — making the locally optimal choice at each step (e.g. Dijkstra's shortest path).
- **Graph Algorithms** — BFS and DFS for traversal; Dijkstra and A* for pathfinding.

Algorithms are the difference between a system that handles 1,000 users and one that handles 1,000,000.

---

## 6. Networking & The Internet

The internet is a global network of computers communicating via agreed-upon protocols.

How it works at a high level:

- **IP addresses** identify every device on the network
- **DNS (Domain Name System)** translates `google.com` into an IP address — it's the internet's phone book
- **TCP/IP** governs how data is broken into packets, sent, and reassembled at the destination
- **HTTP/HTTPS** is the protocol browsers and servers use to exchange web pages and APIs
- **TLS/SSL** encrypts that traffic so it can't be read in transit

When you type a URL in your browser, it: resolves the domain via DNS → opens a TCP connection → performs a TLS handshake → sends an HTTP request → receives a response → renders the page. All in under a second.

---

## 7. Databases — Storing & Querying Data at Scale

Programs need to persist data beyond a single run. **Databases** are purpose-built systems for storing, indexing, and querying large amounts of data reliably.

Two major families:

- **Relational databases (SQL)** — data is stored in tables with defined schemas. Relationships are modeled via foreign keys. SQL (Structured Query Language) is used for querying. Examples: PostgreSQL, MySQL, SQLite.
- **NoSQL databases** — schema-flexible storage for documents (MongoDB), key-value pairs (Redis), wide-column data (Cassandra), or graphs (Neo4j). Chosen for scale, flexibility, or access pattern requirements.

Core database concepts: **ACID** (Atomicity, Consistency, Isolation, Durability), **indexes** (speed up queries), **transactions** (all-or-nothing operations), and **normalization** (reducing data redundancy).

---

## 8. Search & Retrieval Systems

Search is one of the most practically important problems in computer science. It underpins Google, e-commerce product search, code search, and document retrieval.

**Classic information retrieval** is built on:

- **Inverted indexes** — for every word, store a list of documents containing it. This makes full-text search fast.
- **TF-IDF (Term Frequency-Inverse Document Frequency)** — a score that weights terms by how often they appear in a document vs. how common they are across all documents.
- **BM25** — the industry-standard relevance ranking algorithm still used by Elasticsearch and Solr today.

**Vector search** (semantic search) is a newer and increasingly dominant approach:

- Documents and queries are converted into **embedding vectors** — lists of numbers that capture meaning
- Similar documents cluster close together in this high-dimensional space
- Search becomes a **nearest-neighbor lookup** in vector space, not a keyword match
- Tools: FAISS, Pinecone, pgvector, Weaviate

Modern search systems often combine both: keyword matching for precision, vector search for semantic recall.

---

## 9. Systems Design — Architecture at Scale

When a single machine isn't enough, you start thinking about **distributed systems** — multiple machines working together as one.

Core concepts:

- **Horizontal vs. vertical scaling** — add more machines vs. make one machine more powerful
- **Load balancing** — distribute incoming requests across multiple servers
- **Caching** — store frequently-accessed data in fast memory (Redis, Memcached) to avoid expensive recomputation or database hits
- **Message queues** — decouple producers and consumers of data for resilience and throughput (Kafka, RabbitMQ)
- **CAP Theorem** — in a distributed system, you can only guarantee two of: Consistency, Availability, and Partition tolerance
- **Replication & Sharding** — copy data across nodes for redundancy; split it across nodes for scale

This is the gap between a side project and a production system. Systems design interviews at top tech companies test exactly this.

---

## 10. Machine Learning — Teaching Machines to Learn

Traditional programming is explicit: you write rules, the machine follows them. **Machine learning** flips this: you give the machine data and outcomes, and it learns the rules itself.

The core idea:

1. Collect labeled training data (inputs + correct outputs)
2. Choose a model architecture (a parameterized function)
3. Train: adjust the parameters to minimize a loss function using **gradient descent**
4. Evaluate on unseen test data
5. Deploy

Key paradigms:

- **Supervised learning** — learn from labeled examples (classification, regression). Examples: spam detection, house price prediction.
- **Unsupervised learning** — find structure in unlabeled data (clustering, dimensionality reduction). Examples: customer segmentation, anomaly detection.
- **Reinforcement learning** — an agent learns by taking actions and receiving rewards. Used in game-playing AI (AlphaGo) and robotics.

Essential algorithms: linear regression, logistic regression, decision trees, random forests, support vector machines, k-means clustering, and **neural networks**.

---

## 11. Deep Learning — Neural Networks at Scale

**Deep learning** is a subfield of machine learning using **neural networks** with many layers. Each layer learns increasingly abstract representations of the input.

- **CNNs (Convolutional Neural Networks)** — excel at image data; detect edges, textures, shapes, objects in sequence
- **RNNs (Recurrent Neural Networks)** — designed for sequences; used in early NLP and time-series modeling
- **Transformers** — the architecture that changed everything. Uses self-attention to model relationships between all parts of the input simultaneously. Introduced in the 2017 paper *Attention Is All You Need*.

Deep learning powers: image recognition, speech recognition, language translation, protein folding (AlphaFold), drug discovery, and much more.

---

## 12. Generative AI — Machines That Create

**Generative AI** refers to models that can produce new content — text, images, audio, code, video — that didn't exist before.

The major families:

- **Large Language Models (LLMs)** — transformers trained on massive text datasets to predict the next token. GPT-4, Claude, Gemini. Given a prompt, they generate coherent, contextually appropriate text. The same architecture powers code completion, summarization, translation, and reasoning.
- **Diffusion models** — learn to denoise random noise into structured outputs. Power image generators like DALL-E, Stable Diffusion, and Midjourney.
- **Retrieval-Augmented Generation (RAG)** — combines a vector search system (section 8) with an LLM. The model retrieves relevant documents at inference time and uses them as context, reducing hallucination and enabling up-to-date answers.
- **Agents** — LLMs connected to tools (search, code execution, APIs) to complete multi-step tasks autonomously.

Generative AI sits at the intersection of nearly everything above: it runs on specialized hardware (GPUs/TPUs), is built on transformer architectures (deep learning), uses vector search (retrieval), and is served via distributed systems (systems design).

---

## The Map

Here's how all these topics connect:

```
Bits & Bytes
    └── Hardware (CPU, RAM, GPU)
         └── Software & Programs
              ├── Data Structures & Algorithms
              │    └── Databases & Search Systems
              ├── Networking & The Internet
              │    └── Systems Design & Scale
              └── Machine Learning
                   └── Deep Learning
                        └── Generative AI (LLMs, Diffusion, RAG, Agents)
```

Each layer builds on the one below it. You can enter the field at any point, but the deeper your understanding of the foundations, the more clearly you see what's happening at the top.

---

## What's Next

The next post goes deep on the very first layer — **Bits & Bytes**: how numbers, text, audio, images, and video are encoded as binary; how data travels across the internet through TCP/IP, TLS, and CDNs; and how it's decoded and rendered on the receiving end.

**[Read next: Bits & Bytes — How Computers Encode, Transmit, and Decode Everything →](/computer-science/2026/03/16/bits-and-bytes/)**

Future posts will continue down the map — hardware, operating systems, networking, databases, and more. If there's a topic you'd like me to prioritize, drop a comment below.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)

---

## References

- [Stanford CS101: Introduction to Computing Principles](https://online.stanford.edu/courses/soe-ycscs101-computer-science-101) — the course that inspired the structure of this post
- [Stanford CS101 Syllabus](https://web.stanford.edu/class/cs101/syllabus.html)
