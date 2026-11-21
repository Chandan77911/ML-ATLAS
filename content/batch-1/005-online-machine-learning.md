# 005 — Online Machine Learning

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 005
- Transcript title: "Online Machine Learning | Online Learning | Online Vs Offline Machine Learning"
- Transcript file: `005 - 2021-03-18 - Online Machine Learning _ Online Learning _ Online Vs Offline Machine Learning.txt`
- Topic: training paradigms
- Subtopic: online learning and incremental updates

## Original CampusX concept

The transcript focuses on the streaming nature of online learning: as new data arrives, the model keeps updating itself. Instead of retraining from scratch, it learns incrementally from a constant stream of examples.

This is the operational version of the idea introduced in lesson 004. The model is not merely trained in a different mode; it is designed to keep improving in production as user behavior and system inputs change.

### Beginner intuition

Online learning is like updating your understanding after every new experience, rather than waiting until the end of a year to study everything together.

### Technical understanding

In online learning, the model sees one example or a small chunk of examples at a time and updates its parameters immediately. This is often called incremental learning or streaming learning.

It is useful when:

- data arrives continuously
- user behavior shifts over time
- the system must adapt quickly without full retraining

## IMPORTANT DISTINCTION: 004 vs 005

Lesson 004 explains the broad distinction between batch and online learning.

Lesson 005 explains the mechanics of online learning in real systems:

- streaming updates
- continued learning after deployment
- adaptation to changing user behavior
- concept drift and evolving data distributions

So, 004 answers “what are the two training modes?”, while 005 answers “how does online learning actually behave in production?”

## SUPPLEMENTARY: Why concept drift matters

The transcript's practical examples (keyboard prediction, recommendations, personalization) make an important point: user behavior changes over time. A model trained on older data may become less useful if the underlying behavior shifts.

This is called concept drift: the real relationship between inputs and outputs changes over time.

## INTERVIEW EXTENSION

Q: Why is online learning useful in recommendation systems?

A: Because user interests change over time and the model needs to adapt continuously.

Q: What is concept drift?

A: A change in the underlying pattern or distribution of the data over time.

Q: Is online learning always better than batch learning?

A: No. It is better when the data stream is continuous and the model must keep adapting, but not always necessary for stable environments.

## Practical Python example

```python
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
model = SGDClassifier(loss='log_loss', random_state=42)

# Simulate a streaming environment by updating the model incrementally
for start in range(0, len(X), 100):
    stop = start + 100
    model.partial_fit(X[start:stop], y[start:stop], classes=[0, 1])

print(round(model.score(X, y), 3))
```

Expected output (approximate):

```text
0.86
```

### Why this matters

This example demonstrates incremental learning: the model is updated in several steps rather than trained once on the full dataset.

## COMMON MISTAKES AND MISCONCEPTIONS

- Thinking online learning is the default mode for all ML systems
- Forgetting that online learning needs monitoring and validation
- Ignoring that the data distribution may change over time
- Assuming “continuous learning” automatically means “better performance”

## Practice

1. Explain online learning using a real-world product example.
2. Why is online learning helpful for rapidly changing user behavior?
3. Compare online learning to a periodic retraining pipeline.
4. Explain the idea of concept drift in your own words.

## Code-to-practice mapping

- Original concept: incremental model updates with new data
- Supplementary concept: drift, adaptation, and streaming environments
- Code: SGDClassifier with partial_fit
- Practice: understanding online adaptation in production settings
