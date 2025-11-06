The weight matrix for the first hidden layer, \( W^{[1]} \), has dimensions \( p \times (n+1) \), where \( p \) is the number of neurons in the hidden layer, and \( n \) is the number of input features (dimensions of the dataset). The \( +1 \) in the second dimension accounts for the bias term included in the matrix formulation.

In neural networks, each neuron in a layer computes a weighted sum of inputs plus a bias: $\( z_{ik} = \sum_{j=1}^n w_{kj} x_{ij} + b_k \)$. To incorporate the bias into the matrix formulation, we augment the input data matrix $\( X \in \mathbb{R}^{n \times m} \)$ (where $\( m \)$ is the number of samples) by adding a row of ones, creating an augmented input matrix $\( X_{\text{aug}} \in \mathbb{R}^{(n+1) \times m} \)$:
$$
\[ X_{\text{aug}} = \begin{bmatrix}
x_1^1 & x_2^1 & \cdots & x_m^1 \\
x_1^2 & x_2^2 & \cdots & x_m^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_1^n & x_2^n & \cdots & x_m^n \\
1 & 1 & \cdots & 1
\end{bmatrix} \]
$$
The weight matrix $\( W^{[1]} \in \mathbb{R}^{p \times (n+1)} \)$ then includes weights for each of the $\( n \)$ input features plus an additional column for the bias terms for each of the \( p \) neurons:
$$
\[ W^{[1]} = \begin{bmatrix}
w_{11}^{[1]} & w_{12}^{[1]} & \cdots & w_{1n}^{[1]} & b_1 \\
w_{21}^{[1]} & w_{22}^{[1]} & \cdots & w_{2n}^{[1]} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
w_{p1}^{[1]} & w_{p2}^{[1]} & \cdots & w_{pn}^{[1]} & b_p
\end{bmatrix} \]
$$
Here, the last column of \( $W^{[1]}$ \) represents the biases \( $b_1, b_2, \ldots, b_p$ \). This allows the computation \( $Z^{[1]} = W^{[1]} \cdot X_{\text{aug}}$ \), where the bias is seamlessly included in the matrix multiplication, eliminating the need to handle it separately. Thus, the \( $+1$ \) comes from this augmentation to incorporate the bias term for each neuron in the hidden layer.

---

## Overview

This package provides LangChain support for Google Gemini models (via the official [Google Generative AI SDK](https://googleapis.github.io/python-genai/)). It supports:

- Text and vision-based chat models
- Embeddings for semantic search
- Multimodal inputs and outputs
- Retrieval-Augmented Generation (RAG)
- Thought tracing with reasoning tokens

---

## Installation

```
pip install -U langchain-google-genai
```

---

## Quickstart

Set up your environment variable with your Gemini API key:

```
export GOOGLE_API_KEY=your-api-key
```

Then use the `ChatGoogleGenerativeAI` interface:

```
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
response = llm.invoke("Sing a ballad of LangChain.")
print(response.content)
```

---

## Chat Models

The main interface for Gemini chat models is `ChatGoogleGenerativeAI`.

### Multimodal Inputs

Gemini vision models support image inputs in single messages.
```
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {"type": "text", "text": "What's in this image?"},
        {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
    ]
)

response = llm.invoke([message])
print(response.content)
```

✅ `image_url` can be:

- A public image URL
- A Google Cloud Storage path (`gcs://...`)
- A base64-encoded image (e.g., `data:image/png;base64,...`)

---

### Multimodal Outputs

The Gemini 2.0 Flash Experimental model supports both text and inline image outputs.

```
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-exp-image-generation")

response = llm.invoke(
    "Generate an image of a cat and say meow",
    generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
)

image_base64 = response.content[0].get("image_url").get("url").split(",")[-1]
meow_text = response.content[1]
print(meow_text)
```

---

### Audio Output

```
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash-preview-tts")
# example
response = llm.invoke(
    "Please say The quick brown fox jumps over the lazy dog",
    generation_config=dict(response_modalities=["AUDIO"]),
)

# Base64 encoded binary data of the image
wav_data = response.additional_kwargs.get("audio")
with open("output.wav", "wb") as f:
    f.write(wav_data)
```

---

### Multimodal Outputs in Chains

You can use Gemini models in a LangChain chain:

```
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, Modality

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-exp-image-generation",
    response_modalities=[Modality.TEXT, Modality.IMAGE],
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "Generate an image of {animal} and tell me the sound it makes.")
])

chain = {"animal": RunnablePassthrough()} | prompt | llm
response = chain.invoke("cat")
```

---

### Thinking Support

Gemini 2.5 Flash Preview supports internal reasoning ("thoughts").

```
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash-preview-04-17",
    thinking_budget=1024
)

response = llm.invoke("How many O's are in Google? How did you verify your answer?")
reasoning_score = response.usage_metadata["output_token_details"]["reasoning"]

print("Response:", response.content)
print("Reasoning tokens used:", reasoning_score)
```

---

## Embeddings

You can use Gemini embeddings in LangChain:

```
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector = embeddings.embed_query("hello, world!")
print(vector)
```

---

## Semantic Retrieval (RAG)

Use Gemini with RAG to retrieve relevant documents from your knowledge base.

```
from langchain_google_genai.vectorstores import GoogleVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
```

# Create a corpus (collection of documents)
```
corpus_store = GoogleVectorStore.create_corpus(display_name="My Corpus")
```

# Create a document under that corpus
```
document_store = GoogleVectorStore.create_document(
    corpus_id=corpus_store.corpus_id, display_name="My Document"
)
```

# Load and upload documents
```
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
for file in DirectoryLoader(path="data/").load():
    chunks = text_splitter.split_documents([file])
    document_store.add_documents(chunks)
```

# Query the document corpus
```
aqa = corpus_store.as_aqa()
response = aqa.invoke("What is the meaning of life?")

print("Answer:", response.answer)
print("Passages:", response.attributed_passages)
print("Answerable probability:", response.answerable_probability)
```

---

## Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [Google Generative AI SDK](https://googleapis.github.io/python-genai/)
- [Gemini Model Documentation](https://ai.google.dev/)