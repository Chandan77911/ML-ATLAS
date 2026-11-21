# 043 — IQR Outlier Detection

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 043
- Transcript title: "Outlier Detection and Removal using the IQR Method _ Handing Outliers Part 3"
- Transcript file: `043 - 2021-05-01 - Outlier Detection and Removal using the IQR Method _ Handing Outliers Part 3.txt`
- Topic: outlier detection using interquartile range

## Learning objectives
- Explain the IQR method.
- Learn how to compute quartiles and fences.
- Detect outliers using lower and upper bounds.
- Use IQR in a practical example.

## What is IQR?
The interquartile range is the spread between the 25th percentile and 75th percentile.

$$
IQR = Q_3 - Q_1
$$

where:
- $Q_1$ is the first quartile
- $Q_3$ is the third quartile

## Outlier fences
The typical boundaries are:

$$
\text{Lower fence} = Q_1 - 1.5 \times IQR
$$

$$
\text{Upper fence} = Q_3 + 1.5 \times IQR
$$

Any value below the lower fence or above the upper fence is often treated as an outlier.

## Python example
```python
import pandas as pd

scores = pd.Series([20, 22, 23, 24, 24, 25, 30, 200])
Q1 = scores.quantile(0.25)
Q3 = scores.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = scores[(scores < lower) | (scores > upper)]
print('Q1:', Q1)
print('Q3:', Q3)
print('IQR:', IQR)
print('Lower fence:', lower)
print('Upper fence:', upper)
print('Outliers:', outliers.tolist())
```

Expected output:
```text
Q1: 22.75
Q3: 26.25
IQR: 3.5
Lower fence: 17.5
Upper fence: 31.5
Outliers: [200]
```

## Why IQR is popular
It is robust to extreme values because it uses the middle 50% of the data rather than the full mean and standard deviation.

## Common mistakes
- using IQR on a dataset with very few points
- removing outliers without understanding whether they are real or erroneous
- applying the same threshold blindly across all features

## Key takeaways
- IQR is a robust method for outlier detection.
- It defines a normal range based on the central bulk of the data.
- It is often more reliable than z-score for skewed distributions.

## Practice questions
1. What does IQR measure?
2. How are upper and lower fences computed?
3. Why is IQR often considered more robust than z-score?
4. What should you do after identifying an outlier?

## Source reference
- Transcript title: "Outlier Detection and Removal using the IQR Method _ Handing Outliers Part 3"
- File: `043 - 2021-05-01 - Outlier Detection and Removal using the IQR Method _ Handing Outliers Part 3.txt`
