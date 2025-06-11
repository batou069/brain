Okay, let's continue with the remaining TensorFlow concepts, starting with `tf.data` for data pipelines.

---

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Data_Pipeline_tf_data.md
````markdown
---
tags: [python, tensorflow, tf, data_pipeline, tf_data, input_pipeline, performance, etl, concept, example]
aliases: [tf.data API, TensorFlow Datasets, Efficient Data Input TF]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Keras_API_in_TensorFlow]]" # tf.data is used to feed Keras models
  - "[[_NumPy_MOC|NumPy]]" # Can create datasets from NumPy arrays
  - "[[TensorFlow_Tensors|TF Tensors]]"
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow: Data Pipelines with `tf.data`

The `tf.data` API in TensorFlow is a powerful and efficient tool for building complex input pipelines for training machine learning models, especially deep learning models. It allows you to handle large datasets that may not fit in memory, apply various transformations, and feed data to your model in an optimized way.

## Why `tf.data`?
-   **Performance:** Designed for high performance. It can prefetch data, parallelize data loading and preprocessing, and overlap these operations with model training on CPU/GPU/TPU, preventing the training process from being bottlenecked by data input.
-   **Handling Large Datasets:** Can efficiently read data from disk or distributed file systems (like GCS, HDFS if configured) without loading everything into memory at once.
-   **Complex Transformations:** Provides a rich set of operations to preprocess and augment data (e.g., shuffling, batching, mapping functions, filtering, interleaving).
-   **Integration with `tf.keras`:** `tf.data.Dataset` objects can be directly passed to the `fit()`, `evaluate()`, and `predict()` methods of Keras models.
-   **Flexibility:** Can read from various data sources like NumPy arrays, TFRecord files, text files, CSV files, and can be extended for custom data formats.

## Core Concepts of `tf.data`

1.  **`tf.data.Dataset` Object:**
    -   The central abstraction in the `tf.data` API. It represents a sequence of elements, where each element consists of one or more components (tensors).
    -   For example, in supervised learning, an element might be a tuple `(features, label)`.

2.  **Creating Datasets (Sources):**
    You can create `Dataset` objects from various sources:
    -   **From Tensors in Memory:**
        -   `tf.data.Dataset.from_tensors(tensors)`: Creates a dataset with a single element (or a tuple of elements if `tensors` is a tuple).
        -   `tf.data.Dataset.from_tensor_slices(tensors)`: Creates a dataset by slicing the given tensors along their first dimension. This is very common for creating datasets from NumPy arrays or TensorFlow tensors representing features and labels.
            ```python
            import tensorflow as tf
            import numpy as np
            # Example: features and labels for an e-commerce recommendation model
            # User IDs, Item IDs (features), and Clicked (label)
            # user_ids = np.array()
            # item_ids = np.array()
            # clicked_labels = np.array() # 0 or 1

            # Create a dataset from NumPy arrays
            # feature_dataset = tf.data.Dataset.from_tensor_slices((user_ids, item_ids))
            # label_dataset = tf.data.Dataset.from_tensor_slices(clicked_labels)
            # combined_dataset = tf.data.Dataset.zip((feature_dataset, label_dataset))
            # More commonly:
            # combined_dataset_direct = tf.data.Dataset.from_tensor_slices(((user_ids, item_ids), clicked_labels))
            # for features, label in combined_dataset_direct.take(2):
            #     user_id_tensor, item_id_tensor = features
            #     print(f"User ID: {user_id_tensor.numpy()}, Item ID: {item_id_tensor.numpy()}, Clicked: {label.numpy()}")
            ```
    -   **From Files:**
        -   `tf.data.TextLineDataset(filenames)`: Reads lines from text files.
        -   `tf.data.TFRecordDataset(filenames)`: Reads records from TFRecord files (a binary format efficient for TensorFlow).
        -   `tf.data.experimental.CsvDataset(...)` (or use `tf.data.experimental.make_csv_dataset` for easier CSV reading into features and labels).
    -   **From Generators:**
        -   `tf.data.Dataset.from_generator(generator_func, output_signature)`: Creates a dataset from a Python generator.

3.  **Dataset Transformations:**
    These methods transform one dataset into another, allowing you to build a processing pipeline. They are typically chained together.
    -   **`map(map_func, num_parallel_calls=tf.data.AUTOTUNE)`:** Applies a given function `map_func` to each element of the dataset. `num_parallel_calls` allows for parallel processing of elements. `tf.data.AUTOTUNE` lets TensorFlow dynamically adjust the level of parallelism.
        -   Used for parsing, decoding, data augmentation, feature engineering.
        ```python
        # def parse_product_image(image_path_tensor, label_tensor):
        #     image_content = tf.io.read_file(image_path_tensor)
        #     image = tf.image.decode_jpeg(image_content, channels=3)
        #     image = tf.image.resize(image, [128, 128])
        #     image = image / 255.0 # Normalize
        #     return image, label_tensor
        # image_paths = ["img1.jpg", "img2.jpg", ...]
        # labels = [...]
        # path_label_dataset = tf.data.Dataset.from_tensor_slices((image_paths, labels))
        # image_label_dataset = path_label_dataset.map(parse_product_image, num_parallel_calls=tf.data.AUTOTUNE)
        ```
    -   **`filter(predicate_func)`:** Filters the dataset, keeping only elements for which `predicate_func` returns `True`.
    -   **`shuffle(buffer_size, seed=None, reshuffle_each_iteration=True)`:** Randomly shuffles the elements of the dataset. `buffer_size` should be large enough for good shuffling (e.g., dataset size).
    -   **`batch(batch_size, drop_remainder=False)`:** Combines consecutive elements into batches. `drop_remainder=True` drops the last batch if it's smaller than `batch_size`.
    -   **`repeat(count=None)`:** Repeats the dataset `count` times. If `count` is `None` or `-1`, repeats indefinitely (common for training).
    -   **`prefetch(buffer_size=tf.data.AUTOTUNE)`:** Prepares data for future steps while the current step is executing. Overlaps data preprocessing with model training, significantly improving performance. This should typically be the **last** transformation in your input pipeline.
    -   **`cache(filename=None)`:** Caches elements of the dataset either in memory (if `filename` is None) or to a file. Useful if the initial data loading or preprocessing is expensive and the dataset fits in memory/disk cache.
    -   `interleave(map_func, cycle_length, block_length, num_parallel_calls)`: Maps `map_func` to input elements and interleaves the results from the resulting datasets. Useful for reading from multiple files in parallel.
    -   `flat_map(map_func)`: Maps `map_func` to each element and then flattens the result.

## Typical `tf.data` Pipeline for Training
A common pattern for a training input pipeline:
```python
# BATCH_SIZE = 32
# AUTOTUNE = tf.data.AUTOTUNE # For num_parallel_calls and prefetch buffer_size

# Assuming 'file_paths' is a list of paths to TFRecord files or image files,
# and 'labels' is a corresponding list/array of labels.

# 1. Create a dataset of file paths and labels
# dataset = tf.data.Dataset.from_tensor_slices((file_paths, labels))

# 2. Shuffle the file paths (important for training to see data in different orders)
# dataset = dataset.shuffle(buffer_size=len(file_paths), reshuffle_each_iteration=True)

# 3. Load and preprocess data (e.g., read images, decode, augment)
# def load_and_preprocess_image_and_label(path, label):
#     # ... (image loading, decoding, resizing, normalization as in map() example) ...
#     # ... (potential data augmentation for images) ...
#     return image, label
# dataset = dataset.map(load_and_preprocess_image_and_label, num_parallel_calls=AUTOTUNE)

# 4. Batch the data
# dataset = dataset.batch(BATCH_SIZE)

# 5. Prefetch data for performance
# dataset = dataset.prefetch(buffer_size=AUTOTUNE)

# 6. Repeat (optional, Keras model.fit handles epochs)
# dataset = dataset.repeat() # If not using Keras fit's epoch handling

# Now 'dataset' is ready to be passed to model.fit()
# model.fit(dataset, epochs=10, steps_per_epoch=len(file_paths) // BATCH_SIZE)
```

## Benefits of Using `tf.data` in `tf.keras`
-   When you pass a `tf.data.Dataset` object to `model.fit()`, Keras handles iterating over the dataset, managing epochs, and feeding batches to the model.
-   Leverages the performance optimizations of `tf.data` (prefetching, parallel mapping).
-   Simplifies handling of large datasets that don't fit in memory.

## Example: E-commerce Product Recommendation Features
Imagine preparing features for a model that recommends products. Features might include user ID, previously viewed product IDs, and target could be a purchased product ID.

```python
import tensorflow as tf
import numpy as np

# Conceptual data
num_samples = 1000
user_ids = np.random.randint(1, 100, num_samples)
# Each user has a sequence of 5 previously viewed items (padding might be needed for variable length)
viewed_item_sequences = np.random.randint(1, 500, (num_samples, 5))
target_purchased_item = np.random.randint(1, 500, num_samples)

# Create tf.data.Dataset
# Using a dictionary for features makes it easy to feed into Keras models with named inputs
# features_dataset = tf.data.Dataset.from_tensor_slices({
#     "user_id_input": user_ids,
#     "viewed_items_input": viewed_item_sequences
# })
# labels_dataset = tf.data.Dataset.from_tensor_slices(target_purchased_item)
# full_dataset = tf.data.Dataset.zip((features_dataset, labels_dataset))

# Define a preprocessing function (if needed, e.g., one-hot encoding IDs if they are categorical)
# def preprocess_features(features, label):
#     # Example: could convert user_id to one-hot or use an embedding layer later
#     # For now, just pass through
#     return features, label

# Build the pipeline
# BATCH_SIZE = 64
# AUTOTUNE = tf.data.AUTOTUNE

# training_pipeline = full_dataset.shuffle(buffer_size=num_samples) \
#                                .map(preprocess_features, num_parallel_calls=AUTOTUNE) \
#                                .batch(BATCH_SIZE) \
#                                .prefetch(buffer_size=AUTOTUNE)

# Iterate through a few batches (conceptual)
# print("Batches from the tf.data pipeline:")
# for batch_features, batch_labels in training_pipeline.take(2): # Take 2 batches
#     print("User IDs in batch:", batch_features["user_id_input"].numpy()[:3])
#     print("Viewed Items in batch (first sample):", batch_features["viewed_items_input"].numpy())
#     print("Labels in batch:", batch_labels.numpy()[:3])
#     print("-" * 20)

# This 'training_pipeline' could then be passed to model.fit()
```

The `tf.data` API is a powerful and essential tool for building efficient and scalable input pipelines for TensorFlow and Keras models, especially when dealing with large datasets or complex preprocessing requirements.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Saving_Loading_Models.md
````markdown
---
tags: [python, tensorflow, tf, keras, model_persistence, saving_models, loading_models, savedmodel, hdf5, concept, example]
aliases: [Saving Keras Models, Loading Keras Models, TensorFlow Model Persistence, tf.saved_model]
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Callbacks|ModelCheckpoint Callback]]" # For saving during training
  - "[[TensorFlow_Lite_TFLite]]" # For deploying to mobile/edge
  - "[[TensorFlow_Serving]]" # For deploying to production servers
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow: Saving and Loading Models (`tf.keras`)

Persisting trained machine learning models is crucial for several reasons:
-   **Resuming Training:** To continue training later without starting from scratch.
-   **Inference/Prediction:** To use the trained model to make predictions on new data.
-   **Deployment:** To deploy the model to production environments (servers, mobile devices, web).
-   **Sharing Models:** To share trained models with others.

`tf.keras` provides convenient ways to save and load entire models, just the weights, or just the architecture.

## Saving an Entire Model
This saves the model's architecture, weights (learned parameters), and training configuration (optimizer, loss, metrics compiled with). This is the most comprehensive way to save a model.

**Formats:**
1.  **TensorFlow SavedModel format (Recommended):**
    -   This is the default and recommended format in TensorFlow 2.x.
    -   Saves the model as a directory containing assets, variables, and a `saved_model.pb` file (which includes the graph definition).
    -   Language-agnostic and suitable for deployment with [[TensorFlow_Serving]], [[TensorFlow_Lite_TFLite|TFLite]], [[TensorFlow_js_TFJS|TensorFlow.js]], or other TensorFlow runtimes.
    -   **Method:** `model.save("path/to/my_model_directory")` (no extension needed for directory) or `model.save("my_model.keras")` (newer Keras v3 format, also SavedModel based).

