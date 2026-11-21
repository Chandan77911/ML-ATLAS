# 93 — SVM Hard Margin

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 93
- Transcript title: "Mathematics of SVM _ Support Vector Machines _ Hard margin SVM"
- Transcript file: `093 - 2020-07-10 - Mathematics of SVM _ Support Vector Machines _ Hard margin SVM.txt`
- Topic: Mathematics of hard-margin SVM

## Learning objectives
- Explain the main idea behind svm hard margin.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
The hard-margin formulation maximizes the margin under the constraint that all points are correctly classified.

## Why this matters
The hard-margin SVM assumes the data are linearly separable and aims to find the boundary with the largest possible margin while classifying every point correctly.

## Intuition
If the classes are perfectly separable, the best boundary is the one that keeps the training points farthest away. This gives the strongest geometric separation before any noise or overlap is considered.

## Mathematical view
The optimization problem is:

$$
\min_{w,b} \frac{1}{2}\|w\|^2
$$

subject to:

$$
 y_i(w^T x_i + b) \geq 1 \quad \forall i
$$

This is a convex optimization problem, and the solution depends only on support vectors. The larger the margin, the less likely the classifier is to overfit in simple separable settings.

## Python example
```python
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

X, y = make_blobs(n_samples=120, centers=2, cluster_std=0.7, random_state=0)
model = SVC(kernel='linear', C=1000)
model.fit(X, y)

print('Training accuracy:', round(model.score(X, y), 3))
print('Number of support vectors:', len(model.support_vectors_))
```

Expected output:
```text
Training accuracy: 1.0
Number of support vectors: 2
```

## Advantages
- Clear interpretation as maximum-margin separation
- Strong geometric intuition
- Excellent for clean, linearly separable data

## Limitations
- Requires linear separability for the strict formulation
- Sensitive to outliers and noisy labels
- Real-world data often violate the hard-margin assumption

## Common mistakes
- Applying hard margin to data that are not cleanly separable
- Forgetting that the solution is defined by support vectors
- Ignoring the role of the margin in stability and generalization

## Revision questions
1. What does “hard margin” mean in SVM?
2. Why is the optimization problem written in terms of minimizing $\|w\|^2$?
3. What happens when the data are not linearly separable?
4. Why are support vectors important in the hard-margin solution?

## Source reference
- Transcript title: "Mathematics of SVM _ Support Vector Machines _ Hard margin SVM"
- File: `093 - 2020-07-10 - Mathematics of SVM _ Support Vector Machines _ Hard margin SVM.txt`
