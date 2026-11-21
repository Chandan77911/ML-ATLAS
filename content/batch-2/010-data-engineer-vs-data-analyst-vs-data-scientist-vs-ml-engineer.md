# 010 — Data Engineer vs Data Analyst vs Data Scientist vs ML Engineer

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 010
- Transcript title: "Data Engineer Vs Data Analyst Vs Data Scientist Vs ML Engineer _ Data Science Job Roles"
- Transcript file: `010 - 2021-03-24 - Data Engineer Vs Data Analyst Vs Data Scientist Vs ML Engineer _ Data Science Job Roles.txt`
- Topic: data science roles
- Subtopic: responsibilities and overlap between data roles

## Original CampusX concept

The transcript explains that different data roles exist in the industry, even though the boundaries can overlap. The key idea is that each role contributes to the same data-driven system from a different angle.

### The major roles

- Data Engineer: builds pipelines, storage systems, and data infrastructure
- Data Analyst: explores data, summarizes it, and helps answer business questions
- Data Scientist: builds models, analyzes patterns, and extracts insights
- ML Engineer: brings models into production and maintains them in real systems

### Beginner intuition

A simple way to think about it is:

- Data Engineer builds the roads and highways of data
- Data Analyst reads the map and explains what is happening
- Data Scientist finds patterns and predicts what may happen
- ML Engineer turns the model into a useful product feature

### Technical understanding

Each role works with different parts of the data value chain.

- Data engineering focuses on collection, storage, ETL, data quality, and pipeline reliability.
- Data analysis focuses on descriptive statistics, dashboards, business reporting, and experimentation.
- Data science focuses on model building, inference, and experimentation.
- Machine learning engineering focuses on deployment, monitoring, optimization, and serving models at scale.

## IMPORTANT TERMS EXPLAINED

- ETL: extract, transform, load
- Pipeline: a sequence of steps that moves and processes data
- Serving: making a model available for predictions in an application
- Experimentation: evaluating changes to improve a product or system
- Production: the real deployed environment where users interact with the system

## SUPPLEMENTARY: Why these roles are different

These roles are often combined in startups and small teams, but in larger organizations they are separate. The core difference is not intelligence or ability but the kind of problem each role solves.

A data analyst may prioritize business metrics and dashboards; a data scientist may prioritize prediction accuracy; an ML engineer may prioritize scalability, reliability, and throughput.

## INTERVIEW EXTENSION

Q: Which role is closest to model deployment?

A: ML Engineer.

Q: Which role is most focused on data pipeline reliability?

A: Data Engineer.

Q: Which role is most focused on business insights?

A: Data Analyst.

Q: Which role usually drives model experimentation?

A: Data Scientist.

## Practical Python example

```python
import pandas as pd

# Example of a business dataset used in analytics and modeling
sales = pd.DataFrame({
    'region': ['north', 'south', 'east', 'west', 'north', 'south'],
    'sales': [1200, 950, 1400, 1100, 1300, 980],
    'orders': [40, 31, 52, 38, 45, 33]
})

print(sales.groupby('region')['sales'].sum())
```

Expected output:

```text
region
north    2500
south    1930
east    1400
west    1100
dtype: int64
```

### Why this matters

This is the kind of work that analysts and scientists do before building production-grade ML systems: summarizing the signal in the data and understanding patterns.

## Common mistakes

- Thinking all data roles are the same
- assuming ML Engineers just write notebooks
- ignoring that production systems need infrastructure and monitoring
- forgetting that business context matters as much as technical ability

## Practice

1. Explain the difference between a Data Engineer and an ML Engineer.
2. Which role would you choose for building a predictive model from scratch?
3. What role is most needed for data pipeline reliability?
4. Why might one team member need to work across multiple roles in a startup?

## Code-to-practice mapping

- Original concept: role taxonomy in the ML ecosystem
- Supplementary concept: workflow ownership and team responsibilities
- Code: grouping and summarizing business data
- Practice: mapping data tasks to role responsibilities
