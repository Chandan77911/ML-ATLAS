# 059 — Stochastic Gradient Descent

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 059
- Transcript title: "Stochastic Gradient Descent"
- Transcript file: `059 - 2021-05-25 - Stochastic Gradient Descent.txt`
- Topic: online parameter updates using one sample at a time

## Learning objectives
- Define stochastic gradient descent.
- Compare it to batch gradient descent.
- Understand why it is faster for large datasets.
- Recognize the trade-offs in stability and convergence.

## Definition
In stochastic gradient descent (SGD), the model updates parameters using one training example at a time.

$$
\theta := \theta - \eta \nabla L(\theta; x_i, y_i)
$$

This is different from computing the full-batch average gradient across all examples.

## Intuition
Instead of waiting for all samples to be processed, the algorithm updates immediately after seeing each sample. This makes learning faster in large datasets.

## Pros
- much faster on large datasets
- can escape shallow local minima more easily in some settings
- efficient when data arrives in streaming or online settings

## Cons
- noisier updates
- may oscillate around the optimum
- requires careful tuning of learning rate and schedule

## Python example
```python
import numpy as np

X = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2, 4, 6, 8], dtype=float)

w = 0.0
b = 0.0
lr = 0.01

for i in range(len(X)):
    pred = w * X[i] + b
    err = y[i] - pred
    w += lr * 2 * X[i] * err
    b += lr * 2 * err

print('w =', w)
print('b =', b)
```

## Key takeaways
- SGD uses one sample at a time.
- It is more scalable but less stable than batch gradient descent.
- In practice, mini-batch and adaptive optimizers are often preferred in modern ML.

## Practice questions
1. How does SGD differ from batch gradient descent?
2. Why is SGD useful for large-scale learning?
3. What is the cost of noisy updates?
4. Why might a learning-rate schedule be important?

## Source reference
- Transcript title: "Stochastic Gradient Descent"
- File: `059 - 2021-05-25 - Stochastic Gradient Descent.txt`
