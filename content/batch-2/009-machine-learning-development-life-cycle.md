# 009 — Machine Learning Development Life Cycle

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 009
- Transcript title: "Machine Learning Development Life Cycle _ MLDLC in Data Science"
- Transcript file: `009 - 2021-03-23 - Machine Learning Development Life Cycle _ MLDLC in Data Science.txt`
- Topic: project lifecycle
- Subtopic: machine learning development lifecycle and production pipeline

## Original CampusX concept

The transcript introduces the idea that machine learning is not just about writing an algorithm. A real ML project involves several stages, from defining the business problem to deploying and monitoring the model.

This is the practical lifecycle behind ML work:

- problem understanding
- data collection
- data preparation
- feature engineering
- model selection
- training and evaluation
- deployment
- monitoring and maintenance

### Beginner intuition

A machine learning project is a workflow, not a single code cell. You do not just train a model once and stop. You define the task, make sure the data is usable, train and evaluate the model, then deploy it in a way that keeps working in the real world.

### Technical understanding

The lifecycle is a structured process for turning raw data into an operational prediction system.

A common pipeline is:

$$
\text{Problem} \rightarrow \text{Data} \rightarrow \text{Cleaning} \rightarrow \text{Features} \rightarrow \text{Model} \rightarrow \text{Evaluation} \rightarrow \text{Deployment}
$$

Each stage affects the final performance. If the problem is defined poorly or the data is weak, even a strong algorithm will underperform.

## IMPORTANT TERMS EXPLAINED

- Business objective: the actual goal of the system, such as reducing churn or improving recommendation quality
- Feature engineering: transforming raw data into meaningful inputs for a model
- Training: learning parameters from data
- Validation: checking how well the model generalizes on unseen data
- Deployment: making the model available in a real system
- Monitoring: tracking performance after deployment

## SUPPLEMENTARY: Why this lifecycle matters

In practice, most ML failures happen not because the model is “wrong” in theory, but because one step in the lifecycle was weak. Examples include:

- poor problem definition
- wrong target variable
- unbalanced data
- data leakage
- weak evaluation strategy
- no monitoring after deployment

This is why the lifecycle is so important.

## INTERVIEW EXTENSION

Q: Why is the ML lifecycle important?

A: Because building a model is only one part of the project; the full system must be defined, validated, and maintained.

Q: What is data leakage?

A: Using information from the future or from the target itself during training, which inflates performance on a misleading benchmark.

Q: Why does monitoring matter after deployment?

A: Data distributions change over time, so performance can degrade even when the model was good initially.

## Mermaid diagram

```mermaid
flowchart LR
    A[Business Problem] --> B[Data Collection]
    B --> C[Data Cleaning]
    C --> D[Feature Engineering]
    D --> E[Model Training]
    E --> F[Validation & Testing]
    F --> G[Deployment]
    G --> H[Monitoring & Retraining]
    H --> B
```

## Practical Python example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
preds = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, preds), 3))
```

Expected output:

```text
Accuracy: 0.974
```

## Common mistakes

- Treating model training as the only step in the project
- ignoring evaluation and hold-out data
- deploying without monitoring
- using the wrong metric for the business objective

## Practice

1. List the major stages of the ML lifecycle.
2. Why is monitoring needed after deployment?
3. What happens if the target variable is defined poorly?
4. Explain the difference between training and deployment.

## Code-to-practice mapping

- Original concept: the ML lifecycle as a series of stages
- Supplementary concept: evaluation, deployment, and maintenance
- Code: a minimal training and validation pipeline
- Practice: framing the workflow as a real project process
