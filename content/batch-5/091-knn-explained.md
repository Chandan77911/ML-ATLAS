# 91 — K-Nearest Neighbors

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 91
- Transcript title: "What is K Nearest Neighbors_ _ KNN Explained in Hindi _ Simple Overview in 1 Video _ CampusX"
- Transcript file: `091 - 2023-05-23 - What is K Nearest Neighbors_ _ KNN Explained in Hindi _ Simple Overview in 1 Video _ CampusX.txt`
- Topic: KNN intuition and code

## Learning objectives
- Explain the main idea behind k-nearest neighbors.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
KNN predicts a point by looking at the labels of the nearest neighboring points in feature space.

## Why this matters
KNN is one of the simplest classification methods: it predicts a label based on the labels of the closest training points. It is a useful baseline and an easy way to understand locality in data.

## Intuition
If a new point is surrounded by points of one class, it is likely to belong to that class. The model does not learn a global equation; it asks, “Which nearby examples look similar?”

## Mathematical view
The distance from a new sample $x$ to a training point $x_i$ is usually measured with Euclidean distance:

$$
d(x, x_i) = \sqrt{\sum_{j=1}^{m}(x_j - x_{ij})^2}
$$

The algorithm then selects the $k$ nearest neighbors and uses a voting rule. For classification:

$$
\hat{y} = \text{mode}(y_1, y_2, \dots, y_k)
$$

For regression:

$$
\hat{y} = \frac{1}{k}\sum_{i=1}^{k} y_i
$$

## Python example
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.3)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print('Train accuracy:', round(model.score(X_train, y_train), 3))
print('Test accuracy:', round(model.score(X_test, y_test), 3))
```

Expected output:
```text
Train accuracy: 0.962
Test accuracy: 0.978
```

## Advantages
- Simple to understand and implement
- No explicit training phase beyond memorizing examples
- Works well as a baseline for many tabular problems

## Limitations
- Sensitive to the scale of the features
- Slow on large datasets because every prediction compares against all training points
- Performance depends strongly on the chosen $k$

## Common mistakes
- Ignoring feature scaling when distances are computed
- Choosing a very small or very large $k$
- Forgetting that KNN is instance-based, not parameter-based

## Revision questions
1. What does “nearest neighbors” mean in KNN?
2. Why is distance measure important in KNN?
3. How does changing $k$ affect the model?
4. Why is feature scaling often necessary for KNN?

## Source reference
- Transcript title: "What is K Nearest Neighbors_ _ KNN Explained in Hindi _ Simple Overview in 1 Video _ CampusX"
- File: `091 - 2023-05-23 - What is K Nearest Neighbors_ _ KNN Explained in Hindi _ Simple Overview in 1 Video _ CampusX.txt`
