# 97 — Decision Trees

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 97
- Transcript title: "Decision Trees Geometric Intuition _ Entropy _ Gini impurity _ Information Gain"
- Transcript file: `097 - 2021-07-02 - Decision Trees Geometric Intuition _ Entropy _ Gini impurity _ Information Gain.txt`
- Topic: Decision trees and entropy

## Learning objectives
- Explain the main idea behind decision trees.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Decision trees split the dataset based on feature tests that reduce impurity and improve class separation.

## Why this matters
Decision trees partition the data using a sequence of feature-based questions. The goal is to form subsets that are as pure as possible, meaning they contain mostly one class or a narrow range of target values.

## Intuition
A decision tree asks a question like “Is feature $x_1 > 5$?” and then continues down the branch that matches the answer. Each split reduces impurity, making the later leaves more informative.

## Mathematical view
A common impurity measure is entropy:

$$
H(S) = -\sum_{c=1}^{C} p_c \log_2(p_c)
$$

Another is Gini impurity:

$$
Gini(S) = 1 - \sum_{c=1}^{C} p_c^2
$$

A split is chosen to minimize the weighted impurity after the split. This is where the idea of information gain comes from.

## Python example
```python
from collections import Counter

labels = ['yes', 'yes', 'no', 'no', 'yes']
counts = Counter(labels)
probs = [count / len(labels) for count in counts.values()]
entropy = -sum(p * __import__('math').log2(p) for p in probs)

print('Label counts:', dict(counts))
print('Entropy:', round(entropy, 3))
```

Expected output:
```text
Label counts: {'yes': 3, 'no': 2}
Entropy: 0.971
```

## Advantages
- Easy to visualize and explain
- Handles both classification and regression tasks
- Captures nonlinear decision boundaries without a black-box transformation

## Limitations
- Prone to overfitting if the tree grows too deep
- Can be unstable with small changes in the training data
- Feature splits can be biased toward high-cardinality variables

## Common mistakes
- Growing trees without limiting depth or leaf size
- Ignoring purity measures when selecting splits
- Treating the tree as globally optimal instead of greedily built

## Revision questions
1. What is the purpose of a split in a decision tree?
2. Why is entropy or Gini impurity useful?
3. How does a decision tree make a prediction?
4. Why can overfitting become a problem?

## Source reference
- Transcript title: "Decision Trees Geometric Intuition _ Entropy _ Gini impurity _ Information Gain"
- File: `097 - 2021-07-02 - Decision Trees Geometric Intuition _ Entropy _ Gini impurity _ Information Gain.txt`
