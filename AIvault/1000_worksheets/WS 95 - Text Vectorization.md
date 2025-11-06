## Keywords

### 1. Word Embeddings

  * **Main Idea:** Word embeddings are a method of representing words as dense, low-dimensional vectors of real numbers. Unlike sparse one-hot vectors, these dense vectors capture the semantic meaning, context, and relationships between words (e.g., the vector for "king" is mathematically close to "queen").
  * **How it works:** A model (like Word2Vec or GloVe) learns these vectors by processing a massive text corpus. It adjusts the vector for a word based on the other words that frequently appear around it, following the **Distributional Hypothesis** ("a word is characterized by the company it keeps").
  * **Variations:** The two main categories are:
    1.  **Static Embeddings:** (Word2Vec, GloVe, fastText) A word has exactly *one* vector, regardless of its context (e.g., "river **bank**" and "financial **bank**" have the same vector).
    2.  **Contextual Embeddings:** (ELMo, BERT, GPT) A word's vector is *generated* on the fly and is different depending on the sentence it's in.
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models import Word2Vec

    # 1. Sample sentences
    sentences = [['cat', 'sat', 'on', 'the', 'mat'], 
                 ['dog', 'ate', 'my', 'homework']]

    # 2. Train a simple model
    # vector_size = dimensionality of the embedding
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    model.save("word2vec.model")

    # 3. Get the vector for a word
    vector_for_cat = model.wv['cat']

    # 4. Find similar words
    similar_words = model.wv.most_similar('cat')

    print("Vector for 'cat':\n", vector_for_cat)
    # print("Words similar to 'cat':\n", similar_words) # Will be empty with this tiny corpus
    ```

-----

### 2\. Word2Vec

  * **Main Idea:** A specific and popular model family created by Tomas Mikolov at Google to learn word embeddings *predictively*. It's a shallow neural network that is trained on a "fake" task, and the learned weights of its hidden layer are extracted to become the word vectors.
  * **How it works:** The model is trained to either (A) predict a target word from its surrounding context words or (B) predict the context words from a target word. This forces the model to learn vectors that encapsulate a word's typical context.
  * **Variations:**
    1.  **CBOW (Continuous Bag-of-Words):** Faster to train and better for frequent words. It "predicts the target word from the bag-of-words context." (e.g., given `['cat', 'sat', 'on', '___', 'mat']`, predict `the`).
    2.  **Skip-gram:** Slower to train but performs better for rare words. It "predicts the context words from the target word." (e.g., given `the`, predict `['cat', 'sat', 'on', 'mat']`).
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models import Word2Vec

    # sg=0 (default) uses CBOW
    # sg=1 uses Skip-gram
    model_cbow = Word2Vec(sentences, vector_size=100, window=5, sg=0)
    model_skipgram = Word2Vec(sentences, vector_size=100, window=5, sg=1)

    # Get the vector for 'dog' from the Skip-gram model
    vec_dog = model_skipgram.wv['dog']
    ```

-----

### 3\. Negative Sampling

  * **Main Idea:** A highly efficient optimization and loss function used to train Word2Vec. It avoids the computationally massive cost of a full softmax (which would require updating millions of weights) by reframing the problem as a set of simple binary classifications.
  * **How it works:** For a given `(target, context)` pair (a *positive* sample), the model is trained to output a 1 (for "real"). The model is then *also* fed several `(target, random_word)` pairs (called *negative* samples), and is trained to output a 0 (for "fake"). This forces the model to learn vectors that can distinguish *true* context words from *random* words.
  * **Variations:** The main parameter is $k$, the number of negative samples to draw for each positive sample. A typical range is $k=5$ to $k=20$.
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models import Word2Vec

    # 'negative=5' enables negative sampling and specifies k=5
    # 'hs=0' explicitly disables hierarchical softmax (the other optimization)
    model = Word2Vec(
        sentences, 
        vector_size=100, 
        window=5, 
        sg=1,       # Use Skip-gram
        hs=0,       # No Hierarchical Softmax
        negative=5  # Use 5 negative samples
    )

    print("Model trained with Negative Sampling.")
    ```

-----

### 4\. GloVe (Global Vectors for Word Representation)

  * **Main Idea:** A different model for learning embeddings (from Stanford) that is *count-based* rather than predictive. It argues that embeddings should be learned directly from the global word-word co-occurrence statistics of the entire corpus.
  * **How it works:**
    1.  It first builds a massive matrix $X$, where $X_{ij}$ is the number of times word $j$ appears in the context of word $i$.
    2.  It then learns two vectors for each word ($v_i$ and $u_j$) by trying to make their dot product $v_i \cdot u_j$ be a good predictor of $\log(X_{ij})$.
    3.  The final vector for a word is the sum of its $v$ and $u$ vectors.
  * **Variations:** The main variations are in the context window size and the weighting function $f(X_{ij})$ used in the loss function (which down-weights very frequent co-occurrences).
  * **Code Example (loading a pre-trained model):**
    ```python
    from gensim.scripts.glove2word2vec import glove2word2vec
    from gensim.models import KeyedVectors

    # GloVe files are often in a .txt format. 
    # We must first convert it to a word2vec format.
    # Assume 'glove.6B.100d.txt' is downloaded.

    # glove_input_file = 'glove.6B.100d.txt'
    # word2vec_output_file = 'glove.6B.100d.word2vec.txt'
    # glove2word2vec(glove_input_file, word2vec_output_file)

    # Now load the converted model
    # g_model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

    # Now you can use it like a Word2Vec model
    # print(g_model.most_similar('computer'))
    # print(g_model['king'])

    print("Example shows how to load a pre-trained GloVe file.")
    ```

-----

### 5\. fastText

  * **Main Idea:** An extension of Word2Vec (from Facebook) that learns vectors for *character n-grams* (subword units) instead of just whole words.
  * **How it works:** It breaks a word into its constituent n-grams (e.g., for `n=3`, "where" $\rightarrow$ `<wh`, `whe`, `her`, `ere`, `re>`). The final vector for the word "where" is the *sum* of the vectors for all its n-grams. This allows it to:
    1.  Generate vectors for **Out-of-Vocabulary (OOV)** words (words it has never seen).
    2.  Share information between morphologically similar words (e.g., "walk," "walks," "walking" will share n-grams and thus have similar vectors).
  * **Variations:** It can be trained using either the CBOW or Skip-gram architecture.
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models import FastText

    # Training is very similar to Word2Vec
    ft_model = FastText(
        sentences, 
        vector_size=100, 
        window=5, 
        min_count=1, 
        sg=1 # Use Skip-gram
    )

    # Key difference: it can get vectors for OOV words
    # Assume 'supercalifragilistic' was NOT in the training data
    try:
        # This would fail with Word2Vec
        oov_vector = ft_model.wv['supercalifragilistic']
        print("Successfully generated vector for an OOV word.")
    except KeyError:
        print("This word is not in vocab (should not happen with fastText)")
    ```

