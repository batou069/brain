---
tags:
  - python
  - tensorflow
  - tf
  - operations
  - math_ops
  - tf_function
  - graph_execution
  - concept
  - example
aliases:
  - TensorFlow Ops
  - tf.function
  - TF Math Operations
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Tensors|TF Tensors]]"
  - "[[TensorFlow_Variables]]"
  - "[[TensorFlow_Graphs_Eager_Execution|TF Graphs and Eager Execution]]"
  - "[[_NumPy_MOC|NumPy]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow: Operations (`tf.math`, `tf.linalg`, `tf.function`)

TensorFlow provides a rich set of operations (ops) that can be performed on [[TensorFlow_Tensors|Tensors]] and [[TensorFlow_Variables|Variables]]. These operations form the basis of computations in TensorFlow models. Many of these operations are similar to those found in [[_NumPy_MOC|NumPy]] but are optimized for execution on various hardware (CPUs, GPUs, TPUs) and for building computation graphs.

## Categories of Operations

[list2tab|#TF Operation Categories]
- Element-wise Mathematical Operations (`tf.math`)
    -   These operations apply a mathematical function to each element of a tensor independently.
    -   **Examples:**
        -   `tf.add(x, y)` or `x + y`
        -   `tf.subtract(x, y)` or `x - y`
        -   `tf.multiply(x, y)` or `x * y` (element-wise product, NOT matrix multiplication)
        -   `tf.divide(x, y)` or `x / y`
        -   `tf.pow(x, y)` or `x ** y`
        -   `tf.exp(x)`: $e^x$
        -   `tf.log(x)`: Natural logarithm $\ln(x)$
        -   `tf.sqrt(x)`
        -   `tf.sin(x)`, `tf.cos(x)`, `tf.tan(x)`
        -   `tf.abs(x)`
        -   `tf.round(x)`
        -   `tf.maximum(x, y)`, `tf.minimum(x, y)` (element-wise max/min)
        -   `tf.logical_and(x, y)`, `tf.logical_or(x, y)`, `tf.logical_not(x)` (for boolean tensors)
    -   **Example:**
        ```python
        import tensorflow as tf
        a = tf.constant()
        b = tf.constant()

        # c = tf.add(a, b)  # c will be tf.Tensor(, shape=(3,), dtype=int32)
        # d = tf.multiply(a, 3) # d will be tf.Tensor(, shape=(3,), dtype=int32)
        # e = tf.math.log(tf.cast(b, tf.float32)) # Cast b to float for log
        # print("a+b:", c.numpy())
        # print("a*3:", d.numpy())
        # print("log(b):", e.numpy())
        ```
- Matrix Operations (`tf.linalg` and others)
    -   Operations specific to matrices (2D tensors) or higher-rank tensors involving matrix-like properties.
    -   **Examples:**
        -   `tf.matmul(a, b)` or `a @ b`: Matrix multiplication.
        -   `tf.transpose(a, perm=None)`: Transposes a tensor. `perm` specifies permutation for higher-rank tensors.
        -   `tf.linalg.inv(matrix)`: Computes matrix inverse.
        -   `tf.linalg.det(matrix)`: Computes matrix determinant.
        -   `tf.linalg.eig(matrix)`: Computes eigenvalues and eigenvectors (for general matrices).
        -   `tf.linalg.eigh(matrix)`: Computes eigenvalues and eigenvectors for Hermitian/symmetric matrices.
        -   `tf.linalg.svd(matrix)`: Computes Singular Value Decomposition.
        -   `tf.linalg.trace(matrix)`: Computes the trace (sum of diagonal elements).
        -   `tf.eye(num_rows, num_columns=None, ...)`: Creates an identity matrix.
    -   **Example:**
        ```python
        import tensorflow as tf
        # matrix_a = tf.constant([,], dtype=tf.float32)
        # matrix_b = tf.constant([,], dtype=tf.float32)

        # product = tf.matmul(matrix_a, matrix_b)
        # print("Matrix Product (A @ B):\n", product.numpy())

        # transpose_a = tf.transpose(matrix_a)
        # print("\nTranspose of A:\n", transpose_a.numpy())
        ```
- Reduction Operations (`tf.reduce_*`)
    -   Reduce tensor dimensions by performing an operation along specified axes.
    -   **Examples:**
        -   `tf.reduce_sum(input_tensor, axis=None, keepdims=False)`
        -   `tf.reduce_mean(input_tensor, axis=None, keepdims=False)`
        -   `tf.reduce_max(input_tensor, axis=None, keepdims=False)`
        -   `tf.reduce_min(input_tensor, axis=None, keepdims=False)`
        -   `tf.reduce_prod(input_tensor, axis=None, keepdims=False)`
        -   `tf.reduce_all(boolean_tensor, axis=None, keepdims=False)` (logical AND)
        -   `tf.reduce_any(boolean_tensor, axis=None, keepdims=False)` (logical OR)
    -   `axis`: The dimension(s) to reduce. If `None`, reduces all dimensions.
    -   `keepdims`: If `True`, retains reduced dimensions with length 1.
    -   **Example:**
        ```python
        import tensorflow as tf
        # matrix_c = tf.constant([,,], dtype=tf.float32)

        # sum_all_elements = tf.reduce_sum(matrix_c)
        # print("Sum of all elements:", sum_all_elements.numpy()) # 45.0

        # sum_along_rows = tf.reduce_sum(matrix_c, axis=0) # Sum each column
        # print("Sum along rows (sum of each column):", sum_along_rows.numpy()) # [12. 15. 18.]

        # mean_along_cols = tf.reduce_mean(matrix_c, axis=1) # Mean of each row
        # print("Mean along columns (mean of each row):", mean_along_cols.numpy()) # [ 2.  5.  8.]
        ```
- Indexing and Slicing Operations
    -   Similar to NumPy: `tensor[start:stop:step]`, `tensor[index]`, `tensor[..., index]`.
    -   **`tf.gather(params, indices, axis=None)`:** Gathers slices from `params` according to `indices`.
    -   **`tf.gather_nd(params, indices)`:** Gathers slices from `params` into a Tensor with shape `indices.shape[:-1] + params.shape[indices.shape[-1]:]`.
    -   **`tf.where(condition, x=None, y=None)`:** Returns elements chosen from `x` or `y` depending on `condition`. If `x` and `y` are None, returns the coordinates of `True` elements in `condition`.
    -   **`tf.boolean_mask(tensor, mask)`:** Applies a boolean mask to a tensor.
- Reshaping and Shape Manipulation
    -   `tf.reshape(tensor, shape)`
    -   `tf.squeeze(tensor, axis=None)`: Removes dimensions of size 1.
    -   `tf.expand_dims(tensor, axis)`: Inserts a dimension of size 1.
    -   `tf.concat(values, axis)`: Concatenates tensors along an existing axis.
    -   `tf.stack(values, axis=0)`: Stacks a list of rank-R tensors into one rank-(R+1) tensor.
    -   `tf.unstack(value, num=None, axis=0)`: Unstacks a rank-R tensor into a list of rank-(R-1) tensors.
    -   `tf.tile(input, multiples)`: Constructs a tensor by tiling a given tensor.
- Neural Network Specific Operations (`tf.nn`)
    -   This module contains many operations commonly used in neural networks.
    -   **Examples:**
        -   Activation functions: `tf.nn.relu`, `tf.nn.sigmoid`, `tf.nn.tanh`, `tf.nn.softmax`.
        -   Loss functions: `tf.nn.softmax_cross_entropy_with_logits`, `tf.nn.sigmoid_cross_entropy_with_logits`.
        -   Convolution operations: `tf.nn.conv2d`, `tf.nn.depthwise_conv2d`.
        -   Pooling operations: `tf.nn.max_pool`, `tf.nn.avg_pool`.
        -   Normalization: `tf.nn.moments`, `tf.nn.batch_normalization` (though `tf.keras.layers.BatchNormalization` is usually preferred).
    -   Many of these are wrapped by higher-level [[Keras_Layers|`tf.keras.layers`]].

## `tf.function` Decorator
-   **Purpose:** In TensorFlow 2.x (with [[TensorFlow_Graphs_Eager_Execution|Eager Execution]] by default), Python functions involving TensorFlow operations are executed imperatively. The `@tf.function` decorator can be used to **compile a Python function into a callable TensorFlow graph**.
-   **Benefits:**
    -   **Performance:** Graphs can be optimized by TensorFlow (e.g., pruning unused nodes, fusing operations) and can lead to significant speedups, especially for complex computations or when running on GPUs/TPUs.
    -   **Portability:** Graphs can be saved (as SavedModel) and deployed to various environments (TensorFlow Serving, TensorFlow Lite, TensorFlow.js) without needing the Python code.
    -   **Graph Mode Features:** Allows use of graph-specific control flow (e.g., `tf.cond`, `tf.while_loop`) which can be more efficient than Python control flow in graphs.
-   **How it Works (AutoGraph):** TensorFlow uses a feature called AutoGraph to convert Python control flow (if, for, while) into TensorFlow graph operations.
-   **Tracing:** When a `@tf.function`-decorated function is called for the first time with a new set of input signatures (shapes and dtypes of tensor arguments, or values of Python arguments), it is "traced." This means TensorFlow executes the Python code once, records the sequence of TensorFlow operations as a graph, and then caches this graph. Subsequent calls with the same input signature will use the cached graph.
-   **Example:**
    ```python
    import tensorflow as tf

    # Define a Python function with TF ops
    # def my_python_func(x, y):
    #     print("Python function executed (tracing or eager)") # Will print during tracing
    #     return tf.matmul(x, y) + tf.reduce_sum(x)

    # Decorate with @tf.function
    # @tf.function
    # def my_tf_func(x, y):
    #     print("TF function Python code executed (tracing)") # Will print only during tracing
    #     return tf.matmul(x, y) + tf.reduce_sum(x)

    # matrix1 = tf.constant([,], dtype=tf.float32)
    # matrix2 = tf.constant([,], dtype=tf.float32)

    # print("--- Calling Python function (eager) ---")
    # result_eager = my_python_func(matrix1, matrix2)
    # print(result_eager)
    # result_eager_again = my_python_func(matrix1, matrix2) # Python code runs again
    # print(result_eager_again)

    # print("\n--- Calling @tf.function decorated function ---")
    # result_graph = my_tf_func(matrix1, matrix2) # Tracing happens here, "TF function Python code executed" prints
    # print(result_graph)
    # result_graph_again = my_tf_func(matrix1, matrix2) # Uses cached graph, "TF function Python code executed" does NOT print again
    # print(result_graph_again)

    # # Example with a different input signature (will re-trace)
    # matrix3 = tf.constant([,,], dtype=tf.float32) # Different shape
    # result_graph_new_shape = my_tf_func(matrix3, matrix2) # Tracing happens again
    # print(result_graph_new_shape)
    ```
-   **Considerations with `tf.function`:**
    -   Side effects (like printing from Python, appending to lists) in the Python code will only happen during tracing, not during subsequent graph executions.
    -   [[TensorFlow_Variables|`tf.Variable`]]s are handled correctly (state is maintained).
    -   Python non-Tensor arguments can trigger re-tracing if their values change. It's often better to pass Tensors as arguments if possible.

TensorFlow's rich set of operations, combined with the ability to compile Python code into optimized graphs using `tf.function`, provides a powerful and flexible environment for numerical computation and deep learning.

---