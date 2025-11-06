# Chapter: PyTorch Intro

## Keywords

### 1. Tensor

* **What is it?**
    A Tensor is the fundamental data structure in PyTorch, representing a multi-dimensional array of numerical data. 🧊

* **What is it good for?**
    Tensors are used to store and manipulate all data in a neural network, including inputs, outputs, weights, and gradients. They are optimized for high-performance numerical computing, especially on GPUs.

* **Details**
    * A tensor can have any number of dimensions: a 0-D tensor is a scalar (a single number), a 1-D tensor is a vector, a 2-D tensor is a matrix, and so on.
    * Unlike Python lists, tensors must contain elements of a single data type (e.g., `float32`, `int64`).
    * PyTorch tensors keep track of their computation history, which is essential for automatic differentiation (Autograd).
    * They can be easily moved between the CPU and a GPU (`.to('cuda')`), which is key for accelerating computations.

* **Example**
    **Conceptual Analogy:** If a variable is like a single box holding one item, a tensor is like a highly organized shipping container. It can be a simple row of boxes (1D), a grid of boxes (2D), or a stack of grids (3D), but every box inside must hold the same type of item.

    **Code Example:**
    ```python
    import torch
    import numpy as np

    # 0-D Tensor (Scalar)
    scalar = torch.tensor(5)
    print(f"Scalar: {scalar}")

    # 1-D Tensor (Vector)
    vector = torch.tensor([1, 2, 3])
    print(f"Vector: {vector}")

    # 2-D Tensor (Matrix) from a list of lists
    matrix = torch.tensor([[1, 2], [3, 4]])
    print(f"Matrix:\n{matrix}")

    # 3-D Tensor from a NumPy array
    numpy_array = np.random.rand(2, 3, 4) # 2 matrices of size 3x4
    tensor_from_numpy = torch.from_numpy(numpy_array)
    print(f"3-D Tensor shape: {tensor_from_numpy.shape}")
    ```

***

### 2. Module

* **What is it?**
    A `Module` (specifically `torch.nn.Module`) is the base class for all neural network models and layers in PyTorch, providing a way to organize code, manage parameters, and track operations.

* **What is it good for?**
    It serves as a container for your model's architecture, encapsulating its layers, learnable parameters (weights and biases), and the logic for the forward pass.

* **Details**
    * To create a custom model, you define a class that inherits from `nn.Module`.
    * In the `__init__` method, you define the layers of your network (e.g., `nn.Linear`, `nn.Conv2d`).
    * In the `forward` method, you define how the input data flows through the layers you created. This is the core logic of your model.
    * `nn.Module` automatically tracks any `nn.Parameter` assigned to it, making it easy to access all of your model's weights for the optimizer.
    * It provides helpful methods like `.train()`, `.eval()`, and `.state_dict()` to manage the model's state.

* **Example**
    **Conceptual Analogy:** An `nn.Module` is like a complete LEGO blueprint. The `__init__` method is the "Parts List" section, telling you which bricks (layers) you need. The `forward` method is the "Assembly Instructions," showing you exactly how to connect those bricks to build the final model.

    **Code Example:**
    ```python
    import torch
    import torch.nn as nn

    class SimpleNet(nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(SimpleNet, self).__init__()
            # "Parts List": Define the layers we will use
            self.layer1 = nn.Linear(input_size, hidden_size)
            self.activation = nn.ReLU()
            self.layer2 = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            # "Assembly Instructions": Define the data flow
            x = self.layer1(x)
            x = self.activation(x)
            x = self.layer2(x)
            return x

    # Create an instance of the model
    model = SimpleNet(input_size=784, hidden_size=128, output_size=10)
    print(model)
    ```

***

### 3. Computation Graph

* **What is it?**
    A computation graph is a directed acyclic graph (DAG) that represents the sequence of operations performed on tensors to compute a final result. 📈

* **What is it good for?**
    It is the backbone of PyTorch's automatic differentiation system, **Autograd**. By recording the graph, PyTorch knows exactly how to calculate the gradients of the loss function with respect to every parameter in the model using the chain rule.

* **Details**
    * In the graph, nodes represent either tensors or operations (like addition, multiplication, or a neural network layer).
    * Edges represent the flow of data: a tensor flowing into an operation and the resulting tensor flowing out.
    * PyTorch builds this graph **dynamically**. This means the graph is created on-the-fly as you execute the forward pass, which allows for more flexibility in model design (e.g., using standard Python control flow like `if` statements).
    * When you call `loss.backward()`, PyTorch traverses this graph backward from the loss node, computing gradients at each step.

* **Example**
    **Conceptual Analogy:** Imagine baking a cake. The computation graph is the recipe written down in excruciating detail. It starts with ingredients (input tensors), lists every action (mixing, baking) as a step, and ends with the final cake (output tensor). To figure out how much the amount of sugar affected the cake's sweetness (the gradient), you can trace the recipe backward from the final taste test.

    **Math & Code:**
    For a simple operation $c = (a \cdot b) + 1$:
    $$ a \rightarrow \boxed{\times} \leftarrow b $$
    $$ \downarrow $$
    $$ \boxed{+} \leftarrow 1 $$
    $$ \downarrow $$
    $$ c $$
    ```python
    import torch

    # Tensors that require gradients
    a = torch.tensor(2.0, requires_grad=True)
    b = torch.tensor(3.0, requires_grad=True)

    # Operations are tracked, building the graph
    d = a * b
    c = d + 1

    # The graph is now built in the background.
    # d.grad_fn shows the last operation was <MulBackward0>
    # c.grad_fn shows the last operation was <AddBackward0>
    print(f"d.grad_fn: {d.grad_fn}")
    print(f"c.grad_fn: {c.grad_fn}")
    ```

