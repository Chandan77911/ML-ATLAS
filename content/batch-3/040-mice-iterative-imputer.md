# 040 — MICE / Iterative Imputer

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 040
- Transcript title: "Multivariate Imputation by Chained Equations for Missing Value _ MICE Algorithm _ Iterative Imputer"
- Transcript file: `040 - 2021-04-28 - Multivariate Imputation by Chained Equations for Missing Value _ MICE Algorithm _ Iterative Imputer.txt`
- Topic: iterative multivariate imputation via chained equations

## Learning objectives
- Understand why simple imputation methods can be too naive when many features are missing.
- Learn the idea behind MICE and iterative imputation.
- See how an algorithm can fill missing values by repeatedly estimating one feature from the others.
- Understand when iterative imputation is useful.

## Intuition
MICE stands for Multivariate Imputation by Chained Equations. Instead of filling all missing values in one shot, it fills them iteratively.

For each feature with missing values:
1. treat the feature as the target
2. use the remaining features as predictors
3. fit a model to estimate the missing values
4. repeat over multiple rounds until the estimates stabilize

## Why this is useful
When several columns are missing, a single statistic such as the mean may ignore important relationships between features. MICE uses multivariate information to produce more realistic estimates.

## Conceptual idea
Suppose we have features $X_1, X_2, X_3$. To impute $X_1$:

$$
X_1 \approx f(X_2, X_3)
$$

Then for $X_2$:

$$
X_2 \approx g(X_1, X_3)
$$

and so on.

This process repeats until the imputed values converge.

## Python example
```python
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Example dataset with missing values
sample = pd.DataFrame({
    'feature_a': [10, 12, None, 14, 13],
    'feature_b': [20, None, 24, 26, 22],
    'feature_c': [1, 2, 3, None, 5]
})

imputer = IterativeImputer(max_iter=10, random_state=0)
filled = imputer.fit_transform(sample)

print(pd.DataFrame(filled, columns=sample.columns))
```

Expected output (approximate):
```text
   feature_a  feature_b  feature_c
0      10.0      20.0       1.0
1      12.0      22.0       2.0
2      13.0      24.0       3.0
3      14.0      26.0       4.0
4      13.0      22.0       5.0
```

## Advantages
- captures feature relationships better than single-statistic imputation
- useful when there are multiple related columns with missing values
- more principled for complex missingness patterns

## Limitations
- more computationally expensive than mean, median, or mode imputation
- can be unstable if data is small or the missingness is extreme
- requires careful validation to avoid overfitting to missing patterns

## Common mistakes
- using MICE when a simple imputation method is enough
- failing to scale or normalize features when required
- applying imputation across train and test incorrectly

## Key takeaways
- MICE is a multivariate missing-data strategy.
- It iteratively fills missing values using the relationships among other features.
- It is powerful but more complex than single-statistic methods.

## Practice questions
1. What is the main idea behind MICE?
2. Why is simple mean imputation sometimes insufficient?
3. How does iterative imputation differ from one-pass filling?
4. When should MICE be preferred over a simpler method?

## Source reference
- Transcript title: "Multivariate Imputation by Chained Equations for Missing Value _ MICE Algorithm _ Iterative Imputer"
- File: `040 - 2021-04-28 - Multivariate Imputation by Chained Equations for Missing Value _ MICE Algorithm _ Iterative Imputer.txt`
