# I
Follow Part 1 of the annotated version of the seminal paper "Attention Is All You Need" by Vaswani et al (https://nlp.seas.harvard.edu/annotated-transformer/), which introduced the Transformer architecture.

This should help you in understanding some of the keywords below.
Spend a short while reading Part 2.

```
## Keywords

1. Self-Attention
2. Query, Key, Value
3. Multi-Head Attention
4. Position-Wise Feed-Forward Network
5. Positional Encoding
6. Residual Connection
7. Embedding / Unembedding
8. Encoder / Decoder layers
9. Encoder-Only Model
10. Decoder-Only Model
11. Bidirectional Encoder Representations from Transformers (BERT)
12. Semantic Search

## Questions

1. Is Attention really all you need?
2. How does the Transformer architecture solve the issues of RNNs?
3. How do transformer-based neural networks take into account words order?
4. What is the difference between Encoder-only and Decoder-only architectures?
5. What are the advantages of transformers that made them so popular?
6. Take a look at the cornucopia of papers that use Transformers since the first paper was published. What tasks are transformers good at?
7. Can you generate images with Transformers?
8. What tasks are BERT models trained to solve? How come these allow for generalized representation of sentences?
9. We met a computer vision neural network that relies on residual connections. What are the same connections doing here?
10. Do we get any hidden/latent representation of the input in decoder-only models?
11. "We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training" - Why would the authors think that? Are there any studies reporting on this?
12. We usually have an input and an output for a neural network, so why do we have three "elements" for this model (Q, K, V)? Which of these is the input, which is the output, and which of these participate in the loss? - Give concrete examples of each.
13. What problem are the authors trying to solve with label smoothing?
14. Why does the plot showing the masking scheme look like a staircase?
```

# Answers Deepseek
## Keywords

### Self-Attention
- **short answer**: A mechanism that allows each position in a sequence to look at all other positions and weigh their importance when encoding information.
- **long answer**: 
  - Computes attention weights between all pairs of positions in a sequence
  - Each token gets a representation that's a weighted sum of all other tokens
  - Enables modeling of long-range dependencies regardless of distance
  - Uses query-key-value mechanism to compute compatibility scores
- **existing alternatives**: 
  - Local attention (restricted window)
  - Strided attention patterns
  - Linear attention variants for efficiency
- **example**:
```python
import torch
import torch.nn as nn
import math

class SelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        
    def forward(self, x):
        # x: (batch_size, seq_len, d_model)
        Q = self.w_q(x)  # Query
        K = self.w_k(x)  # Key  
        V = self.w_v(x)  # Value
        
        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_model)
        attention_weights = torch.softmax(scores, dim=-1)
        output = torch.matmul(attention_weights, V)
        return output

# Usage
attention = SelfAttention(d_model=512)
x = torch.randn(2, 10, 512)  # batch_size=2, seq_len=10, d_model=512
output = attention(x)
```

### Query, Key, Value
- **short answer**: Three representations used in attention where Query seeks information, Key provides what to look for, and Value provides the actual content.
- **long answer**:
  - **Query**: Represents "what I'm looking for" - current position's perspective
  - **Key**: Represents "what I can offer" - what each position contains
  - **Value**: Represents "my actual content" - the information to be aggregated
  - Attention weights are computed from Query-Key compatibility
  - Output is weighted sum of Values based on these weights
- **existing alternatives**:
  - Linear attention without explicit QKV
  - Multi-query attention (shared K/V across heads)
  - Grouped-query attention
- **example**:
```python
import torch
import torch.nn as nn

class QKVAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
        self.w_q = nn.Linear(d_model, d_model)  # Query projection
        self.w_k = nn.Linear(d_model, d_model)  # Key projection  
        self.w_v = nn.Linear(d_model, d_model)  # Value projection
        
    def forward(self, x):
        # For self-attention, all three come from same input
        Q = self.w_q(x)  # What each position is looking for
        K = self.w_k(x)  # What each position contains
        V = self.w_v(x)  # The actual content to aggregate
        
        # Cross-attention example (encoder-decoder)
        # Q comes from decoder, K,V come from encoder
        
        return Q, K, V

model = QKVAttention(d_model=512)
x = torch.randn(1, 5, 512)
Q, K, V = model(x)
print(f"Q shape: {Q.shape}, K shape: {K.shape}, V shape: {V.shape}")
```

### Multi-Head Attention
- **short answer**: Running multiple attention mechanisms in parallel to capture different types of relationships in the data.
- **long answer**:
  - Divides the model dimension into multiple "heads"
  - Each head learns different attention patterns
  - Allows model to attend to different representation subspaces
  - Heads are concatenated and projected back to original dimension
  - Enables richer representation learning
- **existing alternatives**:
  - Single-head attention (original)
  - Multi-query attention
  - Grouped-query attention
- **example**:
```python
import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)
        
    def forward(self, x):
        batch_size, seq_len = x.size(0), x.size(1)
        
        # Linear projections
        Q = self.w_q(x)  # (batch_size, seq_len, d_model)
        K = self.w_k(x)
        V = self.w_v(x)
        
        # Reshape for multi-head: (batch_size, num_heads, seq_len, head_dim)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Scaled dot-product attention per head
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        attention_weights = torch.softmax(scores, dim=-1)
        head_output = torch.matmul(attention_weights, V)
        
        # Concatenate heads and project back
        head_output = head_output.transpose(1, 2).contiguous().view(
            batch_size, seq_len, self.d_model)
        output = self.w_o(head_output)
        
        return output

mha = MultiHeadAttention(d_model=512, num_heads=8)
x = torch.randn(2, 10, 512)
output = mha(x)
```

### Position-Wise Feed-Forward Network
- **short answer**: A small neural network applied independently to each position in the sequence after attention.
- **long answer**:
  - Also called position-wise fully connected feed-forward network
  - Applied to each token position separately and identically
  - Consists of two linear transformations with ReLU activation in between
  - Expands dimension then projects back (e.g., 512 → 2048 → 512)
  - Adds non-linearity and transformation capacity
- **existing alternatives**:
  - Convolutional feed-forward
  - Gated linear units
  - SwiGLU variants
- **example**:
```python
import torch.nn as nn

class PositionWiseFFN(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)  # Expansion
        self.linear2 = nn.Linear(d_ff, d_model)  # Projection back
        self.activation = nn.ReLU()
        
    def forward(self, x):
        # x: (batch_size, seq_len, d_model)
        # Applied to each position independently
        return self.linear2(self.activation(self.linear1(x)))

ffn = PositionWiseFFN(d_model=512, d_ff=2048)
x = torch.randn(2, 10, 512)
output = ffn(x)  # Shape remains (2, 10, 512)
```

### Positional Encoding
- **short answer**: Adding information about the position of tokens in the sequence since self-attention is position-agnostic.
- **long answer**:
  - Self-attention is permutation invariant - needs positional information
  - Sinusoidal encodings use sine/cosine functions of different frequencies
  - Each position gets a unique encoding vector
  - Added to token embeddings before attention layers
  - Allows model to learn relative and absolute positions
- **existing alternatives**:
  - Learned positional embeddings
  - Relative positional encodings
  - Rotary Position Embeddings (RoPE)
  - ALiBi (Attention with Linear Biases)
- **example**:
```python
import torch
import math

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        
        # Create positional encoding matrix
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * 
                           (-math.log(10000.0) / d_model))
        
        pe[:, 0::2] = torch.sin(position * div_term)  # Even indices
        pe[:, 1::2] = torch.cos(position * div_term)  # Odd indices
        pe = pe.unsqueeze(0)  # (1, max_len, d_model)
        
        self.register_buffer('pe', pe)
        
    def forward(self, x):
        # x: (batch_size, seq_len, d_model)
        return x + self.pe[:, :x.size(1)]

# Usage
pos_encoding = PositionalEncoding(d_model=512)
x = torch.randn(2, 10, 512)
x_with_pos = pos_encoding(x)
```

### Residual Connection
- **short answer**: Adding the input of a layer to its output to help gradients flow through deep networks.
- **long answer**:
  - Also called skip connections or identity mappings
  - Helps mitigate vanishing gradient problem in deep networks
  - Enables training of very deep models (dozens of layers)
  - Usually followed by layer normalization
  - Formula: output = layer_norm(x + sublayer(x))
- **existing alternatives**:
  - Pre-norm vs post-norm arrangements
  - Dense connections (DenseNet)
  - Highway networks
- **example**:
```python
class ResidualConnection(nn.Module):
    def __init__(self, d_model, dropout=0.1):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, sublayer):
        # Pre-norm: norm then sublayer then residual
        return x + self.dropout(sublayer(self.norm(x)))
        
# Usage in transformer layer
residual = ResidualConnection(d_model=512)
attention_output = residual(x, lambda x: attention_layer(x))
```

### Embedding / Unembedding
- **short answer**: Converting tokens to vectors (embedding) and vectors back to tokens (unembedding) using learned lookups.
- **long answer**:
  - **Embedding**: Maps discrete token IDs to continuous vectors
  - **Unembedding**: Maps hidden states back to vocabulary probabilities
  - Often share weights between embedding and unembedding matrices
  - Scale embeddings by √d_model to match transformer residual stream magnitude
- **existing alternatives**:
  - Character-level embeddings
  - Subword tokenization embeddings
  - Frozen vs learned embeddings
- **example**:
```python
import torch.nn as nn

class EmbeddingUnembedding(nn.Module):
    def __init__(self, vocab_size, d_model):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.unembedding = nn.Linear(d_model, vocab_size)
        
        # Often share weights
        self.unembedding.weight = self.embedding.weight
        
    def embed(self, token_ids):
        # token_ids: (batch_size, seq_len)
        embeddings = self.embedding(token_ids) * math.sqrt(self.embedding.embedding_dim)
        return embeddings  # (batch_size, seq_len, d_model)
        
    def unembed(self, hidden_states):
        # hidden_states: (batch_size, seq_len, d_model)
        logits = self.unembedding(hidden_states)  # (batch_size, seq_len, vocab_size)
        return logits

embedder = EmbeddingUnembedding(vocab_size=10000, d_model=512)
tokens = torch.randint(0, 10000, (2, 10))
embeddings = embedder.embed(tokens)
logits = embedder.unembed(embeddings)
```

### Encoder / Decoder layers
- **short answer**: Encoder processes input to create representations, decoder generates output using encoder representations and previous outputs.
- **long answer**:
  - **Encoder Layer**:
    - Self-attention over input sequence
    - Position-wise feed-forward network
    - Residual connections and layer norm throughout
  - **Decoder Layer**:
    - Masked self-attention (prevents looking ahead)
    - Cross-attention (attends to encoder outputs)
    - Position-wise feed-forward network
    - Residual connections and layer norm
- **existing alternatives**:
  - Encoder-only models (BERT)
  - Decoder-only models (GPT)
  - Encoder-decoder models (original Transformer, T5)
- **example**:
```python
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.self_attention = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFFN(d_model, d_ff)
        self.residual1 = ResidualConnection(d_model, dropout)
        self.residual2 = ResidualConnection(d_model, dropout)
        
    def forward(self, x):
        x = self.residual1(x, self.self_attention)
        x = self.residual2(x, self.feed_forward)
        return x

class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.masked_attention = MultiHeadAttention(d_model, num_heads)
        self.cross_attention = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFFN(d_model, d_ff)
        self.residual1 = ResidualConnection(d_model, dropout)
        self.residual2 = ResidualConnection(d_model, dropout)
        self.residual3 = ResidualConnection(d_model, dropout)
        
    def forward(self, x, encoder_output):
        # x: decoder input, encoder_output: from encoder
        x = self.residual1(x, self.masked_attention)
        x = self.residual2(x, lambda x: self.cross_attention(x, encoder_output, encoder_output))
        x = self.residual3(x, self.feed_forward)
        return x
```

### Encoder-Only Model
- **short answer**: A transformer that only uses the encoder stack, producing contextual representations for each input token.
- **long answer**:
  - Processes entire input sequence bidirectionally
  - Each token representation incorporates context from all positions
  - Used for understanding tasks: classification, NER, sentiment analysis
  - Examples: BERT, RoBERTa, DeBERTa
  - Pretrained with masked language modeling objectives
- **existing alternatives**:
  - BERT variants (base, large, distilled)
  - ELECTRA, ALBERT, DeBERTa
- **example**:
```python
class EncoderOnlyModel(nn.Module):
    def __init__(self, vocab_size, d_model, num_layers, num_heads, d_ff):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model)
        self.layers = nn.ModuleList([
            EncoderLayer(d_model, num_heads, d_ff) for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)
        
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        x = self.pos_encoding(x)
        for layer in self.layers:
            x = layer(x)
        return self.norm(x)  # Contextual representations
```

### Decoder-Only Model
- **short answer**: A transformer that only uses the decoder stack, generating sequences auto-regressively one token at a time.
- **long answer**:
  - Uses masked self-attention to prevent looking ahead
  - Generates sequences left-to-right (or right-to-left)
  - Used for generation tasks: text generation, translation, summarization
  - Examples: GPT series, Transformer-XL, CTRL
  - Pretrained with causal language modeling
- **existing alternatives**:
  - GPT-1,2,3,4 series
  - Transformer-XL, XLNet
  - CTRL, Grover
- **example**:
```python
class DecoderOnlyModel(nn.Module):
    def __init__(self, vocab_size, d_model, num_layers, num_heads, d_ff):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model)
        self.layers = nn.ModuleList([
            DecoderLayer(d_model, num_heads, d_ff) for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size)
        
    def forward(self, input_ids):
        x = self.embedding(input_ids)
        x = self.pos_encoding(x)
        for layer in self.layers:
            x = layer(x, None)  # No encoder output for pure decoder
        x = self.norm(x)
        return self.lm_head(x)  # Next token predictions
```

### Bidirectional Encoder Representations from Transformers (BERT)
- **short answer**: An encoder-only transformer pretrained with masked language modeling to create powerful contextual embeddings.
- **long answer**:
  - Bidirectional: sees full context from both left and right
  - Pretrained with Masked Language Modeling (MLM) and Next Sentence Prediction (NSP)
  - Creates rich contextual representations for each token
  - Fine-tuned on downstream tasks with minimal architecture changes
  - Revolutionized NLP with state-of-the-art performance
- **existing alternatives**:
  - RoBERTa (optimized BERT)
  - ALBERT (parameter-efficient)
  - DistilBERT (smaller, faster)
  - ELECTRA (more sample efficient)
- **example**:
```python
# Simplified BERT-like model
class BERTLike(nn.Module):
    def __init__(self, vocab_size, d_model, num_layers, num_heads, d_ff):
        super().__init__()
        self.encoder = EncoderOnlyModel(vocab_size, d_model, num_layers, num_heads, d_ff)
        self.mlm_head = nn.Linear(d_model, vocab_size)  # Masked LM head
        
    def forward(self, input_ids, masked_positions=None):
        hidden_states = self.encoder(input_ids)
        
        if masked_positions is not None:
            # Get representations only at masked positions
            masked_states = hidden_states.gather(1, masked_positions.unsqueeze(-1).expand(-1, -1, hidden_states.size(-1)))
            mlm_logits = self.mlm_head(masked_states)
            return mlm_logits
            
        return hidden_states
```

### Semantic Search
- **short answer**: Finding documents or passages that are semantically similar to a query, not just keyword matches.
- **long answer**:
  - Uses dense vector representations of text
  - Measures similarity in high-dimensional space (cosine similarity, dot product)
  - Transformer encoders create contextual embeddings
  - Enables understanding of meaning beyond exact word matches
  - Used in search engines, recommendation systems, QA
- **existing alternatives**:
  - Sparse retrieval (TF-IDF, BM25)
  - Dense retrieval (DPR, ANCE)
  - Hybrid approaches
- **example**:
```python
class SemanticSearchModel(nn.Module):
    def __init__(self, encoder):
        super().__init__()
        self.encoder = encoder
        
    def encode_query(self, query_text):
        # Encode query to dense vector
        query_emb = self.encoder(query_text)
        return query_emb[:, 0, :]  # Use [CLS] token or mean pooling
        
    def encode_documents(self, doc_texts):
        # Encode documents to dense vectors
        doc_embs = self.encoder(doc_texts)
        return doc_embs[:, 0, :]
        
    def similarity(self, query_emb, doc_embs):
        # Compute cosine similarity
        return torch.nn.functional.cosine_similarity(query_emb, doc_embs, dim=-1)

# Usage
encoder = EncoderOnlyModel(vocab_size=10000, d_model=512, num_layers=6, num_heads=8, d_ff=2048)
search_model = SemanticSearchModel(encoder)
```

## Questions

### Is Attention really all you need?
- **short answer**: While attention is incredibly powerful, modern architectures still need other components like feed-forward networks, normalization, and residual connections for optimal performance.
- **long answer**:
  - Attention provides the core mechanism for modeling dependencies
  - However, feed-forward networks add necessary non-linear transformations
  - Residual connections enable training of deep networks
  - Layer normalization stabilizes training
  - Positional encodings provide sequence order information
  - The title was somewhat provocative - attention is necessary but not sufficient alone

### How does the Transformer architecture solve the issues of RNNs?
- **short answer**: Transformers replace sequential processing with parallel computation of all positions simultaneously, eliminating vanishing gradients and enabling efficient training on long sequences.
- **long answer**:
  - **Parallelization**: All sequence positions processed simultaneously vs sequential RNN processing
  - **Vanishing Gradients**: Constant path length between any two positions vs growing path in RNNs
  - **Long-range Dependencies**: Direct attention between distant tokens vs diluted information through many RNN steps
  - **Computational Efficiency**: O(1) operations for layer-to-layer vs O(n) in RNNs
  - **Memory**: Constant memory per layer vs growing memory with sequence length

### How do transformer-based neural networks take into account words order?
- **short answer**: Through explicit positional encodings that are added to token embeddings, providing the model with information about each token's position in the sequence.
- **long answer**:
  - **Positional Encodings**: Sinusoidal or learned vectors encoding position information
  - **Addition to Embeddings**: Position encodings are added to token embeddings before attention
  - **Relative Position Encodings**: Some models encode relative distances between tokens
  - **Attention Patterns**: The model learns to use positional information through attention weights
  - Without positional encodings, transformers would be permutation invariant

### What is the difference between Encoder-only and Decoder-only architectures?
- **short answer**: Encoder-only models process entire input bidirectionally for understanding tasks, while decoder-only models generate sequences auto-regressively for generation tasks.
- **long answer**:
  - **Encoder-Only**:
    - Bidirectional attention (sees full context)
    - Used for classification, extraction, understanding
    - Examples: BERT, RoBERTa
    - Pretrained with masked language modeling
  - **Decoder-Only**:
    - Causal/masked attention (only sees previous tokens)
    - Used for generation, prediction, completion
    - Examples: GPT series, CTRL
    - Pretrained with causal language modeling
  - **Encoder-Decoder**: Both components for sequence-to-sequence tasks

### What are the advantages of transformers that made them so popular?
- **short answer**: Superior performance on NLP tasks, parallelizable training, ability to handle long-range dependencies, and scalability to massive models and datasets.
- **long answer**:
  - **State-of-the-Art Performance**: Consistently beat previous models on benchmarks
  - **Parallelization**: Efficient GPU utilization during training
  - **Long-range Context**: Attention captures dependencies regardless of distance
  - **Scalability**: Performance improves with more data and parameters
  - **Transfer Learning**: Pretrain once, fine-tune for multiple tasks
  - **Multimodal Capability**: Extendable to vision, audio, etc.

### Take a look at the cornucopia of papers that use Transformers since the first paper was published. What tasks are transformers good at?
- **short answer**: Transformers excel at natural language processing, computer vision, speech processing, multimodal tasks, and any domain requiring modeling of complex dependencies.
- **long answer**:
  - **NLP**: Translation, summarization, question answering, text generation
  - **Computer Vision**: Image classification, object detection, segmentation
  - **Speech Processing**: Speech recognition, text-to-speech, audio generation
  - **Multimodal**: Image captioning, visual question answering, cross-modal retrieval
  - **Code Generation**: Program synthesis, code completion
  - **Reasoning**: Mathematical problem solving, logical inference
  - **Recommendation Systems**: Sequential recommendation, personalized content

    ### Can you generate images with Transformers?
- **short answer**: Yes, by treating images as sequences of patches or tokens and using autoregressive generation similar to text.
- **long answer**:
  - **Image as Sequence**: Split image into patches, flatten as sequence
  - **Autoregressive Generation**: Generate patches one by one like tokens
  - **Examples**: iGPT, DALL-E, Image Transformer
  - **Vector Quantization**: Use VQ-VAE to convert images to discrete tokens
  - **Challenges**: Long sequences make generation computationally expensive
  - **Recent Advances**: Diffusion transformers combine transformers with diffusion models

### What tasks are BERT models trained to solve? How come these allow for generalized representation of sentences?
- **short answer**: BERT is pretrained on Masked Language Modeling and Next Sentence Prediction, forcing it to learn deep bidirectional contextual understanding that transfers well to other tasks.
- **long answer**:
  - **Masked Language Modeling (MLM)**: Randomly mask tokens and predict them, requiring understanding of bidirectional context
  - **Next Sentence Prediction (NSP)**: Predict if two sentences follow each other, learning relationships between sentences
  - **Generalization Mechanism**:
    - Bidirectional context creates rich token representations
    - Self-supervised learning on massive text corpora
    - Task-agnostic representations transfer to various downstream tasks
    - Fine-tuning adapts these general representations to specific tasks

### We met a computer vision neural network that relies on residual connections. What are the same connections doing here?
- **short answer**: Residual connections in transformers serve the same purpose as in ResNet - they enable training of very deep networks by preventing vanishing gradients and facilitating gradient flow.
- **long answer**:
  - **Gradient Flow**: Direct paths for gradients to flow backwards through many layers
  - **Preventing Degradation**: Networks don't get worse with more layers
  - **Identity Mapping**: Allows layers to learn residuals rather than complete transformations
  - **Deep Networks**: Enables stacking dozens or hundreds of layers
  - **Stable Training**: Similar benefits observed in both vision and language domains

### Do we get any hidden/latent representation of the input in decoder-only models?
- **short answer**: Yes, decoder-only models produce hidden representations at each layer that encode contextual information about the input sequence up to each position.
- **long answer**:
  - **Layer-wise Representations**: Each transformer layer produces hidden states
  - **Contextual Encoding**: Representations incorporate left-side context through masked attention
  - **Final Hidden States**: Used for next token prediction but also serve as latent representations
  - **Feature Extraction**: Can be used for downstream tasks similar to encoder representations
  - **Limitation**: Only unidirectional context compared to bidirectional encoders

### "We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training" - Why would the authors think that? Are there any studies reporting on this?
- **short answer**: Sinusoidal encodings have smooth, predictable patterns that can generalize to unseen positions, unlike learned embeddings which are fixed to training positions.
- **long answer**:
  - **Smooth Extrapolation**: Sine/cosine functions naturally extend beyond trained range
  - **Periodic Nature**: Repeating patterns allow generalization
  - **Theoretical Basis**: Trigonometric functions have well-defined behavior for any input
  - **Empirical Evidence**: Subsequent studies show sinusoidal encodings generalize better to longer sequences
  - **Limitations**: Still degradation at very long sequences, leading to relative position encodings

### We usually have an input and an output for a neural network, so why do we have three "elements" for this model (Q, K, V)? Which of these is the input, which is the output, and which of these participate in the loss? - Give concrete examples of each.
- **short answer**: Q, K, V are all derived from the input through linear transformations, and the attention output (weighted sum of V) participates in the loss; they're internal mechanism components, not traditional inputs/outputs.
- **long answer**:
  - **Input**: Original sequence embeddings are the true input
  - **Q, K, V**: All are linear projections of the input for the attention mechanism
  - **Output**: Weighted sum of V based on Q-K compatibility scores
  - **Loss Participation**: Final transformer output (after all layers) participates in loss
  - **Concrete Example**:
    - Input: "The cat sat on the"
    - Q: What each position wants to find (current word's perspective)
    - K: What each position offers (content available)
    - V: Actual content to aggregate
    - Output: Next word prediction "mat" → cross-entropy loss

### What problem are the authors trying to solve with label smoothing?
- **short answer**: Label smoothing prevents overconfidence in model predictions and improves generalization by softening the hard 0/1 targets during training.
- **long answer**:
  - **Overconfidence Prevention**: Models become too confident in predictions
  - **Regularization Effect**: Soft targets act as regularizer
  - **Calibration**: Better calibrated probability estimates
  - **Noisy Labels**: More robust to label errors in training data
  - **Implementation**: Replace one-hot [0,0,1,0] with smoothed [ε,ε,1-3ε,ε]

### Why does the plot showing the masking scheme look like a staircase?
- **short answer**: The staircase pattern results from the causal masking that prevents each position from attending to future positions, creating a triangular attention matrix.
- **long answer**:
  - **Causal Constraint**: Each position can only see previous positions
  - **Triangular Matrix**: Attention weights matrix has zeros in upper triangle
  - **Auto-regressive Generation**: Essential for sequential generation without cheating
  - **Visual Pattern**: Creates staircase when visualizing attention masks
  - **Implementation**: Add -∞ to future positions before softmax


# Answers Gemini

## Keywords

### Self-Attention


| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Short Answer**                        | A mechanism that calculates how much a token should weigh (attend to) every other token in the sequence to compute its new, context-aware representation.                                                                                                                                                                                                                                                                                   |
| **Long Answer**                         | Self-attention is the core component that replaces recurrence. It computes the attention output by comparing a token's **Query (Q)** vector against all tokens' **Key (K)** vectors to get similarity scores. These scores are normalized with **Softmax** and used as weights for a weighted sum of the **Value (V)** vectors. This allows the model to capture **global dependencies** regardless of distance, a key advantage over RNNs. |
| **Existing Alternatives or Variations** | **Cross-Attention** (in the Decoder attending to the Encoder), **Local Attention**, **Sparse Attention** (to reduce $O(n^2)$ complexity), **Linear Attention**.                                                                                                                                                                                                                                                                             |
| **Example in Python Code, PyTorch**     | The Scaled Dot-Product Attention:                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
```python
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.size(-1)
    # 1. Compute scores: Q * K_transpose
    scores = torch.matmul(Q, K.transpose(-2, -1))
    # 2. Scale
    scores = scores / (d_k ** 0.5)
    # 3. Apply Softmax to get attention weights
    weights = F.softmax(scores, dim=-1)
    # 4. Multiply weights by Value
    output = torch.matmul(weights, V)
    return output
```


### Query, Key, Value

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | Three abstract vectors projected from the input embedding: **Query** (what's being looked for), **Key** (what's available), and **Value** (the content to be extracted).                                                                                                                                                                                                                                    |
| **Long Answer**                         | Q, K, and V are linear projections of the input/output of the previous layer. They are used to implement associative addressing: the Query vector is matched against the Key vectors to determine a weight for each Value vector. In **Self-Attention**, Q, K, and V all come from the same sequence. In **Cross-Attention**, Q comes from the Decoder, while K and V come from the Encoder's final output. |
| **Existing Alternatives or Variations** | In models like **Multi-Query Attention (MQA)**, Key and Value matrices are shared across all heads, while Query matrices remain separate, primarily to speed up decoding.                                                                                                                                                                                                                                   |
| **Example in Python Code, PyTorch**     | Simplified projection from an input tensor `X`:                                                                                                                                                                                                                                                                                                                                                             |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                             |
```python
import torch.nn as nn

d_model = 512
d_k = 64

# Linear layers for projection
W_q = nn.Linear(d_model, d_k)
W_k = nn.Linear(d_model, d_k)
W_v = nn.Linear(d_model, d_k)

X = torch.randn(1, 10, d_model) # Input tensor
Q = W_q(X) 
K = W_k(X)
V = W_v(X)
```

 

### Multi-Head Attention

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | Running multiple self-attention mechanisms in parallel to allow the model to capture different facets or relationships within the sequence simultaneously.                                                                                                                                                                                                                                                                                |
| **Long Answer**                         | Instead of a single attention calculation, the input is split into $h$ different subspaces (heads). Each head performs attention independently. This enables the model to jointly attend to information from different representation subspaces at different positions (e.g., one head may focus on syntax, another on semantics). The outputs of all $h$ heads are then concatenated and linearly projected to produce the final output. |
| **Existing Alternatives or Variations** | **Multi-Query Attention (MQA)** and **Grouped-Query Attention (GQA)** are variations designed for faster inference by reducing the Key/Value parameter size.                                                                                                                                                                                                                                                                              |
| **Example in Python Code, PyTorch**     | Conceptual concatenation step:                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
```python
import torch
import torch.nn as nn

h = 8
d_model = 512
d_v = d_model // h # 64

# Outputs from 8 parallel attention heads (e.g., 8 x (B, SeqLen, 64))
head_outputs = [torch.randn(2, 10, d_v) for _ in range(h)]

# Concatenate along the last dimension to restore d_model
concatenated = torch.cat(head_outputs, dim=-1) # (2, 10, 512)

# Final linear projection
W_o = nn.Linear(d_model, d_model)
output = W_o(concatenated) 
```
 |

### Position-Wise Feed-Forward Network

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | A simple two-layer, fully connected network (with ReLU activation) applied identically and independently to every position's vector after the attention layer.                                                                                                                                                                                                                                                  |
| **Long Answer**                         | It consists of two linear transformations: a wider inner layer ($d_{ff}=2048$ in the base model) and a narrower output layer ($d_{model}=512$). It is "position-wise" because the same FFN is applied to each token's position vector, allowing the network to process the attention output locally at each token and perform non-linear transformations without mixing information across different positions. |
| **Existing Alternatives or Variations** | Replacing the ReLU activation with **GELU** (common in BERT/GPT), or replacing the FFN entirely with a **Mixture of Experts (MoE)** layer for scaling.                                                                                                                                                                                                                                                          |
| **Example in Python Code, PyTorch**     |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                 |
```python
import torch.nn as nn
import torch.nn.functional as F

class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff=2048):
        super().__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)

    def forward(self, x):
        return self.w_2(F.relu(self.w_1(x)))
```


### Positional Encoding

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | A unique vector, derived from sine and cosine functions, added to the input embedding to inject crucial information about the token's position and order into the model.                                                                                                                                                                                                                                                                                           |
| **Long Answer**                         | Since the self-attention mechanism is permutation-invariant (order-agnostic), positional encoding is essential. The original Transformer uses a deterministic, fixed sinusoidal function where different dimensions of the vector use sine and cosine functions of varying frequencies. This allows the model to learn relationships based on the absolute position and to easily compute information about **relative positions** through linear transformations. |
| **Existing Alternatives or Variations** | **Learnable Positional Encodings** (e.g., in BERT), and **Relative Positional Encodings (RoPE)** (a modern standard that modifies the attention scores directly).                                                                                                                                                                                                                                                                                                  |
| **Example in Python Code, PyTorch**     | Conceptual calculation of the positional matrix:                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
```python

import torch
import math

def positional_encoding(pos, i, d_model):
    # Sinusoidal formula from the paper
    denominator = 10000.0 ** (i / d_model)
    if i % 2 == 0: # Even dimensions use sine
        return math.sin(pos / denominator)
    else: # Odd dimensions use cosine
        return math.cos(pos / denominator)

# The final input vector is: Embedding + Positional_Encoding
```


### Residual Connection

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | A "skip" connection that simply adds the input of a sublayer to its output ($x + \text{Sublayer}(x)$), which helps gradients flow efficiently and stabilizes training for deep stacks.                                                                                                                                                                                                                                                 |
| **Long Answer**                         | Every sublayer (attention and FFN) in the Transformer block is wrapped with a Residual Connection, followed by **Layer Normalization** ($\text{LayerNorm}(\mathbf{x} + \text{Sublayer}(\mathbf{x}))$). This design (introduced in ResNet) solves the **vanishing gradient problem** by providing a direct identity path for the gradient during backpropagation, enabling the training of the deep 6-layer Encoder and Decoder stacks. |
| **Existing Alternatives or Variations** | **Pre-norm** (normalization before the sublayer) is a popular variation for improved stability in very deep modern transformers, contrasting with the original paper's **Post-norm**.                                                                                                                                                                                                                                                  |
| **Example in Python Code, PyTorch**     | Implementation of a layer wrapper:                                                                                                                                                                                                                                                                                                                                                                                                     |
```python
import torch.nn as nn

class SublayerConnection(nn.Module):
    def __init__(self, size):
        super().__init__()
        self.norm = nn.LayerNorm(size)

    def forward(self, x, sublayer):
        # Post-norm: Add and then Norm (original Transformer)
        return self.norm(x + sublayer(x)) 
```
 |

### Embedding / Unembedding

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | **Embedding** converts discrete tokens (words) into dense vectors; **Unembedding** (the final linear projection) converts the final hidden vectors back into probability scores over the vocabulary.                                                                                                                                                                                                                                                                                                                  |
| **Long Answer**                         | The **Embedding Layer** is the first step, mapping a one-hot word index to a dense vector of size $d_{model}$, capturing semantic meaning. The **Unembedding Layer** is the final step in the decoder, a linear projection that maps the final $d_{model}$-sized vector to a vector of size $V$ (vocabulary size), which are the logits for the next token prediction. The paper suggests **weight tying**, using the same weight matrix for both the input Embedding and the output Unembedding, to save parameters. |
| **Existing Alternatives or Variations** | Using **Subword Tokenization** (e.g., WordPiece, BPE) instead of whole word embeddings to handle rare words and manage vocabulary size.                                                                                                                                                                                                                                                                                                                                                                               |
| **Example in Python Code, PyTorch**     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
```python

vocab_size = 10000
d_model = 512

# Input Embedding
input_embed = nn.Embedding(vocab_size, d_model)

# Unembedding (output linear layer) - often tied weights
output_linear = nn.Linear(d_model, vocab_size, bias=False) 

# final_logits = output_linear(final_decoder_output)
```
 |

### Encoder / Decoder layers

| Component                               | Description                                                                                                                                                                                                                                                                             |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | The **Encoder** creates a contextual representation of the input sentence; the **Decoder** uses this representation (via cross-attention) to generate the output sentence token by token.                                                                                               |
| **Long Answer**                         | The architecture is a sequence-to-sequence model:                                                                                                                                                                                                                                       |
|                                         | - **Encoder Layer:** Contains two sub-layers: Multi-Head Self-Attention and a Position-Wise FFN. It processes the input **bidirectionally** to create a rich, static memory of the source.                                                                                              |
|                                         | - **Decoder Layer:** Contains three sub-layers: **Masked** Multi-Head Self-Attention, Multi-Head **Cross-Attention** (attending to the Encoder output), and a Position-Wise FFN. It operates **autoregressively** and unidirectionally, using the Encoder's output to guide generation. |
| **Existing Alternatives or Variations** | **Encoder-Only** (BERT) and **Decoder-Only** (GPT) models, which specialize in understanding and generation, respectively.                                                                                                                                                              |
| **Example in Python Code, PyTorch**     | (Conceptual structure of a Decoder layer's core blocks)                                                                                                                                                                                                                                 |

```python
class DecoderLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.masked_self_attn = MultiHeadAttention() # 1st sublayer
        self.cross_attn = MultiHeadAttention()       # 2nd sublayer
        self.feed_forward = PositionWiseFeedForward() # 3rd sublayer
```

### Encoder-Only Model

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Short Answer**                        | A stack of only Encoder layers that uses bidirectional attention to create deep, contextualized representations, primarily for language understanding tasks.                                                                                                                                                                                                                                                                                                                          |
| **Long Answer**                         | This architecture (e.g., **BERT**) leverages the full, unmasked **bidirectional self-attention** of the Encoder to capture dependencies between words regardless of their position. It's best suited for **Natural Language Understanding (NLU)** tasks like classification, sequence labeling, and semantic similarity, where a rich, non-directional understanding of a single sentence is required. It cannot generate text naturally because it lacks the autoregressive masking. |
| **Existing Alternatives or Variations** | **RoBERTa** (an optimized BERT), **XLM-R**, **ELECTRA**.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Example in Python Code, PyTorch**     | (See BERT keyword code example below)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Decoder-Only Model

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | A stack of only Decoder layers (without the cross-attention block) that uses masked self-attention to generate text autoregressively (token-by-token).                                                                                                                                                                                                                                                                                                         |
| **Long Answer**                         | This architecture (e.g., **GPT**) uses the **masked self-attention** to ensure that the prediction of the next token only depends on the previously generated tokens (unidirectional flow). This **autoregressive** nature makes them the standard for **Natural Language Generation (NLG)** tasks, such as language modeling, story writing, and chat responses. They are simpler than the full Encoder-Decoder model as they lack the cross-attention block. |
| **Existing Alternatives or Variations** | **GPT-3/4**, **LLaMA**, **Mistral**.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Example in Python Code, PyTorch**     | (Conceptual generation step)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
```python
# 1. Get the hidden state of the last generated token
hidden_state_last_token = decoder_stack(input_embeddings)[:, -1, :]
# 2. Predict the next word
logits = output_linear(hidden_state_last_token)
next_token = torch.argmax(logits, dim=-1)
# 3. Append to sequence and repeat
``` 
|

### Bidirectional Encoder Representations from Transformers (BERT)

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer** | A pre-trained Encoder-Only model that learns generalized language understanding by solving two tasks: Masked Language Modeling and Next Sentence Prediction. |
| **Long Answer** | BERT's success stems from its pre-training tasks: |
| 1. **Masked Language Modeling (MLM):** | Randomly masking 15% of tokens and predicting the original words. This forces the model to learn context bidirectionally (from both left and right). |
| 2. **Next Sentence Prediction (NSP):** | Determining if one sentence logically follows another. This teaches the model about sentence-level coherence and relationship. |
| | The bidirectional context from MLM, combined with the sentence-level coherence from NSP, yields a highly versatile and generalized set of word/sentence representations. |
|**Existing Alternatives or Variations** | **RoBERTa** (found that removing NSP and using dynamic masking was more effective), **ELECTRA** (uses a more efficient discriminative pre-training task). |
| **Example in Python Code, PyTorch** | Conceptual forward pass during MLM pre-training: |

```python
# Input: 'The [MASK] sat on the [MASK]'
input_ids = tokenizer.encode(masked_text, return_tensors='pt')
bert_output = bert_model(input_ids)

# Loss is computed for the output logits corresponding to the [MASK] tokens
# loss = criterion(bert_output.logits, true_token_ids)
``` 
|

### Semantic Search

| Component | Description |
| :--- | :--- |
| **Short Answer** | Search that matches the *meaning* or *intent* of a query, rather than just matching keywords, by converting both the query and documents into dense Transformer vectors (embeddings). |
| **Long Answer** | Traditional search (lexical search like BM25) relies on exact keyword overlap. Semantic Search uses a **Transformer Encoder** (often a specialized BERT variant like Sentence-BERT) to map a query and a document into vectors in a high-dimensional space. The search then finds the document whose vector is the **closest** to the query vector (e.g., using **cosine similarity**). This allows a query like "How to teach a dog tricks" to match a document titled "A complete guide to canine training." |
| **Existing Alternatives or Variations** | **Lexical Search (BM25)**, **Hybrid Search** (combining both lexical and semantic methods), and **Re-rankers** (a small Transformer used to refine the list of candidates retrieved by an initial search). |
| **Example in Python Code, PyTorch** | (Conceptual use of a vector store) |
| | 

```python
# Assuming encoder is a trained Sentence Transformer model
query_vec = encoder.encode("best way to train a puppy")

# Calculate similarity against document vectors in the vector database
# similarities = cosine_similarity(query_vec, doc_vectors) 
# best_match = find_top_k(similarities)
``` 

|

---
## Questions

### Is Attention really all you need?

| Component | Description |
| :--- | :--- |
| **Short Answer** | While attention is sufficient to replace recurrence/convolution, the complete Transformer architecture requires **Positional Encoding**, **Feed-Forward Networks**, and **Residual Connections** to be functional and effective. |
| **Long Answer** | The title highlights attention's power, but the model's success comes from the entire design. Without **Positional Encoding**, the model is order-agnostic. Without **Residual Connections**, training deep stacks becomes impossible due to vanishing gradients. Without the non-linear **FFNs**, the model's expressive power would be severely limited. Furthermore, attention still faces the limitation of **$O(n^2)$ computational complexity** with respect to sequence length, which requires workarounds for very long texts. |
| **Existing Alternatives or Variations** | Models like **Transformer-XL** reintroduce recurrence to address the long-sequence issue, and newer architectures like **Mamba** replace attention with a state-space model for $O(n)$ complexity while retaining performance. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### How does the Transformer architecture solve the issues of RNNs?

| Component | Description |
| :--- | :--- |
| **Short Answer** | It replaces the sequential step-by-step processing of RNNs with the parallel processing capability of self-attention, and it models long-range dependencies directly in a constant number of steps. |
| **Long Answer** | 1. **Parallelization:** RNNs must compute hidden states sequentially ($h_t$ depends on $h_{t-1}$), which limits parallel processing on GPUs/TPUs. The Transformer's attention mechanism computes representations for all tokens simultaneously, drastically reducing training time. 2. **Long-Range Dependencies:** RNNs suffer from vanishing gradients, losing information over long distances. Self-attention connects any two words in the sequence directly, regardless of distance, solving this issue effectively. |
| **Existing Alternatives or Variations** | **Convolutional Sequence-to-Sequence (ConvS2S)** models (which use CNNs) also offered better parallelization than RNNs, but were still generally outperformed by the Transformer's ability to model global context. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### How do transformer-based neural networks take into account words order?

| Component | Description |
| :--- | :--- |
| **Short Answer** | They explicitly add **Positional Encoding (PE)** vectors to the input word embeddings, providing the model with a unique, fixed pattern that represents the position of each token in the sequence. |
| **Long Answer** | The core self-attention operation is order-invariant (shuffling the input tokens and their corresponding Q/K/V vectors would not change the output). To re-introduce order, the Transformer adds the PE vector to the token's embedding vector *before* the first Encoder/Decoder layer. The network then learns to interpret these sinusoidal PE patterns as position and relative distance. |
| **Existing Alternatives or Variations** | **Relative Positional Encodings (RoPE)** are preferred in many modern models as they encode relative distance directly into the attention mechanism, leading to better extrapolation. |
| **Example in Python Code, PyTorch** | (See Positional Encoding keyword code example above) |

### What is the difference between Encoder-only and Decoder-only architectures?

| Component | Description |
| :--- | :--- |
| **Short Answer** | **Encoder-only** (e.g., BERT) uses **bidirectional** attention for understanding; **Decoder-only** (e.g., GPT) uses **unidirectional (masked)** attention for autoregressive generation. |
| **Long Answer** | - **Encoder-Only:** Designed for **Natural Language Understanding (NLU)**. The full self-attention allows any token to look at all other tokens (bidirectional context), giving a rich, deep understanding of the whole sequence. |
| | - **Decoder-Only:** Designed for **Natural Language Generation (NLG)**. The **masked** self-attention ensures that the model can only look at tokens that have already been processed/generated, enabling the sequential, autoregressive prediction of the next token. |
| | **Full Encoder-Decoder** models are used for sequence-to-sequence tasks like translation, requiring both understanding and generation components. |
| **Existing Alternatives or Variations** | **Prefix-Decoder** architectures (e.g., T5 in its generation phase) combine both: an unmasked Encoder processes the input prompt, and a masked Decoder generates the rest of the sequence. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### What are the advantages of transformers that made them so popular?

| Component | Description |
| :--- | :--- |
| **Short Answer** | Massively improved **parallelization**, effective handling of **long-range dependencies**, and **superior scalability** with data and model size. |
| **Long Answer** | 1. **Training Speed:** Full parallelization of sequence processing dramatically speeds up training compared to sequential RNNs, making large-scale training feasible. 2. **Performance:** The direct connection between any two tokens via attention results in superior performance in capturing global context and long-range relationships. 3. **Transfer Learning:** The standardized, modular architecture made pre-training large models (like BERT/GPT) on massive text corpora possible, enabling efficient **transfer learning** via fine-tuning on smaller, task-specific datasets. |
| **Existing Alternatives or Variations** | The main drawback of the Transformer is the quadratic complexity $O(n^2)$, which is being addressed by alternatives like **Linear Transformers** or **State Space Models**. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### Take a look at the cornucopia of papers that use Transformers since the first paper was published. What tasks are transformers good at?

| Component | Description |
| :--- | :--- |
| **Short Answer** | All sequence-based tasks (NLP), as well as Computer Vision and Multimodal generation, wherever data can be treated as a sequence of tokens. |
| **Long Answer** | Transformers have achieved state-of-the-art results across various domains: |
| | - **Natural Language Processing (NLP):** Machine Translation, Summarization, Question Answering, Text Generation (LLMs). |
| | - **Computer Vision (CV):** **Vision Transformers (ViT)** process image patches as tokens, excelling in image classification, segmentation, and object detection. |
| | - **Multimodal:** Combining text and image/video (e.g., DALL-E, Sora) by treating both modalities as sequences of tokens for generation and cross-attention. |
| | - **Speech/Audio:** Speech recognition and audio synthesis by encoding acoustic signals into token sequences. |
| **Existing Alternatives or Variations** | (Not applicable for this question, as it asks for applications) |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### Can you generate images with Transformers?

| Component | Description |
| :--- | :--- |
| **Short Answer** | Yes, by representing the image as a sequence of discrete visual tokens (e.g., VQ-VAE codes), a Decoder-Only Transformer can autoregressively predict the next token to generate an image from a text prompt. |
| **Long Answer** | Models like **DALL-E** use a two-stage process: 1. A VQ-VAE compresses the image into a sequence of "visual tokens." 2. A large **Decoder-Only Transformer** is trained on the conditional probability of these visual tokens given a text prompt (encoded by a Transformer Encoder). By predicting the next visual token sequentially, the model generates an image in the discrete latent space, which is then decoded back to pixels by the VQ-VAE decoder. |
| **Existing Alternatives or Variations** | **Diffusion Models** (the current SOTA) also often use a Transformer Encoder to process and condition the image generation based on the input text prompt. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### What tasks are BERT models trained to solve? How come these allow for generalized representation of sentences?

| Component | Description |
| :--- | :--- |
| **Short Answer** | **Masked Language Modeling (MLM)** and **Next Sentence Prediction (NSP)**. MLM enforces deep **bidirectional** context, and NSP enforces **sentence relationship** and coherence, allowing for versatile transfer learning. |
| **Long Answer** | The pre-training tasks provide a powerful generalization mechanism: |
| | - **MLM** requires predicting a masked word using context from *both sides*. This forces the model to learn deep, contextual understanding of word meaning (e.g., how the word "bank" is used differently in a sentence about money vs. a river). The **bidirectional** nature is key to its power. |
| | - **NSP** requires understanding the relationship between two sentences, enabling the model to grasp higher-level linguistic structures like discourse and coreference across sentences. |
| | These two self-supervised tasks allow BERT to learn a generalized "language model" of English structure that can be easily adapted to almost any NLP task through fine-tuning. |
| **Existing Alternatives or Variations** | (See BERT keyword code example above) |
| **Example in Python Code, PyTorch** | (See BERT keyword code example above) |

### We met a computer vision neural network that relies on residual connections. What are the same connections doing here?

| Component | Description |
| :--- | :--- |
| **Short Answer** | They perform the same core function as in **ResNet**: facilitating unimpeded gradient flow to enable the training of the very deep stacked layers without performance degradation (vanishing gradient problem). |
| **Long Answer** | The computer vision model that relies on them is the **Residual Network (ResNet)**. In both ResNet and the Transformer, residual connections ensure that the output of a layer is the input plus the function of the input ($x + f(x)$). This identity mapping allows the gradient to pass directly to earlier layers during backpropagation, solving the **vanishing gradient problem**. For the Transformer, this is critical because it relies on deep stacks (6 or more layers) to achieve its high performance. Without the residual connection and the following Layer Normalization, training a deep Transformer would be practically impossible. |
| **Existing Alternatives or Variations** | (See Residual Connection keyword for variations like Pre-norm vs. Post-norm) |
| **Example in Python Code, PyTorch** | (See Residual Connection keyword code example above) |

### Do we get any hidden/latent representation of the input in decoder-only models?

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | Yes, the final output of the last Decoder layer (before the unembedding projection) is the contextualized **hidden state** (or latent representation) of the entire sequence up to that point.                                                                                                                                                                                                                                                                                                                                       |
| **Long Answer**                         | In a Decoder-Only model (like GPT), the stack of Decoder layers transforms the input token embeddings into a sequence of output vectors, each of size $d_{model}$. These output vectors are the **latent representations** that contain all the contextual information learned by the model for that position. For prediction, the vector corresponding to the last generated token is used. For a downstream task (like classification), this vector can be extracted and used as the feature vector for the entire input sequence. |
| **Existing Alternatives or Variations** | The representation can sometimes be improved by combining (e.g., averaging) the latent representations from multiple upper layers, rather than just using the final layer's output.                                                                                                                                                                                                                                                                                                                                                  |
| **Example in Python Code, PyTorch**     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
```python
# hidden_states is the final output of the stack of decoder layers
hidden_states = decoder_stack(input_embeddings) # Shape: (B, SeqLen, d_model)

# For sequence classification/feature extraction:
sequence_representation = hidden_states.mean(dim=1) # Average over sequence length
``` 
|

### "We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training" - Why would the authors think that? Are there any studies reporting on this?

| Component | Description |
| :--- | :--- |
| **Short Answer** | The sinusoidal functions' mathematical properties allow the positional encoding of a relative offset ($PE_{pos+k}$) to be expressed as a linear function of the absolute position ($PE_{pos}$), which theoretically generalizes to new positions. |
| **Long Answer** | The core mathematical property is the trigonometric identity $\sin(\alpha + \beta)$ and $\cos(\alpha + \beta)$, which shows that $PE(pos+k)$ is a linear combination of $PE(pos)$ and $PE(k)$. Since the functions are fixed and deterministic, the model can potentially learn to recognize the relationship between any two positions *based on their difference* ($k$), even if the absolute position $pos+k$ was never seen during training. |
| | **Studies:** While the original sinusoidal PE offered this *theoretical* benefit, studies have shown that it often fails to extrapolate reliably in practice. This led to the development of **Relative Positional Encodings (RoPE)**, which apply the rotation property *directly* to Q and K vectors, resulting in vastly improved and more robust extrapolation. |
| **Existing Alternatives or Variations** | **RoPE** and **ALiBi** (Attention with Linear Biases) are modern techniques that have demonstrated superior ability to generalize to longer, unseen sequences than the original sinusoidal approach. |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### We usually have an input and an output for a neural network, so why do we have three "elements" for this model (Q, K, V)? Which of these is the input, which is the output, and which of these participate in the loss? - Give concrete examples of each.

| Component | Description |
| :--- | :--- |
| **Short Answer** | Q, K, and V are *internal vectors* derived from the input; they implement the attention lookup mechanism, not the overall network input/output. |
| **Long Answer** | The overall network components are distinct from the internal Q, K, V vectors: |
| | - **Network Input:** The **Input Embedding** of the source/target tokens. *Example: The vector for the word "cat" at the start of the Encoder.* |
| | - **Network Output:** The **Logits** (pre-softmax scores) produced by the Unembedding layer at the end of the Decoder. *Example: The 10,000-dimension vector of scores for the next word.* |
| | - **Participate in Loss:** The **Network Output (Logits)** and the **Ground Truth Target** (the correct next word ID). The Cross-Entropy Loss is calculated between the predicted probability distribution (Softmax of Logits) and the true label. |
| | **Q, K, V Role:** They are used *inside* the attention layer to compute an **internal representation**. Q and K calculate the weights, and V provides the content for the weighted sum. They do not directly participate in the final loss calculation; only the final network output does. |
| **Existing Alternatives or Variations** | (Not applicable for this conceptual question) |
| **Example in Python Code, PyTorch** | (Not applicable for a conceptual question) |

### What problem are the authors trying to solve with label smoothing?

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | To prevent the model from becoming overly **confident** in its predictions (overfitting) by slightly softening the target one-hot labels, which improves generalization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Long Answer**                         | In a typical classification task, the ground truth uses "hard" one-hot labels (e.g., probability 1 for the correct class, 0 for all others). Training with these can cause the model to push its logits to extreme values (positive infinity for the correct class), leading to **overfitting** and poor generalization. **Label Smoothing** changes the hard target to a "soft" distribution by distributing a small probability mass $\epsilon$ (e.g., 0.1) across all classes. This acts as a regularizer, making the model less confident but more robust. The authors of "Attention Is All You Need" state that it led to increased accuracy and perplexity. |
| **Existing Alternatives or Variations** | Label smoothing is a form of **regularization**, similar in goal to **Dropout** (which is also used in the Transformer).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Example in Python Code, PyTorch**     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
```python
import torch

# K is vocab size, epsilon=0.1 from the paper
K = 10000 
epsilon = 0.1

# Hard target for the correct word (ID 5)
hard_target = torch.zeros(K)
hard_target[5] = 1.0

# Smoothed target
smoothed_target = hard_target * (1.0 - epsilon) + (epsilon / K)

# Check value at correct index
# print(smoothed_target[5].item()) # Will be 0.9 + 0.1/10000 = 0.90001
```


### Why does the plot showing the masking scheme look like a staircase?

| Component                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short Answer**                        | The plot is a visual representation of the lower triangular **causal mask** used in the Decoder's self-attention, which ensures that a token at position $i$ can only attend to tokens at positions $j \leq i$.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Long Answer**                         | The plot displays the attention scores matrix (Query $\times$ Key). Each row represents the Query for a token, and columns are the Keys for all tokens. In the Decoder, to maintain the autoregressive property (only looking at past information), attention to all future tokens ($j > i$) must be prevented. This is done by setting their corresponding attention scores to a very large negative number ($-\infty$) *before* the Softmax operation. The resulting matrix is a **lower triangular matrix** where the top-right half is blocked/masked out, and the allowed attention forms the staircase-like pattern of the bottom-left half. |
| **Existing Alternatives or Variations** | In the **Encoder's** self-attention, no masking is applied, resulting in a solid square plot, as attention is allowed bidirectionally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Example in Python Code, PyTorch**     | Generating the mask (where 0 is allowed and -inf is masked):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
```python
import torch

seq_len = 5
# Create a mask where the upper triangle (future positions) is -inf
mask = torch.triu(torch.ones(seq_len, seq_len) * float('-inf'), diagonal=1)

# print(mask)
# tensor([[ 0., -inf, -inf, -inf, -inf],
#         [ 0.,  0., -inf, -inf, -inf],
#         [ 0.,  0.,  0., -inf, -inf],
#         [ 0.,  0.,  0.,  0., -inf],
#         [ 0.,  0.,  0.,  0.,  0.]])
```

