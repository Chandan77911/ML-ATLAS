# 011 — What are Tensors?

## Source traceability

- Course: CampusX — 100 Days of Machine Learning
- Lesson: 011
- Transcript title: "What are Tensors _ Tensor In-depth Explanation _ Tensor in Machine Learning"
- Transcript file: `011 - 2021-03-25 - What are Tensors _ Tensor In-depth Explanation _ Tensor in Machine Learning.txt`
- Topic: tensor foundations
- Subtopic: scalars, vectors, matrices, and tensors in ML

## Original CampusX concept

The transcript introduces tensors as the core data structure used in machine learning and deep learning. A tensor is a generalization of numbers, vectors, and matrices to higher dimensions.

### Beginner intuition

A tensor is just a container of numbers arranged in a structured way.

- a single number is a scalar
- a list of numbers is a vector
- a grid of numbers is a matrix
- multiple grids together form a tensor

### Technical understanding

A tensor has:

- shape: the size along each dimension
- rank: the number of dimensions
- dtype: the numeric type such as float32 or int64

For example:

- scalar: shape = ()
- vector: shape = (n,)
- matrix: shape = (m, n)
- 3D tensor: shape = (batch, height, width)

In ML, data often arrives as tensors. Images are often tensors with shape like $(H, W, C)$ or $(N, H, W, C)$ depending on the convention.

## IMPORTANT FORMULA AND NOTATION

A tensor can be thought of as an array $T$ with elements indexed by multiple dimensions:

$$
T \in \mathbb{R}^{d_1 \times d_2 \times \cdots \times d_n}
$$

where each $d_i$ is the size of dimension $i$.

This is the mathematical generalization of vectors and matrices.

## SUPPLEMENTARY: Why tensors matter

Modern ML frameworks such as PyTorch and TensorFlow use tensors because they are efficient for linear algebra and automatic differentiation. Tensors allow batch processing, matrix multiplication, and gradient calculation during optimization.

## INTERVIEW EXTENSION

Q: What is a tensor?

A: A tensor is a multidimensional array of numbers.

Q: What is the difference between a vector and a matrix?

A: A vector is 1D and a matrix is 2D.

Q: Why are tensors important in deep learning?

A: They store inputs, weights, activations, and gradients in a computationally efficient format.

## Practical Python example

```python
import numpy as np

# Scalar, vector, matrix, and tensor
scalar = np.array(5)
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("scalar shape:", scalar.shape)
print("vector shape:", vector.shape)
print("matrix shape:", matrix.shape)
print("tensor shape:", tensor.shape)
```

Expected output:

```text
scalar shape: ()
vector shape: (3,)
matrix shape: (2, 2)
tensor shape: (2, 2, 2)
```

## Common mistakes

- thinking tensors are only used in deep learning
- confusing rank with number of elements
- assuming a tensor must be 3D or higher

## Practice

1. Give one example of a scalar, vector, matrix, and tensor.
2. What is shape in tensor terminology?
3. Why are tensors useful in ML frameworks?
4. Explain the difference between rank and shape.

## Code-to-practice mapping

- Original concept: tensor as a multidimensional numerical container
- Supplementary concept: shape, rank, and deep learning relevance
- Code: NumPy examples of different tensor shapes
- Practice: conceptual understanding of array structure in ML
