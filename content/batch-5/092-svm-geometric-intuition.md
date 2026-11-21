# 92 — Support Vector Machines

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 92
- Transcript title: "Support Vector Machines _ Geometric Intuition"
- Transcript file: `092 - 2020-07-10 - Support Vector Machines _ Geometric Intuition.txt`
- Topic: SVM geometric intuition

## Learning objectives
- Explain the main idea behind support vector machines.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
SVM finds a decision boundary that maximizes the margin between classes, leading to robust separation.

## Why this matters
SVM is built around the idea of a large margin: it finds the decision boundary that separates the classes with the maximum possible distance to the nearest training points.

## Intuition
In a two-class problem, imagine drawing a line that separates the red points from the blue points. SVM picks the line that leaves the largest buffer around it, making the model less sensitive to noise and more robust on unseen data.

## Mathematical view
For a binary classifier, the decision function is:

$$
 f(x) = w^T x + b
$$

The optimal boundary maximizes the margin $\frac{2}{\|w\|}$ subject to:

$$
 y_i(w^T x_i + b) \geq 1 \quad \text{for all } i
$$

This means every point must be classified correctly and safely away from the decision boundary. The support vectors are the points closest to the margin boundary.

## Python example
```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

X, y = make_blobs(n_samples=200, centers=2, cluster_std=1.0, random_state=0)
model = SVC(kernel='linear', C=1.0)
model.fit(X, y)

print('Support vector count:', len(model.support_vectors_))
print('Decision function shape:', model.decision_function(X[:3]).shape)
```

Expected output:
```text
Support vector count: 2
Decision function shape: (3,)
```

## Advantages
- Strong geometric intuition and clear margin-based interpretation
- Good generalization, especially in high-dimensional spaces
- Robust to some forms of noisy data when margins are large

## Limitations
- Sensitive to scaling and kernel choice
- Can struggle with very large datasets or overlapping classes
- Hard-margin formulations can fail to separate noisy data perfectly

## Common mistakes
- Ignoring feature scaling before fitting SVM
- Forgetting that support vectors define the boundary
- Assuming a large margin always means the model is better without validation

## Revision questions
1. What is a margin in SVM?
2. Why do support vectors matter?
3. How does SVM differ from a simple line-fitting classifier?
4. Why does maximizing the margin improve generalization?

## Source reference
- Transcript title: "Support Vector Machines _ Geometric Intuition"
- File: `092 - 2020-07-10 - Support Vector Machines _ Geometric Intuition.txt`
