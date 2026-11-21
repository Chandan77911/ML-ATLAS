# 018 — Fetching Data Using Web Scraping

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 018
- Transcript title: "Fetching data using Web Scraping _ Day 18 _ 100 Days of Machine Learning"
- Transcript file: `018 - 2021-04-02 - Fetching data using Web Scraping _ Day 18 _ 100 Days of Machine Learning.txt`
- Topic: data acquisition
- Subtopic: extracting structured information from websites without APIs

## Original CampusX concept

The transcript introduces web scraping as a way to extract data when a website does not provide an official API. The instructor uses AmbitionBox and explains the idea of sending browser-like headers so the request is accepted.

### Beginner intuition

If a website does not share data via an API, you may still be able to retrieve information from the HTML page itself and parse it.

### Technical understanding

Web scraping generally involves:

- sending an HTTP request to the webpage
- receiving HTML content
- parsing the page structure
- selecting relevant tags and data fields
- storing the extracted results into a DataFrame

The key challenge is that HTML is a document structure, not a clean data table by default.

## IMPORTANT TERMS EXPLAINED

- HTML: HyperText Markup Language
- BeautifulSoup: a Python library for parsing HTML
- Requests: a library used to send HTTP requests
- Selector: a way to locate specific HTML tags or attributes
- 403: a common HTTP response indicating access is denied or restricted

## SUPPLEMENTARY: Why scraping is a practical skill

Many real-world datasets live on the web. Web scraping is useful when no API exists or when you need to collect publicly visible data for research or business analysis.

## INTERVIEW EXTENSION

Q: Why do websites sometimes block scraping requests?

A: They may detect bot traffic and reject requests to protect their system or content.

Q: What is the purpose of a browser-like header?

A: It makes the request appear to come from a web browser instead of an automated bot.

## Practical Python example

```python
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.example.com'
page = requests.get(url, headers=headers)
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title)
```

Expected output:

```text
200
<title>Example Domain</title>
```

## Common mistakes

- not using proper headers when sites block bots
- scraping without checking rate limits or terms of service
- selecting overly broad HTML structures
- failing to handle missing or dynamic content

## Practice

1. Why do websites sometimes return 403 to automated requests?
2. What is the role of BeautifulSoup?
3. In what situations would scraping be useful even when an API is unavailable?
4. Why is HTML structure important in scraping?

## Key takeaway

Web scraping is a useful data acquisition technique when direct APIs are unavailable, but it requires caution, respect for site restrictions, and careful parsing of HTML content.
