---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - deep_learning
  - neural_networks
  - api
  - concept
  - model_building
  - example
aliases:
  - tf.keras
  - TensorFlow Keras API
  - Keras in TF
  - High-Level API TensorFlow
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[Keras_Library]]"
  - "[[Keras_Sequential_Functional_API]]"
  - "[[Keras_Layers]]"
  - "[[Keras_Optimizers]]"
  - "[[Keras_Loss_Functions]]"
  - "[[Keras_Metrics]]"
  - "[[TensorFlow_Saving_Loading_Models]]"
  - "[[Deep_Learning_Overview]]"
worksheet:
  - WS_DeepLearning_1
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Keras API in TensorFlow (`tf.keras`)

## Overview
**Keras** is a high-level API for building and training deep learning models. It focuses on user-friendliness, modularity, and ease of extensibility. Originally a standalone library that could run on multiple backends (TensorFlow, Theano, CNTK), Keras is now **fully integrated into TensorFlow as `tf.keras`** and is the official recommended high-level API for TensorFlow.

Using `tf.keras` makes it significantly easier to define, train, and evaluate neural networks compared to using lower-level TensorFlow operations directly for model building.

## Key Advantages of `tf.keras`
-   **User-Friendly:** Designed for rapid prototyping and ease of use. Complex models can often be built with relatively few lines of code.
-   **Modularity:** Models are built by connecting composable building blocks (layers, optimizers, loss functions, metrics).
-   **Extensibility:** Easy to create custom layers, loss functions, metrics, and other components.
-   **Full TensorFlow Integration:** Seamlessly integrates with other TensorFlow features like `tf.data` for input pipelines, `tf.distribute` for distributed training, Eager Execution, and `tf.function` for performance optimization.
-   **Wide Adoption:** Large community and abundant learning resources.

## Core Components of `tf.keras`

