# 002 — AI vs ML vs DL for Beginners

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 002
- Transcript title: "AI Vs ML Vs DL for Beginners in Hindi"
- Transcript file: `002 - 2021-03-15 - AI Vs ML Vs DL for Beginners in Hindi.txt`
- Topic: foundations
- Subtopic: relationship between AI, machine learning, and deep learning

## Original CampusX concept

The instructor explains the relationship using nested circles:

- AI is the broadest field: making machines behave intelligently
- ML is a subset of AI: systems learn patterns from data
- Deep learning is a subset of ML: models with layered representations learned from data

The transcript also contrasts modern ML with older symbolic AI. In symbolic AI, humans wrote an expert rule system or if-else logic. That works on narrow, well-defined tasks but fails when the problem is fuzzy, high-dimensional, or difficult to express as rules.

### Beginner intuition

Think of the relationship like this:

- AI = the overall goal of intelligent machines
- ML = a major way to achieve AI by learning patterns from examples
- Deep learning = a special type of ML that learns many layers of features automatically

### Technical understanding

If you want a very practical mental model:

- AI asks, “Can a machine act intelligently?”
- ML asks, “Can a machine learn patterns from data?”
- Deep learning asks, “Can a neural network learn representations automatically, without manual feature engineering?”

The transcript highlights that many real problems, like image recognition or speech recognition, are too complex to solve with explicit rules. Deep learning became powerful because it can learn features directly from raw inputs, such as pixel values or audio waveforms.

## IMPORTANT TERMS EXPLAINED

- Artificial Intelligence (AI): the broad field of building machine behavior that seems intelligent
- Machine Learning (ML): a subset of AI where models learn from data
- Deep Learning (DL): a subset of ML using multi-layer neural networks
- Symbolic AI: rule-based systems with hand-written logic
- Expert system: a program that encodes expert knowledge as rules
- Fuzzy logic: situations where the pattern is not clearly expressible in fixed rules

## SUPPLEMENTARY: Why the different layers matter

The nested-circle view is useful because it shows the historical progression.

1. Early AI focused on explicit human-coded rules.
2. That failed on hard-to-specify tasks.
3. Machine learning learned patterns directly from data.
4. Deep learning pushed this further by learning hierarchical features.

This progression explains why deep learning is not separate from machine learning; it is a specialized and more powerful family inside ML.

## INTERVIEW EXTENSION

Q: Why is deep learning not the same as AI?

A: AI is the broader field. Deep learning is one technique used within AI and ML.

Q: Why did expert systems become limited?

A: Because they struggle with problems that are fuzzy, high-dimensional, or difficult to encode manually.

Q: Is every ML system deep learning?

A: No. Many ML systems are simpler statistical or tree-based models that do not require neural networks.

## Practical Python example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
print(round(model.score(X_test, y_test), 3))
```

Expected output:

```text
0.974
```

### Why this example matters

This is a simple ML model that learns from examples and predicts the class of a new flower measurement. It is not deep learning, but it is still clearly within the broad ML family.

## COMMON MISTAKES AND MISCONCEPTIONS

- Treating AI and ML as exact synonyms
- Thinking deep learning is the same thing as AI
- Assuming every intelligent system must be neural-network based
- Forgetting that rule-based AI still exists, but is not always the best solution

## Practice

1. Draw the three-circle diagram from memory.
2. Explain why expert systems struggle in fuzzy tasks.
3. Write one real-world example for AI, one for ML, and one for DL.
4. Explain why image classification is harder for symbolic rules than for data-driven learning.

## Code-to-practice mapping

- Original concept: ML as part of AI, with deep learning nested inside it
- Supplementary concept: expert systems vs data-driven learning
- Code: a simple ML model using the Iris dataset
- Practice: conceptual classification of AI/ML/DL use-cases
