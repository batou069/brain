---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - optimizers
  - gradient_descent
  - adam
  - sgd
  - concept
  - example
aliases:
  - tf.keras.optimizers
  - Keras Optimization Algorithms
  - Neural Network Optimizers
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[TensorFlow_Automatic_Differentiation|TF Automatic Differentiation]]"
  - "[[Gradient_Descent]]"
  - "[[Keras_Loss_Functions]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Optimizers (`tf.keras.optimizers`)

**Optimizers** in Keras (`tf.keras.optimizers`) are algorithms or methods used to change the attributes of your neural network, such as weights and learning rate, in order to reduce the losses. They help to minimize the [[Keras_Loss_Functions|loss function]] by updating the model's trainable parameters ([[TensorFlow_Variables|`tf.Variable`s]]) based on the gradients computed during backpropagation (via [[TensorFlow_Automatic_Differentiation|`tf.GradientTape`]]).

Optimizers are specified during the `model.compile()` step.

## How Optimizers Work (General Idea)
1.  During training, a batch of data is passed through the model (forward pass).
2.  A loss value is computed, measuring how far the model's predictions are from the true targets.
3.  Gradients of the loss function with respect to each trainable parameter (weight/bias) are calculated using automatic differentiation (backpropagation).
4.  The optimizer uses these gradients to update the parameters in a direction that is expected to reduce the loss. Different optimizers use different strategies for these updates (e.g., adjusting learning rates, incorporating momentum).

## Common Optimizers in `tf.keras.optimizers`

