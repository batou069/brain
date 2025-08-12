---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - distributed_training
  - scaling
  - multi_gpu
  - tpu
  - concept
  - example
aliases:
  - tf.distribute.Strategy
  - Distributed TensorFlow
  - Scaling TF Training
related:
  - "[[_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Keras_API_in_TensorFlow]]"
  - "[[TensorFlow_Data_Pipeline_tf_data|tf.data]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# TensorFlow: Distributed Training (`tf.distribute.Strategy`)

Training large deep learning models on massive datasets can be time-consuming on a single processor (CPU or GPU). TensorFlow provides the `tf.distribute.Strategy` API to distribute training across multiple GPUs, multiple machines, or TPUs with minimal changes to your existing Keras model training code.

## Why Distributed Training?
-   **Speed Up Training:** By parallelizing computation across multiple processing units, training time can be significantly reduced.
-   **Train Larger Models:** Models that are too large to fit into the memory of a single GPU can be trained using model parallelism (though data parallelism is more common).
-   **Process Larger Datasets:** Distribute large datasets that cannot be processed efficiently on a single machine.

## `tf.distribute.Strategy` API
This is the primary API for distributed training in TensorFlow 2.x. It's an abstraction that handles the complexities of distributing the model, data, and computation.

**Key Idea:** You define your Keras model as usual. Then, you create a `Strategy` object and open a `strategy.scope()`. Any model, optimizer, or metrics created within this scope will be distributed according to the chosen strategy.

```python
import tensorflow as tf
from tensorflow import keras

# strategy = ... # Choose a strategy (see below)

# with strategy.scope():
#   # Model definition, optimizer creation, and model.compile() go here
#   model = keras.Sequential([...])
#   optimizer = keras.optimizers.Adam()
#   model.compile(optimizer=optimizer, loss='...', metrics=['...'])

# Prepare your tf.data.Dataset
# train_dataset = ... # Your tf.data pipeline

# Train the model
# model.fit(train_dataset, epochs=...)
```

## Common Distribution Strategies