2.  **Keras HDF5 format (`.h5` or `.hdf5`):**
    -   A legacy format, widely used with older Keras versions.
    -   Saves the model architecture, weights, and training config into a single HDF5 file.
    -   **Method:** `model.save("my_model.h5")` or `model.save("my_model.keras")` (Keras v3 can also use `.keras` for HDF5 if configured, but it's moving towards SavedModel as the primary content for `.keras`).
    -   **Note:** While still supported, SavedModel is generally preferred for TensorFlow 2.x due to better integration with the TF ecosystem. The new `.keras` format (Keras v3) is designed to be a more robust replacement for `.h5`, often based on SavedModel principles.

**Example (Saving in SavedModel format):**
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Create a simple Keras model (e.g., for e-commerce product category prediction)
# model = keras.Sequential([
#     layers.Dense(64, activation='relu', input_shape=(784,)), # Example input shape
#     layers.Dense(10, activation='softmax') # 10 product categories
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Conceptual: Train the model for a few epochs
# X_train_dummy = np.random.rand(100, 784)
# y_train_dummy = np.random.randint(0, 10, 100)
# model.fit(X_train_dummy, y_train_dummy, epochs=1, verbose=0)

# Save the entire model to a directory (SavedModel format)
# model_save_path = "./my_saved_model_directory"
# model.save(model_save_path)
# print(f"Model saved to directory: {model_save_path}")

# Save using the .keras extension (Keras v3 format, often SavedModel based)
# model_keras_format_path = "./my_model_v3.keras"
# model.save(model_keras_format_path)
# print(f"Model saved in .keras format: {model_keras_format_path}")

# Save in legacy HDF5 format (if needed)
# model_h5_path = "./my_model_legacy.h5"
# model.save(model_h5_path)
# print(f"Model saved in HDF5 format: {model_h5_path}")
```

## Loading an Entire Model
You can load a saved model (architecture, weights, optimizer state) using `tf.keras.models.load_model()`.

```python
# from tensorflow import keras

# Load from SavedModel directory
# loaded_model_from_dir = keras.models.load_model("./my_saved_model_directory")
# loaded_model_from_dir.summary()

# Load from .keras format
# loaded_model_keras_format = keras.models.load_model("./my_model_v3.keras")
# loaded_model_keras_format.summary()

# Load from HDF5 format
# loaded_model_h5 = keras.models.load_model("./my_model_legacy.h5")
# loaded_model_h5.summary()

# After loading, the model can be used for evaluation or prediction
# conceptual_test_data = np.random.rand(10, 784)
# predictions = loaded_model_from_dir.predict(conceptual_test_data)
# print("\nPredictions from loaded model (first 2):\n", predictions[:2])
```
-   If you used custom objects (custom layers, loss functions, metrics) when creating the model, you might need to pass them to `load_model` via the `custom_objects` argument.

## Saving and Loading Only Model Weights
Sometimes, you only need to save the model's learned parameters (weights and biases) and not the entire architecture or optimizer state. This is useful if you want to use the same architecture but with different weights, or if you want a smaller file.

-   **Saving Weights:** `model.save_weights("path/to/my_weights_checkpoint")`
    -   This saves weights in TensorFlow's checkpoint format by default. You can also specify `save_format='h5'` for HDF5.
-   **Loading Weights:**
    1.  First, you need to have the **same model architecture** already built.
    2.  Then, call `model.load_weights("path/to/my_weights_checkpoint")`.

**Example:**
```python
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import numpy as np

# Define the model architecture (must be the same as when weights were saved)
# model_for_weights = keras.Sequential([
#     layers.Dense(64, activation='relu', input_shape=(784,)),
#     layers.Dense(10, activation='softmax')
# ])
# model_for_weights.compile(optimizer='adam', loss='sparse_categorical_crossentropy') # Compile to build it

# Assume 'my_model_weights_checkpoint' was saved earlier from a model with this architecture
# model_weights_path = "./my_model_weights_checkpoint" # No extension for TF checkpoint format
# model.save_weights(model_weights_path) # Conceptual save from a trained 'model'
# print(f"\nModel weights saved to: {model_weights_path}")

# Now load the weights into the newly defined model_for_weights
# try:
#     model_for_weights.load_weights(model_weights_path)
#     print("Model weights loaded successfully.")
#     # model_for_weights can now be used for inference
# except tf.errors.NotFoundError:
#     print(f"Weight file not found at {model_weights_path}. Run saving part first.")
```

## Saving/Loading Only Model Architecture
If you only want to save the model's configuration (architecture) without its weights or training config:
-   **Get Config:** `config = model.get_config()` (returns a Python dict).
-   **Recreate Model from Config:** `reinitialized_model = keras.Model.from_config(config)` (for Functional/Subclassed models) or `reinitialized_model = keras.Sequential.from_config(config)` (for Sequential models).
-   **JSON/YAML:** You can also get the architecture as a JSON string (`model.to_json()`) or YAML string (`model.to_yaml()`) and recreate from it (`keras.models.model_from_json()`, `keras.models.model_from_yaml()`). These are older methods.

## Using `ModelCheckpoint` Callback
During training with `model.fit()`, the [[Keras_Callbacks|`tf.keras.callbacks.ModelCheckpoint`]] callback is highly recommended for automatically saving the model (or its weights) at regular intervals or when a monitored metric improves. This helps in:
-   Saving the best performing model during a long training run.
-   Recovering from interruptions.

See [[Keras_Callbacks]] for an example.

Choosing the right saving strategy depends on your needs: full model for deployment or complete state restoration, weights only for transfer learning or when architecture is defined separately, and architecture only for sharing model structure. The TensorFlow SavedModel format (often via `.keras` extension in Keras v3) is the most robust and recommended for general use.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorBoard_TensorFlow.md
````markdown
---
tags: [python, tensorflow, tf, keras, tensorboard, visualization, monitoring, debugging, deep_learning, concept, example]
aliases: [TensorBoard, TFBoard, TensorFlow Visualization]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Callbacks|TensorBoard Callback]]"
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorBoard: TensorFlow's Visualization Toolkit

**TensorBoard** is a powerful visualization toolkit provided with TensorFlow. It allows you to visualize various aspects of your TensorFlow/Keras model training and execution, making it easier to understand, debug, and optimize your machine learning workflows.

TensorBoard works by reading log files generated by TensorFlow (or other libraries like PyTorch via `torch.utils.tensorboard`). You then run TensorBoard as a web server, which provides an interactive web interface to view the logged data.

## Key Features and Dashboards

[list2tab|#TensorBoard Features]
- Scalars Dashboard
    -   **Purpose:** Track and visualize scalar metrics over time (epochs or steps), such as:
        -   Loss (training and validation)
        -   Accuracy (training and validation)
        -   Learning rate
    -   **Use Case:** Monitoring training progress, identifying overfitting/underfitting, comparing different training runs.
- Graphs Dashboard
    -   **Purpose:** Visualize the computation graph of your TensorFlow model.
    -   **Use Case:** Understanding model architecture, debugging graph construction issues (less critical with Eager Execution default but still useful for `@tf.function` graphs or Keras model structures).
- Histograms Dashboard
    -   **Purpose:** Visualize the distribution of tensor values (e.g., weights, biases, activations, gradients) over time as histograms.
    -   **Use Case:** Diagnosing issues like vanishing/exploding gradients, dead neurons, or observing how weights evolve during training.
- Distributions Dashboard
    -   **Purpose:** Similar to histograms, but shows a more condensed view of how distributions of tensor values change over time.
- Images Dashboard
    -   **Purpose:** Display images that are logged during training or evaluation (e.g., input images, generated images from a GAN, feature maps).
- Audio Dashboard
    -   **Purpose:** Embed and play audio clips logged during training (e.g., for speech synthesis or audio generation models).
- Text Dashboard
    -   **Purpose:** Display arbitrary text information logged during runs.
- Projector (Embedding Projector)
    -   **Purpose:** Visualize high-dimensional embeddings (e.g., word embeddings, image embeddings) in a lower-dimensional space (typically 2D or 3D using PCA or t-SNE).
    -   **Use Case:** Exploring relationships and clusters within embedding spaces.
- Profiler
    -   **Purpose:** Helps understand the performance characteristics of your model execution on CPU/GPU/TPU.
    -   **Use Case:** Identifying performance bottlenecks, optimizing execution time and resource usage.
- HParams (Hyperparameters) Dashboard
    -   **Purpose:** Systematically log and compare the results of multiple training runs with different hyperparameter settings.
    -   **Use Case:** Facilitating hyperparameter tuning and understanding their impact on model performance.

## Using TensorBoard with `tf.keras`
The most common way to use TensorBoard with Keras models is via the **`tf.keras.callbacks.TensorBoard` callback**.

1.  **Create the Callback:**
    ```python
    from tensorflow import keras
    import datetime

    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = keras.callbacks.TensorBoard(
        log_dir=log_dir,
        histogram_freq=1,  # Log histograms every 1 epoch
        write_graph=True,
        write_images=False, # Set to True if you log images
        update_freq='epoch', # 'batch' or integer for steps
        profile_batch=0 # Disable profiler by default, or set e.g., '100,200' to profile batches 100-200
    )
    ```
    -   `log_dir`: Directory where TensorBoard log files will be written. It's good practice to use timestamped subdirectories for different runs.
    -   `histogram_freq`: Frequency (in epochs) to compute activation and weight histograms. Can be performance intensive.
    -   `write_graph`: Whether to visualize the Keras model graph.
    -   `update_freq`: How often to write scalar summaries.

2.  **Pass to `model.fit()`:**
    ```python
    # model = ... # Your compiled Keras model
    # X_train, y_train = ...
    # X_val, y_val = ...

    # history = model.fit(
    #     X_train, y_train,
    #     epochs=20,
    #     validation_data=(X_val, y_val),
    #     callbacks=[tensorboard_callback] # Add the callback here
    # )
    ```

3.  **Launch TensorBoard:**
    Open your terminal or command prompt, navigate to the directory *above* your `logs` directory (or provide the full path to `log_dir`), and run:
    ```bash
    tensorboard --logdir logs/fit
    # Or, if your log_dir was, e.g., "my_custom_logs/run1":
    # tensorboard --logdir my_custom_logs
    ```    TensorBoard will start a web server, typically on `http://localhost:6006` (or another port if 6006 is busy). Open this URL in your web browser to view the dashboards.

## Logging Custom Data with `tf.summary`
For more fine-grained control or logging custom scalars, images, histograms, etc., you can use the `tf.summary` API directly, often within custom training loops or custom Keras callbacks.

1.  **Create a Summary File Writer:**
    ```python
    # summary_writer = tf.summary.create_file_writer(log_dir_custom_run)
    ```
2.  **Log Data within a `with summary_writer.as_default():` context:**
    ```python
    # with summary_writer.as_default():
    #     tf.summary.scalar("my_custom_metric", metric_value, step=epoch_or_step)
    #     tf.summary.image("my_input_image", image_tensor, step=epoch_or_step)
    #     tf.summary.histogram("layer_weights", layer.get_weights(), step=epoch_or_step)
    ```

**Example: Logging custom scalar in a custom training loop (conceptual)**
```python
import tensorflow as tf
# Assume model, optimizer, loss_fn, train_dataset are defined

# logdir = "logs/custom_training/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# summary_writer = tf.summary.create_file_writer(logdir)

# num_epochs = 5
# for epoch in range(num_epochs):
#     for step, (x_batch, y_batch) in enumerate(train_dataset):
#         with tf.GradientTape() as tape:
#             predictions = model(x_batch, training=True)
#             loss = loss_fn(y_batch, predictions)
#         grads = tape.gradient(loss, model.trainable_variables)
#         optimizer.apply_gradients(zip(grads, model.trainable_variables))

#         if step % 100 == 0:
#             with summary_writer.as_default():
#                 tf.summary.scalar('batch_loss', loss, step=optimizer.iterations)
#                 # Log learning rate if it changes
#                 # current_lr = optimizer.learning_rate
#                 # if callable(current_lr): # If it's a schedule
#                 #    current_lr = current_lr(optimizer.iterations)
#                 # tf.summary.scalar('learning_rate', current_lr, step=optimizer.iterations)
#             print(f"Epoch {epoch+1}, Step {step}, Loss: {loss.numpy()}")
```

TensorBoard is an invaluable tool for debugging, monitoring, and optimizing TensorFlow/Keras models, providing rich visualizations of the training process and model internals.

---
`````

This completes the Keras API components and the initial set of TensorFlow core concepts. Next, I'll create notes for TensorFlow Distributed Training, TFLite, and TF.js. These might be slightly higher-level overviews as they are extensive topics themselves.

---

Okay, let's address the remaining Spark questions. I'll create new notes for those that warrant it or integrate answers into existing notes if more appropriate and not yet fully covered.

**Remaining Spark Questions Review & Plan:**
*   "What is the difference between Hadoop and Spark?" -> Covered in `Spark_vs_Hadoop_MapReduce.md`.
*   "what is the difference between MapReduce and Spark?" -> Covered in `Spark_vs_Hadoop_MapReduce.md`.
*   "Why do we need Spark? Can't we just easily read files/databases directly?" -> Covered in `Why_Spark_Needed.md`.
*   "What is a Spark Context?" -> Covered in `PySpark_SparkSession_SparkContext.md`.
*   "What is the difference between a Session and a Context?" -> Covered in `PySpark_SparkSession_SparkContext.md`.
*   "What is the purpose of a Spark Cluster?" -> Covered in `Spark_Cluster_Architecture.md`.
*   "For each of the following modules/classes, explain what is its purpose and its advantages: RDD, DataFrame and SQL, Streaming, MLlib, GraphFrames, Resource" -> RDD, DataFrame/SQL, Streaming, MLlib, GraphFrames/GraphX are covered in their respective notes (`RDD_Resilient_Distributed_Dataset.md`, `Spark_DataFrame_SQL.md` (implicitly, but I can add more detail here or in `PySpark_DataFrame_Operations.md`), `Spark_Streaming_Structured_Streaming.md`, `Spark_MLlib.md`, `Spark_GraphX_GraphFrames.md`). "Resource" is broad; resource management is covered under `Spark_Cluster_Manager.md` and `YARN.md`. I will create a summary note `Spark_Ecosystem_Components_Purpose_Advantages.md` to explicitly address this question by linking and summarizing.
*   "What is the difference between a Spark DataFrame and a Pandas DataFrame?" -> Covered in `Spark_DataFrame_vs_Pandas_DataFrame.md`.
*   "What are the Spark data sources?" -> Covered in `PySpark_Data_Sources.md`.
*   "What is the difference between a transformation and an action?" -> Covered in `Spark_Transformations_Actions.md`.
*   "What are the advantages of laziness?" -> Covered in `Spark_Lazy_vs_Eager_Execution.md`.
*   "When is a shuffle operation needed?" -> Covered in `Spark_Shuffle_Operations.md`.
*   "Explain `explain`" -> Covered in `Spark_explain_Plan.md`.
*   "What is the importance of `repartition`?" -> Primarily covered in `Spark_Performance_Tuning.md` (under Partitioning). I can make this more explicit or add a dedicated small note if needed, but it fits well there.
*   "Describe a use case for `map` and another for `mapPartitions`." -> Covered in `Spark_map_vs_mapPartitions.md`.
*   "Is there a parallel for SQL constraints in Spark? What about indexes? If yes - what is it? If no - why?" -> Covered in `Spark_SQL_Constraints_Indexes.md`.
*   "Why and when are `lit` and `col` useful?" -> Covered in `PySpark_SQL_Functions.md`.
*   "What is the difference between `parquet` files and `csv` files?" -> Covered in `Parquet_vs_CSV_Spark.md`.
*   "Can we read data directly from a JSON file using Spark? How? Why would we do that?" -> Covered in `PySpark_Data_Sources.md`.

The main one needing a dedicated note is the summary for "For each of the following modules/classes, explain what is its purpose and its advantages...".

Let's create that summary note first.

---

`````markdown

Filename: 180_Big_Data/Spark/Spark_Ecosystem_Components_Purpose_Advantages.md
````markdown
---
tags: [spark, ecosystem, rdd, dataframe, sql, streaming, mllib, graphx, graphframes, purpose, advantages, concept]
aliases: [Spark Modules Purpose, Advantages of Spark Components]
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_Streaming_Structured_Streaming]]"
  - "[[Spark_MLlib]]"
  - "[[Spark_GraphX_GraphFrames]]"
  - "[[Spark_Cluster_Manager]]" # For "Resource" aspect
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark Ecosystem Components: Purpose and Advantages

