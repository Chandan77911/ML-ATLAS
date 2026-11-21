# 016 — Working with JSON and SQL

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 016
- Transcript title: "Working with JSON_SQL _ Day 16 _ 100 Days of Machine Learning"
- Transcript file: `016 - 2021-03-31 - Working with JSON_SQL _ Day 16 _ 100 Days of Machine Learning.txt`
- Topic: data ingestion
- Subtopic: structured data sources using JSON and SQL

## Original CampusX concept

The transcript introduces two very common data access patterns in ML and analytics:

- JSON: a lightweight structured data format commonly used in APIs and web services
- SQL: a language for querying relational databases

The lesson teaches that ML projects often start with data stored in formats beyond CSV, and that a practical data pipeline needs to handle those formats.

### Beginner intuition

CSV is simple, but many real systems store data in JSON or in databases. A good ML workflow needs to handle all of them.

### Technical understanding

JSON is hierarchical and often used when data is nested or semi-structured. SQL is used when data lives in tables with relationships between entities.

Typical operations include:

- reading JSON records into a DataFrame
- flattening nested structures
- querying a database with SQL
- selecting columns and filtering rows

## IMPORTANT TERMS EXPLAINED

- JSON: JavaScript Object Notation; a human-readable structured format
- SQL: Structured Query Language; used for relational database queries
- Relational database: a database made of tables with rows and columns
- Query: a request for data from a database
- Nested data: data values that are embedded within other data values, such as a list within a record

## SUPPLEMENTARY: Why these formats matter

Most real-world systems pull data from APIs, logs, or databases. For example, event data might arrive in JSON and customer data may live in a SQL table. ML projects must be able to join and preprocess those sources.

## INTERVIEW EXTENSION

Q: Why should an ML engineer know JSON and SQL?

A: Because data often comes from APIs and production databases, not just CSV files.

Q: What is the advantage of using SQL?

A: It allows efficient filtering, aggregation, and joins across tables.

Q: When is JSON more useful than CSV?

A: When the dataset includes nested or semi-structured values.

## Practical Python example: JSON

```python
import json
import pandas as pd

records = [
    {"id": 1, "name": "Alice", "skills": ["Python", "SQL"]},
    {"id": 2, "name": "Bob", "skills": ["AI", "ML"]}
]

json_data = json.dumps(records)
parsed = json.loads(json_data)
df = pd.DataFrame(parsed)
print(df)
```

Expected output:

```text
   id   name              skills
0   1  Alice  [Python, SQL]
1   2    Bob      [AI, ML]
```

## Practical Python example: SQL

```python
import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)')
cur.execute('INSERT INTO users VALUES (1, "Alice", 25)')
cur.execute('INSERT INTO users VALUES (2, "Bob", 30)')
print(cur.execute('SELECT * FROM users WHERE age > 20').fetchall())
```

Expected output:

```text
[(1, 'Alice', 25), (2, 'Bob', 30)]
```

## Common mistakes

- assuming all data is stored in one simple format
- ignoring nested JSON structures
- forgetting that database queries must be efficient and intentional

## Practice

1. What is the main difference between JSON and CSV?
2. When would you use SQL instead of loading a file directly?
3. Why is nested JSON harder to work with than flat CSV data?
4. What are the advantages of querying a database instead of reading everything into memory?

## Code-to-practice mapping

- Original concept: using JSON and SQL in a real data pipeline
- Supplementary concept: data extraction and preparation for ML
- Code: JSON parsing and SQLite querying examples
- Practice: understanding real-world data sources and storage formats
