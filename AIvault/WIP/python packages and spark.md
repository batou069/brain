Okay, I will now create the notes for the remaining TensorFlow topics: Distributed Training, TensorFlow Lite (TFLite), TensorFlow.js (TF.js), and TensorFlow Serving. These notes will provide overviews and conceptual examples.

---

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Distributed_Training.md
````markdown
---
tags: [python, tensorflow, tf, keras, distributed_training, scaling, multi_gpu, tpu, concept, example]
aliases: [tf.distribute.Strategy, Distributed TensorFlow, Scaling TF Training, Multi-Worker Training TF]
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
-   **Train Larger Models:** Models that are too large to fit into the memory of a single GPU can be trained using model parallelism (though data parallelism is more common and simpler to implement with `tf.distribute.Strategy`).
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
#   model = keras.Sequential([...]) # Define your Keras model
#   optimizer = keras.optimizers.Adam()
#   model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Prepare your tf.data.Dataset
# train_dataset = ... # Your tf.data pipeline, properly sharded or distributed

# Train the model
# model.fit(train_dataset, epochs=...)
```

## Common Distribution Strategies

[list2tab|#TF Distribute Strategies]
- `MirroredStrategy`
    -   **Class:** `tf.distribute.MirroredStrategy`
    -   **Use Case:** For training on **multiple GPUs on a single machine (host)**.
    -   **How it Works (Data Parallelism):**
        1.  All model variables (weights) are mirrored (copied) to each available GPU on the host.
        2.  Each GPU processes a different slice of the input data batch.
        3.  Gradients are computed independently on each GPU for its slice of data.
        4.  Gradients are aggregated across all GPUs using an efficient all-reduce algorithm (e.g., NCCL).
        5.  The aggregated gradients are used to update the mirrored variables on each GPU synchronously, ensuring all replicas remain identical.
    -   **Example:**
        ```python
        import tensorflow as tf
        from tensorflow import keras
        from tensorflow.keras import layers
        import numpy as np
        
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            print(f"Found {len(gpus)} GPUs.")
            strategy = tf.distribute.MirroredStrategy() # Uses all available GPUs by default
            # Or: strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])
            print(f"Number of devices in MirroredStrategy: {strategy.num_replicas_in_sync}")

            with strategy.scope():
                # Define and compile your Keras model inside the strategy scope
                mirrored_model = keras.Sequential([
                    layers.Dense(128, activation='relu', input_shape=(784,)), # Example MNIST-like input
                    layers.Dense(10, activation='softmax') # 10 output classes
                ])
                mirrored_model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
                                       loss='sparse_categorical_crossentropy',
                                       metrics=['accuracy'])
            
            # Prepare a tf.data.Dataset (conceptual)
            # (X_train_np, y_train_np) = ... load your data ...
            # BATCH_SIZE_PER_REPLICA = 64
            # GLOBAL_BATCH_SIZE = BATCH_SIZE_PER_REPLICA * strategy.num_replicas_in_sync
            # train_dataset = tf.data.Dataset.from_tensor_slices((X_train_np, y_train_np)).shuffle(10000).batch(GLOBAL_BATCH_SIZE)
            
            print("Training with MirroredStrategy (conceptual)...")
            # mirrored_model.fit(train_dataset, epochs=2) # This would run distributed training
        else:
            print("No GPUs found, MirroredStrategy example primarily for multi-GPU setup.")
            # Fallback for non-GPU environment (single device training)
            # model = keras.Sequential([...]) # Define model
            # model.compile(...)
            # model.fit(...)
        ```
- `MultiWorkerMirroredStrategy`
    -   **Class:** `tf.distribute.MultiWorkerMirroredStrategy`
    -   **Use Case:** For **synchronous distributed training across multiple machines (workers)**, where each machine might have one or more GPUs.
    -   **How it Works (Data Parallelism):** Similar to `MirroredStrategy`, but variables are mirrored, and gradient aggregation (all-reduce) happens across all GPUs on all participating worker machines.
    -   **Setup:** Requires setting up a `TF_CONFIG` environment variable on each worker. This JSON string defines the cluster structure (worker addresses, task types like 'worker' or 'chief', and task indices).
- `TPUStrategy`
    -   **Class:** `tf.distribute.experimental.TPUStrategy` (may move out of `experimental` in future TF versions)
    -   **Use Case:** For training on Google's Tensor Processing Units (TPUs), which are specialized hardware for accelerating ML workloads.
    -   **How it Works:** Connects to a TPU cluster resource and distributes computation across TPU cores. Requires specific initialization to connect to the TPU system.
- `ParameterServerStrategy`
    -   **Class:** `tf.distribute.experimental.ParameterServerStrategy`
    -   **Use Case:** For **asynchronous data parallelism**. Model parameters (variables) are sharded and managed by dedicated "parameter server" tasks. Worker tasks fetch the latest parameters, compute gradients on their local data, and push gradients back to the parameter servers asynchronously.
    -   **Pros:** Can be beneficial for very large models that don't fit on a single device, or when network bandwidth between workers is a bottleneck for synchronous all-reduce operations. Can sometimes tolerate slower workers better.
    -   **Cons:** Asynchronous updates can lead to stale gradients and might require more careful tuning of learning rates and optimization algorithms. More complex to set up with `TF_CONFIG`.
- `CentralStorageStrategy`
    -   **Class:** `tf.distribute.CentralStorageStrategy`
    -   **Use Case:** Synchronous training where variables are placed on the CPU (or a single specified GPU), and operations are replicated across all local GPUs. Gradients are aggregated back to the CPU (or central GPU) for variable updates.
    -   **Difference from MirroredStrategy:** Variables are not mirrored. `MirroredStrategy` is generally preferred for multi-GPU training on a single host due to better performance from keeping variables on GPUs.

## Key Considerations for Distributed Training
1.  **Data Pipeline (`tf.data`):**
    -   An efficient input pipeline using [[TensorFlow_Data_Pipeline_tf_data|`tf.data`]] is critical.
    -   The dataset needs to be distributed or sharded appropriately so each replica/worker processes a unique portion of the data. `tf.data.experimental.DistributeOptions` or auto-sharding policies can help.
    -   The **global batch size** is the total batch size processed across all replicas in one step. It's usually `batch_size_per_replica * num_replicas_in_sync`. This global batch size is what you pass to `dataset.batch()`.
2.  **Learning Rate Scaling:**
    -   When increasing the global batch size (due to more replicas), it's often necessary to adjust the learning rate. A common heuristic is the "linear scaling rule": multiply the base learning rate by the number of replicas. However, this may require further tuning (e.g., with a learning rate warmup period).
3.  **[[TensorFlow_Saving_Loading_Models|Saving and Loading Models]]:**
    -   Models defined and trained within a `strategy.scope()` should ideally also be saved and loaded within a `strategy.scope()` if you intend to continue distributed training or perform distributed inference with the same strategy.
    -   `model.save()` (to SavedModel format) works correctly with `tf.distribute.Strategy`. The saved model is a standard, non-distributed model that can be loaded with or without a strategy for inference.
4.  **Custom Training Loops:**
    -   If you are writing a custom training loop using `tf.GradientTape` instead of `model.fit()`, you'll need to use strategy-specific methods like `strategy.run(step_fn, args=(data_batch,))` to execute a training step per replica, and `strategy.reduce()` to aggregate per-replica values (like loss) back to the host.
5.  **Environment Setup (for Multi-Worker):**
    -   Strategies like `MultiWorkerMirroredStrategy` and `ParameterServerStrategy` require proper configuration of the `TF_CONFIG` environment variable on each worker node to define the cluster topology and each worker's role.

The `tf.distribute.Strategy` API significantly simplifies the process of scaling out TensorFlow Keras model training, allowing developers to leverage multiple processing units with relatively minor code changes.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Lite_TFLite.md
````markdown
---
tags: [python, tensorflow, tf, tflite, mobile_deployment, edge_computing, model_optimization, inference, concept, example]
aliases: [TFLite, TensorFlow Lite, TF Lite, On-Device ML]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]" # Models are converted to TFLite
  - "[[Model_Quantization]]"
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow Lite (TFLite)

**TensorFlow Lite (TFLite)** is an open-source deep learning framework from Google designed for **on-device inference** on mobile phones (Android and iOS), embedded Linux devices (like Raspberry Pi), and microcontrollers. It enables running [[TensorFlow_MOC|_TensorFlow_MOC]] models with low latency and a small binary size, optimized for resource-constrained devices.

## Core Purpose and Benefits
-   **On-Device Machine Learning:** Run ML models directly on edge devices without needing a server connection.
-   **Low Latency:** Faster inference by avoiding network round-trips.
-   **Small Model Size:** Tools to convert and optimize TensorFlow models into a compact `.tflite` format.
-   **Privacy:** User data can remain on the device, enhancing privacy.
-   **Offline Capability:** Models can run without an internet connection.
-   **Power Efficiency:** Optimized for low power consumption on mobile and embedded hardware.
-   **Hardware Acceleration:** Supports acceleration using device GPUs, DSPs (Digital Signal Processors), and NPUs (Neural Processing Units) where available, through TFLite Delegates.

## TFLite Workflow

The typical workflow involves several steps:

[d2]
```d2
direction: right
shape: sequence_diagram

TF_Keras_Model: "1. Train TensorFlow/Keras Model" {
  shape: process
  style.fill: "#BBDEFB" # Light blue
}

TFLite_Converter: "2. TFLite Converter (Python)" {
  shape: process
  style.fill: "#C8E6C9" # Light green
  Optimization: "Optimization (e.g., Quantization)"
}

TFLite_Model_File: "3. `.tflite` Model File" {
  shape: document
  style.fill: "#FFF9C4" # Light yellow
}

Edge_Device: "4. Deploy to Edge Device\n(Mobile, Embedded, MCU)" {
  shape: device
  style.fill: "#FFCCBC" # Light red
  TFLite_Interpreter_Device: "TFLite Interpreter (Java/Swift/C++/Python)" {
    shape: process
    style.fill: "#FFAB91"
  }
  InputData_Device: "New Input Data"
  OutputPredictions_Device: "Predictions"
}

TF_Keras_Model -> TFLite_Converter: "SavedModel or Keras .h5/.keras"
TFLite_Converter -> TFLite_Model_File: "Generates"
TFLite_Converter.Optimization -> TFLite_Converter
TFLite_Model_File -> Edge_Device.TFLite_Interpreter_Device: "Load Model"
Edge_Device.InputData_Device -> Edge_Device.TFLite_Interpreter_Device: "Feed Data"
Edge_Device.TFLite_Interpreter_Device -> Edge_Device.OutputPredictions_Device: "Run Inference"

style TF_Keras_Model { icon: "🧠" }
style TFLite_Converter { icon: "🔄" }
style TFLite_Model_File { icon: "📄" }
style Edge_Device { icon: "📱" }
```

1.  **Train a TensorFlow Model:** Develop and train your model using TensorFlow, typically with `tf.keras`.
2.  **Convert the Model:** Use the **TensorFlow Lite Converter** (Python API) to convert the trained TensorFlow model into the TensorFlow Lite FlatBuffer format (`.tflite`). This step can also include optimizations like [[Model_Quantization|quantization]].
3.  **Deploy to Device:** Integrate the `.tflite` model file into your mobile application (Android/iOS), embedded system, or microcontroller project.
4.  **Run Inference:** Use the **TensorFlow Lite Interpreter** (available for various platforms and languages) to load the `.tflite` model and perform inference on new input data directly on the device.

## Model Optimization Techniques for TFLite
To make models suitable for on-device execution, TFLite employs several optimization techniques, often applied during the conversion process:

[list2tab|#TFLite Optimizations]
- [[Model_Quantization|Quantization]]
    -   **Concept:** Reducing the precision of the model's weights and/or activations from floating-point (e.g., `float32`) to lower-bit representations (e.g., `int8`, `float16`).
    -   **Benefits:** Reduced model size, faster inference (especially with hardware support for lower precision), lower power consumption.
    -   **Types:**
        -   **Post-Training Quantization:** Quantize an already trained `float32` model.
            -   *Dynamic range quantization:* Weights to `int8`, activations remain `float32` (or `float16`), dynamically quantized at runtime. Good balance of size reduction and ease of use.
            -   *Full integer quantization (INT8):* Weights and activations to `int8`. Requires a representative dataset for calibration to determine scaling factors. Maximizes performance on integer-only hardware (like many MCUs or DSPs).
            -   *Float16 quantization:* Weights and activations to `float16`. Reduces model size by half, can speed up inference on GPUs that support float16.
        -   **Quantization-Aware Training (QAT):** Simulates quantization effects (fake quantization nodes) during the TensorFlow training process. This allows the model to adapt to quantization, often leading to better accuracy for the final quantized model compared to post-training quantization, especially for full integer quantization.
- Pruning
    -   **Concept:** Systematically removing weights from the model that have minimal impact on its performance, creating sparse models. This is typically done during or after training in TensorFlow before conversion.
    -   **Benefits:** Can reduce model size and sometimes inference time, especially if hardware supports sparse computations.
- Weight Clustering
    -   **Concept:** Grouping similar weight values into a smaller number of clusters and representing all weights in a cluster by the cluster's centroid value.
    -   **Benefits:** Reduces the number of unique weight values, enabling better compression of the model.

## TensorFlow Lite Converter (Python API)
The converter is part of the TensorFlow Python library.

**Example: Converting a Keras SavedModel to TFLite with default optimization**
```python
import tensorflow as tf
import numpy as np

# Assume 'model' is a trained tf.keras.Model
# For e-commerce: a model to classify product images (e.g., 'shoe', 'shirt', 'accessory')
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(32, 32, 3)), # Example input
#     tf.keras.layers.MaxPooling2D((2,2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(3, activation='softmax') # 3 product classes
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
# model.fit(np.random.rand(10, 32, 32, 3), np.random.randint(0,3,10), epochs=1, verbose=0) # Dummy train

# Convert the Keras model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Apply default optimizations (often includes dynamic range quantization)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert the model
tflite_model_content = converter.convert()

# Save the TFLite model to a .tflite file
tflite_model_file_path = "product_image_classifier.tflite"
with open(tflite_model_file_path, 'wb') as f:
    f.write(tflite_model_content)
print(f"TFLite model saved to: {tflite_model_file_path}")
```

## TensorFlow Lite Interpreter
Once you have the `.tflite` model, you use the TFLite interpreter on the target device to run inference.

**Example: Python TFLite Interpreter (for testing or on devices like Raspberry Pi)**
```python
import tensorflow as tf # For interpreter in Python
import numpy as np

tflite_model_path = "product_image_classifier.tflite" # From previous step

try:
    interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
    interpreter.allocate_tensors() # Allocate memory for tensors

    # Get input and output tensor details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    # print("Input Details:", input_details)
    # print("Output Details:", output_details)

    # Prepare a sample input (must match model's expected input shape and type)
    input_shape = input_details['shape'] # e.g., for one 32x32 RGB image
    # Create a dummy image that matches the input shape and type
    sample_input_image = np.random.rand(*input_shape).astype(input_details['dtype'])

    # Set the value of the input tensor
    interpreter.set_tensor(input_details['index'], sample_input_image)

    # Run inference
    interpreter.invoke()

    # Get the result from the output tensor
    output_data = interpreter.get_tensor(output_details['index'])
    # print("\nPrediction output from TFLite model (probabilities for 3 classes):", output_data)
    # predicted_class_index = np.argmax(output_data)
    # print("Predicted class index:", predicted_class_index)

except Exception as e:
    print(f"Error with TFLite interpreter (is model file '{tflite_model_path}' valid and path correct?): {e}")
    print("Ensure the model was converted successfully and the path is correct.")
