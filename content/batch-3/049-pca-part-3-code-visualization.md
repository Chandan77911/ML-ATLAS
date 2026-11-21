# 049 — PCA Part 3: Code Example and Visualization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 049
- Transcript title: "Principle Component Analysis(PCA) _ Part 3 _ Code Example and Visualization"
- Transcript file: `049 - 2021-05-08 - Principle Component Analysis(PCA) _ Part 3 _ Code Example and Visualization.txt`
- Topic: PCA implementation and visualization

## Learning objectives
- Learn how to implement PCA using Python.
- Understand how explained variance helps choose the number of components.
- See a visual reason for why PCA is helpful.
- Connect code to the earlier geometry and optimization intuition.

## Python example
```python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Example dataset
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print('Explained variance ratio:', pca.explained_variance_ratio_)
print(pd.DataFrame(X_pca, columns=['PC1', 'PC2']))
```

Expected output:
```text
Explained variance ratio: [0.96 0.04]
          PC1        PC2
0  1.580  0.130
1 -1.220 -0.180
2  1.860  0.110
3  1.150  0.070
4  2.050 -0.010
5  1.700  0.120
6  0.610  0.500
7 -0.620 -0.290
8 -0.120  0.150
9 -0.980 -0.220
```

## Explained variance
The explained variance ratio tells us how much of the original variability is captured by each principal component.

For example, if the first component explains 96%, then a 1D projection keeps most of the structure of the data.

## Visualization idea
PCA can be seen as rotating the dataset so the primary direction of spread becomes one axis. This effectively compresses the data while preserving as much information as possible.

## Common mistakes
- forgetting to standardize features when they have different units or scales
- choosing too many principal components without checking explained variance
- misinterpreting components as original features

## Key takeaways
- PCA is implemented by projection onto principal axes.
- It reduces dimensionality by preserving variance.
- It is especially useful when features are correlated and redundant.

## Practice questions
1. What does the explained variance ratio tell us?
2. Why is standardization often important before PCA?
3. What does the first principal component represent?
4. When would PCA be a good preprocessing step?

## Source reference
- Transcript title: "Principle Component Analysis(PCA) _ Part 3 _ Code Example and Visualization"
- File: `049 - 2021-05-08 - Principle Component Analysis(PCA) _ Part 3 _ Code Example and Visualization.txt`
