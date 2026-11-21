# 025 — Feature Scaling: Normalization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 025
- Transcript title: "Feature Scaling - Normalization _ MinMaxScaling _ MaxAbsScaling _ RobustScaling"
- Transcript file: `025 - 2021-04-10 - Feature Scaling - Normalization _ MinMaxScaling _ MaxAbsScaling _ RobustScaling.txt`
- Topic: feature normalization techniques

## Learning objectives
- Define normalization and contrast it with standardization.
- Understand MinMax scaling, MaxAbs scaling, and Robust scaling.
- Learn when each method is useful.
- See how normalization affects optimization and model behavior.

## Original CampusX concept
The transcript explains that normalization is another common form of feature scaling. Unlike standardization, which centers data around zero and uses standard deviation, normalization brings the feature into a finite range.

The main idea is to scale features so they become comparable without losing their relative order.

## Why normalization matters
Some models work better when features are bounded to a known range, often $[0, 1]$ or $[-1, 1]$. This is especially useful when:
- the model uses gradient descent
- the feature values differ by orders of magnitude
- the data contains sparse numeric features

## MinMax scaling
The standard MinMax formula is:

$$
 x' = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

This rescales values into the range $[0, 1]$.

### Example
For values `[10, 20, 30]`:
- min = 10
- max = 30

So:

$$
 x' = \frac{x - 10}{20}
$$

- $10 \rightarrow 0$
- $20 \rightarrow 0.5$
- $30 \rightarrow 1$

## MaxAbs scaling
This method divides by the maximum absolute value:

$$
 x' = \frac{x}{|x_{max}|}
$$

This works well for sparse data and preserves sign information. It maps values into the range $[-1, 1]$.

## Robust scaling
Robust scaling is designed for data with outliers. It uses the median and interquartile range:

$$
 x' = \frac{x - Q_2}{Q_3 - Q_1}
$$

Where:
- $Q_2$ is the median
- $Q_1$ and $Q_3$ are quartiles

This makes it less sensitive to extreme values than MinMax scaling.

## Python example
```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, RobustScaler
import numpy as np

X = np.array([[10.0], [20.0], [30.0], [40.0], [50.0]])

mms = MinMaxScaler()
print('MinMax:', mms.fit_transform(X).ravel())

mas = MaxAbsScaler()
print('MaxAbs:', mas.fit_transform(X).ravel())

rs = RobustScaler()
print('Robust:', rs.fit_transform(X).ravel())
```

Expected output:
```text
MinMax: [0.   0.25 0.5  0.75 1.  ]
MaxAbs: [0.2 0.4 0.6 0.8 1. ]
Robust: [-1.6 -0.8 0.0 0.8 1.6]
```

## When to use each scaler
- MinMax: useful when a bounded range is helpful and outliers are not dominant
- MaxAbs: useful for sparse matrices and signed values
- Robust: better when the data contains outliers
- Standardization: preferred when you want zero-mean, unit-variance features

## Common mistakes
- using MinMax on heavily skewed data without considering outliers
- confusing normalization with encoding
- scaling the target variable when the model should predict original units
- applying scaling after the split in a way that leaks information

## Key takeaways
- Normalization rescales features into a smaller range.
- Standardization and normalization are related but not the same.
- Robust scaling is useful when the data contains outliers.
- The correct choice depends on the model and the dataset distribution.

## Practice questions
1. What is the main difference between normalization and standardization?
2. When would you prefer RobustScaler over MinMaxScaler?
3. Why are sparse datasets often better with MaxAbsScaler?
4. Give one example where scaling can improve model performance.

## Source reference
- Transcript title: "Feature Scaling - Normalization _ MinMaxScaling _ MaxAbsScaling _ RobustScaling"
- File: `025 - 2021-04-10 - Feature Scaling - Normalization _ MinMaxScaling _ MaxAbsScaling _ RobustScaling.txt`
