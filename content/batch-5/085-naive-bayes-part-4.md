# 85 — Naive Bayes Classifier Part 4

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 85
- Transcript title: "Naive Bayes Classifier _ Part 4 _ Bayes Theorem in Probability"
- Transcript file: `085 - 2020-03-14 - Naive Bayes Classifier _ Part 4 _ Bayes Theorem in Probability.txt`
- Topic: Bayes Theorem

## Learning objectives
- Explain the main idea behind naive bayes classifier part 4.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Bayes theorem updates prior beliefs with evidence and is central to the posterior probability used by Naive Bayes.

## Why this matters
Bayes theorem is the engine behind probabilistic classification: it tells us how to revise our belief in a class after seeing evidence.

## Intuition
A doctor may start with a prior suspicion of disease. After seeing a test result, the posterior probability may increase or decrease. That update is exactly what Bayes theorem formalizes.

## Mathematical view
The theorem is:

$$
P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}
$$

where:
- $A$ = class or hypothesis
- $B$ = observed evidence
- $P(A)$ = prior probability
- $P(B \mid A)$ = likelihood
- $P(B)$ = evidence term
- $P(A \mid B)$ = posterior probability

## Python example
```python
p_disease = 0.01
p_positive_given_disease = 0.9
p_positive_given_no_disease = 0.1

p_positive = (
    p_disease * p_positive_given_disease
    + (1 - p_disease) * p_positive_given_no_disease
)
p_disease_given_positive = (
    p_positive_given_disease * p_disease / p_positive
)

print('P(Disease):', p_disease)
print('P(Positive):', round(p_positive, 4))
print('P(Disease | Positive):', round(p_disease_given_positive, 4))
```

Expected output:
```text
P(Disease): 0.01
P(Positive): 0.108
P(Disease | Positive): 0.0833
```

## Advantages
- Provides a principled update rule for uncertain beliefs
- Gives a clean bridge from probability theory to classification
- Works naturally with prior information and observed evidence

## Limitations
- Requires a valid probability model for the evidence
- The formulation can be poor if the assumptions are wrong
- A weak prior or poor likelihood estimate leads to weak posterior inference

## Common mistakes
- Confusing prior, likelihood, and posterior
- Forgetting to normalize by $P(B)$
- Using Bayes theorem without clearly defining the evidence

## Revision questions
1. What is the difference between a prior and a posterior?
2. Why is Bayes theorem useful in ML classification?
3. What does the denominator $P(B)$ do in the formula?
4. How does this connect to Naive Bayes?

## Source reference
- Transcript title: "Naive Bayes Classifier _ Part 4 _ Bayes Theorem in Probability"
- File: `085 - 2020-03-14 - Naive Bayes Classifier _ Part 4 _ Bayes Theorem in Probability.txt`