Apache Spark is a unified analytics engine composed of several key components or modules, each designed for specific data processing tasks. This note summarizes their purpose and advantages.

>[!question] For each of the following modules/classes, explain what is its purpose and its advantages: RDD, DataFrame and SQL, Streaming, MLlib, GraphFrames, Resource.

[list2tab|#Spark Component Summary]
- Component/Module
    - Purpose
        - Key Advantages
- [[RDD_Resilient_Distributed_Dataset|RDD (Resilient Distributed Dataset)]]
    -   **Purpose:** Spark's fundamental, low-level data abstraction. Represents an immutable, partitioned collection of elements that can be operated on in parallel across a cluster. Forms the foundation upon which higher-level APIs are built.
    -   **Advantages:**
        -   **Fault Tolerance:** Can be recomputed from lineage if a partition is lost.
        -   **Immutability:** Simplifies consistency and reasoning about transformations.
        -   **Flexibility:** Can store any type of Python, Java, or Scala objects, making them suitable for unstructured or semi-structured data.
        -   **Low-Level Control:** Offers fine-grained control over data partitioning and physical execution.
        -   **[[Spark_Lazy_vs_Eager_Execution|Lazy Evaluation]]:** Enables optimizations by deferring computation.
- [[Spark_DataFrame_SQL|DataFrame and Spark SQL]]
    -   **Purpose:**
        -   **DataFrame:** A distributed collection of data organized into named columns, similar to a relational table or Pandas DataFrame, but distributed and optimized for Spark.
        -   **Spark SQL:** A module for structured data processing that allows querying data via SQL (standard SQL or HiveQL) as well as with the programmatic DataFrame API.
    -   **Advantages:**
        -   **Optimization:** Benefits significantly from Spark's [[Catalyst_Optimizer_Tungsten_Engine|Catalyst optimizer]] and [[Catalyst_Optimizer_Tungsten_Engine|Tungsten execution engine]], often leading to better performance than raw RDD operations for structured data.
        -   **Schema:** Enforces a schema, providing structure, error checking, and enabling more efficient storage and processing.
        -   **Ease of Use:** DataFrame API and SQL are generally more intuitive and concise for structured data manipulation.
        -   **Data Source Integration:** Excellent support for reading from and writing to various structured [[PySpark_Data_Sources|data sources]] (JSON, Parquet, CSV, JDBC, Hive).
        -   **Interoperability:** Can be easily converted to/from RDDs and Pandas DataFrames.
- [[Spark_Streaming_Structured_Streaming|Streaming (Spark Streaming & Structured Streaming)]]
    -   **Purpose:** To process live data streams in a scalable, high-throughput, and fault-tolerant manner.
        -   **Spark Streaming (DStream API - Legacy):** Processes data in micro-batches (sequences of RDDs).
        -   **Structured Streaming (DataFrame API - Recommended):** Treats a live data stream as a continuously appending, unbounded table, allowing use of DataFrame/SQL API for stream processing.
    -   **Advantages (especially Structured Streaming):**
        -   **Unified API:** Use largely the same DataFrame/SQL API for both batch and stream processing.
        -   **End-to-End Exactly-Once Semantics:** Strong fault tolerance guarantees with supported sources/sinks.
        -   **Event Time Processing & Windowing:** Robust support for handling out-of-order data (with watermarking) and complex windowed aggregations.
        -   **Integration:** Connects to various streaming sources like Kafka, Kinesis, Flume, file systems.
        -   **Stateful Operations:** Efficiently manages complex stateful stream processing.
- [[Spark_MLlib|MLlib (Machine Learning Library)]]
    -   **Purpose:** Spark's built-in library for scalable machine learning. Provides common ML algorithms and utilities.
    -   **Components:** Includes tools for classification, regression, clustering, collaborative filtering, dimensionality reduction, feature extraction/transformation, and ML pipeline construction (`spark.ml` package is DataFrame-based and recommended).
    -   **Advantages:**
        -   **Scalability:** Designed to train models on large datasets distributed across a cluster.
        -   **Integration:** Works seamlessly with Spark DataFrames for data input, feature engineering, and model deployment.
        -   **Ease of Use:** High-level API for common ML tasks and building ML pipelines.
        -   **Distributed Algorithms:** Implements distributed versions of many common ML algorithms.
- [[Spark_GraphX_GraphFrames|GraphX / GraphFrames (Graph Processing)]]
    -   **Purpose:** Libraries for performing graph computations and analytics on Spark.
        -   **GraphX (RDD-based):** Spark's original graph processing API. Provides property graphs and a Pregel-like API.
        -   **GraphFrames (DataFrame-based):** Newer API representing graphs using DataFrames for vertices and edges. Allows leveraging Spark SQL and DataFrame optimizations.
    -   **Advantages:**
        -   **Scalable Graph Analysis:** Enables analysis of large-scale graphs that don't fit on a single machine.
        -   **Integration:** Can combine graph processing with other Spark components (SQL, MLlib, Streaming).
        -   **Common Algorithms:** Provides standard graph algorithms like PageRank, Connected Components, Shortest Paths, Triangle Counting.
        -   **Querying (GraphFrames):** Supports declarative graph queries and motif finding.
- Resource (Management Aspect)
    -   **Purpose:** Spark itself doesn't have a module named "Resource." Instead, it relies on an external **[[Spark_Cluster_Manager|Cluster Manager]]** (like Standalone, YARN, Mesos, Kubernetes) for resource allocation and management across the cluster. Spark's driver program, through the `SparkContext`, negotiates with the Cluster Manager for resources (CPU cores, memory) to launch executors.
    -   **Advantages of this decoupled approach:**
        -   **Flexibility:** Spark can run in various environments and alongside other applications managed by the same cluster manager (e.g., MapReduce jobs on YARN).
        -   **Efficient Resource Sharing:** Cluster managers can implement sophisticated scheduling policies (e.g., fair sharing, capacity scheduling) to manage resources among multiple users and applications.
        -   **Scalability:** The cluster manager handles the complexities of resource tracking and allocation across potentially thousands of nodes.
        -   **Isolation:** Executors for different applications run in isolated processes (or containers in Kubernetes), providing resource and fault isolation.

Each component in the Spark ecosystem is designed to tackle specific aspects of Big Data processing, and their integration within a unified engine provides a powerful and versatile platform.

---
````

Now that these Spark conceptual questions are addressed, I will proceed to **Part 2: Creating notes for the remaining Python libraries (TensorFlow details, Beautiful Soup details, Scrapy details)** as per your previous instruction. I'll start with TensorFlow, continuing to build out its MOC with more specific notes.

I will create notes for:
-   `TensorFlow_Variables.md` (This was already created, I'll ensure it's robust if it was a stub)
-   `TensorFlow_Operations.md` (This was also created, will review)
-   `TensorFlow_Graphs_Eager_Execution.md` (Created, will review)
-   `TensorFlow_Automatic_Differentiation.md` (Created, will review)
-   `Keras_API_in_TensorFlow.md` (Created, will review)
-   `Keras_Sequential_Functional_API.md` (Created, will review)
-   `Keras_Layers.md` (Created, will review)
-   `Keras_Optimizers.md` (Created, will review)
-   `Keras_Loss_Functions.md` (Created, will review)
-   `Keras_Metrics.md` (Created, will review)
-   `Keras_Callbacks.md` (Created, will review)
-   `TensorFlow_Data_Pipeline_tf_data.md` (Created, will review)
-   `TensorFlow_Saving_Loading_Models.md` (Created, will review)
-   `TensorBoard_TensorFlow.md` (Created, will review)

It seems I have already created many of these in the previous turns. I will now focus on any missing ones or those that need more detail, specifically:
-   `TensorFlow_Distributed_Training.md`
-   `TensorFlow_Lite_TFLite.md`
-   `TensorFlow_js_TFJS.md`
-   `TensorFlow_Serving.md`

And then move to the detailed notes for Beautiful Soup and Scrapy.

---

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Distributed_Training.md
````markdown
---
tags: [python, tensorflow, tf, keras, distributed_training, scaling, multi_gpu, tpu, concept, example]
aliases: [tf.distribute.Strategy, Distributed TensorFlow, Scaling TF Training]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Keras_API_in_TensorFlow]]" # Distributed training works with Keras models
  - "[[TensorFlow_Data_Pipeline_tf_data|tf.data]]" # Efficient input pipelines are crucial
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
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
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Lite_TFLite.md
````markdown
---
tags: [python, tensorflow, tf, tflite, mobile_deployment, edge_computing, model_optimization, inference, concept, example]
aliases: [TFLite, TensorFlow Lite, TF Lite]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]" # Models are converted to TFLite
  - "[[Model_Quantization]]" # Placeholder for quantization concept
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow Lite (TFLite)

**TensorFlow Lite (TFLite)** is an open-source deep learning framework from Google designed for on-device inference on mobile phones (Android and iOS), embedded Linux devices (like Raspberry Pi), and microcontrollers. It enables running [[TensorFlow_MOC|_TensorFlow_MOC]] models with low latency and a small binary size, optimized for resource-constrained devices.

## Core Purpose and Benefits
-   **On-Device Machine Learning:** Run ML models directly on edge devices without needing a server connection.
-   **Low Latency:** Faster inference by avoiding network round-trips.
-   **Small Model Size:** Tools to convert and optimize TensorFlow models into a compact `.tflite` format.
-   **Privacy:** User data can remain on the device.
-   **Offline Capability:** Models can run without an internet connection.
-   **Power Efficiency:** Optimized for low power consumption on mobile and embedded hardware.
-   **Hardware Acceleration:** Supports acceleration using device GPUs, DSPs (Digital Signal Processors), and NPUs (Neural Processing Units) where available.

## TFLite Workflow

The typical workflow involves:
1.  **Training a TensorFlow Model:** Train a standard TensorFlow model (usually using `tf.keras`).
2.  **Converting the Model:** Use the **TensorFlow Lite Converter** to convert the trained TensorFlow model into the TensorFlow Lite FlatBuffer format (`.tflite`).
    -   This step can also involve optimizations like [[Model_Quantization|quantization]].
3.  **Deploying to Device:** Deploy the `.tflite` model to a mobile app, embedded device, or microcontroller.
4.  **Running Inference:** Use the **TensorFlow Lite Interpreter** (available for various platforms like Java/Kotlin for Android, Swift/Objective-C for iOS, C++, Python) to load the `.tflite` model and perform inference on new input data.

[d2]
```d2
direction: right
shape: sequence_diagram

TF_Keras_Model: "1. Train TensorFlow/Keras Model" {
  shape: process
  style.fill: "#BBDEFB" # Light blue
}

TFLite_Converter: "2. TFLite Converter" {
  shape: process
  style.fill: "#C8E6C9" # Light green
  Optimization: "Optimization (e.g., Quantization)"
}

TFLite_Model: "3. `.tflite` Model File" {
  shape: document
  style.fill: "#FFF9C4" # Light yellow
}

Device: "4. Deploy to Edge Device\n(Mobile, Embedded, MCU)" {
  shape: device
  style.fill: "#FFCCBC" # Light red
  TFLite_Interpreter: "TFLite Interpreter" {
    shape: process
    style.fill: "#FFAB91"
  }
  InputData: "New Input Data"
  OutputPredictions: "Predictions"
}

TF_Keras_Model -> TFLite_Converter: "SavedModel or Keras .h5/.keras"
TFLite_Converter -> TFLite_Model: "Generates"
TFLite_Converter.Optimization -> TFLite_Converter
TFLite_Model -> Device.TFLite_Interpreter: "Load Model"
Device.InputData -> Device.TFLite_Interpreter: "Feed Data"
Device.TFLite_Interpreter -> Device.OutputPredictions: "Run Inference"

style TF_Keras_Model { icon: "🧠" }
style TFLite_Converter { icon: "🔄" }
style TFLite_Model { icon: "📄" }
style Device { icon: "📱" }
```

## Model Optimization Techniques for TFLite

