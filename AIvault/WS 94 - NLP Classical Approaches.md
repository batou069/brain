# Worksheet

## Keywords
1. Tokenization
2. Vocabulary
3. Special tokens:
    - SOS
    - UNK
    - PAD
    - MASK
4. Stop Words
5. Context
6. Text normalization
7. Bag of Words
8. Bigram/Trigram/N-gram
9. Skip Gram
10. TF-IDF
11. Latent Dirichlet Allocation (LDA)
12. Hidden Markov Model (HMM)
13. Viterbi Algorithm
14. Statistical Language Model
15. Statistical Machine Translation
## Questions
1. What is a token?
    - Why not call it "a word"?
2. Build a comprehensive list of special tokens and their intended use. Are they always the same in all frameworks?
3. What are the steps in NLP preprocessing? Do we alwys use all of them?
4. What is TF-IDF? How does it help us?
5. What is the input/output of LDA? How can we interpret the output?
6. How would you deal with misspellings and slang?
7. Why can't/shouldn't we have the vocabulary include all words (including conjugations/pluralities/genders/etc.)?
    - Find common vocabulary sizes.
8. What are the constraints for transition matrices in a HMM?
9. Explain what are transition and emission probabilities in HMM.
    - Describe how these may apply to using HMM for POS tagging.
10. The basic idea of a language model is to predict the next word using all previous words, which seems computationally infeasible. What can you "relax" to make it tractable?
11. How can language models be used for transcribing speech?
12. Machine translation has evolved from rule-based to statistical. What is the big difference between the two?
13. Stop words are everywhere, so they might not be very helpful as predictors. Should we just discard them?
    - Propose a method to decide which words are stop words.
    - Should fillers be treated as stop words?
14. Is making all the text lower case in preprocessing to reduce sparsity worth the loss of information?
    - How can we lower sparsity of numbers in the text?
    - Should we remove all punctuation from text, or does some punctuation carry more information?
    - What other sources of sparsity are there, and how should we treat them?
## Exercises
Solve the "Yahoo! Answers Topic Classification” dataset using classical approaches.
- You may use any tool that does not employ modern (deep learning) techniques.
- Compare yourself to the benchmark available on the "Papers With Code” website.

# gem

## Keywords

### 1. Tokenization
* **What is it?** Tokenization is the process of breaking down a stream of text into its constituent parts, called tokens.
* **Why is it done?** It's the very first step in nearly every NLP pipeline, converting raw text into a list of items that a program can work with.
* **More Details:**
    * **Word Tokenization:** The most common form, where tokens are words separated by spaces and punctuation.
    * **Subword Tokenization:** A more advanced method where tokens can be parts of words (e.g., "tokenization" -> "token", "##ization"). This helps manage large vocabularies and unknown words.
    * The process can be complex due to hyphens, contractions ("don't" -> "do", "n't"), and punctuation.
* **Example (Python with NLTK):**
    ```python
    import nltk
    # nltk.download('punkt') # Run once if needed
    
    text = "Don't you love N.L.P.? It's fascinating!"
    tokens = nltk.word_tokenize(text)
    
    print(tokens)
    # Output: ['Do', "n't", 'you', 'love', 'N.L.P.', '?', 'It', "'s", 'fascinating', '!']
    # Note how it splits the contraction "Don't" and handles punctuation.
    ```

---

### 2. Vocabulary
* **What is it?** The vocabulary (or lexicon) is the complete set of unique tokens that a specific model or system is designed to recognize and process.
* **Why is it done?** It allows us to map each token to a unique numerical ID, which is the only format machine learning models can process.
* **More Details:**
    * A vocabulary is typically built from a training corpus by counting all tokens.
    * To keep it a manageable size, words that appear very infrequently (e.g., only once or twice) are often excluded and mapped to an "unknown" token.
    * The size of the vocabulary is a critical hyperparameter that balances coverage and computational complexity.
