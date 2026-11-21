# 98 — Decision Tree Hyperparameters

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 98
- Transcript title: "Decision Trees - Hyperparameters _ Overfitting and Underfitting in Decision Trees"
- Transcript file: `098 - 2021-07-03 - Decision Trees - Hyperparameters _ Overfitting and Underfitting in Decision Trees.txt`
- Topic: Hyperparameters in tree models

## Learning objectives
- Explain the main idea behind decision tree hyperparameters.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Tree depth, minimum samples per leaf, and split criteria control overfitting and interpretability.

## Why this matters
Tree hyperparameters control how much the model is allowed to fit the training data. In practice, this means balancing interpretability and accuracy against overfitting.

## Intuition
A very deep tree can memorize noise in the training set. A shallow tree may miss real structure. Hyperparameters such as maximum depth and minimum leaf size help control that trade-off.

## Mathematical view
The tree is built greedily, choosing the split that improves impurity the most. The complexity of the final model is controlled by constraints such as:

- maximum depth
- minimum samples per split
- minimum samples per leaf
- maximum number of leaf nodes

These constraints act as regularization for the tree model.

## Python example
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model_deep = DecisionTreeClassifier(max_depth=None, random_state=0)
model_shallow = DecisionTreeClassifier(max_depth=2, random_state=0)

model_deep.fit(X_train, y_train)
model_shallow.fit(X_train, y_train)

print('Deep train acc:', round(model_deep.score(X_train, y_train), 3))
print('Shallow train acc:', round(model_shallow.score(X_train, y_train), 3))
```

Expected output:
```text
Deep train acc: 1.0
Shallow train acc: 0.955
```

## Advantages
- Easy way to manage overfitting
- Helps produce simpler, more interpretable trees
- Common in production pipelines when explainability matters

## Limitations
- Tuning is still required for best performance
- Too much regularization can underfit real patterns
- Trees remain sensitive to data distribution changes

## Common mistakes
- Letting depth grow without validation
- Treating tree depth as a universal target
- Ignoring the bias-variance trade-off in tree learning

## Revision questions
1. Why is tree depth a critical hyperparameter?
2. What do minimum leaf and minimum split constraints do?
3. How can a tree overfit the training data?
4. Why is regularization still needed even for a decision tree?

## Source reference
- Transcript title: "Decision Trees - Hyperparameters _ Overfitting and Underfitting in Decision Trees"
- File: `098 - 2021-07-03 - Decision Trees - Hyperparameters _ Overfitting and Underfitting in Decision Trees.txt`
