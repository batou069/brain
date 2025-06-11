---
tags:
  - python
  - tensorflow
  - tf
  - automatic_differentiation
  - autodiff
  - gradient_tape
  - gradients
  - backpropagation
  - concept
  - example
aliases:
  - tf.GradientTape
  - TensorFlow Autodiff
  - Gradient Computation TF
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Variables|TF Variables]]"
  - "[[TensorFlow_Tensors|TF Tensors]]"
  - "[[TensorFlow_Operations]]"
  - "[[Calculus_Derivatives|Derivatives]]"
  - "[[Gradient]]"
  - "[[Backpropagation_Algorithm]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow: Automatic Differentiation with `tf.GradientTape`

**Automatic Differentiation (Autodiff)** is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. TensorFlow uses autodiff to compute gradients, which are essential for optimizing machine learning models (e.g., neural networks) using gradient-based methods like gradient descent.

The primary tool for automatic differentiation in TensorFlow (especially in Eager Execution mode or within `@tf.function`) is **`tf.GradientTape`**.

## `tf.GradientTape`
-   **Purpose:** Records operations executed within its context ("tape") to compute gradients using reverse mode automatic differentiation (backpropagation).
-   **How it Works:**
    1.  You define a `tf.GradientTape()` context.
    2.  Inside this context, any TensorFlow operations involving **trainable** [[TensorFlow_Variables|`tf.Variable`s]] (or [[TensorFlow_Tensors|`tf.Tensor`s]] explicitly "watched" by the tape) are recorded.
    3.  After the forward pass computations are done within the tape's context, you call `tape.gradient(target, sources)` to compute the gradient of a `target` scalar (e.g., loss) with respect to a list of `sources` (e.g., model weights/variables).
-   **Key Features:**
    -   **Persistent Tapes:** By default, a `GradientTape` is released after `tape.gradient()` is called once. To compute multiple gradients over the same computation, create a persistent tape: `with tf.GradientTape(persistent=True) as tape:`. Remember to `del tape` when done with a persistent tape to free resources.
    -   **Watching Tensors:** By default, `GradientTape` only tracks operations involving trainable `tf.Variable`s. To compute gradients with respect to a `tf.Tensor`, you must explicitly tell the tape to "watch" it using `tape.watch(my_tensor)`.
    -   **Higher-Order Gradients:** You can nest `GradientTape` contexts to compute higher-order derivatives (e.g., gradients of gradients, like the Hessian).

## Basic Usage

**Example 1: Gradient of a simple function w.r.t. a Variable**
```python
import tensorflow as tf

# Define a trainable variable
x = tf.Variable(3.0, name="x_var")

with tf.GradientTape() as tape:
  # Define a function y = x^2
  y = x * x 
  # y = x**2 # Also works

# Compute the gradient of y with respect to x (dy/dx)
# dy_dx should be 2*x = 2*3.0 = 6.0
dy_dx = tape.gradient(y, x)

# print(f"x = {x.numpy()}")
# print(f"y = x^2 = {y.numpy()}")
# print(f"dy/dx = {dy_dx.numpy()}") # Expected: 6.0
```

**Example 2: Gradients of a loss w.r.t. multiple model parameters (Variables)**
```python
import tensorflow as tf

# Conceptual model parameters
W = tf.Variable(tf.random.normal((2, 1)), name="weights") # Shape (features, output_units)
b = tf.Variable(tf.zeros(1), name="bias")       # Shape (output_units,)

# Conceptual input data and target
x_input = tf.constant([,], dtype=tf.float32) # Shape (batch_size, features)
y_true = tf.constant([[]], dtype=tf.float32) # Shape (batch_size, output_units)

with tf.GradientTape() as tape:
    # Forward pass: y_pred = x_input @ W + b
    y_pred = tf.matmul(x_input, W) + b
    # Simple squared error loss
    loss = tf.reduce_mean(tf.square(y_true - y_pred))

# Compute gradients of loss with respect to W and b
gradients = tape.gradient(loss, [W, b])
dW = gradients[0]
db = gradients[1]

# print(f"Loss: {loss.numpy()}")
# print("Gradient w.r.t. W (dW):\n", dW.numpy())
# print("Gradient w.r.t. b (db):\n", db.numpy())

# These gradients would then be used by an optimizer to update W and b
# optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
# optimizer.apply_gradients(zip(gradients, [W, b]))
# print("\nAfter one optimization step:")
# print("Updated W:\n", W.numpy())
# print("Updated b:\n", b.numpy())
```

**Example 3: Watching a `tf.Tensor` and Persistent Tape**
```python
import tensorflow as tf

x0 = tf.constant(3.0) # A constant tensor, not a Variable
x1 = tf.Variable(2.0) # A variable

with tf.GradientTape(persistent=True) as tape:
  tape.watch(x0) # Explicitly watch the tensor x0
  y0 = x0 * x0
  y1 = x1 * x1 * x0 # y1 = x1^2 * x0

# Gradients
# dy0_dx0 = tape.gradient(y0, x0) # dy0/dx0 = 2*x0 = 6.0
# dy1_dx0 = tape.gradient(y1, x0) # dy1/dx0 = x1^2 = 4.0
# dy1_dx1 = tape.gradient(y1, x1) # dy1/dx1 = 2*x1*x0 = 2*2*3 = 12.0

# print(f"dy0/dx0: {dy0_dx0.numpy() if dy0_dx0 is not None else 'None'}")
# print(f"dy1/dx0: {dy1_dx0.numpy() if dy1_dx0 is not None else 'None'}")
# print(f"dy1/dx1: {dy1_dx1.numpy() if dy1_dx1 is not None else 'None'}")

del tape # Important to delete persistent tapes when done
```-   **Note:** If `tape.gradient()` returns `None` for a source, it means the target is not connected to that source in the recorded computation graph, or the source was not "watched" (if it's a Tensor) or was marked `trainable=False` (if it's a Variable).

## How it Works (Reverse Mode Autodiff / Backpropagation)
1.  **Forward Pass Recording:** As operations are executed within the `tf.GradientTape` context, TensorFlow builds a record of the sequence of operations (the "tape") and any intermediate values needed for gradient computation.
2.  **Backward Pass (Gradient Calculation):** When `tape.gradient(target, sources)` is called, TensorFlow traverses this recorded graph of operations in reverse order (from `target` back to `sources`).
3.  It applies the **chain rule** of calculus at each step to compute the gradients of the `target` with respect to the `sources`.

This process is essentially what happens during [[Backpropagation_Algorithm|backpropagation]] in neural networks.

## Use in `tf.keras`
While `tf.GradientTape` can be used for custom training loops, the `tf.keras` high-level API largely abstracts this away:
-   When you compile a `tf.keras.Model` with an optimizer and loss, and then call `model.fit()`, Keras automatically uses `tf.GradientTape` internally to compute gradients and apply updates to the model's trainable variables.
-   However, for custom training logic, research, or when subclassing `tf.keras.Model` and overriding `train_step`, you would use `tf.GradientTape` explicitly.

## Controlling Gradients
-   **`tf.stop_gradient(tensor)`:** Prevents gradients from flowing through a particular tensor during backpropagation. Useful if you want to treat a part of your computation as a constant with respect to differentiation.
-   **`trainable=False` for `tf.Variable`:** Variables created with `trainable=False` will not be tracked by default, and `tape.gradient()` will return `None` for them. This is useful for freezing layers or parts of a model during training.

Automatic differentiation via `tf.GradientTape` is a cornerstone of TensorFlow, enabling the efficient training of complex models by automatically handling the intricate process of gradient computation.

---