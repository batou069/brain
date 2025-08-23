---
tags:
  - python
  - pytorch
  - torch
  - tensor
  - data_structure
  - numerical_computing
  - concept
  - example
aliases:
  - PyTorch Tensors
  - torch.Tensor
related:
  - "[[160_Python_Libraries/PyTorch/_PyTorch_MOC|_PyTorch_MOC]]"
  - "[[_NumPy_MOC|NumPy ndarray]]"
  - "[[PyTorch_Autograd]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-08-20
---
# PyTorch: Tensors (`torch.Tensor`)

## Definition
A **`torch.Tensor`** is the primary data structure in PyTorch. It is a multi-dimensional array, conceptually identical to a [[_NumPy_MOC|NumPy `ndarray`]], but with two key additions:
1.  **GPU Acceleration:** Tensors can be moved to and processed on a GPU to significantly accelerate computation.
2.  **Automatic Differentiation:** Tensors can keep track of the operations performed on them to automatically compute gradients, which is the foundation of [[PyTorch_Autograd|`torch.autograd`]] for training neural networks.

Like NumPy arrays, tensors have a `dtype` (e.g., `torch.float32`, `torch.long`) and a `shape`.

## Creating Tensors

[list2tab|#Tensor Creation]
- From Python Lists/NumPy Arrays
    -
        ```python
        import torch
        import numpy as np

        # From a Python list
        data_list = [,]
        tensor_from_list = torch.tensor(data_list)
        print("Tensor from list:\n", tensor_from_list)
        print("Shape:", tensor_from_list.shape)
        print("Dtype:", tensor_from_list.dtype) # Infers dtype (e.g., torch.int64)

        # From a NumPy array (shares memory by default, very efficient)
        data_numpy = np.array([,], dtype=np.float32)
        tensor_from_numpy = torch.from_numpy(data_numpy)
        print("\nTensor from NumPy:\n", tensor_from_numpy)
        print("Dtype:", tensor_from_numpy.dtype)

        # To convert a tensor back to NumPy
        numpy_from_tensor = tensor_from_numpy.numpy()
        print("\nNumPy array from tensor:\n", numpy_from_tensor)
        ```
    -   `torch.tensor()` always copies the data. `torch.from_numpy()` shares memory.
- Special Tensors
    -
        ```python
        import torch

        # Tensor of zeros with a specific shape
        shape = (2, 3)
        zeros_tensor = torch.zeros(shape)
        print("Zeros Tensor:\n", zeros_tensor)

        # Tensor of ones
        ones_tensor = torch.ones(shape)
        print("\nOnes Tensor:\n", ones_tensor)

        # Tensor with random values from a uniform distribution on [0, 1)
        rand_tensor = torch.rand(shape)
        print("\nRandom Uniform Tensor:\n", rand_tensor)

        # Tensor with random values from a standard normal distribution (mean=0, var=1)
        randn_tensor = torch.randn(shape)
        print("\nRandom Normal Tensor:\n", randn_tensor)
        ```
    -   Functions like `torch.zeros_like(input_tensor)` create a tensor of zeros with the same shape as another tensor.
- Casting Data Type
    -
        ```python
        import torch
        int_tensor = torch.tensor()
        float_tensor = int_tensor.to(torch.float32) # Preferred way
        # or float_tensor = int_tensor.float()
        print("Original int tensor:", int_tensor.dtype)
        print("Casted to float32 tensor:", float_tensor.dtype)
        ```
    -   Use the `.to(dtype)` method or convenience methods like `.float()`, `.long()`, `.int()`.

## Tensor Operations
Operations on PyTorch tensors are syntactically similar to NumPy.

```python
import torch
t1 = torch.tensor([,])
t2 = torch.tensor([,])

# Element-wise addition
add_result = t1 + t2
# or: add_result = torch.add(t1, t2)
print("t1 + t2:\n", add_result)

# Element-wise multiplication
mul_result = t1 * t2
# or: mul_result = torch.multiply(t1, t2)
print("\nt1 * t2 (element-wise):\n", mul_result)

# Matrix multiplication
matmul_result = t1 @ t2
# or: matmul_result = torch.matmul(t1, t2)
print("\nt1 @ t2 (matrix multiplication):\n", matmul_result)

# In-place operations (modify the tensor)
print("\nOriginal t1:\n", t1)
t1.add_(t2) # The underscore denotes an in-place operation
print("t1 after t1.add_(t2):\n", t1)
```

## Indexing and Slicing
Tensor indexing and slicing are identical to NumPy.
```python
import torch
matrix = torch.tensor([,,])

# Get an element
print("Element (0,1):", matrix.item()) # .item() to get standard Python number

# Get a row
print("Row 1:", matrix)

# Get a column
print("Column 2:", matrix[:, 2])
```

## Tensors and GPU
One of the most powerful features of PyTorch is the ability to seamlessly move computations to a CUDA-enabled GPU.

```python
import torch

# Check if CUDA (GPU support) is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Create a tensor on the CPU
cpu_tensor = torch.randn(3, 3)
print("\nTensor on CPU:\n", cpu_tensor)

# Move the tensor to the GPU (if available)
gpu_tensor = cpu_tensor.to(device)
print("\nTensor on GPU (or CPU if no GPU):\n", gpu_tensor)

# Operations on the GPU tensor will be executed on the GPU
gpu_result = gpu_tensor * gpu_tensor + 2
print("\nResult of GPU computation:\n", gpu_result)

# To bring a tensor back to the CPU (e.g., to convert to NumPy)
cpu_result = gpu_result.to("cpu")
numpy_result = cpu_result.numpy()
```
> **Note:** You cannot directly convert a GPU tensor to a NumPy array. You must first move it back to the CPU: `tensor.to("cpu").numpy()`.

Tensors are the fundamental building blocks for all models and computations in PyTorch. Their NumPy-like API makes them easy to learn, while their GPU and autograd capabilities make them incredibly powerful for deep learning.

---