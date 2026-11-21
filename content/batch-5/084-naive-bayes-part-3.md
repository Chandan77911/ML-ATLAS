# 84 — Naive Bayes Classifier Part 3

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 84
- Transcript title: "Naive Bayes Classifier _ Part 3 _ Mutually Exclusive Events"
- Transcript file: `084 - 2020-03-14 - Naive Bayes Classifier _ Part 3 _ Mutually Exclusive Events.txt`
- Topic: Mutually Exclusive Events

## Learning objectives
- Explain the main idea behind naive bayes classifier part 3.
- Connect the concept with the original CampusX sequence.
- Describe the mathematics or geometry behind the method.
- Show a practical Python example.

## Original CampusX concept
Mutual exclusivity explains why probabilities for disjoint events do not overlap and how this supports probability decomposition.

## Why this matters
Mutually exclusive events are the opposite of independent events: they cannot happen together, and that matters when we reason about unions and probabilities.

## Intuition
If a coin lands heads, it cannot land tails at the same time. This is the simplest example of mutually exclusive outcomes.

## Mathematical view
For mutually exclusive events $A$ and $B$:

$$
P(A \cap B) = 0
$$

and therefore:

$$
P(A \cup B) = P(A) + P(B)
$$

This differs from independence, where $P(A \cap B) = P(A)P(B)$.

## Python example
```python
outcomes = {1, 2, 3, 4, 5, 6}
A = {2, 4, 6}
B = {1, 3, 5}

p_a = len(A) / len(outcomes)
p_b = len(B) / len(outcomes)
print('P(A):', round(p_a, 3))
print('P(B):', round(p_b, 3))
print('P(A and B):', 0)
print('P(A or B):', round(p_a + p_b, 3))
```

Expected output:
```text
P(A): 0.5
P(B): 0.5
P(A and B): 0
P(A or B): 1.0
```

## Advantages
- Clarifies a common probability confusion
- Helps distinguish disjoint events from independent ones
- Builds a useful concept for probability-based classifiers

## Limitations
- Many real-world events are not mutually exclusive
- Overusing this rule can be wrong when overlap exists
- It is only one piece of the probability toolbox

## Common mistakes
- Assuming mutually exclusive events are automatically independent
- Forgetting that the intersection is zero
- Mixing up union and intersection formulas

## Revision questions
1. What does it mean for two events to be mutually exclusive?
2. Why is $P(A \cap B)=0$ important?
3. How is mutual exclusivity different from independence?
4. Why is this idea relevant in probabilistic ML?

## Source reference
- Transcript title: "Naive Bayes Classifier _ Part 3 _ Mutually Exclusive Events"
- File: `084 - 2020-03-14 - Naive Bayes Classifier _ Part 3 _ Mutually Exclusive Events.txt`
