# 060 — Mini-Batch Gradient Descent

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 060
- Transcript title: "Mini-Batch Gradient Descent"
- Transcript file: `060 - 2021-05-26 - Mini-Batch Gradient Descent.txt`
- Topic: parameter updates using subsets of data

## Learning objectives
- Explain mini-batch gradient descent.
- Compare it to batch and stochastic versions.
- Understand why it is the common default in deep learning.
- Know the trade-offs in computational efficiency and optimization stability.

## Definition
Mini-batch gradient descent processes a small group of samples at a time instead of the full dataset or a single example.

$$
\theta := \theta - \eta \frac{1}{m} \sum_{i \in B} \nabla L(\theta; x_i, y_i)
$$

where:
- $B$ is a mini-batch of size $m$
- $\eta$ is the learning rate

## Why it is popular
Mini-batch gradient descent does a good job balancing:
- speed
- computational efficiency
- stable updates

It is often easier to implement on GPUs and large data pipelines than full-batch methods.

## Pros
- faster than full-batch gradient descent
- less noisy than SGD
- widely used in modern deep learning frameworks

## Cons
- requires choosing batch size
- may require tuning learning rate and scheduler
- still needs careful training setup

## Example idea
Instead of using all 10,000 training samples at once, a model may update parameters every 32 or 64 examples. This smooths noise while remaining efficient.

## Key takeaways
- Mini-batch gradient descent is a hybrid approach.
- It uses subsets of data to avoid the extremes of full-batch and single-sample updates.
- It is the most common optimization strategy in modern ML systems.

## Practice questions
1. What is a mini-batch?
2. How is mini-batch gradient descent different from batch and stochastic methods?
3. Why is it popular in deep learning?
4. What is the trade-off of choosing a very small batch size?

## Source reference
- Transcript title: "Mini-Batch Gradient Descent"
- File: `060 - 2021-05-26 - Mini-Batch Gradient Descent.txt`