[list2tab|#TF Distribute Strategies]
- `MirroredStrategy`
    -   **Class:** `tf.distribute.MirroredStrategy`
    -   **Use Case:** For training on **multiple GPUs on a single machine**.
    -   **How it Works (Data Parallelism):**
        1.  All model variables are mirrored (copied) to each GPU.
        2.  Each GPU processes a different slice of the input data batch.
        3.  Gradients are computed on each GPU.
        4.  Gradients are aggregated across all GPUs (typically by summing and then averaging).
        5.  The aggregated gradients are used to update the mirrored variables on each GPU (all-reduce synchronization).
    -   **Example:**
        ```python
        import tensorflow as tf
        from tensorflow import keras
        from tensorflow.keras import layers
        import numpy as np
        
        # Check for available GPUs
        # gpus = tf.config.list_physical_devices('GPU')
        # if gpus:
        #     print(f"Found {len(gpus)} GPUs.")
        #     # Create a MirroredStrategy
        #     strategy = tf.distribute.MirroredStrategy() # Uses all available GPUs by default
        #     # strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"]) # Or specify devices
        #     print(f"Number of devices in strategy: {strategy.num_replicas_in_sync}")

        #     with strategy.scope():
        #         # Define and compile your Keras model inside the strategy scope
        #         mirrored_model = keras.Sequential([
        #             layers.Dense(128, activation='relu', input_shape=(784,)),
        #             layers.Dense(10, activation='softmax')
        #         ])
        #         mirrored_model.compile(optimizer=keras.optimizers.Adam(),
        #                                loss='sparse_categorical_crossentropy',
        #                                metrics=['accuracy'])
            
        #     # Prepare a tf.data.Dataset (conceptual)
        #     # (X_train_np, y_train_np) = ... load your data ...
        #     # BATCH_SIZE_PER_REPLICA = 64
        #     # GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * strategy.num_replicas_in_sync
        #     # train_dataset = tf.data.Dataset.from_tensor_slices((X_train_np, y_train_np)).shuffle(10000).batch(GLOBAL_BATCH_SIZE)
            
        #     # print("Training with MirroredStrategy (conceptual)...")
        #     # mirrored_model.fit(train_dataset, epochs=2)
        # else:
        #     print("No GPUs found, MirroredStrategy example skipped.")
        #     # Fallback for non-GPU environment (single device training)
        #     # model = keras.Sequential(...)
        #     # model.compile(...)
        #     # model.fit(...)
        ```
- `MultiWorkerMirroredStrategy`
    -   **Class:** `tf.distribute.MultiWorkerMirroredStrategy`
    -   **Use Case:** For **synchronous distributed training across multiple machines (workers)**, each potentially having multiple GPUs.
    -   **How it Works (Data Parallelism):** Similar to `MirroredStrategy`, but variables are mirrored, and gradient aggregation (all-reduce) happens across all GPUs on all workers.
    -   **Setup:** Requires setting up a `TF_CONFIG` environment variable on each worker to define the cluster structure (worker addresses, task types, task indices).
- `TPUStrategy`
    -   **Class:** `tf.distribute.experimental.TPUStrategy` (path might change slightly with TF versions)
    -   **Use Case:** For training on Google's Tensor Processing Units (TPUs).
    -   **How it Works:** Connects to a TPU cluster and distributes computation across TPU cores.
- `ParameterServerStrategy`
    -   **Class:** `tf.distribute.experimental.ParameterServerStrategy`
    -   **Use Case:** For asynchronous data parallelism. Model parameters are sharded across parameter servers, and workers pull parameters and push gradients asynchronously. Can be useful for very large models or when network bandwidth between workers is a bottleneck for synchronous strategies.
    -   **Note:** More complex to set up and tune than synchronous strategies.
- `CentralStorageStrategy`
    -   **Class:** `tf.distribute.CentralStorageStrategy`
    -   **Use Case:** Synchronous training where variables are not mirrored. Instead, they are placed on the CPU, and operations are replicated across all local GPUs. Gradients are aggregated and applied to the central variables.
    -   Less common than `MirroredStrategy` for multi-GPU on one machine.

## Key Considerations for Distributed Training
1.  **Data Pipeline (`tf.data`):**
    -   An efficient input pipeline using [[TensorFlow_Data_Pipeline_tf_data|`tf.data`]] is crucial to prevent data loading from becoming a bottleneck.
    -   Use `dataset.distribute_datasets_from_function` or ensure your dataset is correctly sharded or processed by each worker/replica.
    -   For `MirroredStrategy` and `MultiWorkerMirroredStrategy`, the global batch size should be divisible by the number of replicas (`num_replicas_in_sync`). Each replica will process `global_batch_size / num_replicas_in_sync` samples.
2.  **Batch Size:**
    -   The **global batch size** (total batch size across all replicas) is what you pass to `dataset.batch()`.
    -   Each replica processes a portion of this global batch.
    -   You might need to adjust the learning rate based on the global batch size (e.g., linear scaling rule, though this is not always optimal).
3.  **Saving and Loading Models:**
    -   Models trained under a `strategy.scope()` should ideally be saved and loaded also within a `strategy.scope()` if you intend to continue distributed training or inference with the same strategy.
    -   `model.save()` works correctly with `tf.distribute.Strategy`. The saved model (SavedModel format) is a single, non-distributed graph that can be loaded with or without a strategy.
4.  **Custom Training Loops:**
    -   If using a custom training loop (with `tf.GradientTape`), you need to adapt it for distributed training. This typically involves:
        -   Using `strategy.run(step_fn, args=(data_batch,))` to execute a training step per replica.
        -   Aggregating losses and gradients from replicas using `strategy.reduce()`.
        -   Applying gradients using `optimizer.apply_gradients()` within the strategy scope.
5.  **Environment Setup (for Multi-Worker):**
    -   `MultiWorkerMirroredStrategy` and `ParameterServerStrategy` require proper configuration of the `TF_CONFIG` environment variable on each worker node to define the cluster topology.

The `tf.distribute.Strategy` API provides a high-level and relatively easy way to scale out TensorFlow Keras model training, abstracting many of the complexities of distributed computing.

---