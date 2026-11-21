# 020 — EDA Using Univariate Analysis

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 020
- Transcript title: "EDA using Univariate Analysis _ Day 20 _ 100 Days of Machine Learning"
- Transcript file: `020 - 2021-04-05 - EDA using Univariate Analysis _ Day 20 _ 100 Days of Machine Learning.txt`
- Topic: exploratory data analysis
- Subtopic: univariate analysis for categorical and numerical variables

## Original CampusX concept

The transcript introduces univariate analysis as the study of one variable at a time. It distinguishes between numerical and categorical data and shows how different plots reveal useful structure.

### Beginner intuition

Univariate analysis answers a simple question: “What does this single column look like?”

### Technical understanding

For a single variable, the analysis depends on data type:

- categorical variables: frequency counts, pie charts, bar plots
- numerical variables: histograms, box plots, distributions, summary stats

This helps reveal patterns such as skewness, outliers, and central tendency.

## IMPORTANT TERMS EXPLAINED

- Univariate analysis: analysis of one variable at a time
- Numerical variable: values that are quantitative and continuous or discrete
- Categorical variable: values that represent groups or labels
- Histogram: a graph showing the distribution of numerical values across bins
- Count plot: a bar chart showing category frequencies

## SUPPLEMENTARY: Why this matters

The first pass of EDA is about understanding distributions before making modeling choices. A model can be strong only if the data is understood well enough to choose the right features and preprocessing steps.

## INTERVIEW EXTENSION

Q: What is univariate analysis?

A: Analysis of a single feature or column.

Q: How is categorical data typically visualized?

A: With count plots or pie charts.

Q: How is numerical data typically visualized?

A: With histograms and summary statistics.

## Practical Python example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
sales = pd.DataFrame({
    'age': [22, 25, 28, 30, 35, 42, 50, 62],
    'city': ['Delhi', 'Delhi', 'Mumbai', 'Bengaluru', 'Delhi', 'Mumbai', 'Bengaluru', 'Delhi']
})

# Frequency of categories
print(sales['city'].value_counts())

# Histogram for numerical variable
plt.hist(sales['age'], bins=5)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age distribution')
plt.show()
```

Expected output:

```text
Delhi        4
Mumbai       2
Bengaluru    2
Name: city, dtype: int64
```

## Common mistakes

- treating all columns as equally useful without checking type
- using the wrong plot for the wrong data type
- ignoring outliers and skewness

## Practice

1. Explain the difference between categorical and numerical data.
2. Which plot is useful for a categorical feature?
3. Which plot is useful for a numerical feature?
4. Why do we care about distributions before modeling?

## Key takeaway

Univariate analysis is the first lens used to understand a dataset. It tells us what each column looks like and which variables deserve deeper modeling attention.
