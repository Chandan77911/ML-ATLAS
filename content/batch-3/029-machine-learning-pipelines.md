# 029 — Machine Learning Pipelines

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 029
- Transcript title: "Machine Learning Pipelines A-Z _ Day 29 _ 100 Days of Machine Learning"
- Transcript file: `029 - 2021-04-15 - Machine Learning Pipelines A-Z _ Day 29 _ 100 Days of Machine Learning.txt`
- Topic: ML pipelines and end-to-end preprocessing

## Learning objectives
- Understand the purpose of a machine learning pipeline.
- Learn how to chain preprocessing and modeling steps reproducibly.
- Avoid data leakage and improve consistency during training and validation.
- Use scikit-learn `Pipeline` for real ML workflows.

## Original CampusX concept
The lecture explains that a machine learning workflow is not just a model; it is a sequence of tasks. Data cleaning, feature engineering, scaling, encoding, and model fitting belong to a single pipeline. A pipeline ensures that the same transformations are applied in the same way to train and test data.

This is critical because it reduces errors and makes workflows easier to manage.

## Why pipelines matter
Without a pipeline, it is easy to:
- fit scalers on the full dataset
- forget transformations during prediction
- apply preprocessing inconsistently
- leak information from validation into training

A pipeline encapsulates these steps so training and inference stay aligned.

## Pipeline structure
The typical structure is:

$$
\text{Preprocess} \rightarrow \text{Train model} \rightarrow \text{Predict}
$$

With scikit-learn, a pipeline can combine multiple steps:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
```

## Python example
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000))
])

pipe.fit(X_train, y_train)
print('Train score:', pipe.score(X_train, y_train))
print('Test score:', pipe.score(X_test, y_test))
```

Expected output:
```text
Train score: 0.9666666666666667
Test score: 1.0
```

## Common mistakes
- fitting preprocessing on the whole dataset before splitting
- mixing transformed and untransformed data in evaluation
- forgetting to use the same pipeline for inference
- using a pipeline without understanding the steps inside it

## Key takeaways
- Pipelines keep preprocessing and modeling together.
- They help avoid leakage and reproducibility issues.
- They make real-world ML workflows cleaner and easier to maintain.

## Practice questions
1. What is a machine learning pipeline?
2. Why is it important to keep preprocessing and modeling in one workflow?
3. How does a pipeline prevent leakage?
4. Why is standardization often part of the pipeline?

## Source reference
- Transcript title: "Machine Learning Pipelines A-Z _ Day 29 _ 100 Days of Machine Learning"
- File: `029 - 2021-04-15 - Machine Learning Pipelines A-Z _ Day 29 _ 100 Days of Machine Learning.txt`
