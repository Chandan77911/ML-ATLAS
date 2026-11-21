# 037 — Handling Missing Categorical Data

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 037
- Transcript title: "Handling Missing Categorical Data _ Simple Imputer _ Most Frequent Imputation _ Missing Category Imputation"
- Transcript file: `037 - 2021-04-24 - Handling Missing Categorical Data _ Simple Imputer _ Most Frequent Imputation _ Missing Category Imputation.txt`
- Topic: missing-value treatment for categorical variables

## Learning objectives
- Understand why categorical missing values cannot be handled like numeric ones.
- Learn about the mode or most-frequent category imputation.
- See how a missing category can itself be treated as a distinct category.
- Apply a practical imputation strategy in Python.

## Why categorical missing values matter
Categorical variables often include strings such as `male`, `female`, `urban`, `rural`, or `low`, `medium`, `high`. If missing values are present, many models require them to be filled or encoded before training.

The most common strategy is to replace the missing entries with the most frequent category, also called the mode.

## Mode-based imputation
For a categorical feature with observed values:

$$
\{\text{A}, \text{A}, \text{B}, \text{A}, \text{C}\}
$$

The mode is `A` because it appears most often.

We replace the missing values with `A` when `A` is the most frequent value.

## Alternative: missing-category indicator
Sometimes a missing value is not random noise. It may carry information. In that case, we can create a new category such as `Unknown` or `Missing` and treat it as a real category.

This is particularly useful when missingness is common and not well represented by the mode alone.

## Python example
```python
import pandas as pd
from sklearn.impute import SimpleImputer

salary_data = pd.DataFrame({
    'city': ['Delhi', 'Mumbai', None, 'Delhi', 'Bengaluru', None],
    'income_group': ['High', 'Low', 'Medium', None, 'High', 'Low']
})

print('Before imputation:\n', salary_data)

city_imputer = SimpleImputer(strategy='most_frequent')
salary_data['city'] = city_imputer.fit_transform(salary_data[['city']])

income_imputer = SimpleImputer(strategy='most_frequent')
salary_data['income_group'] = income_imputer.fit_transform(salary_data[['income_group']])

print('\nAfter imputation:\n', salary_data)
```

Expected output:
```text
Before imputation:
        city income_group
0    Delhi         High
1    Mumbai         Low
2     None       Medium
3    Delhi         None
4  Bengaluru        High
5     None          Low

After imputation:
        city income_group
0    Delhi         High
1    Mumbai         Low
2    Delhi       Medium
3    Delhi         High
4  Bengaluru        High
5    Delhi          Low
```

## Common mistakes
- imputing missing categories with a numeric placeholder like `0` without considering encoding
- treating missing as if it were a real value with no meaning
- forgetting that categorical imputation should be based on training data only

## Key takeaways
- Categorical missing values are usually filled using the mode.
- Missing entries may also be represented as a dedicated category.
- The strategy depends on whether the missingness is random or informative.

## Practice questions
1. Why do we handle categorical missing data differently from numeric missing data?
2. What is the mode in a categorical feature?
3. Why might a missing category be encoded as `Unknown` instead of being replaced by the mode?
4. What is the risk of imputing using the full dataset instead of the training split?

## Source reference
- Transcript title: "Handling Missing Categorical Data _ Simple Imputer _ Most Frequent Imputation _ Missing Category Imputation"
- File: `037 - 2021-04-24 - Handling Missing Categorical Data _ Simple Imputer _ Most Frequent Imputation _ Missing Category Imputation.txt`
