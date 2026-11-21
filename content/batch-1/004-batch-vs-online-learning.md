# 004 — Batch / Offline vs Online Learning

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 004
- Transcript title: "Batch Machine Learning | Offline Vs Online Learning | Machine Learning Types"
- Transcript file: `004 - 2021-03-17 - Batch Machine Learning _ Offline Vs Online Learning _ Machine Learning Types.txt`
- Topic: training paradigms
- Subtopic: batch learning vs online learning

## Original CampusX concept

This lesson is about the training process itself. The transcript distinguishes between two major production patterns:

- Batch / offline learning: the model is trained on the whole dataset (or a large chunk of it), then deployed
- Online learning: the model is updated incrementally as new data arrives

This is a conceptual distinction about how learning happens over time, not about whether the model is supervised or unsupervised.

### Beginner intuition

Batch learning is like preparing for an exam using a full set of notes at once. Online learning is like learning as new information arrives during the semester.

### Technical understanding

In batch learning:

- you collect a dataset
- train the model on it
- deploy it
- retrain later on a scheduled basis

In online learning:

- the model starts with some initial data
- new data arrives continuously
- the model updates itself as each batch or example comes in

This is why the instructor connects the idea to production systems: the real world changes, and a fixed model may become outdated.

## IMPORTANT DISTINCTION: How 004 relates to 005

Lesson 004 defines the broad concept of training mode. It answers the question:

- Should the model train once on a large batch, or should it keep adapting?

Lesson 005 then goes deeper into the operational mechanics of online learning: streaming data, improvement on the fly, and concept drift.

So, 004 is the high-level decision, and 005 is the detailed implementation story.

## SUPPLEMENTARY: Why retraining matters

A model trained once can become stale. If user behavior or market patterns shift, then predictions drift away from reality.

This is exactly why companies often retrain models periodically or use online updates.

## INTERVIEW EXTENSION

Q: What is the difference between batch learning and online learning?

A: Batch learning trains on a full dataset in one go; online learning updates continuously with new data.

Q: When is batch learning preferred?

A: When the data does not change fast and retraining is enough.

Q: When is online learning more useful?

A: When the environment changes continuously and the model must adapt quickly.

## Practical Python example

```python
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=1000, n_features=5, noise=10, random_state=42)
model = SGDRegressor(loss='squared_error', learning_rate='constant', eta0=0.01, random_state=42)

# Simulate incremental updates using small chunks of data
for i in range(10):
    start = i * 100
    end = (i + 1) * 100
    model.partial_fit(X[start:end], y[start:end])

print(round(model.score(X, y), 3))
```

Expected output (approximate):

```text
0.94
```

### Why this matters

This demonstrates the core difference: online learning does not require a full retrain from scratch for every new data block.

## COMMON MISTAKES AND MISCONCEPTIONS

- Assuming a model stays accurate forever after one training run
- Believing online learning is always better than batch learning
- Ignoring that many real systems use periodic retraining instead of full streaming updates

## Practice

1. Explain batch learning in plain English.
2. Explain online learning in plain English.
3. Name one production scenario where online learning is better than batch learning.
4. Why do models become stale over time?

## Code-to-practice mapping

- Original concept: training mode difference between offline and online learning
- Supplementary concept: deployment and retraining strategy
- Code: incremental training with SGDRegressor
- Practice: deciding when adaptation is needed
