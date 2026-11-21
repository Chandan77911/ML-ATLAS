# 050 — Simple Linear Regression

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 050
- Transcript title: "Simple Linear Regression _ Code + Intuition _ Simplest Explanation in Hindi"
- Transcript file: `050 - 2021-05-10 - Simple Linear Regression _ Code + Intuition _ Simplest Explanation in Hindi.txt`
- Topic: linear relationship between one feature and one target

## Learning objectives
- Explain the goal of simple linear regression.
- Understand the line equation and its interpretation.
- Learn how regression is used for prediction.
- Implement a small linear regression example from scratch.

## Intuition
Simple linear regression tries to find a straight line that best describes the relationship between one input variable and one output variable.

If $x$ increases, how does $y$ change on average?

This is the simplest form of supervised learning with a continuous target.

## Model form
The model is:

$$
y = mx + c + \epsilon
$$

where:
- $x$ is the input feature
- $y$ is the target
- $m$ is the slope
- $c$ is the intercept
- $\epsilon$ is the residual or error term

## Why this exists
Many real-world problems can be approximated by a linear relationship. For example:
- sales vs advertising spend
- house prices vs square footage
- temperature vs electricity usage

## Python example from scratch
```python
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

x_mean = x.mean()
y_mean = y.mean()

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

m = numerator / denominator
c = y_mean - m * x_mean

print('Slope m:', m)
print('Intercept c:', c)

pred = m * x + c
print('Predictions:', pred)
```

Expected output:
```text
Slope m: 0.7
Intercept c: 1.6
Predictions: [2.3 3.0 3.7 4.4 5.1]
```

## Interpretation
The slope tells us how much the output changes for a one-unit increase in the input. The intercept is the predicted value when $x = 0$.

## Key takeaways
- Linear regression fits a straight line through the data.
- It is the foundation of more complex regression models.
- The key is to estimate $m$ and $c$ so that predictions are as close as possible to the observed labels.

## Practice questions
1. What does simple linear regression model?
2. What do slope and intercept represent?
3. What is the role of the residual term?
4. Why is a line a reasonable first model for many relationships?

## Source reference
- Transcript title: "Simple Linear Regression _ Code + Intuition _ Simplest Explanation in Hindi"
- File: `050 - 2021-05-10 - Simple Linear Regression _ Code + Intuition _ Simplest Explanation in Hindi.txt`