```
Interpreters are also available for Java/Kotlin (Android), Swift/Objective-C (iOS), and C++ for embedded systems and microcontrollers.

## Use Cases
-   **Mobile Applications:** Image classification (e.g., identifying products from a photo), object detection, text classification (e.g., sentiment of a review), smart replies, on-device speech recognition, translation.
-   **Embedded Systems & IoT:** Anomaly detection in sensor data from industrial equipment, keyword spotting in voice assistants, simple gesture recognition on smart devices.
-   **Microcontrollers (MCU):** Ultra-low power ML applications using TensorFlow Lite for Microcontrollers (e.g., wake-word detection, simple sensor-based activity recognition).

TensorFlow Lite is a key technology for deploying machine learning models to edge devices, enabling intelligent applications that are responsive, privacy-preserving, and can operate offline.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_js_TFJS.md
````markdown
---
tags: [python, tensorflow, tf, tfjs, javascript, web_ml, browser_ml, nodejs_ml, model_deployment, concept, example]
aliases: [TF.js, TensorFlow.js, JavaScript TensorFlow, Client-Side ML]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models]]" # Models can be converted for TF.js
  - "[[Deep_Learning_Overview]]"
  - "[[Web_Development_Basics]]" # Placeholder for web concepts
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow.js (TF.js)

**TensorFlow.js (TF.js)** is an open-source hardware-accelerated JavaScript library for training and running machine learning models directly **in the browser** or in **Node.js**. It brings the power of TensorFlow and deep learning to the JavaScript ecosystem, enabling a wide range of client-side and server-side JavaScript ML applications.

## Core Purpose and Benefits
-   **ML in the Browser:** Enables running ML models directly in the user's web browser.
    -   **Interactivity:** Models can interact with webpage content (DOM elements), user inputs (camera, microphone, mouse movements).
    -   **Privacy:** User data can remain client-side, not needing to be sent to a server for inference. This is crucial for sensitive data.
    -   **Low Latency:** Inference happens locally on the user's device, avoiding network delays associated with server round-trips.
    -   **Accessibility & Reach:** Deploy ML models to anyone with a web browser without requiring them to install specific software or drivers.
    -   **Offline Capability:** Once models and assets are cached by the browser, applications can run offline.
-   **ML in Node.js:** Allows for server-side JavaScript ML applications using TensorFlow's performance capabilities (e.g., binding to TensorFlow's C++ backend).
-   **Run Existing Models:** Convert pre-trained TensorFlow (Python) models or Keras models into a format that can be loaded and run by TensorFlow.js.
-   **Train Models from Scratch:** Define, train, and run models entirely in JavaScript using an API very similar to the Keras API.
-   **Hardware Acceleration:**
    -   In the browser: Can leverage WebGL for GPU acceleration.
    -   In Node.js: Can bind to the native TensorFlow C++ backend for CPU and GPU (CUDA) acceleration.

## Key Components and APIs of TensorFlow.js

[list2tab|#TF.js Components]
- Core API (`@tensorflow/tfjs-core`)
    -   Provides low-level linear algebra operations and the `tf.Tensor` object in JavaScript, which is the fundamental data structure.
    -   Includes operations for tensor creation, manipulation, mathematical functions, etc., similar in spirit to NumPy and TensorFlow Python's core.
- Layers API (`@tensorflow/tfjs-layers`)
    -   A high-level API for building neural networks, modeled directly after the [[Keras_API_in_TensorFlow|Keras API]].
    -   Define models using `tf.sequential()` or the functional API `tf.model()`.
    -   Includes common layers: `tf.layers.dense()`, `tf.layers.conv2d()`, `tf.layers.lstm()`, `tf.layers.embedding()`, etc.
    -   Compile models with optimizers (`tf.train.*`), loss functions, and metrics.
    -   Train models using `model.fit()` or `model.fitDataset()`.
- Converter (`@tensorflow/tfjs-converter`)
    -   A command-line tool (`tensorflowjs_converter`) and Python library functions to convert pre-trained TensorFlow SavedModels or Keras H5/.keras models (from Python) into a format that can be loaded by TensorFlow.js.
    -   The conversion typically results in a `model.json` file (describing the graph topology and weights manifest) and one or more binary shard files for the weights.
- Data API (`@tensorflow/tfjs-data`)
    -   Provides an API similar to `tf.data` for creating efficient input pipelines for training models in JavaScript.
    -   Can handle data from various sources like webcams, microphones, files, DOM elements (e.g., HTMLImageElement, HTMLCanvasElement, HTMLVideoElement), and CSV/TSV files.
- Pre-trained Models (`@tensorflow-models/*`)
    -   A collection of pre-trained models for common tasks, packaged for easy use in JavaScript applications.
    -   Examples: MobileNet (image classification), PoseNet (pose estimation), Coco-SSD (object detection), Universal Sentence Encoder (text embeddings), Speech Commands, Face Landmarks Detection.
- Backends
    -   TensorFlow.js can run on different backends for computation:
        -   **`tfjs-backend-cpu`**: Runs on CPU using pure JavaScript. Default for Node.js if no GPU backend is found.
        -   **`tfjs-backend-webgl`**: Uses WebGL for GPU acceleration in the browser. Usually the fastest option in browsers.
        -   **`tfjs-backend-wasm` (WebAssembly)**: Uses WebAssembly for CPU acceleration. Can be faster than plain JavaScript CPU backend, especially for operations not well-suited for WebGL.
        -   **`tfjs-node`** (for Node.js): Binds to the TensorFlow C library for native speed on CPU.
        -   **`tfjs-node-gpu`** (for Node.js): Binds to TensorFlow C library with GPU support (requires CUDA drivers and compatible hardware).

## Workflow Examples

### 1. Using a Pre-trained Model (e.g., MobileNet for Image Classification in Browser HTML/JS)
```html
<!DOCTYPE html>
<html>
<head>
    <title>TF.js Image Classification with MobileNet</title>
    <!-- 1. Load TensorFlow.js Core -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <!-- 2. Load the MobileNet model -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@latest/dist/mobilenet.min.js"></script>
</head>
<body>
    <h1>Product Image Classifier (Conceptual)</h1>
    <!-- Assume an image of a product -->
    <img id="productImage" src="https://via.placeholder.com/224" width="224" height="224" alt="product image" crossorigin="anonymous" />
    <input type="file" id="fileInput" accept="image/*" />
    <div id="predictions">Loading model and classifying...</div>

    <script>
        const imgElement = document.getElementById('productImage');
        const predictionsElement = document.getElementById('predictions');
        const fileInputElement = document.getElementById('fileInput');
        let mobilenetModel;

        async function classifyImage() {
            if (!mobilenetModel) {
                predictionsElement.innerText = 'Loading MobileNet model...';
                mobilenetModel = await mobilenet.load(); // Load the MobileNet model
                predictionsElement.innerText = 'Model loaded. Ready to classify.';
            }
            
            if (imgElement.src && imgElement.naturalWidth > 0) { // Check if image is loaded
                try {
                    predictionsElement.innerText = 'Classifying...';
                    const predictions = await mobilenetModel.classify(imgElement);
                    
                    predictionsElement.innerHTML = '<h3>Top Predictions:</h3>';
                    predictions.forEach(p => {
                        predictionsElement.innerHTML += `${p.className} : ${p.probability.toFixed(4)}<br>`;
                    });
                } catch (e) {
                    predictionsElement.innerText = 'Error during classification.';
                    console.error(e);
                }
            } else {
                predictionsElement.innerText = 'Image not loaded yet or invalid.';
            }
        }
        
        // Classify when the image (default or uploaded) is loaded
        imgElement.onload = classifyImage;
        
        // Handle file upload
        fileInputElement.onchange = (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    imgElement.src = e.target.result; // This will trigger imgElement.onload
                }
                reader.readAsDataURL(file);
            }
        };

        // Initial classification if default image src is valid and image is already loaded (e.g. from cache)
        if (imgElement.complete && imgElement.naturalHeight !== 0) {
            classifyImage();
        } else if (!imgElement.src || imgElement.src === window.location.href) {
             predictionsElement.innerText = 'Please upload an image to classify.';
        }
    </script>
</body>
</html>
```
*(To run this, save as HTML and open in a browser. Replace placeholder image src with a real one or use the file input.)*

### 2. Converting a Python Keras Model and Using it in Node.js
**Step A: Save Keras model in Python and Convert (same as in TFLite example, but target TF.js)**
```python
# Python script
# import tensorflow as tf
# from tensorflow import keras
# import numpy as np

# model = keras.Sequential([
#     keras.layers.Dense(64, activation='relu', input_shape=(50,)), # Example: 50 input features
#     keras.layers.Dense(3, activation='softmax') # Example: 3 product categories
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
# model.fit(np.random.rand(10, 50), np.random.randint(0,3,10), epochs=1, verbose=0)
# model.save("./my_keras_model_for_conversion") # SavedModel format

# Terminal command for conversion:
# pip install tensorflowjs
# tensorflowjs_converter --input_format=tf_saved_model \
#                        ./my_keras_model_for_conversion \
#                        ./my_tfjs_model_output_node
```
This creates `model.json` and weight shard files in `./my_tfjs_model_output_node`.

**Step B: Load and use in Node.js**
```javascript
// Node.js script (e.g., predict_server.js)
// const tf = require('@tensorflow/tfjs-node'); // For CPU
// // const tf = require('@tensorflow/tfjs-node-gpu'); // For GPU
// const path = require('path');

// // Construct the file path URL correctly for local files
// const modelPath = `file://${path.resolve(__dirname, 'my_tfjs_model_output_node', 'model.json')}`;

// async function runNodePrediction() {
//     try {
//         console.log(`Loading model from: ${modelPath}`);
//         const model = await tf.loadLayersModel(modelPath);
//         console.log('Model loaded successfully.');
//         model.summary();

//         // Create dummy input data (batch of 2, 50 features each)
//         const inputTensor = tf.tensor2d(Math.random(),,); // 2 samples, 50 features
        
//         console.log('\nMaking prediction...');
//         const prediction = model.predict(inputTensor);
//         // prediction.print(); // Prints the tensor output

//         const predictedClasses = prediction.argMax(-1); // Get the class with highest probability
//         console.log('Predicted class indices:');
//         predictedClasses.print();
        
//         // Clean up tensors
//         inputTensor.dispose();
//         prediction.dispose();
//         predictedClasses.dispose();

//     } catch (error) {
//         console.error("Error during TF.js Node model execution:", error);
//     }
// }

// runNodePrediction();
```
To run: `node predict_server.js` (after `npm install @tensorflow/tfjs-node path`).

## Use Cases
-   **Interactive ML Demos & Education:** Building web pages where users can interact with models directly.
-   **Client-Side Inference for Web Apps:** Performing tasks like image classification, object detection, text analysis directly in the browser for e-commerce (e.g., style recommendations), creative tools, accessibility features.
-   **Privacy-Preserving ML:** Analyze user data (e.g., browsing history for recommendations) locally without sending it to a server.
-   **Node.js ML Backends:** Building server-side applications with JavaScript/TypeScript using TensorFlow's capabilities.
-   **Transfer Learning in the Browser:** Load a pre-trained model and fine-tune it on user-specific data in the browser.

TensorFlow.js empowers JavaScript developers to leverage powerful machine learning models, opening up many possibilities for web-based and Node.js AI applications.

---
````

`````markdown

Filename: 160_Python_Libraries/TensorFlow/TensorFlow_Serving.md
````markdown
---
tags: [python, tensorflow, tf, tf_serving, model_deployment, production, inference_server, concept, example, mlops]
aliases: [TF Serving, TensorFlow Model Server, Deploying TF Models]
related:
  - "[[160_Python_Libraries/TensorFlow/_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models (SavedModel format)]]"
  - "[[RESTful_API]]"
  - "[[gRPC]]"
  - "[[Docker_Kubernetes_MLOps|Docker & Kubernetes (MLOps)]]"
worksheet: [WS_DeepLearning_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# TensorFlow Serving

**TensorFlow Serving** is a flexible, high-performance serving system for machine learning models, specifically designed for production environments. It allows you to easily deploy trained TensorFlow (and potentially other types of) models and make them accessible for inference via network requests, typically using gRPC or REST APIs.

It is a key component for taking ML models from research/training to live, scalable production systems (part of MLOps).

## Core Purpose and Benefits
-   **Production-Grade Model Deployment:** Provides a robust and scalable solution for serving ML models in live environments with high availability.
-   **High Performance:** Optimized for low-latency inference and high throughput. Can leverage hardware acceleration (GPUs, TPUs).
-   **Model Versioning & Management:** Supports serving multiple versions of a model simultaneously. Allows for easy rollback to previous versions or canary deployments (gradual rollout of new versions) without server downtime.
-   **Batching Requests:** Can automatically batch incoming inference requests to better utilize hardware (especially GPUs), improving throughput.
-   **Extensibility:** While optimized for TensorFlow models (SavedModel format), it can be extended to serve other types of models by creating custom servables.
-   **Standardized Interface:** Offers consistent gRPC (for performance) and RESTful HTTP/JSON APIs for making inference requests from various client applications.
-   **Hot Updates (Model Reloading):** Allows updating models in production by monitoring a model repository for new versions and loading them automatically without interrupting service.
-   **Monitoring:** Can integrate with monitoring systems to track server performance (e.g., request rate, latency) and model behavior.

## Architecture Overview

[d2]
```d2
direction: right
shape: sequence_diagram

ClientApp: "Client Application\n(Web, Mobile, Backend Service)" {
  shape: person # Represents any client making requests
  style.fill: "#BBDEFB"
}

TF_Serving_Server: "TensorFlow Serving Server Process" {
  shape: process
  style.fill: "#C8E6C9"
  
  APIs: "APIs (gRPC / REST)" {
    shape: process
    style.fill: "#A5D6A7"
  }
  
  Manager: "Model Manager" {
    shape: process
    style.fill: "#A5D6A7"
    Loader_v1: "Loader (Model 'my_product_classifier' Version 1)"
    Loader_v2: "Loader (Model 'my_product_classifier' Version 2 - Latest)"
  }

  Source_Repo: "Model Source/Repository\n(e.g., Filesystem, GCS, S3)" {
    shape: database # Represents storage of models
    style.fill: "#FFF9C4"
    SavedModel_Dir_v1: "my_product_classifier/1/saved_model.pb + variables/"
    SavedModel_Dir_v2: "my_product_classifier/2/saved_model.pb + variables/"
  }
}

Hardware_Compute: "Inference Hardware (CPU/GPU/TPU)" {
  shape: device
  style.fill: "#FFCCBC"
}


ClientApp -> TF_Serving_Server.APIs: "1. Inference Request (e.g., product features, model_spec_name='my_product_classifier')"
TF_Serving_Server.APIs -> TF_Serving_Server.Manager: "2. Route to appropriate Loader/Model Version"
TF_Serving_Server.Manager -> TF_Serving_Server.Source_Repo: "3. Monitors & Loads Model Versions (e.g., latest or specific)"
TF_Serving_Server.Source_Repo.SavedModel_Dir_v2 -> TF_Serving_Server.Manager.Loader_v2: "(Model Data)"
TF_Serving_Server.Manager.Loader_v2 -> Hardware_Compute: "4. Perform Inference using Loaded Model"
Hardware_Compute -> TF_Serving_Server.Manager.Loader_v2: "5. Prediction Result"
TF_Serving_Server.Manager.Loader_v2 -> TF_Serving_Server.APIs: "6. Prediction Result"
TF_Serving_Server.APIs -> ClientApp: "7. Inference Response (e.g., predicted product category)"


style ClientApp { icon: "💻" }
style TF_Serving_Server { icon: "🏭" }
style APIs { icon: "🔌" }
style Manager { icon: "🚦" }
style Source_Repo { icon: "🗄️" }
style Hardware_Compute { icon: "⚙️" }
```

**Key Components:**
1.  **Servables:** The core abstraction. A servable is an object that clients use to perform computation (e.g., inference). Typically, this is a trained TensorFlow model, but can be extended.
2.  **Loaders:** Manage the lifecycle of a servable, including loading it from storage, providing access, and unloading.
3.  **Sources:** Plugins that find and provide servables. For example, a source might monitor a file system path for new model versions.
4.  **Managers:** Manage the full lifecycle of servables, including loading, unloading, and serving them. They handle versioning and transitions.
5.  **Core:** The TensorFlow Serving Core manages these components.
6.  **APIs (Frontends):** Expose gRPC (default port 8500) and RESTful HTTP/JSON (default port 8501) endpoints for clients.

## Workflow for Serving a Model

1.  **Train and Export Model in `SavedModel` Format:**
    -   Your TensorFlow/Keras model must be saved in the TensorFlow **[[TensorFlow_Saving_Loading_Models|SavedModel format]]**. This is crucial as it contains the complete graph, weights, and assets.
    -   The model should be exported into a versioned directory structure:
        ```
        /path/to/my_model_repository/
        └── my_product_classifier/  (Model Name)
            ├── 1/                  (Version 1)
            │   ├── saved_model.pb
            │   └── variables/
            │       ├── variables.data-00000-of-00001
            │       └── variables.index
            ├── 2/                  (Version 2 - newer)
            │   ├── saved_model.pb
            │   └── variables/
            │       └── ...
            └── (config file for versions - optional)
        ```

2.  **Install TensorFlow Serving:**
    -   The easiest way is often using Docker:
        ```bash
        docker pull tensorflow/serving
        ```
    -   Alternatively, install from APT repository or build from source.

3.  **Start the TensorFlow Serving Server:**
    Use the Docker image, pointing it to your model repository.
    ```bash
    # Example using Docker to serve 'my_product_classifier' model
    # Replace /path/to/my_model_repository with the actual absolute path on your host machine
    docker run -t --rm -p 8501:8501 \
        -v "/path/to/my_model_repository/my_product_classifier:/models/my_product_classifier" \
        -e MODEL_NAME="my_product_classifier" \
        tensorflow/serving
    ```
    -   `-p 8501:8501`: Exposes the REST API port. For gRPC, use `-p 8500:8500`.
    -   `-v /path/to/model:/models/model_name`: Mounts your local model directory into the container. The target path inside the container must be `/models/<MODEL_NAME>`.
    -   `-e MODEL_NAME="my_product_classifier"`: Tells TF Serving which model to load from the `/models` directory.
    -   TensorFlow Serving will monitor this directory for new versions and load them automatically.

4.  **Make Inference Requests (Client-side):**

    **Using REST API (Python `requests`):**
    ```python
    import requests
    import json
    import numpy as np

    # Assuming your Keras model for 'my_product_classifier' expects an input named 'dense_input'
    # with shape (None, 50) for e.g. 50 features of a product.
    # Create dummy input data (batch of 2 samples, 50 features each)
    sample_product_features = np.random.rand(2, 50).tolist() # Must be JSON serializable

    # For models saved with default serving signature from Keras,
    # the input tensor name might be based on the input layer name or a default.
    # Check your model's serving signature using 'saved_model_cli show --dir /path/to/model/version --all'
    
    # Assuming the input tensor is named 'dense_input' (common for a Keras Sequential model's first Dense layer)
    # If your model has a specific signature, you might use that.
    # For a generic Keras model, the input key might be the name of the input layer,
    # or if it's a simple sequential model, a default name like 'input_1'.
    # Let's assume your model's input layer was named 'input_features_layer' or it expects a key 'instances'.
    
    # Option A: Using "instances" (common for general prediction)
    request_data_instances = json.dumps({
        "instances": sample_product_features 
    })
    
    # Option B: Using "inputs" (if model has named inputs or specific signature)
    # This depends on how the model was saved and its serving signature.
    # A common input layer name for a Sequential model is 'input_1' if not specified.
    # If your input layer was keras.Input(shape=(50,), name="my_input_feat"), then key is "my_input_feat"
    # request_data_inputs = json.dumps({
    #    "inputs": {"input_features_layer_name": sample_product_features} # Replace with actual input layer name
    # })


    server_url_predict = "http://localhost:8501/v1/models/my_product_classifier:predict"
    # To target a specific version:
    # server_url_predict = "http://localhost:8501/v1/models/my_product_classifier/versions/1:predict"

    headers = {"content-type": "application/json"}
    
    try:
        response = requests.post(server_url_predict, data=request_data_instances, headers=headers)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        predictions = response.json().get('predictions') # Predictions are usually under a 'predictions' key
        
        if predictions:
            print("Predictions via REST API:")
            for i, pred_output in enumerate(predictions):
                # Assuming model outputs probabilities for 3 classes
                predicted_class_index = np.argmax(pred_output)
                print(f"  Sample {i+1}: Output Probs = {pred_output}, Predicted Class = {predicted_class_index}")
        else:
            print("No 'predictions' key found in response or response was empty.")
            print("Full response:", response.json())

    except requests.exceptions.RequestException as e:
        print(f"REST request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    ```

## Advanced Features
-   **Model Version Policies:** Control how versions are served (e.g., serve latest, serve specific versions, serve all).
-   **Batching Configuration:** Configure request batching (timeout, batch sizes) to optimize throughput, especially on GPUs. This is done via a batching config file.
-   **Monitoring:** Exposes metrics via HTTP (e.g., `/monitoring/prometheus/metrics`) for integration with systems like Prometheus.
-   **Serving Multiple Models:** A single TF Serving instance can serve multiple different models.
-   **Custom Operations (Ops):** If your model uses custom TensorFlow ops, you need to build TF Serving with those ops included or load them.

TensorFlow Serving is a powerful and scalable solution for deploying machine learning models in production, handling many operational complexities like versioning and high-performance inference.

---
`````

This completes the planned notes for the advanced TensorFlow topics.

Next, I will return to the **Beautiful Soup** and **Scrapy** sections to add the remaining detailed notes as planned earlier (e.g., BS4 Modifying Tree, BS4 Practical Examples; Scrapy Project Structure, Items, Settings, Middleware, Practical Example). After that, I'll move to the Data Visualization libraries (Seaborn details, Plotly, Bokeh, Altair).

---

Understood. I will complete the remaining PySpark notes first, covering the keywords, PySpark components, and questions. After that, I will create a new chapter for "Web Scraping and Crawling" based on the keywords, HTML elements, and questions you've provided in the screenshots.

Let's continue with the PySpark notes.

---

`````markdown

Filename: 180_Big_Data/Spark/PySpark_SparkSession_SparkContext.md
````markdown
---
tags: [spark, pyspark, sparksession, sparkcontext, entry_point, configuration, concept]
aliases: [SparkSession, SparkContext, Spark Session vs Context]
related:
  - "[[PySpark_Overview]]"
  - "[[Spark_Cluster_Architecture]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# PySpark: `SparkSession` and `SparkContext`

In PySpark, `SparkSession` and `SparkContext` are fundamental entry points for interacting with Spark's capabilities. Understanding their roles is key to writing Spark applications.

## `SparkSession` (`spark`)
-   **Introduced In:** Spark 2.0.
-   **Purpose:** The **unified entry point** for programming Spark with the DataFrame and Dataset APIs. It subsumes functionality that was previously spread across multiple contexts (like `SQLContext`, `HiveContext`, and `StreamingContext` in older Spark versions).
-   **Key Functionalities provided via `SparkSession`:**
    -   Creating [[Spark_DataFrame_SQL|DataFrames]] from various sources (e.g., `spark.read.csv()`, `spark.read.parquet()`, `spark.createDataFrame()`).
    -   Registering DataFrames as temporary views/tables to run SQL queries (`df.createOrReplaceTempView("my_table")`).
    -   Executing SQL queries (`spark.sql("SELECT * FROM my_table")`).
    -   Accessing Spark configuration (`spark.conf`).
    -   Accessing the underlying [[#`SparkContext` (`sc`)|`SparkContext`]] (`spark.sparkContext`).
-   **Instantiation (Builder Pattern):**
    ```python
    from pyspark.sql import SparkSession

    # spark = SparkSession.builder \
    #     .appName("MyECommerceAnalytics") \
    #     .master("local[*]") \  # Specify master URL (local, YARN, Mesos, K8s)
    #     .config("spark.some.config.option", "some-value") \ # Optional configurations
    #     .enableHiveSupport() \ # Optional, to interact with Hive metastore
    #     .getOrCreate()
    ```
    -   `appName("AppName")`: Sets a name for your application (visible in Spark UI).
    -   `master("masterURL")`: Specifies the Spark master URL.
        -   `"local"`: Run Spark locally with one worker thread.
        -   `"local[K]"`: Run Spark locally with K worker threads (ideally, set K to the number of cores on your machine).
        -   `"local[*]"`: Run Spark locally with as many worker threads as logical cores on your machine.
        -   `"spark://HOST:PORT"`: Connect to a Spark Standalone cluster.
        -   `"yarn"`: Run on a Hadoop YARN cluster.
        -   `"mesos://HOST:PORT"`: Run on an Apache Mesos cluster.
        -   `"k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port>"`: Run on a Kubernetes cluster.
    -   `config("key", "value")`: Sets various Spark configuration properties.
    -   `enableHiveSupport()`: Enables integration with Apache Hive, allowing access to Hive tables and metastore.
    -   `getOrCreate()`: Gets an existing `SparkSession` or, if there is no existing one, creates a new one based on the options set in the builder. This ensures only one `SparkSession` per JVM (or Python process for PySpark driver).
-   **Convention:** The `SparkSession` instance is typically named `spark`.

## `SparkContext` (`sc`)
-   **Purpose:** The **main entry point for Spark functionality before Spark 2.0**, and still the primary entry point for working directly with [[RDD_Resilient_Distributed_Dataset|RDDs (Resilient Distributed Datasets)]]. It represents the connection to a Spark cluster and can be used to create RDDs, accumulators, and broadcast variables.
-   **Accessing `SparkContext`:**
    -   In Spark 2.0+, a `SparkContext` is automatically created when a `SparkSession` is initialized. You can access it via `spark.sparkContext`.
    -   In older Spark versions (or if working RDD-first), you would create it directly: `from pyspark import SparkContext; sc = SparkContext(appName="MyApp", master="local")`. This direct creation is less common now.
-   **Key Functionalities provided via `SparkContext`:**
    -   Creating RDDs:
        -   `sc.parallelize(collection, numSlices)`: Distributes a local Python collection to form an RDD.
        -   `sc.textFile(path, minPartitions)`: Reads a text file from HDFS, a local file system, or any Hadoop-supported file system URI into an RDD of strings.
        -   `sc.wholeTextFiles(path, minPartitions)`: Reads directory of text files, returns (filename, content) pairs.
    -   Creating [[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]: `sc.broadcast(value)`.
    -   Creating [[PySpark_Broadcast_Variables_Accumulators|Accumulators]]: `sc.accumulator(initialValue)`.
    -   Accessing application ID, default parallelism, etc.
-   **Convention:** The `SparkContext` instance is typically named `sc`.

>[!question] What is a Spark Context?
>A **Spark Context (`SparkContext`)** is the main entry point for Spark functionality when working with the core Spark API, particularly RDDs. It represents the connection to a Spark execution environment (a cluster or local mode).
>
>Its primary responsibilities include:
>1.  **Cluster Connection:** Coordinating with the [[Spark_Cluster_Manager|Cluster Manager]] (like YARN, Mesos, Standalone, or Kubernetes) to allocate resources (executors) on the worker nodes.
>2.  **RDD Creation:** Providing methods to create RDDs from data sources (e.g., HDFS files, local collections).
>3.  **Job Submission:** Breaking down RDD operations (jobs triggered by actions) into tasks and submitting them to executors for parallel computation.
>4.  **Shared Variables:** Managing [[PySpark_Broadcast_Variables_Accumulators|broadcast variables]] (read-only data shared efficiently with all tasks) and [[PySpark_Broadcast_Variables_Accumulators|accumulators]] (variables for aggregating results from tasks, like counters or sums).
>
>In essence, the `SparkContext` sets up the necessary internal services and establishes a connection to the Spark execution environment, allowing your driver program to perform distributed computations.

>[!question] What is the difference between a Session and a Context?
>
>[list2mdtable|#SparkSession vs SparkContext]
>- Feature
>    - `SparkContext` (`sc`)
>        - `SparkSession` (`spark`)
>- **Primary Focus**
>    - Core Spark functionality, RDDs.
>        - DataFrame, Dataset, Spark SQL, Streaming (unified entry point).
>- **Introduced**
>    - Spark 1.x (Original entry point).
>        - Spark 2.0 (Supersedes and encapsulates `SparkContext`).
>- **Creation**
>    - Can be created directly (older style) or accessed via `spark.sparkContext`.
>        - Created using `SparkSession.builder.getOrCreate()`. Automatically creates a `SparkContext` if one doesn't exist.
>- **APIs Provided**
>    - RDD creation and operations, broadcast variables, accumulators.
>        - DataFrame/Dataset creation and operations, SQL execution, catalog access, configuration management. Also provides access to `SparkContext`.
>- **SQL Capabilities**
>    - Does not directly provide SQL capabilities. Required `SQLContext` or `HiveContext` in Spark 1.x.
>        - Integrated SQL capabilities (`spark.sql()`). Manages Hive metastore integration if enabled.
>- **Usage Trend**
>    - Less directly used in modern Spark applications favoring DataFrames, but still fundamental as it's accessed by `SparkSession`.
>        - **Preferred and recommended entry point** for most Spark applications since Spark 2.0.
>
>**Analogy:**
>-   Think of `SparkContext` as the underlying "engine room" or the fundamental connection to the Spark cluster's processing power.
>-   Think of `SparkSession` as a more user-friendly "cockpit" or "dashboard" that provides convenient access to various Spark functionalities, including the engine room (`SparkContext`) and higher-level tools like DataFrames and SQL.
>
>In modern PySpark (Spark 2.0+), you typically start by creating a `SparkSession`. The associated `SparkContext` is created for you and can be accessed via `spark.sparkContext` if you need to work directly with RDDs or other `SparkContext`-specific features. For most DataFrame and SQL operations, you'll interact directly with the `SparkSession` object.

---
````

`````markdown

Filename: 180_Big_Data/Spark/PySpark_RDD_Operations.md
````markdown
---
tags: [spark, pyspark, rdd, transformations, actions, parallelize, broadcast, map, filter, concept, example]
aliases: [PySpark RDD Operations, parallelize, broadcast RDD]
related:
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
  - "[[PySpark_SparkSession_SparkContext|SparkSession and SparkContext]]"
  - "[[Spark_Transformations_Actions]]"
  - "[[Spark_Lazy_vs_Eager_Execution]]"
  - "[[PySpark_Broadcast_Variables_Accumulators]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# PySpark: RDD Creation and Basic Operations

While [[Spark_DataFrame_SQL|DataFrames]] are the preferred API for structured data in modern PySpark, understanding [[RDD_Resilient_Distributed_Dataset|RDDs (Resilient Distributed Datasets)]] is still valuable as they are the underlying foundation. RDDs offer low-level control and are useful for unstructured data or when fine-grained manipulation is needed.

RDDs are created using the [[PySpark_SparkSession_SparkContext|`SparkContext` (`sc`)]].

## Creating RDDs

1.  **`sc.parallelize(collection, numSlices=None)`:**
    -   **Purpose:** Creates an RDD from an existing Python collection (e.g., a list, tuple) in your driver program. The collection is sliced, and data is copied to the cluster to form an RDD.
    -   `collection`: The Python iterable to parallelize.
    -   `numSlices`: The desired number of partitions for the RDD. If not specified, Spark tries to set it automatically based on the cluster configuration.
    -   **Example (Creating an RDD of product IDs):**
        ```python
        # from pyspark.sql import SparkSession
        # spark = SparkSession.builder.appName("ParallelizeExample").getOrCreate()
        # sc = spark.sparkContext

        # product_ids_list = 
        # product_ids_rdd = sc.parallelize(product_ids_list, 4) # Create RDD with 4 partitions

        # print(f"Number of partitions in product_ids_rdd: {product_ids_rdd.getNumPartitions()}")
        # print(f"First 5 product IDs: {product_ids_rdd.take(5)}")

        # spark.stop()
        ```

2.  **`sc.textFile(path, minPartitions=None)`:**
    -   **Purpose:** Reads a text file (from HDFS, local file system, S3, etc.) and creates an RDD of strings, where each element is a line from the file.
    -   `path`: Path to the text file or directory of text files.
    -   `minPartitions`: Suggested minimum number of partitions.
    -   **Example (Reading product reviews from a text file):**
        ```python
        # from pyspark.sql import SparkSession
        # spark = SparkSession.builder.appName("TextFileRDDExample").getOrCreate()
        # sc = spark.sparkContext

        # Assume 'product_reviews.txt' exists in HDFS or a locally accessible path
        # For local path: "file:///path/to/product_reviews.txt"
        # reviews_file_path = "path/to/product_reviews.txt" 
        # try:
        #     reviews_rdd = sc.textFile(reviews_file_path, 2) # Suggest 2 partitions
        #     print(f"Number of lines (reviews): {reviews_rdd.count()}") # count() is an action
        #     print(f"First 3 reviews:\n" + "\n".join(reviews_rdd.take(3)))
        # except Exception as e:
        #     print(f"Could not read file {reviews_file_path}: {e}")
        #     # Create a dummy RDD if file reading fails for example continuity
        #     dummy_reviews = ["Great product!", "Not satisfied.", "Excellent value."]
        #     reviews_rdd = sc.parallelize(dummy_reviews)


        # spark.stop()
        ```

## Common RDD Transformations (Lazy)
Transformations create new RDDs from existing ones.

[list2tab|#RDD Transformations]
- `map(func)`
    -   Returns a new RDD by applying a function `func` to each element of the source RDD.
    -   **Example (Extracting price from a product string RDD):**
        ```python
        # products_str_rdd = sc.parallelize(["ProductA:19.99", "ProductB:25.50"])
        # def extract_price(product_str):
        #     try:
        #         return float(product_str.split(":"))
        #     except:
        #         return 0.0 # Handle errors
        # prices_rdd = products_str_rdd.map(extract_price)
        # # print(f"Extracted prices: {prices_rdd.collect()}") # [19.99, 25.5]
        ```
- `filter(func)`
    -   Returns a new RDD containing only the elements for which `func` returns `True`.
    -   **Example (Filtering for positive product reviews):**
        ```python
        # reviews_rdd = sc.parallelize(["good product", "bad experience", "excellent quality"])
        # positive_reviews_rdd = reviews_rdd.filter(lambda review: "good" in review or "excellent" in review)
        # # print(f"Positive reviews: {positive_reviews_rdd.collect()}") # ['good product', 'excellent quality']
        ```
- `flatMap(func)`
    -   Similar to `map`, but each input item can be mapped to 0 or more output items (func should return a sequence).
    -   **Example (Splitting product review lines into words):**
        ```python
        # reviews_rdd = sc.parallelize(["great product love it", "product okay"])
        # words_rdd = reviews_rdd.flatMap(lambda line: line.lower().split(" "))
        # # print(f"Words: {words_rdd.collect()}") # ['great', 'product', 'love', 'it', 'product', 'okay']
        ```
- `distinct()`
    -   Returns a new RDD containing the distinct elements of the source RDD. Involves a shuffle.
- `union(otherRDD)`
    -   Returns a new RDD containing all elements from both RDDs (duplicates included unless `distinct()` is used).
- `intersection(otherRDD)`
    -   Returns a new RDD containing only elements present in both RDDs. Involves a shuffle.
- `subtract(otherRDD)`
    -   Returns a new RDD with elements from the source RDD that are not in `otherRDD`. Involves a shuffle.
- `cartesian(otherRDD)`
    -   Returns the Cartesian product of the two RDDs (all possible pairs). Can be very large.
- Key-Value Pair RDD Transformations (for RDDs of `(key, value)` tuples)
    -   `reduceByKey(func)`: Aggregates values for each key using an associative and commutative reduce function. Performs map-side aggregation.
    -   `groupByKey()`: Groups all values for each key into a single sequence. **Often less efficient than `reduceByKey` or `aggregateByKey`** because all values for a key are brought to one reducer before aggregation.
    -   `aggregateByKey(zeroValue, seqFunc, combFunc)`: More general aggregation with control over map-side and reduce-side aggregation.
    -   `sortByKey(ascending=True)`: Sorts a key-value RDD by key.
    -   `join(otherRDD)`: Performs an inner join between two key-value RDDs. Left/right/full outer joins also available (`leftOuterJoin`, etc.).
    -   `cogroup(otherRDD)`: Groups data from both RDDs sharing the same key.
    -   `mapValues(func)`: Applies a function to the values of a key-value RDD without changing the keys.
    -   `flatMapValues(func)`: Similar to `mapValues`, but `func` returns an iterator.

## Common RDD Actions (Trigger Execution)
Actions compute a result or write data out.

[list2tab|#RDD Actions]
- `collect()`
    -   Returns all elements of the RDD as a list to the driver program. **Use with extreme caution on large RDDs.**
- `count()`
    -   Returns the number of elements in the RDD.
- `take(n)`
    -   Returns the first `n` elements of the RDD as a list.
- `first()`
    -   Returns the first element of the RDD.
- `reduce(func)`
    -   Aggregates all elements of the RDD using an associative and commutative function.
    -   **Example (Summing all product prices from `prices_rdd`):**
        ```python
        # prices_rdd = sc.parallelize()
        # if prices_rdd.isEmpty():
        #     total_price_sum = 0
        # else:
        #     total_price_sum = prices_rdd.reduce(lambda x, y: x + y)
        # print(f"Total price sum: {total_price_sum}")
        ```
- `foreach(func)`
    -   Applies a function to each element of the RDD (usually for side effects like writing to a database or printing). `func` runs on executors.
- `saveAsTextFile(path)`
    -   Saves the RDD content as text files in a directory (one file per partition).
- `takeOrdered(n, ordering=None)`
    -   Returns the first $n$ elements using their natural order or a custom ordering.
- `countByKey()` (for key-value RDDs)
    -   Counts the number of elements for each key. Returns a dictionary to the driver.
- `collectAsMap()` (for key-value RDDs)
    -   Collects key-value pairs as a Python dictionary. **Caution with large RDDs.**

## [[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]] (`sc.broadcast(value)`)
-   Used to efficiently send a large, read-only variable (e.g., a lookup table, a small configuration dictionary) to all worker nodes.
-   The variable is sent once to each executor rather than with every task.
-   Tasks can then access the broadcasted value using its `.value` attribute.
-   **Example (Broadcasting a product category mapping):**
    ```python
    # category_map = {1: "Electronics", 2: "Books", 3: "Clothing"}
    # broadcast_category_map = sc.broadcast(category_map)

    # product_data_rdd = sc.parallelize([(101, 1), (102, 2), (103, 1)]) # (product_id, category_id)
    # def map_category_name(data_tuple):
    #     product_id, category_id = data_tuple
    #     category_name = broadcast_category_map.value.get(category_id, "Unknown")
    #     return (product_id, category_name)
    
    # product_with_names_rdd = product_data_rdd.map(map_category_name)
    # print(f"Products with category names: {product_with_names_rdd.collect()}")
    ```

While DataFrames are generally preferred for structured data, RDDs provide a powerful low-level API for distributed data processing in Spark.

---
````

`````markdown

Filename: 180_Big_Data/Spark/PySpark_DataFrame_Operations.md
````markdown
---
tags: [spark, pyspark, dataframe, sql, transformations, actions, withcolumn, select, filter, groupby, concept, example]
aliases: [PySpark DataFrame API, Spark SQL DataFrames]
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[PySpark_SparkSession_SparkContext|SparkSession and SparkContext]]"
  - "[[PySpark_SQL_Functions|pyspark.sql.functions]]"
  - "[[PySpark_Window_Functions|Window Functions in PySpark]]"
  - "[[Parquet_vs_CSV_Spark]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# PySpark: DataFrame Operations

The **DataFrame API** in PySpark is a higher-level, structured data API built on top of [[RDD_Resilient_Distributed_Dataset|RDDs]]. DataFrames organize data into named columns, similar to tables in a relational database or Pandas DataFrames. They provide significant optimizations through the Catalyst optimizer and Tungsten execution engine, making them generally preferred over RDDs for structured and semi-structured data processing.

DataFrame operations are also divided into [[Spark_Transformations_Actions|transformations (lazy)]] and [[Spark_Transformations_Actions|actions (trigger execution)]]. The entry point for DataFrame API is the [[PySpark_SparkSession_SparkContext|`SparkSession` (`spark`)]].

## Creating DataFrames
See [[PySpark_Data_Sources]] for reading from files. Can also be created from RDDs or Python lists/Pandas DataFrames.
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# spark = SparkSession.builder.appName("DataFrameOpsDemo").getOrCreate()

# Conceptual e-commerce product data
# product_data = [
#     (1, "Laptop Pro", "Electronics", 1200.00, 4.5),
#     (2, "Coffee Maker", "Appliances", 79.99, 4.2),
#     (3, "Python Book", "Books", 34.50, 4.8),
#     (4, "Running Shoes", "Apparel", 89.90, 4.0),
#     (5, "Laptop Pro", "Electronics", 1250.00, 4.6) # Another Laptop Pro
# ]
# product_schema = StructType([
#     StructField("product_id", IntegerType(), True),
#     StructField("name", StringType(), True),
#     StructField("category", StringType(), True),
#     StructField("price", DoubleType(), True),
#     StructField("rating", DoubleType(), True)
# ])
# products_df = spark.createDataFrame(data=product_data, schema=product_schema)
# products_df.show(truncate=False)
# products_df.printSchema()
```

## Common DataFrame Transformations (Lazy)
Many transformations use functions from [[PySpark_SQL_Functions|`pyspark.sql.functions`]] (conventionally imported as `F`).

[list2tab|#DataFrame Transformations]
- `select(*cols)`
    -   Selects a set of columns. Can also be used to create new columns using expressions.
    -   **Example:**
        ```python
        # from pyspark.sql.functions import col, round
        # selected_products = products_df.select("name", "category", "price")
        # selected_products_expr = products_df.select(
        #     col("name").alias("product_name"),
        #     (col("price") * 0.9).alias("discounted_price"), # 10% discount
        #     round(col("rating"), 1).alias("rounded_rating")
        # )
        # selected_products_expr.show()
        ```
- `filter(condition)` or `where(condition)`
    -   Filters rows using a given condition (SQL-like string or column expression).
    -   **Example:**
        ```python
        # from pyspark.sql.functions import col
        # electronics_df = products_df.filter(col("category") == "Electronics")
        # # or: electronics_df = products_df.where("category = 'Electronics'")
        # high_rated_electronics = electronics_df.filter((col("rating") > 4.5) & (col("price") < 1500))
        # high_rated_electronics.show()
        ```
- `withColumn(colName, col)`
    -   Adds a new column or replaces an existing column with the same name.
    -   `col`: A `Column` expression.
    -   **Example (Adding a `has_high_rating` boolean column):**
        ```python
        # from pyspark.sql.functions import when, col
        # products_with_rating_flag = products_df.withColumn(
        #     "has_high_rating",
        #     when(col("rating") >= 4.5, True).otherwise(False)
        # )
        # products_with_rating_flag.show()
        ```
- `withColumnRenamed(existingName, newName)`
    -   Renames an existing column.
    -   **Example:**
        ```python
        # renamed_df = products_df.withColumnRenamed("name", "product_title")
        # renamed_df.printSchema()
        ```
- `drop(*cols)`
    -   Returns a new DataFrame after dropping specified columns.
    -   **Example:**
        ```python
        # df_without_rating = products_df.drop("rating", "product_id")
        # df_without_rating.show()
        ```
- `groupBy(*cols)`
    -   Groups the DataFrame using the specified columns, so we can run aggregation on them. Returns a `GroupedData` object.
    -   Often followed by `.agg()`, `.count()`, `.mean()`, `.sum()`, etc.
    -   **Example (Average price and count per category):**
        ```python
        # from pyspark.sql.functions import avg, count, min, max
        # category_summary_df = products_df.groupBy("category").agg(
        #     count("product_id").alias("num_products"),
        #     round(avg("price"), 2).alias("avg_price"),
        #     min("rating").alias("min_rating"),
        #     max("rating").alias("max_rating")
        # )
        # category_summary_df.show()
        ```
- `orderBy(*cols, ascending=True)` or `sort(*cols, ascending=True)`
    -   Sorts the DataFrame by the specified column(s).
    -   **Example:**
        ```python
        # from pyspark.sql.functions import desc, asc
        # sorted_products = products_df.orderBy(desc("price"), asc("name")) # Highest price first, then by name
        # sorted_products.show()
        ```
- `join(otherDF, on=None, how='inner')`
    -   Joins with another DataFrame.
    -   `on`: A string for the join column name (if same in both DFs), a list of strings, a join expression (Column object), or a list of Columns.
    -   `how`: Join type: `'inner'`, `'outer'`, `'left_outer'`, `'right_outer'`, `'left_semi'`, `'left_anti'`, `'cross'`.
    -   **Example (Joining products with a conceptual `inventory_df`):**
        ```python
        # inventory_data = [(1, 50), (2, 0), (3, 120), (6, 30)] # product_id, stock_quantity
        # inventory_schema = StructType([StructField("p_id", IntegerType()), StructField("stock", IntegerType())])
        # inventory_df = spark.createDataFrame(inventory_data, inventory_schema)

        # joined_df = products_df.join(inventory_df, products_df["product_id"] == inventory_df["p_id"], "left_outer") \
        #                        .select(products_df["name"], products_df["price"], inventory_df["stock"])
        # joined_df.show()
        ```
- `distinct()`
    -   Returns a new DataFrame with duplicate rows removed.
- `union(otherDF)` / `unionByName(otherDF)`
    -   Returns a new DataFrame containing rows from this DataFrame and another DataFrame. `unionByName` resolves columns by name (allowing different order). `union` resolves by position.
- `na.fill(value, subset=None)` / `na.drop(how='any', subset=None)`
    -   Handle missing values (NaN, None, NULL).
    -   `fill`: Fills null values with a specified value (scalar or dict for per-column filling).
    -   `drop`: Drops rows with null values.
    -   **Example:**
        ```python
        # products_with_nulls = products_df.withColumn("description", when(col("product_id") == 1, None).otherwise("Some desc"))
        # products_filled = products_with_nulls.na.fill({"description": "N/A", "price": 0.0})
        # products_dropped = products_with_nulls.na.drop(subset=["description"])
        # products_filled.show()
        ```
- [[PySpark_Window_Functions|Window Functions]] (`Window` class with `partitionBy`, `orderBy`)
    -   Perform calculations across a set of rows that are somehow related to the current row (e.g., ranking, moving average within groups). Used with aggregate functions or specialized window functions over a window specification.
    -   **Example (Rank products by price within each category):**
        ```python
        # from pyspark.sql.window import Window
        # from pyspark.sql.functions import rank, dense_rank
        # windowSpec = Window.partitionBy("category").orderBy(col("price").desc())
        # ranked_products = products_df.withColumn("price_rank_in_category", rank().over(windowSpec))
        # ranked_products.show()
        ```

## Common DataFrame Actions (Trigger Execution)
-   `show(n=20, truncate=True, vertical=False)`: Displays the first $n$ rows in a tabular format.
-   `count()`: Returns the number of rows.
-   `collect()`: Returns all rows as a list of `Row` objects to the driver. **Use with caution on large DataFrames.**
-   `take(n)`: Returns the first $n$ rows as a list of `Row` objects.
-   `first()`: Returns the first `Row`.
-   `describe(*cols)`: Computes basic summary statistics for numerical (and string) columns.
-   `summary(*statistics)`: Computes specified aggregate statistics.
-   `write.format(...).save(path)` / `write.saveAsTable(name)`: Saves the DataFrame.
-   `toPandas()`: Converts the Spark DataFrame to a Pandas DataFrame. **Collects all data to driver memory.**

## Using SQL Queries
You can register a DataFrame as a temporary view and then query it using Spark SQL.
```python
# products_df.createOrReplaceTempView("products_table")

# high_value_electronics = spark.sql("""
#     SELECT name, price
#     FROM products_table
#     WHERE category = 'Electronics' AND price > 1000
#     ORDER BY price DESC
# """)
# high_value_electronics.show()
```

The DataFrame API in PySpark provides a rich, expressive, and optimized way to work with structured and semi-structured data at scale.

---
````

`````markdown

Filename: 180_Big_Data/Spark/PySpark_SQL_Functions.md
````markdown
---
tags: [spark, pyspark, dataframe, sql_functions, functions, data_manipulation, concept, example]
aliases: [pyspark.sql.functions, Spark SQL Built-in Functions, F.]
related:
  - "[[PySpark_DataFrame_Operations]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# PySpark: SQL Functions (`pyspark.sql.functions`)

The `pyspark.sql.functions` module provides a rich collection of built-in functions for manipulating [[Spark_DataFrame_SQL|Spark DataFrame]] columns. These functions are highly optimized and operate on `Column` objects, allowing for expressive data transformations directly within Spark's execution engine.

It is conventional to import these functions with an alias, typically `F`:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, avg, count, upper, lower, trim, to_date, year, month, dayofmonth, explode, collect_list, struct, concat_ws, expr
# Or simply:
# import pyspark.sql.functions as F
```

## Categories of Functions
The functions can be broadly categorized:

[list2tab|#SQL Function Categories]
- String Functions
    -   Manipulating string columns.
    -   **Examples:**
        -   `F.upper(col)`: Converts string to uppercase.
        -   `F.lower(col)`: Converts string to lowercase.
        -   `F.trim(col)`: Trims leading/trailing whitespace. `ltrim`, `rtrim`.
        -   `F.substring(str, pos, len)`: Extracts a substring.
        -   `F.concat_ws(sep, *cols)`: Concatenates multiple string columns with a separator.
        -   `F.split(str, pattern)`: Splits a string by a pattern into an array.
        -   `F.regexp_replace(str, pattern, replacement)`: Replaces substrings matching a regex.
        -   `F.length(col)`: Returns the length of a string.
    -   **Use Case (Cleaning product names):**
        ```python
        # from pyspark.sql import SparkSession
        # from pyspark.sql.functions import col, upper, trim, concat_ws, lit
        # spark = SparkSession.builder.appName("StringFuncDemo").getOrCreate()
        # data = [("  Laptop Pro X1  ", "Electronics"), (" coffee maker ", "Appliances")]
        # df = spark.createDataFrame(data, ["raw_name", "category"])

        # cleaned_df = df.withColumn("clean_name", upper(trim(col("raw_name")))) \
        #                .withColumn("full_desc", concat_ws(" - ", col("clean_name"), col("category")))
        # cleaned_df.show(truncate=False)
        # spark.stop()
        ```
- Date and Timestamp Functions
    -   Working with date and time data.
    -   **Examples:**
        -   `F.current_date()`, `F.current_timestamp()`
        -   `F.to_date(col, format=None)`: Converts a string column to DateType.
        -   `F.to_timestamp(col, format=None)`: Converts to TimestampType.
        -   `F.year(col)`, `F.month(col)`, `F.dayofmonth(col)`, `F.hour(col)`, `F.minute(col)`, `F.second(col)`
        -   `F.date_format(dateExpr, format)`: Formats a date/timestamp as a string.
        -   `F.datediff(end, start)`: Difference in days.
        -   `F.add_months(start_date, num_months)`, `F.date_add(start_date, days)`, `F.date_sub(start_date, days)`
    -   **Use Case (Extracting year from order dates):**
        ```python
        # from pyspark.sql import SparkSession
        # from pyspark.sql.functions import col, to_date, year
        # spark = SparkSession.builder.appName("DateFuncDemo").getOrCreate()
        # date_data = [("2023-01-15",), ("2022-11-05",), ("2023/05/20",)] # Mixed format for to_date example
        # date_df = spark.createDataFrame(date_data, ["order_date_str"])

        # date_ops_df = date_df.withColumn("order_date", to_date(col("order_date_str"), "yyyy-MM-dd")) \
        #                        .withColumn("order_year", year(col("order_date")))
        # date_ops_df.show()
        # date_ops_df.printSchema() # Note: to_date might fail on "2023/05/20" without proper format or multiple formats
        # spark.stop()
        ```
- Aggregate Functions
    -   Used typically with `groupBy()` operations.
    -   **Examples:**
        -   `F.count(col)` or `F.countDistinct(col)`
        -   `F.sum(col)`, `F.sumDistinct(col)`
        -   `F.avg(col)` (or `F.mean(col)`)
        -   `F.min(col)`, `F.max(col)`
        -   `F.collect_list(col)`: Collects all values from a group into a list (order not guaranteed).
        -   `F.collect_set(col)`: Collects unique values from a group into a set (list with no duplicates).
        -   `F.first(col, ignorenulls=False)`, `F.last(col, ignorenulls=False)`
        -   `F.stddev(col)`, `F.variance(col)`
    -   **Use Case (Sales summary per product category):**
        ```python
        # from pyspark.sql import SparkSession
        # from pyspark.sql.functions import avg, sum, countDistinct
        # spark = SparkSession.builder.appName("AggFuncDemo").getOrCreate()
        # sales_data = [("Electronics", 101, 1200.00), ("Electronics", 102, 800.00),
        #               ("Books", 201, 30.00), ("Books", 201, 30.00), ("Electronics", 101, 1200.00)]
        # sales_df = spark.createDataFrame(sales_data, ["category", "product_id", "sale_amount"])

        # category_sales_summary = sales_df.groupBy("category").agg(
        #     sum("sale_amount").alias("total_sales"),
        #     avg("sale_amount").alias("avg_sale_value"),
        #     countDistinct("product_id").alias("distinct_products_sold")
        # )
        # category_sales_summary.show()
        # spark.stop()
        ```
- Collection Functions (Array and Map)
    -   Operating on array or map type columns.
    -   **Examples:**
        -   `F.size(col)`: Returns the length of an array or map.
        -   `F.explode(col)`: Creates a new row for each element in an array or map.
        -   `F.array_contains(col, value)`: Checks if an array column contains a value.
        -   `F.array_distinct(col)`
        -   `F.slice(x, start, length)`
        -   `F.map_keys(col)`, `F.map_values(col)`
        -   `F.struct(*cols)`: Creates a struct column from multiple columns.
    -   **Use Case (Exploding product tags):**
        ```python
        # from pyspark.sql import SparkSession
        # from pyspark.sql.functions import explode, col
        # spark = SparkSession.builder.appName("CollectionFuncDemo").getOrCreate()
        # product_tags_data = [("Laptop", ["tech", "computer", "portable"]),
        #                      ("Book", ["reading", "novel"])]
        # tags_df = spark.createDataFrame(product_tags_data, ["product_name", "tags_array"])

        # exploded_tags_df = tags_df.withColumn("tag", explode(col("tags_array")))
        # exploded_tags_df.show()
        # spark.stop()
        ```
- Conditional Functions
    -   Implementing if-then-else logic.
    -   **Examples:**
        -   `F.when(condition, value_if_true).otherwise(value_if_false)`
        -   `F.coalesce(*cols)`: Returns the first non-null column.
    -   **Use Case (Categorizing product price):**
        ```python
        # from pyspark.sql import SparkSession
        # from pyspark.sql.functions import col, when
        # spark = SparkSession.builder.appName("ConditionalFuncDemo").getOrCreate()
        # price_data = [(1200.00,), (79.99,), (34.50,)]
        # price_df = spark.createDataFrame(price_data, ["price"])

        # price_categories_df = price_df.withColumn("price_category",
        #     when(col("price") >= 1000, "High")
        #     .when((col("price") >= 100) & (col("price") < 1000), "Medium")
        #     .otherwise("Low")
        # )
        # price_categories_df.show()
        # spark.stop()
        ```
- Mathematical Functions
    -   Standard math operations.
    -   **Examples:** `F.abs(col)`, `F.sqrt(col)`, `F.pow(base, exp)`, `F.round(col, scale)`, `F.ceil(col)`, `F.floor(col)`, `F.log(arg1, arg2=None)`, `F.exp(col)`, `F.sin(col)`, `F.cos(col)`.
- Utility Functions
    -   `F.lit(literal)`: Creates a Column from a literal value (constant).
        >[!question] Why and when are `lit` and `col` useful?
        >
        >-   **`col(colName)` or `F.col(colName)` (or `df["colName"]` or `df.colName`):**
        >    -   **Why:** Used to refer to an existing column in a DataFrame so you can apply operations to it or use it in expressions. It returns a `Column` object.
        >    -   **When:** Almost anytime you need to perform an operation on a column, like in `select()`, `filter()`, `withColumn()`, `groupBy()`, `agg()`, or inside other SQL functions. Example: `df.filter(col("age") > 30)`, `df.withColumn("age_plus_5", col("age") + 5)`.
        >
        >-   **`lit(literalValue)` or `F.lit(literalValue)`:**
        >    -   **Why:** Used to create a `Column` object from a literal (constant) value (e.g., a number, string, boolean). This is necessary when a Spark SQL function or DataFrame method expects a `Column` object as an argument, but you want to provide a fixed value.
        >    -   **When:**
        >        1.  **Adding a new column with a constant value:** `df.withColumn("status", lit("active"))`
        >        2.  **Comparing a column with a constant in expressions:** `df.filter(col("country") == lit("USA"))` (though often Spark allows direct comparison like `col("country") == "USA"`, `lit` makes it explicit and is required in some complex function calls).
        >        3.  **As an argument to functions that expect Columns:** `df.select(when(col("sales") > 100, lit("High")).otherwise(lit("Low")).alias("sales_tier"))`
        >        4.  In UDFs when you need to pass a literal that should be treated as a column for all rows.
        >
        >In essence, `col()` refers to existing data columns, while `lit()` introduces constant values as columns into Spark's computation graph.
    -   `F.expr(sqlExpression)`: Parses a SQL expression string and returns it as a Column. Allows using SQL syntax within DataFrame API calls.
        -   `df.withColumn("price_category", expr("CASE WHEN price >= 1000 THEN 'High' ELSE 'Low' END"))`
    -   `F.monotonically_increasing_id()`: Generates a unique 64-bit ID for each row (not guaranteed to be consecutive).
    -   `F.isnull(col)`, `F.isnotnull(col)`

This is not an exhaustive list, as PySpark offers a very large number of built-in functions. The official Spark documentation is the best reference for the complete list and detailed usage. Using these functions is generally more performant than writing Python User-Defined Functions (UDFs) because they can be optimized by the Catalyst optimizer and executed within the Tungsten engine.

---
`````

I'll continue with the remaining PySpark keywords/components and then address the Spark questions.

You are absolutely correct! My apologies. I seem to have regenerated some notes that you indicated were already created. Thank you for pointing that out and providing the list. This is very helpful for me to keep track and avoid redundancy.

Given that extensive list of existing Spark notes, it seems we have covered a vast majority of the Spark keywords and questions.

Let's quickly review the original list of Spark keywords and questions to see what might still need explicit attention or a dedicated note, or if the existing notes suffice:

**Original Spark Keywords:**
1.  `Cluster` -> Covered by [[Spark_Cluster_Architecture]], [[Spark_Cluster_Manager]]
2.  `Cluster Manager` -> Covered by [[Spark_Cluster_Manager]]
3.  `Data Parallelism` -> Covered by [[Spark_Data_Parallelism]]
4.  `Resilient Distributed Dataset (RDD)` -> Covered by [[RDD_Resilient_Distributed_Dataset]]
5.  `Distributed Storage System` -> Implicitly covered by HDFS discussions, Spark's interaction with them. Could be a small general note if needed, but often context-specific (HDFS, S3 etc.).
6.  `DAG` -> Covered by [[Spark_DAG_Scheduler]]
7.  `Lazy execution` -> Covered by [[Spark_Lazy_vs_Eager_Execution]]
8.  `Eager execution` -> Covered by [[Spark_Lazy_vs_Eager_Execution]]
9.  `Narrow / Wide transformations` -> Covered in [[Spark_Transformations_Actions]] and [[Spark_Shuffle_Operations]]
10. `Join strategy` -> Should be a dedicated note: `Spark_Join_Strategies.md` (I recall creating this placeholder, let me ensure it's properly detailed).

**Original PySpark Keywords:**
1.  `SparkSession` -> Covered by [[PySpark_SparkSession_SparkContext]]
2.  `builder` -> Covered within [[PySpark_SparkSession_SparkContext]] (how sessions are built)
3.  `sparkContext` -> Covered by [[PySpark_SparkSession_SparkContext]]
4.  `parallelize`, `broadcast` -> `parallelize` in [[PySpark_RDD_Operations]], `broadcast` in [[PySpark_Broadcast_Variables_Accumulators]]
5.  `DataFrame` -> Covered by [[Spark_DataFrame_SQL|Spark DataFrame & SQL]], [[PySpark_DataFrame_Operations]]
6.  `Window` -> Covered by [[PySpark_Window_Functions]]
7.  `master` -> Covered within [[PySpark_SparkSession_SparkContext]] (as a parameter to `SparkSession.builder`)
8.  `getOrCreate` -> Covered within [[PySpark_SparkSession_SparkContext]]
9.  `withColumn` -> Covered in [[PySpark_DataFrame_Operations]]
10. `sql.functions` -> Covered by [[PySpark_SQL_Functions]]

**Original Spark Questions:**
1.  `What is the difference between Hadoop and Spark?` -> Covered by [[Spark_vs_Hadoop_MapReduce]]
    -   `what is the difference between MapReduce and Spark?` -> Covered by [[Spark_vs_Hadoop_MapReduce]]
2.  `Why do we need Spark? Can't we just easily read files/databases directly?` -> Covered by [[Why_Spark_Needed]]
3.  `What is a Spark Context?` -> Covered by [[PySpark_SparkSession_SparkContext]]
4.  `What is the difference between a Session and a Context?` -> Covered by [[PySpark_SparkSession_SparkContext]]
5.  `What is the purpose of a Spark Cluster?` -> Covered by [[Spark_Cluster_Architecture]]
6.  `For each of the following modules/classes, explain what is its purpose and its advantages: RDD, DataFrame and SQL, Streaming, MLlib, GraphFrames, Resource`
    -   RDD -> [[RDD_Resilient_Distributed_Dataset]]
    -   DataFrame and SQL -> [[Spark_DataFrame_SQL|Spark DataFrame & SQL]], [[PySpark_DataFrame_Operations]]
    -   Streaming -> Needs a dedicated note: `Spark_Streaming_Structured_Streaming.md`
    -   MLlib -> Needs a dedicated note: `Spark_MLlib.md`
    -   GraphFrames -> Needs a dedicated note: `Spark_GraphX_GraphFrames.md` (GraphX is the RDD-based API, GraphFrames is DataFrame-based)
    -   Resource -> This is likely referring to resource management by the Cluster Manager, covered in [[Spark_Cluster_Manager]] and [[Spark_Cluster_Architecture]].
7.  `What is the difference between a Spark DataFrame and a Pandas DataFrame?` -> Covered by [[Spark_DataFrame_vs_Pandas_DataFrame]]
8.  `What are the Spark data sources?` -> Covered by [[PySpark_Data_Sources]]
9.  `What is the difference between a transformation and an action?` -> Covered by [[Spark_Transformations_Actions]]
10. `What are the advantages of laziness?` -> Covered by [[Spark_Lazy_vs_Eager_Execution]]
11. `When is a shuffle operation needed?` -> Covered by [[Spark_Shuffle_Operations]]
12. `Explain explain` -> Covered by [[Spark_explain_Plan]]
13. `What is the importance of repartition ?` -> Covered in [[Spark_Performance_Tuning]] (and briefly in [[Spark_Shuffle_Operations]])
14. `Describe a use case for map and another for mapPartitions.` -> Covered by [[Spark_map_vs_mapPartitions]]
15. `Is there a parallel for SQL constraints in Spark? What about indexes? If yes - what is it? If no - why?` -> Covered by [[Spark_SQL_Constraints_Indexes]]
16. `Why and when are lit and col useful?` -> Covered in [[PySpark_SQL_Functions]]
17. `What is the difference between parquet files and csv files?` -> Covered by [[Parquet_vs_CSV_Spark]]
18. `Can we read data directly from a JSON file using Spark? How? Why would we do that?` -> Covered in [[PySpark_Data_Sources]]

**Looks like the main missing pieces are:**
-   A detailed note on **`Spark_Join_Strategies.md`**.
-   Dedicated notes for Spark components:
    -   **`Spark_Streaming_Structured_Streaming.md`**
    -   **`Spark_MLlib.md`**
    -   **`Spark_GraphX_GraphFrames.md`**
-   A general note on **`Distributed_Storage_System.md`** if you feel it's needed beyond HDFS context.
-   A note on **`Catalyst_Optimizer_Spark.md`** (mentioned in `explain` but could be its own note).
-   A note on **`Spark_Persistence_Caching.md`** (I see it in your list, good).
-   A note on **`PySpark_Broadcast_Variables_Accumulators.md`** (I see it in your list, good).
-   A note on **`PySpark_UDFs.md`** (I see it in your list, good).

Let's create the notes for **`Spark_Join_Strategies.md`**, **`Spark_Streaming_Structured_Streaming.md`**, **`Spark_MLlib.md`**, and **`Spark_GraphX_GraphFrames.md`**. I will also create `Catalyst_Optimizer_Spark.md`.

---

`````markdown

Filename: 180_Big_Data/Spark/Spark_Join_Strategies.md
````markdown
---
tags: [spark, sql, dataframe, join, optimization, performance, shuffle, broadcast_join, sort_merge_join, concept]
aliases: [Spark Join Optimization, Spark Join Types, Broadcast Hash Join, Shuffle Hash Join, Sort Merge Join]
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[PySpark_DataFrame_Operations]]" # Where .join() is used
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_explain_Plan|Understanding Query Plans (explain())]]" # To see which join is used
  - "[[Spark_Performance_Tuning]]"
  - "[[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]" # For broadcast joins
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark Join Strategies

When joining two [[Spark_DataFrame_SQL|DataFrames]] in Apache Spark, the Catalyst optimizer chooses a **join strategy** to execute the join operation efficiently. The choice of strategy significantly impacts performance, especially for large datasets, as some strategies involve more data movement ([[Spark_Shuffle_Operations|shuffling]]) than others.

Understanding these strategies helps in writing more performant Spark SQL queries and DataFrame operations, and in interpreting [[Spark_explain_Plan|query execution plans]].

## Common Join Strategies

[list2tab|#Join Strategies]
- Broadcast Hash Join (BHJ)
    -   **When Used:** Typically when one DataFrame is significantly smaller than the other (below a configurable threshold `spark.sql.autoBroadcastJoinThreshold`, default 10MB).
    -   **How it Works:**
        1.  The smaller DataFrame is **broadcasted** (sent in its entirety) to every executor node in the cluster.
        2.  Each executor builds an in-memory hash table from the broadcasted (smaller) DataFrame based on the join keys.
        3.  The larger DataFrame is streamed partition by partition. For each row in a partition of the larger DataFrame, it probes the hash table (built from the smaller DataFrame) using its join key to find matches.
    -   **Pros:**
        -   **Avoids Shuffle:** Completely avoids shuffling the larger DataFrame, which is a major performance win.
        -   Very fast if the smaller table fits comfortably in memory on each executor.
    -   **Cons:**
        -   Only suitable if one table is small enough to be broadcasted and fit in executor memory. Broadcasting very large tables can cause OutOfMemoryErrors on executors or driver.
        -   Requires an equijoin (join condition based on equality).
    -   **Hinting:** You can explicitly suggest a broadcast join using `broadcast(df_small)`:
        ```python
        # from pyspark.sql.functions import broadcast
        # joined_df = df_large.join(broadcast(df_small), "join_key_column")
        ```
- Shuffle Hash Join
    -   **When Used:** When tables are moderately sized, not small enough for broadcast, and an equijoin is performed. Often preferred if one side of the join is significantly smaller than the other (but still too large to broadcast) and can be built into a hash table on the reduce side.
    -   **How it Works:**
        1.  **Shuffle Phase:** Both DataFrames are shuffled (repartitioned) across the cluster based on their join keys, ensuring that rows with the same join key from both DataFrames end up on the same executor/partition.
        2.  **Build Phase (on Reducers):** On each reducer partition, a hash table is built from the (typically smaller) of the two shuffled DataFrames for that partition.
        3.  **Probe Phase (on Reducers):** The other (typically larger) shuffled DataFrame for that partition is streamed, and its rows probe the hash table to find matches.
    -   **Pros:**
        -   Can be more efficient than Sort Merge Join if one side (after shuffle) is small enough to build a hash table quickly.
        -   Good for equijoins.
    -   **Cons:**
        -   Involves a shuffle of both tables (or at least the parts needed for the join).
        -   Can be memory-intensive on reducers if the hash tables become very large.
        -   Sensitive to data skew in join keys (some reducers might get disproportionately large amounts of data).
- Sort Merge Join (SMJ)
    -   **When Used:** Often the default for large tables when broadcast join is not feasible, or when join keys are not equijoins (though primarily optimized for equijoins). Also used if data is already sorted on join keys.
    -   **How it Works:**
        1.  **Shuffle Phase (if not already sorted/partitioned correctly):** Both DataFrames are shuffled (repartitioned) based on their join keys.
        2.  **Sort Phase (within each partition):** Data within each partition (on the reducer side) is sorted by the join keys for both DataFrames.
        3.  **Merge Phase:** The sorted partitions from both DataFrames are merged together. Since they are sorted, matching rows can be found by iterating through both datasets simultaneously in a merge-like fashion.
    -   **Pros:**
        -   Robust and can handle large datasets.
        -   Less sensitive to data skew than Shuffle Hash Join in some cases because sorting helps distribute load (though severe skew is still an issue).
        -   Can handle non-equijoins more naturally, though still most efficient for equijoins.
    -   **Cons:**
        -   Involves shuffling (if not pre-partitioned/sorted).
        -   Sorting can be expensive.
- Cartesian Product (Cross Join)
    -   **When Used:** When an explicit `CROSS JOIN` is specified or if a join condition is missing or cannot be optimized into another type.
    -   **How it Works:** Produces every possible combination of rows from the two DataFrames.
    -   **Pros:** None in terms of performance for typical analytical joins.
    -   **Cons:**
        -   **Extremely Expensive:** The size of the result is (num_rows_df1 * num_rows_df2). This can lead to massive data generation and usually indicates a logical error in the join condition or an intentional but resource-intensive operation.
        -   Spark will often try to prevent or warn about accidental cross joins if `spark.sql.crossJoin.enabled` is false (default).
- Broadcast Nested Loop Join
    -   **When Used:** For non-equijoins or complex join conditions when one table is small enough to broadcast.
    -   **How it Works:** The smaller table is broadcasted. Then, for each row in the larger table, it iterates through all rows of the broadcasted smaller table to evaluate the join condition.
    -   **Pros:** Can handle arbitrary join conditions when one table is small.
    -   **Cons:** Can be very slow if the broadcasted table is not very small, as it involves a nested loop comparison ($O(N \cdot M)$ complexity per partition).

## Spark's Choice of Join Strategy
Spark's Catalyst optimizer automatically chooses a join strategy based on:
-   **Table Sizes:** Statistics about table sizes (if available, or estimated).
-   **Join Type:** Inner, left, right, full, cross, etc.
-   **Join Condition:** Equijoin vs. non-equijoin.
-   **Configuration Parameters:**
    -   `spark.sql.autoBroadcastJoinThreshold`: Maximum size (in bytes) of a table that will be broadcasted.
    -   `spark.sql.join.preferSortMergeJoin`: Can be set to `true` to hint Spark to prefer Sort Merge Join (though Catalyst often makes a good choice).
    -   Other cost-based optimization parameters.

## Viewing the Join Strategy
You can use `DataFrame.explain()` to see the physical plan, which will show the join strategy Spark has chosen.
```python
# Conceptual example
# large_df.join(small_df, "id").explain()
# Look for terms like "BroadcastHashJoin", "SortMergeJoin", "ShuffledHashJoin" in the physical plan.
```

Understanding and sometimes influencing join strategies (e.g., by ensuring accurate table statistics, using broadcast hints, or repartitioning data) is a key part of [[Spark_Performance_Tuning|Spark performance tuning]].

---
````

`````markdown

Filename: 180_Big_Data/Spark/Spark_Streaming_Structured_Streaming.md
````markdown
---
tags: [spark, streaming, structured_streaming, real_time_processing, micro_batch, continuous_processing, concept]
aliases: [Spark Streaming, Structured Streaming, DStream]
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Data_Streaming_Big_Data]]"
  - "[[Apache_Kafka]]" # Common source/sink for Spark Streaming
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]" # Structured Streaming uses DataFrame API
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]" # Original Spark Streaming used DStreams (RDDs over time)
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark Streaming & Structured Streaming

Apache Spark provides capabilities for processing [[Data_Streaming_Big_Data|streaming data]], allowing applications to analyze and act upon data in real-time or near real-time as it arrives. Spark has two main streaming APIs:

1.  **Spark Streaming (Legacy):** The original streaming library based on Discretized Streams (DStreams).
2.  **Structured Streaming (Current & Recommended):** A newer, higher-level API built on the Spark SQL engine and [[Spark_DataFrame_SQL|DataFrame]] API, designed for easier and more robust stream processing.

## 1. Spark Streaming (DStream API - Legacy)
-   **Concept:** Processes live data streams by dividing them into a sequence of small batches (micro-batches). Each batch is treated as an [[RDD_Resilient_Distributed_Dataset|RDD]]. Transformations on these DStreams (Discretized Streams) are applied to each underlying RDD in the sequence.
-   **DStream:** A DStream is a continuous sequence of RDDs representing a stream of data.
-   **Operations:** Supports transformations (e.g., `map`, `filter`, `reduceByKeyAndWindow`, `updateStateByKey`) and output operations (e.g., `print`, `saveAsTextFiles`, `foreachRDD`).
-   **Windowing:** Supports windowed computations (e.g., `window()`, `countByWindow()`, `reduceByWindow()`).
-   **Stateful Operations:** Can maintain state across batches using `updateStateByKey` or `mapWithState`.
-   **Fault Tolerance:** Inherits RDD fault tolerance.
-   **Status:** While still functional, **Spark Streaming (DStream API) is largely considered legacy**. Most new development and focus have shifted to Structured Streaming due to its advantages.

## 2. Structured Streaming (DataFrame/Dataset API - Recommended)
-   **Concept:** A scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express streaming computations in the same way you would express batch computations on static data using the DataFrame/Dataset API.
-   **Core Idea:** Treats a live data stream as a continuously appending, unbounded table. Each new item in the stream is like a new row being appended to this table.
-   **Queries:** You define a query on this "input table" as if it were a static table, using standard DataFrame/Dataset operations (e.g., `select`, `filter`, `groupBy`, `join`, window functions).
-   **Incremental Execution:** Spark automatically converts these batch-like queries into incremental execution plans that run continuously as new stream data arrives.
-   **Output Modes:**
    -   `complete`: The entire updated result table is written to the output sink at each trigger.
    -   `append`: Only new rows added to the result table since the last trigger are written to the sink. (Default, suitable for queries where existing rows don't change).
    -   `update`: Only rows that were updated in the result table since the last trigger are written. (If query has aggregations, only updated rows are output).
-   **Triggers:** Defines when to process new data (e.g., process all available data, process every N seconds).
-   **Event Time Processing & Watermarking:** Strong support for handling out-of-order data based on event timestamps embedded in the data itself, using watermarks to manage late data and state.
-   **Stateful Operations:** Supports complex stateful operations like aggregations, windowing, and joins between streams or a stream and a static table. State is managed reliably.
-   **End-to-End Exactly-Once Semantics:** Aims to provide exactly-once processing guarantees with supported sources and sinks.

### Key Components of Structured Streaming
[list2tab|#Structured Streaming]
- Input Sources
    -   **File Source:** Reads files written into a directory (e.g., CSV, JSON, Parquet, ORC). Treats new files as a stream.
    -   **[[Apache_Kafka|Kafka Source]]:** Reads data from Apache Kafka topics. Very common for stream ingestion.
    -   Socket Source (for testing).
    -   Rate Source (for testing, generates data at a fixed rate).
    -   Custom sources can be implemented.
- Query Definition (DataFrame API)
    -   Use standard DataFrame transformations (`select`, `filter`, `groupBy`, `agg`, `withWatermark`, `window`, `join`).
- Output Sinks
    -   **File Sink:** Writes the output to files (CSV, JSON, Parquet, ORC).
    -   **Kafka Sink:** Writes output to a Kafka topic.
    -   **Foreach/ForeachBatch Sink:** Allows custom logic to write output to arbitrary storage systems (e.g., databases, key-value stores).
    -   Console Sink (for debugging, prints to console).
    -   Memory Sink (for debugging, stores output in an in-memory table).
- Output Modes
    -   `append`, `complete`, `update` (as described above).
- Triggers
    -   `processingTime`: Trigger based on processing time intervals (e.g., every 10 seconds).
    -   `once`: Trigger only once to process all available data and then stop.
    -   `continuous`: (Experimental) A low-latency continuous processing mode.

### Example: Structured Streaming Word Count from a Socket Source
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import explode, split, window

# spark = SparkSession.builder \
#     .appName("StructuredStreamingWordCount") \
#     .master("local[*]") \
#     .getOrCreate()

# # Create a DataFrame representing the stream of input lines from a netcat server
# # To run this, start a netcat server: nc -lk 9999 on your terminal
# lines_df = spark.readStream \
#     .format("socket") \
#     .option("host", "localhost") \
#     .option("port", 9999) \
#     .load()

# # Split the lines into words
# # lines_df is a DataFrame with a single string column "value"
# words_df = lines_df.select(
#    explode(
#        split(lines_df.value, " ")
#    ).alias("word")
# )

# # Generate running word count
# word_counts_df = words_df.groupBy("word").count()

# # Start running the query that prints the running counts to the console
# query = word_counts_df.writeStream \
#     .outputMode("complete") \ # Show all counts every time
#     .format("console") \
#     .trigger(processingTime="5 seconds") \ # Process data every 5 seconds
#     .start()

# print("Streaming query started. Type words into netcat (localhost:9999).")
# query.awaitTermination() # Wait for the query to terminate (e.g., by Ctrl-C)

# spark.stop()
```
> To test this, you would run `nc -lk 9999` in one terminal and then run the PySpark script. Words typed into the netcat terminal will be processed.

### Example: Structured Streaming with Event Time and Watermarking (Conceptual)
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import window, col, current_timestamp, expr
# from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# spark = SparkSession.builder.appName("EventTimeWindowing").master("local[*]").getOrCreate()

# Define schema for incoming data (e.g., product click events)
# event_schema = StructType([
#     StructField("event_time", TimestampType(), True),
#     StructField("product_id", StringType(), True),
#     StructField("action", StringType(), True) # e.g., "view", "click"
# ])

# Read from a source like Kafka or a directory of files
# For example, reading from a directory of JSON files
# input_stream_df = spark.readStream \
#     .schema(event_schema) \
#     .json("path/to/streaming_event_data_json/") # Directory to monitor

# Group by a tumbling window of 10 minutes on 'event_time' and 'product_id', count actions
# Add a watermark to handle late data (e.g., events arriving up to 5 minutes late)
# windowed_counts = input_stream_df \
#     .withWatermark("event_time", "5 minutes") \
#     .groupBy(
#         window(col("event_time"), "10 minutes", "5 minutes"), # 10 min window, slides every 5 min
#         col("product_id"),
#         col("action")
#     ).count()

# query_event_time = windowed_counts.writeStream \
#     .outputMode("update") \ # Update mode for aggregations
#     .format("console") \
#     .option("truncate", "false") \
#     .trigger(processingTime="1 minute") \
#     .start()

# query_event_time.awaitTermination()
# spark.stop()
```

## Advantages of Structured Streaming over DStream API
-   **Higher-Level API:** Built on DataFrames/Datasets and Spark SQL, making it easier to write and reason about stream processing logic using familiar batch-like constructs.
-   **Unified Batch and Streaming:** Code for batch and stream processing is largely the same.
-   **Event Time Processing:** Robust support for event time semantics and handling late data with watermarks.
-   **End-to-End Guarantees:** Better support for exactly-once processing semantics with compatible sources/sinks.
-   **Catalyst Optimizer:** Leverages Spark SQL's Catalyst optimizer for query optimization.

Structured Streaming is the recommended approach for most new stream processing applications in Spark.

---
````

`````markdown

Filename: 180_Big_Data/Spark/Spark_MLlib.md
````markdown
---
tags: [spark, pyspark, mllib, machine_learning, distributed_ml, classification, regression, clustering, concept]
aliases: [Spark MLlib, MLlib, Spark Machine Learning Library]
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]" # Newer MLlib API uses DataFrames
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]" # Older MLlib API used RDDs
  - "[[Scikit_learn_MOC|_Scikit_learn_MOC]]" # Comparison, MLlib focuses on distributed
  - "[[Machine_Learning_Overview]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark MLlib (Machine Learning Library)

**MLlib** is Apache Spark's scalable machine learning library. It aims to make practical machine learning scalable and easy, providing tools such as:
-   Common learning algorithms (classification, regression, clustering, collaborative filtering).
-   Featurization utilities (feature extraction, transformation, dimensionality reduction, selection).
-   Pipelines for constructing, evaluating, and tuning ML workflows.
-   Persistence utilities for saving and loading algorithms, models, and pipelines.

MLlib has two main APIs:
1.  **`spark.mllib` (RDD-based API - Older):** The original API built on top of [[RDD_Resilient_Distributed_Dataset|RDDs]]. It is now in maintenance mode.
2.  **`spark.ml` (DataFrame-based API - Recommended):** The primary API since Spark 2.0, built on top of [[Spark_DataFrame_SQL|DataFrames]]. It offers a more user-friendly and uniform API, leveraging the optimizations of Spark SQL and DataFrames. This note will focus on the `spark.ml` API.

## Key Components of `spark.ml`

[list2tab|#spark.ml Components]
- DataFrame as Primary Data Structure
    -   `spark.ml` uses DataFrames to represent datasets, which can hold a variety of data types. A typical DataFrame has columns for features, labels (for supervised learning), and predictions.
- Transformers
    -   An algorithm that can transform one DataFrame into another DataFrame.
    -   Implements a `.transform()` method.
    -   Examples:
        -   Feature Transformers: `VectorAssembler` (combines multiple columns into a single feature vector), `StandardScaler`, `MinMaxScaler`, `StringIndexer` (encodes string labels to numerical indices), `OneHotEncoder`, `PCA`.
        -   Fitted Models: A trained model is also a transformer that transforms a DataFrame with features into a DataFrame with predictions.
- Estimators
    -   An algorithm which can be fit on a DataFrame to produce a Transformer.
    -   Implements a `.fit()` method, which takes a DataFrame and returns a model (which is a Transformer).
    -   Examples: `LogisticRegression` (classifier), `DecisionTreeRegressor` (regressor), `KMeans` (clustering algorithm).
- Pipelines (`Pipeline`)
    -   Chains multiple Transformers and Estimators together to specify an ML workflow.
    -   A `Pipeline` itself is an Estimator. When `fit()` is called on a Pipeline, it fits all Estimators in sequence. The resulting `PipelineModel` is a Transformer.
    -   Ensures that training and test data go through the same processing steps.
    -   Example: A pipeline might consist of `StringIndexer` -> `OneHotEncoder` -> `VectorAssembler` -> `LogisticRegression`.
- Evaluation (`Evaluator`)
    -   Used to measure the performance of a model.
    -   Examples: `BinaryClassificationEvaluator` (metrics: areaUnderROC, areaUnderPR), `MulticlassClassificationEvaluator` (metrics: accuracy, f1, precision, recall), `RegressionEvaluator` (metrics: rmse, mse, r2, mae).
- Parameter Tuning (Hyperparameter Optimization)
    -   Tools for finding the best hyperparameters for models.
    -   `CrossValidator`: Uses K-fold cross-validation to evaluate each parameter combination.
    -   `TrainValidationSplit`: Simpler, splits data once into training and validation sets.
    -   Requires an `Estimator` (e.g., a model or a full Pipeline), a set of `ParamGridBuilder` (parameter grids), and an `Evaluator`.

## Common ML Tasks and Algorithms in `spark.ml`

[list2tab|#MLlib Algorithms]
- Classification
    -   `LogisticRegression`
    -   `DecisionTreeClassifier`
    -   `RandomForestClassifier`
    -   `GBTClassifier` (Gradient-Boosted Trees)
    -   `MultilayerPerceptronClassifier` (Basic Neural Network)
    -   `LinearSVC` (Linear Support Vector Classifier)
    -   `NaiveBayes`
- Regression
    -   `LinearRegression`
    -   `DecisionTreeRegressor`
    -   `RandomForestRegressor`
    -   `GBTRegressor`
    -   `GeneralizedLinearRegression` (GLM)
    -   `IsotonicRegression`
- Clustering
    -   `KMeans`
    -   `LDA` (Latent Dirichlet Allocation - for topic modeling, can be seen as a form of clustering)
    -   `BisectingKMeans`
    -   `GaussianMixture` (GMM)
- Collaborative Filtering
    -   `ALS` (Alternating Least Squares): For building recommendation systems.
- Featurization
    -   **Extraction:** `TFIDF`, `Word2Vec`, `CountVectorizer`, `FeatureHasher`.
    -   **Transformation:** `StringIndexer`, `OneHotEncoder`, `VectorAssembler`, `StandardScaler`, `MinMaxScaler`, `PCA`, `Normalizer`, `Bucketizer`, `QuantileDiscretizer`.
    -   **Selection:** `ChiSqSelector`, `VectorSlicer`.

## Example: Logistic Regression for E-commerce Customer Churn Prediction
```python
# from pyspark.sql import SparkSession
# from pyspark.ml.feature import VectorAssembler, StringIndexer, StandardScaler
# from pyspark.ml.classification import LogisticRegression
# from pyspark.ml import Pipeline
# from pyspark.ml.evaluation import BinaryClassificationEvaluator
# from pyspark.sql.functions import col
# import pandas as pd # For creating initial dummy data

# spark = SparkSession.builder.appName("MLlibChurnPrediction").master("local[*]").getOrCreate()

# Sample customer data (conceptual - replace with actual data loading)
# pandas_df = pd.DataFrame({
#     'customer_id': ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'],
#     'age':,
#     'gender': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
#     'monthly_spend':,
#     'last_purchase_days_ago':,
#     'churned': # Target variable
# })
# spark_df = spark.createDataFrame(pandas_df)

# 1. Feature Engineering
# Index 'gender' string column to numerical
# gender_indexer = StringIndexer(inputCol="gender", outputCol="gender_indexed", handleInvalid="keep")
# Assemble features into a single vector
# feature_cols = ["age", "gender_indexed", "monthly_spend", "last_purchase_days_ago"]
# assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
# Scale features
# scaler = StandardScaler(inputCol="raw_features", outputCol="scaled_features")

# 2. Define the Model
# logistic_regression = LogisticRegression(featuresCol="scaled_features", labelCol="churned")

# 3. Create a Pipeline
# pipeline = Pipeline(stages=[gender_indexer, assembler, scaler, logistic_regression])

# 4. Split Data
# train_data, test_data = spark_df.randomSplit([0.7, 0.3], seed=42)

# 5. Train the Model (Fit the Pipeline)
# try:
#     pipeline_model = pipeline.fit(train_data)
# except Exception as e: # Catch potential errors with tiny dummy data
#     print(f"Error during pipeline fitting (likely due to small/dummy data): {e}")
#     pipeline_model = None # Ensure it's defined

# 6. Make Predictions
# if pipeline_model:
#     predictions = pipeline_model.transform(test_data)
#     print("--- Predictions (sample) ---")
#     predictions.select("customer_id", "churned", "probability", "prediction").show(5)

    # 7. Evaluate the Model
    # evaluator = BinaryClassificationEvaluator(labelCol="churned", rawPredictionCol="rawPrediction", metricName="areaUnderROC")
    # auc = evaluator.evaluate(predictions)
    # print(f"Area Under ROC on Test Data: {auc:.4f}")

    # For accuracy:
    # from pyspark.ml.evaluation import MulticlassClassificationEvaluator
    # acc_evaluator = MulticlassClassificationEvaluator(labelCol="churned", predictionCol="prediction", metricName="accuracy")
    # accuracy = acc_evaluator.evaluate(predictions)
    # print(f"Accuracy on Test Data: {accuracy:.4f}")

# spark.stop()
```

## Advantages of MLlib (`spark.ml`)
-   **Scalability:** Designed to run on large distributed datasets.
-   **DataFrame Integration:** Leverages the power and optimizations of Spark SQL and DataFrames.
-   **Unified API:** Consistent API across different algorithms and pipeline stages.
-   **Pipeline Persistence:** Entire ML pipelines (including preprocessing and model) can be saved and loaded.

MLlib provides a robust framework for building scalable machine learning pipelines in Spark, making it suitable for handling Big Data ML tasks.

---
````

`````markdown

Filename: 180_Big_Data/Spark/Spark_GraphX_GraphFrames.md
````markdown
---
tags: [spark, pyspark, graphx, graphframes, graph_processing, distributed_graph, concept]
aliases: [Spark Graph Processing, GraphX, GraphFrames]
related:
  - "[[180_Big_Data/Spark/_Spark_MOC|_Spark_MOC]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]" # GraphX is RDD-based
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]" # GraphFrames is DataFrame-based
  - "[[Graph_Theory_Concepts]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark: Graph Processing (GraphX and GraphFrames)

Apache Spark provides capabilities for graph processing and analytics through two main libraries/APIs: **GraphX** (the original RDD-based API) and **GraphFrames** (a newer DataFrame-based API). These allow users to model, transform, and query graph-structured data at scale.

Graphs consist of vertices (nodes) and edges (relationships between nodes). Examples include social networks, web graphs, protein interaction networks, and transportation networks.

## 1. GraphX (RDD-based API)
-   **Core Abstraction:** `Graph[VD, ED]`, where `VD` is the type of vertex attributes and `ED` is the type of edge attributes. A graph is represented by two [[RDD_Resilient_Distributed_Dataset|RDDs]]: one for vertices (`graph.vertices`) and one for edges (`graph.edges`). Edges are typically `Edge(srcId, dstId, attribute)` triplets.
-   **Language:** Primarily available in Scala and Java. PySpark has limited support for GraphX, mainly for loading graphs or calling some algorithms, but defining complex graph computations directly in PySpark with GraphX is less common/ergonomic.
-   **Key Features:**
    -   Property graphs (vertices and edges can have attributes).
    -   A rich set of graph operators: `subgraph()`, `mask()`, `joinVertices()`, `aggregateMessages()`.
    -   Implementations of common graph algorithms:
        -   PageRank
        -   Connected Components
        -   Strongly Connected Components
        -   Triangle Counting
        -   Shortest Paths (though often limited to non-negative weights or unweighted)
    -   Pregel API: A vertex-centric bulk-synchronous parallel programming model for iterative graph algorithms.
-   **Status:** While powerful, GraphX development has slowed, and the community focus has somewhat shifted towards GraphFrames for users preferring DataFrame APIs, especially in PySpark.

**Conceptual GraphX Usage (Illustrative - more natural in Scala/Java):**
```scala
// Scala Example for GraphX
// import org.apache.spark.graphx._
// import org.apache.spark.rdd.RDD

// val sc: SparkContext = ... // SparkContext

// Create an RDD for vertices
// val users: RDD[(VertexId, (String, String))] =
//   sc.parallelize(Array((3L, ("rxin", "student")), (7L, ("jgonzal", "postdoc")),
//                        (5L, ("franklin", "prof")), (2L, ("istoica", "prof"))))
// Create an RDD for edges
// val relationships: RDD[Edge[String]] =
//   sc.parallelize(Array(Edge(3L, 7L, "collab"),    Edge(5L, 3L, "advisor"),
//                        Edge(2L, 5L, "colleague"), Edge(5L, 7L, "pi")))
// Define a default user in case some users are only referenced in relationships
// val defaultUser = ("John Doe", "Missing")
// Build the initial Graph
// val graph = Graph(users, relationships, defaultUser)

// Count all users who are postdocs
// val postdocCount = graph.vertices.filter { case (id, (name, pos)) => pos == "postdoc" }.count()
// println(s"Number of postdocs: $postdocCount")

// Run PageRank
// val ranks = graph.pageRank(0.001).vertices
// ranks.join(users).sortBy(_._2._1, ascending=false).map {
//   case (id, (rank, (name, pos))) => s"$name ($pos) has rank $rank."
// }.take(5).foreach(println)
```

## 2. GraphFrames (DataFrame-based API)
-   **Core Abstraction:** Graphs are represented by two [[Spark_DataFrame_SQL|Spark DataFrames]]: one for vertices and one for edges.
    -   **Vertex DataFrame:** Must have a special column named `"id"` specifying unique vertex IDs. Can have other columns for vertex attributes.
    -   **Edge DataFrame:** Must have two special columns: `"src"` (source vertex ID of edge) and `"dst"` (destination vertex ID of edge). Can have other columns for edge attributes.
-   **Language:** Available in Python (PySpark), Scala, and Java. It's the preferred graph API for PySpark users.
-   **Integration:** Built on top of Spark DataFrames, allowing seamless integration with Spark SQL and MLlib. Leverages Catalyst optimizer.
-   **Key Features:**
    -   Motif finding: Searching for structural patterns in the graph (e.g., find all triangles where users A, B, C follow each other).
    -   Standard graph algorithms: PageRank, Connected Components, Strongly Connected Components, Shortest Paths (BFS-based), Label Propagation Algorithm (LPA) for community detection, Triangle Counting.
    -   Graph queries similar to Cypher (from Neo4j) but expressed using DataFrame operations.
    -   Message passing via `aggregateMessages` framework (similar to GraphX but adapted for DataFrames).
-   **Installation:** GraphFrames is a separate package that needs to be added to Spark applications (e.g., using `--packages graphframes:graphframes:0.8.x-spark3.y-s_2.12` when submitting a job, or configured in `SparkSession`).

**PySpark GraphFrames Example (Conceptual E-commerce: Customers and Co-purchased Products):**
```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# # Assuming GraphFrames package is available to SparkSession

# spark = SparkSession.builder \
#     .appName("GraphFramesExample") \
#     .master("local[*]") \
#     .config("spark.jars.packages", "graphframes:graphframes:0.8.2-spark3.2-s_2.12") \ # Adjust version as needed
#     .getOrCreate()

# # Create Vertex DataFrame (e.g., customers and products)
# # Nodes can be customers or products
# vertices_data = [
#     ("c1", "Alice", "customer"), ("c2", "Bob", "customer"), ("c3", "Carol", "customer"),
#     ("p1", "Laptop", "product"), ("p2", "Mouse", "product"), ("p3", "Keyboard", "product")
# ]
# v_df = spark.createDataFrame(vertices_data, ["id", "name", "type"])

# # Create Edge DataFrame (e.g., customer 'purchased' product)
# edges_data = [
#     ("c1", "p1", "purchased"), ("c1", "p2", "purchased"), # Alice bought Laptop, Mouse
#     ("c2", "p1", "purchased"), ("c2", "p3", "purchased"), # Bob bought Laptop, Keyboard
#     ("c3", "p2", "purchased")                            # Carol bought Mouse
# ]
# e_df = spark.createDataFrame(edges_data, ["src", "dst", "relationship"])

# # Create a GraphFrame
# try:
#     from graphframes import GraphFrame # Import after SparkSession with package is created
#     g = GraphFrame(v_df, e_df)
# except ImportError:
#     print("GraphFrames package not found or not configured correctly with SparkSession.")
#     g = None # So rest of conceptual example doesn't break immediately

# if g:
    # Display vertices and edges
    # print("--- Vertices ---")
    # g.vertices.show()
    # print("--- Edges ---")
    # g.edges.show()

    # Query: Find customers who purchased a "Laptop"
    # laptop_buyers = g.filterEdges("relationship = 'purchased'") \
    #                  .filterVertices("type = 'customer'") \
    #                  .find("(a)-[e]->(b)") \
    #                  .filter("b.name = 'Laptop' AND a.type = 'customer'") \
    #                  .select("a.name as customer_name") \
    #                  .distinct()
    # print("--- Customers who bought a Laptop ---")
    # laptop_buyers.show()

    # Run PageRank (conceptual, might need more specific graph structure for meaningful PageRank)
    # results_pagerank = g.pageRank(resetProbability=0.15, tol=0.01)
    # print("--- PageRank Vertices (sample) ---")
    # results_pagerank.vertices.select("id", "name", "pagerank").orderBy(col("pagerank").desc()).show(5)
    # print("--- PageRank Edges (sample) ---")
    # results_pagerank.edges.select("src", "dst", "weight").show(5) # 'weight' is added by PageRank

    # Find connected components
    # connected_components_df = g.connectedComponents()
    # print("--- Connected Components ---")
    # connected_components_df.select("id", "name", "component").orderBy("component", "id").show()

# spark.stop()
```
> **Note:** Running GraphFrames examples requires the GraphFrames package to be correctly linked with your Spark session.

## Choosing Between GraphX and GraphFrames
-   **Language Preference:**
    -   **GraphX:** Primarily for Scala/Java users. PySpark API is limited.
    -   **GraphFrames:** First-class support for Python (PySpark), Scala, and Java. More natural for PySpark users.
-   **API Style:**
    -   **GraphX:** RDD-based, lower-level, offers fine-grained control (e.g., Pregel API).
    -   **GraphFrames:** DataFrame-based, higher-level, benefits from Catalyst optimizations, allows SQL-like queries on graph motifs.
-   **Performance:**
    -   GraphX can sometimes be more performant for highly iterative, low-level graph algorithms due to direct RDD manipulation and less overhead than DataFrames for certain operations.
    -   GraphFrames can leverage Catalyst query optimizations and Tungsten execution, which can be very efficient for queries and algorithms expressible in DataFrame operations.
-   **Ease of Use:**
    -   GraphFrames are often considered easier to use for those already familiar with Spark DataFrames and SQL.
-   **Community and Development:**
    -   GraphFrames has seen more active development and community focus in recent years compared to GraphX.

For most new graph processing tasks in PySpark, **GraphFrames is generally the recommended choice** due to its Python-friendliness and integration with the DataFrame ecosystem. GraphX remains relevant for complex, low-level graph algorithms primarily in Scala/Java environments.

---
`````

This covers the main Spark components (Streaming, MLlib, GraphX/GraphFrames). Next, I will address the remaining Spark questions that might not have been fully covered in dedicated notes yet.

Okay, let's address the remaining Spark questions. I'll create new notes for those that warrant it or integrate answers into existing notes if more appropriate.

Based on our previous review, the questions that might need more direct attention or their own notes are:

-   `What is the difference between Hadoop and Spark?` - Covered by [[Spark_vs_Hadoop_MapReduce]]
-   `what is the difference between MapReduce and Spark?` - Covered by [[Spark_vs_Hadoop_MapReduce]]
-   `Why do we need Spark? Can't we just easily read files/databases directly?` - Covered by [[Why_Spark_Needed]]
-   `What is a Spark Context?` - Covered by [[PySpark_SparkSession_SparkContext]]
-   `What is the difference between a Session and a Context?` - Covered by [[PySpark_SparkSession_SparkContext]]
-   `What is the purpose of a Spark Cluster?` - Covered by [[Spark_Cluster_Architecture]]
-   `For each of the following modules/classes, explain what is its purpose and its advantages: RDD, DataFrame and SQL, Streaming, MLlib, GraphFrames, Resource` - Mostly covered by individual notes. "Resource" is general; I'll assume it refers to resource management.
-   `What is the difference between a Spark DataFrame and a Pandas DataFrame?` - Covered by [[Spark_DataFrame_vs_Pandas_DataFrame]]
-   `What are the Spark data sources?` - Covered by [[PySpark_Data_Sources]]
-   `What is the difference between a transformation and an action?` - Covered by [[Spark_Transformations_Actions]]
-   `What are the advantages of laziness?` - Covered by [[Spark_Lazy_vs_Eager_Execution]]
-   `When is a shuffle operation needed?` - Covered by [[Spark_Shuffle_Operations]]
-   `Explain explain` - Covered by [[Spark_explain_Plan]]
-   `What is the importance of repartition ?` - Covered in [[Spark_Performance_Tuning]] (and briefly in `Spark_Shuffle_Operations`). I can create a specific note for `Spark_Repartition_Coalesce.md` to detail this more.
-   `Describe a use case for map and another for mapPartitions.` - Covered by [[Spark_map_vs_mapPartitions]]
-   `Is there a parallel for SQL constraints in Spark? What about indexes? If yes - what is it? If no - why?` - Covered by [[Spark_SQL_Constraints_Indexes]]
-   `Why and when are lit and col useful?` - Covered in [[PySpark_SQL_Functions]]
-   `What is the difference between parquet files and csv files?` - Covered by [[Parquet_vs_CSV_Spark]]
-   `Can we read data directly from a JSON file using Spark? How? Why would we do that?` - Covered in [[PySpark_Data_Sources]]

It seems the main items needing specific notes are:
1.  A dedicated note for `Spark_Repartition_Coalesce.md`.
2.  Consolidating the purpose/advantages of Spark Ecosystem Components if not fully covered. The notes `Spark_Streaming_Structured_Streaming.md`, `Spark_MLlib.md`, and `Spark_GraphX_GraphFrames.md` were created to address this for those specific components. RDD and DataFrame/SQL are also well-covered. "Resource" is tied to Cluster Management.

Let's create `Spark_Repartition_Coalesce.md`.

---

`````markdown

Filename: 180_Big_Data/Spark/Spark_Repartition_Coalesce.md
````markdown
---
tags: [spark, pyspark, dataframe, rdd, repartition, coalesce, partitioning, performance, shuffle, concept]
aliases: [Spark Repartition, Spark Coalesce, Changing Partitions Spark]
related:
  - "[[Spark_Performance_Tuning]]"
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_Data_Parallelism]]"
  - "[[Spark_DataFrame_SQL|Spark DataFrame]]"
  - "[[RDD_Resilient_Distributed_Dataset|RDD]]"
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark: `repartition()` vs. `coalesce()`

In Apache Spark, `repartition()` and `coalesce()` are transformations used to change the number of partitions of a [[RDD_Resilient_Distributed_Dataset|RDD]] or [[Spark_DataFrame_SQL|DataFrame]]. While both affect partitioning, they do so in different ways and have different performance implications, primarily concerning [[Spark_Shuffle_Operations|shuffle operations]].

>[!question] What is the importance of `repartition`? (and `coalesce`)

The importance of `repartition()` and `coalesce()` lies in their ability to control the level of [[Spark_Data_Parallelism|parallelism]] and manage data distribution, which are critical for [[Spark_Performance_Tuning|Spark performance tuning]].

-   **Controlling Parallelism:** The number of partitions often dictates the number of tasks Spark can run in parallel for subsequent stages. Adjusting partitions can help fully utilize cluster resources or prevent too many small tasks.
-   **Data Skew Mitigation:** `repartition()` (especially by key) can help redistribute skewed data more evenly.
-   **Optimizing Shuffles:** While `repartition()` itself is a shuffle, it can sometimes be used to set up data in a way that benefits subsequent shuffles (e.g., for joins).
-   **Controlling Output File Numbers:** When writing data to a file system, the number of output files typically corresponds to the number of partitions in the final RDD/DataFrame. `repartition()` or `coalesce()` can be used to control this.
-   **Reducing Overhead of Small Partitions:** `coalesce()` is particularly useful for reducing the number of partitions after filtering operations that might have created many small, inefficient partitions.

## `repartition(numPartitions, *cols)`
-   **Purpose:** Reshuffles the data in the RDD/DataFrame to create exactly `numPartitions`.
-   **Mechanism:** Always triggers a **full shuffle** of the data across the network. Data is redistributed based on a hash of the partitioning columns (if specified) or round-robin if no columns are specified.
-   **Use Cases:**
    1.  **Increasing the number of partitions:** If you have too few partitions and want to increase parallelism for subsequent operations. This is common after filtering data heavily or reading from a source that creates few partitions.
    2.  **Decreasing the number of partitions AND redistributing data:** If you want to reduce partitions and also ensure data is re-hashed and potentially more evenly distributed.
    3.  **Partitioning by specific columns (`df.repartition(N, col("key_col"))` or `rdd.repartitionAndSortWithinPartitions(...)` for RDDs):** This shuffles data such that all rows/elements with the same values in the specified columns end up in the same partition. This can be very beneficial for optimizing subsequent joins or aggregations on those keys.
-   **Performance:** Can be expensive due to the full shuffle. Use judiciously.
-   **Example (DataFrame):**
    ```python
    # from pyspark.sql import SparkSession
    # from pyspark.sql.functions import spark_partition_id

    # spark = SparkSession.builder.appName("RepartitionExample").master("local").getOrCreate()
    # data = [(i, "value_" + str(i % 3)) for i in range(100)]
    # df = spark.createDataFrame(data, ["id", "category"])
    # print(f"Original number of partitions: {df.rdd.getNumPartitions()}") # Might be default parallelism
    # df.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()

    # Repartition into 5 partitions (full shuffle)
    # df_repartitioned = df.repartition(5)
    # print(f"Number of partitions after repartition(5): {df_repartitioned.rdd.getNumPartitions()}")
    # df_repartitioned.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()

    # Repartition by 'category' column into 3 partitions (if possible, based on distinct categories)
    # df_repartitioned_by_cat = df.repartition(3, "category") # Data with same category goes to same partition
    # print(f"Number of partitions after repartition(3, 'category'): {df_repartitioned_by_cat.rdd.getNumPartitions()}")
    # df_repartitioned_by_cat.select("category", "id", spark_partition_id().alias("pid")).orderBy("pid", "category").show(30)

    # spark.stop()
    ```

## `coalesce(numPartitions)`
-   **Purpose:** Reduces the number of partitions in an RDD/DataFrame to `numPartitions`.
-   **Mechanism:** This operation tries to **avoid a full shuffle** when decreasing the number of partitions. It achieves this by merging existing partitions on the same worker nodes. Data from some partitions is moved to reside on fewer nodes.
    -   If you are *drastically* reducing the number of partitions (e.g., from 1000 to 10), or if data is very skewed, `coalesce` might still involve some data movement that resembles a partial shuffle to achieve better balance, but it aims to be less expensive than a full `repartition`.
    -   `coalesce` **cannot** be used to increase the number of partitions (it will have no effect or might error if `numPartitions` is greater than current). For increasing partitions, `repartition` is needed.
-   **Use Cases:**
    1.  **Decreasing the number of partitions efficiently:** This is its primary use case, especially after operations like `filter()` that might result in many small, sparse partitions. Reducing partitions can reduce task scheduling overhead and improve performance of subsequent operations or when writing output (fewer output files).
-   **Performance:** Generally more efficient than `repartition()` when *only decreasing* the number of partitions because it minimizes data movement.
-   **Example (DataFrame):**
    ```python
    # from pyspark.sql import SparkSession
    # from pyspark.sql.functions import spark_partition_id

    # spark = SparkSession.builder.appName("CoalesceExample").master("local").getOrCreate()
    # # Create a DataFrame with more partitions initially, e.g., by repartitioning
    # initial_df = spark.range(1000).repartition(10)
    # print(f"Number of partitions before coalesce: {initial_df.rdd.getNumPartitions()}")
    # initial_df.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()


    # Coalesce into 3 partitions
    # df_coalesced = initial_df.coalesce(3)
    # print(f"Number of partitions after coalesce(3): {df_coalesced.rdd.getNumPartitions()}")
    # df_coalesced.withColumn("partition_id", spark_partition_id()).groupBy("partition_id").count().show()
    # Note: The distribution after coalesce might not be perfectly even if it avoids a full shuffle.

    # spark.stop()
    ```

## `repartitionByRange(*cols)` (DataFrame specific)
-   **Purpose:** Repartitions the DataFrame according to the ranges of the specified columns. Rows with column values within the same range will go to the same partition.
-   **Mechanism:** Involves a shuffle and sorting by the partitioning columns. Useful if you want data to be physically ordered by certain columns across partitions.

## Key Differences Summarized

[list2mdtable|#Repartition vs Coalesce]
- Feature
    - `repartition(numPartitions, *cols)`
        - `coalesce(numPartitions)`
- **Primary Use**
    - Increase or decrease partitions; redistribute data (optionally by key).
        - Decrease partitions efficiently.
- **Shuffle**
    - Always performs a full shuffle.
        - Avoids a full shuffle if possible (merges existing partitions). Can involve some data movement for balancing if reducing drastically.
- **Increasing Partitions**
    - Yes.
        - No (use `repartition` for this).
- **Performance Cost**
    - Generally more expensive due to full shuffle.
        - Generally less expensive when decreasing partitions.
- **Data Distribution**
    - Can lead to more even data distribution due to hashing/sorting in shuffle.
        - May result in less even data distribution if it simply merges existing partitions without rebalancing.

**When to Use Which:**
-   Use **`repartition()`**:
    -   When you need to **increase** the number of partitions.
    -   When you need to **decrease** the number of partitions AND ensure data is **re-shuffled and potentially more evenly distributed** (e.g., to mitigate skew before a join, or if partitioning by specific keys).
    -   Before writing data if you need a specific number of output files with potentially more even sizes.
-   Use **`coalesce()`**:
    -   When you need to **decrease** the number of partitions and want to **minimize data movement** (avoid a full shuffle). This is common after filtering operations that create many small partitions.
    -   Typically faster than `repartition()` for reducing partition count.

Choosing the right number of partitions and using `repartition` or `coalesce` appropriately is a common Spark optimization technique. Monitor the Spark UI to observe the number of tasks and stages to help guide these decisions.

---````

`````markdown

Filename: 180_Big_Data/Spark/Catalyst_Optimizer_Spark.md
````markdown
---
tags: [spark, catalyst_optimizer, query_optimization, sql, dataframe, logical_plan, physical_plan, concept]
aliases: [Spark Catalyst, Catalyst, Spark Query Optimizer]
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[Spark_explain_Plan|Understanding Query Plans (explain())]]"
  - "[[Spark_DAG_Scheduler|Spark DAG Scheduler]]"
  - "[[Tungsten_Execution_Engine]]" # Placeholder
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Catalyst Optimizer in Spark

The **Catalyst optimizer** is the core query optimization engine in Apache Spark, particularly for [[Spark_DataFrame_SQL|Spark SQL]] and the DataFrame/Dataset API. It is an extensible optimizer based on functional programming constructs in Scala. Catalyst allows Spark to automatically apply various optimization techniques to user queries, translating high-level DataFrame operations or SQL queries into efficient physical execution plans.

## Role and Goal
-   **Goal:** To improve the performance and efficiency of Spark SQL and DataFrame queries without requiring users to manually optimize their code extensively.
-   **How it Works:** Catalyst takes an unresolved logical plan (representing the user's query), resolves it against Spark's catalog, applies a series of rule-based and cost-based optimizations to create an optimized logical plan, and then translates this into one or more physical execution plans. Spark then chooses the "best" physical plan for execution.

## Phases of Optimization in Catalyst
The optimization process in Catalyst typically involves several phases, which can be observed using `DataFrame.explain(extended=True)` or `DataFrame.explain(mode="formatted")`:

1.  **Parsing:**
    -   The SQL query string is parsed into an Abstract Syntax Tree (AST).
    -   For DataFrame API calls, an AST-like tree of unresolved logical operators is constructed directly.

2.  **Analysis (Creating an Analyzed Logical Plan):**
    -   The unresolved logical plan (AST) is resolved against Spark's **catalog** (which stores metadata about tables, views, functions, columns, and data types).
    -   **Resolution:** Unresolved attributes (column names) and relations (table names) are bound to actual data sources and schema information.
    -   **Type Checking:** Data types are verified, and implicit type casts are added if necessary and safe.
    -   **Semantic Validation:** The query is checked for semantic correctness (e.g., correct number of arguments to functions).
    -   The output is an **Analyzed Logical Plan**, which is a semantically valid representation of what the query needs to compute.

3.  **Logical Optimization (Creating an Optimized Logical Plan):**
    -   The analyzed logical plan is transformed by applying a series of **rule-based optimizations**. These rules aim to restructure the plan into a more efficient equivalent form without changing the result.
    -   Common rules include:
        -   **Predicate Pushdown:** Moving filter conditions (`WHERE` clauses) as close to the data source as possible. This reduces the amount of data read and processed in later stages.
        -   **Projection Pruning:** Eliminating unnecessary columns (those not used in subsequent operations or the final result) early in the query plan.
        -   **Constant Folding:** Evaluating constant expressions at compile time (e.g., `1+1` becomes `2`).
        -   **Boolean Expression Simplification:** Simplifying `AND`/`OR` conditions.
        -   **Operator Reordering:** E.g., pushing limits down, reordering joins (if cost-based optimization is enabled and statistics are available).
        -   **Null Propagation/Simplification.**
        -   Converting outer joins to inner joins if predicates make them equivalent.
    -   The output is an **Optimized Logical Plan**.

4.  **Physical Planning (Creating a Physical Plan):**
    -   The optimized logical plan is translated into one or more **physical execution plans**. A physical plan describes *how* the query will be executed on the cluster using specific physical operators (e.g., `HashAggregate`, `SortMergeJoin`, `BroadcastHashJoin`, `FileScan`).
    -   Spark may generate multiple physical plans for a given logical plan.
    -   **Cost-Based Optimization (CBO):** If enabled and statistics about the data are available (e.g., table sizes, column cardinalities, histograms), Spark can use a cost model to estimate the execution cost of different physical plans and choose the one with the lowest estimated cost. This is particularly important for choosing [[Spark_Join_Strategies|join algorithms]] and join order.
    -   The chosen physical plan is a DAG of RDD operations that will be submitted to the [[Spark_DAG_Scheduler|DAG Scheduler]] and then the Task Scheduler for execution.
    -   Physical operators often have a `*` prefix (e.g., `*Project`, `*Filter`) in the `explain()` output, indicating that Spark's [[Tungsten_Execution_Engine|Tungsten execution engine]] might generate optimized bytecode (whole-stage code generation) for that part of the plan to improve performance by reducing virtual function calls and leveraging CPU caches.

## Extensibility
Catalyst is designed to be extensible:
-   **External Data Sources:** New data source connectors can integrate with Catalyst to provide schema information and support optimizations like predicate and projection pushdown.
-   **User-Defined Functions (UDFs):** While standard UDFs are often black boxes to Catalyst, newer interfaces like Pandas UDFs (Vectorized UDFs) can sometimes be better optimized.
-   **Custom Optimization Rules:** Advanced users can potentially add their own optimization rules to Catalyst (though this is a Scala-level activity).

## Benefits of Catalyst
-   **Performance:** Automatically applies many standard database query optimizations, leading to significant performance improvements without manual intervention.
-   **Abstraction:** Allows users to write queries in high-level APIs (DataFrame, SQL) while Catalyst handles the complex task of generating efficient low-level execution code.
-   **Extensibility:** Can be extended to support new data sources and optimization techniques.
-   **Unified Optimization:** Provides a common optimization framework for both SQL queries and DataFrame operations.

Understanding the basics of Catalyst and how to read query plans using `explain()` is crucial for [[Spark_Performance_Tuning|tuning Spark applications]] and diagnosing performance issues.

---


---

Understood! I will use the `>[!question]-` format for expandable callouts for future questions integrated into notes.

Let's finish the remaining PySpark conceptual notes and then create the note for Plotly & Plotly Express.

The PySpark items that seem to still need dedicated notes or more fleshing out based on the original keyword/question list are:
-   `Spark_Join_Strategies.md` (I created this, but we can ensure it's detailed enough)
-   `Spark_Streaming_Structured_Streaming.md` (Created)
-   `Spark_MLlib.md` (Created)
-   `Spark_GraphX_GraphFrames.md` (Created)
-   `PySpark_Broadcast_Variables_Accumulators.md` (I see this in your "already written" list, so it should be fine)
-   `PySpark_UDFs.md` (I see this in your "already written" list, so it should be fine)
-   `Catalyst_Optimizer_Spark.md` (Created)

It seems the main Spark components are largely covered by the notes you listed as existing and the ones I've just generated. If there's a specific aspect of "Resource" (from "For each of the following modules/classes, explain what is its purpose and its advantages: ... Resource") that isn't covered by [[Spark_Cluster_Manager]] or [[Spark_Cluster_Architecture]], please let me know. Otherwise, I'll assume it's sufficiently addressed.

Let's ensure `Spark_Join_Strategies.md` is robust and then move to Plotly. I'll re-generate it to ensure it's comprehensive and uses the new callout style if any implicit questions are answered.

---

`````markdown

Filename: 180_Big_Data/Spark/Spark_Join_Strategies.md
````markdown
---
tags: [spark, sql, dataframe, join, optimization, performance, shuffle, broadcast_join, sort_merge_join, concept]
aliases: [Spark Join Optimization, Spark Join Types, Broadcast Hash Join, Shuffle Hash Join, Sort Merge Join, BHJ, SMJ, SHJ]
related:
  - "[[Spark_DataFrame_SQL|Spark DataFrame & SQL]]"
  - "[[PySpark_DataFrame_Operations]]" # Where .join() is used
  - "[[Spark_Shuffle_Operations]]"
  - "[[Spark_explain_Plan|Understanding Query Plans (explain())]]" # To see which join is used
  - "[[Spark_Performance_Tuning]]"
  - "[[PySpark_Broadcast_Variables_Accumulators|Broadcast Variables]]" # For broadcast joins
worksheet: [WS_Spark_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Spark Join Strategies

When joining two [[Spark_DataFrame_SQL|DataFrames]] in Apache Spark, the Catalyst optimizer automatically chooses a **join strategy** to execute the operation efficiently. The selected strategy significantly impacts performance, especially for large datasets, by influencing data movement ([[Spark_Shuffle_Operations|shuffling]]) and computational load.

Understanding these strategies helps in writing performant Spark SQL queries and DataFrame operations, and in interpreting [[Spark_explain_Plan|query execution plans]].

## Common Join Strategies in Spark

[list2tab|#Join Strategies Overview]
- Broadcast Hash Join (BHJ)
    -   **Also Known As:** Map-side Join (though technically the "map" side is the broadcast and hash table build, probe is on the other side).
    -   **When Used:** When one DataFrame is significantly smaller than the other and can fit comfortably in the memory of each executor. The size threshold is controlled by `spark.sql.autoBroadcastJoinThreshold` (default typically 10MB).
    -   **How it Works:**
        1.  **Broadcast:** The smaller DataFrame is collected to the driver and then broadcasted (sent in its entirety) to every executor node in the cluster.
        2.  **Hash Table Build:** Each executor builds an in-memory hash table from the broadcasted (smaller) DataFrame based on the join keys.
        3.  **Probe:** The larger DataFrame (which is not moved) is processed partition by partition. For each row in a partition of the larger DataFrame, its join key is used to probe the hash table (built from the smaller DataFrame) to find matches.
    -   **Pros:**
        -   **Avoids Shuffle of Larger Table:** Completely avoids shuffling the larger DataFrame, which is a major performance advantage. Only the small table is moved.
        -   Very fast if the broadcasted table is indeed small.
    -   **Cons:**
        -   Only suitable if one table is small enough. Broadcasting very large tables can cause OutOfMemoryErrors on the driver (during collect) or executors.
        -   Requires an equijoin (join condition based on equality of keys).
    -   **Hinting:** You can explicitly suggest a broadcast join using `broadcast()` function:
        ```python
        from pyspark.sql.functions import broadcast
        # joined_df = df_large.join(broadcast(df_small), "join_key_column")
        ```
- Shuffle Hash Join (SHJ)
    -   **When Used:** For equijoins when tables are moderately sized, neither is small enough for a broadcast, but one side (after shuffling) is small enough to build a hash table on each partition. Spark might choose this if it estimates building hash tables is feasible.
    -   **How it Works:**
        1.  **Shuffle Phase:** Both DataFrames are shuffled (repartitioned) across the cluster based on their join keys. Rows with the same join key from both DataFrames are guaranteed to land on the same executor/partition.
        2.  **Build Phase (on Reducers/Executors):** On each partition, a hash table is built from one of the DataFrames (typically the smaller one for that partition after shuffling).
        3.  **Probe Phase (on Reducers/Executors):** The other DataFrame's partition is streamed, and its rows probe the hash table to find matches.
    -   **Pros:**
        -   Can be more efficient than Sort Merge Join if the hash table build is fast and fits in memory.
        -   Good for equijoins.
    -   **Cons:**
        -   Involves a shuffle of both tables (or the parts being joined).
        -   Memory-intensive on executors if the hash tables become large.
        -   Sensitive to data skew in join keys, which can lead to some executors having very large hash tables to build/probe.
- Sort Merge Join (SMJ)
    -   **When Used:** Often the default for joining large tables when a broadcast join is not feasible. It's robust and can handle large data sizes. Also used if data is already sorted or partitioned on the join keys.
    -   **How it Works:**
        1.  **Shuffle Phase (if not already co-partitioned and sorted):** Both DataFrames are shuffled (repartitioned) based on their join keys so that rows with the same join keys are on the same partition.
        2.  **Sort Phase (within each partition):** Data within each partition is sorted by the join keys for both DataFrames.
        3.  **Merge Phase:** The sorted partitions from both DataFrames are "merged" together. Since they are sorted by the join key, matching rows can be found by iterating through both datasets simultaneously in a manner similar to the merge step of a merge sort algorithm.
    -   **Pros:**
        -   Robust and can handle very large datasets as it doesn't require holding large hash tables in memory (it streams and sorts).
        -   Less sensitive to data skew in terms of memory blowup compared to Shuffle Hash Join, though severe skew can still lead to long-running tasks.
        -   Can handle non-equijoins if the condition allows for sorting and merging (though primarily optimized for equijoins).
    -   **Cons:**
        -   Involves shuffling (if data is not already appropriately partitioned and sorted).
        -   The sorting step itself can be computationally expensive.
- Cartesian Product (Cross Join) / Broadcast Nested Loop Join (BNLJ)
    -   **Cartesian Product (`CROSS JOIN`):**
        -   **When Used:** When an explicit `CROSS JOIN` is specified, or if no join condition is provided, or if the join condition cannot be optimized by Spark into a more efficient join.
        -   **How it Works:** Produces every possible combination of rows from the two DataFrames. The size of the result is $N \times M$.
        -   **Cons:** Extremely expensive and usually indicates an error or a very specific (and often problematic) requirement. Spark often requires `spark.sql.crossJoin.enabled=true` to allow it.
    -   **Broadcast Nested Loop Join (BNLJ):**
        -   **When Used:** For non-equijoins or complex join conditions where one DataFrame is small enough to be broadcast. If no specific optimization for the join condition is available, Spark might fall back to this if one side is broadcastable.
        -   **How it Works:** The smaller DataFrame is broadcasted to all executors. Then, for each partition of the larger DataFrame, Spark iterates through its rows, and for each row, it iterates through all rows of the (broadcasted) smaller DataFrame to evaluate the join condition.
        -   **Pros:** Can handle arbitrary join conditions when one table is small.
        -   **Cons:** Very high computational complexity ($O(N \cdot M)$ per partition of the larger table) if the broadcasted table is not extremely small.

## Spark's Choice and Influencing Factors
Spark's Catalyst optimizer automatically chooses a join strategy. Key factors influencing this choice include:
-   **Table Size Statistics:** If available (e.g., from `ANALYZE TABLE`), Spark uses these to estimate costs.
-   **`spark.sql.autoBroadcastJoinThreshold`:** Configures the maximum size (in bytes) of a DataFrame that will be broadcasted.
-   **Join Type:** Inner, left, right, full, cross.
-   **Join Condition:** Equijoin (e.g., `df1.key == df2.key`) vs. non-equijoin (e.g., `df1.key > df2.key`, complex UDFs). Equijoins have more optimization possibilities.
-   **Data Skew:** Highly skewed join keys can degrade the performance of shuffle-based joins.
-   **Availability of Sorted/Partitioned Data:** If input DataFrames are already partitioned and/or sorted on the join keys in a compatible way, Spark might skip some shuffle/sort steps.

## Checking the Join Strategy
Use `DataFrame.explain()` to inspect the physical plan and see which join strategy Spark has chosen. Look for operators like `BroadcastHashJoin`, `ShuffledHashJoin`, `SortMergeJoin`, or `BroadcastNestedLoopJoin`.

```python
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import broadcast

# spark = SparkSession.builder.appName("JoinStrategyDemo").master("local[*]").getOrCreate()

# df_large = spark.createDataFrame([(i, f"val_large_{i}") for i in range(10000)], ["id", "value_large"])
# df_small = spark.createDataFrame([(i, f"val_small_{i}") for i in range(100)], ["id", "value_small"])

# # Example 1: Likely BroadcastHashJoin due to broadcast hint or small size of df_small
# joined_bhj = df_large.join(broadcast(df_small), "id")
# print("--- Plan for likely BroadcastHashJoin ---")
# joined_bhj.explain()

# # Example 2: Potentially SortMergeJoin or ShuffledHashJoin if df_small were larger
# # and broadcast threshold not met.
# # To force a sort-merge join (for illustration, not always recommended to force)
# # spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
# # spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1") # Disable auto-broadcast

# # df_large2 = spark.createDataFrame([(i, f"val_large2_{i}") for i in range(10000)], ["id", "value_large2"])
# # df_medium = spark.createDataFrame([(i, f"val_medium_{i}") for i in range(5000)], ["id", "value_medium"])
# # joined_smj_shj = df_large2.join(df_medium, "id")
# # print("\n--- Plan for likely SortMergeJoin or ShuffledHashJoin ---")
# # joined_smj_shj.explain()

# spark.stop()
```

Understanding these strategies is crucial for optimizing join performance in Spark, which is often a critical part of data processing pipelines.

---
````

Now, moving to Plotly & Plotly Express.

---

`````markdown

Filename: 170_Data_Visualization/Plotly_Express_Library.md
````markdown
---
tags: [python, data_visualization, plotting, plotly, plotly_express, interactive_plots, web_based_viz, library, concept, example]
aliases: [Plotly, Plotly.Express, Interactive Python Plots]
related:
  - "[[_Data_Visualization_MOC]]"
  - "[[_Pandas_MOC]]" # Plotly Express integrates well with Pandas
  - "[[_Matplotlib_MOC]]" # Alternative, often for static plots
  - "[[170_Data_Visualization/Seaborn/_Seaborn_MOC|Seaborn]]" # Alternative for statistical plots
  - "[[Bokeh_Library]]" # Another interactive visualization library
  - "[[Dash_Plotly]]" # Placeholder for Dash (web apps with Plotly)
worksheet: [WS_DataViz_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Plotly and Plotly Express

**Plotly** is a versatile Python graphing library that makes interactive, publication-quality graphs. Plotly graphs can be rendered in Jupyter notebooks, standalone HTML files, or embedded in web applications using [[Dash_Plotly|Dash]].

**Plotly Express** (`plotly.express` or `px`) is a high-level wrapper for Plotly that provides a simple and concise syntax for creating a wide variety of figures. It's often the recommended starting point for creating Plotly figures, similar to how Seaborn provides a high-level interface for Matplotlib.

## Key Features of Plotly & Plotly Express
-   **Interactivity:** Generated plots are inherently interactive, allowing for zoom, pan, hover-to-see-data, and selection of data points.
-   **Web-Based:** Outputs are typically HTML/JavaScript, making them suitable for web embedding and sharing.
-   **Wide Range of Chart Types:** Supports common charts like scatter, line, bar, histogram, box, violin, pie, as well as more specialized ones like 3D plots, maps (choropleth, scatter_mapbox), sunbursts, treemaps, parallel coordinates, etc.
-   **High-Level API (Plotly Express):** `plotly.express` allows creating complex figures with a single function call, often directly from [[_Pandas_MOC|Pandas DataFrames]]. It automatically handles many details like legends and color mapping.
-   **Lower-Level API (Graph Objects - `plotly.graph_objects` or `go`):** For more fine-grained control and customization, Plotly provides a "Graph Objects" interface. Plotly Express functions actually return `plotly.graph_objects.Figure` instances, which can then be further customized.
-   **Animations and Sliders:** Supports creating animated plots and plots with interactive controls like sliders and dropdowns.
-   **Theming and Templates:** Offers built-in themes for styling plots.
-   **Export Options:** Can export to static image formats (PNG, JPG, SVG, PDF - requires `kaleido` package) and interactive HTML.
-   **Integration with Dash:** Plotly is the core visualization engine for Dash, a Python framework for building analytical web applications.

## Plotly Express (`px`) - Common Usage
Plotly Express functions typically accept a Pandas DataFrame as the first argument and then column names as strings for `x`, `y`, `color`, `size`, `facet_row`, `facet_col`, etc.

**Example: Interactive Scatter Plot of E-commerce Product Data**
```python
import plotly.express as px
import pandas as pd
import numpy as np

# Conceptual product data
# np.random.seed(42)
# product_data = pd.DataFrame({
#     'product_name': [f"Product {i}" for i in range(50)],
#     'price': np.random.uniform(10, 500, 50),
#     'avg_rating': np.random.uniform(1, 5, 50).round(1),
#     'category': np.random.choice(['Electronics', 'Books', 'Apparel', 'Home Goods'], 50),
#     'units_sold': np.random.randint(5, 200, 50)
# })

# Create an interactive scatter plot
# fig_scatter = px.scatter(
#     product_data,
#     x="price",
#     y="avg_rating",
#     color="category",         # Color points by category
#     size="units_sold",        # Size points by units_sold
#     hover_name="product_name",# Show product name on hover
#     title="Product Price vs. Average Rating (Interactive)",
#     labels={"price": "Price ($)", "avg_rating": "Average Customer Rating"}
# )

# To display in a Jupyter Notebook or environment that supports Plotly rendering:
# fig_scatter.show()

# To save as an HTML file:
# fig_scatter.write_html("interactive_product_scatter.html")
```
> This plot would allow hovering over points to see product names, zooming, panning, and filtering by category via the legend.

## Plotly Graph Objects (`go`) - For More Control
If Plotly Express doesn't offer enough customization, you can use `plotly.graph_objects` to build figures from scratch or modify figures created by Plotly Express.

**Example: Creating a Line Chart with Graph Objects**
```python
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Conceptual monthly sales data for two product categories
# dates = pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'])
# sales_electronics = 
# sales_books = 

# fig_line_go = go.Figure()

# Add traces (lines)
# fig_line_go.add_trace(go.Scatter(x=dates, y=sales_electronics, mode='lines+markers', name='Electronics Sales'))
# fig_line_go.add_trace(go.Scatter(x=dates, y=sales_books, mode='lines+markers', name='Book Sales'))

# Update layout
# fig_line_go.update_layout(
#     title_text="Monthly Sales by Category (Graph Objects)",
#     xaxis_title="Month",
#     yaxis_title="Sales Amount ($)",
#     legend_title_text="Category"
# )

# fig_line_go.show()
```

## Common Plot Types with Plotly Express

[list2tab|#Plotly Express Plots]
- Scatter & Line
    -   `px.scatter(df, x, y, color, size, symbol, hover_data, trendline, facet_row, facet_col)`
    -   `px.line(df, x, y, color, line_group, symbol, hover_data, facet_row, facet_col)`
    -   `px.scatter_3d()`, `px.line_3d()`
- Bar Charts
    -   `px.bar(df, x, y, color, orientation, barmode, hover_data, facet_row, facet_col)` (`barmode`: 'group', 'stack', 'relative')
- Histograms & Box Plots
    -   `px.histogram(df, x, y, color, marginal, cumulative, histnorm, nbins)`
    -   `px.box(df, x, y, color, notched, points, orientation)`
    -   `px.violin(df, x, y, color, box, points, orientation)`
- Pie Charts & Sunbursts
    -   `px.pie(df, names, values, color, hole)`
    -   `px.sunburst(df, path, values, color)` (for hierarchical data)
    -   `px.treemap(df, path, values, color)`
- Maps
    -   `px.scatter_geo(df, lat, lon, color, size, hover_name, projection)`
    -   `px.line_geo()`
    -   `px.choropleth(df, geojson, locations, color, featureidkey, projection)`
    -   `px.scatter_mapbox(df, lat, lon, color, size, zoom, mapbox_style)` (requires Mapbox token for some styles)
    -   `px.choropleth_mapbox()`
- Specialized
    -   `px.imshow()` (for heatmaps from 2D arrays)
    -   `px.parallel_coordinates(df, dimensions, color)`
    -   `px.scatter_matrix(df, dimensions, color)` (similar to pair plot)

## Advantages
-   **Interactivity:** Rich built-in interactivity is a major strength.
-   **Ease of Use (Plotly Express):** Quickly create complex, attractive plots.
-   **Web-Native:** Ideal for embedding in web pages and dashboards ([[Dash_Plotly|Dash]]).
-   **Wide Chart Variety:** Supports a very broad range of chart types.
-   **Good Aesthetics:** Default styles are generally modern and visually appealing.

## Considerations
-   **Performance with Very Large Datasets (in Browser):** While Plotly can handle large datasets for backend rendering or aggregation, rendering tens of thousands of interactive points directly in a web browser can sometimes become slow. Techniques like Datashader can be used with Plotly for visualizing massive datasets.
-   **Offline Use:** While plots can be saved as HTML, full interactivity in some environments (like static HTML without an internet connection for certain map tiles) might have limitations. JupyterLab/Notebook rendering is excellent.
-   **Dependencies for Exporting Static Images:** Requires `kaleido` for static image export (PNG, SVG, PDF).

Plotly and Plotly Express provide a powerful and user-friendly way to create rich, interactive visualizations in Python, bridging the gap between static scientific plotting and dynamic web-based data exploration.

---
`````

---

Okay, understood. I will create a few more essential but concise notes to round out the Selenium section, focusing on the core concepts needed for basic usage, and then we can move on.

I will create notes for:
-   `Selenium_Locating_Elements.md`
-   `Selenium_Interacting_Elements.md`
-   `Selenium_Waits.md`
-   `Selenium_Headless_Browsing.md`

This will provide a solid "getting started" guide for using Selenium in web scraping.

---

`````markdown

Filename: 160_Python_Libraries/Selenium/Selenium_Locating_Elements.md
````markdown
---
tags: [python, selenium, webdriver, locators, find_element, css_selector, xpath, concept, example]
aliases: [Selenium Locators, Finding Elements with Selenium, By Class]
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_WebDriver_Basics]]"
  - "[[Selenium_Interacting_Elements]]"
  - "[[CSS_Selectors]]"
  - "[[XPath_Selectors]]"
worksheet: [WS_WebScraping_1, WS_Automation_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Selenium: Locating HTML Elements

After navigating to a page, the next step is to locate the specific HTML elements you want to interact with or extract data from. Selenium WebDriver provides the `find_element()` (to find a single element) and `find_elements()` (to find all matching elements) methods, which use different locator strategies defined in the `By` class.

## The `By` Class
To specify a locator strategy, you import the `By` class:
```python
from selenium.webdriver.common.by import By
```

## Common Locator Strategies
The `By` class provides the following strategies:

[list2tab|#Locator Strategies]
- `By.ID`
    -   **Description:** Locates an element by its unique `id` attribute. This is usually the fastest and most reliable locator if available.
    -   **Example:** `driver.find_element(By.ID, "product-title")`
- `By.NAME`
    -   **Description:** Locates an element by its `name` attribute. Often used for form elements.
    -   **Example:** `driver.find_element(By.NAME, "username")`
- `By.CLASS_NAME`
    -   **Description:** Locates elements that have a specific CSS class name. If an element has multiple classes, you must use one of them.
    -   **Example:** `driver.find_elements(By.CLASS_NAME, "product-card")`
- `By.TAG_NAME`
    -   **Description:** Locates elements by their HTML tag name.
    -   **Example:** `driver.find_elements(By.TAG_NAME, "a")` (finds all links)
- `By.LINK_TEXT`
    -   **Description:** Locates an anchor element (`<a>`) by its exact visible text.
    -   **Example:** `driver.find_element(By.LINK_TEXT, "Read More")`
- `By.PARTIAL_LINK_TEXT`
    -   **Description:** Locates an anchor element (`<a>`) whose visible text contains the given substring.
    -   **Example:** `driver.find_element(By.PARTIAL_LINK_TEXT, "More Info")`
- `By.CSS_SELECTOR`
    -   **Description:** Locates elements using a [[CSS_Selectors|CSS selector]]. This is a very powerful and versatile strategy.
    -   **Example:** `driver.find_element(By.CSS_SELECTOR, "div#main-content p.intro")`
- `By.XPATH`
    -   **Description:** Locates elements using an [[XPath_Selectors|XPath expression]]. This is the most powerful and flexible locator, allowing complex navigation of the DOM tree.
    -   **Example:** `driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]')`

## `find_element()` vs. `find_elements()`
-   **`driver.find_element(By.STRATEGY, "value")`**:
    -   Finds the **first** web element that matches the locator.
    -   Returns a single `WebElement` object.
    -   If no element is found, it raises a `NoSuchElementException`.
-   **`driver.find_elements(By.STRATEGY, "value")`**:
    -   Finds **all** web elements that match the locator.
    -   Returns a **list** of `WebElement` objects.
    -   If no elements are found, it returns an empty list.

## Example: Locating Elements on a Conceptual Product Page
```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# try:
#     # Assume we navigate to a product page
#     # driver.get("http://example-ecommerce.com/product/123")

#     # --- Using find_element (for unique elements) ---
#     # Find the product title by its ID
#     # product_title_element = driver.find_element(By.ID, "product-name")

#     # Find the price using a CSS selector
#     # price_element = driver.find_element(By.CSS_SELECTOR, "span.current-price")

#     # Find the "Add to Cart" button using XPath based on its text
#     # add_to_cart_button = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')

#     # --- Using find_elements (for multiple elements) ---
#     # Find all feature list items
#     # feature_elements = driver.find_elements(By.CSS_SELECTOR, "ul.features li")

#     # Find all review containers
#     # review_elements = driver.find_elements(By.CLASS_NAME, "review-card")

#     # print(f"Found {len(feature_elements)} features.")
#     # print(f"Found {len(review_elements)} reviews.")

# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     if 'driver' in locals():
#         driver.quit()
```

## Best Practices for Locators
-   **Prefer unique and stable locators:** `ID` is usually the best choice if available and unique.
-   **Use descriptive `class` names or `data-*` attributes:** These are often more stable than the HTML structure itself. `[data-testid="..."]` is a common pattern for stable test/automation hooks.
-   **Use CSS selectors for most cases:** They are readable and powerful enough for most common selection tasks.
-   **Use XPath for complex scenarios:** Use XPath when you need to select based on text content or navigate complex relationships (e.g., finding a parent or sibling based on a child's content).
-   **Avoid brittle locators:** Avoid relying on auto-generated IDs or class names (e.g., `class="css-1dbjc4n r-13awgt0"`), as they can change on every page load. Also, avoid long, absolute XPath paths (e.g., `/html/body/div/div[2]/div/p[3]`) as they break easily with minor layout changes.
-   **Use [[Selenium_Waits|Waits]]:** Before locating an element, especially on dynamic pages, use explicit waits to ensure the element is present and interactive.

Choosing the right locator strategy is key to creating robust and maintainable browser automation scripts.

---
````

`````markdown

Filename: 160_Python_Libraries/Selenium/Selenium_Interacting_Elements.md
````markdown
---
tags: [python, selenium, webdriver, browser_automation, interaction, click, send_keys, concept, example]
aliases: [Interacting with Web Elements Selenium, Selenium Actions]
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_Locating_Elements]]"
  - "[[Selenium_Waits]]"
worksheet: [WS_WebScraping_1, WS_Automation_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Selenium: Interacting with Web Elements

Once you have located a `WebElement` object using one of the methods from [[Selenium_Locating_Elements]], you can perform various actions on it to simulate user interaction. This is essential for tasks like filling out forms, clicking buttons to load dynamic content, or navigating menus.

## Common Interaction Methods
These methods are called on a `WebElement` object (e.g., `element.click()`).

[list2tab|#Element Interactions]
- `.click()`
    -   **Purpose:** Simulates a left mouse click on an element.
    -   **Use Cases:** Clicking buttons, links, radio buttons, checkboxes, etc.
    -   **Example:**
        ```python
        # login_button = driver.find_element(By.ID, "login-btn")
        # login_button.click()
        ```
- `.send_keys(*value)`
    -   **Purpose:** Simulates typing into an element, typically an `<input>` or `<textarea>` field.
    -   **Use Cases:** Filling out forms (usernames, passwords, search queries), uploading files (by sending the file path to an `<input type="file">`).
    -   **Example:**
        ```python
        # search_bar = driver.find_element(By.NAME, "q")
        # search_bar.send_keys("Selenium WebDriver")
        # search_bar.send_keys(Keys.RETURN) # To simulate pressing Enter
        # from selenium.webdriver.common.keys import Keys # Needs this import
        ```
- `.clear()`
    -   **Purpose:** Clears the text from an editable element (like an `<input>` or `<textarea>`).
    -   **Use Cases:** Resetting a form field before typing new text into it.
    -   **Example:**
        ```python
        # username_field = driver.find_element(By.ID, "username")
        # username_field.clear()
        # username_field.send_keys("new_username")
        ```
- `.submit()`
    -   **Purpose:** Submits a form. This can be called on any element within a `<form>`. It's often more convenient than finding and clicking the specific submit button.
    -   **Use Cases:** Submitting login forms, search forms, etc.
    -   **Example:**
        ```python
        # search_bar = driver.find_element(By.NAME, "q")
        # search_bar.send_keys("Scraping with Selenium")
        # search_bar.submit() # Submits the form the search bar belongs to
        ```
- `.get_attribute('name')`
    -   **Purpose:** Fetches the value of a given attribute of the element. This is used for [[Selenium_Extracting_Data|data extraction]].
    -   **Example:**
        ```python
        # link = driver.find_element(By.TAG_NAME, "a")
        # link_url = link.get_attribute("href")
        # print(f"Found link URL: {link_url}")
        ```
- `.text` (Property)
    -   **Purpose:** Gets the visible text content of the element and its sub-elements. This is used for [[Selenium_Extracting_Data|data extraction]].
    -   **Example:**
        ```python
        # heading = driver.find_element(By.TAG_NAME, "h1")
        # heading_text = heading.text
        # print(f"Heading text: {heading_text}")
        ```
- `.is_displayed()`, `.is_enabled()`, `.is_selected()` (Properties)
    -   **Purpose:** Check the state of an element. Return `True` or `False`.
    -   **Use Cases:** Verifying element states in tests or before interacting (e.g., check if a button is enabled before clicking).
    -   **Example:**
        ```python
        # submit_button = driver.find_element(By.ID, "submit")
        # if submit_button.is_enabled():
        #     print("Submit button is enabled.")
        #     # submit_button.click()
        # else:
        #     print("Submit button is disabled.")
        ```

## Example: Automating a Login Form
This conceptual example combines locating elements and interacting with them.

```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# try:
#     # 1. Navigate to the login page
#     driver.get("http://example.com/login") # Replace with a real login page

#     # 2. Locate the form elements
#     username_input = driver.find_element(By.ID, "user-name") # Replace with actual ID
#     password_input = driver.find_element(By.ID, "password") # Replace with actual ID
#     login_button = driver.find_element(By.TAG_NAME, "button") # Replace with actual locator

#     # 3. Interact with the elements
#     username_input.clear()
#     username_input.send_keys("my_test_user")

#     password_input.clear()
#     password_input.send_keys("my_secure_password")

#     print("Form filled. Clicking login button...")
#     login_button.click()

#     # 4. Wait for the next page to load
#     time.sleep(5) # In a real script, use an explicit wait here! See [[Selenium_Waits]]

#     # 5. Verify successful login by checking the new URL or a welcome message
#     # if "dashboard" in driver.current_url:
#     #     print("Login successful!")
#     #     welcome_message = driver.find_element(By.ID, "welcome-message").text
#     #     print(f"Welcome message: {welcome_message}")
#     # else:
#     #     print("Login may have failed.")
#     #     error_message = driver.find_element(By.ID, "error-message").text
#     #     print(f"Error message: {error_message}")

# except Exception as e:
#     print(f"An error occurred during interaction: {e}")
# finally:
#     if 'driver' in locals():
#         driver.quit()
```

## Advanced Interactions (`ActionChains`)
For more complex actions like mouse movements, hovering, right-clicking, or drag-and-drop, Selenium provides the `ActionChains` class.

```python
# from selenium.webdriver.common.action_chains import ActionChains

# # Conceptual example for hovering over a menu
# menu = driver.find_element(By.ID, "main-menu")
# submenu = driver.find_element(By.ID, "submenu-item")

# actions = ActionChains(driver)
# actions.move_to_element(menu) # Hover over the main menu
# actions.click(submenu) # Click the submenu item that appears
# actions.perform() # Execute the chain of actions
```

Effective interaction with web elements is the key to automating workflows and scraping data from dynamic, interactive websites. Always pair interactions with appropriate [[Selenium_Waits|waits]] to ensure stability.

---
````

`````markdown

Filename: 160_Python_Libraries/Selenium/Selenium_Waits.md
````markdown
---
tags: [python, selenium, webdriver, browser_automation, waits, explicit_wait, implicit_wait, dynamic_content, concept]
aliases: [Selenium Waits, Explicit Waits, Implicit Waits, Handling Asynchronous Load Selenium]
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_Locating_Elements]]"
  - "[[Handling_Dynamic_Content_Scraping]]"
worksheet: [WS_WebScraping_1, WS_Automation_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Selenium: Handling Waits

When automating a web browser, especially for scraping [[Static_vs_Dynamic_Web_Pages|dynamic web pages]], scripts often run faster than the browser can load, render, and execute JavaScript. If your script tries to find or interact with an element before it exists or is ready, it will fail, typically with a `NoSuchElementException`.

To create robust and reliable Selenium scripts, it's crucial to handle these timing issues by using **waits**.

## The Problem: Race Conditions
Without waits, your script is in a "race" against the browser. You are betting that the element will be ready by the time your `find_element` command executes. This leads to flaky tests and scrapers that work sometimes but fail at other times depending on network speed, server response time, and client-side processing load.

**Bad Practice: `time.sleep()`**
A common but poor solution is to use fixed delays:```python
import time
# driver.find_element(...).click()
# time.sleep(5) # BAD: Pauses script for exactly 5 seconds
# driver.find_element(...) # Hope the next element is ready
```
This is bad because:
-   If the element loads in 1 second, you've wasted 4 seconds.
-   If the element takes 6 seconds to load, your script will still fail.
-   It makes your script unnecessarily slow and unreliable.

## Types of Waits in Selenium

[list2tab|#Selenium Wait Types]
- Implicit Wait
    -   **Concept:** An implicit wait tells the WebDriver to poll the DOM for a certain amount of time when trying to find any element that is not immediately available. The setting is configured once per session.
    -   **How it Works:** You set a maximum time (e.g., 10 seconds). When you call `find_element`, if the element is not found immediately, the driver will keep trying to find it for up to 10 seconds before throwing a `NoSuchElementException`.
    -   **Syntax:**
        ```python
        # driver.implicitly_wait(10) # Set for the entire driver session
        # Now, any find_element call will wait up to 10 seconds
        # element = driver.find_element(By.ID, "some-dynamic-element")
        ```
    -   **Pros:** Simple to set up (one line).
    -   **Cons:**
        -   Applies globally to all `find_element` calls, which can slow down tests if you need to quickly check for the *absence* of an element.
        -   Only waits for the element to be *present in the DOM*. It does not wait for it to be visible, clickable, or in any other state. This is a major limitation.
        -   Mixing implicit and explicit waits can lead to unpredictable wait times. **It is generally recommended to avoid mixing them and to prefer explicit waits.**
- Explicit Wait
    -   **Concept:** An explicit wait is a piece of code you define to wait for a certain **condition** to be met before proceeding. It is applied to specific elements or situations and is the **recommended approach** for handling dynamic content.
    -   **How it Works:** You use the `WebDriverWait` class in combination with the `expected_conditions` module. `WebDriverWait` will poll for the condition at a specified frequency until the condition is met or a timeout is reached.
    -   **Syntax:**
        ```python
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        # from selenium import webdriver
        # driver = webdriver.Chrome(...)
        
        # try:
        #     # Wait up to 10 seconds until the element with id 'my-element' is visible
        #     element = WebDriverWait(driver, 10).until(
        #         EC.visibility_of_element_located((By.ID, "my-element"))
        #     )
        #     # Now that the element is guaranteed to be visible, you can interact with it
        #     element.click()
        # except TimeoutException:
        #     print("Element did not become visible within 10 seconds.")
        ```
    -   **Pros:**
        -   **Precise and Flexible:** You wait for exactly the condition you need (e.g., presence, visibility, clickability).
        -   **Robust:** Makes scripts much more reliable by synchronizing them with the state of the web page.
        -   **Specific:** Applied only where needed, doesn't slow down other parts of the script.
    -   **Common `expected_conditions`:**
        -   `presence_of_element_located(locator)`: Element is present in the DOM.
        -   `visibility_of_element_located(locator)`: Element is present and visible.
        -   `element_to_be_clickable(locator)`: Element is visible and enabled so you can click it.
        -   `text_to_be_present_in_element(locator, text)`: Specific text is present in the element.
        -   `alert_is_present()`: An alert dialog is present.
        -   `invisibility_of_element_located(locator)`: Wait until an element is no longer visible (e.g., a loading spinner disappears).
- Fluent Wait
    -   **Concept:** A more advanced type of explicit wait. It allows you to configure the polling frequency and to ignore specific types of exceptions (like `NoSuchElementException`) during the wait.
    -   **Note:** `WebDriverWait` is actually a specialized implementation of a fluent wait with sensible defaults. For most cases, `WebDriverWait` is sufficient.

## Best Practice
**Always prefer explicit waits over implicit waits and `time.sleep()`**.
-   Use `WebDriverWait` to synchronize your script with the browser's state.
-   Wait for the specific condition you need before interacting with an element (e.g., wait for it to be clickable before clicking).
-   Avoid mixing implicit and explicit waits. If you must, be aware of the potential for combined and unpredictable wait times.

By using explicit waits correctly, you can create Selenium scripts that are both fast (they proceed as soon as the condition is met) and robust (they don't fail due to simple timing issues).

---
````

`````markdown

Filename: 160_Python_Libraries/Selenium/Selenium_Headless_Browsing.md
````markdown
---
tags: [python, selenium, webdriver, browser_automation, headless, server_side_scraping, concept, example]
aliases: [Selenium Headless Mode, Headless Chrome, Headless Firefox]
related:
  - "[[160_Python_Libraries/Selenium/_Selenium_MOC|_Selenium_MOC]]"
  - "[[Selenium_WebDriver_Basics]]"
worksheet: [WS_WebScraping_1, WS_Automation_1]
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# Selenium: Headless Browsing

## Definition
**Headless browsing** refers to running a web browser without a graphical user interface (GUI). When you run Selenium in headless mode, the browser does everything it normally would—loading pages, executing JavaScript, rendering HTML—but it does so in the background without displaying any visible UI window.

This capability is crucial for running automated browser tasks on servers or in environments where a graphical display is not available or desired.

## Why Use Headless Mode?
-   **Server-Side Execution:** The primary reason. Most servers (e.g., Linux servers used for CI/CD pipelines, cloud virtual machines) do not have a graphical desktop environment installed. Headless mode allows Selenium scripts to run in these environments.
-   **Performance:** Running without a GUI can be slightly faster and consume fewer system resources (CPU, memory) compared to running a full browser window, as the overhead of rendering visual elements is eliminated.
-   **Parallel Execution:** When running multiple browser instances in parallel for large-scale testing or scraping, headless mode prevents numerous browser windows from cluttering the screen and consuming desktop resources.
-   **Automation & CI/CD:** Essential for integrating browser automation into continuous integration/continuous deployment (CI/CD) pipelines.

## How to Configure Headless Mode
Headless mode is enabled by setting a specific argument in the browser's `Options` object before initializing the WebDriver.

[list2tab|#Headless Configuration]
- Google Chrome
    -   **Argument:** `--headless` or (newer versions) `--headless=new`. The new headless mode is recommended as it's closer to the regular browser's behavior.
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        # chrome_options = Options()
        # chrome_options.add_argument("--headless=new") # Use new headless mode
        # chrome_options.add_argument("--disable-gpu") # Often recommended for headless on some systems
        # chrome_options.add_argument("--window-size=1920,1080") # Set a window size to avoid issues with responsive design

        # driver = webdriver.Chrome(
        #     service=Service(ChromeDriverManager().install()),
        #     options=chrome_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Chrome Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```
- Mozilla Firefox
    -   **Argument:** `-headless`
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        # firefox_options = Options()
        # firefox_options.add_argument("-headless")

        # driver = webdriver.Firefox(
        #     service=Service(GeckoDriverManager().install()),
        #     options=firefox_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Firefox Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```
- Microsoft Edge
    -   **Argument:** `--headless=new` (similar to Chrome)
    -   **Code:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        # edge_options = Options()
        # edge_options.add_argument("--headless=new")

        # driver = webdriver.Edge(
        #     service=Service(EdgeChromiumDriverManager().install()),
        #     options=edge_options
        # )

        # try:
        #     driver.get("http://example.com")
        #     print(f"Headless Edge Page Title: {driver.title}")
        # finally:
        #     driver.quit()
        ```

## Considerations and Potential Issues
-   **Different Behavior:** In some rare cases, websites might behave differently when they detect a headless browser. The "new" headless mode in Chrome (`--headless=new`) is designed to be more like the regular browser to mitigate this.
-   **Debugging:** Debugging can be more challenging without a visible browser window. It's often useful to develop and debug scripts in normal (headed) mode first, and then switch to headless mode for deployment.
-   **Taking Screenshots:** Even in headless mode, you can still take screenshots (`driver.save_screenshot('screenshot.png')`), which is an invaluable tool for debugging what the headless browser "sees."
-   **Window Size:** Some websites render differently based on the viewport size. It's good practice to set a realistic window size (e.g., `options.add_argument("--window-size=1920,1080")`) even in headless mode to ensure consistent rendering.

Headless browsing is an essential feature that makes Selenium a viable tool for server-side web scraping and automated testing at scale.

---
`````

This completes the brief but essential overview of Selenium. We can now move on to the next chapter. Based on your previous request, that would be the Data Visualization libraries (Bokeh, Altair, and expanding Seaborn). Please confirm if this is the desired next step.

---