* **Conceptual Example:**
    * Corpus: "The cat sat. The dog ran."
    * Tokens: {"The", "cat", "sat", ".", "dog", "ran"}
    * Vocabulary Mapping: `{"The": 0, "cat": 1, "sat": 2, ".": 3, "dog": 4, "ran": 5}`

---

### 3. Special tokens
* **What is it?** These are artificial tokens added to a model's vocabulary to handle metadata or structural information about the text, rather than representing actual words.
* **Why is it done?** They provide the model with essential information for tasks like sequence processing, handling unknown words, and batching data.
* **More Details:**
    * `[UNK]` or `<UNK>` (**Unknown**): Represents a token that is not in the model's vocabulary.
    * `[PAD]` or `<PAD>` (**Padding**): Used to make all sequences in a batch the same length by adding this token to shorter sequences.
    * `[SOS]` / `[BOS]` or `<s>` (**Start/Beginning of Sentence**): Marks the beginning of a sequence, often used in generative models.
    * `[EOS]` or `</s>` (**End of Sentence**): Marks the end of a sequence.
    * `[MASK]` (**Mask**): Used in some models (like BERT) to represent a token that has been hidden and which the model must predict.
* **Example:** A sentence prepared for a model might look like this:
    `[SOS] The quick brown fox . [EOS] [PAD] [PAD]`

---

### 4. Stop Words
* **What is it?** Stop words are extremely common words (like "the", "a", "is", "in") that are often filtered out from text before processing.
* **Why is it done?** In many tasks (like search or topic modeling), these words add a lot of noise and carry very little unique information. Removing them helps the model focus on the important keywords.
* **More Details:**
    * There is no single, universal list of stop words; they can be context- or language-dependent.
    * Removing them is a form of dimensionality reduction.
    * **Caution:** For some tasks like language modeling or sentiment analysis where sentence structure and negation are important ("not good"), removing stop words can be harmful.
* **Example (Python with NLTK):**
    ```python
    from nltk.corpus import stopwords
    # nltk.download('stopwords') # Run once if needed
    
    english_stopwords = set(stopwords.words('english'))
    text = "This is a sample sentence showing off stop word filtration."
    tokens = text.lower().split()
    
    filtered_tokens = [word for word in tokens if word not in english_stopwords]
    print(filtered_tokens)
    # Output: ['sample', 'sentence', 'showing', 'stop', 'word', 'filtration.']
    ```

---

### 5. Context
* **What is it?** In NLP, context refers to the words surrounding a target word, which provide clues to the target word's meaning and function.
* **Why is it important?** Language is ambiguous, and context is the primary mechanism for disambiguation. The meaning of "bank" is determined entirely by its context.
* **More Details:**
    * **Local Context:** The immediate neighboring words. N-gram models operate on a fixed window of local context.
    * **Global Context:** Information from the entire document or conversation. Modern Transformer models are designed to process this much broader context.
* **Conceptual Example:**
    * Sentence 1: "I need to deposit money at the **bank**." (Context: "deposit money" -> financial institution)
    * Sentence 2: "We sat on the river **bank** and fished." (Context: "river", "fished" -> side of a river)

---

### 6. Text Normalization
* **What is it?** The process of transforming text into a single, canonical form to ensure consistency.
* **Why is it done?** To reduce the vocabulary size and the overall sparsity of the data. It ensures that "Run", "running", and "ran" are all treated as the same concept.
* **More Details:** This is an umbrella term that includes several preprocessing steps:
    * **Lowercasing:** Converting all text to lowercase.
    * **Stemming/Lemmatization:** Reducing words to their root form.
    * **Punctuation Removal:** Stripping out punctuation marks.
    * **Expanding Contractions:** Changing "he's" to "he is".
    * **Removing numbers or special characters.**
* **Example Pipeline:**
    * **Input:** "He's running at 5 p.m.!"
    * **Output after normalization:** `['he', 'be', 'run', 'at', '5', 'p', 'm']` (after expanding, lowercasing, tokenizing, and lemmatizing).

---

