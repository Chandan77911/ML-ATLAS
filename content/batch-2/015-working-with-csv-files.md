# 015 — Working with CSV Files

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 015
- Transcript title: "Working with CSV files _ Day 15 _ 100 Days of Machine Learning"
- Transcript file: `015 - 2021-03-30 - Working with CSV files _ Day 15 _ 100 Days of Machine Learning.txt`
- Topic: data ingestion
- Subtopic: loading and exploring CSV files with Python

## Original CampusX concept

The transcript starts the practical data handling portion of the course by showing how to work with CSV files, which are among the most common data formats in ML and analytics.

The core tasks include:

- reading a CSV file
- inspecting columns and rows
- checking data types
- understanding missing values
- preparing data for modeling

### Beginner intuition

CSV files are like tables stored in text form. They are easy to share and easy to inspect, which makes them a standard format for datasets.

### Technical understanding

A CSV file is a text representation of tabular data. Each row corresponds to a record, and each column corresponds to a feature or target.

In Python, pandas makes this simple:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
print(df.info())
```

This gives both a quick preview and a summary of each column.

## IMPORTANT TERMS EXPLAINED

- CSV: comma-separated values
- DataFrame: a tabular data structure used in pandas
- Missing value: a blank or null value in a dataset
- Feature column: an input variable
- Target column: the value the model tries to predict

## SUPPLEMENTARY: Why CSV work matters

Many real datasets begin as CSV files, especially in business settings, research, and open-source ML benchmarks. A solid understanding of reading and data inspection is a foundational skill.

## INTERVIEW EXTENSION

Q: Why is CSV still widely used in ML projects?

A: Because it is simple, portable, and easy to inspect.

Q: What is the first thing you check after loading a CSV file?

A: Column names, row count, data types, and missing values.

## Practical Python example

```python
import pandas as pd

# Example dataset
raw = {
    'age': [25, 30, 35, 40, 45],
    'income': [40000, 55000, 62000, 70000, 90000],
    'city': ['NY', 'LA', 'NY', 'SF', 'LA']
}

df = pd.DataFrame(raw)
print(df.head())
print(df.isnull().sum())
print(df.describe())
```

Expected output:

```text
   age  income city
0   25   40000   NY
1   30   55000   LA
2   35   62000   NY
3   40   70000   SF
4   45   90000   LA
age      0
income   0
city     0
dtype: int64

             age        income
count   5.000000      5.000000
mean   35.000000   63400.000000
std     7.906...     18900.0...
min    25.000000   40000.000000
max    45.000000   90000.000000
```

## Common mistakes

- assuming CSV files are always clean
- not checking missing values and wrong dtypes
- ignoring column names and metadata

## Practice

1. Write a Python snippet to read a CSV file into a DataFrame.
2. What would you inspect immediately after loading a CSV file?
3. Why is missing-value analysis important before modeling?
4. Explain the difference between a row and a column in a CSV dataset.

## Code-to-practice mapping

- Original concept: reading and inspecting CSV data
- Supplementary concept: data quality checks and feature understanding
- Code: DataFrame reading and summary exploration
- Practice: basic data inspection workflow
