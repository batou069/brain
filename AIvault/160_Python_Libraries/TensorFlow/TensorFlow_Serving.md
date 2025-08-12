---
tags:
  - python
  - tensorflow
  - tf
  - tf_serving
  - model_deployment
  - production
  - inference_server
  - concept
aliases:
  - TF Serving
  - TensorFlow Model Server
related:
  - "[[_TensorFlow_MOC|_TensorFlow_MOC]]"
  - "[[TensorFlow_Saving_Loading_Models|Saving Keras/TF Models (SavedModel format)]]"
  - "[[RESTful_API]]"
  - "[[gRPC]]"
  - "[[Docker_Kubernetes_MLOps|Docker & Kubernetes (MLOps)]]"
worksheet:
  - WS_DeepLearning_1
date_created: 2025-06-11
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