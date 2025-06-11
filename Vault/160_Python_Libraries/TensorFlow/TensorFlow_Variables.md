---
tags:
  - python
  - tensorflow
  - tf
  - variable
  - mutable_state
  - model_parameters
  - concept
  - example
aliases:
  - tf.Variable
  - TensorFlow Mutable Tensors
  - TF Variables
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Tensors|TF Tensors]]"
  - "[[TensorFlow_Automatic_Differentiation|TF Automatic Differentiation]]"
  - "[[Keras_Layers]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow: Variables (`tf.Variable`)

While [[TensorFlow_Tensors|`tf.Tensor` objects]] are immutable (their values cannot be changed once created), machine learning models require **mutable state** to store and update parameters like weights and biases during training. In TensorFlow, this mutable state is handled by **`tf.Variable`**.

## Definition
A `tf.Variable` is a special type of tensor whose value can be changed by running operations on it. It represents a tensor whose value can be modified by running ops (e.g., `assign()`, `assign_add()`). Variables are primarily used to store and update the trainable parameters of a model.

## Key Characteristics
-   **Mutability:** Unlike `tf.Tensor` objects, the value of a `tf.Variable` can be changed after its creation using methods like `assign()`, `assign_add()`, `assign_sub()`.
-   **Trainable by Default:** By default, `tf.Variable` objects are marked as "trainable." This means they are automatically tracked by `tf.GradientTape` for [[TensorFlow_Automatic_Differentiation|automatic differentiation]], allowing gradients to be computed with respect to them during backpropagation.
-   **Initialization:** Variables must be initialized with a value when created.
-   **Shape and `dtype`:** Like tensors, variables have a shape and a data type (`dtype`) which are typically fixed after creation (though some shape flexibility exists with `shape=tf.TensorShape(None)` or `validate_shape=False`, it's less common for standard model parameters).
-   **Placement:** TensorFlow can place variables on different devices (CPU, GPU, TPU).

## Creating Variables
Variables are created using the `tf.Variable()` constructor.

```python
import tensorflow as tf

# 1. Creating a scalar variable
initial_value_scalar = 0.0
my_scalar_var = tf.Variable(initial_value_scalar, name="my_scalar", dtype=tf.float32)
# print("Scalar Variable:", my_scalar_var)
# print("Name:", my_scalar_var.name)
# print("Dtype:", my_scalar_var.dtype)
# print("Shape:", my_scalar_var.shape)
# print("Initial Value:", my_scalar_var.numpy()) # Access value as NumPy array

# 2. Creating a vector variable from a list
initial_value_vector = 
my_vector_var = tf.Variable(initial_value_vector, name="my_vector")
# print("\nVector Variable:\n", my_vector_var)

# 3. Creating a matrix variable from a NumPy array
import numpy as np
initial_value_matrix_np = np.array([,,], dtype=np.float32)
my_matrix_var = tf.Variable(initial_value_matrix_np, name="my_matrix")
# print("\nMatrix Variable:\n", my_matrix_var)

# 4. Specifying trainability
# non_trainable_var = tf.Variable(initial_value=5.0, trainable=False, name="non_trainable")
# print("\nNon-trainable Variable, Trainable:", non_trainable_var.trainable)
```

## Modifying Variable Values
The primary way to change the value of a `tf.Variable` is through its `assign` methods:
-   `variable.assign(new_value)`: Assigns a new value to the variable.
-   `variable.assign_add(delta)`: Adds `delta` to the variable (equivalent to `variable = variable + delta`).
-   `variable.assign_sub(delta)`: Subtracts `delta` from the variable (equivalent to `variable = variable - delta`).

```python
# (Continuing from above, assuming my_scalar_var is defined)
# print(f"\nInitial scalar_var value: {my_scalar_var.numpy()}")

# my_scalar_var.assign(100.0)
# print(f"After assign(100.0): {my_scalar_var.numpy()}")

# my_scalar_var.assign_add(10.0)
# print(f"After assign_add(10.0): {my_scalar_var.numpy()}") # Should be 110.0

# my_scalar_var.assign_sub(5.0)
# print(f"After assign_sub(5.0): {my_scalar_var.numpy()}") # Should be 105.0

# Note: Operations like `my_scalar_var = my_scalar_var + 1` create a new tf.Tensor,
# they do NOT update the variable in-place unless re-assigned with .assign().
# new_tensor = my_scalar_var + 1 # new_tensor is a tf.Tensor, my_scalar_var is unchanged
# my_scalar_var.assign(my_scalar_var + 1) # This updates my_scalar_var
```

## Role in Machine Learning / Deep Learning
`tf.Variable` objects are fundamental for training machine learning models:
1.  **Model Parameters:** Weights and biases in neural network [[Keras_Layers|layers]] are typically `tf.Variable`s.
    -   When you define a layer in `tf.keras` (e.g., `tf.keras.layers.Dense(...)`), the layer automatically creates and manages its weights and biases as `tf.Variable`s. These are usually initialized when the layer is first called with input data (build step).
2.  **Training:**
    -   During the training process, an [[Keras_Optimizers|optimizer]] (e.g., Adam, SGD) calculates gradients of the [[Keras_Loss_Functions|loss function]] with respect to these trainable variables using [[TensorFlow_Automatic_Differentiation|`tf.GradientTape`]].
    -   The optimizer then applies these gradients to update the values of the `tf.Variable`s, thereby "learning" the optimal parameters.
    ```python
    # Conceptual training step
    # W = tf.Variable(tf.random.normal((num_features, num_classes)))
    # b = tf.Variable(tf.zeros(num_classes))

    # with tf.GradientTape() as tape:
    #     logits = tf.matmul(inputs, W) + b
    #     loss = compute_loss_function(labels, logits) # Some loss function
    
    # gradients = tape.gradient(loss, [W, b]) # Compute gradients w.r.t. W and b
    # optimizer.apply_gradients(zip(gradients, [W, b])) # Optimizer updates W and b
    ```
3.  **Stateful Operations:** Variables can also be used to maintain other kinds of state in a model, such as the non-trainable running mean and variance in `BatchNormalization` layers.

## Variables and `tf.function`
When using `tf.function` to compile Python functions into TensorFlow graphs for performance, `tf.Variable`s maintain their stateful nature across function calls within the graph. Python variables or `tf.Tensor`s inside a `tf.function` are typically traced into constants in the graph for each distinct value they take.

## Converting to Tensors
You can get the current value of a `tf.Variable` as an immutable `tf.Tensor` using:
-   `variable.value()`: Returns a `tf.Tensor` snapshot of the variable's current value.
-   `variable.numpy()`: Returns a NumPy array of the variable's current value (if in Eager Execution).
-   Simply using the variable in a TensorFlow operation often implicitly converts it to a tensor for that operation.

`tf.Variable` is the mechanism by which TensorFlow models store and update the parameters that are learned during the training process, making them a cornerstone of building and training models.

---