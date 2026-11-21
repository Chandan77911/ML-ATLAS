# 038 — Missing Indicator and Random Sample Imputation

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 038
- Transcript title: "Missing Indicator _ Random Sample Imputation _ Handling Missing Data Part 4"
- Transcript file: `038 - 2021-04-26 - Missing Indicator _ Random Sample Imputation _ Handling Missing Data Part 4.txt`
- Topic: missingness as information and random-value imputation

## Learning objectives
- Understand the idea of a missing indicator feature.
- Learn why missingness itself can be informative.
- Explore random sample imputation as an alternative to mean or median filling.
- Use this strategy appropriately in real ML pipelines.

## Why missingness matters
Sometimes the fact that a value is missing is itself predictive. For example, in a medical dataset, a missing blood-pressure reading may correlate with a patient being in a critical state.

If we discard the information that the value was missing, we lose signal.

## Missing indicator
A missing indicator creates a new binary feature:

$$
M_i =
\begin{cases}
1, & \text{if value is missing} \\
0, & \text{otherwise}
\end{cases}
$$

This lets the model learn whether the absence of data is associated with the target.

## Random sample imputation
Instead of filling missing values with a fixed statistic such as the mean, random sample imputation replaces missing entries with a randomly sampled observed value from the same feature.

This helps preserve variability and can sometimes avoid unrealistic distortions from constant replacements.

## Python example
```python
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    'salary': [12000, np.nan, 18000, np.nan, 15000, 13000]
})

observed = df['salary'].dropna().values
missing_mask = df['salary'].isna()

random_values = np.random.choice(observed, size=missing_mask.sum(), replace=True)
df.loc[missing_mask, 'salary'] = random_values

print(df)
```

Expected output:
```text
    salary
0  12000.0
1  13000.0
2  18000.0
3  15000.0
4  15000.0
5  13000.0
```

## When to use this strategy
- when a feature is noisy and a constant value would distort the distribution
- when the missing mechanism is not simply random but you still want a reasonable imputation strategy
- when you want to preserve the variability of the feature

## Common mistakes
- ignoring the missingness indicator when the missing pattern is meaningful
- using random sample imputation without understanding the feature distribution
- forgetting that random imputation adds variance and should be reproducible with a seed

## Key takeaways
- Missing values can carry predictive information.
- Missing indicators allow the model to learn this signal.
- Random sample imputation preserves variation better than a single fixed value in some situations.

## Practice questions
1. What does a missing indicator represent?
2. Why can missingness be informative?
3. How does random sample imputation differ from mean imputation?
4. Why should random imputation use a fixed seed in experiments?

## Source reference
- Transcript title: "Missing Indicator _ Random Sample Imputation _ Handling Missing Data Part 4"
- File: `038 - 2021-04-26 - Missing Indicator _ Random Sample Imputation _ Handling Missing Data Part 4.txt`
