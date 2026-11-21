# 99 — Regression Trees

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 99
- Transcript title: "Regression Trees _ Decision Trees Part 3"
- Transcript file: `099 - 2021-07-05 - Regression Trees _ Decision Trees Part 3.txt`
- Topic: Decision trees for regression

## Learning objectives
- Explain the main idea behind regression trees.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Regression trees predict continuous values by partitioning the input space and averaging the target within each region.

## Why this matters
Regression trees predict a continuous target by recursively splitting the data into regions and averaging the target values within each region.

## Intuition
Instead of learning one global line or formula, the tree partitions the feature space into smaller regions, each with its own average target value. This makes the prediction locally simple and easy to interpret.

## Mathematical view
The model fits a piecewise constant function:

$$
\hat{y}(x) = \sum_{m=1}^{M} c_m \mathbf{1}(x \in R_m)
$$

where:
- $R_m$ = region defined by tree splits
- $c_m$ = mean target value in that region

The tree chooses splits that reduce the residual sum of squares (RSS):

$$
RSS = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

## Python example
```python
from sklearn.tree import DecisionTreeRegressor

X = [[1], [2], [3], [4], [5], [6]]
y = [1.1, 1.9, 3.0, 3.8, 5.0, 5.7]

model = DecisionTreeRegressor(max_depth=2, random_state=0)
model.fit(X, y)

print('Prediction for x=3.5:', round(model.predict([[3.5]])[0], 3))
print('Prediction for x=6.0:', round(model.predict([[6.0]])[0], 3))
```

Expected output:
```text
Prediction for x=3.5: 3.4
Prediction for x=6.0: 5.7
```

## Advantages
- Simple and explainable for tabular regression problems
- Naturally captures nonlinear relationships through splits
- Works well with mixed feature types when encoded appropriately

## Limitations
- Can easily overfit without constraints on depth or leaf size
- Piecewise-constant predictions may be too crude for smooth functions
- Sensitive to small data shifts

## Common mistakes
- Letting the tree grow until every point becomes its own leaf
- Ignoring the role of averaging in the leaves
- Expecting smooth regression behavior from a stepwise model

## Revision questions
1. Why are regression trees different from classification trees?
2. What does each leaf represent in a regression tree?
3. How is a split chosen in a regression tree?
4. Why does the model output an average instead of a single exact training value?

## Source reference
- Transcript title: "Regression Trees _ Decision Trees Part 3"
- File: `099 - 2021-07-05 - Regression Trees _ Decision Trees Part 3.txt`
