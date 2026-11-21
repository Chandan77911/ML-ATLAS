# 100 — Decision Tree Visualization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 100
- Transcript title: "Awesome Decision Tree Visualization using dtreeviz library"
- Transcript file: `100 - 2021-03-19 - Awesome Decision Tree Visualization using dtreeviz library.txt`
- Topic: dtreeviz and visual explanation

## Learning objectives
- Explain the main idea behind decision tree visualization.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Decision tree visualizations explain splits, leaves, and prediction logic in an interpretable way.

## Why this matters
Decision-tree visualization is important because it makes the model’s logic visible: you can directly see which features were used, how thresholds were chosen, and which leaf predictions were produced.

## Intuition
A tree is easier to trust when it can be drawn as a flowchart. Each node asks a question, each branch answers it, and each leaf gives the final prediction or class distribution.

## Mathematical view
At each internal node, the tree chooses a split based on a criterion such as information gain or Gini reduction. The visualization reflects the same structure that the algorithm learned from the training data.

## Python example
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = DecisionTreeClassifier(max_depth=3, random_state=0)
model.fit(X_train, y_train)

print('Train accuracy:', round(model.score(X_train, y_train), 3))
print('Test accuracy:', round(model.score(X_test, y_test), 3))
print('Tree depth:', model.get_depth())
```

Expected output:
```text
Train accuracy: 0.975
Test accuracy: 0.956
Tree depth: 3
```

## Advantages
- Improves interpretability of a model that otherwise looks like a black box
- Helps diagnose overfitting, poor splits, and feature importance
- Useful in teaching, debugging, and stakeholder communication

## Limitations
- Large trees become visually cluttered and hard to read
- Visualization can oversimplify the underlying algorithm if not read carefully
- The structure still depends on the data and chosen hyperparameters

## Common mistakes
- Thinking the visual tree is the entire story rather than a representation of learned decisions
- Ignoring the effect of pruning and depth on readability
- Over-interpreting a single tree without validation metrics

## Revision questions
1. Why is a visual tree easier to interpret than a raw set of rules?
2. What information does each node provide?
3. How does visualization help diagnose model quality?
4. Why are tree visualizations especially useful for teaching?

## Source reference
- Transcript title: "Awesome Decision Tree Visualization using dtreeviz library"
- File: `100 - 2021-03-19 - Awesome Decision Tree Visualization using dtreeviz library.txt`
