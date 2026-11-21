# 019 — Understanding Your Data

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 019
- Transcript title: "Understanding Your Data _ Day 19 _ 100 Days of Machine Learning"
- Transcript file: `019 - 2021-04-03 - Understanding Your Data _ Day 19 _ 100 Days of Machine Learning.txt`
- Topic: data exploration
- Subtopic: first-pass questions to ask when inspecting a dataset

## Original CampusX concept

The transcript emphasizes that before any modeling, you must understand the basic shape and structure of the data. The instructor introduces a set of questions that are usually asked immediately when a dataset is first loaded.

These include questions such as:

- how big is the dataset?
- what are the column names and types?
- what does the first few rows look like?
- are there missing values?
- what is the distribution of numerical features?
- which columns are likely relevant?

### Beginner intuition

Before building a model, it helps to ask: what am I looking at? This is the difference between blindly training on a dataset and actually understanding the problem.

### Technical understanding

A good first check includes:

- shape: number of rows and columns
- dtypes: numeric vs categorical
- head/tail: sample rows
- missing values: counts per column
- summary statistics: mean, median, min, max, quantiles

This reduces the chance that we train on data we do not understand.

## IMPORTANT TERMS EXPLAINED

- Shape: number of rows and columns in a DataFrame
- Data type: integer, float, object, datetime, category, etc.
- Missing value: an absent or null value in the dataset
- Summary statistics: a compact description of a variable distribution
- Exploratory Data Analysis (EDA): the process of understanding the data before modeling

## SUPPLEMENTARY: Why this is not optional

Many model failures are not algorithmic failures; they are data-understanding failures. Without checking the data, you may train on bad labels, poor features, or impossible data patterns.

## INTERVIEW EXTENSION

Q: What is the first thing you do when you get a dataset?

A: Inspect its shape, columns, dtypes, missing values, and sample rows.

Q: Why is sampling useful during EDA?

A: It gives a quick sense of the data without reading the entire dataset in detail.

## Practical Python example

```python
import pandas as pd

df = pd.DataFrame({
    'age': [22, 30, 41, 28, 35],
    'income': [30000, 42000, 80000, 50000, 76000],
    'city': ['Delhi', 'Mumbai', 'Bengaluru', 'Delhi', 'Chennai']
})

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
print(df.describe())
```

Expected output:

```text
(5, 3)
age            int64
income         int64
city          object
dtype: object

   age  income        city
0   22   30000       Delhi
1   30   42000      Mumbai
2   41   80000  Bengaluru
3   28   50000       Delhi
4   35   76000     Chennai

age      0
income   0
city     0
dtype: int64

             age        income
count   5.000000      5.000000
mean   31.200000   55600.000000
std     7.326...    19455.4...
min    22.000000   30000.000000
max    41.000000   80000.000000
```

## Common mistakes

- skipping the initial dataset inspection
- assuming the dataset is clean without checking nulls
- ignoring data types and categories
- using only a few rows without a broader view of the data

## Practice

1. What is the purpose of `df.head()`?
2. Why is `df.isnull().sum()` important?
3. What does `df.shape` tell you?
4. What is the value of summary statistics in EDA?

## Key takeaway

Understanding the data is not a formality. It is the foundation of every good ML workflow.
