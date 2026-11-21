# 057 — Gradient Descent from Scratch

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 057
- Transcript title: "Gradient Descent From Scratch _ End to End Gradient Descent _ Gradient Descent Animation"
- Transcript file: `057 - 2021-05-21 - Gradient Descent From Scratch _ End to End Gradient Descent _ Gradient Descent Animation.txt`
- Topic: optimization method for minimizing a loss function

## Learning objectives
- Explain the intuition behind gradient descent.
- Learn the update rule for model parameters.
- See how the gradient tells the algorithm in which direction to move.
- Implement gradient descent from scratch.

## Intuition
Gradient descent is an optimization algorithm. It adjusts parameters step by step so that the loss function decreases.

If we imagine a mountain, the gradient tells us the steepest upward direction. To minimize the loss, we move in the opposite direction.

## Gradient descent update rule
For parameter $\theta$:

$$
\theta_{new} = \theta_{old} - \eta \nabla J(\theta)
$$

where:
- $\eta$ is the learning rate
- $J(\theta)$ is the loss function
- $\nabla J(\theta)$ is the gradient

## Example with linear regression
For a simple model:

$$
\hat{y} = wx + b
$$

the loss is often the mean squared error:

$$
J(w, b) = \frac{1}{n} \sum (y_i - (wx_i + b))^2
$$

The partial derivatives are:

$$
\frac{\partial J}{\partial w} = -\frac{2}{n} \sum x_i(y_i - \hat{y}_i)
$$

$$
\frac{\partial J}{\partial b} = -\frac{2}{n} \sum (y_i - \hat{y}_i)
$$

## Python example
```python
import numpy as np

X = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2, 4, 6, 8], dtype=float)

w = 0.0
b = 0.0
learning_rate = 0.01
n = len(X)

for _ in range(1000):
    y_pred = w * X + b
    dw = -(2/n) * np.sum(X * (y - y_pred))
    db = -(2/n) * np.sum(y - y_pred)
    w -= learning_rate * dw
    b -= learning_rate * db

print('Final w:', w)
print('Final b:', b)
```

Expected output (approximate):
```text
Final w: 1.999
Final b: 0.001
```

## Common mistakes
- choosing a learning rate that is too large or too small
- stopping too early before convergence
- forgetting that gradients depend on the chosen loss function

## Key takeaways
- Gradient descent is the core optimization tool in machine learning.
- It iteratively reduces the loss by moving in the negative gradient direction.
- The learning rate controls how large each update is.

## Practice questions
1. What is the purpose of gradient descent?
2. What does the learning rate control?
3. Why do we move in the negative gradient direction?
4. How does the loss function affect the gradients?

## Source reference
- Transcript title: "Gradient Descent From Scratch _ End to End Gradient Descent _ Gradient Descent Animation"
- File: `057 - 2021-05-21 - Gradient Descent From Scratch _ End to End Gradient Descent _ Gradient Descent Animation.txt`
