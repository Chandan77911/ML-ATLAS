# 024 — Feature Scaling: Standardization

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 024
- Transcript title: "Feature Scaling - Standardization _ Day 24 _ 100 Days of Machine Learning"
- Transcript file: `024 - 2021-04-09 - Feature Scaling - Standardization _ Day 24 _ 100 Days of Machine Learning.txt`
- Topic: feature scaling and standardization

## Learning objectives
- Define feature scaling and explain why it matters.
- Understand standardization as a scaling method.
- Compute the z-score transformation and interpret its meaning.
- Understand why some algorithms are sensitive to feature magnitude.

## Original CampusX concept
The transcript introduces feature scaling as a final preprocessing step in the feature engineering pipeline. After missing values, transformations, and encoding, features are often brought onto a similar scale before being passed to a model.

The instructor uses different units such as age, salary, and IQ to explain why some models behave badly when one feature dominates simply because its values are much larger in magnitude.

## Why feature scaling is needed
Many algorithms are sensitive to the scale of the input features. Distance-based models such as KNN and SVM are especially affected because their objective functions depend on the geometry of the feature space.

If one feature ranges from 1000 to 5000 and another ranges from 0 to 10, the larger-scale feature dominates distance calculations. The model may ignore the smaller feature even if it is important.

### Beginner intuition
Imagine comparing two students using age and salary. If salary is in thousands and age is in tens, one variable will dominate the distance calculation. Scaling brings both variables onto a similar footing so that neither unfairly controls the result.

### Technical understanding
Feature scaling is the process of transforming independent variables so they share a common range or variance. Standardization is one of the most common approaches.

## Mathematical foundation: standardization
The z-score transformation is:

$$
 z_i = \frac{x_i - \mu}{\sigma}
$$

Where:
- $x_i$ is one value in the feature column
- $\mu$ is the mean of the feature
- $\sigma$ is the standard deviation
- $z_i$ is the standardized value

This transformation centers the data around zero and scales the spread to one standard deviation.

After standardization:
- mean becomes approximately 0
- standard deviation becomes approximately 1

This is why standardization is also called z-score normalization.

### Example
Suppose the feature values are:

$$
[20, 24, 28, 32]
$$

Mean:

$$
\mu = \frac{20 + 24 + 28 + 32}{4} = 26
$$

Standard deviation is about $5.29$.

Then the standardized value of $20$ is:

$$
z = \frac{20 - 26}{5.29} \approx -1.14
$$

This shows that $20$ is about $1.14$ standard deviations below the mean.

## Python example
```python
import pandas as pd

ages = pd.Series([20, 24, 28, 32, 36, 40])
mean = ages.mean()
std = ages.std(ddof=0)

standardized = (ages - mean) / std
print('mean:', standardized.mean())
print('std:', standardized.std(ddof=0))
print(standardized.round(3).to_list())
```

Expected output:
```text
mean: 0.0
std: 1.0
[-1.414, -0.707, 0.0, 0.707, 1.414, 2.121]
```

## Why standardization helps
Standardization helps in algorithms that rely on:
- Euclidean distance
- gradient descent optimization
- covariance structure
- regularization

It prevents features with large numeric ranges from dominating optimization or the geometry of the model.

## Common mistakes
- applying standardization after train/test split incorrectly
- standardizing the target variable when the task is supervised regression
- using standardization on sparse or one-hot encoded features without understanding the algorithm
- forgetting that scaling is usually done on numerical columns only

## Key takeaways
- Feature scaling brings different features onto a comparable range.
- Standardization is the z-score transformation.
- It is especially useful for distance-based and gradient-based algorithms.
- It does not change the relative order of values; it only changes their center and spread.

## Practice questions
1. What is feature scaling and why is it important?
2. Write the standardization formula and define each symbol.
3. Why do KNN and SVM often benefit from scaling?
4. What happens to the mean and standard deviation after standardization?

## Source reference
- Transcript title: "Feature Scaling - Standardization _ Day 24 _ 100 Days of Machine Learning"
- File: `024 - 2021-04-09 - Feature Scaling - Standardization _ Day 24 _ 100 Days of Machine Learning.txt`