To make models suitable for on-device execution, TFLite employs several optimization techniques, often applied during the conversion process:

[list2tab|#TFLite Optimizations]
- [[Model_Quantization|Quantization]]
    -   **Concept:** Reducing the precision of the model's weights and/or activations from floating-point (e.g., `float32`) to lower-bit representations (e.g., `int8`, `float16`).
    -   **Benefits:**
        -   **Reduced Model Size:** Significantly smaller model files.
        -   **Faster Inference:** Integer arithmetic is often faster on many CPUs and specialized hardware (DSPs, NPUs).
        -   **Lower Power Consumption.**
    -   **Types:**
        -   **Post-Training Quantization:** Quantize an already trained `float32` model. Several modes exist:
            -   Dynamic range quantization (weights to int8, activations float32, dynamic range at runtime).
            -   Full integer quantization (weights and activations to int8, requires a representative dataset for calibration).
            -   Float16 quantization (weights and activations to float16).
        -   **Quantization-Aware Training (QAT):** Simulates quantization effects during training, often leading to better accuracy for quantized models compared to post-training quantization.
- Pruning
    -   **Concept:** Systematically removing weights from the model that have minimal impact on its performance, creating sparse models.
    -   **Benefits:** Can reduce model size and sometimes inference time.
    -   Often requires fine-tuning after pruning.
- Weight Clustering
    -   **Concept:** Grouping weights into a smaller number of clusters and sharing a single weight value per cluster.
    -   **Benefits:** Reduces the number of unique weight values, enabling better compression.

## TensorFlow Lite Converter (Python API)
The converter is part of the TensorFlow Python library.

**Example: Converting a Keras SavedModel to TFLite**
```python
import tensorflow as tf
import numpy as np

# 1. Create and train a simple Keras model (or load an existing one)
# For e-commerce: predict if a product image contains a 'shoe' or 'shirt'
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(32, 32, 3)), # Dummy input shape
#     tf.keras.layers.MaxPooling2D((2,2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(1, activation='sigmoid') # Binary: shoe vs shirt
# ])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Dummy training data
# X_train_dummy_img = np.random.rand(10, 32, 32, 3).astype(np.float32)
# y_train_dummy_label = np.random.randint(0, 2, 10)
# model.fit(X_train_dummy_img, y_train_dummy_label, epochs=1, verbose=0)

# Save the Keras model in SavedModel format (default for model.save without .h5)
# keras_model_path = "./my_image_classifier_keras_model"
# model.save(keras_model_path)

# 2. Convert the SavedModel to TensorFlow Lite format
# converter = tf.lite.TFLiteConverter.from_saved_model(keras_model_path)

# Optional: Apply optimizations (e.g., default optimization which includes quantization)
# converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Optional: Provide a representative dataset for full integer quantization
# def representative_dataset_gen():
#     for _ in range(100): # Yield a few samples
#         yield [np.random.rand(1, 32, 32, 3).astype(np.float32)] # Must be a list of inputs
# converter.representative_dataset = representative_dataset_gen
# converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8] # For int8 quantization
# converter.inference_input_type = tf.int8  # or tf.uint8
# converter.inference_output_type = tf.int8 # or tf.uint8


# Convert the model
# tflite_model_content = converter.convert()

# 3. Save the TFLite model to a .tflite file
# tflite_model_file_path = "my_image_classifier.tflite"
# with open(tflite_model_file_path, 'wb') as f:
#     f.write(tflite_model_content)
# print(f"TFLite model saved to: {tflite_model_file_path}")

# You can also convert from a Keras model object directly:
# converter_from_keras = tf.lite.TFLiteConverter.from_keras_model(model)
# tflite_model_keras_direct = converter_from_keras.convert()
```

## TensorFlow Lite Interpreter
Once you have the `.tflite` model, you use the TFLite interpreter on the target device to run inference.

**Example: Python TFLite Interpreter (for testing, or on devices like Raspberry Pi)**
```python
import tensorflow as tf # For interpreter in Python
import numpy as np

# Load the TFLite model and allocate tensors.
# tflite_model_path = "my_image_classifier.tflite" # From previous step
# try:
#     interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
#     interpreter.allocate_tensors() # Important step

    # Get input and output tensor details
    # input_details = interpreter.get_input_details()
    # output_details = interpreter.get_output_details()
    # print("\nInput Details:", input_details)
    # print("Output Details:", output_details)

    # Prepare a sample input (must match model's expected input shape and type)
    # input_shape = input_details[0]['shape'] # e.g., [1, 32, 32, 3]
    # sample_input_image = np.random.rand(*input_shape).astype(np.float32)
    # If model is quantized to int8, input data also needs to be int8 and scaled appropriately
    # if input_details[0]['dtype'] == np.int8:
    #     input_scale, input_zero_point = input_details[0]['quantization']
    #     sample_input_image = (sample_input_image / input_scale + input_zero_point).astype(np.int8)


    # Set the value of the input tensor
    # interpreter.set_tensor(input_details[0]['index'], sample_input_image)

    # Run inference
    # interpreter.invoke()

    # Get the result
    # output_data = interpreter.get_tensor(output_details[0]['index'])
    # print("\nPrediction output from TFLite model:", output_data)

# except Exception as e:
#     print(f"Error with TFLite interpreter (is model file valid and path correct?): {e}")
```
Interpreters are also available for Java/Kotlin (Android), Swift/Objective-C (iOS), and C++.

## Use Cases
-   **Mobile Applications:** Image classification, object detection, text classification, smart replies, on-device speech recognition.
-   **Embedded Systems & IoT:** Anomaly detection in sensor data, keyword spotting, simple gesture recognition.
-   **Microcontrollers:** Ultra-low power ML applications with TensorFlow Lite for Microcontrollers.

TensorFlow Lite bridges the gap between powerful TensorFlow models trained on servers/desktops and the resource constraints of edge devices, enabling a new class of intelligent applications.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_js_TFJS.md
````markdown
---
tags: [python, tensorflow, tf, tfjs, javascript, web_ml, browser_ml, nodejs_ml, concept, example]
aliases: [TF.js, TensorFlow.js, JavaScript TensorFlow]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]" # Models can be converted for TF.js
  - "[[Deep_Learning_Overview]]"
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow.js (TF.js)

**TensorFlow.js (TF.js)** is an open-source hardware-accelerated JavaScript library for training and running machine learning models directly in the browser or in Node.js. It brings the power of TensorFlow and deep learning to the JavaScript ecosystem.

## Core Purpose and Benefits
-   **ML in the Browser:** Enables running ML models directly in the user's web browser.
    -   **Interactivity:** Models can interact with webpage content, user inputs (camera, microphone).
    -   **Privacy:** User data can remain client-side, not needing to be sent to a server for inference.
    -   **Low Latency:** Inference happens locally, avoiding network delays.
    -   **Accessibility:** No complex server-side setup needed for users to experience ML features.
-   **ML in Node.js:** Allows for server-side JavaScript ML applications using TensorFlow.
-   **Run Existing Models:** Convert pre-trained TensorFlow (Python) models to a format usable by TensorFlow.js.
-   **Train Models from Scratch:** Define, train, and run models entirely in JavaScript using an API similar to Keras.
-   **Hardware Acceleration:** Can leverage WebGL for GPU acceleration in the browser, and TensorFlow's C++ backend in Node.js.

## Key Components and APIs of TensorFlow.js

