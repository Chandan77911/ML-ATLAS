# 96 — Kernel Trick in SVM Code

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 96
- Transcript title: "Kernel Trick in SVM _ Code Example"
- Transcript file: `096 - 2020-08-07 - Kernel Trick in SVM _ Code Example.txt`
- Topic: Kernel trick implementation

## Learning objectives
- Explain the main idea behind kernel trick in svm code.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
A kernel function computes similarity between points without explicitly building the transformed feature space.

## Why this matters
The kernel trick is important because it lets a linear SVM behave like a nonlinear classifier without writing out an explicit high-dimensional feature transform.

## Intuition
Instead of manually creating new features, the algorithm computes how similar two points are in the transformed space. That similarity is enough to build a nonlinear boundary.

## Mathematical view
The decision function becomes:

$$
 f(x) = \sum_{i=1}^{n} \alpha_i y_i K(x_i, x) + b
$$

where $K(x_i, x)$ is the kernel function. This is the practical form used in the SVM implementation.

## Python example
```python
from sklearn.datasets import make_moons
from sklearn.svm import SVC

X, y = make_moons(n_samples=200, noise=0.15, random_state=0)
model = SVC(kernel='rbf', C=3.0, gamma='scale')
model.fit(X, y)

print('Training accuracy:', round(model.score(X, y), 3))
print('Predicted labels:', model.predict(X[:5]).tolist())
```

Expected output:
```text
Training accuracy: 0.97
Predicted labels: [1, 0, 1, 0, 1]
```

## Advantages
- Avoids explicit construction of transformed features
- Can model complex nonlinear boundaries
- Keeps the underlying linear SVM optimization largely intact

## Limitations
- Kernel and regularization parameters require tuning
- More complex than a linear model
- Harder to explain and debug compared to a simple linear boundary

## Common mistakes
- Assuming the kernel magically solves every nonlinearity issue
- Forgetting to scale the data before fitting
- Choosing over-aggressive gamma values that create overfitting

## Revision questions
1. What is the purpose of the kernel function?
2. Why does the kernel trick matter for nonlinear data?
3. How does the decision function change in the kernelized setting?
4. What is the effect of changing the kernel parameters?

## Source reference
- Transcript title: "Kernel Trick in SVM _ Code Example"
- File: `096 - 2020-08-07 - Kernel Trick in SVM _ Code Example.txt`
