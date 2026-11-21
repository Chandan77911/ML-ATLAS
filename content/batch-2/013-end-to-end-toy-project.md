# 013 — End-to-End Toy Project

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 013
- Transcript title: "End to End Toy Project _ Day 13 _ 100 Days of Machine Learning"
- Transcript file: `013 - 2021-03-27 - End to End Toy Project _ Day 13 _ 100 Days of Machine Learning.txt`
- Topic: project workflow
- Subtopic: end-to-end toy machine learning project

## Original CampusX concept

The transcript introduces the idea of building a small ML project from start to finish. The goal is not to memorize algorithms but to understand the complete pipeline: data loading, exploration, preprocessing, modeling, and evaluation.

### Beginner intuition

A toy project is a mini version of a real ML project. It is small enough to understand but complete enough to show the flow of work.

### Technical understanding

A simple project typically follows this structure:

1. import data
2. inspect columns and patterns
3. split data into training and test sets
4. choose a model
5. train the model
6. evaluate the predictions
7. interpret the result

This gives a working mental model before moving into larger datasets.

## SUPPLEMENTARY: Why toy projects matter

Toy projects are important because they teach the full pipeline without making the system overly complex. They help you learn how each step interacts with the others and reveal where failures often happen.

## INTERVIEW EXTENSION

Q: Why do we build toy projects before larger ML systems?

A: They help us learn the full workflow without high project risk.

Q: What is the value of a train/test split?

A: It measures whether the model generalizes to unseen data.

## Practical Python example

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Simple toy regression task
house_data = pd.DataFrame({
    'sqft': [1000, 1200, 1500, 1800, 2100, 2400],
    'price': [150000, 180000, 220000, 260000, 300000, 350000]
})

X = house_data[['sqft']]
y = house_data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
train_pred = model.predict(X_test)
print("MSE:", round(mean_squared_error(y_test, train_pred), 2))
print("Slope:", round(model.coef_[0], 2))
```

Expected output:

```text
MSE: 675000000.0
Slope: 124.29
```

### Why this matters

This tiny example shows the whole ML pipeline in a compact form: data, train/test split, linear model, and error evaluation.

## Common mistakes

- using the whole dataset for training and testing
- ignoring the importance of evaluation metrics
- forgetting that the project must be framed around a real objective

## Practice

1. What is the purpose of a toy project?
2. Why do we split data into train and test subsets?
3. What metric would you use for a regression task?
4. Explain the difference between understanding the problem and training the model.

## Code-to-practice mapping

- Original concept: an end-to-end toy ML project workflow
- Supplementary concept: evaluation, project framing, and train/test logic
- Code: regression pipeline on a tiny dataset
- Practice: connecting steps to real project work
