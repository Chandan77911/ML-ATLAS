# 033 — Handling Mixed Variables

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 033
- Transcript title: "Handling Mixed Variables _ Feature Engineering"
- Transcript file: `033 - 2021-04-20 - Handling Mixed Variables _ Feature Engineering.txt`
- Topic: mixed-variable preprocessing

## Learning objectives
- Understand what mixed variables are.
- Learn how to handle numeric and categorical signals in the same feature set.
- Split, transform, and encode mixed data appropriately.
- Avoid common mistakes in mixed-feature pipelines.

## Original CampusX concept
Real data is often a mixture of different variable types. A single dataset may contain numeric measurements, categorical labels, and free-form text. Handling mixed variables means preparing these features in a way that each segment is transformed correctly before the model sees them.

This is a common engineering task in real ML work.

## What are mixed variables?
Mixed variables are features whose values do not belong to a single type. Examples include:
- `price_in_rupees` and `city_name`
- date + categorical status
- amount + payment mode
- age + category labels

These need to be treated differently in the pipeline.

## How to handle them
A typical approach is:
1. separate numeric and categorical columns
2. impute missing values separately
3. scale numeric features
4. encode categorical features
5. combine all transformed columns into the final feature matrix

## Python example
```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

X = pd.DataFrame({
    'age': [25, 30, None, 40],
    'income': [35000, 60000, 80000, 90000],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore']
})
y = pd.Series([0, 1, 1, 0])

preprocess = ColumnTransformer([
    ('num', Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ]), ['age', 'income']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city'])
])

model = Pipeline([
    ('preprocess', preprocess),
    ('clf', LogisticRegression(max_iter=1000))
])

model.fit(X, y)
print('Training complete')
```

Expected output:
```text
Training complete
```

## Common mistakes
- scaling categorical columns as if they were numeric
- forgetting to encode category columns separately
- applying missing-value rules to the full dataset instead of each feature subset
- building a pipeline that works for one column type but fails on the rest

## Key takeaways
- Mixed-variable handling is a standard part of real ML workflows.
- Numeric and categorical features usually require different treatments.
- Column-wise preprocessing is often more effective than a one-size-fits-all approach.

## Practice questions
1. What is a mixed-variable dataset?
2. Why do numeric and categorical columns need different preprocessing?
3. What is the purpose of a preprocessing pipeline for mixed data?
4. Why is it important to impute missing values before modeling?

## Source reference
- Transcript title: "Handling Mixed Variables _ Feature Engineering"
- File: `033 - 2021-04-20 - Handling Mixed Variables _ Feature Engineering.txt`