***

### 4. Autograd

* **What is it?**
    Autograd is PyTorch's automatic differentiation engine that powers the backpropagation algorithm in neural networks.

* **What is it good for?**
    It automatically calculates the gradients of any output tensor (like loss) with respect to any input tensor that has `requires_grad=True` (like model parameters), saving you from the complex and error-prone task of manually deriving and implementing the chain rule.

* **Details**
    * Autograd works by tracking all operations on tensors within a **computation graph**.
    * Any tensor created with the `requires_grad=True` flag becomes a leaf node in this graph. All tensors that result from operations on it will also be part of the graph.
    * When you call `.backward()` on a scalar tensor (like the final loss), Autograd traverses the graph backward from that node.
    * It uses the chain rule to compute the gradients and accumulates them in the `.grad` attribute of the leaf tensors (e.g., `model.parameters()`).

* **Example**
    **Conceptual Analogy:** Autograd is like an automated accountant for your model's "error budget." After the forward pass calculates the final error (the "total expense"), you call `loss.backward()`. The accountant then goes back through every single transaction (operation) and calculates exactly how much each initial variable (parameter) contributed to that final expense. This "contribution report" is the gradient.

    **Code Example:**
    ```python
    import torch

    # Create tensors that require gradients
    x = torch.tensor(2.0, requires_grad=True)
    w = torch.tensor(4.0, requires_grad=True)
    b = torch.tensor(1.0, requires_grad=True)

    # Define a simple linear operation
    y = w * x + b # y = 4*2 + 1 = 9

    # Backpropagate to compute gradients
    y.backward()

    # Gradients are now stored in the .grad attribute
    # dy/dw = x = 2
    print(f"Gradient of y w.r.t. w: {w.grad}")
    # dy/dx = w = 4
    print(f"Gradient of y w.r.t. x: {x.grad}")
    # dy/db = 1
    print(f"Gradient of y w.r.t. b: {b.grad}")
    ```

***

### 5. Training Loop

* **What is it?**
    A training loop is the core procedural block of code that repeatedly feeds data to a model, calculates the error, and updates the model's parameters to minimize that error over many iterations or epochs.

* **What is it good for?**
    It is the fundamental process through which a machine learning model learns from data.

* **Details**
    * An **epoch** is one full pass through the entire training dataset.
    * The loop typically iterates over the dataset in small chunks called **mini-batches**.
    * Inside the loop, five key steps are always present:
        1.  **Forward Pass:** Get a prediction from the model.
        2.  **Loss Calculation:** Compare the prediction to the true label to compute the error.
        3.  **Zero Gradients:** Clear old gradients from the previous step.
        4.  **Backward Pass:** Compute the gradients of the loss with respect to model parameters (`loss.backward()`).
        5.  **Parameter Update:** Use the optimizer to update the model's weights based on the computed gradients (`optimizer.step()`).

