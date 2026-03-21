---
layout: single
title: "Large Language Models: How AI Understands and Generates Language"
date: 2026-01-14 10:00:00 +0800
permalink: /computer-science/2026/03/31/large-language-models/
categories:
  - computer-science
tags:
  - llm
  - generative-ai
  - transformers
  - rlhf
  - tokenization
  - gpt
  - claude
---

This is Post 12 — the final post — in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [previous post](/computer-science/2026/03/30/deep-learning/) explained deep learning and transformers. Now we put it all together: **Large Language Models** — the technology behind ChatGPT, Claude, Gemini, and the AI revolution of the 2020s.

You've seen the entire stack: bits → CPU → OS → algorithms → data structures → networks → databases → applications → distributed systems → machine learning → deep learning. LLMs sit at the very top of this stack, built on all of it.

---

<img src="/assets/images/arch-llm.svg" alt="Large Language Models Overview" style="width:100%;max-width:860px;margin:1.5rem auto;display:block;border-radius:8px;">

## The Big Picture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    How an LLM Works                                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  1. Tokenization: "Hello world!" → [Hello] [world] [!] → [1234, 5678, 256]   ║
║                                                                              ║
║  2. Embedding: token IDs → high-dimensional vectors (numbers)                ║
║                                                                              ║
║  3. Transformer layers (96 of them for a large model):                       ║
║     Self-attention: each token looks at all other tokens                     ║
║     Feed-forward:   transform each token independently                       ║
║                                                                              ║
║  4. Output: probability distribution over all tokens in vocabulary           ║
║     "The next token is most likely [world] with prob 0.82"                   ║
║                                                                              ║
║  5. Sample: pick a token → append → repeat until done                        ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Training pipeline                                                           ║
║  Pretraining   → predict next token on internet-scale text (trillions)       ║
║  Fine-tuning   → train on high-quality examples of the target behavior       ║
║  RLHF          → human feedback → reward model → reinforcement learning      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. What Is a Language Model?

A **language model** is a probability distribution over text. Given some context, it predicts what comes next.

```
P(next token | previous tokens)

"The cat sat on the ___"
  → "mat" (0.45)
  → "floor" (0.23)
  → "chair" (0.12)
  → "sofa" (0.08)
  → ... (all other tokens)
```

**Large** means: billions of parameters (weights), trained on trillions of words.

GPT-3 (2020): 175 billion parameters.
GPT-4 (2023): estimated 1 trillion parameters.
Claude 3 (2024): hundreds of billions of parameters.

The "large" in LLM is what unlocked emergent capabilities that smaller models didn't have.

---

## 2. Tokenization — Breaking Text into Pieces

Computers don't process characters or words — they process **tokens**.

**Tokenization** breaks text into chunks using an algorithm (BPE — Byte Pair Encoding is most common):

```
"Hello world!" → ["Hello", " world", "!"]
Token IDs:     → [15496, 995, 0]

"Unbelievable!" → ["Un", "believ", "able", "!"]
(rarer words split into subword pieces)

"😀"          → [128512]
(emoji gets one token)
```

A vocabulary of ~50,000 to 100,000 tokens covers essentially all text. The LLM only ever sees numbers — never raw characters.

**Why not use words?** "Unbelievable", "unbelievably", "Unbelievably" would be three separate words, each needing to be learned separately. Subword tokenization shares "believ" across all of them.

**Context window**: the maximum number of tokens a model can process at once. GPT-3: 4,096 tokens. GPT-4: 128,000. Claude 3.5: 200,000. Longer context = can read entire books and reason over them.

---

## 3. Embeddings — Numbers That Carry Meaning

Token IDs (like 15496) are arbitrary numbers. They need to become meaningful vectors.

An **embedding** maps each token ID to a vector of numbers — typically 768 to 12,288 dimensions.

```
Token "king"  → [0.25, -0.13, 0.89, 0.04, ..., -0.67]   (12,288 numbers)
Token "queen" → [0.23, -0.15, 0.88, 0.17, ..., -0.62]   (similar vector!)
Token "car"   → [0.91, 0.45, -0.23, 0.78, ..., 0.34]    (very different)
```

The embedding space captures semantic relationships:

```
embedding("king") - embedding("man") + embedding("woman") ≈ embedding("queen")
```

This is not programmed — the network discovers these relationships during training. The geometry of the vector space mirrors the structure of language and the world.

---

## 4. Pretraining — Learning from the Internet

LLMs are pretrained on massive text datasets:

- Books (fiction, non-fiction, academic)
- Wikipedia
- Web pages (Common Crawl — a snapshot of the internet)
- Code (GitHub)
- Scientific papers (ArXiv, PubMed)
- Forums, news, subtitles

Total: **trillions of tokens** — more text than any human could read in thousands of lifetimes.

### The Training Objective: Next Token Prediction

The model is given text with the last token hidden, and must predict it.

