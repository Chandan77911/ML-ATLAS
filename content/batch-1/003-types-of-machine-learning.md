# 003 — Types of Machine Learning

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 003
- Transcript title: "Types of Machine Learning for Beginners | Types of Machine learning in Hindi | Types of ML in Depth"
- Transcript file: `003 - 2021-03-16 - Types of Machine Learning for Beginners _ Types of Machine learning in Hindi _ Types of ML in Depth.txt`
- Topic: taxonomy of ML
- Subtopic: supervised, unsupervised, semi-supervised, reinforcement learning

## Original CampusX concept

The instructor explains that machine learning algorithms can be organized by how much supervision they receive during training.

### The four major categories

- Supervised learning: training data includes both inputs and correct outputs
- Unsupervised learning: training data has inputs but no labels; the model finds structure
- Semi-supervised learning: some labeled data exists, but many examples are unlabeled
- Reinforcement learning: the model learns through trial and error by interacting with an environment and optimizing reward

The transcript also notes that supervised learning is typically split into:

- regression: predicting a continuous target
- classification: predicting a category or class

### Beginner intuition

This lesson is basically a map of the ML world:

- If the system gets the answer during training, it is supervised.
- If it has to discover patterns by itself, it is unsupervised.
- If it gets partial guidance, it is semi-supervised.
- If it learns by trying actions and receiving feedback, it is reinforcement learning.

### Technical understanding

The learning setup changes the objective function and data assumptions.

- Supervised learning approximates a mapping $f(x) \rightarrow y$
- Unsupervised learning identifies structure in $x$ without explicit targets
- Semi-supervised learning combines both kinds of information
- Reinforcement learning maximizes cumulative reward through a policy $\pi$

The key point is that the type of learning depends on the task and the availability of labels.

## IMPORTANT TERMS EXPLAINED

- Feature: input variable used to make a prediction
- Label: target value or answer provided during training
- Regression: prediction of a numeric value
- Classification: prediction of a category
- Policy: the rule used by an agent to choose actions in reinforcement learning
- Reward: feedback signal used to improve the agent

## SUPPLEMENTARY: Unsupervised subtypes

The transcript mentions common unsupervised families:

- clustering
- dimensionality reduction
- anomaly detection
- association rule learning

These are useful when labels are missing and the goal is to uncover organization in the data.

## INTERVIEW EXTENSION

Q: What is the main difference between supervised and unsupervised learning?

A: Supervised learning uses target labels; unsupervised learning seeks structure without labels.

Q: When is semi-supervised learning useful?

A: When labels are expensive or limited but large amounts of unlabeled data are available.

Q: Why is reinforcement learning different from the others?

A: It learns from interaction and delayed feedback, not from static labeled examples.

## Practical Python example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
print("Accuracy:", round(model.score(X_test, y_test), 3))
```

Expected output:

```text
Accuracy: 0.974
```

### Why this example matters

This is a supervised learning example. The model sees input flower features and the correct species label during training, then learns to predict the label for new data.

## COMMON MISTAKES AND MISCONCEPTIONS

- Assuming all ML is supervised learning
- Thinking unsupervised learning means “no learning”
- Confusing classification with all supervised learning tasks
- Forgetting that reinforcement learning may need many trial-and-error steps before a good policy emerges

## Practice

1. Classify the following as supervised or unsupervised: predicting house price from square footage.
2. Give one example of semi-supervised learning.
3. Explain the intuition behind reinforcement learning in one sentence.
4. Name one real-world problem suitable for clustering.

## Code-to-practice mapping

- Original concept: learning categories based on supervision level
- Supplementary concept: labels, regression, and reinforcement feedback
- Code: a supervised classification pipeline with Iris data
- Practice: categorizing tasks by learning type