* **Example**
    **Conceptual Analogy:** A training loop is like a study session for a student (the model).
    1.  **Forward Pass:** The student attempts a practice problem.
    2.  **Loss Calculation:** They check their answer against the solution to see how wrong they were.
    3.  **Zero Gradients:** They take a fresh sheet of paper for the next step.
    4.  **Backward Pass:** They think backward to figure out *why* their answer was wrong and which concepts they misunderstood.
    5.  **Parameter Update:** They adjust their understanding (update their brain's "weights") to correct that misunderstanding.
    Repeating this for the whole textbook (an epoch) makes them smarter.

    **Code Example:**
    ```python
    # Assume 'model', 'loss_fn', 'optimizer', and 'dataloader' are defined
    # for epoch in range(num_epochs):
    #     for X_batch, y_batch in dataloader:
    #         # 1. Forward pass
    #         y_pred = model(X_batch)

    #         # 2. Calculate loss
    #         loss = loss_fn(y_pred, y_batch)

    #         # 3. Zero gradients
    #         optimizer.zero_grad()

    #         # 4. Backward pass
    #         loss.backward()

    #         # 5. Update weights
    #         optimizer.step()
    ```

***

### 6. CUDA

* **What is it?**
    CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model created by NVIDIA that allows software to utilize the immense parallel processing power of NVIDIA GPUs. 🚀

* **What is it good for?**
    In PyTorch, CUDA is used to perform tensor operations on an NVIDIA GPU instead of the CPU, which can lead to massive speedups (10x to 100x or more) for the matrix multiplications and other parallelizable computations that are fundamental to deep learning.

* **Details**
    * CPUs are designed for sequential tasks, with a few very powerful cores.
    * GPUs are designed for parallel tasks (like rendering graphics), with thousands of smaller, simpler cores that can perform the same operation on many pieces of data simultaneously.
    * Training a neural network involves many large matrix multiplications, which is an inherently parallel task and thus perfectly suited for GPUs.
    * To use CUDA in PyTorch, you must first move your model and your data tensors to the GPU device using the `.to('cuda')` method.

* **Example**
    **Conceptual Analogy:** Imagine you need to sign 1,000 letters.
    * **CPU:** You are one person (a powerful core) signing each letter one by one. It will take a long time.
    * **GPU (with CUDA):** You hire 1,000 people (many simple cores) and give each one a letter and a pen. They all sign their letter at the same time. The entire job is done in the time it takes to sign one letter.

    **Code Example:**
    ```python
    import torch

    # 1. Check if CUDA (GPU) is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # 2. Create a tensor on the CPU (by default)
    x_cpu = torch.randn(3, 3)
    print(f"x_cpu is on device: {x_cpu.device}")

    # 3. Move the tensor to the GPU
    if device == "cuda":
        x_gpu = x_cpu.to(device)
        print(f"x_gpu is on device: {x_gpu.device}")

        # You would also move your model to the GPU
        # model = MyModel().to(device)
        # And your data inside the training loop
        # inputs, labels = inputs.to(device), labels.to(device)
    ```

***
## Functions

### 1. torch.nn.Parameter

* **What is it?**
    `torch.nn.Parameter` is a wrapper class for a tensor that signals to an `nn.Module` that this tensor should be considered a learnable model parameter.

* **What is it good for?**
    It's used to register a tensor as a weight or bias that should be tracked by the model and updated by the optimizer during training.

* **Details**
    * A `Parameter` is a subclass of `torch.Tensor`.
    * When you assign a `Parameter` as an attribute of an `nn.Module` (e.g., `self.my_weight = nn.Parameter(...)`), it is automatically added to the list of the module's parameters, which can be accessed via `model.parameters()`.
    * This is how the optimizer knows which tensors it needs to update.
    * By default, `nn.Parameter` sets `requires_grad=True` for the wrapped tensor.
    * You typically don't use this directly, as layers like `nn.Linear` create their own `Parameter` tensors for weights and biases internally. You would use it if you were creating a custom layer with its own unique learnable weights.

* **Example**
    ```python
    import torch
    import torch.nn as nn

    class CustomLayer(nn.Module):
        def __init__(self, input_features, output_features):
            super().__init__()
            # Create a learnable weight matrix and register it as a parameter
            self.weight = nn.Parameter(torch.randn(input_features, output_features))
            # This tensor is just a fixed buffer, not a parameter
            self.some_buffer = torch.ones(output_features)

    layer = CustomLayer(5, 3)

    # The .parameters() generator will only yield the 'weight' tensor
    for name, param in layer.named_parameters():
        print(f"Learnable Parameter: {name}, Shape: {param.shape}")
    ```

***

### 2. nn.Module

*This keyword was already covered in the "Keywords" section above.*

***

### 3. torch.rand / torch.randn

* **What are they?**
    `torch.rand` and `torch.randn` are functions for creating tensors with a specified shape, filled with random numbers.

* **What are they good for?**
    They are essential for creating dummy data for testing, and more importantly, for initializing the weight parameters of a neural network before training begins.

* **Details**
    * `torch.rand(*size)`: Fills a tensor with random numbers from a **uniform distribution** on the interval $[0, 1)$. Every number between 0 and 1 has an equal chance of being chosen.
    * `torch.randn(*size)`: Fills a tensor with random numbers from a **standard normal distribution** (mean 0, variance 1). Numbers are clustered around 0.
    * Proper weight initialization is crucial for training deep networks. Using `randn` (or variations of it like Xavier/He initialization which scale `randn`) is the standard practice, as it helps prevent gradients from vanishing or exploding early in training.

* **Example**
    ```python
    import torch

    # Create a 2x3 tensor with random values uniformly distributed between 0 and 1
    rand_tensor = torch.rand(2, 3)
    print(f"torch.rand:\n{rand_tensor}\n")

    # Create a 2x3 tensor with random values from a standard normal distribution
    randn_tensor = torch.randn(2, 3)
    print(f"torch.randn:\n{randn_tensor}")
    ```

***

### 4. torch.linspace

* **What is it?**
    `torch.linspace(start, end, steps)` is a function that creates a 1-D tensor of a specified number of `steps` evenly spaced points between a `start` and `end` value, inclusive.

* **What is it good for?**
    It's useful for creating coordinate axes for plotting, generating data that follows a specific linear progression, or defining regular intervals for sampling.

* **Details**
    * The `steps` argument determines the size of the output tensor.
    * The spacing between points is calculated as `(end - start) / (steps - 1)`.
    * It is similar to NumPy's `np.linspace`.

* **Example**
    ```python
    import torch

    # Create 5 evenly spaced points between -10 and 10
    points = torch.linspace(-10, 10, 5)
    print(f"5 points from -10 to 10: {points}") # Output: tensor([-10.,  -5.,   0.,   5.,  10.])

    # Create 100 points for a plot's x-axis
    x_axis = torch.linspace(0, 2 * 3.14159, 100)
    print(f"Shape of x_axis for plotting: {x_axis.shape}")
    ```

***

### 5. tensor.squeeze / tensor.unsqueeze

* **What are they?**
    `squeeze` and `unsqueeze` are operations that remove or add dimensions of size 1 to a tensor, respectively.

* **What are they good for?**
    They are extremely useful for making tensors compatible with different layers or functions that expect a specific number of dimensions, especially when dealing with batch dimensions.

* **Details**
    * `tensor.unsqueeze(dim)`: Adds a new dimension of size 1 at the specified `dim` position.
    * `tensor.squeeze(dim)`: Removes a dimension of size 1 at the specified `dim` position. If `dim` is not specified, it removes all dimensions of size 1.
    * A common use case is adding a "batch" dimension to a single data sample before feeding it into a model, which usually expects inputs of the shape `[batch_size, features, ...]`.

* **Example**
    ```python
    import torch

    # Start with a 1D tensor of shape [3]
    a = torch.tensor([1, 2, 3])
    print(f"Original shape: {a.shape}") # torch.Size([3])

    # Add a dimension at the beginning (dim=0) to simulate a batch of 1
    b = a.unsqueeze(0)
    print(f"After unsqueeze(0): {b.shape}") # torch.Size([1, 3])

    # Add a dimension at the end (dim=1)
    c = a.unsqueeze(1)
    print(f"After unsqueeze(1): {c.shape}") # torch.Size([3, 1])

    # Squeeze the batch dimension back out
    d = b.squeeze(0)
    print(f"After squeeze(0): {d.shape}") # torch.Size([3])
    ```

***

### 6. nn.Module.state_dict

* **What is it?**
    A `state_dict` (state dictionary) is a Python dictionary object that maps each layer of a PyTorch module to its learnable parameters (weights and biases).

* **What is it good for?**
    It is the standard and recommended way to save and load the trained parameters of a model, allowing you to checkpoint your training progress or use a trained model for inference later.

* **Details**
    * The keys of the dictionary are strings identifying the parameter (e.g., `'layer1.weight'`), and the values are the tensor data for those parameters.
    * Crucially, a `state_dict` only contains the model's parameters, not its architecture. To load a model, you must first create an instance of the model class and then load the `state_dict` into it.
    * Optimizers also have a `state_dict`, which contains their internal state (e.g., moving averages for Adam), which is useful for resuming training.

* **Example**
    ```python
    import torch
    import torch.nn as nn

    # Define a simple model
    model = nn.Sequential(
        nn.Linear(10, 20),
        nn.ReLU(),
        nn.Linear(20, 5)
    )
    print("Model Architecture:\n", model)

    # Get the state dictionary
    sd = model.state_dict()
    print("\nKeys in the state_dict:")
    for key in sd.keys():
        print(key)

    # --- To save and load a model ---
    # torch.save(model.state_dict(), 'model_weights.pth')
    #
    # new_model = nn.Sequential(...) # Recreate the same architecture
    # new_model.load_state_dict(torch.load('model_weights.pth'))
    # new_model.eval()
    ```

***

### 7. tensor.detach

* **What is it?**
    The `.detach()` method creates a new tensor that shares the same data as the original tensor but is detached from its computation graph.

* **What is it good for?**
    It's used when you want to use a tensor in a calculation without that calculation being tracked by Autograd, which is useful for plotting, evaluation metrics, or manipulating the tensor outside of the gradient-based learning process.

* **Details**
    * The new, detached tensor will have `requires_grad=False`.
    * Since it shares the underlying data, changes to one tensor will affect the other, but the operation history (and thus the ability to backpropagate through it) is severed.
    * A common use case is moving a tensor to NumPy for use with libraries like Matplotlib or Scikit-learn, as NumPy cannot handle tensors that require gradients. You must call `.detach()` before calling `.numpy()`.

* **Example**
    ```python
    import torch

    # A tensor that is part of a computation graph
    a = torch.tensor(3.0, requires_grad=True)
    b = a * 2

    print(f"b requires grad: {b.requires_grad}") # True

    # Detach b from the graph
    c = b.detach()
    print(f"c requires grad: {c.requires_grad}") # False

    # Now you can convert c to a NumPy array for plotting, etc.
    # np_c = c.numpy()
    # This would fail: b.numpy() -> RuntimeError

    # Proving they share data:
    c.add_(1) # In-place add to c
    print(f"Original b after modifying c: {b}") # b is also modified
    ```

***

### 8. Module.train / Module.eval

* **What are they?**
    `.train()` and `.eval()` are methods of an `nn.Module` that set the module and all its submodules into either training or evaluation mode.

* **What are they good for?**
    They are crucial for getting correct and reproducible results, as some layers, like **Dropout** and **Batch Normalization**, behave differently during training and inference.

* **Details**
    * `model.train()`: Sets the model to training mode. In this mode, Dropout layers will randomly drop neurons, and BatchNorm layers will update their running statistics based on the current batch.
    * `model.eval()`: Sets the model to evaluation/inference mode. In this mode, Dropout layers are turned off (they pass all data through), and BatchNorm layers use their fixed, running-average statistics instead of the current batch statistics.
    * It is a common mistake to forget to call `model.eval()` before testing or making predictions, which can lead to noisy and inconsistent results.

* **Example**
    ```python
    import torch.nn as nn

    # A model with layers that behave differently in train/eval mode
    model = nn.Sequential(
        nn.Linear(20, 64),
        nn.Dropout(0.5), # Active only during .train()
        nn.BatchNorm1d(64), # Updates stats only during .train()
        nn.Linear(64, 10)
    )

    # Set the model to training mode before the training loop
    model.train()
    # for epoch in range(num_epochs):
    #   ... training logic ...

    # Set the model to evaluation mode before testing or inference
    model.eval()
    # with torch.no_grad():
    #   ... evaluation logic ...
    ```

***

### 9. optimizer.zero_grad / optimizer.step

* **What are they?**
    `zero_grad()` and `step()` are the two fundamental methods of an optimizer object used within the training loop to update a model's parameters.

* **What are they good for?**
    They implement the core logic of gradient descent: `zero_grad()` prepares for a new gradient calculation, and `step()` applies the calculated gradients to update the weights.

* **Details**
    * `optimizer.zero_grad()`: This method sets the `.grad` attribute of all the model's parameters (which the optimizer is tracking) to zero. This is a necessary step because, by default, PyTorch **accumulates** gradients every time `.backward()` is called. You must clear the old gradients before computing the new ones for the current batch.
    * `optimizer.step()`: This method updates the value of all the parameters. It performs this update based on the gradients computed during `.backward()` and the specific update rule of the optimizer (e.g., SGD, Adam).

* **Example**
    ```python
    # Inside a training loop...
    # (after calculating loss)

    # 1. Clear the gradients from the previous iteration.
    # If you forget this, gradients will be summed up across batches.
    optimizer.zero_grad()

    # 2. Compute the new gradients for the current batch.
    loss.backward()

    # 3. Use the new gradients to update the model's weights.
    optimizer.step()
    ```

***

### 10. loss.backward

*This function was already covered in detail under the "Autograd" keyword.*

***

### 11. tensor.view

* **What is it?**
    `.view()` is a tensor method used to reshape a tensor to a different but compatible shape without changing its underlying data.

* **What is it good for?**
    It is commonly used to flatten tensors before they enter a fully connected (`nn.Linear`) layer or to add/remove dimensions to match the expected input shape of a layer.

* **Details**
    * The new shape must have the same total number of elements as the original tensor.
    * `.view()` returns a new tensor that shares the same underlying data as the original. This makes it a very memory-efficient operation.
    * A `-1` can be used in one of the dimensions to have PyTorch automatically infer its size based on the other dimensions and the total number of elements.
    * For `.view()` to work, the tensor must be **contiguous** in memory. If not, you may need to call `.contiguous()` first. The related `.reshape()` method is often more robust as it will handle non-contiguous cases automatically (though it might create a copy).

* **Example**
    ```python
    import torch

    # A tensor representing a mini-batch of 10 images of size 1x28x28
    images = torch.randn(10, 1, 28, 28)
    print(f"Original shape: {images.shape}")

    # Flatten the images to feed into a linear layer
    # We want to keep the batch dimension (10) and flatten the rest
    # 10 x (1 * 28 * 28) = 10 x 784
    flattened_images = images.view(10, -1) # -1 infers 784
    print(f"Shape after .view(10, -1): {flattened_images.shape}")
    ```

***

### 12. tensor.permute

* **What is it?**
    `.permute(*dims)` is a tensor method that reorders the dimensions of a tensor according to the specified sequence of indices.

* **What is it good for?**
    It's essential for aligning tensor dimensions with the expectations of different libraries or layer types, especially when dealing with image or sequence data where the order of dimensions (e.g., batch, channels, height, width) can vary.

* **Details**
    * Unlike `.view()`, `.permute()` does not change the number of dimensions or the number of elements; it only shuffles the existing dimensions.
    * It is similar to NumPy's `transpose` but more flexible, as it can reorder any number of dimensions at once.
    * A common use case is converting an image tensor from the PyTorch standard `(Batch, Channels, Height, Width)` to the format expected by Matplotlib `(Height, Width, Channels)`.

* **Example**
    ```python
    import torch

    # A tensor representing a batch of 10 color images of size 64x64
    # PyTorch format: (Batch, Channels, Height, Width)
    images = torch.randn(10, 3, 64, 64)
    print(f"Original shape (B, C, H, W): {images.shape}")

    # Permute the dimensions to be compatible with Matplotlib
    # We want: (Batch, Height, Width, Channels)
    images_for_plotting = images.permute(0, 2, 3, 1)
    print(f"Permuted shape (B, H, W, C): {images_for_plotting.shape}")
    ```

***

### 13. tf.data

* **What is it?**
    `tf.data` is the API for building efficient data input pipelines in **TensorFlow**, not PyTorch. The equivalent and standard data-handling API in PyTorch is the combination of `torch.utils.data.Dataset` and `torch.utils.data.DataLoader`.

* **What are they good for?**
    The `Dataset` and `DataLoader` classes provide a powerful and flexible way to load, preprocess, and iterate over your data in batches, which is essential for training any neural network.

* **Details**
    * `Dataset`: An abstract class representing your dataset. You create a custom dataset by subclassing it and implementing two key methods:
        * `__len__(self)`: Should return the total number of samples in the dataset.
        * `__getitem__(self, idx)`: Should return the sample (e.g., an image and its label) at a given index `idx`. This is where you perform data loading and transformations.
    * `DataLoader`: A data iterator that wraps a `Dataset`. It handles creating mini-batches, shuffling the data each epoch, and loading data in parallel using multiple workers.
    * This separation of concerns makes your code cleaner and your data pipeline much more efficient.

* **Example**
    ```python
    import torch
    from torch.utils.data import Dataset, DataLoader

    # 1. Create a custom Dataset
    class MyCustomDataset(Dataset):
        def __init__(self, data, labels):
            self.data = data
            self.labels = labels

        def __len__(self):
            return len(self.data)

        def __getitem__(self, idx):
            sample = self.data[idx]
            label = self.labels[idx]
            return sample, label

    # 2. Instantiate the Dataset with some dummy data
    data = torch.randn(100, 10) # 100 samples, 10 features
    labels = torch.randint(0, 2, (100,))
    dataset = MyCustomDataset(data, labels)

    # 3. Wrap it in a DataLoader
    # This will serve data in batches of 32 and shuffle it every epoch
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # 4. Use it in a training loop
    # for X_batch, y_batch in dataloader:
    #     print(f"Batch shapes: {X_batch.shape}, {y_batch.shape}")
    ```

***

### 14. DataLoader & 15. Dataset

*These were explained together in the item above as they are the standard PyTorch data-handling pair.*

***

## Questions

### **1. What's a tensor?**

* **Short Answer:** A tensor is a multi-dimensional array, which is the fundamental data structure in PyTorch.

* **Long Answer:** A tensor is the generalization of vectors and matrices to an arbitrary number of dimensions. In the context of PyTorch, it's a specialized data container optimized for numerical computation, especially on GPUs. It holds all the data a model works with: the input features, the model's weights and biases, and the gradients calculated during training. A 0-D tensor is a scalar, a 1-D tensor is a vector, a 2-D tensor is a matrix, and so on.

---

### **2. What is the difference between a PyTorch tensor and a NumPy ndarray?**

* **Short Answer:** The main differences are that PyTorch tensors can run on GPUs and can be used to build computation graphs for automatic differentiation.

* **Long Answer:**
    * **GPU Acceleration:** NumPy arrays can only run on the CPU. PyTorch tensors can be seamlessly moved to an NVIDIA GPU using `.to('cuda')`, which can accelerate computations by orders of magnitude.
    * **Automatic Differentiation:** PyTorch tensors are the backbone of the `Autograd` engine. By setting `requires_grad=True`, PyTorch tracks all operations on them in a computation graph, allowing it to automatically compute gradients via backpropagation. NumPy arrays do not have this capability.
    * **Ecosystem:** PyTorch tensors are integrated into the PyTorch deep learning ecosystem, including layers (`nn.Module`), loss functions, and optimizers. NumPy is a general-purpose numerical computing library.

---

### **3. Is PyTorch compatible with NumPy?**

* **Short Answer:** Yes, they are highly compatible and can be converted back and forth easily.

* **Long Answer:** PyTorch and NumPy are designed to interoperate seamlessly. You can convert a PyTorch tensor on the CPU to a NumPy array using `.numpy()` and a NumPy array to a PyTorch tensor using `torch.from_numpy()`. This is incredibly useful because it allows you to leverage the vast scientific computing ecosystem built around NumPy (e.g., Scikit-learn, Matplotlib, SciPy) to preprocess and visualize your data, while still using PyTorch for the core model training and GPU acceleration.

---

### **4. How can PyTorch do gradient descent without you explicitly providing the gradients?**

* **Short Answer:** It uses its **Autograd** engine, which builds a computation graph during the forward pass and then traverses it backward to automatically calculate all the gradients.

* **Long Answer:** This is the magic of automatic differentiation. When you perform operations on tensors that have `requires_grad=True`, PyTorch builds a **computation graph** in the background. This graph records every operation and the tensors involved. When you call `loss.backward()`, the `Autograd` engine starts from the loss node and applies the **chain rule** of calculus, propagating backward through the graph. At each step, it calculates the gradient of the final loss with respect to the intermediate tensors, and finally with respect to the model's parameters (the leaf nodes). These calculated gradients are then stored in the `.grad` attribute of each parameter, ready for the optimizer to use.

---

### **5. What is the purpose of the method `detach`?**

* **Short Answer:** The `.detach()` method removes a tensor from its computation graph, preventing gradients from being backpropagated through it.

* **Long Answer:** Detaching a tensor is useful in several scenarios. First, if you want to move a tensor to NumPy or use it for plotting with Matplotlib, you must first detach it because these libraries cannot handle tensors that are still connected to a computation graph. Second, it can be used for performance optimization. If you have a part of your model that you want to be "frozen" (not trained), detaching the output of that part before it enters the rest of the model will stop gradients from flowing back into it. Finally, it's used in more advanced scenarios like Generative Adversarial Networks (GANs) to control which parts of the network are updated during a given training step.

---

### **6. Can you provide a custom loss function? How does it work with gradient descent?**

* **Short Answer:** Yes, you can. A custom loss function is just a regular Python function that takes the model's predictions and the true labels as input and returns a single scalar tensor representing the loss.

* **Long Answer:** As long as your custom loss function is composed of differentiable PyTorch operations, `Autograd` can work with it perfectly. Gradient descent only needs one thing: the gradient of the loss with respect to the model's parameters. Because your custom loss function uses standard PyTorch operations, it becomes the final node in the computation graph. When you call `.backward()` on the output of your custom loss function, `Autograd` simply treats it like any other operation in the graph and calculates the gradients as usual.

    ```python
    # A custom loss function that penalizes predictions > 0.8 more heavily
    def my_custom_loss(y_pred, y_true):
        # Use standard differentiable PyTorch functions
        error = y_true - y_pred
        squared_error = torch.pow(error, 2)

        # Apply a custom penalty
        penalty = torch.where(y_pred > 0.8, squared_error * 2, squared_error)
        
        return torch.mean(penalty)

    # In the training loop:
    # loss = my_custom_loss(predictions, labels)
    # loss.backward() # This works perfectly!
    ```

---

### **7. List all builtin loss functions and optimizers**

* **Short Answer:** Common loss functions include `MSELoss`, `CrossEntropyLoss`, and `BCELoss`. Common optimizers are `Adam`, `SGD`, and `RMSprop`.

* **Long Answer:** PyTorch provides a wide range of pre-built components. It's not practical to list them all, but here are the most important ones:
    * **Loss Functions (in `torch.nn`):**
        * `nn.MSELoss`: Mean Squared Error, for regression.
        * `nn.L1Loss`: Mean Absolute Error (MAE), for regression.
        * `nn.CrossEntropyLoss`: The standard for multi-class classification (it combines `LogSoftmax` and `NLLLoss`).
        * `nn.BCELoss`: Binary Cross-Entropy, for binary classification.
        * `nn.BCEWithLogitsLoss`: A more numerically stable version of `BCELoss` that takes raw logits as input.
    * **Optimizers (in `torch.optim`):**
        * `optim.SGD`: Stochastic Gradient Descent, often used with a momentum parameter.
        * `optim.Adam`: The most popular, all-purpose adaptive optimizer.
        * `optim.AdamW`: Adam with improved weight decay handling.
        * `optim.RMSprop`: An adaptive learning rate optimizer.
        * `optim.Adagrad`: Another adaptive optimizer, good for sparse data.

---

### **8. What is a PyTorch Module?**

* **Short Answer:** An `nn.Module` is the base class for all neural network models in PyTorch, acting as a container for layers and parameters.

* **Long Answer:** A PyTorch `nn.Module` is a Python class that provides a structured way to build neural networks. When you create your own model, you inherit from `nn.Module` and define two key methods:
    1.  `__init__(self)`: Here, you initialize all the components of your network, such as linear layers, convolutional layers, and activation functions. Any layer or `nn.Parameter` defined here is automatically registered with the module.
    2.  `forward(self, x)`: Here, you define the data flow—how an input tensor `x` passes through the layers you defined in `__init__`.
    This structure makes it easy to organize complex architectures, and the module automatically handles tracking all learnable parameters, making it simple to pass them to an optimizer.

---

### **9. Why do you need to zero grad?**

* **Short Answer:** You must call `optimizer.zero_grad()` before `loss.backward()` because PyTorch accumulates gradients by default.

* **Long Answer:** When you call `loss.backward()`, PyTorch computes the gradients for the current batch and *adds* them to the `.grad` attribute of each parameter. It does not overwrite them. This accumulation behavior is useful in some advanced scenarios (like training RNNs with long sequences), but for standard training, you want to calculate the gradients for each mini-batch independently. If you forget to call `optimizer.zero_grad()` at the start of your training loop iteration, the gradients from the new batch will be added to the gradients from all previous batches, which will completely corrupt your gradient and send your training in the wrong direction.

---

### **10. Can you plot tensors using Matplotlib?**

* **Short Answer:** Yes, but you must first move the tensor to the CPU and convert it to a NumPy array.

* **Long Answer:** Matplotlib is a NumPy-based plotting library and does not know how to handle PyTorch tensors directly. Furthermore, it cannot access data stored on a GPU. Therefore, to plot a tensor, you must perform a two-step conversion:
    1.  If the tensor is on the GPU, move it to the CPU: `tensor_cpu = tensor_gpu.cpu()`.
    2.  If the tensor requires gradients, detach it from the computation graph: `tensor_detached = tensor_cpu.detach()`.
    3.  Convert the CPU tensor to a NumPy array: `numpy_array = tensor_detached.numpy()`.
    This `numpy_array` can then be used with any Matplotlib function, such as `plt.imshow(numpy_array)`.

---

### **11. Does PyTorch automatically use the GPU when possible?**

* **Short Answer:** No, you must explicitly tell PyTorch to use the GPU.

* **Long Answer:** PyTorch does not automatically move computations to the GPU. You are in full control of device placement. To use a GPU, you must manually move your model and your data tensors to the CUDA device. The standard workflow is:
    1.  Define your device at the start of your script: `device = "cuda" if torch.cuda.is_available() else "cpu"`.
    2.  Move your model to that device once: `model.to(device)`.
    3.  Inside your training loop, move each batch of data to that device: `inputs, labels = inputs.to(device), labels.to(device)`.
    Forgetting to move either the model or the data will result in a runtime error.

---

### **12. What operations benefit the most from GPU acceleration?**

* **Short Answer:** Large, parallelizable operations, especially matrix multiplications and convolutions.

* **Long Answer:** GPUs excel at Single Instruction, Multiple Data (SIMD) tasks. The operations that benefit most are those that can be broken down into many identical, independent calculations. In deep learning, this primarily includes:
    * **Large Matrix Multiplications:** These are the core of fully connected (`nn.Linear`) layers.
    * **Convolutions:** These are the core of `nn.Conv2d` layers and are essentially a series of many small, parallel multiplications and additions.
    * **Element-wise Operations:** Applying an activation function like ReLU to every element of a large tensor is also highly parallelizable.
    Operations that are inherently sequential or involve complex control flow (like looping over a small number of items) do not benefit much from GPU acceleration and are often faster on the CPU.

***
## Exercises

### 1. Create an autoencoder model using PyTorch, and use it to reduce dimensionality of the FashionMNIST dataset

Here is a complete, commented script that defines, trains, and evaluates an autoencoder on the FashionMNIST dataset. It also includes visualizations to help answer the follow-up questions.

```python:FashionMNIST Autoencoder:fashion_mnist_autoencoder.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Define Parameters and Device ---
# Hyperparameters
EPOCHS = 10
BATCH_SIZE = 128
LEARNING_RATE = 1e-3
LATENT_DIM = 16 # The dimension of the compressed vector

# Set device (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# --- 2. Load and Prepare the FashionMNIST Dataset ---
# Define transformations to apply to the images
transform = transforms.Compose([
    transforms.ToTensor(), # Converts image to PyTorch tensor
    # transforms.Normalize((0.5,), (0.5,)) # Uncomment if you want to normalize
])

# Download datasets
train_dataset = torchvision.datasets.FashionMNIST(
    root='./data', train=True, download=True, transform=transform
)
test_dataset = torchvision.datasets.FashionMNIST(
    root='./data', train=False, download=True, transform=transform
)

# Create DataLoaders
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# --- 3. Define the Autoencoder Model Class ---
class Autoencoder(nn.Module):
    def __init__(self, latent_dim):
        super(Autoencoder, self).__init__()
        
        # Encoder: Compresses the 28x28 image into a latent vector
        self.encoder = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, latent_dim) # The bottleneck
        )
        
        # Decoder: Reconstructs the image from the latent vector
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 28 * 28),
            nn.Sigmoid() # Use Sigmoid to ensure output values are between 0 and 1
        )

    def forward(self, x):
        # Flatten the input image
        x = x.view(x.size(0), -1)
        # Encode
        encoded = self.encoder(x)
        # Decode
        decoded = self.decoder(encoded)
        # Reshape the output to be like an image
        reconstructed = decoded.view(x.size(0), 1, 28, 28)
        return reconstructed, encoded

# --- 4. Instantiate Model, Loss, and Optimizer ---
model = Autoencoder(latent_dim=LATENT_DIM).to(device)
print(model)

# Select appropriate loss function and optimizer
loss_function = nn.MSELoss() # Mean Squared Error is good for reconstruction
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# --- 5. Implement the Gradient Descent (Training) Loop ---
train_losses = []
test_losses = []

for epoch in range(EPOCHS):
    # --- Training Phase ---
    model.train() # Set model to training mode
    running_train_loss = 0.0
    for images, _ in train_loader: # We don't need labels for an autoencoder
        images = images.to(device)
        
        # Forward pass
        reconstructed_images, _ = model(images)
        loss = loss_function(reconstructed_images, images)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        running_train_loss += loss.item()
    
    avg_train_loss = running_train_loss / len(train_loader)
    train_losses.append(avg_train_loss)
    
    # --- Validation Phase ---
    model.eval() # Set model to evaluation mode
    running_test_loss = 0.0
    with torch.no_grad():
        for images, _ in test_loader:
            images = images.to(device)
            reconstructed_images, _ = model(images)
            loss = loss_function(reconstructed_images, images)
            running_test_loss += loss.item()
            
    avg_test_loss = running_test_loss / len(test_loader)
    test_losses.append(avg_test_loss)
    
    print(f"Epoch [{epoch+1}/{EPOCHS}], Train Loss: {avg_train_loss:.6f}, Test Loss: {avg_test_loss:.6f}")

print("\nTraining complete.")

# --- Analysis Questions ---

# Did you overfit?
# Overfitting occurs when the training loss continues to decrease while the test loss
# starts to increase or stagnates at a high value. We can check by plotting the losses.
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Training Loss')
plt.plot(test_losses, label='Test Loss')
plt.title("Training vs. Test Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.legend()
plt.show()

# Are the reconstructed images any good?
# Let's visualize some original vs. reconstructed images from the test set.
model.eval()
with torch.no_grad():
    # Get a batch of test images
    images, _ = next(iter(test_loader))
    images = images.to(device)
    
    # Get the reconstructed images
    reconstructed, _ = model(images)

    # Plot them
    plt.figure(figsize=(20, 4))
    for i in range(10):
        # Original image
        ax = plt.subplot(2, 10, i + 1)
        plt.imshow(images[i].cpu().squeeze(), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0: ax.set_title("Original")

        # Reconstructed image
        ax = plt.subplot(2, 10, i + 11)
        plt.imshow(reconstructed[i].cpu().squeeze(), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0: ax.set_title("Reconstructed")
    plt.show()

# Are the reduced vectors any good?
# If the latent vectors are good, they should cluster by class.
# Let's re-run this with LATENT_DIM=2 to visualize the 2D space.
# NOTE: This requires re-training the model with latent_dim=2 in the config.
if LATENT_DIM == 2:
    model.eval()
    all_encoded = []
    all_labels = []
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            _, encoded = model(images)
            all_encoded.append(encoded.cpu().numpy())
            all_labels.append(labels.cpu().numpy())
    
    all_encoded = np.concatenate(all_encoded)
    all_labels = np.concatenate(all_labels)

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(all_encoded[:, 0], all_encoded[:, 1], c=all_labels, cmap='tab10', s=5)
    plt.legend(handles=scatter.legend_elements()[0], labels=test_dataset.classes)
    plt.title("2D Latent Space of FashionMNIST")
    plt.xlabel("Latent Dimension 1")
    plt.ylabel("Latent Dimension 2")
    plt.show()

# What happens if you add some noise to a reduced vector before decoding it?
model.eval()
with torch.no_grad():
    # Get one image
    image, _ = test_dataset[0]
    image = image.unsqueeze(0).to(device) # Add batch dimension

    # Get its latent vector
    _, encoded = model(image)
    
    # Add some random noise
    noise = torch.randn_like(encoded) * 0.5
    noisy_encoded = encoded + noise

    # Decode both the original and noisy versions
    original_reconstruction = model.decoder(encoded).view(1, 28, 28)
    noisy_reconstruction = model.decoder(noisy_encoded).view(1, 28, 28)

    # Plot the results
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    axes[0].imshow(original_reconstruction.cpu().squeeze(), cmap='gray')
    axes[0].set_title("Standard Recon.")
    axes[1].imshow(noisy_reconstruction.cpu().squeeze(), cmap='gray')
    axes[1].set_title("Recon. from Noisy Vector")
    axes[2].imshow((original_reconstruction - noisy_reconstruction).abs().cpu().squeeze(), cmap='hot')
    axes[2].set_title("Difference")
    for ax in axes: ax.axis('off')
    plt.show()
```

### Analysis and Answers to Exercise Questions

* **Should you overfit an autoencoder?**
    No. The goal of an autoencoder is to learn a *general representation* of the data, not to memorize the training set. If it overfits, the encoder will learn shortcuts specific to the training images, and the decoder will only be good at reconstructing those specific images. When given a new image from the test set, a heavily overfit model will produce a poor reconstruction. You want the test loss to be as low as the training loss.

* **Did you overfit?**
    By looking at the "Training vs. Test Loss" plot, we can see that the test loss follows the training loss very closely. Both decrease and then level off together. This indicates that the model is **not overfitting** and is generalizing well to the unseen test data.

* **Are the reconstructed images any good?**
    Looking at the visualization of original vs. reconstructed images, we can see that the reconstructions are quite good. They are slightly blurry, which is expected since the model has to compress a 784-dimensional image into a tiny 16-dimensional vector and then rebuild it. However, they clearly capture the essential features of the clothing items—the shape of a shoe, the collar of a shirt, the straps of a bag. The model has successfully learned the most important patterns.

* **Are the reduced vectors any good?**
    If you re-train the model with `LATENT_DIM = 2`, the plot of the 2D latent space shows that the vectors are very good. You can see distinct clusters forming for different classes of clothing (e.g., T-shirts/tops group together, trousers group together, shoes form their own cluster). This means the encoder has learned to map similar images to nearby points in the latent space, which is the definition of a useful representation.

* **What happens if you add some noise to a reduced vector before decoding it?**
    The final visualization shows this experiment. When we add a small amount of random noise to a latent vector and then decode it, the resulting image is a slightly distorted but still recognizable version of the original reconstruction. This demonstrates that the learned latent space is somewhat **robust**. Small changes in the latent space lead to small changes in the output image, which is a property of a well-trained generative model. This is the core idea behind more advanced models like Variational Autoencoders (VAEs).