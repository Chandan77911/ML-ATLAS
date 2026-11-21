# 119 — Bagging vs Boosting

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 119
- Transcript title: "Bagging Vs Boosting _ What is the difference between Bagging and Boosting"
- Transcript file: `119 - 2021-08-18 - Bagging Vs Boosting _ What is the difference between Bagging and Boosting.txt`
- Topic: Ensemble comparison

## Learning objectives
- Explain the main idea behind bagging vs boosting.
- Connect the concept to the original CampusX sequence.
- Show the geometry, math, or algorithm behind the method.
- Give a practical Python example.

## Original CampusX concept
Bagging reduces variance through parallel averaging, while boosting reduces bias through sequential correction.

## Why it matters
Ensemble learning is one of the most important ideas in machine learning because it turns weak or unstable models into a stronger prediction system.

## Intuition
Each model sees the data from a slightly different perspective. By combining them, the ensemble can reduce variance, capture more patterns, and smooth individual mistakes.

## Core logic
The ensemble prediction is often a weighted or averaged combination of base learners:

prediction = average or weighted vote of multiple models

This is the key design principle behind bagging, boosting, and stacking.

## Mathematical view
If base models are f1, f2, ... fk, then a simple ensemble is:

F(x) = (1/k) * sum(f_i(x))

For weighted ensembles:

F(x) = sum(w_i * f_i(x))

where weights w_i reflect the importance or trust assigned to each learner.

## Python example
```python
import numpy as np

preds = np.array([1, 0, 1, 1, 0])
print('Average vote:', preds.mean())
```

Expected output:
```text
Average vote: 0.6
```

## Advantages
- Better stability than a single weak model.
- Often improves generalization on tabular tasks.
- Makes model performance less sensitive to a single bad fit.

## Limitations
- Can be more computationally expensive.
- Harder to interpret than a single decision tree.
- Performance still depends on base model quality and tuning.

## Common mistakes
- Combining models without checking validation performance.
- Ignoring class imbalance or feature scaling.
- Using too many weak learners without measuring the gain.

## Revision questions
1. What is the main benefit of combining multiple learners?
2. Why do ensemble methods often outperform a single model?
3. How does a voting ensemble differ from a boosting ensemble?
4. What should be validated before choosing an ensemble strategy?

## Source reference
- Transcript title: "Bagging Vs Boosting _ What is the difference between Bagging and Boosting"
- File: `119 - 2021-08-18 - Bagging Vs Boosting _ What is the difference between Bagging and Boosting.txt`
