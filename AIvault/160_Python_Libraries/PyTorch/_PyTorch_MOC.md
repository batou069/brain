---
tags:
  - python
  - library
  - pytorch
  - torch
  - deep_learning
  - machine_learning
  - neural_networks
  - moc
  - concept
aliases:
  - PyTorch MOC
  - Torch MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Deep_Learning_Overview]]"
  - "[[Neural_Networks]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-08-20
---
# PyTorch MOC 🔥🤖

**PyTorch** is a popular open-source machine learning library developed primarily by Facebook's AI Research lab (FAIR). It is known for its flexibility, ease of use, and strong support for GPU acceleration, making it a favorite for both researchers and practitioners in the field of deep learning.

## Core Philosophy & Features
-   **Tensors:** The fundamental data structure is the `torch.Tensor`, a multi-dimensional array similar to [[_NumPy_MOC|NumPy arrays]], but with the ability to run on GPUs for accelerated computing.
-   **Dynamic Computation Graphs (Define-by-Run):** PyTorch builds the computation graph on-the-fly as operations are executed. This makes debugging more intuitive and allows for dynamic model architectures that can change based on input data. This is a key feature that initially differentiated it from TensorFlow 1.x.
-   **Automatic Differentiation (`torch.autograd`):** Provides a powerful automatic differentiation engine for calculating gradients, which is essential for training neural networks via backpropagation.
-   **Python-First Approach:** Designed to be deeply integrated with Python, allowing for an imperative and Pythonic programming style.
-   **Extensive Ecosystem:** Supported by a rich ecosystem of libraries and tools, including `TorchVision` (for computer vision), `TorchText` (for NLP), `TorchAudio` (for audio), and `PyTorch Lightning` (a high-level wrapper for organizing code).
-   **Ease of Use & Flexibility:** Often praised for its simple API and the flexibility it offers in building and experimenting with complex model architectures.

## Key Components & Concepts
-   [[PyTorch_Tensors|Tensors (`torch.Tensor`)]]
    -   Creating and manipulating tensors.
    -   Tensor operations and interoperability with NumPy.
-   [[PyTorch_Autograd|Automatic Differentiation (`torch.autograd`)]]
    -   Understanding `requires_grad`, `grad_fn`, and `.backward()`.
-   [[PyTorch_Neural_Network_Module_nn|Neural Network Module (`torch.nn`)]]
    -   Building neural networks as classes inheriting from `nn.Module`.
    -   **Layers (`nn.Linear`, `nn.Conv2d`, `nn.LSTM`, etc.)**: The building blocks of networks.
    -   **Activation Functions (`nn.ReLU`, `nn.Sigmoid`, `F.relu`, etc.)**: Found in `torch.nn` and `torch.nn.functional`.
    -   **Loss Functions (`nn.BCELoss`, `nn.CrossEntropyLoss`, `nn.MSELoss`, etc.)**: For calculating model error.
-   [[PyTorch_Optimizers|Optimizers (`torch.optim`)]]
    -   Algorithms for updating model weights (e.g., `optim.Adam`, `optim.SGD`).
-   [[PyTorch_Training_Loop|The PyTorch Training Loop]]
    -   The standard explicit loop for training models: forward pass, loss calculation, backward pass, optimizer step.
-   [[PyTorch_Datasets_DataLoaders|Datasets and DataLoaders (`torch.utils.data`)]]
    -   Efficiently loading, preprocessing, and batching data for training.
-   [[PyTorch_Saving_Loading_Models|Saving and Loading Models]]
    -   Saving/loading model weights (`state_dict`) and entire models.
-   [[PyTorch_GPU_CUDA_Usage|Using GPUs with PyTorch (`.to(device)`)]]
    -   Moving tensors and models to a GPU for acceleration.
-   **Ecosystem Libraries:**
    -   [[PyTorch_TorchVision|TorchVision]] (for Computer Vision)
    -   [[PyTorch_TorchText|TorchText]] (for Natural Language Processing)
    -   [[PyTorch_Lightning|PyTorch Lightning]] (High-level interface for PyTorch)

## Notes in this PyTorch Section
```dataview
LIST
FROM "160_Python_Libraries/PyTorch"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---