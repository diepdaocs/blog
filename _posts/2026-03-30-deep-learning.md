---
layout: single
title: "Deep Learning: Neural Networks and the Transformer Revolution"
date: 2026-01-13 10:00:00 +0800
permalink: /computer-science/2026/03/30/deep-learning/
categories:
  - computer-science
tags:
  - deep-learning
  - neural-networks
  - transformers
  - attention
  - backpropagation
  - cnn
---

This is Post 11 in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [previous post](/computer-science/2026/03/29/machine-learning/) covered classical machine learning. Now we go deeper: **neural networks** — the technology behind image recognition, speech assistants, translation, and AI that writes code.

Deep learning is what made AI feel magical. A computer recognizing your face, understanding your voice, translating a paragraph — all of this runs on neural networks. The ideas have been around since the 1980s, but two things made them work: much more data and much faster GPUs.

---

<img src="/assets/images/arch-deep-learning.svg" alt="Deep Learning Overview" style="width:100%;max-width:860px;margin:1.5rem auto;display:block;border-radius:8px;">

## The Big Picture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    Deep Learning Architecture Family                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Basic Neural Network (MLP)                                                  ║
║  Input → [hidden layers] → Output                                            ║
║  used for: tabular data, simple classification                               ║
║                                                                              ║
║  Convolutional Neural Network (CNN)                                          ║
║  Input → [Conv layers → Pool] → [Fully connected] → Output                   ║
║  used for: images, video, anything with spatial structure                    ║
║                                                                              ║
║  Recurrent Neural Network (RNN/LSTM)                                         ║
║  Input₁ → Input₂ → Input₃ → ... → Output                                     ║
║  used for: sequences — speech, text, time series                             ║
║                                                                              ║
║  Transformer                                                                 ║
║  [Attention over all tokens simultaneously]                                  ║
║  used for: language, code, images, everything (it took over)                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Neurons — The Building Block

The brain has ~86 billion neurons, each connected to thousands of others. In 1943, McCulloch and Pitts proposed a mathematical model of a neuron.

A **neuron** in a neural network:

1. Receives multiple inputs (x₁, x₂, ..., xₙ)
2. Multiplies each by a weight (w₁, w₂, ..., wₙ)
3. Sums them up, adds a bias
4. Applies an **activation function**
5. Outputs one value

```
       x₁ ──w₁──┐
       x₂ ──w₂──┼──→ (w₁x₁ + w₂x₂ + w₃x₃ + b) → f(z) → output
       x₃ ──w₃──┘

f(z) = activation function (adds non-linearity)
```

Without activation functions, stacking layers would just be a big linear equation — no more powerful than one layer. Activation functions make neural networks able to learn any function.

Common activation functions:

```
ReLU (Rectified Linear Unit): f(z) = max(0, z)
  → most common in hidden layers
  → fast, effective, doesn't "saturate"

Sigmoid: f(z) = 1 / (1 + e^(-z))  → output between 0 and 1
  → used in output layer for probability

Tanh: f(z) = (e^z - e^(-z)) / (e^z + e^(-z))  → output between -1 and 1

Softmax: turns a vector into a probability distribution (sums to 1)
  → used in output layer for multi-class classification
```

---

## 2. Neural Networks — Layers of Neurons

Connect many neurons in layers:

```
Input Layer    Hidden Layer 1   Hidden Layer 2   Output Layer
   x₁ ─────────○ ─────────── ○ ─────────── ○
   x₂ ──────── ○ ─────────── ○ ─────────── ○ ──→ prediction
   x₃ ─────────○ ─────────── ○
   x₄ ──────── ○
```

**Deep** learning = many hidden layers. Networks with 10, 50, 100+ layers are common.

### Why Deep?

Each layer learns increasingly abstract features.

For image recognition:
```
Layer 1: detects edges (horizontal, vertical, diagonal)
Layer 2: combines edges into shapes (corners, circles, curves)
Layer 3: combines shapes into parts (eyes, wheels, windows)
Layer 4: combines parts into objects (face, car, building)
Layer 5: classifies the object
```

No one programs these hierarchical features. The network discovers them during training.

---

## 3. Backpropagation — How Neural Networks Learn

