# 86 — Naive Bayes Classifier Part 5

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 86
- Transcript title: "Naive Bayes Classifier _ Part 5 _ Problem based upon Bayes Theorem"
- Transcript file: `086 - 2020-03-14 - Naive Bayes Classifier _ Part 5 _ Problem based upon Bayes Theorem.txt`
- Topic: Problem Solving with Bayes Theorem

## Learning objectives
- Explain the main idea behind naive bayes classifier part 5.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
The lesson converts the formula into a practical decision rule for choosing the most likely class.

## Why this matters
This lesson turns Bayes theorem into a decision rule: for each possible class, compute its posterior probability and pick the class with the largest value.

## Intuition
If we know the prior chance of a class and the chance of observing the feature under that class, we can compare the two class scores. The class with the higher posterior is the more likely label.

## Mathematical view
The classifier uses:

$$
\hat{y} = \arg\max_y P(y \mid x)
$$

and, via Bayes theorem,

$$
P(y \mid x) = \frac{P(x \mid y)P(y)}{P(x)}
$$

Because $P(x)$ is constant across classes, the decision reduces to comparing:

$$
P(y)P(x \mid y)
$$

## Python example
```python
p_class_a = 0.6
p_class_b = 0.4
p_feature_given_a = 0.8
p_feature_given_b = 0.3

posterior_a = p_class_a * p_feature_given_a
posterior_b = p_class_b * p_feature_given_b

print('Posterior A:', round(posterior_a, 4))
print('Posterior B:', round(posterior_b, 4))
print('Most likely class:', 'A' if posterior_a > posterior_b else 'B')
```

Expected output:
```text
Posterior A: 0.48
Posterior B: 0.12
Most likely class: A
```

## Advantages
- Makes probabilistic predictions concrete and interpretable
- Provides the decision rule that underlies Naive Bayes
- Connects math to a simple classification action

## Limitations
- Assumes the class-conditional probabilities are known or estimated accurately
- The naive independence assumption still matters for multi-feature cases
- Rare evidence can reduce robustness if not smoothed

## Common mistakes
- Computing the wrong probability when comparing classes
- Ignoring the prior probability
- Forgetting that the denominator is the same for all classes

## Revision questions
1. Why is prediction based on posterior probability sensible?
2. What is the role of the class prior?
3. Why can the denominator be ignored during comparison?
4. How would you extend this idea to multiple features?

## Source reference
- Transcript title: "Naive Bayes Classifier _ Part 5 _ Problem based upon Bayes Theorem"
- File: `086 - 2020-03-14 - Naive Bayes Classifier _ Part 5 _ Problem based upon Bayes Theorem.txt`