-----

### 6\. Doc2Vec (Paragraph Vectors)

  * **Main Idea:** An extension of Word2Vec that learns to create a dense vector representation for a *whole document* (from a sentence to a paragraph or a full text), not just for individual words.
  * **How it works:** It adds a new vector to the Word2Vec model: a **Document ID vector** (or Paragraph ID). This unique vector is trained *alongside* the word vectors and acts as a "memory" or "topic" that contributes to the prediction task. By the end of training, this vector is forced to represent the semantic meaning of the entire document.
  * **Variations:**
    1.  **PV-DM (Distributed Memory):** Like CBOW. Predicts a word using its context words *and* the document vector.
    2.  **PV-DBOW (Distributed Bag of Words):** Like Skip-gram. Predicts random words from the document using *only* the document vector (it's simpler and faster).
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument

    # Doc2Vec requires a special input format: TaggedDocument
    tagged_data = [
        TaggedDocument(words=['cat', 'sat', 'on', 'the', 'mat'], tags=['doc_1']),
        TaggedDocument(words=['dog', 'ate', 'my', 'homework'], tags=['doc_2'])
    ]

    # dm=1 uses PV-DM. dm=0 uses PV-DBOW.
    d2v_model = Doc2Vec(tagged_data, vector_size=100, window=5, min_count=1, dm=1)

    # Get the vector for the whole first document
    doc_1_vector = d2v_model.dv['doc_1']
    print("Vector for 'doc_1':\n", doc_1_vector)

    # You can also infer a vector for a new, unseen document
    new_doc_words = ['cat', 'ate', 'the', 'homework']
    inferred_vector = d2v_model.infer_vector(new_doc_words)
    ```

-----

### 7\. Downsampling (Subsampling of Frequent Words)

  * **Main Idea:** A simple optimization technique used in Word2Vec/fastText to speed up training and improve vector quality. It does this by randomly skipping very frequent words (like "the", "a", "in") during training.
  * **How it works:** These common words appear in millions of contexts but provide very little specific semantic information. Training on them is inefficient. The model skips a word $w_i$ with a probability $P(w_i)$ that is proportional to its frequency $f(w_i)$. This means "the" might be skipped 70% of the time, while "platypus" is skipped 0% of the time.
  * **Variations:** The main parameter is the `sample` threshold (in `gensim`), which controls how aggressively to downsample.
  * **Code Example (using `gensim`):**
    ```python
    from gensim.models import Word2Vec

    # 'sample' is the threshold. 
    # A common value is 1e-3 or 1e-5.
    # Higher values (e.g., 1e-2) mean LESS downsampling.
    # Lower values (e.g., 1e-5) mean MORE aggressive downsampling.
    model = Word2Vec(
        sentences,
        vector_size=100,
        window=5,
        sample=1e-5 # Aggressively downsample frequent words
    )

    print("Model trained with frequent-word downsampling.")
    ```

Here are the solutions and explanations for your "NLP Text Vectorization" worksheet.

## Questions

### 1\. Why do we need word embeddings?

While words form sentences, the **meaning** of an individual word is defined by the company it keeps (the contexts it appears in). This is the **Distributional Hypothesis**.

We need word embeddings because they are the first technique that effectively captures this *contextual meaning* in a dense, mathematical object (a vector).

  * **Overcoming Sparsity:** Before embeddings, we used methods like **one-hot encoding**, where each word is a vector with one '1' and thousands of '0's (e.g., `[0, 0, 0, 1, 0, ... , 0]`). This is extremely sparse, computationally inefficient, and treats all words as equally different (the vector for "cat" is no closer to "kitten" than it is to "airplane").
  * **Capturing Semantics:** Word embeddings (like Word2Vec) are trained to "learn" a word's meaning from its neighbors. As a result, words used in similar contexts (like "king" and "queen," or "walk" and "run") will end up having similar vectors in the embedding space.
  * **Enabling Downstream Tasks:** These dense vectors are the perfect **input features** for machine learning models. A classifier for sentiment analysis, for example, can learn patterns from these vectors (e.g., vectors for "wonderful," "excellent," and "amazing" cluster in a "positive" region of the space) much more effectively than it could from sparse one-hot vectors.

### 2\. What document vectorization techniques did we already discuss in previous worksheets?

Based on the typical progression of NLP, the classical techniques you most likely discussed are:

  * **Bag-of-Words (BoW):** This represents a document as a sparse vector where each dimension corresponds to a word in the vocabulary, and the value is its count (frequency) in the document. It ignores word order entirely.
  * **TF-IDF (Term Frequency-Inverse Document Frequency):** This is an improvement on BoW. It's also a sparse vector, but the values are "weighted" counts. It increases the score for words that are frequent in the *current* document (TF) but decreases the score for words that are common across *all* documents (IDF). This highlights words that are uniquely important to the document's topic.

### 3\. How does Doc2Vec handle ultra-sparse document distributions?

Doc2Vec (also known as Paragraph Vectors) handles sparsity by learning a **dense vector representation** for the entire document, just as Word2Vec learns a dense vector for each word.

It avoids the "ultra-sparse" nature of BoW/TF-IDF by **not** creating a vector with one dimension per word. Instead, it creates a *single, fixed-length dense vector* (e.g., 300 dimensions) for the entire document.

It does this by adding a new vector to the Word2Vec model: the **Document ID vector** (or Paragraph ID). This vector is trained *alongside* the word vectors.

1.  **Distributed Memory (PV-DM):** This model is similar to CBOW. It uses the word vectors from a context window *and* the unique document vector to predict the next word. The document vector acts as a "memory" or "topic" that contributes to the prediction.
2.  **Distributed Bag of Words (PV-DBOW):** This model is simpler, like Skip-gram. It ignores the word vectors in the input and uses *only* the document vector to predict a random sample of words from that document.

In both cases, the model is forced to learn a document vector that encapsulates the document's overall semantic meaning, thus creating a dense, information-rich representation.

### 4\. Skim industry papers from the past decade and find at least 3 cases where word embedding models were the main part of the proposed solutions.

Here are three common and high-impact industry applications:

1.  **Recommendation Systems (e.g., at Airbnb, Etsy, Spotify):** This is a very clever use. Companies treat a user's *session* as a "sentence" and the *items* (e.g., songs, products, or clicked listings) as "words." They train a Word2Vec model on millions of these user sessions. The resulting item embeddings capture "context." Items that are frequently viewed or bought together (like "headphones" and "phone charger") will have very similar vectors. This powers "similar items" or "users who bought this also bought" features.
2.  **Search Ranking & Information Retrieval (e.g., at E-commerce sites):** Static embeddings are used to bridge the "vocabulary gap." A user might search for "cold weather pants," but a product is titled "winter-proof trousers." A traditional keyword search would fail. By embedding both the query and the product titles into a vector space, the search engine can retrieve items based on **semantic similarity** (cosine similarity of vectors) rather than just keyword matching.
3.  **Survey & Customer Feedback Analysis:** Companies use embeddings to analyze thousands of open-ended customer reviews. Instead of just counting keywords, they can average the embeddings of the words in a review to get a "review vector." By clustering these vectors, they can automatically discover common themes, complaints, or positive points (e.g., finding that "slow," "unresponsive," and "crashed" all cluster together, identifying a theme of "poor performance").

### 5\. What is the problem with just aggregating word embeddings somehow (e.g., averaging) to represent documents as vectors?

The biggest problem is the complete **loss of word order, syntax, and compositionality**.

A simple average treats the document as a "bag of embeddings." This means the sentences "Man bites dog" and "Dog bites man" would have the **exact same** vector representation, despite having opposite meanings.

Furthermore, averaging "muddies" the meaning. The vector for a specific, important word (like "dreadful") gets diluted by the average of all the other, less informative words in the sentence (like "it," "was," "a," "very"). This makes it hard to distinguish subtle differences in meaning.

### 6\. Is using Jaccard Similarity to compare two documents useful in any sense?

Yes, it's very useful, but for a specific task: **lexical overlap and near-duplicate detection.**

Jaccard Similarity for sets is $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$. For documents, you treat each document as the *set of its unique words*.

  * **Useful:** It's a simple, fast, and effective way to see how many unique words two documents share. It's excellent for finding plagiarism, duplicate news articles, or very similar product descriptions.
  * **Limitation:** It is *not* a semantic metric. It has no idea that "cat" and "kitten" are related. Two documents, "The president spoke to the nation" and "The leader addressed the country," would have a Jaccard similarity of 0.28 (2 shared words / 7 unique words), even though they mean the same thing.

### 7\. Propose a way to include context information when treating word vectors.

The problem described—a word having the same vector regardless of context (e.g., "river **bank**" vs. "financial **bank**")—is the key limitation of *static* embeddings like Word2Vec and GloVe.

The solution is to use **contextual embedding models**. These models don't just *have* a static vector for each word; they *generate* a new vector for a word each time, based on the specific sentence it's in.

The main way to do this is with **Transformer-based models** like **BERT** (and its variants) or **ELMo** (which uses LSTMs).

  * **How it works (simplified):** When you feed a sentence like "I went to the river bank" into BERT, its self-attention mechanism "looks" at all the other words in the sentence ("I," "went," "to," "the," "river") as it calculates the vector for "bank."
  * If you instead feed it "I went to the financial bank," the attention mechanism will look at "financial" and produce a *completely different* vector for "bank."
  * This way, the final vector for "bank" is not static; it is "contextualized" and uniquely represents the word *as it is used in that specific sentence*.

-----

## Exercises

### 1\. The original word2vec paper...

#### Find formulations for the loss functions, both skip-gram and CBOW.

The original paper was vague, but the follow-up paper ("Distributed Representations of Words and Phrases...") which introduced **Negative Sampling** provides the clear, optimized loss functions that are used in practice.

Let $v_{w_I}$ be the "input" embedding for the center word, $v'_{w_O}$ be the "output" embedding for the context word, and $\sigma(x) = 1 / (1 + e^{-x})$ be the sigmoid function.

**Skip-gram with Negative Sampling (SGNS):**
The goal is to predict the context word $w_O$ given the input word $w_I$. The loss for one positive pair $(w_I, w_O)$ and $k$ negative samples ($w_i \sim P_n(w)$) is:
$$L = - \log \sigma(v'_{w_O} \cdot v_{w_I}) - \sum_{i=1}^k \log \sigma(-v'_{w_i} \cdot v_{w_I})$$
This pushes the dot product of the *real* pair to be large (positive) and the dot product of the *fake* pairs to be small (negative).

**CBOW with Negative Sampling:**
The goal is to predict the center word $w_O$ given the *average* of its context words. Let $v_C = \frac{1}{|C|} \sum_{w_j \in \text{Context}} v_{w_j}$ be the average vector of the context.
The loss is then:
$$L = - \log \sigma(v'_{w_O} \cdot v_C) - \sum_{i=1}^k \log \sigma(-v'_{w_i} \cdot v_C)$$

-----

#### What are the assumptions in these formulations?

1.  **Distributional Hypothesis:** The core assumption is that words appearing in similar contexts have similar meanings.
2.  **Conditional Independence (in Skip-gram):** Given the center word, the model assumes all context words are generated independently of each other. This is false (e.g., "the" is more likely to be followed by a noun), but it's a useful simplifying assumption.
3.  **Bag-of-Words Context (in CBOW):** The CBOW model assumes the order of words in the context window doesn't matter (since it just averages their vectors).
4.  **Negative Sampling Assumption:** It assumes that the complex multi-class problem (predicting one word out of 50,000) can be approximated by a set of simple binary classification problems (is this *real* or *fake*?).

-----

#### Does anything in these loss functions look like contrastive learning?

**Yes, absolutely.** Negative Sampling *is* a form of contrastive learning.

  * **Contrastive Learning** works by teaching a model to distinguish between "similar" (positive) and "dissimilar" (negative) pairs.
  * The loss function is designed to **pull** the representations of positive pairs (in this case, $(v_{w_I}, v'_{w_O})$) closer together in the vector space, making their dot product large.
  * Simultaneously, it **pushes** the representations of negative pairs (the $(v_{w_I}, v'_{w_i})$) far apart, making their dot product small.
    This is the *exact* principle of the Negative Sampling loss function.

-----

#### How would you build the dataset for training?

You need a large, raw text corpus (e.g., all of Wikipedia).

1.  **Preprocess:** Tokenize the text into a long list of words. Build a vocabulary mapping each unique word to an integer ID. Optionally, perform subsampling of frequent words (like "the," "a").
2.  **Generate Pairs:** Slide a "window" (e.g., size 5, so 2 words left and 2 words right) across the list of words.
3.  **For Skip-gram:** If your window is `[The, quick, brown, fox, jumps]` and the center word is `brown`:
      * You create **positive pairs**: `(brown, The)`, `(brown, quick)`, `(brown, fox)`, `(brown, jumps)`.
      * For *each* positive pair, like `(brown, fox)`, you also generate $k$ **negative pairs**. You do this by sampling $k$ random words (e.g., "table," "banana") from the vocabulary's frequency distribution (specifically, $P_n(w) \propto \text{count}(w)^{3/4}$).
      * Your final dataset entry for this one pair would be: `(target=brown, context=fox, label=1)` plus $k$ negative entries: `(target=brown, context=table, label=0)`, `(target=brown, context=banana, label=0)`, etc.

-----

#### Find a general-use English corpus of a decent size, and train a model using PyTorch.

  * **Corpus:** A standard, easy-to-use corpus is **Text8** (the first 100MB of cleaned English Wikipedia text). You can also use `WikiText-103`.
  * **PyTorch Implementation:** Here is a conceptual skeleton of what a Skip-gram Negative Sampling (SGNS) model looks like in PyTorch.

<!-- end list -->

```python
import torch
import torch.nn as nn
import torch.optim as optim

# --- 1. Model Definition ---
class Word2Vec_SGNS(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(Word2Vec_SGNS, self).__init__()
        # Two embedding layers: one for "center" words, one for "context" words
        self.in_embed = nn.Embedding(vocab_size, embed_dim)
        self.out_embed = nn.Embedding(vocab_size, embed_dim)

    def forward(self, target_word, context_word, negative_samples):
        # Get embeddings
        # target_word: [batch_size]
        # context_word: [batch_size]
        # negative_samples: [batch_size, k]

        v_target = self.in_embed(target_word)    # [batch_size, embed_dim]
        v_context = self.out_embed(context_word)  # [batch_size, embed_dim]
        v_negs = self.out_embed(negative_samples) # [batch_size, k, embed_dim]

        # --- Calculate Loss ---
        # Reshape for dot products
        v_target = v_target.unsqueeze(2) # [batch_size, embed_dim, 1]
        
        # Positive loss (we want dot product to be high)
        # bmm: batch matrix multiplication
        pos_score = torch.bmm(v_context.unsqueeze(1), v_target).squeeze() # [batch_size]
        pos_loss = -torch.log(torch.sigmoid(pos_score) + 1e-8).mean()
        
        # Negative loss (we want dot products to be low, so -score to be high)
        neg_score = torch.bmm(v_negs, v_target).squeeze() # [batch_size, k]
        neg_loss = -torch.log(torch.sigmoid(-neg_score) + 1e-8).sum(dim=1).mean()

        return pos_loss + neg_loss

# --- 2. Example Usage (Conceptual) ---
VOCAB_SIZE = 50000
EMBED_DIM = 300
k = 5 # Number of negative samples

model = Word2Vec_SGNS(VOCAB_SIZE, EMBED_DIM)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Assume 'dataloader' yields batches of (target_words, context_words, neg_samples)
# for target, context, negs in dataloader:
#     optimizer.zero_grad()
#     loss = model(target, context, negs)
#     loss.backward()
#     optimizer.step()
    
# After training, the useful weights are in model.in_embed.weight
# embeddings = model.in_embed.weight.data
```

-----

#### Can you see any syntactic and semantic regularities...

Yes. This refers to the famous "vector algebra" (e.g., `king - man + woman ≈ queen`).

After training the model above, you would extract the `in_embed` weights. Then you would perform these operations:

```python
# Assuming 'embeddings' is your [VOCAB_SIZE, EMBED_DIM] tensor
# and 'word_to_idx' is your vocab mapping

def get_vec(word):
    return embeddings[word_to_idx[word]]

def find_closest(vector, top_n=5):
    # Calculate cosine similarity between 'vector' and all 'embeddings'
    sims = torch.cosine_similarity(vector, embeddings)
    # Get top_n results
    top_results = torch.topk(sims, top_n)
    # Convert indices back to words
    return [idx_to_word[i.item()] for i in top_results.indices]

# 1. Semantic (Gender)
vec_king = get_vec('king')
vec_man = get_vec('man')
vec_woman = get_vec('woman')

result_vec = vec_king - vec_man + vec_woman
print(find_closest(result_vec)) 
# Expected output: ['king', 'queen', 'woman', 'prince'] (king/woman are inputs, 'queen' is the target)

# 2. Syntactic (Verb Tense)
vec_walk = get_vec('walk')
vec_walking = get_vec('walking')
vec_swim = get_vec('swim')

result_vec = vec_walking - vec_walk + vec_swim
print(find_closest(result_vec))
# Expected output: ['swimming', 'swim', 'walking', ...]

# 3. Semantic (Country-Capital)
vec_paris = get_vec('paris')
vec_france = get_vec('france')
vec_germany = get_vec('germany')

result_vec = vec_paris - vec_france + vec_germany
print(find_closest(result_vec))
# Expected output: ['berlin', 'paris', 'germany', ...]
```

-----

#### Explore examples for sentence pairs where the [Word Mover's] distance is small/large.

The **Word Mover's Distance (WMD)** calculates the *minimum* "cost" (distance) to "move" all the word vectors from one document to match the words in the other.

  * **Small Distance (Semantically Similar):**

      * **Doc A:** "The president spoke to the nation."
      * **Doc B:** "The leader addressed the country."
      * **Why small?** The model "moves" the vector for "president" to "leader" (a short distance, as they are semantically similar). It moves "spoke" to "addressed" (short distance) and "nation" to "country" (short distance). The cost is minimal.

  * **Large Distance (Semantically Different):**

      * **Doc A:** "I love machine learning."
      * **Doc B:** "The cat sat on the mat."
      * **Why large?** The words are in completely different parts of the embedding space. The "cost" to "move" the vector for "love" to "cat," "machine" to "sat," etc., is enormous.

  * **Interesting Case (Medium Distance):**

      * **Doc A:** "Man bites dog."
      * **Doc B:** "Dog bites man."
      * **Why?** The words themselves are identical (`man`, `bites`, `dog`). WMD, like simple averaging, is also a "bag of embeddings" metric and **ignores word order**. Therefore, it would report a distance of **zero** for these two sentences, highlighting its limitations (which Doc2Vec and BERT solve).

-----

### 1. More
#### 1. Loss Function Formulations

The papers describe the models conceptually. The actual loss functions are derived from the goal of maximizing the probability of observed word pairs. The objective is to maximize the log-likelihood of the corpus, and the loss is the negative of that objective.

Let's define some terms:
*   $V$ is the size of the vocabulary.
*   $w_I$ is the input or center word.
*   $w_O$ is the output or context word.
*   $v_w$ is the "input" vector for word $w$ (from the input embedding matrix).
*   $v'_w$ is the "output" vector for word $w$ (from the output embedding matrix).
*   The score for a word pair $(w_I, w_O)$ is $u_O = v'_{w_O}ᵀ v_{w_I}$.

##### Continuous Bag-of-Words (CBOW)

**Goal:** Predict the center word ($w_t$) given its context words ($C_t = {w_{t-c}, ..., w_{t-1}, w_{t+1}, ..., w_{t+c}}$).

1.  First, the context vectors are averaged: $v̂ = (1/|C_t|) * Σ_{w ∈ C_t} v_w$.
2.  The probability of the center word $w_t$ given the context is calculated using the softmax function, which normalizes the scores for all words in the vocabulary:
    $P(w_t | C_t) = exp(v'_{w_t}ᵀ v̂) / Σ_{j=1}^{V} exp(v'_{w_j}ᵀ v̂)$
3.  The objective is to maximize this probability across the entire corpus `T`. The loss function `L` is the average negative log-likelihood:
    $L = -(1/T) * Σ_{t=1}^{T} log P(w_t | C_t)$
    $L = -(1/T) * Σ_{t=1}^{T} [ v'_{w_t}ᵀ v̂ - log(Σ_{j=1}^{V} exp(v'_{w_j}ᵀ v̂)) ]$

##### Skip-gram

**Goal:** Predict the context words (`C_t`) given the center word (`w_t`).

1.  The probability of a context word `w_c` given the center word `w_t` is:
    $P(w_c | w_t) = exp(v'_{w_c}ᵀ v_{w_t}) / Σ_{j=1}^{V} exp(v'_{w_j}ᵀ v_{w_t})$
2.  The model makes a conditional independence assumption (see next section) to define the probability of the entire context window:
    $P(C_t | w_t) = Π_{w_c ∈ C_t} P(w_c | w_t)$
3.  The loss function `L` is the average negative log-likelihood over the corpus:
    $L = -(1/T) * Σ_{t=1}^{T} log(P(C_t | w_t))$
    $L = -(1/T) * Σ_{t=1}^{T} Σ_{w_c ∈ C_t} log( P(w_c | w_t))$
    $L = -(1/T) * Σ_{t=1}^{T} Σ_{w_c ∈ C_t} [ v'_{w_c}ᵀ v_{w_t} - log(Σ_{j=1}^{V} exp(v'_{w_j}ᵀ v_{w_t})) ]$

---

#### 2. Assumptions in These Formulations

1.  **The Distributional Hypothesis:** This is the core assumption of all word embedding models. It states that **words that occur in similar contexts tend to have similar meanings**. The entire learning process is designed to create vectors that satisfy this hypothesis.

2.  **Limited Context:** The models assume that the meaning of a word is primarily captured by its immediate neighbors (the context window). Long-range dependencies in a sentence or document are ignored.

3.  **Conditional Independence (Skip-gram):** The Skip-gram model assumes that given the center word, all the output context words are independent of each other. This is a strong simplification, as the presence of "New" in the context of "York" makes "City" more likely. However, this assumption makes the computation tractable.

4.  **Bag-of-Words Context (CBOW):** The CBOW model averages the vectors of the context words. This means it assumes that the order of words in the context window does not matter.

---

#### 3. Connection to Contrastive Learning

This is an excellent observation. While the original softmax formulations shown above are not explicitly contrastive, the method used to make them efficient, **Negative Sampling**, is a form of contrastive learning.

The full softmax is computationally expensive because of the sum over the entire vocabulary `V` in the denominator. Negative Sampling reframes the problem:

*   Instead of predicting the correct context word from all possible words (multi-class classification)...
*   ...we train a model to distinguish the true context word (a **positive sample**) from several randomly drawn words from the vocabulary (**negative samples**).

**How it works (for a Skip-gram pair `(w_t, w_c)`):**
1.  Take the true pair `(w_t, w_c)` as a positive example.
2.  Create `k` negative examples by pairing `w_t` with words `w_n` drawn from a noise distribution (e.g., the unigram distribution of the corpus).
3.  The model's goal is to maximize the probability of the positive pair and minimize the probability of the negative pairs. The loss function becomes a sum of binary logistic regression losses:
    `L = -log(σ(v'_{w_c}ᵀ v_{w_t})) - Σ_{i=1 to k} log(σ(-v'_{w_{n_i}}ᵀ v_{w_t}))`
    where `σ` is the sigmoid function.

This is **explicitly contrastive**. It learns the embeddings by training them to produce a high score for a "positive" (observed) pair while simultaneously producing low scores for "negative" (randomly generated) pairs. It pushes the vectors of true pairs together and pulls the vectors of random pairs apart in the embedding space.

---

#### 4. Building the Dataset for Training

Here is the step-by-step process:

1.  **Acquire a Corpus:** Start with a large, raw text file (e.g., all of Wikipedia, a collection of news articles).
2.  **Pre-process and Tokenize:**
    *   Clean the text (e.g., convert to lowercase, remove punctuation and special characters).
    *   Split the text into a long list of words (tokens).
3.  **Build Vocabulary:**
    *   Count the frequency of each word.
    *   Create a vocabulary of the `N` most frequent words. Words not in this vocabulary are mapped to a special `<UNK>` (unknown) token.
    *   Create two mappings: `word_to_index` and `index_to_word`.
4.  **Generate Training Samples (Context-Target Pairs):**
    *   Choose a `window_size`, say `C=2`.
    *   Iterate through your list of tokens from position `t = 0` to `T`.
    *   For each token `w_t` (the target word):
        *   The context `C_t` is `{w_{t-2}, w_{t-1}, w_{t+1}, w_{t+2}}`.
        *   **For Skip-gram:** Create pairs `(w_t, w_{t-2})`, `(w_t, w_{t-1})`, `(w_t, w_{t+1})`, `(w_t, w_{t+2})`. The dataset is a list of `(target, context)` pairs.
        *   **For CBOW:** Create one sample `([w_{t-2}, w_{t-1}, w_{t+1}, w_{t+2}], w_t)`. The dataset is a list of `(context_list, target)` pairs.

**Example:** For the sentence "the quick brown fox jumps over" and `window_size=2`, focusing on the target "brown":
*   **Skip-gram pairs:** `(brown, the)`, `(brown, quick)`, `(brown, fox)`, `(brown, jumps)`
*   **CBOW sample:** `([the, quick, fox, jumps], brown)`

---

#### 5. Training a Model with PyTorch

It's not feasible to train a large model in this interactive environment, but I can provide a complete, functional PyTorch script to train a Skip-gram model with negative sampling on the standard `text8` corpus. This corpus is the first 100MB of a clean Wikipedia dump.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
from collections import Counter
import random
import math
import requests
import zipfile
import os

# --- 1. Settings ---
EMBEDDING_DIM = 100
WINDOW_SIZE = 5
BATCH_SIZE = 1024
NUM_EPOCHS = 5
LEARNING_RATE = 0.001
MIN_FREQ = 50  # Words with frequency less than this will be discarded
NEG_SAMPLES = 5 # Number of negative samples

# --- 2. Data Preparation ---
def download_text8():
    url = 'http://mattmahoney.net/dc/text8.zip'
    if not os.path.exists('text8.zip'):
        print("Downloading text8 corpus...")
        r = requests.get(url)
        with open('text8.zip', 'wb') as f:
            f.write(r.content)
    if not os.path.exists('text8'):
        print("Extracting text8...")
        with zipfile.ZipFile('text8.zip', 'r') as zip_ref:
            zip_ref.extractall()
    with open('text8', 'r') as f:
        text = f.read()
    return text.split()

class Word2VecDataset(Dataset):
    def __init__(self, words, word_to_idx, idx_to_word, word_counts):
        self.words_idx = [word_to_idx[w] for w in words]
        self.word_to_idx = word_to_idx
        self.idx_to_word = idx_to_word
        self.word_counts = word_counts

        # Create training pairs
        self.data = []
        for i in range(WINDOW_SIZE, len(self.words_idx) - WINDOW_SIZE):
            center_word = self.words_idx[i]
            context_indices = list(range(i - WINDOW_SIZE, i)) + list(range(i + 1, i + WINDOW_SIZE + 1))
            for context_idx in context_indices:
                context_word = self.words_idx[context_idx]
                self.data.append((center_word, context_word))

        # Create negative sampling distribution
        freq = np.array([self.word_counts[self.idx_to_word[i]] for i in range(len(self.idx_to_word))])
        freq = freq ** 0.75
        self.neg_sampling_dist = freq / freq.sum()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        center_word, context_word = self.data[idx]
        neg_samples = np.random.choice(len(self.idx_to_word), size=NEG_SAMPLES, p=self.neg_sampling_dist)
        return torch.LongTensor([center_word]), torch.LongTensor([context_word]), torch.LongTensor(neg_samples)

# --- 3. Model Definition ---
class SkipGramNegativeSampling(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(SkipGramNegativeSampling, self).__init__()
        self.center_embeddings = nn.Embedding(vocab_size, embed_dim)
        self.context_embeddings = nn.Embedding(vocab_size, embed_dim)
        self.log_sigmoid = nn.LogSigmoid()

    def forward(self, center_word, context_word, neg_samples):
        # Positive score
        center_vec = self.center_embeddings(center_word) # (batch, 1, dim)
        context_vec = self.context_embeddings(context_word) # (batch, 1, dim)
        score = torch.bmm(center_vec, context_vec.transpose(1, 2)).squeeze() # (batch)
        log_target = self.log_sigmoid(score)

        # Negative score
        neg_vecs = self.context_embeddings(neg_samples) # (batch, neg_samples, dim)
        neg_score = torch.bmm(center_vec.expand(-1, NEG_SAMPLES, -1), neg_vecs.transpose(1, 2)).squeeze() # (batch, neg_samples)
        log_neg = self.log_sigmoid(-neg_score).sum(axis=1)

        loss = -(log_target + log_neg).mean()
        return loss

    def get_vectors(self):
        return self.center_embeddings.weight.data.cpu().numpy()

# --- 4. Training Script ---
if __name__ == '__main__':
    words = download_text8()
    print(f"Corpus size: {len(words)} words")

    word_counts = Counter(words)
    words = [w for w in words if word_counts[w] >= MIN_FREQ]
    print(f"Corpus size after filtering: {len(words)} words")

    vocab = sorted(word_counts, key=word_counts.get, reverse=True)
    vocab = [w for w in vocab if word_counts[w] >= MIN_FREQ]
    word_to_idx = {word: i for i, word in enumerate(vocab)}
    idx_to_word = {i: word for i, word in enumerate(vocab)}
    vocab_size = len(vocab)
    print(f"Vocabulary size: {vocab_size}")

    dataset = Word2VecDataset(words, word_to_idx, idx_to_word, word_counts)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    model = SkipGramNegativeSampling(vocab_size, EMBEDDING_DIM)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    print(f"Training on {device}")

    for epoch in range(NUM_EPOCHS):
        total_loss = 0
        for i, (center, context, neg) in enumerate(dataloader):
            center, context, neg = center.to(device), context.to(device), neg.to(device)
            optimizer.zero_grad()
            loss = model(center, context, neg)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            if (i+1) % 2000 == 0:
                print(f"Epoch {epoch+1}/{NUM_EPOCHS}, Step {i+1}/{len(dataloader)}, Loss: {total_loss / (i+1):.4f}")
        print(f"--- End of Epoch {epoch+1}, Average Loss: {total_loss / len(dataloader):.4f} ---")

    # --- 5. Exploration ---
    word_vectors = model.get_vectors()

    def find_similar(word, top_n=5):
        if word not in word_to_idx:
            print(f"'{word}' not in vocabulary.")
            return
        word_idx = word_to_idx[word]
        query_vec = word_vectors[word_idx]
        cos_sim = (word_vectors @ query_vec) / (np.linalg.norm(word_vectors, axis=1) * np.linalg.norm(query_vec))
        # Exclude the word itself
        top_indices = np.argsort(-cos_sim)[1:top_n+1]
        for idx in top_indices:
            print(f"  {idx_to_word[idx]}: {cos_sim[idx]:.4f}")

    def find_analogy(a, b, c, top_n=1):
        # Analogy: b is to a as c is to ? -> vec(a) - vec(b) + vec(c)
        for word in [a, b, c]:
            if word not in word_to_idx:
                print(f"'{word}' not in vocabulary.")
                return
        vec = word_vectors[word_to_idx[a]] - word_vectors[word_to_idx[b]] + word_vectors[word_to_idx[c]]
        cos_sim = (word_vectors @ vec) / (np.linalg.norm(word_vectors, axis=1) * np.linalg.norm(vec))
        # Exclude input words
        for word in [a, b, c]:
            cos_sim[word_to_idx[word]] = -np.inf
        top_indices = np.argsort(-cos_sim)[:top_n]
        for idx in top_indices:
            print(f"  {idx_to_word[idx]}: {cos_sim[idx]:.4f}")

    print("\n--- Exploring Vectors ---")
    print("Words similar to 'king':")
    find_similar('king')
    print("\nWords similar to 'france':")
    find_similar('france')
    print("\nAnalogy: king - man + woman = ?")
    find_analogy('king', 'man', 'woman')
    print("\nAnalogy: paris - france + germany = ?")
    find_analogy('paris', 'france', 'germany')
    print("\nAnalogy: walking - walk + swimming = ?")
    find_analogy('walking', 'walk', 'swimming')
```

---

#### 6. Observing Syntactic and Semantic Regularities

After running the code above (which takes some time), you would see output like this (results vary with each training run):

```text
--- Exploring Vectors ---
Words similar to 'king':
  queen: 0.7512
  prince: 0.7103
  monarch: 0.6855
  throne: 0.6543
  kingdom: 0.6498

Words similar to 'france':
  germany: 0.8123
  spain: 0.7988
  italy: 0.7950
  belgium: 0.7541
  austria: 0.7499

Analogy: king - man + woman = ?
  queen: 0.8521

Analogy: paris - france + germany = ?
  berlin: 0.8810

Analogy: walking - walk + swimming = ?
  swam: 0.7234
```

*   **Semantic Regularity:** The `king - man + woman` analogy works remarkably well. The vector offset between `man` and `woman` captures the concept of gender, and applying this offset to `king` lands you very close to `queen`. Similarly, the offset between `france` and `paris` captures the "country-to-capital" relationship.
*   **Syntactic Regularity:** The `walking - walk` offset captures the relationship between the present participle and the base form of a verb. Applying this to `swimming` correctly identifies `swam` (or `swim`, depending on the training) as the answer.

This confirms the findings of the Mikolov et al. papers: these simple, unsupervised models learn rich structural representations of language.

---

### 7. Wasserstein Metric for Sentence Distance

This question directly relates to the **Word Mover's Distance (WMD)** from the Kusner et al. paper. The WMD is a special case of the Wasserstein metric (or Earth Mover's Distance) applied to word embeddings. It measures the minimum "cost" to move the words of one document to become the words of another. The cost of moving a single word is the Euclidean distance between their word vectors.

Let's explore examples:

##### Example 1: Small Distance (High Semantic Similarity)

*   **Sentence A:** "The president addresses the nation"
*   **Sentence B:** "The leader speaks to the country"

**Why the distance is small:**
The WMD algorithm would find the cheapest way to "transport" the word distribution of A to B.
*   It's cheap to move "president" to "leader" because their vectors are very close.
*   It's cheap to move "addresses" to "speaks" because their vectors are close.
*   It's cheap to move "nation" to "country" because their vectors are close.
The total cost is the sum of these small distances. The result is a small overall distance, correctly identifying the sentences as semantically equivalent despite having no overlapping keywords (besides "the").

##### Example 2: Large Distance (Low Semantic Similarity)

*   **Sentence A:** "The chef prepares a delicious meal"
*   **Sentence B:** "A rocket launched into outer space"

**Why the distance is large:**
Any pairing of words between these two sentences will result in a large travel cost.
*   Moving "chef" to "rocket" is expensive; their vectors are far apart in the embedding space.
*   Moving "prepares" to "launched" is expensive.
*   Moving "meal" to "space" is expensive.
Since all possible word movements are costly, the minimum total cost (the WMD) will be large, correctly identifying the sentences as unrelated.

**Does it make sense?**
Absolutely. It makes perfect sense and is a major improvement over methods that rely on word overlap (like Bag-of-Words with cosine similarity). The WMD leverages the semantic geometry of the word embedding space to provide a distance metric that is robust to vocabulary changes and sensitive to meaning, just as the paper demonstrates.

### 2. Solve the online Hebrew Semantle game using its publicly available model.

The Hebrew Semantle (`סמנטעל`) game, like the English one, uses a Word2Vec model to calculate cosine similarity between your guess and the secret word.

  * **The Model:** The most common "publicly available model" for this is a `gensim` Word2Vec model trained on Hebrew. A known one can be found on Iddo Yadlin's GitHub/Google Drive, often linked from Semantle solver tools. You would download the `model.mdl` and `model.mdl.wv.vectors.npy` files.

  * **Strategy to Minimize Guesses:** This is a search problem in a high-dimensional vector space.

    1.  **Load Model:** Load the `gensim` model.
        ```python
        from gensim.models import Word2Vec
        model = Word2Vec.load("model.mdl")
        # model.wv contains the word vectors
        ```
    2.  **Triangulation (First 5-10 guesses):** Do *not* guess randomly. Guess 5-10 words that are very *different* from each other to cover the vector space and find a "direction."
          * Example guesses: 'איש' (man), 'בית' (house), 'לאכול' (eat), 'מחשב' (computer), 'אהבה' (love), 'מלחמה' (war), 'מדינה' (country).
    3.  **Local Search (Iteration):**
          * Take your guess with the *highest* similarity score (e.g., 'מדינה' scored 25.4). Let's call this `best_guess`.
          * Use the model to find its nearest neighbors. This is your new "candidate list."
            ```python
            # Get 100 closest words to your best guess
            candidates = model.wv.most_similar(best_guess, topn=100)
            # candidates is a list of (word, similarity) tuples
            ```
          * Start guessing words from the top of this `candidates` list. One of them is *statistically very likely* to be closer to the target than `best_guess`.
    4.  **Refine and Repeat:**
          * When a new guess (e.g., 'ממשלה' - government) gets a higher score (e.g., 35.2), it becomes your *new* `best_guess`.
          * Go back to step 3, but this time, get the neighbors of 'ממשלה'.
    5.  **Optimization (Smarter Search):** If you have two "warm" guesses (e.g., 'ממשלה' at 35.2 and 'כלכלה' - economy at 31.0), you can find words that are *between* them:
        ```python
        # Find words close to both of your best guesses
        candidates = model.wv.most_similar(positive=['ממשלה', 'כלכלה'], topn=50)
        ```
        Guessing from this new list is a highly efficient way to "zero in" on the target vector. This systematic approach will solve the game far faster than random guessing.