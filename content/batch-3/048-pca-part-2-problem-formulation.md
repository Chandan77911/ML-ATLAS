# 048 — PCA Part 2: Problem Formulation and Step-by-Step Solution

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 048
- Transcript title: "Principle Component Analysis (PCA) _ Part 2 _ Problem Formulation and Step by Step Solution"
- Transcript file: `048 - 2021-05-07 - Principle Component Analysis (PCA) _ Part 2 _ Problem Formulation and Step by Step Solution.txt`
- Topic: mathematical problem setup of PCA

## Learning objectives
- Frame PCA as an optimization problem.
- Understand the role of covariance and eigenvectors.
- Learn the step-by-step workflow of PCA.
- Connect the formulation to the geometric intuition from lesson 047.

## Problem setup
Given a dataset with $n$ samples and $p$ features, PCA seeks a new set of orthogonal axes such that the data variance is maximized along the first axis, then the second, and so on.

This is equivalent to finding directions in feature space that best summarize the data.

## Covariance matrix
The covariance matrix captures how features vary together:

$$
\Sigma = \frac{1}{n-1} X^T X
$$

where $X$ is the centered data matrix.

The eigenvectors of $\Sigma$ are the principal directions, and the eigenvalues represent the variance captured along those directions.

## Objective
PCA tries to find a unit vector $w$ that maximizes:

$$
\mathrm{Var}(w^T X) = w^T \Sigma w
$$

subject to:

$$
\|w\| = 1
$$

This turns the problem into a constrained optimization problem.

## Step-by-step PCA process
1. Standardize the data if needed.
2. Compute the covariance matrix.
3. Compute eigenvalues and eigenvectors.
4. Sort eigenvectors by descending eigenvalue.
5. Select the top $k$ eigenvectors.
6. Project the data onto those components.

## Why this works
The eigenvectors of the covariance matrix define directions of maximum variance. The corresponding eigenvalues tell us how much variance each principal component explains.

## Key takeaways
- PCA is a projection method built around variance maximization.
- Covariance and eigen decomposition are at the heart of the solution.
- The transformation is optimal under the variance-preservation objective.

## Practice questions
1. Why is covariance important in PCA?
2. What is the role of eigenvectors in PCA?
3. What does the largest eigenvalue correspond to?
4. Why do we often standardize before PCA?

## Source reference
- Transcript title: "Principle Component Analysis (PCA) _ Part 2 _ Problem Formulation and Step by Step Solution"
- File: `048 - 2021-05-07 - Principle Component Analysis (PCA) _ Part 2 _ Problem Formulation and Step by Step Solution.txt`
