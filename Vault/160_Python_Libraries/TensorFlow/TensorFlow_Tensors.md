---
tags:
  - python
  - tensorflow
  - tf
  - tensor
  - data_structure
  - numerical_computing
  - concept
  - example
aliases:
  - TF Tensors
  - TensorFlow Tensor
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[_NumPy_MOC|NumPy ndarray]]"
  - "[[TensorFlow_Variables]]"
  - "[[TensorFlow_Operations]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-09
---
# TensorFlow: Tensors (`tf.Tensor`)

## Definition
A **tensor** is the primary data structure used in TensorFlow. Conceptually, tensors are multi-dimensional arrays with a uniform data type (like `float32`, `int32`, `string`). They are very similar to [[_NumPy_MOC|NumPy `ndarray`s]] and, in fact, TensorFlow tensors can be easily converted to and from NumPy arrays.

Tensors are characterized by:
1.  **Rank (Order or Number of Dimensions):**
    -   Scalar (Rank 0 tensor): A single number, e.g., `tf.constant(5)`
    -   Vector (Rank 1 tensor): A 1D array, e.g., `tf.constant()`
    -   Matrix (Rank 2 tensor): A 2D array, e.g., `tf.constant([,])`
    -   Rank 3 tensor: A 3D array (e.g., a batch of images, where each image is 2D, or a color image [height, width, channels]).
    -   And so on for higher ranks.
2.  **Shape:** A tuple of integers describing the size of each dimension.
    -   Scalar: Shape `()`
    -   Vector of length 3: Shape `(3,)`
    -   Matrix of 2 rows, 3 columns: Shape `(2, 3)`
3.  **Data Type (`dtype`):** The type of data stored in the tensor (e.g., `tf.float32`, `tf.int64`, `tf.string`, `tf.bool`). All elements in a tensor must have the same data type.

## Key Properties of `tf.Tensor` Objects
-   **Immutability:** `tf.Tensor` objects are immutable. Once created, their values cannot be changed. To store model parameters that need to be updated during training, TensorFlow uses [[TensorFlow_Variables|`tf.Variable`]].
-   **GPU Acceleration:** TensorFlow operations on tensors can be transparently accelerated on GPUs (and TPUs) if available and TensorFlow is configured correctly.
-   **Integration with NumPy:**
    -   TensorFlow operations automatically convert NumPy ndarrays to Tensors.
    -   TensorFlow Tensors can be converted to NumPy ndarrays using the `.numpy()` method (in Eager Execution mode).

## Creating Tensors

[list2tab|#Tensor Creation]
- From Python Lists/NumPy Arrays
    -
        ```python
        import tensorflow as tf
        import numpy as np

        # Scalar (Rank 0)
        scalar_tensor = tf.constant(42)
        # print("Scalar Tensor:", scalar_tensor)
        # print("Rank:", tf.rank(scalar_tensor).numpy())
        # print("Shape:", scalar_tensor.shape)
        # print("Dtype:", scalar_tensor.dtype)

        # Vector (Rank 1)
        vector_py_list = 
        vector_tensor = tf.constant(vector_py_list)
        # print("\nVector Tensor (from list):", vector_tensor)

        vector_np_array = np.array()
        vector_tensor_np = tf.constant(vector_np_array, dtype=tf.float32) # Specify dtype
        # print("Vector Tensor (from NumPy, float32):", vector_tensor_np)

        # Matrix (Rank 2)
        matrix_py_list = [,]
        matrix_tensor = tf.constant(matrix_py_list)
        # print("\nMatrix Tensor:\n", matrix_tensor)
        # print("Shape:", matrix_tensor.shape)

        # Higher Rank Tensor
        tensor3d = tf.constant([[,], [,]]) # Shape (2,2,2)
        # print("\n3D Tensor:\n", tensor3d)
        ```
    -   `tf.constant()` creates an immutable tensor.
- Special Tensors
    -
        ```python
        import tensorflow as tf

        # Tensor of zeros
        zeros_tensor = tf.zeros(shape=(2, 3), dtype=tf.int32)
        # print("Zeros Tensor:\n", zeros_tensor)

        # Tensor of ones
        ones_tensor = tf.ones(shape=(3, 2)) # Default dtype is float32
        # print("\nOnes Tensor:\n", ones_tensor)

        # Tensor with values from a normal distribution
        random_normal_tensor = tf.random.normal(shape=(2, 2), mean=0.0, stddev=1.0)
        # print("\nRandom Normal Tensor:\n", random_normal_tensor)

        # Tensor with values from a uniform distribution
        random_uniform_tensor = tf.random.uniform(shape=(2, 2), minval=0, maxval=10, dtype=tf.int32)
        # print("\nRandom Uniform Tensor (int):\n", random_uniform_tensor)

        # Identity matrix (requires tf.linalg)
        # eye_tensor = tf.eye(num_rows=3, num_columns=3, dtype=tf.float32)
        # print("\nIdentity Matrix:\n", eye_tensor)
        ```
    -   `tf.zeros()`, `tf.ones()`, `tf.fill(dims, value)`, `tf.random.*` functions.
- Casting Data Type
    -
        ```python
        import tensorflow as tf
        int_tensor = tf.constant()
        float_tensor_casted = tf.cast(int_tensor, dtype=tf.float64)
        # print("Original int tensor:", int_tensor)
        # print("Casted to float64 tensor:", float_tensor_casted)
        ```
    -   Use `tf.cast()` to change the `dtype` of a tensor.

## Indexing and Slicing
Tensor indexing and slicing work very similarly to NumPy arrays.
```python
import tensorflow as tf
matrix = tf.constant([,,])

# Get an element
# print("Element (0,1):", matrix.numpy()) # -> 2

# Get a row
# print("Row 1:", matrix.numpy()) # -> [4 5 6]

# Get a column (using ... or tf.newaxis for full slice)
# print("Column 2:", matrix[:, 2].numpy()) # -> [3 6 9]

# Slice a sub-matrix
# print("Sub-matrix (rows 0-1, cols 1-2):\n", matrix[0:2, 1:3].numpy())
# [[2 3]
#  [5 6]]
```

## Operations on Tensors
Most standard mathematical operations are available in TensorFlow and operate element-wise on tensors, similar to NumPy. These are covered more in [[TensorFlow_Operations]].
```python
import tensorflow as tf
a = tf.constant()
b = tf.constant()

# Element-wise operations
# add_result = tf.add(a, b) # or a + b
# multiply_result = tf.multiply(a, b) # or a * b
# print("a+b:", add_result)
# print("a*b:", multiply_result)

# Matrix multiplication
# matrix_a = tf.constant([,])
# matrix_b = tf.constant([,])
# matmul_result = tf.matmul(matrix_a, matrix_b)
# print("Matrix A @ Matrix B:\n", matmul_result)
```

## Role in Deep Learning
Tensors are the lifeblood of deep learning models:
-   **Input Data:** Images, text (as numerical sequences), audio are represented as tensors. (e.g., a batch of images might be a 4D tensor: `[batch_size, height, width, channels]`).
-   **Model Parameters:** Weights and biases of neural network layers are stored as tensors (specifically, [[TensorFlow_Variables|`tf.Variable`]]s).
-   **Activations:** Outputs of layers during the forward pass are tensors.
-   **Gradients:** Gradients computed during backpropagation are also tensors.

Understanding how to create, manipulate, and operate on tensors is fundamental to working effectively with TensorFlow.

---