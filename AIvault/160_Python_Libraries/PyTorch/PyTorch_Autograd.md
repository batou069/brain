---
tags:
  - python
  - pytorch
  - torch
  - autograd
  - automatic_differentiation
  - backpropagation
  - gradient
  - concept
  - example
aliases:
  - PyTorch Autograd
  - Automatic Differentiation in PyTorch
  - torch.autograd
related:
  - "[[160_Python_Libraries/PyTorch/_PyTorch_MOC|_PyTorch_MOC]]"
  - "[[PyTorch_Tensors]]"
  - "[[PyTorch_Neural_Network_Module_nn]]"
  - "[[TensorFlow_Automatic_Differentiation|TensorFlow GradientTape]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-08-20
---
# PyTorch: Automatic Differentiation with `torch.autograd`

`torch.autograd` is PyTorch's automatic differentiation engine that powers the training of neural networks. It allows for the automatic computation of gradients for any computational graph.

## Core Concepts
At its core, `autograd` works by keeping track of operations performed on [[PyTorch_Tensors|tensors]] and then replaying them backward to compute gradients (a process known as **backpropagation** or reverse-mode automatic differentiation).

To enable this, a `torch.Tensor` has two important attributes:
-   **`tensor.requires_grad`**: A boolean. If `True`, `autograd` will track all operations on this tensor.
-   **`tensor.grad`**: This attribute is populated with the gradient of some scalar loss function with respect to the tensor.
-   **`tensor.grad_fn`**: A reference to the function that created the tensor as a result of an operation.

## Example: Simple Gradient Calculation
```python
import torch

# Create a tensor and set requires_grad=True to track computation
x = torch.tensor(2.0, requires_grad=True)
w = torch.tensor(5.0, requires_grad=True)
b = torch.tensor(-3.0, requires_grad=True)

# Define a simple computation (a linear layer)
y = w * x + b

# Define a "loss" function (e.g., squared error from a target of 0)
loss = y**2

print(f"x: {x}")
print(f"w: {w}")
print(f"b: {b}")
print(f"y = w*x + b = {y}")
print(f"loss = y^2 = {loss}")

# Now, compute gradients using backpropagation
loss.backward()

# The gradients are now stored in the .grad attribute of the tensors
# d(loss)/dw = 2y * x = 2 * 7 * 2 = 28
# d(loss)/dx = 2y * w = 2 * 7 * 5 = 70
# d(loss)/db = 2y * 1 = 2 * 7 * 1 = 14

print("\n--- Gradients after loss.backward() ---")
print(f"Gradient of loss w.r.t. x (dl/dx): {x.grad}")
print(f"Gradient of loss w.r.t. w (dl/dw): {w.grad}")
print(f"Gradient of loss w.r.t. b (dl/db): {b.grad}")
```

## Disabling Gradient Tracking
Sometimes, you need to perform operations without tracking them for gradient computation, for example, during model evaluation (inference).

[list2tab|#Disabling Gradients]
- `torch.no_grad()`
    -   **Purpose:** A context manager that disables gradient calculation within its block.
    -   **Example:**
        ```python
        print(f"x.requires_grad: {x.requires_grad}")
        with torch.no_grad():
            z = w * x + b # This computation is not tracked
            print(f"z.requires_grad: {z.requires_grad}")
        print(f"x.requires_grad (after block): {x.requires_grad}") # Unchanged
        ```
- `tensor.detach()`
    -   **Purpose:** Creates a new tensor that shares the same storage as the original tensor but is detached from the computation graph.
    -   **Example:**
        ```python
        y_detached = y.detach()
        print(f"y.requires_grad: {y.requires_grad}")
        print(f"y_detached.requires_grad: {y_detached.requires_grad}")
        ```

## Role in Training a Neural Network
The `autograd` system is the engine that makes the standard PyTorch training loop possible:
1.  **`optimizer.zero_grad()`**: Clear the old gradients.
2.  **`outputs = model(inputs)`**: Perform a forward pass.
3.  **`loss = loss_fn(outputs, labels)`**: Calculate the loss.
4.  **`loss.backward()`**: Compute gradients.
5.  **`optimizer.step()`**: Update model parameters.

---