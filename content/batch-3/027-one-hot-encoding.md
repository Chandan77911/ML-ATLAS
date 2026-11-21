# 027 — One-Hot Encoding

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 027
- Transcript title: "One Hot Encoding _ Handling Categorical Data _ Day 27 _ 100 Days of Machine Learning"
- Transcript file: `027 - 2021-04-13 - One Hot Encoding _ Handling Categorical Data _ Day 27 _ 100 Days of Machine Learning.txt`
- Topic: one-hot encoding and categorical handling

## Learning objectives
- Explain what one-hot encoding does.
- Understand the difference between one-hot and ordinal encoding.
- Learn how to encode nominal categories for ML models.
- Recognize the limitations of dense one-hot matrices.

## Original CampusX concept
The transcript explains that one-hot encoding is a way to convert nominal categories into a form that a model can understand without implying any order. Instead of giving a category a single integer, each category becomes its own binary column.

For example, a column `color` with values `Red`, `Green`, and `Blue` becomes three columns: `Red`, `Green`, and `Blue`. Only one is active at a time.

## Why one-hot encoding is used
One-hot encoding avoids the false ordering problem created by assigning integers to categories. It is ideal for nominal data where one category is not greater or smaller than another.

## Mathematical idea
If a category has $k$ possible values, one-hot encoding creates $k$ binary features.

For a value in category $c_j$:

$$
[0, 0, \dots, 1, \dots, 0]
$$

where the 1 is placed in the column corresponding to $c_j$.

Example:

$$
\text{Red} \rightarrow [1, 0, 0]
$$

$$
\text{Green} \rightarrow [0, 1, 0]
$$

$$
\text{Blue} \rightarrow [0, 0, 1]
$$

## Python example
```python
import pandas as pd

df = pd.DataFrame({'color': ['Red', 'Blue', 'Green', 'Red']})
encoded = pd.get_dummies(df['color'], prefix='color')
print(encoded)
```

Expected output:
```text
   color_Blue  color_Green  color_Red
0           0            0          1
1           1            0          0
2           0            1          0
3           0            0          1
```

## When to use one-hot encoding
Use it when:
- categories are nominal
- the order among categories is not meaningful
- you want a model to treat each category as a separate binary feature

## Common mistakes
- using one-hot encoding without checking high cardinality
- forgetting that sparse encoding is often more efficient for large categories
- treating one-hot columns as continuous numeric values
- using ordinal encoding for unordered categories

## Key takeaways
- One-hot encoding turns each category into its own binary column.
- It preserves category information without implying ordering.
- It is one of the standard methods for handling nominal variables.

## Practice questions
1. Why is one-hot encoding preferred over label encoding for nominal categories?
2. What does a one-hot vector look like for three categories?
3. What problem does one-hot encoding avoid?
4. When would you choose one-hot encoding over ordinal encoding?

## Source reference
- Transcript title: "One Hot Encoding _ Handling Categorical Data _ Day 27 _ 100 Days of Machine Learning"
- File: `027 - 2021-04-13 - One Hot Encoding _ Handling Categorical Data _ Day 27 _ 100 Days of Machine Learning.txt`
