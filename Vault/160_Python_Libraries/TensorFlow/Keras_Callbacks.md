---
tags:
  - python
  - tensorflow
  - tf
  - keras
  - neural_networks
  - callbacks
  - training_control
  - model_checkpoint
  - early_stopping
  - tensorboard
  - concept
  - example
aliases:
  - tf.keras.callbacks
  - Keras Training Callbacks
related:
  - "[[Keras_API_in_TensorFlow]]"
  - "[[TensorBoard_TensorFlow]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
---
# Keras: Callbacks (`tf.keras.callbacks`)

**Callbacks** in Keras (`tf.keras.callbacks`) are utilities that can be applied at different stages of the model training process (e.g., at the start/end of an epoch, before/after a batch). They provide a way to customize and control the training loop without modifying the core `model.fit()` logic.

Callbacks are passed to the `model.fit()` method via its `callbacks` argument, which takes a list of callback instances.

## Purpose of Callbacks
-   **Monitoring:** Log metrics, visualize training progress (e.g., with [[TensorBoard_TensorFlow|TensorBoard]]).
-   **Model Checkpointing:** Save the model (or just its weights) periodically during training, typically when performance on a validation set improves.
-   **Early Stopping:** Stop training when a monitored metric has stopped improving, preventing [[Overfitting_Underfitting|overfitting]] and saving computation time.
-   **Learning Rate Scheduling:** Dynamically adjust the learning rate during training.
-   **Custom Actions:** Execute custom Python code at various points in the training loop.

## Common Built-in Callbacks

