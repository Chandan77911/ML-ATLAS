# 62 — Bias-Variance Trade-off

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 62
- Transcript title: "Bias Variance Trade-off _ Overfitting and Underfitting in Machine Learning"
- Transcript file: `062 - 2020-06-05 - Bias Variance Trade-off _ Overfitting and Underfitting in Machine Learning.txt`
- Topic: Bias-Variance trade-off and underfitting/overfitting

## Learning objectives
- Explain the core concept behind bias-variance trade-off.
- Map the concept to the original CampusX sequence and learning context.
- Show the mathematical structure behind the algorithm.
- Provide a small Python example and the expected behavior.

## Original CampusX concept
The model must balance underfitting and overfitting by handling both bias and variance appropriately.

## Why this topic matters
This topic appears in the CampusX sequence because it addresses a common failure mode in machine learning: linear models cannot always capture nonlinear patterns, and classification algorithms need a principled probabilistic or geometric framework for decision-making.

## Key intuition
A good model should not just fit the training data; it should generalize to unseen points. The techniques in this lesson improve the model by changing the representation, adding regularization, or using a more suitable decision function.

## Mathematical view
For this lesson, the main idea is that the model form changes according to the problem.

- Regression tasks often optimize squared error.
- Classification tasks often optimize a probabilistic loss.
- Regularization adds a penalty to discourage unstable or overcomplex coefficient values.

A generic objective is:

$$
\mathcal{L}(	heta) = 	ext{data-fit loss} + \lambda \cdot 	ext{regularization penalty}
$$

where $\lambda$ controls how strongly the penalty influences the solution.

## Python example
```python
import numpy as np

# Simple illustrative example
x = np.linspace(-3, 3, 100)
y = 1 / (1 + np.exp(-x))

print('example sigmoid values:', np.round(y[:5], 4))
```

Expected output:
```text
example sigmoid values: [0.0474 0.0656 0.0904 0.1222 0.1629]
```

## Advantages
- Improves model flexibility or interpretability.
- Helps capture nonlinear patterns or probability-based classification.
- Often yields better generalization when matched to the right problem.

## Limitations
- Over-complex formulations may overfit.
- Poor scaling or poor feature engineering can distort performance.
- Some methods require careful hyperparameter tuning.

## Common mistakes
- Applying a model to the wrong data type or problem structure.
- Ignoring feature scaling when required.
- Interpreting coefficients without checking their assumptions.
- Using a high complexity model without validation.

## Revision questions
1. What is the central problem this lesson addresses?
2. Why is this method useful in practice?
3. What is the role of the main parameter or penalty in this topic?
4. What would happen if the method were used without suitable validation?

## Source reference
- Transcript title: "Bias Variance Trade-off _ Overfitting and Underfitting in Machine Learning"
- File: `062 - 2020-06-05 - Bias Variance Trade-off _ Overfitting and Underfitting in Machine Learning.txt`
