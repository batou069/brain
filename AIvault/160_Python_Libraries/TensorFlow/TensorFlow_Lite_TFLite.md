---
tags:
  - python
  - tensorflow
  - tf
  - tflite
  - mobile_deployment
  - edge_computing
  - model_optimization
  - inference
  - concept
  - example
aliases:
  - TFLite
  - TensorFlow Lite
  - TF Lite
related:
  - "[[_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]"
  - "[[Model_Quantization]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
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