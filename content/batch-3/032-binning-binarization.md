# 032 — Binning, Binarization, and Discretization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 032
- Transcript title: "Binning and Binarization _ Discretization _ Quantile Binning _ KMeans Binning"
- Transcript file: `032 - 2021-04-19 - Binning and Binarization _ Discretization _ Quantile Binning _ KMeans Binning.txt`
- Topic: discretization and binning strategies

## Learning objectives
- Understand why numeric features are sometimes converted into buckets.
- Learn the difference between binning, discretization, and binarization.
- Recognize when quantile bins or KMeans bins are useful.
- Know the benefits and drawbacks of converting continuous values into categories.

## Original CampusX concept
The transcript introduces binning as a feature engineering transformation. Instead of giving a model a continuous value directly, we divide the range of a numeric variable into intervals and represent the value by its interval.

This helps when a continuous variable is noisy, nonlinear, or better represented in a coarse segmented form.

## Why binning is useful
Binning can be helpful when:
- you want to create categories from a continuous variable
- the relationship is non-linear and threshold-based
- the model benefits from simpler segments instead of raw values

Examples:
- age groups: 0–18, 19–35, 36–60, 60+
- income buckets: low, middle, high
- product price tiers: budget, mid, premium

## Types of binning

### Equal-width binning
Divide the range into fixed-width intervals.

### Quantile binning
Create bins with roughly equal numbers of samples per interval. This is useful when the distribution is skewed.

### KMeans binning
Use clustering to create bins based on data density and similarity.

This is often valuable when the variable distribution is irregular and equal-width intervals would be misleading.

## Binarization
Binarization converts a feature into 0/1 depending on whether it crosses a threshold.

Example:

$$
 x' = \begin{cases}
 1, & x > t \\
 0, & x \leq t
 \end{cases}
$$

This is useful when only a high/low condition matters.

## Python example
```python
import pandas as pd

age = pd.Series([18, 22, 30, 41, 55, 68, 72])

print(pd.cut(age, bins=3, labels=['young', 'middle', 'old']))
print((age > 40).astype(int))
```

Expected output:
```text
0    young
1    young
2    middle
3    middle
4    old
5    old
6    old
Name: dtype: category
0    0
1    0
2    0
3    1
4    1
5    1
6    1
```

## Common mistakes
- creating too many bins, which adds noise
- using equal-width bins when the data is highly skewed
- forgetting that binning can remove information
- converting continuous values into categories without understanding business meaning

## Key takeaways
- Binning is a form of discretization.
- It can simplify nonlinear relationships.
- Quantile bins are often better than equal-width bins for skewed variables.
- Binarization is useful when only a threshold matters.

## Practice questions
1. What is the main purpose of discretization?
2. Why might quantile binning be better than equal-width binning?
3. How does binarization differ from general binning?
4. What is one risk of over-binning a feature?

## Source reference
- Transcript title: "Binning and Binarization _ Discretization _ Quantile Binning _ KMeans Binning"
- File: `032 - 2021-04-19 - Binning and Binarization _ Discretization _ Quantile Binning _ KMeans Binning.txt`
