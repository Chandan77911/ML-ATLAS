# 88 — Naive Bayes Classifier Part 7

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 88
- Transcript title: "Naive Bayes Classifier _ Part 7 _ Mathematics behind Naive Bayes Algorithm"
- Transcript file: `088 - 2020-03-14 - Naive Bayes Classifier _ Part 7 _ Mathematics behind Naive Bayes Algorithm.txt`
- Topic: Naive Bayes Mathematics

## Learning objectives
- Explain the main idea behind naive bayes classifier part 7.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
The class-posterior probability is estimated from class priors and feature likelihoods under the conditional independence assumption.

## Why this matters
This is the actual mathematical form of Naive Bayes: the model multiplies the class prior by the probability of each feature under the class and then picks the best class.

## Intuition
Imagine each feature contributes evidence for or against a class. Naive Bayes combines those clues by multiplying them, which is why the model is especially interpretable when features are reasonably independent.

## Mathematical view
The class-posterior is:

$$
P(y \mid x_1, x_2, \dots, x_n) = \frac{P(y)\prod_{i=1}^{n} P(x_i \mid y)}{P(x_1, x_2, \dots, x_n)}
$$

The naive assumption is:

$$
P(x_1, x_2, \dots, x_n \mid y) \approx \prod_{i=1}^{n} P(x_i \mid y)
$$

The model predicts:

$$
\hat{y} = \arg\max_y P(y)\prod_i P(x_i \mid y)
$$

## Python example
```python
class_prior = {'A': 0.6, 'B': 0.4}
feature_likelihood = {
    'A': {'x1': 0.8, 'x2': 0.7},
    'B': {'x1': 0.3, 'x2': 0.9},
}

x_obs = {'x1': 1, 'x2': 0}
score_a = class_prior['A'] * feature_likelihood['A']['x1'] * (1 - feature_likelihood['A']['x2'])
score_b = class_prior['B'] * feature_likelihood['B']['x1'] * (1 - feature_likelihood['B']['x2'])

print('Score A:', round(score_a, 4))
print('Score B:', round(score_b, 4))
print('Predicted class:', 'A' if score_a > score_b else 'B')
```

Expected output:
```text
Score A: 0.336
Score B: 0.108
Predicted class: A
```

## Advantages
- Very fast to train and predict
- Produces probability-based class comparisons
- Works well for text-heavy and categorical problems

## Limitations
- The independence assumption is often a simplification
- Zero probabilities can cause issues without smoothing
- Correlated features may reduce performance

## Common mistakes
- Forgetting that the class prior matters
- Ignoring the feature independence assumption
- Comparing raw counts instead of class-conditional likelihoods

## Revision questions
1. Why is Naive Bayes called naive?
2. What does the product of probabilities represent in the formula?
3. Why is the class prior included in the decision?
4. How does this formula differ from a simple classification rule?

## Source reference
- Transcript title: "Naive Bayes Classifier _ Part 7 _ Mathematics behind Naive Bayes Algorithm"
- File: `088 - 2020-03-14 - Naive Bayes Classifier _ Part 7 _ Mathematics behind Naive Bayes Algorithm.txt`
