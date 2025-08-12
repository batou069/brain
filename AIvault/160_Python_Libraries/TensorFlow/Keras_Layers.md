---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - layers
  - dense
  - conv2d
  - lstm
  - embedding
  - concept
  - example
aliases:
  - tf.keras.layers
  - Keras Neural Network Layers
  - Common Keras Layers
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[Keras_Sequential_Functional_API]]"
  - "[[Activation_Functions_ML|Activation Functions]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Layers (`tf.keras.layers`)

**Layers** are the fundamental building blocks of neural networks in Keras (`tf.keras`). Each layer performs a specific transformation on its input data (which are [[TensorFlow_Tensors|tensors]]) and typically has trainable parameters ([[TensorFlow_Variables|weights and biases]]) that are learned during the training process.

Keras provides a comprehensive set of pre-built layers for various purposes, found in the `tf.keras.layers` module.

## Common Layer Categories and Examples

[list2tab|#Keras Layer Types]
- Core Layers
    -   **`Dense` (Fully Connected Layer):**
        -   Implements the operation: `output = activation(dot(input, kernel) + bias)`.
        -   Every neuron in a dense layer is connected to every neuron in the previous layer.
        -   **Key Arguments:**
            -   `units`: Positive integer, dimensionality of the output space (number of neurons).
            -   `activation`: Activation function to use (e.g., `'relu'`, `'sigmoid'`, `'softmax'`, or a `tf.nn.activation_function`). See [[Activation_Functions_ML]].
            -   `use_bias`: Boolean, whether the layer uses a bias vector.
            -   `kernel_initializer`, `bias_initializer`: Initializers for the kernel weights matrix and bias vector.
        -   **Example (Predicting product price based on features):**
            ```python
            # from tensorflow.keras import layers, Input, Model
            # product_features_input = Input(shape=(10,), name="product_features") # 10 input features
            # hidden_layer = layers.Dense(64, activation='relu', name="hidden_dense")(product_features_input)
            # price_output = layers.Dense(1, activation=None, name="price_output_linear")(hidden_layer) # Linear activation for regression
            # price_model = Model(inputs=product_features_input, outputs=price_output)
            # price_model.summary()
            ```
    -   **`Activation`:**
        -   Applies an activation function to an output. Often, activation is specified directly in other layers (like `Dense`, `Conv2D`).
        -   `layers.Activation('relu')`
    -   **`Embedding`:**
        -   Turns positive integers (indices) into dense vectors of fixed size. Useful for representing categorical data or words in NLP.
        -   Often the first layer in a model processing text data.
        -   **Key Arguments:** `input_dim` (size of vocabulary), `output_dim` (dimension of dense embedding), `input_length` (length of input sequences).
        -   **Example (Embedding product IDs):**
            ```python
            # num_unique_product_ids = 10000
            # embedding_dimension = 50
            # product_id_input = Input(shape=(1,), name="product_id_input") # Input is a single product ID
            # embedding_layer = layers.Embedding(input_dim=num_unique_product_ids,
            #                                   output_dim=embedding_dimension,
            #                                   name="product_embedding")(product_id_input)
            # flattened_embedding = layers.Flatten()(embedding_layer) # Flatten for dense layers
            # # ... further layers ...
            ```
    -   **`Flatten`:** Flattens the input. Does not affect the batch size. Useful for converting multi-dimensional feature maps (e.g., from Conv2D) into a 1D vector before passing to Dense layers.
    -   **`Reshape`:** Reshapes an output to a certain shape.
    -   **`Permute`:** Permutes the dimensions of the input according to a given pattern.
    -   **`Dropout`:**
        -   Applies Dropout to the input. Dropout consists in randomly setting a fraction `rate` of input units to 0 at each update during training time, which helps prevent [[Overfitting_Underfitting|overfitting]].
        -   **Key Argument:** `rate` (float between 0 and 1).
- Convolutional Layers (for spatial data like images)
    -   **`Conv1D`:** 1D convolution layer (e.g., for temporal data, text).
    -   **`Conv2D`:** 2D convolution layer (e.g., for images).
        -   **Key Arguments:** `filters` (number of output filters/kernels), `kernel_size` (e.g., `(3,3)`), `strides`, `padding` (`'valid'` or `'same'`), `activation`.
    -   **`Conv3D`:** 3D convolution layer (e.g., for video or volumetric data).
    -   **SeparableConv1D/2D, DepthwiseConv2D:** More specialized convolutions.
    -   **Example (Part of an image classifier for product images):**
        ```python
        # image_input = Input(shape=(128, 128, 3), name="product_image") # 128x128 RGB
        # conv_layer1 = layers.Conv2D(32, kernel_size=(3,3), activation='relu', padding='same')(image_input)
        # pool_layer1 = layers.MaxPooling2D(pool_size=(2,2))(conv_layer1)
        # conv_layer2 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(pool_layer1)
        # # ... further conv/pool layers ...
        ```
- Pooling Layers (often used with Convolutional layers)
    -   **`MaxPooling1D`, `MaxPooling2D`, `MaxPooling3D`:** Downsamples by taking the maximum value over a window.
    -   **`AveragePooling1D`, `AveragePooling2D`, `AveragePooling3D`:** Downsamples by taking the average value over a window.
    -   **`GlobalMaxPooling1D/2D`, `GlobalAveragePooling1D/2D`:** Takes the max/average over the entire spatial dimensions, reducing them to a single value per feature map.
- Recurrent Layers (for sequential data like text or time series)
    -   **`SimpleRNN`:** Fully-connected RNN where the output is to be fed back to input.
    -   **`LSTM` (Long Short-Term Memory):** A type of RNN particularly good at learning long-range dependencies.
        -   **Key Arguments:** `units` (dimensionality of output space), `activation`, `recurrent_activation`, `return_sequences` (whether to return the last output or the full sequence), `dropout`, `recurrent_dropout`.
    -   **`GRU` (Gated Recurrent Unit):** Another type of RNN similar to LSTM but with a simpler architecture.
    -   **`Bidirectional`:** A wrapper layer that makes an RNN bidirectional (processes sequence forwards and backwards).
    -   **Example (Processing sequences of product browsing history):**
        ```python
        # sequence_input = Input(shape=(None, 50), name="browsing_sequence") # Variable length sequences of 50-dim features
        # lstm_layer = layers.LSTM(64, return_sequences=False, name="lstm_processing")(sequence_input)
        # # if return_sequences=True, output shape is (batch, timesteps, 64)
        # # if return_sequences=False, output shape is (batch, 64) - only last timestep output
        # # ... further layers ...
        ```
- Normalization Layers
    -   **`BatchNormalization`:** Normalizes the activations of the previous layer at each batch, i.e. applies a transformation that maintains the mean activation close to 0 and the activation standard deviation close to 1. Helps stabilize and accelerate training.
    -   **`LayerNormalization`:** Normalizes activations across the features for each data sample independently.
- Regularization Layers
    -   **`Dropout`:** (Already mentioned in Core Layers)
    -   **`GaussianNoise`:** Applies additive zero-centered Gaussian noise.
    -   **`ActivityRegularization`:** Applies a penalty on the layer's activations during training.
- Attention Layers
    -   **`Attention`:** Dot-product attention layer.
    -   **`AdditiveAttention`:** Additive attention layer (Bahdanau-style).
    -   **`MultiHeadAttention`:** Core component of Transformer models.
- Reshaping Layers
    -   `Flatten`, `Reshape`, `Permute`, `RepeatVector`, `UpSampling1D/2D/3D`, `Cropping1D/2D/3D`.
- Merging Layers
    -   `Add`, `Subtract`, `Multiply`, `Average`, `Maximum`, `Minimum`, `Concatenate`, `Dot`. Used to combine multiple input tensors, common in the Functional API.

## Common Layer Arguments
Many layers share common arguments:
-   `activation`: Activation function.
-   `kernel_initializer`, `bias_initializer`: How to initialize weights/biases.
-   `kernel_regularizer`, `bias_regularizer`, `activity_regularizer`: Apply L1/L2 regularization penalties.
-   `name`: Optional name string for the layer.

## Creating Custom Layers
If none of the built-in layers suit your needs, you can create custom layers by subclassing `tf.keras.layers.Layer` and implementing:
-   `__init__(self, **kwargs)`: Define layer attributes.
-   `build(self, input_shape)`: Define the layer's weights (trainable variables). Called once when the layer is first used.
-   `call(self, inputs, training=None, **kwargs)`: Defines the forward pass logic of the layer.
-   `get_config(self)`: For serialization.

Keras layers provide a rich and flexible set of tools for constructing diverse neural network architectures. Understanding their purpose and key arguments is essential for effective deep learning model development.

---