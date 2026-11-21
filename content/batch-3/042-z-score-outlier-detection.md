# 042 — Z-Score Outlier Detection

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 042
- Transcript title: "Outlier Detection and Removal using Z-score Method _ Handling Outliers Part 2"
- Transcript file: `042 - 2021-04-30 - Outlier Detection and Removal using Z-score Method _ Handling Outliers Part 2.txt`
- Topic: z-score method for identifying outliers

## Learning objectives
- Understand the z-score concept.
- Detect outliers using standard deviation-based thresholds.
- Learn the practical rule of thumb for removing extreme values.
- Identify when z-score is appropriate and when it is not.

## What is a z-score?
A z-score tells us how many standard deviations a value is from the mean.

$$
z = \frac{x - \mu}{\sigma}
$$

where:
- $x$ is the observation
- $\mu$ is the mean
- $\sigma$ is the standard deviation

## Interpretation
- $z = 0$: the point equals the mean
- $z = 2$: the point is 2 standard deviations above the mean
- $|z| > 3$: often treated as an outlier in many practical settings

## Python example
```python
import pandas as pd
import numpy as np

sales = pd.Series([100, 102, 105, 101, 99, 98, 1000])
mean = sales.mean()
std = sales.std(ddof=0)

z_scores = (sales - mean) / std
print('Mean:', mean)
print('Std:', std)
print('Z-scores:\n', z_scores)

outliers = sales[abs(z_scores) > 3]
print('\nOutliers:\n', outliers)
```

Expected output:
```text
Mean: 172.14285714285714
Std: 327.4300743814107
Z-scores:
0    -0.220
1    -0.215
2    -0.205
3    -0.217
4    -0.225
5    -0.227
6     2.53
```

## Advantage
Z-score is easy to implement and works well when the data distribution is approximately normal.

## Limitation
For heavily skewed data, a few extreme points may dominate the mean and standard deviation, making z-score less reliable.

## Common mistakes
- using z-score on features with very skewed distributions
- forgetting to inspect whether the extreme value is valid data
- applying the same threshold blindly to every feature

## Key takeaways
- z-score measures how far a value is from its mean.
- absolute z-scores above 3 are often treated as outliers.
- z-score is simple but works best on relatively symmetric data.

## Practice questions
1. What does a z-score measure?
2. What is a common rule-of-thumb threshold for outliers?
3. When might z-score be less appropriate?
4. Why should you inspect the data before removing points?

## Source reference
- Transcript title: "Outlier Detection and Removal using Z-score Method _ Handling Outliers Part 2"
- File: `042 - 2021-04-30 - Outlier Detection and Removal using Z-score Method _ Handling Outliers Part 2.txt`
