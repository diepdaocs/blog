---
layout: single
title: "Machine Learning: Teaching Computers to Learn"
date: 2026-01-12 10:00:00 +0800
permalink: /computer-science/2026/03/29/machine-learning/
categories:
  - computer-science
tags:
  - machine-learning
  - gradient-descent
  - decision-trees
  - supervised-learning
  - classification
  - regression
---

This is Post 10 in the [Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/). The [previous post](/computer-science/2026/03/28/distributed-systems/) covered distributed systems. Now we look at **machine learning** — the technology behind spam filters, face recognition, music recommendations, and medical diagnosis.

Traditional programming: you write rules, the computer follows them.
Machine learning: you show the computer examples, and it figures out the rules itself.

This shift sounds simple but it's profound. Writing rules for "is this email spam?" is hard and brittle. Showing the computer millions of spam and non-spam emails and letting it learn the pattern — that works remarkably well.

---

<img src="/assets/images/arch-machine-learning.svg" alt="Machine Learning Overview" style="width:100%;max-width:860px;margin:1.5rem auto;display:block;border-radius:8px;">

## The Big Picture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                      Machine Learning Landscape                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Supervised Learning          Unsupervised Learning      Reinforcement       ║
║  (labeled examples)           (no labels, find patterns) (reward signal)     ║
║  ──────────────────────       ────────────────────────   ─────────────────   ║
║  Classification               Clustering                 Game playing        ║
║   spam detection              k-means, DBSCAN            robot control       ║
║   image recognition                                                          ║
║                               Dimensionality reduction   Self-driving cars   ║
║  Regression                   PCA, t-SNE                                     ║
║   house price prediction                                                     ║
║   stock price forecasting     Anomaly detection                              ║
║                               fraud, failures                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Key Algorithms                                                              ║
║  Linear Regression · Logistic Regression · Decision Trees                    ║
║  Random Forests · Gradient Boosting (XGBoost) · SVM                          ║
║  k-NN · Naive Bayes · k-Means · PCA                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. The Core Idea: Learning from Examples

Consider teaching a child to recognise cats. You don't write rules like "if has four legs AND has whiskers AND meows → cat". Instead, you show thousands of pictures and say "cat" or "not cat" until the child builds an internal model.

Machine learning does the same:

```
Training data:
  Photo 1 → cat ✓
  Photo 2 → not cat ✗
  Photo 3 → cat ✓
  ... (millions of examples)

Model learns patterns: pointy ears, whiskers, fur texture...

New photo → Model predicts: cat (91% confident)
```

The model is not programmed with cat rules. It **learned** them from data.

### Features

Every example is described by **features** — measurable properties.

| Email      | has_link | CAPS_ratio | word_free | word_winner | → Spam? |
|------------|----------|------------|-----------|-------------|---------|
| Email 1    | Yes      | 0.3        | Yes       | Yes         | Yes     |
| Email 2    | No       | 0.01       | No        | No          | No      |
| Email 3    | Yes      | 0.5        | Yes       | No          | Yes     |

Feature engineering — choosing which features to include — is often as important as choosing the algorithm.

---

## 2. Supervised Learning — Learning from Labeled Data

In supervised learning, every training example comes with the correct answer (label).

**Classification**: predict a category
- Is this email spam or not? (2 classes)
- What digit is this handwriting? (10 classes: 0–9)
- What species is this bird? (thousands of classes)

**Regression**: predict a number
- What will this house sell for?
- How many hours until this machine fails?

### Training and Evaluation

```
All data (100,000 examples)
  ├── Training set (80,000) → model learns from these
  ├── Validation set (10,000) → tune hyperparameters
  └── Test set (10,000) → final evaluation (never seen during training)
```

The test set simulates real-world performance. **Never train on test data** — that would give overly optimistic results (like memorising exam answers).

### Overfitting vs Underfitting

```
Underfitting:  model too simple → misses patterns → poor on training AND test
Overfitting:   model too complex → memorises training data → great on training, poor on test
Just right:    generalizes well → good on both
```

A model that memorizes your training data is useless — it can't generalize to new examples. Techniques to prevent overfitting: more data, simpler models, regularization, dropout (in neural networks).

---

## 3. Linear Regression — The Simplest Model

Predict a number from features by fitting a line (or plane in higher dimensions).

```
House price = 200 × (square_meters) + 50,000 × (bedrooms) + 30,000

Training: find the values (200, 50,000, 30,000) that best fit the data
Predict:  new house → plug in features → get price estimate
```

The model is just: `y = w₁x₁ + w₂x₂ + ... + b`

**w** values are **weights** (how much each feature matters). **b** is the **bias** (baseline value). Training finds the w and b values that minimize the error on training data.

---

## 4. Gradient Descent — How Models Learn

How do we find the right weights? **Gradient descent** — move in the direction that reduces error.

Imagine you're lost in mountains in fog, and you want to reach the lowest valley. You can't see far, but you can feel the ground slope. The strategy: **always step downhill**. Eventually you reach a valley.

```
Error (loss function) = how wrong the model's predictions are
Gradient = direction of steepest increase in error
Step = move opposite to gradient (downhill = less error)

Repeat:
  1. Make predictions with current weights
  2. Calculate error (e.g., mean squared error)
  3. Calculate gradient of error w.r.t. weights
  4. Update: weights = weights - learning_rate × gradient
  5. Repeat until error stops decreasing
```

The **learning rate** controls step size. Too large: you overshoot and bounce around. Too small: takes forever to converge.

