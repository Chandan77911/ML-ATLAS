# 036 — Handling Missing Numerical Data

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 036
- Transcript title: "Handling missing data _ Numerical Data _ Simple Imputer"
- Transcript file: `036 - 2021-04-23 - Handling missing data _ Numerical Data _ Simple Imputer.txt`
- Topic: numerical missing-data imputation

## Learning objectives
- Understand why missing numerical values are often imputed rather than dropped.
- Learn the concept of `SimpleImputer` for numeric columns.
- Distinguish between mean, median, and constant imputation strategies.
- Apply imputation in a machine learning workflow.

## Original CampusX concept
The transcript continues the missing-data discussion by focusing on numerical variables. Instead of deleting rows, a more common approach is to fill missing values using a statistical summary such as the mean or median.

This keeps the dataset size intact while helping the model avoid failure due to missing values.

## Why imputation is needed
Some models cannot handle missing values directly. Imputation fills gaps with estimated values based on the available distribution.

For numerical features, common choices are:
- mean
- median
- most frequent value
- constant fill value

## Mean imputation
The mean is used when the feature is approximately symmetric and not strongly affected by outliers.

$$
 \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

The missing value is replaced by $\bar{x}$.

## Median imputation
The median is often safer for skewed data or data containing outliers because it is robust to extreme values.

## SimpleImputer in scikit-learn
```python
from sklearn.impute import SimpleImputer
import numpy as np

X = np.array([[10.0], [20.0], [np.nan], [30.0]])

imputer = SimpleImputer(strategy='mean')
print(imputer.fit_transform(X))
```

Expected output:
```text
[[10. ]
 [20. ]
 [20. ]
 [30. ]]
```

## Python example with DataFrame
```python
import pandas as pd
from sklearn.impute import SimpleImputer

sales = pd.DataFrame({
    'monthly_sales': [1200, 1500, None, 1800, 2200]
})

imputer = SimpleImputer(strategy='median')
sales['monthly_sales'] = imputer.fit_transform(sales[['monthly_sales']])
print(sales)
```

Expected output:
```text
   monthly_sales
0         1200.0
1         1500.0
2         1650.0
3         1800.0
4         2200.0
```

## When to use mean vs median
- mean: good for relatively symmetric numerical data
- median: better when the feature is skewed or contains outliers

## Common mistakes
- imputing with the mean when outliers dominate the feature
- imputing after split without using training-only statistics
- ignoring whether the missingness pattern is informative
- treating imputed values as actual observed measurements without noting the assumption

## Key takeaways
- Missing numerical values are often imputed rather than dropped.
- `SimpleImputer` is a practical scikit-learn tool.
- The chosen statistic should match the data distribution and the modeling goal.

## Practice questions
1. Why is imputation often preferred over dropping rows?
2. When is median imputation safer than mean imputation?
3. What does `SimpleImputer(strategy='mean')` do?
4. Why should imputation statistics be computed on the training split only?

## Source reference
- Transcript title: "Handling missing data _ Numerical Data _ Simple Imputer"
- File: `036 - 2021-04-23 - Handling missing data _ Numerical Data _ Simple Imputer.txt`
