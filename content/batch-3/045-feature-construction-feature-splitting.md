# 045 — Feature Construction and Feature Splitting

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 045
- Transcript title: "Feature Construction _ Feature Splitting"
- Transcript file: `045 - 2021-05-04 - Feature Construction _ Feature Splitting.txt`
- Topic: creating informative features from existing raw variables

## Learning objectives
- Understand why new features often improve model performance.
- Learn how to split a single feature into multiple informative ones.
- See how feature construction can reveal hidden structure in data.
- Apply feature splitting in a small dataset.

## Why feature construction matters
Some raw features are useful only after being transformed. A single field may hide more information than it appears to carry at first glance.

For instance:
- a date column can be split into month, day, and year
- a full name can be split into first name and last name
- a `timestamp` might reveal time-of-day patterns
- a `customer_id` may encode segments or prefixes

## Feature splitting example
Suppose we have a column called `date`:

```python
import pandas as pd

sales = pd.DataFrame({
    'date': ['2024-01-15', '2024-02-05', '2024-03-11']
})

sales['day'] = pd.to_datetime(sales['date']).dt.day
sales['month'] = pd.to_datetime(sales['date']).dt.month
sales['year'] = pd.to_datetime(sales['date']).dt.year

print(sales)
```

Expected output:
```text
         date  day  month  year
0  2024-01-15   15      1  2024
1  2024-02-05    5      2  2024
2  2024-03-11   11      3  2024
```

This exposes important temporal patterns that a single date string does not directly communicate to a model.

## Intuition
Feature construction helps the model see patterns that were hidden in the original representation.

A useful feature is one that makes the learning problem easier or more informative.

## Common examples
- splitting date into month and year
- extracting text prefixes or numeric codes
- creating interaction terms such as `age * income`
- deriving `is_weekend`, `is_summer`, or `has_discount`

## Common mistakes
- creating too many features without evidence they help
- engineering features based on leakage from the target
- neglecting domain understanding when deciding what to construct

## Key takeaways
- Feature construction is a powerful part of preprocessing.
- Splitting fields into meaningful components can reveal patterns.
- Good features often matter as much as model choice.

## Practice questions
1. Why is feature construction useful?
2. How can a date column be made more useful to a model?
3. What are the risks of creating too many engineered features?
4. Why should feature engineering be guided by domain knowledge?

## Source reference
- Transcript title: "Feature Construction _ Feature Splitting"
- File: `045 - 2021-05-04 - Feature Construction _ Feature Splitting.txt`