[list2tab|#tf.keras Components]
- Models (`tf.keras.Model`)
    -   The main container for layers that defines the network architecture.
    -   Two primary ways to create models:
        -   **[[Keras_Sequential_Functional_API|Sequential API (`tf.keras.Sequential`)]]:** For simple, linear stacks of layers. Easiest to get started with.
        -   **[[Keras_Sequential_Functional_API|Functional API]]:** For more complex architectures, such as models with multiple inputs/outputs, shared layers, or non-linear topology (directed acyclic graphs of layers). More flexible.
    -   **Subclassing `tf.keras.Model`:** For highly customized models where full control over the forward pass is needed.
- Layers (`tf.keras.layers`)
    -   The building blocks of neural networks. Each layer performs a specific transformation on its input [[TensorFlow_Tensors|tensors]] and has trainable parameters ([[TensorFlow_Variables|weights and biases]]).
    -   Common layers include:
        -   `Dense`: Fully connected layer.
        -   `Conv1D`, `Conv2D`, `Conv3D`: Convolutional layers for 1D, 2D, 3D data.
        -   `MaxPooling1D`, `MaxPooling2D`, `AveragePooling2D`: Pooling layers.
        -   `LSTM`, `GRU`, `SimpleRNN`: Recurrent layers for sequence data.
        -   `Embedding`: For representing categorical data (e.g., words) as dense vectors.
        -   `BatchNormalization`: Normalizes activations.
        -   `Dropout`: Regularization technique.
        -   `Flatten`, `Reshape`: Layer manipulation.
        -   Activation layers (`ReLU`, `Softmax`, `Sigmoid`, etc., often available as arguments within other layers too).
    -   See [[Keras_Layers]].
- Compilation (`model.compile()`)
    -   Configures the model for training.
    -   Specifies:
        -   **[[Keras_Optimizers|Optimizer (`tf.keras.optimizers`)]]:** Algorithm to update model weights (e.g., `Adam`, `SGD`, `RMSprop`).
        -   **[[Keras_Loss_Functions|Loss Function (`tf.keras.losses`)]]:** Function to measure how well the model performs on the training data (e.g., `BinaryCrossentropy`, `CategoricalCrossentropy`, `MeanSquaredError`).
        -   **[[Keras_Metrics|Metrics (`tf.keras.metrics`)]]:** Functions used to monitor training and testing steps (e.g., `Accuracy`, `Precision`, `MeanAbsoluteError`).
- Training (`model.fit()`)
    -   Trains the model on the provided training data.
    -   Key arguments: training data (`x`, `y`), `batch_size`, `epochs`, `validation_data`, [[Keras_Callbacks|`callbacks`]].
- Evaluation (`model.evaluate()`)
    -   Evaluates the trained model's performance on a separate test dataset using the specified loss and metrics.
- Prediction (`model.predict()`)
    -   Generates predictions for new, unseen input data.
- Saving and Loading Models
    -   `model.save()` and `tf.keras.models.load_model()` allow for saving the entire model (architecture, weights, optimizer state) or just weights.
    -   See [[TensorFlow_Saving_Loading_Models]].
- Callbacks (`tf.keras.callbacks`)
    -   Utilities that can be applied at different stages of the training process (e.g., at the start/end of an epoch, before/after a batch).
    -   Examples: `ModelCheckpoint` (save model periodically), `EarlyStopping` (stop training if performance plateaus), `TensorBoard` (log metrics for visualization). See [[Keras_Callbacks]].

## Typical Workflow with `tf.keras`

1.  **Prepare Data:** Load and preprocess data, often using `tf.data` or converting NumPy/Pandas data to [[TensorFlow_Tensors|TensorFlow tensors]].
    ```python
    # (Conceptual data loading and splitting)
    # (X_train, y_train), (X_test, y_test) = ...
    ```
2.  **Define Model Architecture:** Using Sequential API, Functional API, or model subclassing.
    ```python
    import tensorflow as tf

    # Example: Simple Sequential model for image classification (e.g., product images)
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)), # Assuming 128x128 RGB images
    #     tf.keras.layers.MaxPooling2D((2,2)),
    #     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    #     tf.keras.layers.MaxPooling2D((2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(64, activation='relu'),
    #     tf.keras.layers.Dense(10, activation='softmax') # Assuming 10 product categories
    # ])
    ```
3.  **Compile Model:** Specify optimizer, loss, and metrics.
    ```python
    # model.compile(optimizer='adam',
    #               loss='sparse_categorical_crossentropy', # If y_train are integer labels
    #               metrics=['accuracy'])
    ```
4.  **Train Model (Fit):**
    ```python
    # history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
    # # validation_split splits a portion of training data for validation during training
    ```
5.  **Evaluate Model:**
    ```python
    # test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    # print(f'\nTest accuracy: {test_acc:.4f}')
    ```
6.  **Make Predictions:**
    ```python
    # predictions = model.predict(X_test_sample) # X_test_sample is a batch of new images
    ```
7.  **Save/Load Model (Optional):**
    ```python
    # model.save('my_product_classifier.keras')
    # loaded_model = tf.keras.models.load_model('my_product_classifier.keras')
    ```

`tf.keras` provides a high-level, user-friendly API that significantly simplifies the process of building and training deep learning models within the TensorFlow ecosystem, while still allowing access to TensorFlow's powerful backend capabilities.

---

# Keras API in TensorFlow (`tf.keras`)

## Overview
**Keras** is a high-level Application Programming Interface (API) for building and training deep learning models. It emphasizes user-friendliness, modularity, and ease of extensibility. Originally a standalone library capable of running on multiple backends (like TensorFlow, Theano, or CNTK), Keras is now **fully integrated into TensorFlow as its official high-level API, accessible via `tf.keras`**.

Using `tf.keras` is the recommended way to build most neural network models in TensorFlow. It simplifies many aspects of model definition, training, evaluation, and deployment.

## Why `tf.keras`?
-   **User Experience:** Designed to be intuitive and easy to learn, allowing for rapid prototyping and experimentation.
-   **Modularity:** Models are built by connecting composable building blocks:
    -   [[Keras_Layers|Layers]]: The fundamental units of a neural network.
    -   [[Keras_Optimizers|Optimizers]]: Algorithms to update model weights.
    -   [[Keras_Loss_Functions|Loss Functions]]: Quantify model error.
    -   [[Keras_Metrics|Metrics]]: Measure model performance.
-   **Full TensorFlow Integration:**
    -   Seamlessly uses TensorFlow's backend capabilities (e.g., [[TensorFlow_Tensors|Tensors]], [[TensorFlow_Automatic_Differentiation|automatic differentiation]] with `tf.GradientTape`, GPU/TPU acceleration).
    -   Integrates with [[TensorFlow_Data_Pipeline_tf_data|`tf.data`]] for efficient input pipelines.
    -   Models can be easily saved and loaded using TensorFlow's [[TensorFlow_Saving_Loading_Models|SavedModel format]].
    -   Works with [[TensorBoard_TensorFlow|TensorBoard]] for visualization.
-   **Flexibility:** Supports different ways of defining models to accommodate varying complexity:
    -   [[Keras_Sequential_Functional_API|Sequential API]]: For simple, linear stacks of layers.
    -   [[Keras_Sequential_Functional_API|Functional API]]: For directed acyclic graphs (DAGs) of layers, allowing for more complex architectures (e.g., multi-input/multi-output models, shared layers).
    -   **Model Subclassing:** For maximum flexibility, where users define the forward pass explicitly by subclassing `tf.keras.Model`.

## Core Components of `tf.keras`

1.  **Models (`tf.keras.Model` or `tf.keras.Sequential`)**
    -   The main container that groups layers into an object with training and inference features.
    -   See [[Keras_Sequential_Functional_API]].

2.  **Layers (`tf.keras.layers`)**
    -   Building blocks of a neural network, performing specific transformations on input data and maintaining trainable weights.
    -   Examples: `Dense`, `Conv2D`, `LSTM`, `Embedding`, `BatchNormalization`, `Dropout`.
    -   See [[Keras_Layers]].

3.  **Compilation (`model.compile()`)**
    -   Configures the learning process for the model before training.
    -   Requires specifying:
        -   **Optimizer:** e.g., `tf.keras.optimizers.Adam()`, `'sgd'`. See [[Keras_Optimizers]].
        -   **Loss Function:** e.g., `tf.keras.losses.BinaryCrossentropy()`, `'categorical_crossentropy'`, `'mean_squared_error'`. See [[Keras_Loss_Functions]].
        -   **Metrics:** e.g., `['accuracy']`, `[tf.keras.metrics.Precision()]`. See [[Keras_Metrics]].

4.  **Training (`model.fit()`)**
    -   Trains the model for a fixed number of epochs (iterations over the entire dataset).
    -   Takes training data (features `x` and labels `y`), `batch_size`, `epochs`, `validation_data`, [[Keras_Callbacks|`callbacks`]], etc.

5.  **Evaluation (`model.evaluate()`)**
    -   Evaluates the trained model's performance on a test dataset, returning the loss value and metric values.

6.  **Prediction (`model.predict()`)**
    -   Generates output predictions for new input data.

7.  **Saving and Loading (`model.save()`, `tf.keras.models.load_model()`)**
    -   Allows saving the entire model (architecture, weights, optimizer state) or just the weights.
    -   See [[TensorFlow_Saving_Loading_Models]].

8.  **Callbacks (`tf.keras.callbacks`)**
    -   Utilities that can be applied at different stages of the training process (e.g., to stop training early, save the model periodically, log to TensorBoard).
    -   See [[Keras_Callbacks]].

## Typical Workflow with `tf.keras`

```python
import tensorflow as tf
from tensorflow import keras # Often imported as keras directly
from tensorflow.keras import layers # Or keras.layers
import numpy as np
import pandas as pd # For creating example data

# 1. Prepare Data (Conceptual e-commerce: predict product category from features)
# Assume features: price_normalized, avg_rating, num_reviews
# Target: category_id (0 for Electronics, 1 for Books, 2 for Apparel)
num_samples = 1000
X_data = np.random.rand(num_samples, 3).astype(np.float32) # 3 features
y_data = np.random.randint(0, 3, num_samples) # 3 categories

# Convert to TensorFlow Datasets for better performance (optional for small data)
# train_dataset = tf.data.Dataset.from_tensor_slices((X_data, y_data)).shuffle(num_samples).batch(32)

# For simplicity with this example, we'll use NumPy arrays directly with fit
# from sklearn.model_selection import train_test_split # Using sklearn for split for simplicity
# X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)


# 2. Define Model Architecture (Sequential API example)
# model = keras.Sequential([
#     layers.Dense(64, activation='relu', input_shape=(X_train.shape,)), # Input layer with 3 features
#     layers.Dropout(0.3),
#     layers.Dense(32, activation='relu'),
#     layers.Dropout(0.2),
#     layers.Dense(3, activation='softmax') # Output layer for 3 categories
# ])
# print("Model Summary:")
# model.summary()

# 3. Compile Model
# model.compile(
#     optimizer=keras.optimizers.Adam(learning_rate=0.001),
#     loss=keras.losses.SparseCategoricalCrossentropy(), # Use if y_train are integer labels
#     # loss=keras.losses.CategoricalCrossentropy(), # Use if y_train is one-hot encoded
#     metrics=[keras.metrics.SparseCategoricalAccuracy(name='accuracy')]
#     # metrics=['accuracy'] # Simpler way if using integer labels and sparse crossentropy
# )

# 4. Train Model (Fit)
# print("\nStarting model training...")
# history = model.fit(
#     X_train, y_train,
#     epochs=10, # Number of passes through the entire training dataset
#     batch_size=32, # Number of samples per gradient update
#     validation_split=0.15, # Fraction of training data to use as validation data
#     verbose=1 # 0 = silent, 1 = progress bar, 2 = one line per epoch
# )
# print("Training finished.")

# Access training history
# training_accuracy = history.history['accuracy']
# validation_accuracy = history.history['val_accuracy']
# print(f"Final training accuracy: {training_accuracy[-1]:.4f}")
# print(f"Final validation accuracy: {validation_accuracy[-1]:.4f}")

# 5. Evaluate Model
# print("\nEvaluating model on test data...")
# test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
# print(f'\nTest accuracy: {test_acc:.4f}')
# print(f'Test loss: {test_loss:.4f}')

# 6. Make Predictions
# sample_to_predict = X_test[:5] # Get first 5 samples from test set
# predictions_proba = model.predict(sample_to_predict)
# predicted_classes = np.argmax(predictions_proba, axis=1)
# print("\nSample predictions (probabilities):\n", predictions_proba)
# print("Predicted classes for samples:", predicted_classes)
# print("Actual classes for samples: ", y_test[:5])
```

`tf.keras` provides a powerful yet user-friendly abstraction for building, training, and deploying deep learning models, making it accessible to a broad range of developers and researchers while leveraging the full power of the TensorFlow backend.

---