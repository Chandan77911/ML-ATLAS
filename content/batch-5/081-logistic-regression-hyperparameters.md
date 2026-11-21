# 81 — Logistic Regression Hyperparameters

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 81
- Transcript title: "Logistic Regression Hyperparameters _ Logistic Regression Part 8"
- Transcript file: `081 - 2021-06-30 - Logistic Regression Hyperparameters _ Logistic Regression Part 8.txt`
- Topic: Logistic Regression Hyperparameters

## Learning objectives
- Explain the main idea behind logistic regression hyperparameters.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
This lesson is about the settings that control how a logistic regression model learns. In practice, the model is still a sigmoid-based classifier, but the learning behavior changes depending on the regularization strength, optimization settings, and class-handling choices used during training.

## Why this matters
Hyperparameters are not the model itself; they are the knobs that determine how strongly the model fits the training data and how stable it remains on unseen data. In logistic regression, this often means balancing fit quality against overfitting and numerical stability.

## Intuition
A logistic regression model tries to learn a decision boundary in a way that separates the classes as well as possible. If the model is too aggressive, large weights may overfit the training set; if the model is too conservative, it may underfit. Hyperparameters such as regularization strength and iteration limits help control that trade-off.

## Mathematical view
The classifier uses the sigmoid function:

$$
P(y=1\mid x) = \sigma(w^T x + b) = \frac{1}{1 + e^{-(w^T x + b)}}
$$

The model is typically trained by minimizing a cross-entropy loss, often with a penalty term:

$$
\min_{w,b} \sum_{i=1}^{n} \text{CrossEntropy}(y_i, \sigma(w^T x_i + b)) + \lambda \|w\|^2
$$

where:
- $w$ = model weights
- $b$ = bias term
- $\lambda$ = regularization strength
- $\|w\|^2$ = penalty on large weights

In scikit-learn, the regularization strength is often controlled by $C$, where smaller $C$ means stronger regularization. This is one of the main hyperparameters discussed in the lesson.

## Python example
```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=300,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    random_state=0,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

clf = LogisticRegression(max_iter=1000, C=1.0, random_state=0)
clf.fit(X_train, y_train)

print('coef_shape:', clf.coef_.shape)
print('train_accuracy:', round(clf.score(X_train, y_train), 3))
print('test_accuracy:', round(clf.score(X_test, y_test), 3))
```

Expected output:
```text
coef_shape: (1, 5)
train_accuracy: 0.943
test_accuracy: 0.9
```

## Advantages
- Keeps the same core logistic-regression intuition while controlling fit quality
- Helps handle noisy or high-dimensional data through regularization
- Very common in production classification pipelines

## Limitations
- Hyperparameter tuning requires validation and can be sensitive to data scale
- A poor choice of solver or regularization strength can underfit or overfit
- Logistic regression still assumes a roughly linear decision boundary in the feature space unless transformed data are used

## Common mistakes
- Treating hyperparameters as magic values without validation
- Ignoring feature scaling when using optimization-based models
- Changing many settings at once without understanding the bias-variance trade-off

## Revision questions
1. What does a regularization hyperparameter change in logistic regression?
2. Why is a smaller or larger regularization strength not always better?
3. How do optimization settings affect convergence and model stability?
4. What evidence would you use to choose a good hyperparameter value?

## Source reference
- Transcript title: "Logistic Regression Hyperparameters _ Logistic Regression Part 8"
- File: `081 - 2021-06-30 - Logistic Regression Hyperparameters _ Logistic Regression Part 8.txt`
