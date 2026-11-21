# 044 — Percentile-Based Outlier Detection and Winsorization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 044
- Transcript title: "Outlier Detection using the Percentile Method _ Winsorization Technique"
- Transcript file: `044 - 2021-05-03 - Outlier Detection using the Percentile Method _ Winsorization Technique.txt`
- Topic: percentile-based outlier detection and winsorization

## Learning objectives
- Understand how percentiles help identify extreme values.
- Learn the winsorization technique for capping extreme values.
- Differentiate between outlier removal and outlier clipping.
- Apply these ideas in practical ML workflows.

## Percentile method
Percentiles define where a value sits in the overall distribution. For example:
- 1st percentile = lower 1% of values
- 99th percentile = value below which 99% of observations fall

A common strategy is to flag values beyond the 1st and 99th percentiles (or more extreme bounds) as outliers.

## Winsorization
Winsorization caps extreme values to a chosen percentile threshold.

Instead of deleting the extreme points, we replace them with the nearest acceptable boundary.

This is useful when you want to keep sample size while reducing the influence of outliers.

## Python example
```python
import pandas as pd

scores = pd.Series([10, 12, 13, 12, 14, 500, 15, 16, 17, 18])
low = scores.quantile(0.01)
high = scores.quantile(0.99)

print('1st percentile:', low)
print('99th percentile:', high)

winsorized = scores.clip(lower=low, upper=high)
print(winsorized)
```

Expected output:
```text
1st percentile: 10.69
99th percentile: 33.34
0     10.00
1     12.00
2     13.00
3     12.00
4     14.00
5     33.34
6     15.00
7     16.00
8     17.00
9     18.00
```

## When to use this approach
- when dataset size matters and deleting rows would be costly
- when outliers are valid but excessive
- when the model is sensitive to extreme values

## Common mistakes
- setting thresholds too aggressive or too loose
- capping values without understanding whether they are true anomalies or valid business behavior
- using percentiles on tiny datasets without considering sample instability

## Key takeaways
- Percentiles provide an interpretable way to detect extreme observations.
- Winsorization limits the influence of rare but valid extremes.
- Outlier treatment should depend on the data and the modeling task.

## Practice questions
1. What is a percentile-based outlier strategy?
2. What does winsorization do?
3. Why might we prefer clipping over deletion?
4. What is the risk of setting brittle thresholds?

## Source reference
- Transcript title: "Outlier Detection using the Percentile Method _ Winsorization Technique"
- File: `044 - 2021-05-03 - Outlier Detection using the Percentile Method _ Winsorization Technique.txt`
