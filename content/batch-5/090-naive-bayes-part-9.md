# 90 — Naive Bayes Part 9

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 90
- Transcript title: "Naive Bayes Part 9 _ Handling Numerical Data"
- Transcript file: `090 - 2020-04-27 - Naive Bayes Part 9 _ Handling Numerical Data.txt`
- Topic: Handling Numerical Data

## Learning objectives
- Explain the main idea behind naive bayes part 9.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Numerical features need Gaussian or continuous likelihood estimates instead of simple counts or categorical frequency tables.

## Why this matters
Real data often contains continuous values, so Naive Bayes needs a way to score a numeric feature under each class instead of using only category counts.

## Intuition
If we know the average and spread of a feature within each class, then a new value can be scored by how typical it is for that class. This is the continuous-feature version of Naive Bayes.

## Mathematical view
For a continuous feature $x_i$, a common model is a Gaussian likelihood:

$$
P(x_i \mid y) = \frac{1}{\sqrt{2\pi\sigma_y^2}}\exp\left(-\frac{(x_i - \mu_y)^2}{2\sigma_y^2}\right)
$$

where:
- $\mu_y$ = mean of the feature within class $y$
- $\sigma_y^2$ = variance of that feature within class $y$

Then the prediction remains:

$$
\hat{y} = \arg\max_y P(y)\prod_i P(x_i \mid y)
$$

## Python example
```python
from math import sqrt, pi, exp

mu_class_a = 10.0
var_class_a = 4.0
mu_class_b = 18.0
var_class_b = 9.0
x = 12.0

def gaussian_pdf(x_value, mean, variance):
    return (1 / (sqrt(2 * pi * variance))) * exp(-((x_value - mean) ** 2) / (2 * variance))

score_a = gaussian_pdf(x, mu_class_a, var_class_a)
score_b = gaussian_pdf(x, mu_class_b, var_class_b)

print('p(x|A):', round(score_a, 4))
print('p(x|B):', round(score_b, 4))
print('Likely class:', 'A' if score_a > score_b else 'B')
```

Expected output:
```text
p(x|A): 0.1210
p(x|B): 0.0358
Likely class: A
```

## Advantages
- Handles numerical features naturally
- Keeps classification simple and interpretable
- Extends Naive Bayes beyond purely categorical data

## Limitations
- Assumes a distribution for continuous features such as Gaussian
- Still relies on the naive independence assumption
- Poor class statistics can reduce accuracy

## Common mistakes
- Treating continuous values as if they were categorical
- Ignoring the variance when scoring a numeric likelihood
- Overestimating the quality of the independence assumption

## Revision questions
1. Why do we need a different treatment for numerical features?
2. What does the Gaussian likelihood model?
3. How does the class-conditional density affect the final prediction?
4. Why is Naive Bayes still an approximation even with continuous features?

## Source reference
- Transcript title: "Naive Bayes Part 9 _ Handling Numerical Data"
- File: `090 - 2020-04-27 - Naive Bayes Part 9 _ Handling Numerical Data.txt`