[list2tab|#Keras Optimizers]
- SGD (Stochastic Gradient Descent)
    -   **Class:** `tf.keras.optimizers.SGD`
    -   **Concept:** A fundamental optimization algorithm. Updates parameters by moving them in the opposite direction of the gradient of the loss function.
    -   **Key Arguments:**
        -   `learning_rate`: Float. Controls the step size of updates (default 0.01).
        -   `momentum`: Float >= 0. Parameter that accelerates SGD in the relevant direction and dampens oscillations (default 0.0).
        -   `nesterov`: Boolean. Whether to apply Nesterov momentum (default False).
    -   **Use Case:** Simple, effective baseline. Can be sensitive to learning rate. Momentum often helps.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # optimizer_sgd = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
        # model.compile(optimizer=optimizer_sgd, loss='mse')
        ```
- Adam (Adaptive Moment Estimation)
    -   **Class:** `tf.keras.optimizers.Adam`
    -   **Concept:** An adaptive learning rate optimization algorithm that computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients. Often a good default choice.
    -   **Key Arguments:**
        -   `learning_rate`: Float (default 0.001).
        -   `beta_1`: Float, defaults to 0.9 (exponential decay rate for the first moment estimates).
        -   `beta_2`: Float, defaults to 0.999 (exponential decay rate for the second-moment estimates).
        -   `epsilon`: Float, defaults to 1e-7 (small constant for numerical stability).
    -   **Use Case:** Widely used, often converges faster and works well on a variety of problems with default settings.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # optimizer_adam = keras.optimizers.Adam(learning_rate=0.001)
        # model.compile(optimizer=optimizer_adam, loss='categorical_crossentropy')
        ```
- RMSprop (Root Mean Square Propagation)
    -   **Class:** `tf.keras.optimizers.RMSprop`
    -   **Concept:** Another adaptive learning rate method. It divides the learning rate by an exponentially decaying average of squared gradients.
    -   **Key Arguments:**
        -   `learning_rate`: Float (default 0.001).
        -   `rho`: Float, defaults to 0.9 (decay rate).
        -   `momentum`: Float >= 0 (default 0.0).
        -   `epsilon`: Float, defaults to 1e-7.
    -   **Use Case:** Often performs well, especially in recurrent neural networks.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # optimizer_rmsprop = keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)
        # model.compile(optimizer=optimizer_rmsprop, loss='binary_crossentropy')
        ```
- Adagrad (Adaptive Gradient Algorithm)
    -   **Class:** `tf.keras.optimizers.Adagrad`
    -   **Concept:** Adapts the learning rate to parameters, performing larger updates for infrequent parameters and smaller updates for frequent parameters. Good for sparse data.
    -   **Key Arguments:**
        -   `learning_rate`: Float (default 0.001).
        -   `initial_accumulator_value`: Float (default 0.1).
        -   `epsilon`: Float, defaults to 1e-7.
    -   **Use Case:** Can be effective for sparse data (e.g., in NLP with large vocabularies). Learning rate tends to decrease significantly over time.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # optimizer_adagrad = keras.optimizers.Adagrad(learning_rate=0.01)
        # model.compile(optimizer=optimizer_adagrad, loss='mse')
        ```
- Adadelta
    -   **Class:** `tf.keras.optimizers.Adadelta`
    -   **Concept:** An extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate. It adapts learning rates based on a moving window of gradient updates, rather than accumulating all past gradients.
    -   **Key Arguments:**
        -   `learning_rate`: Float (default 0.001).
        -   `rho`: Float, defaults to 0.95 (decay rate).
        -   `epsilon`: Float, defaults to 1e-7.
    -   **Use Case:** Less common than Adam or RMSprop but can be effective. Does not require manual tuning of a learning rate as much.
- AdamW
    -   **Class:** `tf.keras.optimizers.AdamW`
    -   **Concept:** A variant of Adam that decouples weight decay from the gradient-based updates. Often reported to improve generalization in some cases compared to Adam with L2 regularization.
    -   **Key Arguments:** `learning_rate`, `weight_decay`, `beta_1`, `beta_2`, `epsilon`.
- Nadam (Nesterov-accelerated Adaptive Moment Estimation)
    -   **Class:** `tf.keras.optimizers.Nadam`
    -   **Concept:** Adam optimizer with Nesterov momentum.
- Ftrl
    -   **Class:** `tf.keras.optimizers.Ftrl`
    -   **Concept:** Follow The Regularized Leader algorithm, often good for shallow models with sparse features.

## Using Optimizers
Optimizers are passed to the `model.compile()` method:
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# model = keras.Sequential([layers.Dense(10, input_shape=(784,)), layers.Dense(1, activation='sigmoid')])

# Option 1: Pass optimizer instance
# adam_opt = keras.optimizers.Adam(learning_rate=0.005)
# model.compile(optimizer=adam_opt, loss='binary_crossentropy', metrics=['accuracy'])

# Option 2: Pass optimizer name string (uses default parameters)
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
```

## Learning Rate Scheduling
The learning rate is a critical hyperparameter. Instead of a fixed learning rate, it's often beneficial to use a **learning rate schedule** that changes the learning rate during training (e.g., decreasing it over time).
`tf.keras.optimizers.schedules` provides classes for this:
-   `ExponentialDecay`
-   `PiecewiseConstantDecay`
-   `InverseTimeDecay`
-   And others.

**Example with Learning Rate Schedule:**
```python
# from tensorflow import keras

# initial_learning_rate = 0.1
# lr_schedule = keras.optimizers.schedules.ExponentialDecay(
#     initial_learning_rate,
#     decay_steps=100000,
#     decay_rate=0.96,
#     staircase=True)

# optimizer_with_schedule = keras.optimizers.Adam(learning_rate=lr_schedule)
# model.compile(optimizer=optimizer_with_schedule, ...)
```

## Gradient Clipping
To prevent exploding gradients (where gradients become excessively large, leading to unstable training), optimizers in Keras often have a `clipnorm` or `clipvalue` argument.
-   `clipnorm`: Clips gradients element-wise if their L2 norm exceeds this value.
-   `clipvalue`: Clips gradients element-wise to be within `[-value, value]`.

```python
# optimizer_clipped = keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0)
```

Choosing the right optimizer and tuning its parameters (especially the learning rate) is a crucial part of the model training process and often requires experimentation. Adam is a common and robust starting point for many problems.

---