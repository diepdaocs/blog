---
layout: single
title: "How Andrew Ng's Courses Changed the Way I Think About AI"
date: 2026-02-27 10:00:00 +0800
categories:
  - ai
tags:
  - machine-learning
  - deep-learning
  - andrew-ng
  - coursera
  - deeplearning-ai
  - learning
---

If there's one person whose teaching shaped my understanding of AI more than anyone else, it's Andrew Ng. This post is about that journey — from watching his original Machine Learning lectures to working through the Deep Learning Specialization and eventually the short courses on deeplearning.ai.

## Where It Started — The Machine Learning Course

When I first encountered machine learning seriously, I was a data engineer at Sentifi, building ETL pipelines and streaming systems. I understood data, I understood code, but I didn't really understand *learning from data*. A colleague recommended Andrew Ng's Machine Learning course on Coursera, and I decided to give it a go.

I wasn't prepared for how good it was.

The course starts from first principles — linear algebra, probability, gradient descent — and builds up to SVMs, neural networks, and clustering in a way that feels inevitable rather than arbitrary. What set it apart wasn't just the content, but the way Ng explains *why* things work. Not just "here's the formula" but "here's the intuition, here's what goes wrong, here's how to fix it."

The programming assignments were in MATLAB/Octave at the time, which felt a little dated, but the concepts were timeless. By the end I had implemented gradient descent, regularisation, a neural network from scratch, and an anomaly detection system. More importantly, I had a mental model of machine learning that I still use every day.

**Key takeaway:** Understanding the mathematics behind the algorithms — even roughly — makes you a far better practitioner. You stop treating models as black boxes and start reasoning about why they fail.

## The Deep Learning Specialization

A few years later, when deep learning was becoming unavoidable in NLP, I went back to Coursera for the Deep Learning Specialization — five courses co-created by Andrew Ng through deeplearning.ai.

The specialization covers:

1. **Neural Networks and Deep Learning** — backpropagation, activation functions, initialisation
2. **Improving Deep Neural Networks** — regularisation, optimisation (Adam, RMSProp), batch norm, hyperparameter tuning
3. **Structuring Machine Learning Projects** — arguably the most underrated course; how to actually run ML projects, diagnose bias/variance, and prioritise improvements
4. **Convolutional Neural Networks** — CNNs, object detection, face recognition
5. **Sequence Models** — RNNs, LSTMs, GRUs, and an introduction to attention mechanisms

The standout for me was **Course 3 — Structuring ML Projects**. It's not glamorous, but it tackles the questions that actually matter when you're working on real problems: Is your model underfitting or overfitting? Should you collect more data or tune the model? How do you set up train/dev/test splits correctly? I've applied those frameworks on every ML project since.

The LSTM and sequence modelling content in Course 5 came at exactly the right time. I was about to start working on NLP models at Refinitiv, and the foundations I built here directly informed the work I did building LSTM-based models for financial news tagging — including the first deep learning model we deployed to production.

**Key takeaway:** Course 3 is worth the price of the entire specialization. Learning to *diagnose* ML problems is more valuable than knowing more algorithms.

## Short Courses on deeplearning.ai

More recently, deeplearning.ai has launched a series of short courses — typically 1 to 2 hours — on practical, current topics. These are a different format from the specializations: less mathematical rigour, more hands-on with real tools and APIs.

Some that I found genuinely useful:

- **ChatGPT Prompt Engineering for Developers** — a solid introduction to prompt design, covering zero-shot, few-shot, chain-of-thought, and how to structure prompts for reliable outputs
- **LangChain for LLM Application Development** — building applications on top of LLMs using chains, agents, and memory
- **Building Systems with the ChatGPT API** — how to structure multi-step LLM pipelines for production use cases

These short courses are best thought of as accelerated onboarding to new tools rather than deep education. They get you productive quickly, but you'll still need to go deeper on your own. That said, for keeping up with a fast-moving field, they're excellent.

## What I'd Tell Someone Starting Today

1. **Start with the Machine Learning course** (now updated to use Python and TensorFlow). The fundamentals haven't changed, and they matter.
2. **Do the Deep Learning Specialization** if you're serious about working in AI. Don't skip Course 3.
3. **Pick short courses on deeplearning.ai selectively** based on what you're actively working on — they're most useful when you have an immediate application in mind.
4. **Build something**. The courses give you the tools, but real understanding comes from applying them to a problem you actually care about.

Andrew Ng's courses gave me the confidence to move from data engineering into machine learning, and eventually into senior NLP roles building production AI systems. That's not a small thing. If you're on the fence about starting — don't be.