### 7. Bag of Words (BoW)
* **What is it?** A simple text representation model that treats a piece of text as an unordered collection (a "bag") of its words, disregarding grammar and word order but keeping track of frequency.
* **Why is it done?** It converts variable-length, unstructured text into a fixed-length numerical vector, which is required by most classical machine learning algorithms.
* **Example:**
    * Sentence 1: "The cat sat on the mat."
    * Sentence 2: "The dog ate the cat."
    * **Vocabulary:** `{The, cat, sat, on, mat, dog, ate}`
    * **BoW Vector for Sentence 1:** `[2, 1, 1, 1, 1, 0, 0]` (#The, #cat, #sat, ...)

---

### 8. Bigram/Trigram/N-gram
* **What is it?** An n-gram is a contiguous sequence of 'n' items (typically words) from a given text. A bigram has n=2, and a trigram has n=3.
* **Why is it done?** They are a simple yet effective way to capture local word order and context, which the basic Bag-of-Words model completely ignores.
* **Example:** For the sentence "The quick brown fox jumps."
    * **Bigrams (2-grams):** "The quick", "quick brown", "brown fox", "fox jumps"
    * **Trigrams (3-grams):** "The quick brown", "quick brown fox", "brown fox jumps"

---

### 9. Skip Gram
* **What is it?** A model architecture used to learn word embeddings (like Word2Vec) by taking a target word as input and trying to predict its surrounding context words.
* **Why is it done?** It's a highly effective method for creating dense vector representations of words (word embeddings) from unlabeled text data. These embeddings capture semantic relationships.
* **More Details:**
    * It's the conceptual inverse of the **Continuous Bag-of-Words (CBOW)** model, which predicts a target word from its context.
    * For a sentence like "... quick brown **fox** jumps over ...", the skip-gram model would create training pairs like `(fox, quick)`, `(fox, brown)`, `(fox, jumps)`, `(fox, over)`.
    * Skip-gram is known to perform better for rare words compared to CBOW.


---

### 10. TF-IDF
* **What is it?** Term Frequency-Inverse Document Frequency is a numerical statistic that reflects how important a word is to a specific document within a larger collection (corpus).
* **Why is it done?** It's an improvement over simple Bag-of-Words. It increases the weight of words that are frequent in a document but rare across the corpus, effectively highlighting the document's key terms.
* **Math:** The score is the product of two components:
    * **Term Frequency (TF):** How often a term `t` appears in a document `d`. $`\text{tf}(t, d)`$
    * **Inverse Document Frequency (IDF):** A measure of the term's rarity across the corpus `D`. $`\text{idf}(t, D) = \log \frac{|D|}{|\{d \in D : t \in d\}|}`$
    * **Score:** $\text{tfidf}(t, d, D) = \text{tf}(t, d) \times \text{idf}(t, D)$

---

### 11. Latent Dirichlet Allocation (LDA)
* **What is it?** An unsupervised generative statistical model used for topic modeling. It assumes that documents are a mixture of topics, and topics are a mixture of words.
* **Why is it done?** To discover and extract the hidden thematic structure (topics) from a large collection of unlabeled documents.
* **Conceptual Example:**
    * **Input:** 10,000 news articles.
    * **LDA Process:** The algorithm analyzes word co-occurrence patterns.
    * **Output:** Might identify "Topic 1" (with words like "election," "government," "vote") and "Topic 2" (with words like "stock," "market," "trade"), and then describe each article as a mix of these topics (e.g., Article 101 is 80% Topic 1, 20% Topic 2).

---

### 12. Hidden Markov Model (HMM)
* **What is it?** A statistical model used for sequential data, which assumes that the system is a Markov process with unobserved (hidden) states.
* **Why is it done?** It's excellent for tasks where you have a sequence of observations and want to infer the most likely sequence of underlying states. The classic NLP application is **Part-of-Speech (POS) Tagging**.
* **More Details:**
    * **Hidden States:** The thing you want to predict (e.g., POS tags like `NOUN`, `VERB`).
    * **Observations:** The data you can see (e.g., the words in a sentence).
    * It's defined by **Transition Probabilities** (chance of moving from one state to another) and **Emission Probabilities** (chance of a state producing an observation).

---

### 13. Viterbi Algorithm
* **What is it?** A dynamic programming algorithm for finding the most likely sequence of hidden states—known as the Viterbi path—that results in a sequence of observed events.
* **Why is it done?** It's the standard algorithm for "decoding" a Hidden Markov Model. Given a sentence (observations), Viterbi efficiently calculates the most probable sequence of POS tags (hidden states).
* **Conceptual Example:** For the sentence "Time flies like an arrow," Viterbi would build a grid of all possible tags for each word and find the single path through that grid with the highest overall probability, preventing a combinatorial explosion of possibilities.
* **Math (Core Recurrence):** The algorithm finds the probability of the most likely path ending in state `j` at time `t` using the probabilities from time `t-1`:
    $$ v_t(j) = \max_{i=1}^{N} [v_{t-1}(i) \cdot a_{ij}] \cdot b_j(o_t) $$
    where $`v_t(j)`$ is the Viterbi probability, $`a_{ij}`$ is the transition probability, and $`b_j(o_t)`$ is the emission probability.

---

### 14. Statistical Language Model
* **What is it?** A probability distribution over a sequence of words. Its core function is to assign a probability to a piece of text or to predict the next word in a sequence.
* **Why is it done?** It forms the basis for tasks like machine translation, speech recognition, and spelling correction by allowing a system to distinguish between plausible and implausible sentences.
* **More Details:**
    * The classic statistical LM is the **n-gram model**. It uses the probability of previous `n-1` words to predict the next word.
    * It answers the question: "How likely is this sentence to occur in this language?" A well-trained model would assign $`P(\text{"the cat sat on the mat"}) > P(\text{"mat the cat on sat the"})`$.

---

### 15. Statistical Machine Translation (SMT)
* **What is it?** An approach to machine translation that learns to translate by analyzing statistical models whose parameters are derived from analyzing bilingual text corpora.
* **Why is it done?** It was a major leap forward from brittle, rule-based systems. SMT could learn translation patterns automatically from data without needing hand-crafted linguistic rules.
* **More Details:**
    * It consists of two main components: a **translation model** (which learns phrase-to-phrase translations like "wie geht es Ihnen" -> "how are you") and a **language model** (which ensures the output in the target language is fluent).
    * It was the dominant paradigm for MT before being superseded by Neural Machine Translation (NMT) in the mid-2010s.

***

## Questions

### **1. What is a token? Why not call it "a word"?**

* **Short Answer:** A token is a useful unit of text for a program. It's often a word, but can also be punctuation, a part of a word, or a symbol.

* **Long Answer:** We use the term "token" because it's more precise from a computational standpoint. The concept of a "word" is linguistic and can be ambiguous. Tokens can be:
    * **Words:** "cat", "house", "running"
    * **Punctuation:** ".", "?", "!"
    * **Symbols:** "$", "%", "@"
    * **Parts of words:** In "don't", the tokens might be "do" and "n't". In subword tokenization, "unhappiness" could be tokenized into "un" and "happiness".
    The term "token" encompasses all these possibilities that a program needs to handle.

### **2. Build a comprehensive list of special tokens and their intended use. Are they always the same in all frameworks?**

* **Short Answer:** Common special tokens include `[UNK]`, `[PAD]`, `[SOS]`/`[BOS]`, `[EOS]`, and `[MASK]`. They are **not** standardized and often have different names and exact behaviors across different models and frameworks.

* **Long Answer:**
    * `[UNK]` (**Unknown**): Replaces any word not present in the model's vocabulary.
    * `[PAD]` (**Padding**): Added to the end of shorter sequences in a batch to make them all equal length for efficient processing.
    * `[SOS]` / `[BOS]` (**Start of Sequence/Sentence**): An initial token given to generative models to prompt them to start generating text.
    * `[EOS]` (**End of Sequence/Sentence**): A token that a generative model learns to predict to signal that it has finished its output.
    * `[MASK]` (**Masking**): A placeholder used during training for models like BERT. The model's task is to predict the original token that was masked.
    * `[CLS]` (**Classification**): In models like BERT, this token is prepended to the input, and its final hidden state is used as the aggregate sequence representation for classification tasks.
    * `[SEP]` (**Separator**): Used to separate two different sentences or segments within a single input (e.g., for question-answering tasks).

    **Framework Differences:** For example, BERT uses `[CLS]` and `[SEP]`, while models like GPT-2 use an `|endoftext|` token for both starting and ending sequences. The exact string representation (`<pad>` vs `[PAD]`) also varies.

### **3. What are the steps in NLP preprocessing? Do we always use all of them?**

* **Short Answer:** Common steps include tokenization, lowercasing, stop word removal, and stemming/lemmatization. No, we do not always use all of them; the pipeline must be tailored to the specific task.

* **Long Answer:** A typical preprocessing pipeline might look like this:
    1.  **Sentence Segmentation:** Breaking a document into individual sentences.
    2.  **Tokenization:** Breaking sentences into tokens.
    3.  **Lowercasing:** Converting all text to a single case.
    4.  **Stop Word Removal:** Deleting common, low-information words.
    5.  **Punctuation Removal:** Stripping out punctuation marks.
    6.  **Stemming or Lemmatization:** Reducing words to their root form.

    **We do not always use all steps.** For example:
    * In **sentiment analysis**, punctuation like "!" is important, and removing the stop word "not" would completely flip the meaning.
    * In **machine translation** or **language modeling**, the original sentence structure, including stop words and case, is essential.
    * For **named entity recognition**, capitalization is a key feature ("Apple" vs. "apple").

### **4. What is TF-IDF? How does it help us?**

* **Short Answer:** TF-IDF is a scoring method that measures how important a word is to a document in a corpus. It helps by highlighting keywords that are unique to a document, improving the performance of search and classification models.

* **Long Answer:** TF-IDF improves upon simple word counts (Bag-of-Words) by balancing two factors:
    1.  **Term Frequency (TF):** How often a word appears in a document. This suggests the word is important to *that* document.
    2.  **Inverse Document Frequency (IDF):** How rare the word is across all documents. This gives more weight to words that are not just common fluff (like "the" or "is").

    By multiplying these two scores, TF-IDF assigns the highest values to words that are frequent in a specific document but rare everywhere else. This makes it an excellent feature for tasks like identifying the topic of a document or finding documents relevant to a specific search query.

### **5. What is the input/output of LDA? How can we interpret the output?**

* **Short Answer:** The input is a corpus of documents (usually represented as bag-of-words). The output is a set of topics (defined by word probabilities) and a topic mixture for each document.

* **Long Answer:**
    * **Input:** A document-term matrix, which is essentially a bag-of-words representation for every document in the corpus.
    * **Output:**
        1.  **Topic-Word Distribution ($`\phi`$):** For each topic, a list of words and their probability of belonging to that topic. For example: `Topic 1: {"gene": 0.05, "dna": 0.04, ...}`.
        2.  **Document-Topic Distribution ($`\theta`$):** For each document, a distribution showing its mixture of topics. For example: `Document 12: {"Topic 1": 0.7, "Topic 5": 0.2, "Topic 8": 0.1}`.

    * **Interpretation:** LDA itself does not name the topics. A human must look at the top 10-15 most probable words for a given topic and assign a human-readable label. If the top words are "gene," "dna," "sequence," and "protein," you would interpret that as the "Genetics" topic.

### **6. How would you deal with misspellings and slang?**

* **Short Answer:** By using text normalization techniques, such as applying a spell checker for misspellings and creating a custom dictionary to map slang to standard words.

* **Long Answer:**
    * **Misspellings:**
        * **Algorithmic Spell Checkers:** Use libraries (like `pyspellchecker`) that check words against a dictionary and suggest corrections based on **edit distance** (e.g., Levenshtein distance), which measures the number of changes needed to get from one word to another.
        * **Corpus-based Correction:** Analyze a large corpus to find common misspellings and their likely corrections (e.g., "tomorow" almost always means "tomorrow").
    * **Slang and Jargon:**
        * **Custom Dictionaries:** The most common approach is to manually create a dictionary or key-value map to replace slang with its standard equivalent (e.g., `{"brb": "be right back", "lol": "laughing out loud"}`). This is domain-specific and requires maintenance.
        * **Word Embeddings:** Sometimes, word embedding models trained on large, informal corpora (like Twitter data) can learn that slang words are semantically close to their standard equivalents, handling them implicitly.

### **7. Why can't/shouldn't we have the vocabulary include all words? Find common vocabulary sizes.**

* **Short Answer:** Including all word forms would create a massive, sparse vocabulary, making models computationally expensive, slow, and poor at generalizing to new text.

* **Long Answer:**
    * **The Curse of Dimensionality:** Every unique word in the vocabulary becomes a dimension in our data. A vocabulary with millions of words (including all inflections like "run", "running", "ran") creates an incredibly high-dimensional and sparse space. Most models struggle with this.
    * **Poor Generalization:** If a model learns separate meanings for "car" and "cars," it might not apply what it learned from sentences about "car" to sentences about "cars." Normalization (stemming/lemmatization) helps the model understand these are the same concept.
    * **Computational Cost:** Larger vocabularies require more memory and processing power.

    * **Common Vocabulary Sizes:**
        * **Classical Models:** Often in the range of 10,000 to 100,000 unique words, after filtering by frequency.
        * **Modern Subword Models (BERT, GPT):** Typically between **30,000 and 50,000 subword tokens**. This size is a sweet spot that can represent almost any word while remaining manageable.

### **8. What are the constraints for transition matrices in a HMM?**

* **Short Answer:** Every row in the transition matrix (and the emission matrix) must sum to 1.

* **Long Answer:** Both the transition and emission matrices represent probability distributions.
    * **Transition Matrix ($`A`$):** The entry $`A_{ij}`$ is the probability of moving from state `i` to state `j` ($`P(state_j | state_i)`$). For any given state `i`, the model *must* transition to *some* next state. Therefore, the sum of probabilities of transitioning from state `i` to all possible states `j` must be 1.  $`\sum_{j=1}^{N} A_{ij} = 1`$ for all `i`.
    * **Emission Matrix ($`B`$):** The entry $`B_j(k)`$ is the probability of observing symbol `k` given that you are in state `j` ($`P(observation_k | state_j)`$). For any given state `j`, it *must* emit *some* observation. Therefore, the probabilities of emitting all possible observations must sum to 1.

### **9. Explain what are transition and emission probabilities in HMM. Describe how these may apply to using HMM for POS tagging.**

* **Short Answer:** Transition probability is the chance of one tag following another. Emission probability is the chance of a tag generating a specific word.

* **Long Answer:** In the context of POS tagging:
    * **Transition Probability ($`P(tag_j | tag_i)`$):** This is the probability that one part-of-speech tag will follow another. This captures grammatical structure.
        * **Example:** The probability of a `NOUN` following a `DETERMINER` (like "the") is very high. $`P(NOUN | DETERMINER) \approx 0.9`$.
        * **Example:** The probability of a `VERB` following another `VERB` is low. $`P(VERB | VERB) \approx 0.1`$.
    * **Emission Probability ($`P(word_k | tag_j)`$):** This is the probability of observing a particular word given a certain part-of-speech tag. This captures the lexical properties of the language.
        * **Example:** Given the tag is `NOUN`, the probability of the word being "cat" is relatively high. $`P(\text{"cat"} | NOUN)`$.
        * **Example:** Given the tag is `NOUN`, the probability of the word being "jumped" is nearly zero. $`P(\text{"jumped"} | NOUN) \approx 0`$.

    An HMM combines these two probabilities to find the most likely tag sequence for a given sentence.

### **10. The basic idea of a language model is to predict the next word using all previous words, which seems computationally infeasible. What can you "relax" to make it tractable?**

* **Short Answer:** You relax the condition by making the **Markov Assumption**.

* **Long Answer:** The chain rule of probability states that the probability of a sequence is $`P(w_1, w_2, ..., w_n) = P(w_1)P(w_2|w_1)...P(w_n|w_1,...,w_{n-1})`$. Calculating the final term, which depends on the entire history, is indeed intractable.

    The relaxation is the **Markov Assumption**: we assume that the probability of the next word depends *only* on a fixed window of the `n-1` preceding words, not the entire history.

    * For a **bigram model (n=2)**, we assume $`P(w_k | w_1, ..., w_{k-1}) \approx P(w_k | w_{k-1})`$.
    * For a **trigram model (n=3)**, we assume $`P(w_k | w_1, ..., w_{k-1}) \approx P(w_k | w_{k-2}, w_{k-1})`$.

    This simplification makes the problem computationally feasible, as we only need to count and store probabilities for fixed-size n-grams.

### **11. How can language models be used for transcribing speech?**

* **Short Answer:** A language model helps an Automatic Speech Recognition (ASR) system decide between phonetically similar phrases by choosing the one that is grammatically and semantically more probable.

* **Long Answer:** An ASR system has two main components:
    1.  **Acoustic Model:** This model listens to the audio signal and produces a list of likely phoneme sequences. For example, it might not be able to distinguish between the sounds for "recognize speech" and "wreck a nice beach."
    2.  **Language Model:** This model takes the candidate transcriptions from the acoustic model and assigns a probability to each one based on how likely that sequence of words is in the target language.

    The language model will assign a much, much higher probability to the sequence "recognize speech" than to "wreck a nice beach." The ASR system then outputs the sequence with the highest combined score from both models.

### **12. Machine translation has evolved from rule-based to statistical. What is the big difference between the two?**

* **Short Answer:** Rule-based systems rely on hand-crafted linguistic rules, while statistical systems learn translation patterns automatically from massive amounts of data.

* **Long Answer:**
    * **Rule-Based Machine Translation (RBMT):**
        * **How it works:** Linguists and programmers write explicit rules for grammar, syntax, and dictionaries for both the source and target languages. The system parses the source sentence, transforms the structure based on rules, and then generates the target sentence.
        * **Pros:** Grammatically precise (when rules exist), predictable.
        * **Cons:** Incredibly brittle, astronomically expensive to create and maintain, cannot handle exceptions or new linguistic phenomena, and often produces unnatural-sounding translations.

    * **Statistical Machine Translation (SMT):**
        * **How it works:** The system is given a huge parallel corpus (e.g., millions of sentences translated by humans). It learns the probability that a source phrase translates to a target phrase. It then combines these phrase probabilities with a language model to find the most probable and fluent translation.
        * **Pros:** Learns from data, much more robust, handles idioms better, produces more fluent output.
        * **Cons:** Heavily dependent on the quality and quantity of data, can make strange, non-grammatical errors.

### **13. Stop words are everywhere, so they might not be very helpful as predictors. Should we just discard them? Propose a method to decide which words are stop words. Should fillers be treated as stop words?**

* **Short Answer:** No, we shouldn't always discard them, especially when sentence structure or negation is important. A good way to identify stop words is to find words with the highest document frequency. Fillers are typically treated as stop words.

* **Long Answer:**
    * **When to keep them:** Discarding stop words is often harmful for:
        * **Sentiment Analysis:** "not good" vs "good". "not" is a critical stop word.
        * **Language Modeling:** These models need to understand grammar and fluency, which relies heavily on function words.
        * **Machine Translation:** Structure is everything.
    * **Method to decide:** The most common data-driven method is to use **Document Frequency** (DF), which is the percentage of documents in the corpus that contain a given word. Words that appear in a very high percentage of documents (e.g., > 80-90%) are excellent candidates for a stop word list because they don't help differentiate between documents.
    * **Fillers:** Yes, fillers like "uh," "um," "like," "you know" are almost always treated as stop words in text analysis and are removed during preprocessing, as they add no semantic content.

### **14. Is making all the text lower case in preprocessing to reduce sparsity worth the loss of information?**

* **Short Answer:** In most classical NLP tasks like text classification, yes, the benefit of reducing sparsity outweighs the information loss. For tasks like Named Entity Recognition, it's often better to preserve case.

* **Long Answer:**
    * **How can we lower sparsity of numbers in the text?**
        The standard approach is to replace all numbers with a single special token, like `<NUM>` or `[NUM]`. This way, the model learns a single representation for "any number" instead of treating "10", "3.14", and "2025" as entirely different, rare tokens.
    * **Should we remove all punctuation from text, or does some punctuation carry more information?**
        Some punctuation definitely carries more information. While commas or hyphens might be safely removed for a simple bag-of-words model, others are critical:
        * `.` is the primary signal for sentence boundaries.
        * `?` indicates a question, a vital piece of information for dialogue systems.
        * `!` is a strong signal for sentiment analysis.
    * **What other sources of sparsity are there, and how should we treat them?**
        * **Misspellings and Typos:** Create huge sparsity. Treatment: Spell correction.
        * **Rare Words:** Words that appear only once or twice in a large corpus. Treatment: Group them all under a single `[UNK]` token.
        * **Rich Morphology:** Languages with many word forms (e.g., German, Russian). Treatment: Heavy reliance on stemming or lemmatization.

***

## Exercises

### **Task:** Solve the "Yahoo! Answers Topic Classification” dataset using classical approaches.ual plan to tackle this exercise using `scikit-learn`, a powerful library for classical machine learning.

### 1.  **Setup and Data Loading:**
* Find and download the dataset. It usually comes as a CSV file with columns for the question/answer text and the corresponding topic/category.
* Load the data into a pandas DataFrame. Explore the data: check the number of samples, the number of classes (topics), and the class distribution.

### 2.  **Preprocessing Pipeline:**
* Write a Python function to preprocess the text. This is the most critical step.
* Start with a simple pipeline: **lowercasing** and **tokenization**.
* Later, experiment with adding **stop word removal** and **lemmatization** (or stemming) to see how it affects performance.

### 3.  **Feature Extraction (Vectorization):**
* The goal is to convert your preprocessed text into numerical vectors.
* **Approach A: CountVectorizer (Bag-of-Words):** This will create vectors where each element is the count of a word from the vocabulary.
* **Approach B: TfidfVectorizer (TF-IDF):** This will create vectors where word counts are weighted by their importance (TF-IDF score). TF-IDF usually outperforms simple counts.
* Use `scikit-learn`'s `TfidfVectorizer`, which can handle tokenization, lowercasing, and stop word removal all in one step.

### 4.  **Model Training and Evaluation:**
* Split your data into a training set and a testing set (e.g., 80% train, 20% test).
* Train several classical classifiers on the TF-IDF vectors:
    * **Multinomial Naive Bayes (`MultinomialNB`):** A very fast and effective baseline for text classification.
    * **Logistic Regression (`LogisticRegression`):** Another powerful and interpretable baseline.
    * **Linear Support Vector Machine (`LinearSVC`):** Often one of the best-performing classical models for this task.
* For each model, predict the topics for the test set and evaluate the performance using `sklearn.metrics.classification_report`, which gives you **accuracy, precision, recall, and F1-score**.

### 5.  **Benchmarking:**
* Take your best model's accuracy score.
* Go to the "Papers With Code" page for the Yahoo! Answers dataset.
* Find the benchmarks for non-deep-learning models (look for methods like "SVM," "BoW," "LR"). Compare your result. Don't be discouraged if you don't match the top score perfectly—they often use more advanced feature engineering, but you should be in the same ballpark. Good luck! 🚀