# 017 — Fetching Data From an API

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 017
- Transcript title: "Fetching Data From an API | Day 17 | 100 Days of Machine Learning"
- Transcript file: `017 - 2021-04-01 - Fetching Data From an API _ Day 17 _ 100 Days of Machine Learning.txt`
- Topic: data acquisition
- Subtopic: using APIs to fetch machine-readable data

## Original CampusX concept

The transcript explains that an API is an interface that lets two software systems communicate. In data science, APIs are often the cleanest way to get structured data from a service without manually downloading files.

The instructor uses the TMDB API as a practical example. The idea is that a request can be sent to a server with parameters such as a movie category or an API key, and the server returns JSON.

### Beginner intuition

An API is a bridge between programs. Instead of manually copying data, one program asks another program for data and receives a structured answer.

### Technical understanding

In a typical request:

- the client sends an HTTP request to an API endpoint
- the endpoint validates the request
- the server returns a JSON response
- the data is parsed into a Python object or DataFrame

This is a standard pattern in real ML pipelines.

## IMPORTANT TERMS EXPLAINED

- API: Application Programming Interface
- Endpoint: a specific URL for a data resource or action
- JSON: a lightweight structured data format often returned by APIs
- Request: a message sent to the server
- Response: data returned by the server
- API key: a token used to authenticate requests

## SUPPLEMENTARY: Why APIs matter

APIs are hugely important in production ML because they let systems pull real-time or regularly updated data. This is common in finance, e-commerce, weather, and recommendation systems.

## INTERVIEW EXTENSION

Q: What is an API in simple words?

A: An interface that allows one software system to request data or actions from another.

Q: Why is JSON commonly used in APIs?

A: It is lightweight, readable, and easy to parse in Python and JavaScript.

Q: Why are API keys needed?

A: They help the service control access and rate limits.

## Practical Python example

```python
import requests
import pandas as pd

api_key = "your_api_key_here"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"
response = requests.get(url)
print(response.status_code)

data = response.json()
movies = data.get("results", [])
df = pd.DataFrame(movies)
print(df[['title', 'vote_average']].head())
```

Expected output:

```text
200
                          title  vote_average
0  Dilwale Dulhania Le Jayenge         8.7
1          Gabriel's Inferno II         8.4
2                    Wolfwalkers         8.4
```

## Common mistakes

- forgetting to include required parameters or headers
- not checking the HTTP status code
- assuming the response is already a DataFrame
- not handling rate limits and API usage restrictions

## Practice

1. Explain why APIs are useful in real-world ML systems.
2. What is the difference between an API endpoint and a response?
3. Which Python library is commonly used to make API requests?
4. Why is JSON a natural format for API data?

## Key takeaway

APIs are one of the most common ways to fetch data in modern ML systems. The key skill is turning a structured API response into a usable dataset for analysis and model building.
