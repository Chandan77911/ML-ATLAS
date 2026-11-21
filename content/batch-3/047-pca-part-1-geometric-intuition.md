# 047 — PCA Part 1: Geometric Intuition

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 047
- Transcript title: "Principle Component Analysis (PCA) _ Part 1 _ Geometric Intuition"
- Transcript file: `047 - 2021-05-06 - Principle Component Analysis (PCA) _ Part 1 _ Geometric Intuition.txt`
- Topic: principal component analysis as a geometric projection method

## Learning objectives
- Understand PCA at an intuitive level.
- Learn why PCA finds the direction of maximum variance.
- See how a 2D dataset can be projected onto a lower-dimensional axis.
- Prepare for the algebraic formulation of PCA.

## Intuition
PCA looks for the direction in which the data varies the most. This direction is called the first principal component.

Why is this useful? Because if most of the information in the data lies along one direction, we can project the dataset onto that direction and reduce dimensionality while keeping most of the variation.

## Geometric picture
Imagine a cloud of points scattered in 2D space. The data is not spread equally in all directions. There is one direction along which the points stretch more than along the perpendicular direction.

PCA finds this primary axis and rotates the coordinate system so the new axis captures the maximum variance.

## Why variance matters
Variance tells us how much the data changes. If a direction has high variance, it likely contains important information.

For a feature vector $x$, variance is:

$$
\mathrm{Var}(x) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2
$$

PCA tries to choose a projection axis that maximizes this variance.

## Example
If a dataset has features like `height` and `weight`, these features may be strongly correlated. Instead of using both coordinates separately, PCA finds the main trend and projects the data onto that trend line.

## Key idea
The first principal component is the direction of greatest variance. The second principal component is orthogonal to it and captures the remaining variance.

## Common misconceptions
- PCA does not necessarily preserve the original feature meanings.
- PCA is not always the best choice if interpretability is critical.
- PCA is mainly for compression and variance capture, not for classification by itself.

## Key takeaways
- PCA is a geometric projection method for reducing dimensions.
- It finds directions of maximum variance.
- It is especially useful when many features are correlated or redundant.

## Practice questions
1. What is the main goal of PCA?
2. Why does PCA care about variance?
3. What does the first principal component represent?
4. Why is PCA useful for high-dimensional data?

## Source reference
- Transcript title: "Principle Component Analysis (PCA) _ Part 1 _ Geometric Intuition"
- File: `047 - 2021-05-06 - Principle Component Analysis (PCA) _ Part 1 _ Geometric Intuition.txt`
