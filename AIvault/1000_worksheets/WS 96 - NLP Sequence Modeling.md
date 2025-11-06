# Q
## Keywords

1. Recurrent Neural Networks (RNN)
2. Long Short-Term Memory (LSTM)
3. Gated Recurrent Units (GRU)
4. Encoder-Decoder Model
5. Attention
* Bahdanau Mechanism
* Luong Attention
- Cross-Attention
6. Beam Search
7. Zero-Shot Learning

## Questions

1. What is a "forget gate" in LSTM, and how is it different in GRU?
2. Which NLP tasks are considered seq2seq?
- Is sequence modeling always seq2seq?
3. What is the meaning of 2 different words being very close vectors in the embedding?
4. Propose 10 cases that are not NLP where sequence modeling can be helpful.
5. We all loved Cloze tests in high school. Propose a modeling scheme to solve those.
6. How can sequence modeling be used for zero-shot learning in NLP?
7. How is beam search different from Viterbi decoding?
8. Sequence modeling is often related to a progression in time (things happen in a specific order), however amount of time between steps is seldom used.
 - Find examples (papers) where time between steps is used.
9. Is attention relevant for models that are not seq2seq?
10. Do we really need DL for sequence modeling?

# A

## 🧠 Keywords

| Keyword                                | Short Answer                                                                                                                                                                                                                                               | Long Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Recurrent Neural Networks (RNN)** | A neural network designed to handle sequential data by maintaining a hidden state that captures information from previous steps.                                                                                                                           | RNNs are the foundational architecture for sequence data. They process inputs one element at a time, and at each step $t$, they compute a hidden state $h_t$ using the current input $x_t$ and the previous hidden state $h_{t-1}$: $h_t = f(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$. This shared mechanism allows the model to theoretically use information from far back in the sequence. **Alternatives:** LSTMs, GRUs, and Transformers (which use attention instead of recurrence).                                                                                                  |
| **2. Long Short-Term Memory (LSTM)**   | An advanced type of RNN that solves the vanishing gradient problem using specialized gates to regulate information flow into and out of a cell state.                                                                                                      | LSTMs use a **cell state** ($C_t$), a "conveyor belt" of information, and three gates (input, forget, and output) to control the flow. The **Forget Gate** decides what information to discard from $C_{t-1}$, the **Input Gate** decides what new information to add, and the **Output Gate** decides what part of $C_t$ to expose as the hidden state $h_t$. This design allows LSTMs to capture long-range dependencies far more effectively than basic RNNs.                                                                                                                       |
| **3. Gated Recurrent Units (GRU)**     | A simpler, more computationally efficient variant of the LSTM that combines the cell state and hidden state into a single vector and uses only two gates: a reset gate and an update gate.                                                                 | GRUs streamline the LSTM structure. The **Update Gate** acts as both the input and forget gates of an LSTM, deciding what information to pass through from the past and what to incorporate from the current input. The **Reset Gate** determines how much of the past hidden state to ignore. They typically offer performance comparable to LSTMs while having fewer parameters, making them faster to train.                                                                                                                                                                        |
| **4. Encoder-Decoder Model**           | An architecture composed of two separate RNNs (or Transformers) where the Encoder reads an input sequence and compresses it into a single context vector, and the Decoder takes this vector to generate an output sequence.                                | This model is essential for sequence-to-sequence (seq2seq) tasks like Machine Translation or Summarization where the input and output lengths may differ. The **Encoder** consumes the entire input, generating a final hidden state (context vector) that encapsulates the source meaning. The **Decoder** then uses this context vector as its initial state and generates the output sequence one token at a time, conditioning each step on the previously generated tokens.                                                                                                       |
| **5. Attention**                       | A mechanism that allows the model to selectively focus on the most relevant parts of the input sequence when generating a specific part of the output sequence.                                                                                            | Attention revolutionized seq2seq models by overcoming the "bottleneck" problem of the fixed-size context vector. It computes a set of alignment scores (weights) between the current decoder state and all encoder hidden states. These weights are used to create a dynamic context vector, allowing the decoder to "look back" at the source input wherever needed. This drastically improves performance on long sequences.                                                                                                                                                         |
| **- Bahdanau Mechanism**               | The first widely adopted form of Attention, which is **additive** (concatenates states) and computed **before** the decoder generates its output. Often called **Global Attention**.                                                                       | Introduced in 2014, it computes the alignment score based on the *previous* decoder hidden state and *all* encoder hidden states. It is considered "soft" (focuses on the entire input) and is sometimes termed **content-based attention**.                                                                                                                                                                                                                                                                                                                                           |
| **- Luong Attention**                  | A later form of Attention, which is **multiplicative** (uses dot products/matrix multiplication) and computed **after** the decoder generates its output (but before the final prediction). Often called **Local Attention** or **Dot-Product Attention**. | Introduced in 2015, it offers several computation methods (dot, general, concat) but is generally simpler and faster than Bahdanau. It computes the attention score using the *current* decoder hidden state. **Local Attention** is a variant where the model only focuses on a small window of encoder states, increasing efficiency for very long sequences.                                                                                                                                                                                                                        |
| **- Cross-Attention**                  | An attention mechanism used in Transformer decoders where the query comes from the decoder's previous layer, and the keys/values come from the **encoder's output**.                                                                                       | It is the key innovation in Transformer seq2seq models. It enables the decoder to find the most relevant parts of the input sequence (encoder output) to generate the next token, mimicking the standard Encoder-Decoder Attention mechanism.                                                                                                                                                                                                                                                                                                                                          |
| **6. Beam Search**                     | A heuristic search algorithm used by generative sequence models to find the most likely output sequence by exploring a fixed number ($k$, the beam width) of the most promising partial sequences at each time step.                                       | When generating a sequence, the model calculates probabilities for the next token. Instead of the greedy approach (taking the single highest-probability token), Beam Search keeps track of the top $k$ hypotheses (sequences). At step $t$, it extends these $k$ hypotheses into $k \times V$ candidates ($V$ is vocabulary size) and then selects the new top $k$ best sequences based on their cumulative probability. This vastly improves the chance of finding an optimal sequence compared to simple greedy decoding. **Alternative:** Greedy Search, Sampling (for diversity). |
| **7. Zero-Shot Learning (ZSL)**        | The model's ability to perform a task or classify data for categories/classes that it was **never explicitly trained on** by leveraging related knowledge and rich feature representations.                                                                | In NLP, large Language Models (LLMs) trained on vast amounts of data can perform ZSL. For example, a model trained only on translation and summarization might be able to correctly classify a document into a new category by understanding the prompt ("Classify this text as [new category X]") due to the strong semantic knowledge embedded in its parameters.                                                                                                                                                                                                                    |

***

## ❓ Questions

### 1. What is a "forget gate" in LSTM, and how is it different in GRU?

| Feature | Forget Gate (LSTM) | Update Gate (GRU) |
| :--- | :--- | :--- |
| **Function** | Explicitly decides which information from the previous **Cell State ($C_{t-1}$)** should be **discarded** (i.e., forgotten) or kept. | Acts as both the forget and input gates, deciding simultaneously what to **keep** from the previous **Hidden State ($h_{t-1}$)** and what to **add** from the new input. |
| **Gate Count** | 3 gates (Input, Forget, Output) + 1 Cell State | 2 gates (Reset, Update) + 1 Hidden State |
| **Equation** | $\mathbf{f}_t = \sigma(W_f \cdot [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$ | $\mathbf{z}_t = \sigma(W_z \cdot [\mathbf{h}_{t-1}, \mathbf{x}_t])$ (Update Gate) |
| **How it Works** | Multiplies the old cell state $C_{t-1}$ by the element-wise output of the forget gate ($\mathbf{f}_t$), where values closer to 0 mean "forget" and closer to 1 mean "keep." | The update gate ($\mathbf{z}_t$) is used to linearly interpolate between the past hidden state and the new candidate state, implicitly controlling the forgetting/keeping of the past. |

---

### 2. Which NLP tasks are considered seq2seq? Is sequence modeling always seq2seq?

Seq2seq (Sequence-to-Sequence) tasks involve mapping an input sequence to an output sequence, where the output sequence is generated sequentially.

**Common Seq2seq Tasks:**

* **Machine Translation:** (English Sentence $\rightarrow$ French Sentence)
* **Text Summarization (Abstractive):** (Document $\rightarrow$ Summary Text)
* **Image Captioning:** (Image Pixel Sequence $\rightarrow$ Caption Sentence)
* **Chatbots/Dialogue Generation:** (User Query $\rightarrow$ Response Sentence)
* **Speech Recognition:** (Acoustic Feature Sequence $\rightarrow$ Word Sequence)

**Is sequence modeling always seq2seq?**

**No.** Sequence modeling is a broad term for any task where the order of data matters. It includes three main categories:

| Category | Description | NLP Example |
| :--- | :--- | :--- |
| **Seq-to-Seq** | Input is a sequence, output is a sequence (often of different lengths). | Machine Translation |
| **Seq-to-One** | Input is a sequence, output is a single element. | **Sentiment Analysis** (Sentence $\rightarrow$ Positive/Negative), **Text Classification**. |
| **One-to-Seq** | Input is a single element, output is a sequence. | **Image Captioning** (Image $\rightarrow$ Sentence), **Music Generation** (Genre $\rightarrow$ Notes). |

---

### 3. What is the meaning of 2 different words being very close vectors in the embedding?

If two different words have **very close vectors** in an embedding space (like Word2Vec, GloVe, or the embeddings from a Transformer), it means they are considered **semantically similar or contextually related** by the model. 

* **Semantic Similarity:** The words have similar meanings (e.g., "king" and "queen," "big" and "large").
* **Contextual Similarity:** The words appear in similar contexts across the training data (e.g., "doctor" and "hospital," "cat" and "dog").
* **Substitutability:** The model has learned that one word can often replace the other in a sentence without significantly changing the sentence's overall meaning or grammatical correctness.

The distance between the vectors (often measured by cosine similarity) is a proxy for the degree of association between the two concepts.

---

### 4. Propose 10 cases that are not NLP where sequence modeling can be helpful.

Sequence modeling is vital for any domain where data points are dependent on previous data points:

1.  **Time Series Forecasting:** Predicting future stock prices based on historical market data.
2.  **Music Generation:** Generating a sequence of notes or chords to create a melody.
3.  **Video Classification:** Classifying the activity in a video (e.g., classifying a surgical procedure video by analyzing the sequence of actions).
4.  **Anomaly Detection in Sensor Data:** Detecting equipment failure patterns based on a sequence of temperature, pressure, or vibration readings.
5.  **Weather Forecasting:** Predicting future temperature, rainfall, etc., based on a sequence of atmospheric measurements.
6.  **Human Activity Recognition:** Identifying an activity (walking, jumping) from the sequence of accelerometer/gyroscope readings from a wearable device.
7.  **DNA/RNA Sequence Analysis:** Predicting protein folding or gene function based on the sequence of nucleotides.
8.  **Robotics Control:** Generating a sequence of motor commands for a robot arm to complete a complex task.
9.  **Reinforcement Learning (State Trajectories):** Modeling the sequence of states and actions taken by an agent in an environment.
10. **Financial Fraud Detection:** Analyzing the sequence of transactions made by a user to detect unusual temporal patterns.

---

### 5. We all loved Cloze tests in high school. Propose a modeling scheme to solve those.

A Cloze test requires filling in a blank word in a sentence. This is fundamentally a **Masked Language Modeling (MLM)** task, typically solved using a **Bidirectional Transformer Encoder** (like **BERT**).

| Scheme | Description | How it Works |
| :--- | :--- | :--- |
| **Bidirectional Encoder (BERT/RoBERTa)** | The preferred scheme, treating the task as filling a blank using surrounding context. | The model takes the input sentence with the blank word replaced by a special `[MASK]` token. Unlike RNNs, the encoder processes the entire sequence simultaneously and **bidirectionally**. The final layer produces a vector for the `[MASK]` position, which is then passed through a classification head (a linear layer followed by softmax) to predict the correct word from the entire vocabulary. |
| **Alternative (Seq2Seq):** | An encoder-decoder could be used, where the encoder processes the context (before the blank) and the decoder generates the missing word. | This is **less efficient** because the word's context *after* the blank is crucial. It only works if you structure the task as: (Prefix Text) $\rightarrow$ (Missing Word + Suffix Text). |

---

### 6. How can sequence modeling be used for zero-shot learning in NLP?

Sequence modeling enables zero-shot learning (ZSL) by leveraging the **pre-trained semantic knowledge** embedded in large sequence models (like GPT or Llama).

1.  **Instruction-Following:** The core method is to use a **seq2seq model** (a Transformer Decoder, often called a Large Language Model) and frame the unseen task as an instruction or prompt:
    * *Example ZSL Task:* Classify an email as "Urgent" or "Spam," where the model has never seen those labels.
    * *Prompt:* "Classify the following email into one of these categories: [Urgent, Spam, Personal]. Email: [Text of Email]."
2.  **Mechanism:** The model doesn't need task-specific training (zero-shot) because its vast pre-training corpus has taught it:
    * **Semantic Space:** The vector distance between the input text and the category labels.
    * **Instruction Adherence:** How to follow commands and reason about text based on a given structure.

The sequence model acts as a general knowledge engine capable of mapping unseen inputs to unseen outputs based purely on high-level instruction.

---

### 7. How is beam search different from Viterbi decoding?

Both Beam Search and Viterbi Decoding are algorithms used to find an optimal sequence, but they serve different purposes and have different guarantees.

| Feature | Beam Search | Viterbi Decoding |
| :--- | :--- | :--- |
| **Task** | Generative models (e.g., NMT, Summarization). | Statistical sequence models (e.g., HMM, CRF, simple RNNs). |
| **Goal** | Find a *highly probable* sequence in a very large (often infinite) search space. | Find the *single most probable* sequence of hidden states (e.g., POS tags) in a finite search space. |
| **Optimality** | **Heuristic.** Does **not guarantee** the global best sequence. | **Globally Optimal.** Guaranteed to find the sequence with the highest total probability. |
| **Complexity** | $O(T \cdot k \cdot V)$, where $k$ is the beam size and $V$ is vocabulary size. Much faster than exhaustive search. | $O(T \cdot N^2)$, where $N$ is the number of hidden states/labels. |

**In short:** Viterbi is a dynamic programming approach that finds the exact global optimum path efficiently for models with finite, observable states. Beam search is a pruning heuristic that finds a strong local optimum path for generative models with vast, branching possibilities.

---

### 8. Sequence modeling is often related to a progression in time (things happen in a specific order), however amount of time between steps is seldom used. Find examples (papers) where time between steps is used.

Standard RNNs and Transformers treat steps as uniform increments ($t, t+1, t+2$). Models that explicitly incorporate the **duration** or **time difference ($\Delta t$)** between events are crucial in domains like healthcare, finance, and system monitoring.

| Example Model/Paper                              | Domain                                 | Mechanism                                                                                                                                                                                             | URL                              |
| :----------------------------------------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| **T-LSTM (Time-Aware LSTM)**                     | Healthcare (Electronic Health Records) | Modifies the LSTM cell state to include a decay mechanism based on the time interval ($\Delta t$) since the last visit. Older information decays faster.                                              | https://arxiv.org/pdf/2010.00889 |
| **R-RNN (Recurrent-RNN)**                        | Time Series Modeling                   | The recurrence relation is modified to be an arbitrary function of the time interval ($\Delta t$), allowing the hidden state to change based on the elapsed time.                                     |                                  |
| **Neural ODE (Ordinary Differential Equations)** | Irregular Time Series                  | Replaces the discrete steps of an RNN with a continuous, learned differential equation that models the hidden state's evolution over continuous time, making $\Delta t$ intrinsic to the calculation. |                                  |
| **Transformer-XL / R-Transformer**               | Long Context NLP                       | While primarily focused on length, these often use complex **positional encodings** that can be adapted to encode temporal distance or $\Delta t$ between tokens.                                     |                                  |

---

### 9. Is attention relevant for models that are not seq2seq?

**Yes, absolutely.** Attention is a general mechanism for weighted averaging and is highly relevant in non-seq2seq architectures, especially those designed for representation learning or single-output tasks.

| Non-Seq2seq Use Case | Model/Mechanism | How Attention is Used |
| :--- | :--- | :--- |
| **Text Classification (Seq-to-One)** | Self-Attention (e.g., early BERT classification layers) | Attention is applied to the input sequence itself. It helps the model weigh the importance of different words in the sentence (e.g., focusing on "not great" when determining negative sentiment). |
| **Unsupervised Pre-training** | Bidirectional Self-Attention (e.g., BERT, RoBERTa) | Allows every token to interact with every other token to build a rich contextualized representation, independent of any generation task. |
| **Computer Vision** | Vision Transformers (ViT) | Images are broken into patches (sequences), and self-attention is used to understand the relationship between different spatial regions. |

---

### 10. Do we really need DL for sequence modeling?

**No, we don't *always* need Deep Learning (DL)**, but DL methods (RNNs, LSTMs, Transformers) provide superior performance on complex, long-range sequence tasks compared to traditional methods.

| Traditional Method | When to Use | Limitation |
| :--- | :--- | :--- |
| **N-gram Models** | Simple probability estimation, fast text generation, smoothing/backoff. | Cannot model long-range dependencies; prone to data sparsity. |
| **Hidden Markov Models (HMM)** | Part-of-Speech Tagging, Named Entity Recognition (simple, small scale). | Relies on strong independence assumptions; cannot model complex, non-linear relationships. |
| **Conditional Random Fields (CRF)** | Sequence Tagging (often used on top of DL features). | Cannot scale to complex seq2seq tasks like translation; feature engineering is required. |

**Conclusion:** For production-level sequence tasks involving complex semantics, long-range dependencies, and large data (e.g., Machine Translation, LLMs), **Deep Learning (specifically the Transformer architecture)** is necessary. For simpler tasks with limited data (e.g., simple POS tagging on a legacy system), traditional methods are often simpler and faster to implement.


# A2

Here is your worksheet on sequence modeling, with detailed explanations and code examples for each keyword and question.

## Keywords

### 1\. Recurrent Neural Networks (RNN)

  * **Main Idea:** A Recurrent Neural Network (RNN) is a class of neural network that contains a "loop," allowing information to persist. This internal memory makes it uniquely suited for processing sequences of data (like text, speech, or time series) where the context from previous steps is critical.
  * **How it works:**
    At each time step $t$, a standard "Elman" RNN cell performs two calculations:
    1.  **Hidden State:** It computes a new hidden state $h_t$ by combining the current input $x_t$ with the *previous* hidden state $h_{t-1}$. The states are combined using weight matrices ($W_{xh}$ for input, $W_{hh}$ for hidden) and passed through a non-linear activation function (usually $\tanh$).
        $$h_t = \tanh(W_{xh} x_t + W_{hh} h_{t-1} + b_h)$$
    2.  **Output:** It produces an optional output $y_t$ for the current step, typically by applying another weight matrix ($W_{hy}$) and activation function (e.g., `softmax` for classification) to the new hidden state.
        $$y_t = W_{hy} h_t + b_y$$
        The crucial part is that $h_t$ is fed back into the cell at time step $t+1$, creating the recurrent loop that acts as the model's memory.
  * **Variations:**
      * **Bidirectional RNN (BiRNN):** Processes the sequence in two directions (forward and backward) and concatenates the hidden states. This gives the model context from both the past and the future for any given step.
      * **Deep (Stacked) RNN:** Stacks multiple RNN layers, where the output sequence of one layer becomes the input sequence for the next.
  * **Code Example (PyTorch):**
    ```python
    import torch
    import torch.nn as nn

    # --- Model Parameters ---
    input_size = 10   # Dimension of each input vector (e.g., embedding dim)
    hidden_size = 20  # Dimension of the hidden state
    num_layers = 2    # Number of stacked RNN layers

    # --- Create an RNN instance ---
    # batch_first=True means input/output shape is (batch_size, seq_len, dim)
    # This is more intuitive than the default (seq_len, batch_size, dim)
    rnn = nn.RNN(
        input_size=input_size, 
        hidden_size=hidden_size, 
        num_layers=num_layers, 
        batch_first=True,
        bidirectional=True
    )

    # --- Prepare Input Data ---
    batch_size = 5
    seq_len = 7
    # (batch_size, sequence_length, input_features)
    inputs = torch.randn(batch_size, seq_len, input_size)

    # Initialize hidden state: (num_layers * num_directions, batch_size, hidden_size)
    # num_directions = 2 for bidirectional
    h0 = torch.randn(num_layers * 2, batch_size, hidden_size)

    # --- Forward Pass ---
    # 'output' contains the hidden state for *every* time step
    # 'hn' is the *final* hidden state from the last time step
    output, hn = rnn(inputs, h0)

    print(f"Input shape:  {inputs.shape}")
    print(f"Output shape: {output.shape}") # (batch, seq_len, hidden * num_directions)
    print(f"Final Hidden shape: {hn.shape}")  # (layers * directions, batch, hidden)
    ```

-----

### 2\. Long Short-Term Memory (LSTM)

  * **Main Idea:** A highly advanced RNN cell designed specifically to combat the vanishing/exploding gradient problem. This allows it to learn *long-range dependencies* (e.g., connecting a subject at the start of a paragraph to a verb at the end) far more effectively than a simple RNN.
  * **How it works:**
    An LSTM maintains *two* states: the hidden state $h_t$ (short-term memory) and a **cell state** $C_t$ (long-term memory). Its operations are controlled by three "gates":
    1.  **Forget Gate ($f_t$):** A sigmoid layer that looks at $h_{t-1}$ and $x_t$. It decides what percentage of the long-term memory $C_{t-1}$ to *discard*.
        $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
    2.  **Input Gate ($i_t$) & Candidate Gate ($\tilde{C}_t$):** The input gate is a sigmoid layer that decides which *new* values to update. The candidate gate ($\tanh$ layer) creates a vector of new candidate values $\tilde{C}_t$.
        $$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
        $$\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$$
    3.  **Cell State Update:** The old cell state is updated to the new cell state $C_t$ by forgetting old info and adding new info.
        $$C_t = (f_t \odot C_{t-1}) + (i_t \odot \tilde{C}_t)$$
    4.  **Output Gate ($o_t$):** A sigmoid layer that decides what part of the new cell state $C_t$ to output as the new hidden state $h_t$.
        $$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
        $$h_t = o_t \odot \tanh(C_t)$$
  * **Variations:**
      * **Peephole LSTMs:** The gate layers are also given access to the cell state $C_t$.
      * **Bidirectional LSTM (BiLSTM):** Same as BiRNN, but uses LSTM cells.
  * **Code Example (PyTorch):**
    ```python
    import torch
    import torch.nn as nn

    input_size = 10
    hidden_size = 20
    num_layers = 2

    # The API is very similar to nn.RNN
    lstm = nn.LSTM(
        input_size=input_size, 
        hidden_size=hidden_size, 
        num_layers=num_layers, 
        batch_first=True
    )

    # --- Prepare Input Data ---
    batch_size = 5
    seq_len = 7
    inputs = torch.randn(batch_size, seq_len, input_size)

    # LSTM requires *two* initial states: (hidden, cell)
    # h0 shape: (num_layers * num_directions, batch_size, hidden_size)
    h0 = torch.randn(num_layers, batch_size, hidden_size)
    # c0 shape: (num_layers * num_directions, batch_size, hidden_size)
    c0 = torch.randn(num_layers, batch_size, hidden_size)

    # --- Forward Pass ---
    # 'output' contains the hidden state h_t for every time step
    # 'hn' is the final hidden state
    # 'cn' is the final cell state
    output, (hn, cn) = lstm(inputs, (h0, c0))

    print(f"Input shape:  {inputs.shape}")
    print(f"Output shape: {output.shape}") # (batch, seq_len, hidden)
    print(f"Final Hidden shape: {hn.shape}")  # (layers, batch, hidden)
    print(f"Final Cell shape:   {cn.shape}")  # (layers, batch, hidden)
    ```

-----

### 3\. Gated Recurrent Units (GRU)

  * **Main Idea:** A simplification of the LSTM that also addresses the vanishing gradient problem. It combines the LSTM's forget and input gates into a single "update gate" and merges the cell state and hidden state, resulting in a model that is computationally cheaper and often performs just as well.
  * **How it works:**
    A GRU has only *two* gates and one hidden state $h_t$:
    1.  **Reset Gate ($r_t$):** A sigmoid layer that decides how much of the *previous* hidden state $h_{t-1}$ to *forget* when calculating the new candidate state $\tilde{h}_t$.
        $$r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)$$
    2.  **Candidate State ($\tilde{h}_t$):** The new candidate hidden state is computed using *only* the part of $h_{t-1}$ that the reset gate allowed.
        $$\tilde{h}_t = \tanh(W_h \cdot [r_t \odot h_{t-1}, x_t] + b_h)$$
    3.  **Update Gate ($z_t$):** A sigmoid layer that decides the *interpolation* between the old state $h_{t-1}$ and the new candidate $\tilde{h}_t$. It acts like both the forget and input gates of an LSTM.
        $$z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)$$
    4.  **Hidden State Update:** The final state $h_t$ is a convex combination (a blend) of the previous state and the candidate state.
        $$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
  * **Variations:**
      * **Bidirectional GRU (BiGRU):** Processes the sequence in both directions.
  * **Code Example (PyTorch):**
    ```python
    import torch
    import torch.nn as nn

    input_size = 10
    hidden_size = 20
    num_layers = 2

    # The API is simpler than LSTM (no cell state)
    gru = nn.GRU(
        input_size=input_size, 
        hidden_size=hidden_size, 
        num_layers=num_layers, 
        batch_first=True
    )

    # --- Prepare Input Data ---
    batch_size = 5
    seq_len = 7
    inputs = torch.randn(batch_size, seq_len, input_size)

    # GRU only requires one initial hidden state
    h0 = torch.randn(num_layers, batch_size, hidden_size)

    # --- Forward Pass ---
    # 'output' contains the hidden state h_t for every time step
    # 'hn' is the final hidden state
    output, hn = gru(inputs, h0)

    print(f"Input shape:  {inputs.shape}")
    print(f"Output shape: {output.shape}") # (batch, seq_len, hidden)
    print(f"Final Hidden shape: {hn.shape}")  # (layers, batch, hidden)
    ```

-----

### 4\. Encoder-Decoder Model

  * **Main Idea:** An architecture (also called **seq2seq**) designed to map an input sequence of variable length to an output sequence of variable length (e.g., machine translation). It consists of two main components: an Encoder and a Decoder.
  * **How it works:**
    1.  **Encoder:** An RNN (or LSTM/GRU) reads the *entire* input sequence one step at a time (e.g., "Hello world"). It discards the outputs from each step and only keeps its *final* hidden (and cell) state. This final state vector is called the "context vector" (or "thought vector") and serves as a numerical summary of the entire input.
    2.  **Decoder:** A separate RNN is initialized with the Encoder's final hidden state. It is then fed a special `<SOS>` (start-of-sequence) token. Its task is to generate the output sequence one token at a time (e.g., "Bonjour"). The output from step $t$ is fed as the input to step $t+1$, in a process called "auto-regression," until it generates an `<EOS>` (end-of-sequence) token.
  * **Variations:**
      * **Vanilla Encoder-Decoder:** Uses a single, fixed-size context vector. This is a bottleneck for long sequences.
      * **Attention-based Encoder-Decoder:** The Decoder is allowed to "look back" at *all* of the Encoder's hidden states at each step, not just the final one.
  * **Code Example (PyTorch):**
    ```python
    import torch
    import torch.nn as nn

    class Encoder(nn.Module):
        def __init__(self, input_dim, embed_dim, hidden_dim, layers):
            super().__init__()
            self.embedding = nn.Embedding(input_dim, embed_dim)
            self.rnn = nn.LSTM(embed_dim, hidden_dim, layers, batch_first=True)
            
        def forward(self, src):
            # src shape: (batch_size, seq_len)
            embedded = self.embedding(src) # (batch_size, seq_len, embed_dim)
            # We only care about the final hidden/cell states
            outputs, (hidden, cell) = self.rnn(embedded)
            # hidden/cell shapes: (layers, batch_size, hidden_dim)
            return hidden, cell

    class Decoder(nn.Module):
        def __init__(self, output_dim, embed_dim, hidden_dim, layers):
            super().__init__()
            self.output_dim = output_dim
            self.embedding = nn.Embedding(output_dim, embed_dim)
            self.rnn = nn.LSTM(embed_dim, hidden_dim, layers, batch_first=True)
            self.fc_out = nn.Linear(hidden_dim, output_dim)
            
        def forward(self, input, hidden, cell):
            # input shape: (batch_size) -> a single token
            # hidden/cell shapes: (layers, batch_size, hidden_dim)
            input = input.unsqueeze(1) # (batch_size) -> (batch_size, 1)
            embedded = self.embedding(input) # (batch_size, 1, embed_dim)
            
            output, (hidden, cell) = self.rnn(embedded, (hidden, cell))
            
            # output shape: (batch_size, 1, hidden_dim)
            prediction = self.fc_out(output.squeeze(1)) # (batch_size, output_dim)
            return prediction, hidden, cell

    # --- Example Usage ---
    INPUT_DIM = 1000  # Source vocab size
    OUTPUT_DIM = 1200 # Target vocab size
    EMBED_DIM = 256
    HIDDEN_DIM = 512
    LAYERS = 2

    encoder = Encoder(INPUT_DIM, EMBED_DIM, HIDDEN_DIM, LAYERS)
    decoder = Decoder(OUTPUT_DIM, EMBED_DIM, HIDDEN_DIM, LAYERS)

    src_seq = torch.randint(0, INPUT_DIM, (5, 10)) # (batch=5, seq_len=10)
    trg_token = torch.randint(0, OUTPUT_DIM, (5,)) # (batch=5)

    hidden, cell = encoder(src_seq)
    prediction, hidden, cell = decoder(trg_token, hidden, cell)

    print(f"Source sequence shape: {src_seq.shape}")
    print(f"Decoder output prediction shape: {prediction.shape}")
    ```

-----

### 5\. Attention

  * **Main Idea:** A mechanism that allows a model (like a seq2seq Decoder) to *selectively focus* on different parts of its input. Instead of compressing the entire input into one fixed "context vector," attention gives the model access to the *entire* input sequence at every step and lets it decide which parts are most relevant for generating the current output token.
  * **How it works:**
    At each step $t$ in the Decoder:
    1.  We have the Decoder's current "query" state (e.g., its hidden state $s_t$).
    2.  We have the Encoder's "keys" and "values" (for seq2seq, these are both just the set of all encoder hidden states $\{h_1, ..., h_N\}$).
    3.  **Score:** The Decoder's query state $s_t$ is scored against *every* encoder key $h_i$ to get an "alignment score" $e_{ti} = \text{score}(s_t, h_i)$.
    4.  **Weights:** The scores are passed through a `softmax` to create attention weights $\alpha_{ti}$, which sum to 1.
        $$\alpha_{ti} = \frac{\exp(e_{ti})}{\sum_{j=1}^N \exp(e_{tj})}$$
    5.  **Context:** A *dynamic* context vector $c_t$ is computed as the weighted sum of the encoder *values* (the hidden states $h_i$).
        $$c_t = \sum_{i=1}^N \alpha_{ti} h_i$$
    6.  **Predict:** This dynamic $c_t$ (which focuses on the relevant input words for this step) is concatenated with the Decoder's hidden state $s_t$ and fed to a final layer to predict the output word.
  * **Variations:**
      * **Bahdanau (Additive) Attention:** The $\text{score}$ function is a small feed-forward network: $e_{ti} = v_a^\top \tanh(W_s s_{t-1} + W_h h_i)$. It is computed *before* the decoder's RNN cell.
      * **Luong (Multiplicative) Attention:** The $\text{score}$ function is simpler, like `dot` ($s_t^\top h_i$) or `general` ($s_t^\top W h_i$). It is computed *after* the decoder's RNN cell, using its new hidden state $s_t$.
      * **Cross-Attention:** This is the *name* for the attention described above (Decoder attending to Encoder).
      * **Self-Attention:** A different type where a sequence attends *to itself* to build context. This is the core component of the **Transformer**.
  * **Code Example (PyTorch - Luong 'general' attention):**
    ```python
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    class Attention(nn.Module):
        def __init__(self, hidden_dim):
            super().__init__()
            # 'general' score: query^T @ W @ keys
            self.attn = nn.Linear(hidden_dim, hidden_dim, bias=False)
            
        def forward(self, decoder_hidden, encoder_outputs):
            # decoder_hidden shape: (batch_size, hidden_dim)
            # encoder_outputs shape: (batch_size, seq_len, hidden_dim)
            
            # Project decoder_hidden to match encoder_outputs
            # (batch, hidden) -> (batch, hidden)
            query = self.attn(decoder_hidden)
            
            # (batch, hidden) -> (batch, hidden, 1)
            query = query.unsqueeze(2)
            
            # (batch, seq_len, hidden) @ (batch, hidden, 1) -> (batch, seq_len, 1)
            scores = torch.bmm(encoder_outputs, query).squeeze(2)
            
            # weights shape: (batch_size, seq_len)
            weights = F.softmax(scores, dim=1)
            
            # (batch, 1, seq_len) @ (batch, seq_len, hidden) -> (batch, 1, hidden)
            context = torch.bmm(weights.unsqueeze(1), encoder_outputs)
            
            # context shape: (batch_size, hidden_dim)
            return context.squeeze(1), weights

    # --- Example Usage ---
    HIDDEN_DIM = 512
    BATCH_SIZE = 5
    SEQ_LEN = 10

    attention = Attention(HIDDEN_DIM)

    # Decoder's *current* hidden state
    dec_hidden = torch.randn(BATCH_SIZE, HIDDEN_DIM)

    # *All* hidden states from the encoder
    enc_outputs = torch.randn(BATCH_SIZE, SEQ_LEN, HIDDEN_DIM)

    context, weights = attention(dec_hidden, enc_outputs)

    print(f"Decoder Hidden shape: {dec_hidden.shape}")
    print(f"Encoder Outputs shape: {enc_outputs.shape}")
    print(f"Context Vector shape: {context.shape}")
    print(f"Attention Weights shape: {weights.shape}")
    ```

-----

### 6\. Beam Search

  * **Main Idea:** A decoding algorithm used during inference (generation) for seq2seq models. It is a heuristic search that explores multiple possible output sequences simultaneously, finding a much better (higher probability) translation than simple "greedy search" (which just picks the single best word at each step).
  * **How it works:**
    It maintains a "beam" of $k$ (the "beam width") most probable *partial* sequences.
    1.  **Step 0:** Start with $k$ beams, all consisting of just the `<SOS>` token.
    2.  **Step 1:** Run the decoder for all $k$ beams. This generates $k$ probability distributions over the vocabulary.
    3.  **Expand:** Consider all $k \times \text{vocab\_size}$ possible next words.
    4.  **Prune:** Calculate the cumulative log-probability for all these new, one-word-longer sequences. Keep only the **top $k$** most probable sequences.
    5.  **Repeat:** These $k$ new sequences become the beams for the next step.
    6.  **Stop:** The process continues until all $k$ beams have generated an `<EOS>` token. The completed sequence with the highest overall probability is chosen as the final result.
  * **Variations:**
      * **Length Penalty:** A modification that penalizes longer sequences to prevent the model from favoring short, "safe" outputs.
      * **Coverage Penalty:** Discourages the model from attending to the same input word multiple times.
  * **Code Example (Conceptual - a full implementation is very complex):**
    ```python
    import torch

    # --- Conceptual Beam Search (Simplified) ---
    # Assume 'model' is a trained seq2seq model
    # model.decode_step(input_token, prev_hidden) -> (logits, new_hidden)

    BEAM_WIDTH = 3
    vocab_size = 1000

    # Start with <SOS> token (ID=1)
    # Beams store (cumulative_log_prob, sequence, hidden_state)
    beams = [(0.0, [1], initial_hidden_state)] 

    # --- Run for a fixed number of steps (e.g., max_len) ---
    for _ in range(10): # Max sequence length
        all_candidates = []
        for log_prob, seq, hidden in beams:
            # If sequence ended, just add it to candidates
            if seq[-1] == 2: # <EOS> token ID
                all_candidates.append((log_prob, seq, hidden))
                continue
                
            # Get logits and new hidden state from the model
            last_token = torch.tensor([seq[-1]])
            logits, new_hidden = model.decode_step(last_token, hidden)
            
            # Convert to log probabilities
            log_probs = F.log_softmax(logits, dim=-1).squeeze()
            
            # Add top k new candidates
            top_log_probs, top_indices = log_probs.topk(BEAM_WIDTH)
            
            for i in range(BEAM_WIDTH):
                new_seq = seq + [top_indices[i].item()]
                new_log_prob = log_prob + top_log_probs[i].item()
                all_candidates.append((new_log_prob, new_seq, new_hidden))
        
        # Prune: Keep only the top k beams overall
        ordered = sorted(all_candidates, key=lambda x: x[0], reverse=True)
        beams = ordered[:BEAM_WIDTH]
        
    # Final result is the top beam
    best_log_prob, best_seq, _ = beams[0]
    print(f"Best sequence: {best_seq}")
    ```

-----

### 7\. Zero-Shot Learning

  * **Main Idea:** A learning paradigm where a model can successfully perform a task *it was not explicitly trained on*. In NLP, this typically means classifying text into categories or topics that were not part of the training data.
  * **How it works:**
    This is most powerfully demonstrated with models trained on **Natural Language Inference (NLI)**, which is the task of determining if a "premise" *entails*, *contradicts*, or is *neutral* to a "hypothesis".
    To perform zero-shot classification:
    1.  **Input (Premise):** "This was a fantastic movie, I loved it."
    2.  **Hypotheses:** You create hypotheses from your desired labels:
          * "This text is about *cinema*."
          * "This text is about *sports*."
          * "This text is about *politics*."
    3.  **Inference:** You run the NLI model on each `(premise, hypothesis)` pair.
    4.  **Result:** The model will output a high "entailment" score for the "cinema" hypothesis, effectively "classifying" the input text without ever having been trained on that specific label.
  * **Variations:**
      * **Prompting (with LLMs):** Using models like GPT-3 by formatting the task as a text completion prompt (e.g., `Text: "I hated it" \nSentiment: Negative \nText: "I loved it" \nSentiment:` and letting the model complete `Positive`).
  * **Code Example (using Hugging Face `transformers`):**
    ```python
    from transformers import pipeline

    # This downloads a model pre-trained on NLI
    # and configured for this specific task
    classifier = pipeline("zero-shot-classification", 
                              model="facebook/bart-large-mnli")

    sequence_to_classify = "The CEO announced a record-breaking quarter."

    candidate_labels = ["politics", "finance", "sports", "technology"]

    result = classifier(sequence_to_classify, candidate_labels)

    print(f"Sequence: '{sequence_to_classify}'")
    print("Results:")
    print(f"Labels: {result['labels']}")
    print(f"Scores: {[round(s, 3) for s in result['scores']]}")

    # Expected Output: 'finance' will have the highest score.
    ```

-----

## Questions

### 1\. What is a "forget gate" in LSTM, and how is it different in GRU?

  * **Short Answer:** The LSTM's "forget gate" ($f_t$) is a sigmoid-activated vector that decides what percentage of the *long-term cell state* ($C_{t-1}$) to keep vs. discard. GRU doesn't have a separate forget gate; it combines this function into its "update gate" ($z_t$), which directly interpolates between the *previous hidden state* ($h_{t-1}$) and the *new candidate state* ($\tilde{h}_t$).

  * **Long Answer:**
    In an **LSTM**, the forget gate $f_t$ is computed based on the previous hidden state $h_{t-1}$ and the current input $x_t$. Its output is a vector of numbers between 0 and 1. This vector is then element-wise multiplied ($\odot$) with the previous cell state $C_{t-1}$.
    $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
    $$C_{t, \text{forgotten_part}} = f_t \odot C_{t-1}$$
    A '1' in $f_t$ means "keep 100% of this memory," and a '0' means "completely forget this memory." This explicitly protects and controls the long-term memory.

    A **GRU** has no separate cell state $C_t$. Its "memory" is its single hidden state $h_t$. It has two gates:

    1.  **Reset Gate ($r_t$):** This gate "forgets" parts of the *previous hidden state* $h_{t-1}$ *before* it's used to calculate the new candidate $\tilde{h}_t$.
    2.  **Update Gate ($z_t$):** This gate acts as a "blender." It decides how much of $h_{t-1}$ to keep and how much of $\tilde{h}_t$ to add. The final state is a direct interpolation:
        $$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
        So, $1-z_t$ acts as the "forget" mechanism for the previous state, and $z_t$ acts as the "input" mechanism for the new state. It's a simpler, coupled design.

-----

### 2\. Which NLP tasks are considered seq2seq? Is sequence modeling always seq2seq?

  * **Short Answer:** Seq2seq tasks are any tasks that map a variable-length input sequence to a variable-length output sequence. Common examples include **Machine Translation**, **Text Summarization**, **Conversational AI (Chatbots)**, and **Question Answering**.
    And **no**, sequence modeling is not always seq2seq.
  * **Long Answer:**
    "Sequence Modeling" is a broad term for any model that operates on sequential data. "Seq2seq" is a *specific architecture* for a subset of these tasks.
    Other types of sequence modeling tasks include:
      * **Sequence-to-Vector (Many-to-One):** The input is a sequence, but the output is a single, fixed vector.
          * **Example:** Sentiment Analysis (Input: "I loved this movie" $\rightarrow$ Output: "Positive").
          * **Example:** Text Classification (Input: "CEO announces profits" $\rightarrow$ Output: "Finance").
      * **Vector-to-Sequence (One-to-Many):** The input is a single, fixed vector, and the output is a sequence.
          * **Example:** Image Captioning (Input: `[vector_for_image.jpg]` $\rightarrow$ Output: "A cat sitting on a mat").
      * **Sequence-to-Sequence (Many-to-Many, Aligned):** The input and output are sequences of the *same length*, and each output $y_t$ corresponds directly to $x_t$.
          * **Example:** Part-of-Speech Tagging (Input: "The cat sat" $\rightarrow$ Output: "DET NOUN VERB").
          * **Example:** Named Entity Recognition (Input: "Jane lives in London" $\rightarrow$ Output: "B-PER O O B-LOC").

-----

### 3\. What is the meaning of 2 different words being very close vectors in the embedding?

  * **Short Answer:** It means the two words are used in very similar contexts and are therefore **semantically related**.
  * **Long Answer:**
    This is the core principle of the **Distributional Hypothesis** ("a word is characterized by the company it keeps"). Word embedding models (like Word2Vec) are trained to learn a vector for a word based on its surrounding words. If two different words (e.g., "king" and "queen") are frequently surrounded by a similar set of other words (e.g., "majesty," "throne," "palace," "reign"), the model will be forced to learn very similar vectors for them to be effective at its prediction-based training task.
    This "closeness" can represent several types of semantic relationships:
      * **Synonyms:** "happy" and "joyful"
      * **Co-hyponyms (related items):** "cat" and "dog" (both pets, found with "food," "walk," "animal")
      * **Antonyms:** "hot" and "cold" (both used in contexts like "the weather is...", "this water is...")
      * **Related Verbs/Nouns:** "run" and "runner"

-----

### 4\. Propose 10 cases that are not NLP where sequence modeling can be helpful.

  * **Short Answer:** Stock market prediction, weather forecasting, medical signal analysis (EKG/EEG), music generation, video action recognition, DNA analysis, robotics, server log analysis, clickstream prediction, and speech-to-text.
  * **Long Answer:**
    1.  **Financial Time Series:** Predicting stock prices, market volatility, or trading volumes based on a sequence of historical data.
    2.  **Weather Forecasting:** Predicting future temperature, humidity, and precipitation based on a sequence of past satellite, radar, and sensor readings.
    3.  **Medical Signal Processing:** Analyzing EKG (heart) or EEG (brain) signals as sequences to detect anomalies, seizures, or other medical conditions.
    4.  **Music Generation:** Generating a new musical piece (a sequence of notes, chords, and timings) by learning patterns from existing music.
    5.  **Video Action Recognition:** Classifying an action in a video (e.g., "running," "jumping") by treating the video as a sequence of image frames.
    6.  **Genomics & Proteomics:** Analyzing DNA (a sequence of base pairs A, C, G, T) or protein (a sequence of amino acids) to predict gene function or protein folding.
    7.  **Robotics:** Planning the path of a robotic arm as a sequence of joint angles and movements to smoothly and efficiently reach a target.
    8.  **Anomaly Detection in Logs:** Monitoring sequences of server log messages or sensor readings to detect unusual patterns that could indicate a failure, cyberattack, or system fault.
    9.  **User Behavior Analysis:** Predicting a user's next action (e.g., "add to cart," "checkout") on a website based on their sequence of previous clicks ("clickstream").
    10. **Speech-to-Text (ASR):** While it involves language, the *input* is not text but a sequence of audio frames (spectrograms) which are mapped to a sequence of text characters.

-----

### 5\. We all loved Cloze tests in high school. Propose a modeling scheme to solve those.

  * **Short Answer:** Use a pre-trained **Masked Language Model (MLM)** like **BERT**.
  * **Long Answer:**
    The "Cloze test" (filling in a blank in a sentence) is *exactly* the pre-training objective of BERT, known as **Masked Language Modeling**.
    1.  **Model:** You would use a pre-trained `bert-base-cased` (or similar) model and its corresponding tokenizer.
    2.  **Input:** Take the Cloze sentence, e.g., "The cat sat on the \_\_\_\_ and fell asleep."
    3.  **Tokenization:** Tokenize the sentence, which will replace the blank with the special `[MASK]` token: `['The', 'cat', 'sat', 'on', 'the', '[MASK]', 'and', 'fell', 'asleep', '.']`
    4.  **Inference:** Pass these token IDs through the BERT model. The model's output is a set of logits (scores) for *every* token in the vocabulary, at *every* position.
    5.  **Prediction:** You simply extract the logits for the `[MASK]` token's position. The token with the highest score (after a `softmax`) is the model's prediction for the blank. Common predictions would be "mat," "couch," "floor," etc.

-----

### 6\. How can sequence modeling be used for zero-shot learning in NLP?

  * **Short Answer:** By reframing the desired zero-shot task (like classification) into a format that the sequence model *was* trained on (like **Natural Language Inference** or **Masked Language Modeling / Text Generation**).
  * **Long Answer:**
    There are two primary methods:
    1.  **Using NLI Models (like in Keyword \#7):** You use a model (like BERT or BART trained on MNLI) that was pre-trained to determine if a "premise" *entails* a "hypothesis." To classify a new text (the premise), you create candidate "hypotheses" from your labels (e.g., "This text is about finance"). The label whose hypothesis gets the highest "entailment" score wins. This is a sequence-to-vector model (NLI) being cleverly reused.
    2.  **Using Generative/Prompt-based Models (like GPT):** You use a large-scale language model (LLM) that was trained to predict the next token in a sequence. You can "prompt" the model in a zero-shot way by formatting the task as a text-completion problem:
        ```
        Text: "This movie was a masterpiece."
        What is the sentiment of this text?
        Answer: Positive

        Text: "This movie was a total disaster."
        What is the sentiment of this text?
        Answer: 
        ```
        The model's highest probability completion will be "Negative", effectively performing zero-shot classification.

-----

### 7\. How is beam search different from Viterbi decoding?

  * **Short Answer:** **Viterbi** is an *exact* dynamic programming algorithm that is *guaranteed* to find the single most probable sequence. It only works for models with the Markov property (like HMMs). **Beam Search** is a *heuristic* (approximate) search algorithm that is *not* guaranteed to find the most probable sequence. It's used for complex models like RNNs and Transformers where an exact search is computationally intractable.
  * **Long Answer:**
      * **Viterbi:** Works on models like Hidden Markov Models (HMMs) where the probability of a state at step $t$ depends *only* on the state at $t-1$ and the current observation. This "Markov property" allows you to build a table and find the optimal path in polynomial time ($O(N^2 \cdot T)$, where $N$ is states, $T$ is steps). It is *complete and optimal*.
      * **Beam Search:** Used for models like RNNs and Transformers where the probability of a word at step $t$ depends on *all* previous words and the *entire* input sequence (via the hidden state/attention). The number of possible sequences is $(\text{vocab\_size})^T$, which is exponential and impossible to search. Beam search is an *approximation* that prunes this massive search tree by only keeping the top $k$ (beam width) most-likely hypotheses at each step. It is *incomplete and not optimal*, but it's far better than greedy search and is computationally feasible.

-----

### 8\. Sequence modeling is often related to a progression in time, however amount of time between steps is seldom used. Find examples (papers) where time between steps is used.

  * **Short Answer:** Yes, this is a well-known sub-field, particularly for "irregularly-sampled" time series. Models like the **Phased LSTM** (PLSTM) and **Neural Ordinary Differential Equations (Neural ODEs)** are designed for this.
  * **Long Answer:**
    This is a critical problem in real-world data, such as medical records (a patient has visits 3 days apart, then 6 months apart) or financial transactions (which occur sporadically).
    1.  **Phased LSTM (PLSTM):**
          * **Paper:** "Phased LSTM: Accelerating Recurrent Network Training for Long or Irregularly Sampled Time Series" (Neil et al., 2017).
          * **How it works:** It adds a new "time gate" ($k_t$) to the LSTM. This gate is controlled by a rhythmic oscillation, and its "open" and "closed" phases are determined by the *actual timestamp* ($\Delta t$) of the input. The LSTM's cell and hidden states are *only* updated when the time gate is open. This allows the model to learn different behaviors for short vs. long time gaps.
    2.  **Neural Continuous-Time Models (Neural ODEs):**
          * **Paper:** "Neural Ordinary Differential Equations" (Chen et al., 2018).
          * **How it works:** This is a more profound approach. Instead of modeling discrete steps $h_t$, it models the *continuous* evolution of the hidden state $h(t)$ as a differential equation $dh(t)/dt = f(h(t), t)$. To get the state at any future time $T$, it uses a numerical ODE solver to integrate this function from the start time. This naturally handles any irregular time gap.

-----

### 9\. Is attention relevant for models that are not seq2seq?

  * **Short Answer:** Yes, absolutely. **Self-Attention** is the core component of the Transformer model, which is now the state-of-the-art for non-seq2seq tasks like text classification and sentiment analysis. It's also widely used in computer vision.
  * **Long Answer:**
    "Attention" is a general mechanism for computing a weighted sum of features, where the weights are dynamically computed based on relevance.
      * **Text Classification (Many-to-One):** A model can use **self-attention** to read an entire sentence and weigh the importance of different words for its final classification. For example, in "The acting was great, but the plot was terrible," a self-attention mechanism can learn to attend most strongly to "great" and "terrible" (and their modifier "but") to make a "Mixed" or "Negative" sentiment prediction.
      * **Computer Vision (ViT):** The Vision Transformer (ViT) model discards CNNs entirely. It breaks an image into a sequence of 16x16 "patches" and feeds them into a Transformer. The self-attention layers allow different *image patches* to "look at" and "communicate with" each other to build up a global understanding of the image content.
      * **Cross-Modal (Image Captioning):** In a one-to-many task like image captioning, the decoder (generating text) uses **cross-attention** to "look at" different *regions* of the input image (not an input *sequence*) as it generates each word.

-----

### 10\. Do we really need DL for sequence modeling?

  * **Short Answer:** No, we don't *need* it, but it is by far the most powerful and flexible tool we have.

  * **Long Answer:**
    Before the rise of Deep Learning (RNNs, Transformers), sequence modeling was a cornerstone of classical statistics and machine learning. These "classical" models are still used and are very effective, especially for smaller datasets where DL models might overfit.

      * **n-gram Models:** A simple statistical model that predicts the next word based *only* on the previous $n-1$ words. (e.g., a 3-gram model for "the cat sat on \_\_\_" would look at all trigrams in its training data that start with "sat on").
      * **Hidden Markov Models (HMMs):** A probabilistic model that assumes an observed sequence (e.g., words) is generated by a sequence of *unobserved* (hidden) states (e.g., part-of-speech tags). They were the standard for speech recognition and PoS tagging for decades.
      * **Conditional Random Fields (CRFs):** A graphical model that is an improvement on HMMs. It's particularly good at "aligned" seq-to-seq tasks like Named Entity Recognition because it can model the probability of the *entire* tag sequence at once, capturing dependencies between labels (e.g., "a B-PER tag cannot follow an I-ORG tag").

    The primary advantage of DL models is that they learn their own *features* (embeddings) from raw data and can capture extremely complex, long-range, non-linear dependencies that are beyond the scope of these classical models.