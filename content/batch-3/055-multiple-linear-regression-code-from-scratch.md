# 055 — Multiple Linear Regression: Code from Scratch

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 055
- Transcript title: "Multiple Linear Regression _ Part 3 _ Code From Scratch"
- Transcript file: `055 - 2021-05-17 - Multiple Linear Regression _ Part 3 _ Code From Scratch.txt`
- Topic: implementing multivariate regression manually

## Learning objectives
- Implement multiple linear regression from scratch.
- Understand the practical role of the design matrix.
- Learn how coefficients are solved numerically.
- See how the code connects to the mathematical formulation.

## Code example
```python
import numpy as np

X = np.array([
    [1, 1, 2],
    [1, 2, 3],
    [1, 3, 4],
    [1, 4, 5]
], dtype=float)

y = np.array([3, 5, 7, 9], dtype=float)

beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
print('beta =', beta)

pred = X @ beta
print('Predictions =', pred)
```

Expected output:
```text
beta = [1. 1. 1.]
Predictions = [4. 6. 8. 10.]
```

## Interpretation
This example is intentionally simple: the target is approximately a linear combination of the features. The algorithm estimates coefficients that produce the best linear fit.

## Why this matters
Multiple regression is the standard starting point for many predictive tasks, including:
- real estate pricing
- demand forecasting
- sales prediction
- risk modeling

## Common mistakes
- forgetting to add a constant column for the intercept
- using raw features without checking scale differences
- interpreting coefficients without considering feature correlations

## Key takeaways
- Multiple regression is straightforward to implement with matrix algebra.
- The coefficient vector is estimated via least squares.
- This method remains central in applied ML even when more advanced models are later used.

## Practice questions
1. Why is a design matrix useful in multiple regression?
2. What does the intercept column represent?
3. How are coefficients computed numerically?
4. When would we prefer a more flexible model than linear regression?

## Source reference
- Transcript title: "Multiple Linear Regression _ Part 3 _ Code From Scratch"
- File: `055 - 2021-05-17 - Multiple Linear Regression _ Part 3 _ Code From Scratch.txt`