Training a neural network means finding weights that minimize the loss (error). The algorithm is **backpropagation** combined with gradient descent.

### Forward Pass

Run input through the network → get prediction → calculate loss.

```
input → layer 1 → layer 2 → ... → output → loss = (output - true_label)²
```

### Backward Pass

Calculate how much each weight contributed to the error. Using the **chain rule** from calculus, propagate the error backward from output to input.

```
∂loss/∂w = how much changing w changes the loss

Chain rule:
∂loss/∂w₁ = ∂loss/∂output × ∂output/∂layer₂ × ∂layer₂/∂w₁
```

### Update

Move each weight in the direction that reduces loss:

```
w = w - learning_rate × ∂loss/∂w
```

Repeat for every training example (or batch of examples). After thousands of iterations over millions of examples, the weights converge to values that make good predictions.

Frameworks like PyTorch and TensorFlow compute gradients automatically (autograd) — you write the forward pass, and the library handles backpropagation.

---

## 4. CNNs — Seeing the World

**Convolutional Neural Networks** are designed for images (and anything with spatial structure).

The key idea: share weights spatially. Instead of connecting every pixel to every neuron (a 1920×1080 image would need 2 million weights per neuron), use a small **filter** (kernel) that slides across the image.

### Convolution

A 3×3 filter slides over the image, computing a dot product at each position:

```
Image patch:    Filter:     Output:
1 0 1           1 0 1
0 1 0     ×     0 1 0   =  sum = 5  (one value in the feature map)
1 0 1           1 0 1
```

Different filters detect different features:

```
Edge filter:    [ -1  0  1 ]    detects vertical edges
                [ -1  0  1 ]
                [ -1  0  1 ]

Blur filter:    [ 1/9 1/9 1/9 ]   averages neighboring pixels
                [ 1/9 1/9 1/9 ]
                [ 1/9 1/9 1/9 ]
```

The network **learns** what filters to use — you don't specify them. After training, you'll find filters that detect edges, textures, colors, shapes, etc.

### Pooling

After convolution, **max pooling** downsamples by taking the maximum in each region:

```
Feature map:    After 2×2 max pool:
4 2 6 8         6 8
3 5 1 2    →    5 3
9 3 2 1         9 2
0 1 3 1
```

Reduces size, gives some translation invariance (a cat is still a cat if it shifts a few pixels).

### CNN Architecture

```
Input image (3×224×224 pixels)
  → Conv + ReLU → feature maps
  → Conv + ReLU → deeper features
  → Max Pool → halve size
  → Conv + ReLU → ...
  → Flatten
  → Fully Connected → class probabilities
```

Modern CNN architectures (ResNet, EfficientNet, ConvNeXt) achieve superhuman accuracy on image classification by stacking dozens of layers.

**Applications**: image classification, object detection, face recognition, medical imaging, self-driving car vision.

---

## 5. RNNs — Processing Sequences

Standard networks process fixed-size inputs. Language, speech, and time series have **variable-length sequences** — sentences can be 5 words or 500 words.

**Recurrent Neural Networks (RNNs)** process sequences one element at a time, keeping a **hidden state** that summarizes what came before:

```
RNN processing "The cat sat":

h₀(empty) → [The] → h₁ → [cat] → h₂ → [sat] → h₃ → output
                ↑             ↑             ↑
              hidden state passed along
```

The hidden state is like the network's "memory" of what it's seen so far.

**Problem**: RNNs have trouble with long-range dependencies. In "The cat that lived in the old house with the red door sat on the mat", the word "sat" depends on "cat" — 15 words earlier. By the time the RNN processes "sat", the information about "cat" has been diluted.

### LSTMs — Better Memory

**Long Short-Term Memory (LSTM)** networks solve this with explicit memory gates:

- **Forget gate**: what to erase from memory
- **Input gate**: what new information to add
- **Output gate**: what to output from memory

LSTMs dominated NLP (natural language processing) from 2014 to 2017. Then the transformer arrived and changed everything.

---

## 6. Attention — Focus on What Matters

The key insight behind modern AI: when processing a word, which other words are relevant?

"The **animal** didn't cross the street because **it** was too tired."

What does "it" refer to? The animal. The word "animal" is most relevant when processing "it".