```
Input:  "The capital of France is ___"
Target: "Paris"

Input:  "def fibonacci(n):\n    if n <= 1:\n        return ___"
Target: "n"

Input:  "The proof proceeds by ___"
Target: "induction"
```

This simple objective — predict the next word — forces the model to learn an enormous amount:
- Grammar and syntax
- Facts about the world
- How arguments are structured
- Programming patterns
- Mathematical reasoning
- And much more

### The Scale Hypothesis

Bigger models trained on more data are consistently better. This was not obvious — researchers expected diminishing returns. Instead, capability keeps growing with scale.

```
Model size × Data × Compute → emergent capabilities at scale

At 7B parameters:  can write a sentence
At 70B parameters: can write a coherent essay, basic reasoning
At 700B parameters: can write code, nuanced analysis, complex reasoning
```

"Emergent" means these capabilities appear suddenly at scale, not gradually. A model at 70B can do things the 7B model couldn't do at all.

---

## 5. Pretraining vs. a Useful Assistant

A pretrained model is a powerful autocomplete engine. Give it "The capital of France is" and it outputs "Paris". Give it "Write me a poem about cats" and it might output... more examples of that prompt, not an actual poem (it's seen many such prompts in training data).

Pretraining gives knowledge. But it doesn't give helpful behavior.

---

## 6. Fine-tuning — Teaching Helpful Behavior

**Supervised fine-tuning (SFT)**: train on examples of ideal behavior.

```
Human: "Explain quantum entanglement simply."
Assistant: "Imagine two coins that are magically linked..."
```

Thousands of such examples teach the model to follow instructions, answer questions, and behave helpfully.

---

## 7. RLHF — Human Feedback Makes It Better

**Reinforcement Learning from Human Feedback (RLHF)** is the technique that turned autocomplete into a useful assistant.

### Step 1: Collect Human Preferences

Show two model responses to the same prompt. A human picks the better one.

```
Prompt: "How do I make a good cup of coffee?"

Response A: "Use 15g of coffee per 250ml water at 93°C.
            Grind to medium coarseness for pour-over..."

Response B: "Put coffee in machine, press button. Done."
```

Human annotators mark Response A as better (more helpful, more detailed).

### Step 2: Train a Reward Model

Use the preference data to train a **reward model** — a neural network that predicts which response a human would prefer.

```
Reward model input:  (prompt, response)
Reward model output: a score (how good is this response?)

Response A → reward model → score: 0.87
Response B → reward model → score: 0.21
```

### Step 3: Use Reinforcement Learning

Use the reward model to give the LLM feedback as it generates:

```
LLM generates a response → reward model scores it → high score = good, low = bad
LLM adjusts its weights to generate higher-scoring responses
Repeat many times
```

This is like training a dog with treats — reward good behavior, and the model learns to do more of it.

RLHF is why modern LLMs are helpful, harmless, and honest. Without it, a pretrained model might complete "How do I build a bomb?" by continuing the text naturally — with instructions. After RLHF, it declines or redirects.

---

## 8. Inference — How a Response Is Generated

When you send a message to an LLM:

```
1. Tokenize your prompt
2. Feed tokens through the transformer (all layers)
3. Output: probability distribution over 50,000+ tokens
4. Sample one token (using temperature)
5. Append the token to the context
6. Repeat from step 2 until done (e.g., hits end-of-sequence token)
```

**Temperature** controls randomness:
- Temperature 0: always pick the highest-probability token (deterministic, repetitive)
- Temperature 0.7: a bit of randomness (creative but coherent)
- Temperature 2.0: very random (often nonsense)

Most LLMs generate about **10–60 tokens per second**. A 100-token response takes 2–10 seconds — not because the model is thinking, but because it's generating one token at a time.

### KV Cache

Generating each token requires running the full transformer over the entire context. If you've already processed tokens 1–100, there's no need to recompute their key-value pairs for token 101.

The **KV cache** stores these computed values, turning O(n²) generation into O(n). This is why the first token is slower than subsequent ones.

---

## 9. What LLMs Can and Cannot Do

### What they're surprisingly good at:

- Writing code, essays, emails, stories in many styles
- Explaining complex topics in simple terms
- Translating between languages
- Summarizing long documents
- Following complex multi-step instructions
- In-context learning: given a few examples in the prompt, they adapt their behavior

### What they struggle with:

**Factual accuracy**: LLMs generate plausible text. If they don't know something, they may generate a confident-sounding but wrong answer (**hallucination**). Always verify facts from LLM output.

**Arithmetic**: counting tokens is not the same as reasoning about numbers. LLMs often make arithmetic mistakes. Use a calculator or code for math.

**Real-time information**: knowledge is frozen at the training cutoff. The model doesn't know about events after that date (unless given tools to search the web).

**Reasoning chains**: while LLMs can follow a chain of thought if prompted to ("let's think step by step"), they can still make logical errors, especially in multi-step math or logic puzzles.

**Long-term consistency**: in very long conversations, models may contradict themselves or "forget" earlier context.

---

## 10. Prompting — Getting the Best Out of an LLM

How you phrase a request matters enormously.

### Be specific

```
Bad:   "Tell me about Python"
Good:  "Explain Python's list comprehension syntax with 3 examples,
        aimed at someone who knows JavaScript but not Python"
```

### Chain of thought

```
"Solve this step by step: If a train travels 120 km in 2 hours,
 and then 80 km in 1.5 hours, what is its average speed overall?"
```

Prompting the model to "think step by step" dramatically improves accuracy on reasoning tasks.

### Provide context

```
"I'm building a REST API in Python using FastAPI. I need to validate
 that a user-submitted email address is valid. Here's my current code:
 [code block]. How should I add email validation?"
```

The more relevant context you provide, the better the response.

### Few-shot examples

```
"Extract the city and date from each text:
 'Meeting in London on Tuesday' → city: London, date: Tuesday
 'Conference in Tokyo on March 15' → city: Tokyo, date: March 15
 'The event will be held in Berlin next Friday' → "
```

A few examples in the prompt teach the model the format and task.

---

## 11. The Broader Ecosystem

### Retrieval-Augmented Generation (RAG)

LLMs have a knowledge cutoff and limited context. RAG adds a retrieval step:

```
User question
     ↓
Search a vector database (documents embedded as vectors)
     ↓
Retrieve most relevant chunks
     ↓
Send: "Given this context: [retrieved text], answer: [question]"
     ↓
LLM answers based on retrieved context
```

This gives the LLM access to current information, proprietary documents, or knowledge bases — without retraining.

### Tool Use / Function Calling

Modern LLMs can call external tools:

```
User: "What's the weather in Singapore right now?"
LLM:  I'll check the weather API.
      [calls weather_api(city="Singapore")]
API:  {"temperature": 31, "condition": "partly cloudy"}
LLM:  It's 31°C and partly cloudy in Singapore right now.
```

The LLM reasons about which tool to call, when to call it, and how to interpret the result. This extends LLMs from language models to reasoning agents.

### Open Source LLMs

You don't have to use commercial APIs. Many powerful models are open source:

| Model      | Organization | Parameters | Notes                     |
|------------|-------------|------------|---------------------------|
| Llama 3    | Meta        | 8B–70B     | Very capable, free to use |
| Mistral    | Mistral AI  | 7B–141B    | Efficient, open weights   |
| Gemma      | Google      | 2B–9B      | Small but capable         |
| DeepSeek   | DeepSeek    | 7B–671B    | Strong reasoning          |

You can run a 7B model on a laptop with 8GB RAM. Larger models need more GPU VRAM.

---

## 12. The CS Stack, Revisited

We've now covered the entire stack. LLMs rest on every layer below:

```
Bits & Bytes           → model weights stored as float16/bfloat16 tensors
Computer Architecture  → 80GB GPUs run thousands of matrix multiplications/second
Operating Systems      → CUDA (GPU OS) schedules thousands of parallel ops
Algorithms             → attention is O(n²) — context length is limited by this
Data Structures        → KV cache, embedding lookup tables
Networks               → model served via HTTPS API across the internet
Databases              → training data stored in petabyte-scale object storage
Application Dev        → API wrappers, chat interfaces, embedding pipelines
Distributed Systems    → training distributed across 10,000 GPUs via model parallelism
Machine Learning       → gradient descent, loss functions, optimization
Deep Learning          → transformer architecture, attention, backpropagation
LLMs                   → all of the above, at unprecedented scale
```

---

## Summary

Large Language Models are:

```
What they are:
  Transformers pretrained on trillions of text tokens
  Fine-tuned and RLHF'd to be helpful assistants
  Predict the next token, one at a time

What enables them:
  Scale: billions of parameters + trillions of tokens + thousands of GPUs
  Transformer architecture: attention over full context
  RLHF: human preferences shape helpful, safe behavior

What they can do:
  Write, explain, translate, summarize, code, reason (with limitations)
  Follow complex instructions
  Learn from examples in the prompt (in-context learning)

What they can't do reliably:
  Accurate arithmetic
  Up-to-date facts (without tools)
  Multi-step logical proofs
  Guarantee correctness of any output
```

This is the end of the Computer Science Series. We've gone from the humble bit — a single 0 or 1 in a transistor — all the way to AI that writes, codes, and converses. Every layer built on the one below it. None of it is magic. All of it is engineering.

The best thing about understanding this stack is that nothing in technology can surprise you anymore. When you see a new technology, you know where to place it in the stack, what trade-offs it probably makes, and which layer it builds on.

The field keeps moving. New architectures replace old ones. New capabilities emerge from scale. But the foundations — bits, logic, algorithms, data structures, systems — stay relevant because every new layer is built on them.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)