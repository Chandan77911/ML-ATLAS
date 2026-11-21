# 014 — How to Frame a Machine Learning Problem

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 014
- Transcript title: "How to Frame a Machine Learning Problem _ How to plan a Data Science Project Effectively"
- Transcript file: `014 - 2021-03-29 - How to Frame a Machine Learning Problem _ How to plan a Data Science Project Effectively.txt`
- Topic: problem formulation
- Subtopic: converting a business problem into an ML problem

## Original CampusX concept

The transcript explains that the most important part of a machine learning project is not selecting a model first. It is defining the problem correctly.

A common mistake is to say: “I want to use machine learning.” The better question is: “What decision do I want to support, and what output should the model predict?”

### Beginner intuition

A model is only useful if it solves a real problem. If the business question is vague, the model will be vague too.

### Technical understanding

To frame an ML problem, you need to answer:

- What is the target variable?
- What is the prediction task?
- Is it classification, regression, ranking, or clustering?
- What data is available?
- What does success look like?

For example:

- Predict churn: binary classification
- Predict price: regression
- Recommend products: ranking
- Segment users: clustering

## IMPORTANT TERMS EXPLAINED

- Target variable: the value the model predicts
- Label: the correct supervised target used during training
- Objective: the business or research goal of the model
- Evaluation metric: the measure used to judge model quality

## SUPPLEMENTARY: Why framing matters

A poorly framed ML problem often leads to wasted effort. The model can be accurate in a technical sense but still fail to help the business. This is why problem definition is part of data science strategy, not just coding.

## INTERVIEW EXTENSION

Q: Why is problem framing more important than model choice?

A: A model cannot be useful if the task is not clearly defined.

Q: What is a common mistake in a data science project?

A: Jumping straight to modeling without clarifying the target and metric.

## Practical Python example

```python
import pandas as pd

# A simple example of a framing decision: predict whether a customer will churn
customer_data = pd.DataFrame({
    'monthly_spend': [120, 90, 200, 50, 300],
    'last_login_days': [5, 20, 2, 30, 1],
    'churned': [0, 1, 0, 1, 0]
})

print(customer_data)
```

Expected output:

```text
   monthly_spend  last_login_days  churned
0            120                5        0
1             90               20        1
2            200                2        0
3             50               30        1
4            300                1        0
```

### Why this matters

The target variable here is churned. That makes the task a clear binary classification problem.

## Common mistakes

- choosing a model before defining the problem
- predicting the wrong target variable
- using metrics that do not match the business objective
- ignoring data feasibility and availability

## Practice

1. Convert a business problem into a machine learning task.
2. What is the target variable in a fraud detection problem?
3. Why is choosing the wrong metric dangerous?
4. Give one example of a clustering problem and one example of a classification problem.

## Code-to-practice mapping

- Original concept: ML project definition and objective framing
- Supplementary concept: target choice and evaluation alignment
- Code: creating a small binary classification dataset
- Practice: turning a business goal into a prediction task