**Attention** lets the network focus on relevant parts of the input when producing each output:

```
Query: "what is 'it' related to?"
Keys:  [The, animal, didn't, cross, the, street, because, it, was, too, tired]
Values: [embedding vectors for each word]

Attention score = similarity between query and each key
                = softmax(Q × Kᵀ / √d)

Output for 'it' = weighted sum of values (weighted by attention scores)
                = mostly the 'animal' vector → the model knows 'it' = animal
```

This mechanism lets every token "look at" every other token in one step — much better than RNNs' sequential processing.

---

## 7. Transformers — The Architecture That Took Over

**Transformers** (introduced in "Attention Is All You Need", 2017) replaced RNNs almost entirely. They use attention mechanisms exclusively — no recurrence.

```
Input: "The cat sat on the mat"
Tokenize: [The, cat, sat, on, the, mat]
Embed:    [vectors in high-dimensional space]

Multi-Head Self-Attention:
  Each token attends to all other tokens simultaneously
  → capture relationships: "cat" ↔ "sat", "mat" ↔ "on"

Feed-Forward Network:
  Process each token independently

Stack 12–96 of these layers → deep transformer
```

### Why Transformers Won

| Feature       | RNN          | Transformer             |
|---------------|--------------|-------------------------|
| Parallelism   | Sequential   | All tokens at once      |
| Long-range    | Struggles    | Direct attention to any token |
| Training speed| Slow         | Fast (GPU-parallelizable)|
| Context       | ~100 tokens  | 100,000+ tokens         |

Transformers process all tokens in parallel → train much faster on GPUs. They can attend to any position directly → no degradation over long sequences.

---

## 8. Training in Practice

Modern deep learning training:

**Hardware**: NVIDIA GPUs or Google TPUs. Training GPT-4 used thousands of A100 GPUs for months.

**Batch training**: process many examples at once (batch size 32–4096). More efficient on GPU.

**Learning rate scheduling**: start with a high learning rate, reduce over time.

**Regularization techniques:**
- **Dropout**: randomly zero out neurons during training → prevents co-adaptation, reduces overfitting
- **Batch normalization**: normalize layer inputs → more stable training, faster convergence
- **Weight decay**: penalize large weights → simpler models

**Transfer learning**: start from a model pre-trained on a massive dataset, fine-tune for your task. Training from scratch costs millions of dollars. Fine-tuning costs thousands — or less.

---

## 9. What Deep Learning Is Good At

| Task                     | Dominant architecture |
|--------------------------|-----------------------|
| Image classification     | CNN or Vision Transformer |
| Object detection         | YOLO, DETR            |
| Speech recognition       | Transformer (Whisper) |
| Language translation     | Transformer           |
| Text generation          | GPT-style Transformer |
| Code generation          | Transformer           |
| Image generation         | Diffusion model       |
| Drug discovery           | Graph Neural Networks |

If you have lots of data, the right architecture, and GPU time, deep learning can solve problems that seemed impossible 10 years ago.

**What it's not good at:**
- Small datasets (classical ML wins)
- Interpretability (why did it predict this?)
- Reasoning (it pattern-matches, doesn't reason)
- Guarantees (it might be wrong with high confidence)

---

## Summary

```
Neuron:           weighted sum → activation function → output
Neural network:   layers of neurons; learns hierarchical features
Backpropagation:  chain rule → compute gradients → update weights

CNN:      filters slide over images → spatial feature detection
RNN/LSTM: process sequences with memory (largely replaced)
Attention: each token focuses on relevant parts of input

Transformer:
  → multi-head self-attention + feed-forward
  → processes all tokens in parallel
  → scales to huge data and huge models
  → now the dominant architecture for almost everything

Training:
  → huge datasets + GPUs + gradient descent
  → transfer learning: pre-train big, fine-tune specific
```

Deep learning is powerful but it's not magic. It's extremely good pattern recognition. The patterns are real — they generalize to new data. But the model doesn't understand the world the way you do. It finds correlations; it doesn't discover causes.

In the next post — the last in this series — we'll look at **Large Language Models**: how transformers trained on internet-scale text produce AI that can write, code, reason, and converse.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)