[list2tab|#TF.js Components]
- Core API (`@tensorflow/tfjs-core`)
    -   Low-level linear algebra operations (similar to NumPy/TensorFlow Python Core).
    -   Defines `tf.Tensor` objects in JavaScript.
    -   Provides operations for tensor manipulation, math, etc.
- Layers API (`@tensorflow/tfjs-layers`)
    -   A high-level API for building neural networks, modeled directly after the [[Keras_API_in_TensorFlow|Keras API]].
    -   Define models using `tf.sequential()` or the functional API `tf.model()`.
    -   Includes common layers: `tf.layers.dense()`, `tf.layers.conv2d()`, `tf.layers.lstm()`, etc.
    -   Compile models with optimizers, loss functions, and metrics.
    -   Train models using `model.fit()` or `model.fitDataset()`.
- Converter (`@tensorflow/tfjs-converter`)
    -   Tools to convert pre-trained TensorFlow SavedModels or Keras H5 models (from Python) into a format that can be loaded by TensorFlow.js.
    -   The conversion typically results in a `model.json` file (graph topology and weights manifest) and one or more binary shard files for the weights.
- Data API (`@tensorflow/tfjs-data`)
    -   Provides an API similar to `tf.data` for creating efficient input pipelines for training models in JavaScript (e.g., reading from webcams, microphones, files, DOM elements).
- Pre-trained Models (`@tensorflow-models/*`)
    -   A collection of pre-trained models for common tasks, ready to use in JavaScript applications.
    -   Examples: MobileNet (image classification), PoseNet (pose estimation), Coco-SSD (object detection), Universal Sentence Encoder (text embeddings), Speech Commands.
- Backends
    -   TensorFlow.js can run on different backends for computation:
        -   `tfjs-backend-cpu`: Runs on CPU (JavaScript).
        -   `tfjs-backend-webgl`: Uses WebGL for GPU acceleration in the browser (most common for browsers).
        -   `tfjs-backend-wasm`: Uses WebAssembly for CPU acceleration, can be faster than plain JS.
        -   `tfjs-node` (for Node.js): Binds to the TensorFlow C library for native speed on CPU.
        -   `tfjs-node-gpu` (for Node.js): Binds to TensorFlow C library with GPU support (CUDA).

## Workflow Examples

### 1. Using a Pre-trained Model (e.g., MobileNet for Image Classification in Browser)
**HTML:**
```html
<!-- <!DOCTYPE html>
<html>
<head>
    <title>TF.js Image Classification</title>
    <!-- Load TensorFlow.js and MobileNet model -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@latest/dist/mobilenet.min.js"></script>
</head>
<body>
    <h1>Image Classifier with TF.js</h1>
    <img id="myImage" src="path/to/your/image.jpg" width="224" height="224" alt="image to classify"/> <br/>
    <input type="file" id="imageUpload" accept="image/*" />
    <div id="predictions">Loading model and making predictions...</div>

    <script>
        const imgElement = document.getElementById('myImage');
        const predictionsElement = document.getElementById('predictions');
        const imageUpload = document.getElementById('imageUpload');
        let model;

        async function loadAndPredict() {
            if (!model) {
                predictionsElement.innerText = 'Loading MobileNet model...';
                model = await mobilenet.load(); // Load the MobileNet model
                predictionsElement.innerText = 'Model loaded.';
            }
            
            if (imgElement.src && imgElement.src !== window.location.href) { // Check if src is set and not just base URL
                 try {
                    const predictions = await model.classify(imgElement);
                    predictionsElement.innerHTML = '<h3>Predictions:</h3>';
                    predictions.forEach(p => {
                        predictionsElement.innerHTML += `${p.className} : ${p.probability.toFixed(4)}<br>`;
                    });
                } catch (e) {
                    predictionsElement.innerText = 'Error during prediction. Ensure image is loaded correctly.';
                    console.error(e);
                }
            } else {
                 predictionsElement.innerText = 'Please upload an image or ensure the default image path is correct.';
            }
        }
        
        imgElement.onload = () => { // Predict when default image loads
            loadAndPredict();
        };
        if (imgElement.complete && imgElement.naturalHeight !== 0) { // If image already loaded from cache
             loadAndPredict();
        }


        imageUpload.onchange = (event) => {
            const file = event.target.files;
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    imgElement.src = e.target.result;
                    // imgElement.onload will trigger loadAndPredict after src is set
                }
                reader.readAsDataURL(file);
            }
        };
        // Initial prediction if default image is set
        // loadAndPredict(); // Call if default image src is valid
    </script>
</body>
</html> -->
```
*(Note: For the above HTML to work, `path/to/your/image.jpg` needs to be a valid image. The file upload provides interactivity.)*

### 2. Converting a Python Keras Model and Using it in Node.js (Conceptual)
**Step A: Save Keras model in Python and Convert**
```python
# Python (e.g., in a Jupyter Notebook or script)
# import tensorflow as tf
# from tensorflow import keras

# Create and train a simple Keras model (e.g., for classifying product categories)
# model = keras.Sequential([
#     keras.layers.Dense(128, activation='relu', input_shape=(50,)), # 50 features
#     keras.layers.Dense(3, activation='softmax') # 3 product categories
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Dummy training
# X_train = np.random.rand(100, 50)
# y_train = np.random.randint(0, 3, 100)
# model.fit(X_train, y_train, epochs=1, verbose=0)

# Save the model in SavedModel format
# model.save("./my_keras_model_for_tfjs")

# Convert using tensorflowjs_converter (command-line tool)
# Install: pip install tensorflowjs
# In your terminal:
# tensorflowjs_converter --input_format=tf_saved_model \
#                        ./my_keras_model_for_tfjs \
#                        ./my_tfjs_model_output
```
This creates `model.json` and weight shard files in `./my_tfjs_model_output`.

**Step B: Load and use in Node.js**
```javascript
// Node.js script (e.g., predict.js)
// const tf = require('@tensorflow/tfjs-node'); // Or tfjs-node-gpu
// const path = require('path');
// const modelPath = `file://${path.join(__dirname, 'my_tfjs_model_output', 'model.json')}`;

// async function runPrediction() {
//     try {
//         console.log('Loading model...');
//         const model = await tf.loadLayersModel(modelPath);
//         console.log('Model loaded.');
//         model.summary(); // Print model summary

//         // Create dummy input data (batch of 1, 50 features)
//         const inputTensor = tf.tensor2d(Math.random(),);
        
//         console.log('\nMaking prediction...');
//         const prediction = model.predict(inputTensor);
//         prediction.print(); // Prints the tensor

//         const predictedClass = prediction.argMax(-1).dataSync(); // Get the class with highest probability
//         console.log(`Predicted class index: ${predictedClass}`);

//     } catch (error) {
//         console.error("Error during TF.js model execution:", error);
//     }
// }
// runPrediction();
```
To run: `node predict.js` (after `npm install @tensorflow/tfjs-node path`).

## Use Cases
-   **Interactive ML Experiences in Web Browsers:** Image recognition from webcam, real-time pose estimation, style transfer, client-side text analysis.
-   **Accessibility and Reach:** Deploy ML models to anyone with a web browser without requiring them to install specific software or send data to a server.
-   **Privacy-Preserving ML:** Perform inference on user data directly in their browser.
-   **Server-Side JavaScript ML:** Use Node.js for ML tasks like API backends, data preprocessing, or batch inference.
-   **Education:** Teaching ML concepts in a more accessible environment.

TensorFlow.js significantly expands the reach of TensorFlow models to web and JavaScript environments, enabling a wide range of new applications and interactive experiences.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Serving.md
````markdown
---
tags: [python, tensorflow, tf, tf_serving, model_deployment, production, inference_server, concept]
aliases: [TF Serving, TensorFlow Model Server]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models (SavedModel format)]]"
  - "[[RESTful_API]]" # TF Serving often exposes REST APIs
  - "[[gRPC]]" # TF Serving also supports gRPC
  - "[[Docker_Kubernetes_MLOps|Docker & Kubernetes (MLOps)]]" # Common for deploying TF Serving (Placeholder)
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow Serving

**TensorFlow Serving** is a flexible, high-performance serving system for machine learning models, designed for production environments. It allows you to easily deploy trained TensorFlow (and other) models and make them accessible for inference via network requests (typically gRPC or REST APIs).

It helps bridge the gap between model training/research and production deployment.

## Core Purpose and Benefits
-   **Production-Grade Model Deployment:** Provides a robust and scalable solution for serving ML models in live environments.
-   **High Performance:** Optimized for low-latency inference and high throughput. Can leverage hardware acceleration (GPUs).
-   **Model Versioning:** Supports serving multiple versions of a model simultaneously and allows for easy rollback or canary deployments (gradual rollout of new versions).
-   **Batching Requests:** Can automatically batch incoming inference requests to better utilize hardware (especially GPUs).
-   **Extensibility:** Can be extended to serve non-TensorFlow models (e.g., Scikit-learn, XGBoost) by creating custom servables.
-   **Standardized Interface:** Offers consistent gRPC and RESTful HTTP/JSON APIs for making inference requests.
-   **Hot Updates:** Allows updating models in production without server downtime.
-   **Monitoring:** Can integrate with monitoring systems to track server performance and model behavior.

## Architecture Overview

[d2]
```d2
direction: right
shape: sequence_diagram

ClientApp: "Client Application\n(Web, Mobile, Backend)" {
  shape: person
  style.fill: "#BBDEFB"
}

TF_Serving_Server: "TensorFlow Serving Server" {
  shape: process
  style.fill: "#C8E6C9"
  
  APIs: "APIs (gRPC / REST)" {
    shape: process
    style.fill: "#A5D6A7"
  }
  
  Manager: "Manager" {
    shape: process
    style.fill: "#A5D6A7"
    Loader1: "Loader (Model Version 1)"
    Loader2: "Loader (Model Version 2)"
  }

  Source: "Source (Model Repository)" {
    shape: database # Represents storage of models
    style.fill: "#FFF9C4"
    SavedModel_v1: "SavedModel (Version 1)"
    SavedModel_v2: "SavedModel (Version 2)"
  }
}

Hardware: "Hardware (CPU/GPU/TPU)" {
  shape: device
  style.fill: "#FFCCBC"
}


ClientApp -> TF_Serving_Server.APIs: "1. Inference Request (Data + ModelSpec)"
TF_Serving_Server.APIs -> TF_Serving_Server.Manager: "2. Route to appropriate Loader/Model"
TF_Serving_Server.Manager -> TF_Serving_Server.Source: "3. Loads Model (if not already loaded)"
TF_Serving_Server.Source.SavedModel_v1 -> TF_Serving_Server.Manager.Loader1
TF_Serving_Server.Manager.Loader1 -> Hardware: "4. Perform Inference"
Hardware -> TF_Serving_Server.Manager.Loader1: "5. Prediction Result"
TF_Serving_Server.Manager.Loader1 -> TF_Serving_Server.APIs: "6. Prediction Result"
TF_Serving_Server.APIs -> ClientApp: "7. Inference Response (Predictions)"


style ClientApp { icon: "💻" }
style TF_Serving_Server { icon: "🏭" }
style APIs { icon: "🔌" }
style Manager { icon: "🚦" }
style Source { icon: "🗄️" }
style Hardware { icon: "⚙️" }
```

**Key Components:**
1.  **Servables:** The core abstraction in TensorFlow Serving. A servable is an opaque object that clients use to perform computation (e.g., inference). Typically, a servable is a trained TensorFlow model, but it can be any arbitrary computation.
2.  **Loaders:** Manage the lifecycle of a servable, including loading it from storage, providing access to it, and unloading it.
3.  **Sources:** Plugins that find and provide servables. For example, a source might monitor a file system path for new model versions.
4.  **Managers:** Manage the full lifecycle of servables, including loading, unloading, and serving them. They handle versioning and transitions between model versions.
5.  **Core:** The TensorFlow Serving Core manages the servables, loaders, sources, and managers.
6.  **APIs (Frontends):** Expose interfaces for clients to interact with the served models (e.g., gRPC `PredictService`, `ModelService`; RESTful HTTP/JSON endpoints).

## Workflow

1.  **Train and Save Model:** Train your TensorFlow model and save it in the **[[TensorFlow_Saving_Loading_Models|TensorFlow SavedModel format]]**. This format includes the model graph, weights, and assets.
    ```python
    # model = ... # Your trained tf.keras.Model
    # model.save("path/to/my_model_repo/my_model_name/1") # Directory structure: .../model_name/version_number
    ```
    The version number (e.g., `1`) is important for model versioning in TF Serving.

2.  **Install TensorFlow Serving:**
    -   Often done using Docker: `docker pull tensorflow/serving`
    -   Or by installing from source or pre-built binaries.

3.  **Start the TensorFlow Serving Server:**
    Point the server to your model repository.
    ```bash
    # Using Docker (example)
    # docker run -p 8501:8501 --mount type=bind,source=/path/to/my_model_repo/,target=/models/my_model_collection -e MODEL_NAME=my_model_name -t tensorflow/serving
    ```
    -   `-p 8501:8501`: Maps port 8501 (default REST API port) from container to host. Port 8500 is default for gRPC.
    -   `--mount ...`: Mounts your local model repository into the Docker container.
    -   `MODEL_NAME`: The name of the model to serve (must match the subdirectory name in your model repo).
    -   TensorFlow Serving will automatically detect model versions (subdirectories like `1`, `2`, etc.) and can serve the latest or specific versions.

4.  **Make Inference Requests (Client-side):**
    -   **REST API Example (Python `requests`):**
        ```python
        import requests
        import json
        import numpy as np

        # Assume TF Serving is running and serving 'my_model_name' on port 8501
        # server_url = "http://localhost:8501/v1/models/my_model_name:predict" # For latest version
        # server_url_versioned = "http://localhost:8501/v1/models/my_model_name/versions/1:predict" # For specific version

        # Prepare input data in the format expected by your model's serving signature
        # This usually means a JSON object with an "instances" key or "inputs" key.
        # For a model expecting a (None, 784) input (e.g., MNIST):
        # sample_input = np.random.rand(1, 784).tolist() # Batch of 1 instance
        # request_data = json.dumps({"instances": sample_input})
        # For named inputs (common with Keras functional API):
        # request_data_named = json.dumps({
        #     "signature_name": "serving_default", # Often default
        #     "inputs": {
        #         "input_feature_1_name": [[...]], # Batch of data for input 1
        #         "input_feature_2_name": [[...]]  # Batch of data for input 2
        #     }
        # })

        # headers = {"content-type": "application/json"}
        # try:
        #     # response = requests.post(server_url, data=request_data, headers=headers)
        #     # response.raise_for_status() # Raise an exception for HTTP errors
        #     # predictions = response.json()['predictions']
        #     # print("Predictions via REST:", predictions)
        # except requests.exceptions.RequestException as e:
        #     print(f"REST request failed: {e}")
        # except KeyError:
        #     print(f"Could not parse predictions from response: {response.text}")
        ```
    -   **gRPC API:** Generally offers lower latency and higher performance than REST, especially for large payloads or frequent requests. Requires generating client stubs from `.proto` files.

## Key Features for Production
-   **Model Versioning and Rollback:** Serve multiple versions of a model and switch between them seamlessly.
-   **Batching:** TF Serving can automatically batch incoming requests to improve GPU/TPU utilization. Configured via a batching configuration file.
-   **Configuration:** Behavior is controlled via command-line flags or a model server configuration file (for more advanced setups like serving multiple models or custom version policies).
-   **Metrics:** Can expose metrics for monitoring (e.g., request count, latency, error rates) often in Prometheus format.

TensorFlow Serving is a robust solution for taking trained TensorFlow models into production, handling the operational aspects of serving them at scale with high performance and reliability.

---
`````

This completes the planned notes for TensorFlow Distributed Training, TFLite, TF.js, and TF Serving. These provide a good overview of how to scale and deploy TensorFlow models.

Next, I will return to the **Beautiful Soup** and **Scrapy** sections to add more detailed notes on their components as planned earlier.

---

Okay, I will now continue with the detailed notes for **Beautiful Soup** and **Scrapy**, focusing on the remaining key components.

---

### Continuing Beautiful Soup

`````markdown

Filename: 160_Python_Libraries/Beautiful_Soup/BS4_Accessing_Attributes_Text.md
````markdown
---
tags: [python, beautifulsoup, bs4, web_scraping, html_parser, attributes, text_extraction, concept, example]
aliases: [BeautifulSoup Attributes, BS4 Get Text, BS4 Tag Attributes]
related:
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
  - "[[BS4_Parsing_Documents]]"
  - "[[BS4_Navigating_Tree]]"
  - "[[BS4_Searching_Tree]]"
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Beautiful Soup: Accessing Tag Attributes and Text Content

Once you have located a `Tag` object in a parsed Beautiful Soup document (using [[BS4_Navigating_Tree|navigation]] or [[BS4_Searching_Tree|searching]] methods), you'll often need to extract its attributes (like `href` from an `<a>` tag or `class` from a `<div>`) and its textual content.

## Accessing Attributes
A `Tag` object in Beautiful Soup behaves much like a Python dictionary when it comes to accessing its attributes.

[list2tab|#Attribute Access]
- Dictionary-like Access
    -   You can get the value of an attribute by treating the tag like a dictionary:
        ```python
        from bs4 import BeautifulSoup
        html_doc = """
        <a href="http://example.com/product" class="product-link item" id="link123" data-sku="WIDGET-X">Product Page</a>
        <img src="image.jpg" alt="Product Image"/>
        """
        soup = BeautifulSoup(html_doc, 'html.parser')

        # link_tag = soup.find('a')
        # if link_tag:
        #     href_value = link_tag['href'] # Access 'href' attribute
        #     class_value = link_tag['class'] # Access 'class' attribute
        #     id_value = link_tag['id']
        #     data_sku_value = link_tag['data-sku']

        #     print(f"Href: {href_value}")         # Output: http://example.com/product
        #     print(f"Class: {class_value}")       # Output: ['product-link', 'item'] (class can have multiple values, returns a list)
        #     print(f"ID: {id_value}")           # Output: link123
        #     print(f"Data-SKU: {data_sku_value}") # Output: WIDGET-X

            # If an attribute doesn't exist, accessing it like a dict raises a KeyError
            # try:
            #     non_existent_attr = link_tag['style']
            # except KeyError as e:
            #     print(f"KeyError for 'style': {e}")
        ```
- Using `.get()` Method
    -   Similar to Python dictionaries, you can use the `.get()` method, which allows specifying a default value if the attribute is not found (preventing `KeyError`).
        ```python
        # img_tag = soup.find('img')
        # if img_tag:
        #     src_value = img_tag.get('src')
        #     alt_value = img_tag.get('alt')
        #     style_value = img_tag.get('style', 'default-style') # Provide a default

        #     print(f"\nImg Src: {src_value}")       # Output: image.jpg
        #     print(f"Img Alt: {alt_value}")       # Output: Product Image
        #     print(f"Img Style: {style_value}")   # Output: default-style
        ```
- `.attrs` Attribute
    -   You can get a Python dictionary of all a tag's attributes using `tag.attrs`.
        ```python
        # link_tag = soup.find('a')
        # if link_tag:
        #     all_attributes = link_tag.attrs
        #     print("\nAll attributes of <a> tag:", all_attributes)
        #     # Output: {'href': 'http://example.com/product', 'class': ['product-link', 'item'], 'id': 'link123', 'data-sku': 'WIDGET-X'}
        ```
- Multi-valued Attributes
    -   HTML5 allows some attributes (like `class`) to have multiple values. Beautiful Soup usually returns these as a list of strings.
    -   Other attributes that look multi-valued (like `style` in CSS syntax) are typically returned as a single string by Beautiful Soup, as that's how they are represented in the HTML.

## Accessing Text Content
Beautiful Soup provides several ways to get the text content within a tag, excluding the markup itself.

[list2tab|#Text Extraction]
- `.string` Attribute
    -   If a tag has only one child and that child is a `NavigableString` (i.e., just text, no other tags), then `tag.string` will give you that string.
    -   If a tag contains other tags, or multiple strings, or no string content, `tag.string` will be `None`.
    -   Useful for tags that are guaranteed to contain only simple text (e.g., `<title>`, often `<h1>` or simple `<p>`).
    -   **Example:**
        ```python
        html_text_doc = """
        <p>This is <b>bold</b> text.</p>
        <title>Simple Title</title>
        <div>Just text here</div>
        """
        soup_text = BeautifulSoup(html_text_doc, 'html.parser')

        # p_tag = soup_text.find('p')
        # print(f"\n.string of <p>: {p_tag.string}") # Output: None (because it contains a <b> tag)

        # title_tag_text = soup_text.title
        # print(f".string of <title>: {title_tag_text.string}") # Output: Simple Title

        # div_tag_text = soup_text.find('div')
        # print(f".string of <div>: {div_tag_text.string}") # Output: Just text here
        ```- `.strings` Generator
    -   Returns a generator that yields all the strings within a tag, recursively (including strings in child tags).
    -   Preserves whitespace, including newlines.
    -   **Example:**
        ```python
        # p_tag = soup_text.find('p') # <p>This is <b>bold</b> text.</p>
        # print("\n.strings from <p>:")
        # for s in p_tag.strings:
        #     print(repr(s))
        # # Output:
        # # 'This is '
        # # 'bold'
        # # ' text.'
        ```
- `.stripped_strings` Generator
    -   Similar to `.strings`, but it strips leading and trailing whitespace from each string.
    -   It also ignores strings that consist entirely of whitespace.
    -   Often more useful for extracting clean text.
    -   **Example:**
        ```python
        html_whitespace_doc = "<p>  Some \n text with  <b> extra \t space </b>. </p>"
        # soup_whitespace = BeautifulSoup(html_whitespace_doc, 'html.parser')
        # p_whitespace_tag = soup_whitespace.p
        # print("\n.stripped_strings from <p> with extra whitespace:")
        # for s in p_whitespace_tag.stripped_strings:
        #     print(repr(s))
        # # Output:
        # # 'Some'
        # # 'text with'
        # # 'extra \t space' # Note: internal whitespace like \t is kept by default
        # # '.'
        ```
- `.get_text(separator="", strip=False, types=(<NavigableString types>, <CData types>))` Method
    -   This is often the most convenient method for getting all human-readable text from a tag and its children, concatenated into a single Unicode string.
    -   `separator`: A string used to join the different pieces of text found. Default is an empty string (text runs together). A common choice is `" "`.
    -   `strip`: If `True`, whitespace at the beginning and end of each string is stripped before concatenation.
    -   `types`: Allows specifying which types of `NavigableString` elements to include.
    -   **Example (Extracting product description):**
        ```python
        html_product_desc = """
        <div class="description">
            <p>This is an <strong>awesome</strong> e-commerce product. It has many features:</p>
            <ul><li>Feature 1</li><li>Feature 2</li></ul>
            Check it out!
        </div>
        """
        # soup_desc = BeautifulSoup(html_product_desc, 'html.parser')
        # description_div = soup_desc.find('div', class_='description')

        # if description_div:
        #     text_no_sep = description_div.get_text()
        #     print("\nDescription text (no separator):\n", repr(text_no_sep))
            
        #     text_with_space_sep = description_div.get_text(separator=" ", strip=True)
        #     print("\nDescription text (space separator, stripped):\n", repr(text_with_space_sep))
        # # Output (space separator, stripped):
        # # 'This is an awesome e-commerce product. It has many features: Feature 1 Feature 2 Check it out!'
        ```

Choosing the right method for text extraction depends on whether you need a single string, an iterator of strings, and how you want to handle whitespace and nested tags. `.get_text(strip=True, separator=" ")` is often a good starting point for clean, readable text.

---
````

`````markdown

Filename: 160_Python_Libraries/Beautiful_Soup/BS4_Practical_Scraping_Examples.md
````markdown
---
tags: [python, beautifulsoup, bs4, web_scraping, html_parser, example, practical_use_case]
aliases: [BeautifulSoup Scraping Examples, BS4 Use Cases]
related:
  - "[[160_Python_Libraries/Beautiful_Soup/_Beautiful_Soup_MOC|_Beautiful_Soup_MOC]]"
  - "[[BS4_Parsing_Documents]]"
  - "[[BS4_Navigating_Tree]]"
  - "[[BS4_Searching_Tree]]"
  - "[[BS4_Accessing_Attributes_Text]]"
  - "[[Requests_Library]]"
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Beautiful Soup: Practical Scraping Examples

This note demonstrates how to combine [[BS4_Parsing_Documents|parsing]], [[BS4_Navigating_Tree|navigation]], [[BS4_Searching_Tree|searching]], and [[BS4_Accessing_Attributes_Text|attribute/text extraction]] with Beautiful Soup to scrape data from a conceptual e-commerce product page.

**Assumed HTML Structure (Conceptual `product_page.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SuperWidget X1000 - Awesome Products Inc.</title>
</head>
<body>
    <header>
        <img src="/logo.png" alt="Awesome Products Inc. Logo">
        <nav>
            <a href="/">Home</a> | <a href="/products">Products</a> | <a href="/contact">Contact</a>
        </nav>
    </header>
    <main>
        <article class="product-listing" data-product-id="SWX1000">
            <h1 id="product-name">SuperWidget X1000</h1>
            <img class="product-image" src="/images/widget_x1000.jpg" alt="Image of SuperWidget X1000">
            
            <section class="pricing">
                <span class="price-label">Price:</span>
                <span class="current-price">$49.99</span>
                <span class="original-price">$59.99</span>
                <span class="discount-badge">Save 17%</span>
            </section>
            
            <section id="description">
                <h2>Product Description</h2>
                <p>The <strong>SuperWidget X1000</strong> is our latest innovation in widget technology. 
                It offers unparalleled performance and durability. <em>Perfect for all your widgeting needs!</em></p>
                <p>Comes in three exciting colors: Red, Blue, and Green.</p>
            </section>
            
            <section class="features">
                <h2>Key Features</h2>
                <ul>
                    <li>Durable Titanium Alloy</li>
                    <li>Water-Resistant (IP68)</li>
                    <li>Bluetooth 5.2 Connectivity</li>
                    <li>Long-lasting Battery</li>
                </ul>
            </section>
            
            <section class="reviews">
                <h2>Customer Reviews (<span id="review-count">352</span>)</h2>
                <div class="review-item" data-review-id="r001">
                    <p class="reviewer-name">Jane D.</p>
                    <p class="review-rating">Rating: <span>5</span>/5 Stars</p>
                    <p class="review-text">Absolutely love it! Best widget ever.</p>
                </div>
                <div class="review-item" data-review-id="r002">
                    <p class="reviewer-name">John S.</p>
                    <p class="review-rating">Rating: <span>4</span>/5 Stars</p>
                    <p class="review-text">Pretty good, but battery could be better.</p>
                </div>
                <!-- More reviews... -->
                <a href="#more-reviews" class="load-more">Load More Reviews</a>
            </section>
        </article>
    </main>
    <footer>
        <p>&copy; 2024 Awesome Products Inc. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Python Scraping Script:**
```python
import requests # To fetch HTML (conceptually, actual fetching might be blocked)
from bs4 import BeautifulSoup
import pandas as pd # To store scraped data

# --- Step 1: Fetch HTML Content (Conceptual) ---
# In a real scenario, you'd fetch this from a URL.
# For this example, we'll use the HTML string defined above.
# url = "http://example-ecommerce.com/product/SWX1000"
# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status() # Check for HTTP errors
#     html_content = response.text
# except requests.exceptions.RequestException as e:
#     print(f"Could not fetch URL {url}: {e}")
#     # Using the sample HTML directly for this example if fetch fails
html_content_from_above = """... [Copy the HTML from above here for a runnable script] ..."""
# For a script to run, replace the line above with the actual HTML content string.
# For this note, assume html_content_from_above is populated.
if not html_content_from_above.startswith("<!DOCTYPE html>"): # Quick check if it's not populated
    html_content_from_above = """
    <html><head><title>SuperWidget X1000</title></head><body>
    <article class="product-listing" data-product-id="SWX1000">
        <h1 id="product-name">SuperWidget X1000</h1>
        <img class="product-image" src="/images/widget_x1000.jpg" alt="Image of SuperWidget X1000">
        <section class="pricing"><span class="current-price">$49.99</span><span class="original-price">$59.99</span></section>
        <section id="description"><p>The <strong>SuperWidget X1000</strong> is great.</p></section>
        <section class="features"><ul><li>Titanium Alloy</li><li>Water-Resistant</li></ul></section>
        <section class="reviews"><span id="review-count">352</span>
            <div class="review-item" data-review-id="r001"><p class="reviewer-name">Jane D.</p><p class="review-rating">Rating: <span>5</span>/5</p><p class="review-text">Love it!</p></div>
            <div class="review-item" data-review-id="r002"><p class="reviewer-name">John S.</p><p class="review-rating">Rating: <span>4</span>/5</p><p class="review-text">Good.</p></div>
        </section>
    </article></body></html>""" # Minimal fallback

# --- Step 2: Parse HTML with Beautiful Soup ---
soup = BeautifulSoup(html_content_from_above, 'lxml') # Using lxml, or 'html.parser'

# --- Step 3: Extract Product Information ---
product_info = {}

# Product Name
product_name_tag = soup.find('h1', id='product-name')
product_info['name'] = product_name_tag.string.strip() if product_name_tag else None

# Product ID (from data attribute)
product_article_tag = soup.find('article', class_='product-listing')
product_info['id'] = product_article_tag['data-product-id'] if product_article_tag and 'data-product-id' in product_article_tag.attrs else None

# Image URL
product_image_tag = soup.find('img', class_='product-image')
product_info['image_url'] = product_image_tag['src'] if product_image_tag and 'src' in product_image_tag.attrs else None

# Pricing
current_price_tag = soup.select_one('section.pricing span.current-price')
product_info['current_price'] = current_price_tag.string.strip() if current_price_tag else None

original_price_tag = soup.select_one('section.pricing span.original-price')
product_info['original_price'] = original_price_tag.string.strip() if original_price_tag else None

# Description (get all text within the description section)
description_section = soup.find('section', id='description')
if description_section:
    # Find the first <p> tag directly under description_section, or all <p> tags
    # For this example, let's take all text content, stripped
    product_info['description'] = description_section.get_text(separator=" ", strip=True)
else:
    product_info['description'] = None

# Key Features (as a list)
features_list = []
features_section = soup.find('section', class_='features')
if features_section:
    feature_items = features_section.find_all('li')
    for item in feature_items:
        if item.string:
            features_list.append(item.string.strip())
product_info['features'] = features_list if features_list else None

# Review Count
review_count_tag = soup.find('span', id='review-count')
try:
    product_info['review_count'] = int(review_count_tag.string) if review_count_tag and review_count_tag.string else 0
except ValueError:
    product_info['review_count'] = 0


# --- Step 4: Extract Individual Reviews (first few) ---
reviews_data = []
review_item_tags = soup.select('section.reviews div.review-item', limit=5) # Limit to 5 reviews for example

for review_tag in review_item_tags:
    review = {}
    review['review_id'] = review_tag.get('data-review-id')
    
    reviewer_name_tag = review_tag.find('p', class_='reviewer-name')
    review['reviewer_name'] = reviewer_name_tag.string.strip() if reviewer_name_tag and reviewer_name_tag.string else None
    
    rating_tag = review_tag.select_one('p.review-rating span') # Get the span inside p.review-rating
    try:
        review['rating_value'] = int(rating_tag.string) if rating_tag and rating_tag.string else None
    except ValueError:
        review['rating_value'] = None
        
    review_text_tag = review_tag.find('p', class_='review-text')
    review['review_text'] = review_text_tag.string.strip() if review_text_tag and review_text_tag.string else None
    
    reviews_data.append(review)

# --- Step 5: Display or Store Scraped Data ---
# print("--- Product Information ---")
# for key, value in product_info.items():
#     print(f"{key.replace('_', ' ').title()}: {value}")

# print("\n--- Extracted Reviews (First Few) ---")
# for rev in reviews_data:
#     print(rev)

# Optional: Store in a Pandas DataFrame
# product_df = pd.DataFrame([product_info])
# reviews_df = pd.DataFrame(reviews_data)
# print("\n--- Product DataFrame ---")
# print(product_df)
# print("\n--- Reviews DataFrame ---")
# print(reviews_df)
```

**Explanation of Techniques Used:**
-   **`soup.find('tag_name', id='some_id')`**: Finds the first tag with the given name and ID.
-   **`soup.find('tag_name', class_='some_class')`**: Finds the first tag with the given name and CSS class. Note `class_` due to `class` being a Python keyword.
-   **`tag['attribute_name']`**: Accesses the value of an attribute.
-   **`tag.string`**: Gets the text content if the tag has only one string child.
-   **`soup.select('css_selector')`**: Finds all tags matching a CSS selector, returns a list.
-   **`soup.select_one('css_selector')`**: Finds the first tag matching a CSS selector.
-   **`tag.get_text(separator=" ", strip=True)`**: Gets all text from a tag and its children, stripped of whitespace and joined by the separator.
-   **Error Handling (Conceptual):** The `if tag else None` pattern is a simple way to handle cases where an element might not be found. More robust error handling (try-except blocks) would be needed for production scrapers.
-   **Data Cleaning:** The example includes basic `.strip()` for text. Real-world scraping often requires more extensive cleaning (e.g., removing currency symbols, converting types, handling inconsistent formatting).

This example showcases a typical workflow for extracting structured data from an HTML page using Beautiful Soup's searching and data access capabilities. The specific selectors and logic would need to be adapted for different website structures.

---
`````

This completes the Beautiful Soup section. Next, I'll create the remaining detailed notes for Scrapy (Project Structure, Settings, Middleware, and a Practical Example).

---

Okay, let's continue with the detailed notes for Scrapy, focusing on Project Structure, Settings, Middleware, and a Practical Example.

---

### Continuing Scrapy

`````markdown

Filename: 160_Python_Libraries/Scrapy/Scrapy_Project_Structure.md
````markdown
---
tags: [python, scrapy, web_scraping, project_structure, organization, concept]
aliases: [Scrapy Project Layout, Scrapy Directory Structure]
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Spiders]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Item_Pipelines]]"
  - "[[Scrapy_Settings]]"
  - "[[Scrapy_Middleware]]"
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Scrapy: Project Structure

When you start a new Scrapy project using the command `scrapy startproject myprojectname`, Scrapy automatically generates a directory structure with several key files and folders. Understanding this structure is important for organizing your web scraping code.

## Typical Project Layout
After running `scrapy startproject ecommerce_scraper`, you would typically see a structure like this:

```
ecommerce_scraper/  <-- Outer directory (can be renamed)
├── scrapy.cfg      <-- Deploy configuration file
└── ecommerce_scraper/  <-- Inner Python package for your project (project module)
    ├── __init__.py
    ├── items.py    <-- Project items definition file
    ├── middlewares.py <-- Project middlewares file
    ├── pipelines.py   <-- Project pipelines file
    ├── settings.py    <-- Project settings file
    └── spiders/       <-- Directory for your spider modules
        ├── __init__.py
        └── # (e.g., product_spider.py, category_spider.py)
```

[list2tab|#Project Components]
- `scrapy.cfg`
    -   **Location:** Outer project directory.
    -   **Purpose:** This is the project configuration file. It mainly specifies settings for deploying your Scrapy project (e.g., using Scrapyd) and points to the project's settings module.
    -   You typically don't modify this file much for local development and running spiders from the command line.
    -   Example content:
        ```ini
        [settings]
        default = ecommerce_scraper.settings

        [deploy]
        #url = http://localhost:6800/
        project = ecommerce_scraper
        ```
- Inner Project Directory (e.g., `ecommerce_scraper/`)
    -   **Location:** Inside the outer project directory. This is the actual Python package for your Scrapy project.
    -   **Purpose:** Contains all the core code for your spiders, items, pipelines, etc. You'll do most of your work here.
    -   `__init__.py`: Makes this directory a Python package.
    -   **[[Scrapy_Items|`items.py`]]**:
        -   Defines the structure of the data you want to scrape using `scrapy.Item` classes. This acts as a schema for your scraped data.
    -   **[[Scrapy_Middleware|`middlewares.py`]]**:
        -   Defines custom spider middleware and downloader middleware. Middleware are hooks into Scrapy’s request/response processing for advanced customization.
    -   **[[Scrapy_Item_Pipelines|`pipelines.py`]]**:
        -   Defines item pipelines for processing scraped items (e.g., cleaning, validating, storing data in databases or files).
    -   **[[Scrapy_Settings|`settings.py`]]**:
        -   Contains project-specific settings that override Scrapy's default settings. You configure things like concurrency, user-agent, enabled pipelines, middleware, download delays, `robots.txt` obedience, etc., here.
    -   **`spiders/` directory**:
        -   This is where you place your spider modules (Python files containing your [[Scrapy_Spiders|spider classes]]). Each file can contain one or more spiders.
        -   `spiders/__init__.py`: Makes the `spiders` directory a Python package.

## How Scrapy Uses This Structure
-   When you run a Scrapy command like `scrapy crawl myspider` from the outer project directory, Scrapy uses `scrapy.cfg` to locate your project's settings and module.
-   It then loads the settings from `ecommerce_scraper/settings.py`.
-   It discovers spiders defined in Python files within the `ecommerce_scraper/spiders/` directory.
-   If items are yielded by spiders, they are instances of classes defined in `ecommerce_scraper/items.py`.
-   These items are then passed through the item pipelines enabled in `settings.py` and defined in `ecommerce_scraper/pipelines.py`.
-   Middleware defined in `middlewares.py` and enabled in `settings.py` can intercept and modify requests and responses.

## Best Practices
-   **Keep Spiders in `spiders/`:** This is the standard location and helps Scrapy discover them automatically.
-   **Define Data Structure in `items.py`:** Use `scrapy.Item` for clarity and consistency, especially for larger projects.
-   **Modularize Pipelines and Middleware:** Implement distinct processing steps in separate pipeline components or middleware classes.
-   **Configure via `settings.py`:** Avoid hardcoding settings directly in spiders or pipelines where possible. Use `settings.py` for project-wide configurations.
-   **Utilities:** You can create additional Python modules within your project's inner directory (e.g., `ecommerce_scraper/utils.py`) for helper functions or shared code.

Understanding and adhering to this project structure makes your Scrapy projects organized, maintainable, and aligned with the framework's conventions.

---
````

`````markdown

Filename: 160_Python_Libraries/Scrapy/Scrapy_Settings.md
````markdown
---
tags: [python, scrapy, web_scraping, configuration, settings, concept]
aliases: [Scrapy Configuration, settings.py Scrapy]
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Project_Structure]]"
  - "[[Scrapy_Item_Pipelines]]" # Enabled via settings
  - "[[Scrapy_Middleware]]" # Enabled via settings
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Scrapy: Settings (`settings.py`)

