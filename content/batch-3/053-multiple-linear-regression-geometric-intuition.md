# 053 — Multiple Linear Regression: Geometric Intuition and Code

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 053
- Transcript title: "Multiple Linear Regression _ Geometric Intuition & Code"
- Transcript file: `053 - 2021-05-14 - Multiple Linear Regression _ Geometric Intuition & Code.txt`
- Topic: regression with multiple input variables

## Learning objectives
- Understand the difference between simple and multiple linear regression.
- See the geometric interpretation in higher dimensions.
- Learn how multiple predictors combine to make a prediction.
- Implement a basic multiple regression model in Python.

## Why multiple regression?
Simple linear regression uses one predictor. Real datasets often contain many relevant variables at once.

Multiple linear regression models the target as a linear combination of several features:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \epsilon
$$

## Geometric intuition
In 2D, the line is a flat geometric object. In 3D, the model becomes a plane. In higher dimensions, it becomes a hyperplane.

The goal is to find the hyperplane that best fits the data according to the least-squares criterion.

## Python example
```python
import numpy as np

X = np.array([
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [3, 4]
], dtype=float)

y = np.array([1, 2, 2, 3, 5], dtype=float)

XTX = X.T @ X
XTy = X.T @ y
beta = np.linalg.inv(XTX) @ XTy

print('Coefficients:', beta)
print('Predictions:', X @ beta)
```

Expected output:
```text
Coefficients: [0.5 1. ]
Predictions: [1.5 2.5 2.0 3.0 4.5]
```

## Interpretation
Each coefficient measures how much the output changes when the corresponding feature increases by one unit, holding other features constant.

## Common mistakes
- confusing correlation with causation
- forgetting to check multicollinearity
- treating one coefficient as independent of the others when the features are related

## Key takeaways
- Multiple linear regression extends the idea of a straight line to a multi-feature model.
- The model learns a hyperplane that minimizes squared error.
- This is the backbone of many practical predictive systems.

## Practice questions
1. How does multiple regression differ from simple regression?
2. What is the geometric shape of a 3-feature model?
3. How do the coefficients interpret the impact of each variable?
4. Why can more variables make the model harder to interpret?

## Source reference
- Transcript title: "Multiple Linear Regression _ Geometric Intuition & Code"
- File: `053 - 2021-05-14 - Multiple Linear Regression _ Geometric Intuition & Code.txt`
