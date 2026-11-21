# 039 — KNN Imputer

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 039
- Transcript title: "KNN Imputer _ Multivariate Imputation _ Handling Missing Data Part 5"
- Transcript file: `039 - 2021-04-27 - KNN Imputer _ Multivariate Imputation _ Handling Missing Data Part 5.txt`
- Topic: imputation using nearest neighbors

## Learning objectives
- Understand why a missing value can be estimated from similar rows.
- Learn how KNN imputation works.
- Recognize the computational cost and assumptions behind the method.
- Apply KNN imputation in a small example.

## Intuition
A missing value is estimated by considering neighboring rows that are similar in other features.

If two observations have similar values across the other columns, then their missing value in one feature is likely to be close as well.

This is the core idea behind KNN imputation.

## Mathematical intuition
For a missing value in feature $x_j$, we find the $k$ nearest rows based on the other features.

Then we estimate:

$$
\hat{x}_{ij} = \frac{1}{k} \sum_{r \in N_k(i)} x_{rj}
$$

where:
- $N_k(i)$ is the set of the $k$ nearest neighbors of row $i$
- $x_{rj}$ is the observed value of feature $j$ in neighbor $r$

This is essentially a local averaging method.

## Python example
```python
import pandas as pd
from sklearn.impute import KNNImputer

sensor_data = pd.DataFrame({
    'temperature': [30, 32, None, 31, 29],
    'humidity': [70, 68, 74, 72, 69],
    'pressure': [101, 100, 99, 101, 100]
})

imputer = KNNImputer(n_neighbors=2)
filled = imputer.fit_transform(sensor_data)
print(pd.DataFrame(filled, columns=sensor_data.columns))
```

Expected output:
```text
   temperature  humidity  pressure
0        30.0       70      101
1        32.0       68      100
2        31.0       74       99
3        31.0       72      101
4        29.0       69      100
```

## Pros and cons
Advantages:
- often more realistic than mean filling
- uses relationships among features
- can work well when similar rows exist

Disadvantages:
- computationally expensive on large datasets
- sensitive to scaling of features
- poor for very high-dimensional sparse data

## Common mistakes
- not scaling data before KNN imputation
- using too many neighbors or too few neighbors without validation
- applying KNN to irrelevant features that do not contribute structurally

## Key takeaways
- KNN imputation uses the similarity among rows.
- It is a multivariate approach because it considers multiple features together.
- It can improve data quality, but computational cost must be considered.

## Practice questions
1. What is the intuition behind KNN imputation?
2. Why is scaling important before KNN imputation?
3. What is the role of the neighbor count $k$?
4. How does KNN imputation differ from mean imputation?

## Source reference
- Transcript title: "KNN Imputer _ Multivariate Imputation _ Handling Missing Data Part 5"
- File: `039 - 2021-04-27 - KNN Imputer _ Multivariate Imputation _ Handling Missing Data Part 5.txt`