```python
# Simplified gradient descent for linear regression
for epoch in range(1000):
    predictions = X @ weights + bias
    error = predictions - y_true

    # gradients
    dW = (2/n) * X.T @ error
    db = (2/n) * sum(error)

    # update
    weights -= learning_rate * dW
    bias    -= learning_rate * db
```

Gradient descent is the core of training almost every ML model, from linear regression to massive language models.

---

## 5. Decision Trees — Transparent Decisions

A **decision tree** splits data based on feature values, like a flowchart.

```
Is income > $50,000?
├── Yes → Is credit_score > 700?
│          ├── Yes → APPROVE loan
│          └── No  → Is employment_years > 3?
│                    ├── Yes → APPROVE
│                    └── No  → REJECT
└── No  → REJECT
```

Trees are:
- **Interpretable**: you can explain every decision
- **No feature scaling needed**: trees don't care about units
- **Handle mixed data**: numbers and categories in the same model

A single tree tends to overfit. The fix: use many trees together.

### Random Forest

Build 100 decision trees, each on a random subset of training data and features. For prediction, take the majority vote.

```
100 trees each make a prediction:
  63 trees say: SPAM
  37 trees say: NOT SPAM
  → Final: SPAM (majority wins)
```

Random forests are more accurate and much more robust than single trees. They're among the most reliable "out of the box" algorithms.

### Gradient Boosting (XGBoost, LightGBM)

Build trees sequentially. Each new tree corrects the errors of all previous trees.

```
Tree 1: makes predictions, has some errors
Tree 2: trained on the residual errors of Tree 1
Tree 3: trained on the residual errors of Trees 1+2
... (100-1000 trees)
Final prediction = sum of all trees' predictions
```

Gradient boosting is the top algorithm for structured/tabular data competitions. XGBoost and LightGBM have won hundreds of Kaggle competitions.

---

## 6. Support Vector Machines (SVM)

SVMs find the **maximum-margin hyperplane** — the decision boundary that's as far as possible from both classes.

```
Class A points: o o o
Class B points: x x x

Bad boundary: x x | o o o  (close to class A)
Good boundary: x x   | o o o (equal margin on both sides)

The points closest to the boundary are called "support vectors"
```

SVMs with the **kernel trick** can draw non-linear boundaries (circles, curves) by implicitly mapping data to higher dimensions.

Good for: text classification, image classification (before deep learning), when data is small and features are well-engineered.

---

## 7. Unsupervised Learning — Finding Hidden Patterns

What if you don't have labels? Unsupervised learning finds structure in unlabeled data.

### k-Means Clustering

Group data into k clusters, where each point belongs to the cluster with the nearest center.

```
Start: randomly place k cluster centers
Repeat:
  1. Assign each point to nearest center
  2. Move each center to the average of its assigned points
Until centers stop moving

Result: k groups of similar points
```

Uses: customer segmentation (group customers by behaviour), compressing images (group similar colours), finding communities in social networks.

### Principal Component Analysis (PCA)

Reduce many features to a few by finding the directions of maximum variance.

```
10,000 features → 2 features that capture most of the information
```

Used for: visualizing high-dimensional data, reducing computation, removing noise.

---

## 8. Evaluation Metrics

How do you measure if a model is good?

### For Classification

**Accuracy**: fraction of predictions that are correct.
```
accuracy = correct predictions / total predictions
```

Accuracy is misleading for imbalanced datasets: if 99% of emails are not spam, a model that always says "not spam" has 99% accuracy but is useless.

Better metrics:

**Precision**: of everything I predicted as spam, what fraction was actually spam?
**Recall**: of all actual spam emails, what fraction did I catch?

```
Precision = True Positives / (True Positives + False Positives)
Recall    = True Positives / (True Positives + False Negatives)
```

There's a trade-off: higher recall (catch more spam) → more false positives (legitimate email marked spam). You tune based on what matters for your use case.

**F1 Score**: harmonic mean of precision and recall — single number that balances both.

### For Regression

**MAE (Mean Absolute Error)**: average absolute difference between predicted and actual.
**RMSE (Root Mean Squared Error)**: like MAE but penalises large errors more.

---

## 9. Classical ML vs Deep Learning

| Aspect              | Classical ML              | Deep Learning                    |
|---------------------|---------------------------|----------------------------------|
| Data required       | Hundreds–thousands         | Tens of thousands–millions       |
| Feature engineering | Required (you choose)     | Learned automatically            |
| Interpretability    | Often interpretable       | Usually a black box              |
| Training time       | Seconds–minutes           | Hours–weeks (on GPUs)            |
| Best for            | Tabular/structured data   | Images, audio, text, video       |

Classical ML (random forests, XGBoost) still dominates for tabular/structured data (the kind in databases). Deep learning dominates for images, audio, and text — where features are hard to engineer by hand.

---

## Summary

Machine learning is pattern recognition at scale:

```
Supervised:    labeled examples → model → predictions on new data
Classification: predict categories (spam/not, cat/dog)
Regression:    predict numbers (price, temperature, time)

Core technique: gradient descent → minimize prediction error
Key algorithms: linear regression, decision trees, random forests, XGBoost

Pitfalls:
  Overfitting → model memorizes, doesn't generalize
  Data leakage → test data accidentally seen during training
  Wrong metric → accuracy on imbalanced data is misleading
```

ML doesn't magically create knowledge. It finds patterns in the data you give it. Bad data → bad patterns. Biased data → biased models. The data is always the foundation.

In the next post, we'll go deeper: **Deep Learning** — neural networks, convolutional networks, and the transformer architecture that powers modern AI.

Back to the series: [Welcome to the Computer Science Series](/computer-science/2026/02/27/welcome-to-computer-science/)
