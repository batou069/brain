---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - model_building
  - sequential_api
  - functional_api
  - concept
  - example
aliases:
  - tf.keras Sequential API
  - tf.keras Functional API
  - Keras Model Types
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Layers]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Sequential vs. Functional API for Model Building

`tf.keras` provides two main ways to define neural network architectures: the **Sequential API** and the **Functional API**. A third way, **Model Subclassing**, offers maximum flexibility for research and complex models.

## 1. Sequential API (`tf.keras.Sequential`)
-   **Concept:** The simplest way to build a Keras model. It allows you to create models layer-by-layer in a linear stack.
-   **Use Cases:** Suitable for simple architectures where layers are stacked one after another, with a single input and a single output.
-   **How to Use:**
    1.  Create an instance of `tf.keras.Sequential()`.
    2.  Add [[Keras_Layers|layers]] to it, typically via a list in the constructor or using the `.add()` method.
-   **Limitations:** Not suitable for models with:
    -   Multiple inputs or multiple outputs.
    -   Shared layers.
    -   Non-linear topology (e.g., residual connections, branches).

**Example: Simple Image Classifier for E-commerce Product Images**
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Define input shape (e.g., 64x64 RGB product images)
input_shape = (64, 64, 3)
num_product_categories = 10 # e.g., electronics, books, apparel, etc.

model_sequential = keras.Sequential(
    [
        # Input Layer (implicitly defined by input_shape in first Conv2D layer)
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, name="conv1"),
        layers.MaxPooling2D((2, 2), name="pool1"),
        layers.Conv2D(64, (3, 3), activation='relu', name="conv2"),
        layers.MaxPooling2D((2, 2), name="pool2"),
        layers.Flatten(name="flatten"),
        layers.Dense(64, activation='relu', name="dense1"),
        layers.Dropout(0.5, name="dropout1"),
        layers.Dense(num_product_categories, activation='softmax', name="output_softmax") # Output layer
    ],
    name="product_image_classifier_sequential"
)

# Print model summary
model_sequential.summary()

# Conceptual data for demonstration of compilation and fitting
# (X_train_images, y_train_labels), (X_test_images, y_test_labels) = ... load and preprocess image data ...
# For this example, let's create dummy data
num_samples = 100
X_train_dummy = np.random.rand(num_samples, 64, 64, 3).astype(np.float32)
y_train_dummy = np.random.randint(0, num_product_categories, num_samples)

# Compile the model
model_sequential.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy(name="accuracy")]
)

# Train the model (conceptual - on dummy data)
# print("\nTraining Sequential Model (Conceptual)...")
# history_sequential = model_sequential.fit(
#     X_train_dummy, y_train_dummy,
#     epochs=2, # Few epochs for quick demo
#     batch_size=32,
#     verbose=1
# )
# print("Sequential Model Training Finished.")
```

## 2. Functional API
-   **Concept:** Allows for building more complex model architectures, such as directed acyclic graphs (DAGs) of layers. Models are defined by creating layers and connecting them explicitly by calling them on tensors.
-   **Use Cases:**
    -   Multi-input models.
    -   Multi-output models.
    -   Models with shared layers (using the same layer instance multiple times).
    -   Models with non-linear topology (e.g., residual connections in ResNets, inception blocks).
-   **How to Use:**
    1.  Define an input layer(s) using `keras.Input()`.
    2.  Create layer instances and call them on tensors (output of previous layer or input tensor) to connect them: `output_tensor = my_layer(input_tensor)`.
    3.  Create a `keras.Model()` instance, specifying its inputs and outputs.

**Example: Multi-input model for predicting product purchase likelihood**
Imagine predicting purchase likelihood based on product image features and textual review features.

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Define input shapes
image_input_shape = (64, 64, 3) # For image features (e.g., output of a CNN base)
text_input_shape = (100,)      # For text features (e.g., TF-IDF or embedding sequence length)
num_classes_purchase = 1       # Binary: purchase (1) or not (0)

# 1. Define Input layers
image_input = keras.Input(shape=image_input_shape, name="image_features_input")
text_input = keras.Input(shape=text_input_shape, name="text_features_input")

# 2. Define branches for each input type
# Image processing branch (conceptual - could be more complex)
x1 = layers.Flatten(name="flatten_image")(image_input)
x1 = layers.Dense(64, activation='relu', name="dense_image_1")(x1)
x1 = layers.Dropout(0.3, name="dropout_image")(x1)
image_features_processed = layers.Dense(32, activation='relu', name="dense_image_2")(x1)

# Text processing branch (conceptual - could be an LSTM or Dense layer on embeddings)
x2 = layers.Dense(64, activation='relu', name="dense_text_1")(text_input) # Assuming text_input is already vectorized
x2 = layers.Dropout(0.3, name="dropout_text")(x2)
text_features_processed = layers.Dense(32, activation='relu', name="dense_text_2")(x2)

# 3. Concatenate the processed features from both branches
concatenated_features = layers.concatenate([image_features_processed, text_features_processed], name="concatenate_branches")

# 4. Add a common classification head
x_combined = layers.Dense(32, activation='relu', name="dense_combined")(concatenated_features)
output_purchase = layers.Dense(num_classes_purchase, activation='sigmoid', name="output_sigmoid")(x_combined) # Sigmoid for binary

# 5. Create the Model
model_functional = keras.Model(
    inputs=[image_input, text_input], # List of input tensors
    outputs=output_purchase,          # Output tensor
    name="multi_input_purchase_predictor"
)

# Print model summary
model_functional.summary()

# Conceptual data for demonstration
num_samples = 100
X_train_image_dummy = np.random.rand(num_samples, 64, 64, 3).astype(np.float32)
X_train_text_dummy = np.random.rand(num_samples, 100).astype(np.float32)
y_train_purchase_dummy = np.random.randint(0, 2, num_samples)

# Compile the model
model_functional.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=['accuracy']
)

# Train the model (conceptual - on dummy data)
# print("\nTraining Functional Model (Conceptual)...")
# history_functional = model_functional.fit(
#     [X_train_image_dummy, X_train_text_dummy], # Pass inputs as a list
#     y_train_purchase_dummy,
#     epochs=2,
#     batch_size=32,
#     verbose=1
# )
# print("Functional Model Training Finished.")
```

## 3. Model Subclassing (`class MyModel(keras.Model): ...`)
-   **Concept:** For maximum flexibility, you can create a custom model by subclassing `tf.keras.Model` and implementing the `call(self, inputs, training=None, mask=None)` method to define the forward pass. Layers are typically defined in the `__init__` method.
-   **Use Cases:** Research, models with complex control flow, or when the static graph nature of Sequential/Functional API is too restrictive.
-   **Trade-off:** More verbose and can be harder to debug or serialize compared to the Functional API.

## Choosing an API
-   **Sequential API:** Best for simple, linear stacks of layers. Quick and easy.
-   **Functional API:** The most versatile and widely used for building arbitrary DAGs of layers. Recommended for most non-trivial models. Allows for easy model inspection and plotting (`keras.utils.plot_model`).
-   **Model Subclassing:** Use when you need full programmatic control over the forward pass logic, often for research or highly custom architectures.

All three methods produce standard `tf.keras.Model` objects that can be compiled, trained, evaluated, and saved using the same Keras workflows.

---