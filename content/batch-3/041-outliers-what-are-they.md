# 041 — What Are Outliers?

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 041
- Transcript title: "What are Outliers _ Outliers in Machine Learning"
- Transcript file: `041 - 2021-04-29 - What are Outliers _ Outliers in Machine Learning.txt`
- Topic: outlier definition and effect on machine learning

## Learning objectives
- Define what an outlier is.
- Understand why outliers can appear in real-world datasets.
- Learn how outliers affect training, inference, and model performance.
- Prepare for outlier detection methods such as z-score, IQR, and winsorization.

## What is an outlier?
An outlier is a data point that differs significantly from the rest of the dataset.

It can be:
- unusually high
- unusually low
- unusually different in pattern or behavior

Examples:
- a salary of $10 million in a mostly moderate-income sample
- a house with 100 rooms in a neighborhood of small homes
- a transaction far larger than normal shopping behavior

## Why outliers matter
Outliers can distort:
- the mean
- the variance
- the estimated coefficients of a model
- the distance-based calculations in clustering or KNN

In short, a few extreme points can significantly affect learning.

## Visual intuition
If a dataset is centered around a typical range and one point is far away, it is easy to spot on a boxplot or scatter plot. That far-away point is an outlier.

## Mathematical intuition
A point is often considered an outlier if it is far from the central tendency of the feature.

For a feature $x$, a point may be unusual when:

$$
|x_i - \mu| \gg \sigma
$$

where:
- $\mu$ is the mean
- $\sigma$ is the standard deviation

This is the idea behind z-score-based detection.

## Real-world causes
Outliers can arise from:
- data-entry errors
- sensor failures
- fraud or abnormal behavior
- rare but valid events

It is important to distinguish between bad data and meaningful rare events.

## Common mistakes
- deleting every extreme value without checking whether it is a valid observation
- treating all outliers as noise
- ignoring outliers in features that are highly skewed or naturally variable

## Key takeaways
- Outliers are values far from the majority of the distribution.
- They may be errors or genuine rare events.
- Detecting and handling them correctly is essential for robust modeling.

## Practice questions
1. What is an outlier?
2. Why can outliers affect the mean and variance?
3. Name one real-world cause of outliers.
4. Should every extreme value always be removed?

## Source reference
- Transcript title: "What are Outliers _ Outliers in Machine Learning"
- File: `041 - 2021-04-29 - What are Outliers _ Outliers in Machine Learning.txt`
