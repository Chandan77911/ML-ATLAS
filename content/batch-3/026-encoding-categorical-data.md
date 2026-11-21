# 026 — Encoding Categorical Data

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 026
- Transcript title: "Encoding Categorical Data _ Ordinal Encoding _ Label Encoding"
- Transcript file: `026 - 2021-04-12 - Encoding Categorical Data _ Ordinal Encoding _ Label Encoding.txt`
- Topic: categorical encoding

## Learning objectives
- Understand why categorical data must be converted for ML models.
- Distinguish between label encoding and ordinal encoding.
- Recognize the limitations of naive encoding methods.
- Know when not to use a numeric encoding blindly.

## Original CampusX concept
Most machine learning models require numerical input. If a feature contains categories such as `Low`, `Medium`, and `High`, it cannot be fed directly to a model unless those categories are converted into numbers.

The session distinguishes between label encoding and ordinal encoding. The idea is to replace category names with numbers while preserving structure when the categories have a meaningful order.

## Why encoding is needed
A model like logistic regression, SVM, KNN, or neural networks expects numeric arrays. Plain text values cannot be interpreted mathematically.

## Ordinal encoding
Ordinal encoding is used when the categories have a natural order.

Example:
- `Low` < `Medium` < `High`

We map them to:

$$
\text{Low} \rightarrow 0, \quad \text{Medium} \rightarrow 1, \quad \text{High} \rightarrow 2
$$

This is appropriate when the order is meaningful.

## Label encoding
Label encoding is similar but is often used for target variables or for simpler categorical assignments. It converts classes to integers without necessarily implying an ordinal relationship.

Example:

$$
\{\text{Red}, \text{Blue}, \text{Green}\} \rightarrow \{0, 1, 2\}
$$

This does not mean `Red < Blue < Green` in a mathematical sense; it is just a label mapping.

## When not to use simple encoding
A naive integer mapping can incorrectly imply ordering. For example, a model may think `High = 2` is greater than `Low = 0` and treat the category difference as meaningful even when no such ordinal relationship exists.

That is why nominal categories are often better handled with one-hot encoding.

## Python example
```python
import pandas as pd

jobs = pd.DataFrame({'experience': ['Low', 'High', 'Medium', 'Low']})

mapping = {'Low': 0, 'Medium': 1, 'High': 2}
jobs['experience_encoded'] = jobs['experience'].map(mapping)
print(jobs)
```

Expected output:
```text
  experience  experience_encoded
0        Low                   0
1       High                   2
2     Medium                   1
3        Low                   0
```

## Common mistakes
- using ordinal encoding for unordered categories
- ignoring the fact that label encoding can mislead the model
- not checking whether the category order is actually valid
- forgetting to handle unseen categories during deployment

## Key takeaways
- Encoding converts text categories into numeric values.
- Ordinal encoding is valid when category order is meaningful.
- Label encoding is useful for simple label mapping, but it does not represent true semantics unless the order is meaningful.
- For unordered categories, one-hot encoding is usually safer.

## Practice questions
1. Why cannot a model directly use text categories?
2. When is ordinal encoding appropriate?
3. Why is ordinary integer encoding risky for nominal categories?
4. Give one example where ordering is meaningful and one where it is not.

## Source reference
- Transcript title: "Encoding Categorical Data _ Ordinal Encoding _ Label Encoding"
- File: `026 - 2021-04-12 - Encoding Categorical Data _ Ordinal Encoding _ Label Encoding.txt`
