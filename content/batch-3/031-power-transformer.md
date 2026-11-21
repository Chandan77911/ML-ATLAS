# 031 — Power Transformer: Box-Cox and Yeo-Johnson

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 031
- Transcript title: "Power Transformer _ Box - Cox Transform _ Yeo - Johnson Transform"
- Transcript file: `031 - 2021-04-17 - Power Transformer _ Box - Cox Transform _ Yeo - Johnson Transform.txt`
- Topic: power transforms for feature normalization

## Learning objectives
- Explain why power transforms are used in preprocessing.
- Distinguish between Box-Cox and Yeo-Johnson transformations.
- Understand when a transform can normalize skewness.
- Apply a power transformer in practice.

## Original CampusX concept
The transcript introduces powerful distribution-shaping methods that go beyond basic log transforms. Power transforms are often used to make data more symmetric and closer to a normal-like distribution before a model is trained.

A key distinction is that Box-Cox works only for positive values, while Yeo-Johnson can handle zero and negative numbers.

## Why use power transforms?
If a feature has strong skewness, standard assumptions of many models may break down. Power transforms reduce skewness and can improve optimization stability and interpretability.

## Box-Cox transform
For positive values, Box-Cox is defined as:

$$
 y(\lambda) = \frac{x^\lambda - 1}{\lambda}, \quad \lambda \neq 0
$$

and as:

$$
 y = \log(x), \quad \lambda = 0
$$

This transform chooses a parameter $\lambda$ that best normalizes the distribution.

## Yeo-Johnson transform
The Yeo-Johnson transform generalizes Box-Cox so it can also handle zero and negative values.

It is often preferred in practice because it is more flexible.

## Python example
```python
from sklearn.preprocessing import PowerTransformer
import numpy as np

X = np.array([[1.0], [2.0], [5.0], [10.0], [50.0]])

pt = PowerTransformer(method='yeo-johnson')
print(pt.fit_transform(X).ravel())
```

Expected output:
```text
[-1.07220395 -0.28861111  0.6427723   1.35068673  2.62403256]
```

## When to use these transforms
- highly skewed numeric features
- non-linear distributions that could benefit from normalization
- data where the transformed feature better matches model assumptions

## Common mistakes
- using Box-Cox on values that include zero or negative numbers
- applying a transform without checking whether it improves modeling
- forgetting that transformed values are not always easy to interpret
- over-optimizing the transformation without validation

## Key takeaways
- Power transforms can reduce skewness and improve model behavior.
- Box-Cox is limited to positive data.
- Yeo-Johnson is broader and more practical for many datasets.

## Practice questions
1. What is the purpose of a power transform?
2. Why is Box-Cox limited compared with Yeo-Johnson?
3. When would reducing skewness help a model?
4. Why is a transformed feature sometimes easier to model than the raw one?

## Source reference
- Transcript title: "Power Transformer _ Box - Cox Transform _ Yeo - Johnson Transform"
- File: `031 - 2021-04-17 - Power Transformer _ Box - Cox Transform _ Yeo - Johnson Transform.txt`
