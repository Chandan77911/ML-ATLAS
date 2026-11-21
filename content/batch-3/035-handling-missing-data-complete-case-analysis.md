# 035 — Handling Missing Data: Complete Case Analysis

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 035
- Transcript title: "Handling Missing Data _ Part 1 _ Complete Case Analysis"
- Transcript file: `035 - 2021-04-22 - Handling Missing Data _ Part 1 _ Complete Case Analysis.txt`
- Topic: missing-value handling via complete-case analysis

## Learning objectives
- Explain why missing data is a major preprocessing issue.
- Understand complete-case analysis as a missing-data strategy.
- Learn the strengths and weaknesses of dropping rows with missing values.
- Know when dropping rows is acceptable and when it is not.

## Original CampusX concept
The transcript starts with a simple but important idea: missing data is common in real datasets, and a model cannot work with absent values unless something is done about them. One of the simplest strategies is to remove rows that contain missing values.

This is called complete-case analysis or listwise deletion.

## Why missing data matters
Missing values can:
- break algorithms
- bias results if they are not random
- make training data incomplete and inconsistent
- degrade model quality when ignored

## Complete-case analysis
Complete-case analysis deletes any row with at least one missing value.

This is simple and often effective when:
- the dataset is large
- the missingness is small
- the missing data is random and not systematically related to the target

## Mathematical view
If a dataset has $n$ rows and $m$ features, and $r$ rows contain one or more missing values, then the retained rows are:

$$
 n_{kept} = n - r
$$

The loss of information is obvious: a large number of dropped rows means less data for training.

## Python example
```python
import pandas as pd

df = pd.DataFrame({
    'age': [25, 30, None, 40],
    'salary': [40000, 50000, 60000, None],
    'target': [0, 1, 1, 0]
})

print('Original rows:', len(df))
print(df)

clean_df = df.dropna()
print('\nRows after complete-case analysis:', len(clean_df))
print(clean_df)
```

Expected output:
```text
Original rows: 4
    age   salary  target
0  25.0  40000.0       0
1  30.0  50000.0       1
2  NaN  60000.0       1
3  40.0     NaN       0

Rows after complete-case analysis: 2
    age   salary  target
0  25.0  40000.0       0
1  30.0  50000.0       1
```

## When complete-case analysis is acceptable
This approach is often acceptable when:
- missingness is very low
- you have plenty of data
- the missing pattern is random
- there is no evidence that dropping rows introduces bias

## Common mistakes
- dropping rows without checking whether the missingness is informative
- losing too much data in a small dataset
- assuming missingness is random when it is systematic
- ignoring the possibility that the missing value itself could encode information

## Key takeaways
- Complete-case analysis is simple and fast.
- It works best when missingness is small and random.
- It can reduce sample size and potentially create bias if used carelessly.

## Practice questions
1. What is complete-case analysis?
2. When is dropping rows a reasonable choice?
3. Why can row deletion be harmful in small datasets?
4. Why should missingness be inspected before deciding on a strategy?

## Source reference
- Transcript title: "Handling Missing Data _ Part 1 _ Complete Case Analysis"
- File: `035 - 2021-04-22 - Handling Missing Data _ Part 1 _ Complete Case Analysis.txt`
