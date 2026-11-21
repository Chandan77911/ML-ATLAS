# 82 — Naive Bayes Classifier Part 1

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 82
- Transcript title: "Naive Bayes Classifier _ Part 1 _ Conditional Probability"
- Transcript file: `082 - 2020-03-14 - Naive Bayes Classifier _ Part 1 _ Conditional Probability.txt`
- Topic: Conditional Probability

## Learning objectives
- Explain the main idea behind naive bayes classifier part 1.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
This lesson introduces conditional probability: the probability of one event happening given that another event has already happened.

## Why this matters
Naive Bayes is built on conditional probability. The core idea is that the probability of a class given observed features depends on how likely those features are under each class.

## Intuition
If a die is rolled and we already know the total is at most 10, then the sample space shrinks. The probability of one outcome is no longer the same as before. This is exactly what conditional probability formalizes.

## Mathematical view
For two events $A$ and $B$, the conditional probability is:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) \neq 0
$$

where:
- $A$ = event of interest
- $B$ = known condition or evidence
- $P(A \cap B)$ = probability that both events happen together
- $P(B)$ = probability of the condition that restricts the sample space

This is the foundation of Bayes' theorem and the Naive Bayes classifier.

## Python example
```python
# Two-dice conditional-probability example
import itertools

outcomes = list(itertools.product(range(1, 7), repeat=2))
D1_plus_D2_leq_10 = [pair for pair in outcomes if pair[0] + pair[1] <= 10]
D1_equals_5 = [pair for pair in D1_plus_D2_leq_10 if pair[0] == 5]

p_a_given_b = len(D1_equals_5) / len(D1_plus_D2_leq_10)
print('Number of outcomes where D1 + D2 <= 10:', len(D1_plus_D2_leq_10))
print('Number of outcomes where D1=5 and D1+D2<=10:', len(D1_equals_5))
print('P(D1=5 | D1+D2<=10):', round(p_a_given_b, 4))
```

Expected output:
```text
Number of outcomes where D1 + D2 <= 10: 33
Number of outcomes where D1=5 and D1+D2<=10: 5
P(D1=5 | D1+D2<=10): 0.1515
```

## Advantages
- Gives a principled way to update probabilities after new evidence arrives
- Forms the mathematical foundation for Bayes-based classifiers
- Helps explain why prior information matters in prediction

## Limitations
- It is only meaningful when the event space and condition are defined carefully
- It can be misapplied when the dependence structure between variables is ignored
- In a real model, simple probability rules are not enough without a sensible generative assumption

## Common mistakes
- Confusing $P(A \mid B)$ with $P(B \mid A)$
- Forgetting that the denominator is the probability of the condition
- Using conditional probability without checking that $P(B) > 0$

## Revision questions
1. What does $P(A \mid B)$ mean in plain language?
2. Why does the sample space shrink when a condition is given?
3. How is this idea used in Naive Bayes classification?
4. Can you compute a simple conditional probability from a small example?

## Source reference
- Transcript title: "Naive Bayes Classifier _ Part 1 _ Conditional Probability"
- File: `082 - 2020-03-14 - Naive Bayes Classifier _ Part 1 _ Conditional Probability.txt`
