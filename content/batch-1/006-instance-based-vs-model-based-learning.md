# 006 — Instance-Based vs Model-Based Learning

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 006
- Transcript title: "Instance-Based Vs Model-Based Learning | Types of Machine Learning"
- Transcript file: `006 - 2021-03-19 - Instance-Based Vs Model-Based Learning _ Types of Machine Learning.txt`
- Topic: model families
- Subtopic: instance-based learning vs model-based learning

## Original CampusX concept

The instructor compares two broad ways that machine learning models learn:

- Instance-based learning: the model memorizes training examples and makes predictions by comparing new examples to stored ones
- Model-based learning: the model tries to learn a general rule or pattern from the data

This distinction is extremely useful because it explains why some algorithms behave more like “memory systems” and others behave more like mathematical models.

### Beginner intuition

Instance-based learning is like using a reference book of prior examples. If a new case is similar to a known one, you predict the same result.

Model-based learning is like learning the underlying formula behind the examples. You do not need to keep every example in memory to make a decision.

### Technical understanding

A classic instance-based method is KNN. Given a new point $x$, the algorithm finds the nearest neighbors in the training set and uses their labels to decide.

A common distance metric is Euclidean distance:

$$
d(x, x_i) = \sqrt{\sum_{j=1}^{m} (x_j - x_{ij})^2}
$$

where:

- $x$ is the new point
- $x_i$ is a training example
- $m$ is the number of features

The model then uses the nearest examples to classify or regress.

By contrast, model-based learning estimates parameters. For example, linear regression learns coefficients that best describe the relationship between inputs and outputs.

## IMPORTANT TERMS EXPLAINED

- Instance-based learning: learning by storing and comparing examples
- Model-based learning: learning a parameterized rule or structure
- Neighborhood: nearby training examples used for a prediction
- Distance metric: a way to measure similarity between examples
- Parameterized model: a model described by learned coefficients or weights

## SUPPLEMENTARY: Why this distinction matters

This classification is very practical:

- If the decision depends strongly on local similarity, instance-based approaches may be useful.
- If the data has a global structure, model-based methods are often more efficient and interpretable.

It also explains why KNN can be simple but memory-heavy, while linear models are compact but more assumption-driven.

## INTERVIEW EXTENSION

Q: What is a classic example of instance-based learning?

A: K-nearest neighbors.

Q: Why is model-based learning often more scalable?

A: Because it stores learned parameters rather than all training examples.

Q: Which type is more interpretable in general?

A: Model-based learning is often more interpretable because it has a clear mathematical form.

## Practical Python example

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print(round(model.score(X_test, y_test), 3))
```

Expected output (approximate):

```text
0.974
```

### Why this matters

KNN is the standard instance-based example. It matches the transcript's intuition: classify a new point based on nearby examples.

## COMMON MISTAKES AND MISCONCEPTIONS

- Thinking all algorithms follow a single learning philosophy
- Forgetting that KNN stores examples and does not fit a compact model
- Using KNN when the dataset is large and high-dimensional without considering scaling
- Assuming model-based methods are always better; they may be worse when the underlying pattern is very local

## Practice

1. Give one example of instance-based learning and one example of model-based learning.
2. When would KNN be a good choice?
3. What is the trade-off between memory usage and model simplicity?
4. Explain what a distance metric is in your own words.

## Code-to-practice mapping

- Original concept: memory-based vs pattern-based learning
- Supplementary concept: distance metric and model form
- Code: KNN classification example
- Practice: choosing between instance-based and model-based approaches
