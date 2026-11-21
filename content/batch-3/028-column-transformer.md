# 028 — Column Transformer

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 028
- Transcript title: "Column Transformer in Machine Learning _ How to use ColumnTransformer in Sklearn"
- Transcript file: `028 - 2021-04-14 - Column Transformer in Machine Learning _ How to use ColumnTransformer in Sklearn.txt`
- Topic: automatic preprocessing with ColumnTransformer

## Learning objectives
- Explain why different columns often need different preprocessing steps.
- Use `ColumnTransformer` to apply transformations to selected columns.
- Build a practical preprocessing workflow for mixed datasets.
- Understand how pipelines simplify ML model training.

## Original CampusX concept
The transcript emphasizes that real datasets rarely contain only one data type. Some columns are numeric, others are categorical, and some may require missing-value handling before modeling.

The efficient solution is to treat each column type differently: numeric columns may be standardized, while categorical columns may be encoded. `ColumnTransformer` makes this process clean and automatic.

## Why this matters
A large part of ML engineering is not only modeling but also preprocessing. Without careful handling, a model may receive raw categorical strings or unscaled numeric columns, leading to unstable performance.

## Basic idea
`ColumnTransformer` is a scikit-learn tool that applies different transformers to different subsets of columns.

Example setup:
- numeric columns: `SimpleImputer` + `StandardScaler`
- categorical columns: `OneHotEncoder`

This ensures each feature subset is transformed appropriately without manual code duplication.

## Python example
```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

X = pd.DataFrame({
    'age': [25, 30, 35, 40],
    'salary': [40000, 60000, 70000, 80000],
    'city': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai'],
    'gender': ['M', 'F', 'M', 'F']
})
y = pd.Series([0, 1, 1, 0])

num_cols = ['age', 'salary']
cat_cols = ['city', 'gender']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), num_cols),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ]), cat_cols)
    ]
)

model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

model.fit(X, y)
print('Model trained successfully.')
```

Expected output:
```text
Model trained successfully.
```

## Common mistakes
- applying the same transform to every column
- passing strings directly into models without preprocessing
- forgetting `handle_unknown='ignore'` for new categories
- ignoring the difference between numeric and categorical feature handling

## Key takeaways
- Real datasets are mixed, so preprocessing is column-specific.
- `ColumnTransformer` organizes this effort cleanly.
- It is a core building block in scikit-learn pipelines.

## Practice questions
1. Why do different columns often need different preprocessing steps?
2. What does `ColumnTransformer` automate?
3. When would you use `OneHotEncoder` on a column?
4. Why are pipelines useful with preprocessing tools?

## Source reference
- Transcript title: "Column Transformer in Machine Learning _ How to use ColumnTransformer in Sklearn"
- File: `028 - 2021-04-14 - Column Transformer in Machine Learning _ How to use ColumnTransformer in Sklearn.txt`
