# 030 — Function Transformer and Distribution Transformations

## Source traceability
- Course: CampusX — 100 Days of Machine Learning
- Lesson: 030
- Transcript title: "Function Transformer _ Log Transform _ Reciprocal Transform _ Square Root Transform"
- Transcript file: `030 - 2021-04-16 - Function Transformer _ Log Transform _ Reciprocal Transform _ Square Root Transform.txt`
- Topic: distribution transformation and function-based preprocessing

## Learning objectives
- Understand the purpose of function transforms in feature engineering.
- Learn why log and square-root transforms are used for skewed data.
- Explain when reciprocal transforms are useful.
- Use `FunctionTransformer` in scikit-learn.

## Original CampusX concept
The lecture explains that some feature distributions are badly skewed and may not be suitable for models that assume a more symmetric distribution. By applying a transformation such as a log, square-root, or reciprocal function, the feature can become more manageable.

This is a classic preprocessing move when data is highly skewed or spread across a wide range.

## Common transformations

### Log transformation
The log transform is:

$$
 y = \log(x)
$$

This compresses large values and expands small values. It is especially useful for right-skewed data.

### Square-root transformation
The square-root transform is:

$$
 y = \sqrt{x}
$$

This is milder than the log transform and useful when values are positive but still skewed.

### Reciprocal transformation
The reciprocal transform is:

$$
 y = \frac{1}{x}
$$

This strongly compresses large values. It is useful in some domains but can distort low values.

## Why these transforms help
They alter the distribution so extreme values do not dominate training. They are especially useful when:
- income is highly skewed
- counts are very uneven
- values span multiple orders of magnitude

## Python example
```python
import numpy as np

x = np.array([1, 10, 100, 1000, 10000], dtype=float)
print('log:', np.log(x))
print('sqrt:', np.sqrt(x))
print('reciprocal:', 1 / x)
```

Expected output:
```text
log: [0.         2.30258509 4.60517019 6.90775528 9.21034037]
sqrt: [1. 3.16227766 10. 31.6227766 100. ]
reciprocal: [1.00000000e+00 1.00000000e-01 1.00000000e-02 1.00000000e-03 1.00000000e-04]
```

## scikit-learn `FunctionTransformer`
```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

transformer = FunctionTransformer(np.log1p, validate=True)
X = np.array([[0.0], [1.0], [10.0]])
print(transformer.transform(X))
```

## Common mistakes
- applying a log transform to negative values without checking the domain
- using reciprocal transforms on zero values
- transforming the target variable when the business interpretation should remain in original units
- over-transforming data that is already reasonable

## Key takeaways
- Function transforms can stabilize skewed distributions.
- Log and square-root transforms are common for positive, right-skewed variables.
- Reciprocal transform is powerful but can be extreme.
- Transformation choice should be driven by data behavior and business meaning.

## Practice questions
1. Why would a log transformation help a highly skewed distribution?
2. When is a reciprocal transformation risky?
3. What is the difference between a log transform and a square-root transform?
4. How do these transforms affect the interpretation of feature values?

## Source reference
- Transcript title: "Function Transformer _ Log Transform _ Reciprocal Transform _ Square Root Transform"
- File: `030 - 2021-04-16 - Function Transformer _ Log Transform _ Reciprocal Transform _ Square Root Transform.txt`
