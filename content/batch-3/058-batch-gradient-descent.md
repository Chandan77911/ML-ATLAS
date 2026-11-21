# 058 — Batch Gradient Descent

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 058
- Transcript title: "Batch Gradient Descent with Code Demo _ Simple Explanation in Hindi"
- Transcript file: `058 - 2021-05-22 - Batch Gradient Descent with Code Demo _ Simple Explanation in Hindi.txt`
- Topic: gradient descent using the full dataset per update

## Learning objectives
- Explain what batch gradient descent is.
- Understand why it uses the whole dataset at each step.
- Learn the benefits and trade-offs of this approach.
- Connect it to the gradient descent equations.

## Definition
Batch gradient descent computes the gradient using the entire training dataset before updating the parameters.

This means each parameter update uses all samples in the loss function.

## Update rule
$$
\theta := \theta - \eta \frac{1}{n} \sum_{i=1}^{n} \nabla L(\theta; x_i, y_i)
$$

This is the full-batch version of gradient descent.

## Pros
- deterministic updates
- stable convergence for convex problems
- easy to reason about mathematically

## Cons
- computationally expensive on large data
- slower per update than stochastic methods
- may be impractical for extremely large datasets

## Python example
```python
import numpy as np

X = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2, 4, 6, 8], dtype=float)

w = 0.0
b = 0.0
lr = 0.01
n = len(X)

for _ in range(1000):
    y_pred = w * X + b
    loss = np.mean((y_pred - y) ** 2)
    dw = (2 / n) * np.sum(X * (y_pred - y))
    db = (2 / n) * np.sum(y_pred - y)
    w -= lr * dw
    b -= lr * db

print('w =', w)
print('b =', b)
print('loss =', loss)
```

## Key takeaways
- Batch gradient descent is stable and simple.
- It is often the baseline method teachers use to explain optimization.
- For very large datasets, stochastic or mini-batch variants are typically more practical.

## Practice questions
1. What is the difference between batch gradient descent and stochastic gradient descent?
2. Why is batch gradient descent stable?
3. What is a downside of using the full dataset per step?
4. How does the learning rate affect the update size?

## Source reference
- Transcript title: "Batch Gradient Descent with Code Demo _ Simple Explanation in Hindi"
- File: `058 - 2021-05-22 - Batch Gradient Descent with Code Demo _ Simple Explanation in Hindi.txt`
