# 034 — Handling Date and Time Variables

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 034
- Transcript title: "Handling Date and Time Variables _ Day 34 _ 100 Days of Machine Learning"
- Transcript file: `034 - 2021-04-21 - Handling Date and Time Variables _ Day 34 _ 100 Days of Machine Learning.txt`
- Topic: date and time feature engineering

## Learning objectives
- Understand why timestamps should not always be used as raw values.
- Learn how to extract useful time-based features.
- Recognize common date/time transformations for machine learning.
- Use pandas datetime functionality in practice.

## Original CampusX concept
The transcript explains that date and time columns often carry hidden information. A raw timestamp may not be directly useful to many models, but temporal features such as month, year, weekday, or day-of-year can be highly informative.

This is a classic example of feature engineering: converting a raw field into one that captures meaningful patterns.

## Why date/time features matter
Dates encode several useful patterns:
- seasonality
- weekly cycles
- holiday effects
- time trends
- business-day vs weekend patterns

A model may improve if it sees these patterns explicitly rather than only raw timestamps.

## Common extracted features
Examples include:
- weekday
- month
- year
- day of the month
- hour
- weekend flag
- quarter
- time since a key event

## Python example
```python
import pandas as pd

df = pd.DataFrame({
    'purchase_date': ['2023-01-05', '2023-02-14', '2023-04-01', '2023-07-15']
})

df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['year'] = df['purchase_date'].dt.year
df['month'] = df['purchase_date'].dt.month
df['weekday'] = df['purchase_date'].dt.day_name()
df['is_weekend'] = df['purchase_date'].dt.dayofweek.isin([5, 6]).astype(int)
print(df)
```

Expected output:
```text
  purchase_date  year  month    weekday  is_weekend
0    2023-01-05  2023      1   Thursday           0
1    2023-02-14  2023      2    Tuesday           0
2    2023-04-01  2023      4     Saturday           1
3    2023-07-15  2023      7     Saturday           1
```

## Common mistakes
- leaving timestamps as raw strings or large numeric values
- missing timezone or formatting issues
- using too much raw precision without seasonal decomposition
- failing to account for holidays or weekend effects when relevant

## Key takeaways
- Date/time columns are often rich sources of information.
- Extracting calendar-based features can improve model quality.
- The right temporal feature depends on the domain and prediction task.

## Practice questions
1. Why is a raw timestamp usually not enough for modeling?
2. Which date/time features are often useful in business contexts?
3. How can weekday or weekend information help a model?
4. Why is domain knowledge important when engineering temporal features?

## Source reference
- Transcript title: "Handling Date and Time Variables _ Day 34 _ 100 Days of Machine Learning"
- File: `034 - 2021-04-21 - Handling Date and Time Variables _ Day 34 _ 100 Days of Machine Learning.txt`
