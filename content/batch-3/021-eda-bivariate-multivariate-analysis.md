# 021 — EDA Using Bivariate and Multivariate Analysis

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 021
- Transcript title: "EDA using Bivariate and Multivariate Analysis _ Day 21 _ 100 Days of Machine Learning"
- Transcript file: `021 - 2021-04-06 - EDA using Bivariate and Multivariate Analysis _ Day 21 _ 100 Days of Machine Learning.txt`
- Topic: exploratory data analysis
- Subtopic: relationships between variables using bivariate and multivariate plots

## Original CampusX concept

The transcript explains that EDA becomes more insightful when we study relationships between variables, not just single columns. It introduces three main combinations:

- numerical vs numerical
- categorical vs categorical
- numerical vs categorical

### Beginner intuition

A single variable tells us about itself. Two variables together tell us whether they move together, separate, or interact.

### Technical understanding

The right plot depends on the variable types:

- scatterplot for numerical-numerical relationships
- boxplot or violinplot for numerical vs categorical comparison
- heatmap or grouped bars for categorical relationships

This is where patterns like correlation, segmentation, and dependence become visible.

## IMPORTANT TERMS EXPLAINED

- Bivariate analysis: studying two variables together
- Multivariate analysis: studying more than two variables together
- Scatter plot: plot with points representing two numerical variables
- Box plot: shows distribution and outliers for a numerical variable across categories
- Correlation: a measure of how strongly two numerical variables move together

## SUPPLEMENTARY: Why relationships matter

Many modeling decisions depend on understanding relationships in the data. For example, a feature may appear important because it strongly separates classes or correlates with the target.

## INTERVIEW EXTENSION

Q: What is the difference between bivariate and multivariate analysis?

A: Bivariate looks at two variables; multivariate looks at more than two.

Q: Which plot is best for numerical vs numerical data?

A: A scatter plot.

Q: Which plot is useful for comparing a numerical variable across categories?

A: A box plot or violin plot.

## Practical Python example

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Built-in dataset
# Relationship between total bill and tip
# Hue adds a third variable: sex

tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title('Total bill vs tip by sex')
plt.show()
```

Expected output:

A scatter plot showing a positive trend between total bill and tip, with separate color groups for male and female customers.

## Common mistakes

- assuming correlation means causation
- plotting the wrong chart for the variable types
- ignoring category-specific patterns in grouped distributions

## Practice

1. What plot is best for numerical vs numerical data?
2. What plot is best for numerical vs categorical analysis?
3. Why do we use hue in a scatter plot?
4. What does a strong pattern in a scatter plot suggest?

## Key takeaway

Bivariate and multivariate analysis reveal relationships and interactions between features, which are essential for feature selection and model building.