[list2tab|#Keras Callbacks]
- `ModelCheckpoint`
    -   **Class:** `tf.keras.callbacks.ModelCheckpoint`
    -   **Purpose:** Saves the Keras model or model weights at some frequency.
    -   **Key Arguments:**
        -   `filepath`: Path to save the model file. Can contain formatting options like `{epoch:02d}` or `{val_loss:.2f}`.
        -   `monitor`: Quantity to monitor (e.g., `'val_loss'`, `'val_accuracy'`).
        -   `save_best_only`: If `True`, only saves the model when the monitored quantity has improved.
        -   `save_weights_only`: If `True`, only saves the model's weights.
        -   `mode`: `{'auto', 'min', 'max'}`. In `min` mode, saving occurs when the monitored quantity has decreased; in `max` mode, when it has increased.
        -   `save_freq`: `'epoch'` or integer. When using `'epoch'`, the callback saves the model after each epoch. When using an integer, the callback saves the model after `save_freq` batches.
    -   **Example (Save best model based on validation accuracy):**
        ```python
        # from tensorflow import keras
        # checkpoint_filepath = '/tmp/checkpoint/my_best_model.keras' # Use .weights.h5 for weights only
        # model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
        #     filepath=checkpoint_filepath,
        #     monitor='val_accuracy',
        #     mode='max',
        #     save_best_only=True,
        #     save_weights_only=False, # Save entire model
        #     verbose=1
        # )
        # # In model.fit(): callbacks=[model_checkpoint_callback]
        ```
- `EarlyStopping`
    -   **Class:** `tf.keras.callbacks.EarlyStopping`
    -   **Purpose:** Stop training when a monitored metric has stopped improving for a certain number of epochs. Helps prevent overfitting and reduces training time.
    -   **Key Arguments:**
        -   `monitor`: Quantity to be monitored (e.g., `'val_loss'`).
        -   `min_delta`: Minimum change in the monitored quantity to qualify as an improvement (default 0).
        -   `patience`: Number of epochs with no improvement after which training will be stopped (default 0).
        -   `mode`: `{'auto', 'min', 'max'}`.
        -   `restore_best_weights`: Whether to restore model weights from the epoch with the best value of the monitored quantity (default `False`).
    -   **Example (Stop if validation loss doesn't improve for 5 epochs):**
        ```python
        # from tensorflow import keras
        # early_stopping_callback = keras.callbacks.EarlyStopping(
        #     monitor='val_loss',
        #     patience=5,
        #     verbose=1,
        #     mode='min',
        #     restore_best_weights=True
        # )
        # # In model.fit(): callbacks=[early_stopping_callback]
        ```
- `TensorBoard`
    -   **Class:** `tf.keras.callbacks.TensorBoard`
    -   **Purpose:** Enables visualizations for [[TensorBoard_TensorFlow|TensorBoard]], a TensorFlow visualization toolkit. Logs metrics, model graph, histograms of weights/biases/activations, embeddings, etc.
    -   **Key Arguments:**
        -   `log_dir`: Path of the directory where to save the log files to be parsed by TensorBoard (default './logs').
        -   `histogram_freq`: Frequency (in epochs) at which to compute activation and weight histograms.
        -   `write_graph`: Whether to visualize the graph in TensorBoard.
        -   `update_freq`: `'epoch'` or `'batch'` or integer. How often to write logs.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # import datetime
        # log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        # tensorboard_callback = keras.callbacks.TensorBoard(
        #     log_dir=log_dir,
        #     histogram_freq=1, # Log histograms every epoch
        #     write_graph=True,
        #     update_freq='epoch'
        # )
        # # In model.fit(): callbacks=[tensorboard_callback]
        # # To view: tensorboard --logdir logs/fit
        ```
- `ReduceLROnPlateau`
    -   **Class:** `tf.keras.callbacks.ReduceLROnPlateau`
    -   **Purpose:** Reduce learning rate when a metric has stopped improving.
    -   **Key Arguments:**
        -   `monitor`: Quantity to be monitored.
        -   `factor`: Factor by which the learning rate will be reduced (`new_lr = lr * factor`).
        -   `patience`: Number of epochs with no improvement after which learning rate will be reduced.
        -   `min_lr`: Lower bound on the learning rate.
    -   **Example:**
        ```python
        # from tensorflow import keras
        # reduce_lr_callback = keras.callbacks.ReduceLROnPlateau(
        #     monitor='val_loss',
        #     factor=0.2, # Reduce LR by a factor of 5
        #     patience=3,
        #     min_lr=0.00001,
        #     verbose=1
        # )
        # # In model.fit(): callbacks=[reduce_lr_callback]
        ```
- `LearningRateScheduler`
    -   **Class:** `tf.keras.callbacks.LearningRateScheduler`
    -   **Purpose:** Allows defining a custom schedule function that takes the current epoch index (integer, 0-indexed) and current learning rate as input and returns a new learning rate.
    -   **Key Argument:** `schedule`: A function.
    -   **Example (Custom decay schedule):**
        ```python
        # from tensorflow import keras
        # def lr_scheduler(epoch, lr):
        #     if epoch < 10:
        #         return lr
        #     else:
        #         return lr * tf.math.exp(-0.1)
        # lr_schedule_callback = keras.callbacks.LearningRateScheduler(lr_scheduler)
        # # In model.fit(): callbacks=[lr_schedule_callback]
        ```
- `CSVLogger`
    -   **Class:** `tf.keras.callbacks.CSVLogger`
    -   **Purpose:** Streams epoch results to a CSV file.
    -   **Key Argument:** `filename`: Name of the CSV file.
- `LambdaCallback`
    -   **Class:** `tf.keras.callbacks.LambdaCallback`
    -   **Purpose:** For creating simple, custom callbacks on-the-fly using lambda functions for specific events (`on_epoch_begin`, `on_epoch_end`, `on_batch_begin`, `on_batch_end`, `on_train_begin`, `on_train_end`).

## Using Callbacks in `model.fit()`
You pass a list of callback instances to the `callbacks` argument of `model.fit()`:
```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import datetime

# Dummy model and data for demonstration
# model = keras.Sequential([keras.layers.Dense(1, input_shape=(10,))])
# model.compile(optimizer='sgd', loss='mse')
# X_train = np.random.rand(100, 10)
# y_train = np.random.rand(100, 1)
# X_val = np.random.rand(20, 10)
# y_val = np.random.rand(20, 1)

# Define callbacks
# checkpoint_cb = keras.callbacks.ModelCheckpoint("best_model.keras", save_best_only=True, monitor='val_loss')
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True, monitor='val_loss')
# log_dir_tb = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# tensorboard_cb = keras.callbacks.TensorBoard(log_dir=log_dir_tb, histogram_freq=1)
# reduce_lr_cb = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5)

# list_of_callbacks = [checkpoint_cb, early_stopping_cb, tensorboard_cb, reduce_lr_cb]

# print("Starting conceptual training with callbacks...")
# history = model.fit(
#     X_train, y_train,
#     epochs=5, # Short for demo
#     batch_size=16,
#     validation_data=(X_val, y_val),
#     callbacks=list_of_callbacks, # Pass the list here
#     verbose=1
# )
# print("Conceptual training finished.")
```

## Creating Custom Callbacks
For more advanced control, you can create your own callbacks by subclassing `tf.keras.callbacks.Callback` and overriding methods like:
-   `on_epoch_begin(self, epoch, logs=None)`
-   `on_epoch_end(self, epoch, logs=None)`
-   `on_batch_begin(self, batch, logs=None)`
-   `on_batch_end(self, batch, logs=None)`
-   `on_train_begin(self, logs=None)`
-   `on_train_end(self, logs=None)`

Callbacks are a powerful mechanism in Keras for adding custom behavior and control to the training process, helping to monitor performance, save models, prevent overfitting, and more.

---