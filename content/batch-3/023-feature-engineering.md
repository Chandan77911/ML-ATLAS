# 023 — What is Feature Engineering

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 023
- Transcript title: "What is Feature Engineering _ Day 23 _ 100 Days of Machine Learning"
- Transcript file: `023 - 2021-04-08 - What is Feature Engineering _ Day 23 _ 100 Days of Machine Learning.txt`
- Topic: feature engineering fundamentals

## Learning objectives
- Understand what feature engineering means and why it matters.
- Separate feature engineering from preprocessing and model building.
- Identify the main stages of feature engineering.
- Know when to transform, create, select, or extract features.

## Original CampusX concept
The transcript explains that raw data is not always directly usable by machine learning algorithms. A model can only learn from the information represented in the features. Feature engineering is the process of using domain knowledge to transform raw data into better representations for learning.

This is not a magic trick; it is a systematic way to improve the input representation. A simple model with strong features often beats a complex model fed weak features.

## Why feature engineering exists
Real datasets are often messy, sparse, inconsistent, or encoded in a form not suited to a learning algorithm. Common issues include:
- missing values
- categorical strings instead of numbers
- skewed distributions
- timestamps that hide useful patterns
- hidden interactions between variables

A model learns from the representation of the data. Feature engineering changes that representation so the model can see patterns more clearly.

### Beginner intuition
If a student dataset has a `date_of_birth`, `city`, and `score` column, the raw values are not directly useful as-is. Feature engineering converts them into useful predictors, such as `age`, `city_frequency`, or `attendance_score_ratio`.

### Technical understanding
Feature engineering is the process of creating or adjusting input variables so they match the assumptions of the learning algorithm. It can include:
- handling missing values
- transforming distributions
- encoding categories
- creating new features from old ones
- removing weak or redundant features
- extracting patterns from raw data

## Main types of feature engineering

### 1. Feature transformation
This changes the form of an existing feature to make it easier for a model to process.

Examples:
- log-transforming income
- standardizing age
- converting date values into month and year

### 2. Feature creation
This creates new features from existing ones.

Examples:
- `age` from `date_of_birth`
- `total_spent = price * quantity`
- `is_weekend` from a timestamp

### 3. Feature selection
Not every feature is useful. Some are noisy, redundant, or weakly predictive.

Examples:
- dropping unique IDs
- removing constant columns
- selecting the most relevant variables

### 4. Feature extraction
This creates new combinations or lower-dimensional representations from original features.

Examples:
- PCA-based components
- text frequency counts
- image edge and texture features

## SUPPLEMENTARY: mathematical view
Feature engineering can be viewed as choosing a transformation function $f$ such that the new representation $x' = f(x)$ is easier for the model to learn from.

If the original feature space does not match the model assumptions, a feature transform can improve class separation, reduce variance, or normalize scale. The transform does not need to be complex; it only needs to improve the representation.

## Practical Python example
```python
import pandas as pd

df = pd.DataFrame({
    'customer_id': [101, 102, 103, 104],
    'age': [24, 41, 29, 52],
    'income': [25000, 90000, 56000, 110000],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore']
})

df['income_per_month'] = df['income'] / 12
print(df[['age', 'income_per_month', 'city']])
```

Expected output:
```text
   age  income_per_month      city
0   24        2083.333333     Delhi
1   41        7500.000000    Mumbai
2   29        4666.666667     Delhi
3   52        9166.666667  Bangalore
```

## Why this matters in practice
A model is only as good as the information it receives. Feature engineering helps make the information more structured, more informative, and more consistent with the algorithm being used.

In real ML pipelines, the difference between weak and strong features often matters as much as the choice of model.

## Common mistakes
- treating feature engineering as separate from the rest of the pipeline
- creating features without checking whether they are actually useful
- leaking target information into input features
- over-engineering simple datasets with unnecessary transformations
- ignoring domain knowledge

## Key takeaways
- Feature engineering turns raw data into better learning representations.
- It is not limited to one step; it may involve transformation, creation, extraction, and selection.
- Domain knowledge is a major part of the process.
- Good features often matter as much as the algorithm itself.

## Practice questions
1. Why is raw data not always directly usable by a model?
2. What is the difference between feature transformation and feature creation?
3. Give one example of a feature created from date or text data.
4. Why can a strong feature set outperform a more complex model with poor features?

## Source reference
- Transcript title: "What is Feature Engineering _ Day 23 _ 100 Days of Machine Learning"
- File: `023 - 2021-04-08 - What is Feature Engineering _ Day 23 _ 100 Days of Machine Learning.txt`