The `settings.py` file in a Scrapy project is crucial for configuring the behavior of your web crawlers (spiders) and other Scrapy components. When Scrapy runs, it first loads default settings, then overrides them with the settings defined in your project's `settings.py` file.

This file allows you to customize various aspects of the crawling process without modifying the core Scrapy framework or your spider code directly.

## Location
The `settings.py` file is located within your project's inner Python package directory (e.g., `myproject/myproject/settings.py`).

## Common Settings to Configure

[list2tab|#Scrapy Settings]
- Basic Spider Configuration
    -   **`BOT_NAME`**: (String) The name of the bot implemented by this Scrapy project (also known as the project name). Default: `'myproject'`.
    -   **`SPIDER_MODULES`**: (List of strings) A list of modules where Scrapy will look for spiders. Default: `['myproject.spiders']`.
    -   **`NEWSPIDER_MODULE`**: (String) Module where new spiders are created using `scrapy genspider`. Default: `'myproject.spiders'`.
- Crawl Behavior & Politeness
    -   **`ROBOTSTXT_OBEY`**: (Boolean) If `True` (default), Scrapy will respect `robots.txt` rules of websites. It's good practice to keep this `True`.
    -   **`USER_AGENT`**: (String) The default User-Agent string to use for requests, unless overridden per spider or request. Default is `Scrapy/VERSION (+http://scrapy.org)`. It's often recommended to set this to a common browser user-agent or a custom one identifying your bot respectfully.
        ```python
        # USER_AGENT = 'MyECommerceScraper (+http://www.mywebsite.com/botinfo)'
        ```
    -   **`CONCURRENT_REQUESTS`**: (Integer) The maximum number of concurrent (i.e. simultaneous) requests that will be performed by the Scrapy downloader. Default: 16.
    -   **`DOWNLOAD_DELAY`**: (Float) The amount of time (in seconds) that the downloader should wait before downloading consecutive pages from the same website. Helps to avoid overloading servers. Default: 0.
        ```python
        # DOWNLOAD_DELAY = 1 # Wait 1 second between requests to the same domain
        ```
    -   **`CONCURRENT_REQUESTS_PER_DOMAIN`**: (Integer) Maximum number of concurrent requests that will be performed to any single domain. Default: 8.
    -   **`CONCURRENT_REQUESTS_PER_IP`**: (Integer) Maximum number of concurrent requests that will be performed to any single IP. If non-zero, `CONCURRENT_REQUESTS_PER_DOMAIN` is ignored. Default: 0.
    -   **`AUTOTHROTTLE_ENABLED`**: (Boolean) Enables the AutoThrottle extension, which dynamically adjusts download delays based on server load. Default: `False`.
    -   **`AUTOTHROTTLE_START_DELAY`**: (Float) Initial download delay for AutoThrottle. Default: 5.0.
    -   **`AUTOTHROTTLE_MAX_DELAY`**: (Float) Maximum download delay for AutoThrottle. Default: 60.0.
    -   **`AUTOTHROTTLE_TARGET_CONCURRENCY`**: (Float) Average number of parallel requests Scrapy should try to maintain to each remote server. Default: 1.0.
- Item Pipelines (`ITEM_PIPELINES`)
    -   A dictionary specifying the [[Scrapy_Item_Pipelines|item pipelines]] to use and their order of execution (lower integer means earlier execution).
    -   Keys are pipeline class paths, values are integers from 0 to 1000.
        ```python
        # ITEM_PIPELINES = {
        #    'myproject.pipelines.PriceCleanerPipeline': 300,
        #    'myproject.pipelines.DatabaseStoragePipeline': 800,
        # }
        ```
- Middleware (`DOWNLOADER_MIDDLEWARES`, `SPIDER_MIDDLEWARES`)
    -   Dictionaries to enable and order [[Scrapy_Middleware|downloader and spider middleware]].
    -   Keys are middleware class paths, values are integers for order.
        ```python
        # DOWNLOADER_MIDDLEWARES = {
        #    'myproject.middlewares.CustomUserAgentMiddleware': 543,
        #    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750, # Example
        # }
        ```
- Extensions (`EXTENSIONS`)
    -   A dictionary to enable and order Scrapy extensions.
- Request Headers (`DEFAULT_REQUEST_HEADERS`)
    -   A dictionary containing default headers to be sent with each request.
        ```python
        # DEFAULT_REQUEST_HEADERS = {
        #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #   'Accept-Language': 'en-US,en;q=0.5',
        # }
        ```
- Cookies (`COOKIES_ENABLED`, `COOKIES_DEBUG`)
    -   `COOKIES_ENABLED`: (Boolean) Whether cookies are enabled. Default: `True`.
    -   `COOKIES_DEBUG`: (Boolean) Log cookies sent in requests and received in responses. Default: `False`.
- Feed Exports (for `-o` command line option)
    -   **`FEEDS`**: A dictionary to configure feed exports (e.g., output format, path, encoding) if you want more control than the command line provides or want to export multiple feeds.
    -   **`FEED_EXPORT_ENCODING`**: Default encoding for feeds. Default: `'utf-8'`.
    -   **`FEED_EXPORT_FIELDS`**: A list of fields to include in the export, and their order.
- Logging (`LOG_LEVEL`, `LOG_FILE`)
    -   `LOG_LEVEL`: Minimum level of messages to log (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'). Default: 'DEBUG'.
    -   `LOG_FILE`: Path to a file where logs will be written. If None, logs go to standard error.
- Caching (`HTTPCACHE_ENABLED`, etc.)
    -   Scrapy has a built-in HTTP caching middleware that can be enabled to speed up development by caching responses.
    -   `HTTPCACHE_ENABLED = True`
    -   `HTTPCACHE_EXPIRATION_SECS = 0` (0 means cache forever, good for dev)
    -   `HTTPCACHE_DIR = 'httpcache'`
    -   `HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'`

## Overriding Settings
-   **Project Settings (`settings.py`):** The primary place.
-   **Command-Line Options:** Many settings can be overridden using `scrapy crawl myspider -s SETTING_NAME=value`.
-   **Spider-Specific Settings (`custom_settings` attribute):** A spider class can define a `custom_settings` dictionary to override project or default settings specifically for that spider.
    ```python
    # In your spider class:
    # class MySpecialSpider(scrapy.Spider):
    #     name = "special_spider"
    #     custom_settings = {
    #         'DOWNLOAD_DELAY': 0.25,
    #         'USER_AGENT': 'SpecialBot/1.0'
    #     }
    #     # ... rest of spider ...
    ```

Properly configuring `settings.py` is essential for controlling the behavior, politeness, and data processing workflow of your Scrapy spiders. It's recommended to review the default Scrapy settings and adjust them according to the needs of your project and the websites you are crawling.

---
````

`````markdown

Filename: 160_Python_Libraries/Scrapy/Scrapy_Middleware.md
````markdown
---
tags: [python, scrapy, web_scraping, middleware, downloader_middleware, spider_middleware, customization, concept, example]
aliases: [Scrapy Middlewares, Downloader Middleware, Spider Middleware]
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Settings]]" # Middlewares are enabled and ordered in settings
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Scrapy: Middleware (Downloader and Spider Middleware)

Scrapy Middleware are hooks into Scrapy’s request/response processing framework. They provide a way to plug custom code to modify how Scrapy handles requests and responses globally across your project or for specific spiders.

There are two main types of middleware:
1.  **Downloader Middleware:** Sits between the Scrapy Engine and the Downloader. It processes requests just before they are sent to the website and responses just after they are received from the website.
2.  **Spider Middleware:** Sits between the Scrapy Engine and the Spiders. It processes spider output (requests and items) and can modify initial requests sent from the spider.

## 1. Downloader Middleware
Downloader middleware components are processed sequentially for each request and response.

**Key Methods to Implement in a Downloader Middleware Class:**
-   **`process_request(self, request, spider)`:**
    -   Called for each request that passes through the downloader middleware.
    -   Must either:
        -   Return `None`: Scrapy continues processing this request, executing other middleware’s `process_request` and then the downloader.
        -   Return a `Response` object: Scrapy won’t call any other `process_request` or the downloader; it returns this response directly. Other middleware's `process_response` will be called.
        -   Return a `Request` object: Scrapy stops `process_request` chain and reschedules the returned request.
        -   Raise `IgnoreRequest`: The request is ignored, and other middleware's `process_exception` is called.
    -   **Use Cases:** Modifying request headers (e.g., User-Agent, cookies), adding proxies, handling HTTP authentication, filtering out requests to certain domains.
-   **`process_response(self, request, response, spider)`:**
    -   Called with the response returned from the Downloader (or another `process_request` that returned a Response).
    -   Must either:
        -   Return a `Response` object: Passed to the next middleware's `process_response` or to the spider.
        -   Return a `Request` object: Stops `process_response` chain, original request is rescheduled. The new request goes through `process_request` again.
        -   Raise `IgnoreRequest`: The spider's `errback` for the original request is called.
    -   **Use Cases:** Modifying response content (e.g., decompressing, decoding), handling specific HTTP status codes (e.g., retrying on 503), scraping data that is common to all pages.
-   **`process_exception(self, request, exception, spider)`:**
    -   Called when the downloader or a `process_request` method from a previous middleware raises an exception (including `IgnoreRequest`).
    -   Must either:
        -   Return `None`: Scrapy continues processing the exception with subsequent middleware.
        -   Return a `Response` object: Stops exception processing, starts `process_response` chain.
        -   Return a `Request` object: Stops exception processing, reschedules the new request.
    -   **Use Cases:** Custom retry logic, logging specific errors.

**Example: Custom User-Agent Downloader Middleware**
```python
# myproject/middlewares.py
import random

class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # You can get settings from crawler.settings
        user_agents_list = crawler.settings.getlist('MY_USER_AGENTS', [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...', # A default if not set
            'Another User Agent String...'
        ])
        return cls(user_agents_list)

    def process_request(self, request, spider):
        # Randomly select a User-Agent for the request
        user_agent = random.choice(self.user_agents)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
            spider.logger.debug(f"Using User-Agent: {user_agent} for {request.url}")
        return None # Continue processing

# To enable in settings.py:
# DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.RandomUserAgentMiddleware': 543, # Order matters
# }
# MY_USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Chrome/90...",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 ... Safari/15...",
#     # ... more user agents ...
# ]
```

## 2. Spider Middleware
Spider middleware components are processed for requests sent from the spider and for items/requests yielded by the spider.

**Key Methods to Implement in a Spider Middleware Class:**
-   **`process_spider_input(self, response, spider)`:**
    -   Called for each response that passes through the spider middleware and is processed by the spider.
    -   Should return `None` or raise an exception.
    -   **Use Cases:** Logging, modifying response before spider sees it (rare).
-   **`process_spider_output(self, response, result, spider)`:**
    -   Called with the results (requests or items) returned by the Spider, after it has processed the response.
    -   Must return an iterable of `Request` objects, dictionaries, or `Item` objects.
    -   **Use Cases:** Filtering items, modifying items (e.g., adding a timestamp), generating new requests based on item content.
-   **`process_spider_exception(self, response, exception, spider)`:**
    -   Called when a spider or `process_spider_input()` method (from a previous spider middleware) raises an exception.
    -   Should return either `None` (to continue processing the exception with subsequent middleware) or an iterable of `Request`, `dict` or `Item` objects.
-   **`process_start_requests(self, start_requests, spider)`:**
    -   Called with the start requests of the spider. Works like `process_spider_output` but for initial requests.
    -   Must return an iterable of `Request` objects.
    -   **Use Cases:** Modifying the initial set of requests (e.g., filtering URLs, adding cookies).

**Example: Spider Middleware to Add a Timestamp to Items**
```python
# myproject/middlewares.py
import datetime

class AddTimestampSpiderMiddleware:
    def process_spider_output(self, response, result, spider):
        for i in result: # result is an iterable of Requests or Items
            if isinstance(i, scrapy.Item) or isinstance(i, dict): # Check if it's an item-like object
                # Assuming your item has a 'scraped_at' field
                i['scraped_at_timestamp'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            yield i # Must yield all results (requests or items)

# To enable in settings.py:
# SPIDER_MIDDLEWARES = {
#    'myproject.middlewares.AddTimestampSpiderMiddleware': 543,
# }
```

## Enabling Middleware
Middleware are enabled and ordered in the `settings.py` file using the `DOWNLOADER_MIDDLEWARES` and `SPIDER_MIDDLEWARES` dictionaries. The integer values determine the order of execution (lower values are processed closer to the Engine for requests, and closer to the Downloader/Spider for responses).

Scrapy comes with several built-in middleware (e.g., for handling cookies, HTTP compression, retries, `robots.txt`). Custom middleware are merged with these based on their order.

Middleware provide a powerful mechanism to extend and customize Scrapy's functionality at various points in the crawling process.

---
````

`````markdown

Filename: 160_Python_Libraries/Scrapy/Scrapy_Practical_Crawling_Example.md
````markdown
---
tags: [python, scrapy, web_scraping, web_crawling, spider, items, pipelines, example, practical_use_case]
aliases: [Scrapy Crawling Example, E-commerce Scraping Scrapy]
related:
  - "[[160_Python_Libraries/Scrapy/_Scrapy_MOC|_Scrapy_MOC]]"
  - "[[Scrapy_Project_Structure]]"
  - "[[Scrapy_Spiders]]"
  - "[[Scrapy_Items]]"
  - "[[Scrapy_Selectors]]"
  - "[[Scrapy_Item_Pipelines]]"
  - "[[Scrapy_Settings]]"
worksheet: [WS_WebScraping_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Scrapy: Practical Crawling Example (Conceptual E-commerce Site)

This note outlines a more complete, albeit conceptual, example of a Scrapy project designed to scrape product information from a mock e-commerce website. It will touch upon defining items, creating a spider to crawl category and product pages, extracting data, and a simple item pipeline.

**Target Scenario:** Scrape product name, price, description, and image URL from an e-commerce site that has category pages linking to individual product pages.

## 1. Project Setup
First, create a Scrapy project (if not already done):
```bash
scrapy startproject ecom_scraper
cd ecom_scraper
```

## 2. Define Items (`ecom_scraper/items.py`)
Define the structure for the product data we want to extract.

```python
# ecom_scraper/items.py
import scrapy

class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()
    product_url = scrapy.Field() # URL of the product page
    category = scrapy.Field()    # Category it belongs to
```

## 3. Create the Spider (`ecom_scraper/spiders/product_spider.py`)
This spider will start from a main category page, find links to individual product pages, follow them, and then scrape data from each product page.

```python
# ecom_scraper/spiders/product_spider.py
import scrapy
from ..items import ProductItem # Import ProductItem from items.py

class EcomProductSpider(scrapy.Spider):
    name = "ecom_products"
    allowed_domains = ["conceptual-ecommerce.com"] # Restrict to this domain
    
    # Start with a few category pages
    start_urls = [
        "http://conceptual-ecommerce.com/category/electronics",
        "http://conceptual-ecommerce.com/category/books",
    ]

    # Callback for processing category pages
    def parse_category(self, response):
        self.logger.info(f"Crawling category page: {response.url}")
        
        # Extract current category name (example: from a breadcrumb or title)
        # current_category = response.xpath('//h1[@class="category-title"]/text()').get()
        # For simplicity, let's derive from URL or pass via meta
        current_category = response.url.split("/")[-1] if response.url.split("/")[-1] else "Unknown"


        # Selector for links to individual product pages
        # This will depend heavily on the actual website structure
        # product_links = response.css('div.product-listing-item a.product-page-link::attr(href)').getall()
        
        # Conceptual: Assume product links are found
        # In a real scenario, replace these with actual selectors
        if "electronics" in response.url:
            product_links = ["/product/item101", "/product/item102"]
        elif "books" in response.url:
            product_links = ["/product/book201", "/product/book202"]
        else:
            product_links = []

        for product_link_relative in product_links:
            product_url_absolute = response.urljoin(product_link_relative)
            # Yield a request to follow the product link, passing category via meta
            yield scrapy.Request(
                url=product_url_absolute,
                callback=self.parse_product_page,
                meta={'category': current_category} # Pass category to next callback
            )

        # Conceptual: Follow pagination links on category page (if any)
        # next_page_selector = 'a.pagination-next::attr(href)'
        # next_page_relative = response.css(next_page_selector).get()
        # if next_page_relative:
        #     next_page_absolute = response.urljoin(next_page_relative)
        #     yield scrapy.Request(url=next_page_absolute, callback=self.parse_category)

    # Callback for processing individual product pages
    def parse_product_page(self, response):
        self.logger.info(f"Scraping product page: {response.url}")
        
        # Retrieve category from meta
        category = response.meta.get('category', 'N/A')

        # Create an Item instance
        product = ProductItem()
        product['product_url'] = response.url
        product['category'] = category
        
        # Extract data using selectors (these are placeholders)
        # Replace with actual selectors for the target website
        # product['product_name'] = response.xpath('//h1[@itemprop="name"]/text()').get()
        # product['price'] = response.xpath('//span[@itemprop="price"]/text()').get()
        # description_lines = response.css('div.product-description ::text').getall()
        # product['description'] = " ".join([line.strip() for line in description_lines if line.strip()])
        # product['image_url'] = response.urljoin(response.css('img.main-product-image::attr(src)').get())

        # Conceptual data extraction for this example
        product['product_name'] = response.css('title::text').get().split('-').strip() if response.css('title::text').get() else "Sample " + category + " Product"
        product['price'] = f"${np.random.randint(10,500)}.99" # Random price
        product['description'] = f"A high-quality {product['product_name']} from the {category} section."
        product['image_url'] = response.urljoin(f"/images/{response.url.split('/')[-1]}.jpg")
        
        yield product

    # Default parse method if start_urls don't have specific callbacks
    # For this spider, we want parse_category to handle start_urls
    def parse(self, response):
        # Delegate to parse_category for start_urls
        return self.parse_category(response)

# For the conceptual part to run without actual web requests,
# you would need a mock server or local HTML files.
# For this example, we assume the selectors will find something if the HTML structure matches.
import numpy as np # For random price generation in conceptual example
```

## 4. Define an Item Pipeline (`ecom_scraper/pipelines.py`)
A simple pipeline to clean data and print it (or save to JSON).

```python
# ecom_scraper/pipelines.py
import json
from itemadapter import ItemAdapter # For working with Items or dicts

class PriceCleanerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            price_str = str(adapter['price']).replace('$', '').replace(',', '').strip()
            try:
                adapter['price'] = float(price_str)
            except ValueError:
                spider.logger.warning(f"Could not convert price to float: {adapter['price']} for {adapter.get('product_url')}")
                # adapter['price'] = None # Or handle as invalid
        return item

class SimpleJsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open(f'{spider.name}_output.jl', 'w') # JSON Lines format

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        spider.logger.info(f"Saved item: {item.get('product_name')}")
        return item
```

## 5. Configure Settings (`ecom_scraper/settings.py`)
Enable the pipelines and set a polite User-Agent and download delay.

```python
# ecom_scraper/settings.py

BOT_NAME = 'ecom_scraper'

SPIDER_MODULES = ['ecom_scraper.spiders']
NEWSPIDER_MODULE = 'ecom_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1 # 1 second delay
# CONCURRENT_REQUESTS_PER_DOMAIN = 8

USER_AGENT = 'ECommerceProductScraper/1.0 (+http://www.example.com/botinfo)'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ecom_scraper.pipelines.PriceCleanerPipeline': 300,
   'ecom_scraper.pipelines.SimpleJsonWriterPipeline': 800,
}

# Optional: Configure HTTP Caching for development
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0 # Cache forever during dev
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
```

## 6. Running the Spider
Navigate to the outer `ecom_scraper` directory in your terminal:
```bash
scrapy crawl ecom_products
```
This command will:
1.  Look for a spider named "ecom_products".
2.  Start making requests from `start_urls`.
3.  Call `parse_category` for category page responses.
4.  Yield `Request` objects for product pages, which will then be processed by `parse_product_page`.
5.  Yield `ProductItem` objects from `parse_product_page`.
6.  Pass these items through the `PriceCleanerPipeline` and then `SimpleJsonWriterPipeline`.
7.  A file named `ecom_products_output.jl` will be created containing the scraped data in JSON Lines format.

**Important Notes for Real-World Scenario:**
-   **Website Structure:** The CSS/XPath selectors (`response.css(...)`, `response.xpath(...)`) are highly dependent on the target website's HTML structure and will need to be carefully identified using browser developer tools. The selectors in this example are placeholders.
-   **Politeness:** Always respect `robots.txt` (`ROBOTSTXT_OBEY = True`). Set appropriate `DOWNLOAD_DELAY` and `CONCURRENT_REQUESTS_PER_DOMAIN` to avoid overloading the server. Identify your bot with a clear `USER_AGENT`.
-   **Error Handling:** Real spiders need robust error handling (e.g., for missing elements, network issues, changes in website structure).
-   **Dynamic Content:** If the website loads data using JavaScript, Scrapy alone might not be enough. You might need to use tools like Selenium, Playwright, or Scrapy Splash to render JavaScript.
-   **Legality and Ethics:** Always ensure you have permission to scrape a website and comply with its terms of service.

This example provides a foundational structure for a multi-page scraping project using Scrapy.

---
`````

This completes the detailed notes for Scrapy and Beautiful Soup. We've covered their MOCs and key components with examples.

Next, I will proceed with the **Data Visualization libraries**, starting with the remaining **Seaborn** notes, then **Plotly**, **Bokeh**, and **Altair** as per our plan.

---

