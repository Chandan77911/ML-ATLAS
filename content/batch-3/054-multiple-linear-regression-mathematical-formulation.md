# 054 — Multiple Linear Regression: Mathematical Formulation

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 054
- Transcript title: "Multiple Linear Regression _ Part 2 _ Mathematical Formulation From Scratch"
- Transcript file: `054 - 2021-05-15 - Multiple Linear Regression _ Part 2 _ Mathematical Formulation From Scratch.txt`
- Topic: least-squares solution for multiple-feature regression

## Learning objectives
- Represent multiple regression in matrix form.
- Explain the least-squares objective in vector notation.
- Derive the normal equation for multiple regression.
- Link the matrix form to the practical coefficient calculation.

## Model in matrix form
For $n$ samples and $p$ features:

$$
Y = X\beta + \epsilon
$$

where:
- $Y$ is an $n \times 1$ target vector
- $X$ is an $n \times p$ design matrix
- $\beta$ is a $p \times 1$ coefficient vector
- $\epsilon$ is the error vector

## Objective
We minimize the squared residual sum:

$$
\sum_{i=1}^{n} e_i^2 = (Y - X\beta)^T(Y - X\beta)
$$

The optimal coefficients satisfy:

$$
\beta = (X^T X)^{-1} X^T Y
$$

provided $X^T X$ is invertible.

## Interpretation
This is the extension of the scalar formula from simple regression to the full multivariate case. The model finds the coefficients that minimize residual squared error across all samples simultaneously.

## Practical notes
In real data, we often use:
- regularization
- numerical solvers
- standardization
- stability checks for singular matrices

## Python example
```python
import numpy as np

X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4]
], dtype=float)

y = np.array([2, 3, 5, 8], dtype=float)

beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
print('beta:', beta)
```

Expected output:
```text
beta: [0.5 1.5]
```

## Common mistakes
- trying to invert a matrix that is singular or nearly singular
- ignoring the intercept term in the design matrix
- mixing up the feature matrix dimension and the coefficient vector

## Key takeaways
- Matrix notation makes multiple regression compact and scalable.
- The least-squares solution is central to the method.
- The same principle from simple regression extends naturally to multiple inputs.

## Practice questions
1. What is the matrix form of multiple regression?
2. Why do we minimize $(Y - X\beta)^T(Y - X\beta)$?
3. What does the normal equation solve for?
4. Why is invertibility of $X^T X$ important?

## Source reference
- Transcript title: "Multiple Linear Regression _ Part 2 _ Mathematical Formulation From Scratch"
- File: `054 - 2021-05-15 - Multiple Linear Regression _ Part 2 _ Mathematical Formulation From Scratch.txt`
