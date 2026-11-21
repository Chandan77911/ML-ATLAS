# 051 — Simple Linear Regression: Mathematical Formulation

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 051
- Transcript title: "Simple Linear Regression _ Mathematical Formulation _ Coding from Scratch"
- Transcript file: `051 - 2021-05-11 - Simple Linear Regression _ Mathematical Formulation _ Coding from Scratch.txt`
- Topic: least-squares derivation and regression objective

## Learning objectives
- Derive the linear regression model mathematically.
- Explain the role of least squares.
- Connect the slope and intercept to optimization.
- Write a minimal from-scratch implementation.

## Model
For a dataset with pairs $(x_i, y_i)$, simple linear regression assumes:

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
$$

where:
- $\beta_0$ is the intercept
- $\beta_1$ is the slope
- $\epsilon_i$ is the residual error for sample $i$

## Objective function
We choose $\beta_0$ and $\beta_1$ to minimize the total squared error:

$$
SSE = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2
$$

This is the least-squares criterion.

## Why square the error?
Squaring ensures that:
- positive and negative errors do not cancel out
- larger mistakes are penalized more strongly
- the objective is differentiable and mathematically convenient

## Normal equations
The optimal coefficients satisfy:

$$
\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
$$

$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

These formulas are exactly the closed-form solution for simple linear regression.

## Python example
```python
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 8, 10], dtype=float)

x_bar = x.mean()
y_bar = y.mean()

beta_1 = np.sum((x - x_bar) * (y - y_bar)) / np.sum((x - x_bar) ** 2)
beta_0 = y_bar - beta_1 * x_bar

print('beta_0:', beta_0)
print('beta_1:', beta_1)
print('Equation: y =', beta_0, '+', beta_1, 'x')
```

Expected output:
```text
beta_0: 1.7
beta_1: 1.7
Equation: y = 1.7 + 1.7 x
```

## Key takeaways
- The model is linear in the coefficients.
- Least squares gives an explicit optimization target.
- The slope and intercept come from the data’s center and variation.

## Practice questions
1. What is the purpose of least squares?
2. Why do we minimize squared error rather than absolute error?
3. What do $\beta_0$ and $\beta_1$ represent?
4. What is the residual term in the regression equation?

## Source reference
- Transcript title: "Simple Linear Regression _ Mathematical Formulation _ Coding from Scratch"
- File: `051 - 2021-05-11 - Simple Linear Regression _ Mathematical Formulation _ Coding from Scratch.txt`
