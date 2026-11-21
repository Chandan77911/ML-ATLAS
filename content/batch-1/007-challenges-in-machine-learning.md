# 007 — Challenges in Machine Learning

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 007
- Transcript title: "Challenges in Machine Learning | Problems in Machine Learning"
- Transcript file: `007 - 2021-03-20 - Challenges in Machine Learning _ Problems in Machine Learning.txt`
- Topic: practical ML challenges
- Subtopic: data quality, representativeness, missing information, and model reliability

## Original CampusX concept

The instructor stresses a very important reality: machine learning is not just about choosing a model. In real projects, several challenges create failure or poor performance.

The lesson highlights recurring issues such as:

- insufficient or poor-quality data
- non-representative sampling
- missing or noisy labels
- difficult or expensive data collection
- biased data collection processes
- poor feature design or weak feature quality
- mismatch between training population and real deployment population

### Beginner intuition

A model is only as good as the data behind it. A powerful algorithm cannot fix poor data quality.

If your data is missing, biased, or unrepresentative, the model will learn the wrong pattern or generalize poorly.

### Technical understanding

This lesson introduces a theme that matters throughout the course: data is an engineering asset.

A model learns from the distribution in the training data. If the data does not reflect the real-world distribution, then the learned decision boundary or function will be distorted.

This is often summarized as:

- garbage in → garbage out
- unrepresentative sample → poor generalization
- noisy labels → unstable model learning

## IMPORTANT TERMS EXPLAINED

- Sampling bias: when the training sample does not fairly represent the real population
- Label noise: incorrect or unreliable target labels
- Data quality: how clean, complete, and usable the data is
- Feature quality: whether the input variables are informative and meaningful
- Generalization: performance on unseen real-world data

## SUPPLEMENTARY: Why this matters more than model choice

A more complex model will not magically fix weak data. In many projects, the largest gains come from better data collection, data cleaning, and feature engineering.

That is why the course later spends so much time on handling missing values, encoding, scaling, feature engineering, and EDA.

## INTERVIEW EXTENSION

Q: What is one major challenge in ML projects?

A: Data collection and data quality.

Q: Why is representativeness important?

A: A model trained on a narrow sample may fail when applied to the broader population.

Q: Why does a larger dataset not always solve the problem?

A: Large but biased or unrepresentative datasets can still produce poor models.

## Practical Python example

```python
import pandas as pd

# A small example of a skewed or unbalanced sample
sample = pd.DataFrame({
    'age': [18, 22, 25, 30, 40, 80],
    'income': [20000, 25000, 26000, 50000, 80000, 120000],
})

print(sample.describe())
```

Expected output:

```text
             age        income
count   6.000000      6.000000
mean   35.833333   54500.000000
std    22.651...     34824.5...
min    18.000000   20000.000000
max    80.000000   120000.000000
```

### Why this example matters

The sample is small and skewed toward younger ages, which shows how a model trained on such data could misrepresent real-world patterns.

## COMMON MISTAKES AND MISCONCEPTIONS

- Assuming bigger data automatically means better data
- Thinking model complexity can compensate for bad sampling
- Ignoring label quality and feature quality
- Forgetting that deployment data may differ from training data

## Practice

1. List three major ML challenges mentioned in this lesson.
2. Explain how a biased dataset can still be misleading even when it is large.
3. Describe one way to improve data quality before training.
4. Why does representativeness matter more than raw volume?

## Code-to-practice mapping

- Original concept: ML project difficulties and data issues
- Supplementary concept: sampling bias, representativeness, and data quality
- Code: dataset summary illustrating skew and distribution issues
- Practice: diagnosing project risk before modeling
