---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - model_persistence
  - saving_models
  - loading_models
  - savedmodel
  - hdf5
  - concept
  - example
aliases:
  - Saving Keras Models
  - Loading Keras Models
  - TensorFlow Model Persistence
  - tf.saved_model
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Callbacks|ModelCheckpoint Callback]]"
  - "[[TensorFlow_Lite_TFLite]]"
  - "[[TensorFlow_Serving]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
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