---
tags:
  - python
  - library
  - tensorflow
  - tf
  - deep_learning
  - machine_learning
  - neural_networks
  - moc
  - concept
aliases:
  - TensorFlow MOC
  - TF MOC
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[_NumPy_MOC]]"
  - "[[Keras_Library]]"
  - "[[Deep_Learning_Overview]]"
  - "[[Neural_Networks]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-09
---
# TensorFlow MOC 🔥🧠

**TensorFlow** is an open-source end-to-end platform for machine learning, with a particular strength in **deep learning** and **neural networks**. It was developed by the Google Brain team and offers a comprehensive, flexible ecosystem of tools, libraries, and community resources.

TensorFlow allows developers to build and deploy ML-powered applications across a variety of platforms (CPUs, GPUs, TPUs, mobile, web).

## Core Philosophy & Features
-   **Computational Graphs:** TensorFlow traditionally used a static computation graph model (Define-and-Run), though Eager Execution (Define-by-Run, similar to PyTorch) is now the default in TensorFlow 2.x, making it more Pythonic and easier to debug.
-   **Tensors:** The fundamental data structure in TensorFlow is the "tensor," a multi-dimensional array similar to [[_NumPy_MOC|NumPy arrays]].
-   **Scalability:** Designed for large-scale distributed training and inference.
-   **Flexibility:** Supports building a wide range of models, from simple linear regression to complex deep neural networks for computer vision, NLP, reinforcement learning, etc.
-   **[[Keras_Library|Keras API]]:** TensorFlow has adopted Keras as its official high-level API for building and training neural networks, making model development more user-friendly.
-   **Ecosystem (TensorFlow Extended - TFX):** Provides tools for the full MLOps lifecycle, including data ingestion (`tf.data`), model building (`tf.keras`), training, evaluation, deployment (`TensorFlow Serving`, `TensorFlow Lite` for mobile/IoT, `TensorFlow.js` for web).
-   **Automatic Differentiation:** Crucial for training neural networks via backpropagation (`tf.GradientTape`).
-   **Hardware Acceleration:** Strong support for GPUs and Google's TPUs (Tensor Processing Units) for accelerating training and inference.

## Key Components & Concepts
[list2card|addClass(ab-col3)|#TensorFlow Concepts]
- **[[TensorFlow_Tensors|Tensors (`tf.Tensor`)]]**
  - Multi-dimensional arrays, the primary data structure.
- **[[TensorFlow_Variables|Variables (`tf.Variable`)]]**
  - Special tensors used to store mutable model parameters (weights, biases) that are updated during training.
- **[[TensorFlow_Operations|Operations (`tf.function`, tf math ops)]]**
  - Mathematical operations that consume and produce tensors. `tf.function` decorator can compile Python functions into high-performance TensorFlow graphs.
- **[[TensorFlow_Graphs_Eager_Execution|Graphs and Eager Execution]]**
  - Understanding computation graphs (even if abstracted by Eager Execution) and how TensorFlow executes operations.
- **[[TensorFlow_Automatic_Differentiation|Automatic Differentiation (`tf.GradientTape`)]]**
  - Mechanism for computing gradients, essential for backpropagation and model training.
- **[[Keras_API_in_TensorFlow|Keras API (`tf.keras`)]]**
  - The primary way to build, train, and evaluate neural network models in TensorFlow.
    -   [[Keras_Sequential_Functional_API|Sequential and Functional APIs]] for model definition.
    -   [[Keras_Layers|Layers]] (`tf.keras.layers`): Dense, Conv2D, LSTM, etc.
    -   [[Keras_Optimizers|Optimizers]] (`tf.keras.optimizers`): Adam, SGD, RMSprop.
    -   [[Keras_Loss_Functions|Loss Functions]] (`tf.keras.losses`): BinaryCrossentropy, CategoricalCrossentropy, MSE.
    -   [[Keras_Metrics|Metrics]] (`tf.keras.metrics`): Accuracy, Precision, Recall, AUC.
    -   [[Keras_Callbacks|Callbacks]] (`tf.keras.callbacks`): EarlyStopping, ModelCheckpoint.
- **[[TensorFlow_Data_Pipeline_tf_data|Data Pipelines (`tf.data`)]]**
  - Efficiently load and preprocess large datasets for training.
- **[[TensorFlow_Saving_Loading_Models|Saving and Loading Models]]**
  - Formats like SavedModel, HDF5.
- **[[TensorFlow_Distributed_Training|Distributed Training (`tf.distribute.Strategy`)]]**
  - Strategies for training models on multiple GPUs or multiple machines.
- **[[TensorFlow_Lite_TFLite|TensorFlow Lite (TFLite)]]**
  - For deploying models on mobile and embedded devices.
- **[[TensorFlow_js_TFJS|TensorFlow.js (TF.js)]]**
  - For running and training models in web browsers and Node.js.
- **[[TensorFlow_Serving|TensorFlow Serving]]**
  - For deploying models in production environments.
- **[[TensorBoard_TensorFlow|TensorBoard]]**
  - Visualization toolkit for inspecting model graphs, metrics, training progress, and more.

## Notes in this TensorFlow Section
```dataview
LIST
FROM "160_Python_Libraries/TensorFlow"
WHERE file.folder = this.file.folder AND file.name != this.file.name AND !contains(file.name, "MOC")
SORT file.name ASC
```

---