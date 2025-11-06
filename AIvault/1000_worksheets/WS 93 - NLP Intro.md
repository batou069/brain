# Worksheet
## Keywords

- [x] 1. Stemming ✅ 2025-10-15
- [x] 1. Lemmatization ✅ 2025-10-15
- [x] 2. Part-of-speech tagging ✅ 2025-10-15
- [x] 3. Syntax Parsing / Dependency Parsing ✅ 2025-10-16
- [x] 4. Sentence Boundary Detection ✅ 2025-10-16
- [x] 5. Word Sense Disambiguation ✅ 2025-10-16
- [x] 6. Named Entity Recognition/Resolution ✅ 2025-10-16
- [x] 7. Machine Translation ✅ 2025-10-16
- [x] 8. Text Classification ✅ 2025-10-16
- [x] 9. Sentiment Analysis ✅ 2025-10-16
- [x] 10. Topic Modeling ✅ 2025-10-16
- [x] 11. Plagiarism Detection ✅ 2025-10-16
- [x] 12. Language Model ✅ 2025-10-16
- [x] 13. Text Summarization ✅ 2025-10-16
- [x] 14. Coreference Resolution ✅ 2025-10-16
- [x] 15. Question Answering ✅ 2025-10-16
- [x] 16. Conversational Agents (Chatbots) ✅ 2025-10-16

## Questions
- [ ] 1. What makes NLP, which deals with text understanding, different from other domains of ML?
- [ ] 2. Find at least 5 more NLP tasks that are not listed above.
- [ ] 3. How did we solve NLP problems before the deep learning era? What are the pros and cons?
- [ ] 4. Are there unsupervised NLP tasks?
- [ ] 5. Analyzing text is one thing, generating text is another. Which NLP tasks fall under which category?
- [ ] 6. List some key differences between Named Entity Recognition and Named Entity Resolution - both in problem statement and in how they may be
- [ ] solved.
- [ ] 7. Which is better, stemming or lemmatization?
- [ ] 8. A big challenge in some NLP tasks is that there may be many different correct outputs for the same input.
- [ ] Identify the NLP tasks where that would be a problem, and find how is that reflected in different common metrics constructed for these tasks.
- [ ] 9. Which classical ML models can be used for NLP problems?
- [ ]     - Can any of them take into account the order of words?
- [ ] 10. Everyone totally gets sarcasm, so... Like... Why would detecting it be any sort of a "challenge" for a genius computer?
## Exercises
Find an open-source NLP tool that can provide (and preferably visualize) syntax trees, POS tags, and dependency trees.
Play around with English sentences, both simple and complex ones.
Can you understand the different types of POS and dependencies from these examples?

# Gem

## Keywords

### 1. Stemming
* **What is it?** Stemming is a crude, rule-based process for chopping off the ends of words to get to the root form, or "stem".
* **Why is it done?** It's used to group different inflections of a word together. For example, in a search engine, you want a search for "running" to also find documents with "run" and "ran".
* **More Details:**
    * It's a heuristic process, meaning it uses simple rules and doesn't always get it right.
    * The resulting "stem" might not be a real dictionary word (e.g., "studies" might become "studi").
    * It's very fast and computationally cheap.
    * Common algorithms include the **Porter stemmer** (the original and most famous) and the **Snowball stemmer** (an improved version of Porter).
* **Example (Python with NLTK):**
    ```python
    from nltk.stem import PorterStemmer
    
    stemmer = PorterStemmer()
    words = ["program", "programming", "programmers", "programs"]
    stemmed_words = [stemmer.stem(word) for word in words]
    
    print(stemmed_words)
    # Output: ['program', 'program', 'programm', 'program'] 
    # Notice the imperfection with "programmers" -> "programm"
    ```
* **Variations:** The main variations are different algorithms like Porter, Snowball, and Lancaster. They differ in their rule sets and how aggressively they chop words.

---

### 2. Lemmatization
* **What is it?** Lemmatization is the process of reducing a word to its base or dictionary form, known as the "lemma".
* **Why is it done?** Like stemming, it groups different forms of a word. However, it does so with a much higher degree of accuracy, ensuring the root form is a valid word. This is crucial for applications that need to understand meaning.
* **More Details:**
    * It uses a vocabulary and morphological analysis, so it knows that "better" has "good" as its lemma.
    * It's significantly slower than stemming because it needs to look up words in a dictionary (like WordNet).
    * The process is more accurate if you provide the word's **Part-of-Speech (POS)** tag (e.g., telling it that "saw" is a verb, not a noun).
* **Example (Python with NLTK):**
    ```python
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet # To get POS tags
    
    lemmatizer = WordNetLemmatizer()
    
    print(f"Leaf -> {lemmatizer.lemmatize('leaves', pos=wordnet.NOUN)}")  # Specify it's a noun
    print(f"Leave -> {lemmatizer.lemmatize('leaves', pos=wordnet.VERB)}")  # Specify it's a verb
    print(f"Better -> {lemmatizer.lemmatize('better', pos=wordnet.ADJ)}") # Specify it's an adjective
    
    # Output:
    # Leaf -> leaf
    # Leave -> leave
    # Better -> good
    ```
* **Alternatives:** Stemming is the main alternative. The choice between them is a classic **speed vs. accuracy** trade-off.

---

### 3. Part-of-speech (POS) tagging
* **What is it?** POS tagging is the process of assigning a grammatical category—like noun, verb, adjective, etc.—to each word in a sentence. 🏷️
* **Why is it done?** It's a fundamental step for many higher-level NLP tasks. For example, it helps lemmatization work correctly and is crucial for understanding the grammatical structure of a sentence (syntax parsing).
* **More Details:**
    * Early methods were rule-based (e.g., if a word ends in "-ing" and follows a form of "to be", it's a verb).
    * Modern methods are statistical, often using models like **Hidden Markov Models (HMMs)** or deep learning models (LSTMs, Transformers) that learn from large annotated corpora.
    * Tag sets can vary. The most common is the Penn Treebank tag set, which has tags like `NN` (singular noun), `NNS` (plural noun), `VB` (verb, base form), `VBG` (verb, gerund), etc.
* **Example (Python with NLTK):**
    ```python
    import nltk
    
    # You might need to download the tagger first:
    # nltk.download('averaged_perceptron_tagger')
    
    sentence = "The quick brown fox jumps over the lazy dog."
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    
    print(pos_tags)
    # Output:
    # [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'NN'), 
    #  ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), 
    #  ('dog', 'NN'), ('.', '.')]
    # DT: Determiner, JJ: Adjective, NN: Noun, VBZ: Verb (3rd person singular present)
    ```

---

### 4. Syntax Parsing / Dependency Parsing
* **What is it?** It's the process of analyzing the grammatical structure of a sentence to understand how words relate to each other.
* **Why is it done?** To move beyond individual words and understand who did what to whom. It's essential for complex question answering, information extraction, and machine translation.
* **More Details:**
    * **Constituency Parsing:** Breaks a sentence down into nested phrases (Noun Phrase, Verb Phrase, etc.). It's represented as a tree structure.
    * **Dependency Parsing:** Creates a tree where words are connected by directed links representing grammatical relationships (dependencies). Each link has a type (e.g., `nsubj` for nominal subject, `dobj` for direct object).
    * Dependency parsing is more popular now as the relationships it provides are often more directly useful for downstream tasks.
* **Example (Python with spaCy):**
    ```python
    import spacy
    
    # Load a pre-trained model
    # You may need to run: python -m spacy download en_core_web_sm
    nlp = spacy.load("en_core_web_sm")
    
    doc = nlp("Apple is looking at buying a U.K. startup for $1 billion.")
    
    for token in doc:
        print(f"{token.text:<10} | {token.pos_:<7} | {token.dep_:<10} | {token.head.text}")
        
    # Output snippet:
    # Apple      | PROPN   | nsubj      | looking
    # is         | AUX     | aux        | looking
    # looking    | VERB    | ROOT       | looking
    # at         | ADP     | prep       | looking
    # buying     | VERB    | pcomp      | at
    # startup    | NOUN    | dobj       | buying
    
    # This shows "Apple" is the subject of "looking", and "startup" is the object of "buying".
    ```


---

### 5. Sentence Boundary Detection (SBD)
* **What is it?** The task of identifying where sentences begin and end in a text.
* **Why is it done?** It's a crucial first step (pre-processing) for most NLP tasks that operate on a sentence level, like parsing or machine translation.
* **More Details:**
    * It seems easy—just split on periods, right? But it's tricky because periods are ambiguous. They can be used in abbreviations (Mr., U.S.A.), numbers (3.14), or ellipses (...).
    * Modern SBD systems use a combination of rules (e.g., a period followed by a space and a capital letter is likely a sentence end) and machine learning models trained on annotated text.
    * Libraries like NLTK and spaCy have highly accurate, pre-trained models for this.
* **Example (Python with spaCy):**
    ```python
    import spacy
    
    nlp = spacy.load("en_core_web_sm")
    text = "Dr. Strange said, 'This is the first sentence.' Then he left. U.S.A. is a country."
    doc = nlp(text)
    
    for sent in doc.sents:
        print(sent.text)
        
    # Output:
    # Dr. Strange said, 'This is the first sentence.'
    # Then he left.
    # U.S.A. is a country.
    # Note how it correctly handles "Dr." and "U.S.A."
    ```

---

### 6. Word Sense Disambiguation (WSD)
* **What is it?** The task of identifying which specific meaning (sense) of a word is used in a given context.
* **Why is it done?** Many words are polysemous (have multiple meanings). To truly understand a text, a machine needs to know if "bank" refers to a financial institution or a river bank.
* **More Details:**
    * **Knowledge-based methods:** Use external resources like dictionaries or lexical databases (e.g., WordNet) to determine senses.
    * **Supervised methods:** Treat WSD as a classification problem. A model is trained on text where each ambiguous word has been manually labeled with its correct sense. This requires a lot of labeled data.
    * **Unsupervised methods:** Cluster occurrences of a word based on their context, assuming that words in similar contexts have similar meanings.
* **Conceptual Example:**
    * Sentence 1: "I deposited money in the **bank**." -> *Sense: Financial Institution*
    * Sentence 2: "We had a picnic on the river **bank**." -> *Sense: River's Edge*
    * An algorithm would look at surrounding words like "money" and "deposited" vs. "river" and "picnic" to make the decision.

---

### 7. Named Entity Recognition (NER)
* **What is it?** The task of locating and classifying named entities in text into pre-defined categories such as person names, organizations, locations, dates, etc.
* **Why is it done?** It's a cornerstone of information extraction, helping to quickly find the "who, what, where, and when" in a document. It powers search, question answering, and content recommendation.
* **More Details:**
    * Common entity types include `PERSON`, `ORG` (Organization), `GPE` (Geopolitical Entity, like countries/cities), and `DATE`.
    * It's typically framed as a sequence labeling task. Each word is tagged with a label indicating if it's outside an entity (`O`), at the beginning of an entity (`B-TYPE`), or inside an entity (`I-TYPE`). This is called the BIO scheme.
    * Modern NER systems use deep learning models like BiLSTMs with a CRF layer or Transformers (like BERT).
* **Example (Python with spaCy):**
    ```python
    import spacy
    
    nlp = spacy.load("en_core_web_sm")
    text = "Apple, founded by Steve Jobs in California, is looking to buy a U.K. startup for $1 billion in 2025."
    doc = nlp(text)
    
    for ent in doc.ents:
        print(f"Entity: {ent.text:<20} | Label: {ent.label_}")
        
    # Output:
    # Entity: Apple                | Label: ORG
    # Entity: Steve Jobs           | Label: PERSON
    # Entity: California           | Label: GPE
    # Entity: U.K.                 | Label: GPE
    # Entity: $1 billion           | Label: MONEY
    # Entity: 2025                 | Label: DATE
    ```

---

### 8. Machine Translation (MT)
* **What is it?** The task of automatically translating text from a source language to a target language. 🌍
* **Why is it done?** To break down language barriers for communication, information access, and global business.
* **More Details:**
    * **Statistical Machine Translation (SMT):** Pre-deep learning approach. It learned statistical models of word and phrase alignments from large parallel corpora (text translated by humans).
    * **Neural Machine Translation (NMT):** The modern standard. It uses deep learning models, typically an **encoder-decoder** architecture (like LSTMs or Transformers), to learn a mapping between languages.
    * NMT models can capture context and produce much more fluent and accurate translations than SMT. Google Translate and DeepL are famous examples.
* **Conceptual Example:**
    * An NMT model reads the entire source sentence ("Je suis étudiant") into a compressed representation (a vector).
    * A second part of the model, the decoder, then uses this representation to generate the target sentence ("I am a student") word by word.

---

### 9. Text Classification
* **What is it?** The task of assigning a piece of text to one or more predefined categories or labels.
* **Why is it done?** To organize and structure text data. Common applications include email spam detection, sentiment analysis, and news article categorization (sports, politics, tech).
* **More Details:**
    * **Classical approach:** Convert text to numerical features using **Bag-of-Words** or **TF-IDF**, then feed these features into a machine learning classifier like Naive Bayes, SVM, or Logistic Regression.
    * **Deep Learning approach:** Use models like CNNs, LSTMs, or Transformers that can learn features directly from the raw text, often achieving higher accuracy.
* **Example (Scikit-learn with TF-IDF and Naive Bayes):**
    ```python
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import make_pipeline
    
    # Sample data
    texts = ["Godzilla is a fun monster movie", "I love romance and drama films", 
             "That was a scary horror movie", "This comedy was hilarious"]
    labels = ["action", "romance", "horror", "comedy"]
    
    # Create a model pipeline
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    
    # Train the model
    model.fit(texts, labels)
    
    # Predict on new text
    prediction = model.predict(["A new scary monster film is coming out"])
    print(prediction) # Output: ['horror']
    ```

---

### 10. Sentiment Analysis
* **What is it?** A type of text classification that focuses on identifying and extracting subjective information, determining if a text is positive, negative, or neutral.
* **Why is it done?** To gauge public opinion, monitor brand reputation, analyze customer feedback, and understand market trends from social media, reviews, etc.
* **More Details:**
    * **Polarity detection:** Classifying text as positive, negative, or neutral. This is the most common form.
    * **Aspect-based sentiment analysis:** A more fine-grained approach that identifies the sentiment towards specific aspects or features (e.g., "The phone's **camera** is *amazing*, but the **battery life** is *terrible*.").
    * Challenges include sarcasm, irony, and context-dependent words (e.g., "unpredictable" could be good for a movie plot but bad for a car's steering).
* **Conceptual Example:**
    * Input: "I absolutely loved the movie! The acting was superb." -> Output: **Positive**
    * Input: "The flight was delayed and the service was awful." -> Output: **Negative**
    * Input: "The package is scheduled for delivery on Tuesday." -> Output: **Neutral**

---

### 11. Topic Modeling
* **What is it?** An unsupervised machine learning technique for discovering abstract "topics" that occur in a collection of documents.
* **Why is it done?** To automatically organize large volumes of text. It can reveal hidden thematic structures in the data without any prior annotation. Useful for browsing a news archive or analyzing scientific papers.
* **More Details:**
    * It's **unsupervised**, meaning it doesn't need labeled data. The algorithm figures out the topics on its own.
    * The most famous algorithm is **Latent Dirichlet Allocation (LDA)**.
    * The output is typically: 1) A list of topics, where each topic is a distribution of words (e.g., Topic A: 30% "gene", 25% "dna", ...). 2) A breakdown for each document, showing its mixture of topics (e.g., Document X: 60% Topic A, 40% Topic B).
    * The topics are not named by the algorithm; a human needs to interpret the word distributions to assign a meaningful label (e.g., "Genetics").
* **Math (Intuition behind LDA):**
    LDA is a generative model. It assumes documents are produced in the following way:
    1.  For each document, decide on a mixture of topics. (e.g., This document will be 60% politics, 40% economics). This mixture is drawn from a Dirichlet distribution, $`\vec{\theta}_d \sim \text{Dir}(\vec{\alpha})`$.
    2.  For each word in that document:
        a. First, pick a topic based on the document's mixture. (e.g., Roll a die, 60% chance it lands on politics). Let's say we pick topic $`z_n`$.
        b. Then, pick a word based on that topic's word distribution. (e.g., The politics topic has a high probability of generating words like "government", "election", etc.). The word $`w_n`$ is chosen from a multinomial distribution defined by the topic, $`\vec{\phi}_{z_n}`$.
    The goal of the LDA algorithm is to work backward: given the documents, what are the topic mixtures ($`\theta`$) and word distributions ($`\phi`$) that were most likely to have generated them?

---

### 12. Plagiarism Detection
* **What is it?** The task of identifying instances of plagiarism or copyright infringement within a work or document.
* **Why is it done?** To ensure academic integrity and protect intellectual property.
* **More Details:**
    * It involves comparing a source document against a large corpus of reference documents.
    * Techniques range from simple **fingerprinting** (hashing n-grams and comparing hashes) to more advanced methods that look for semantiplagiarismc similarity to detect paraphrased plagiarism.
    * This task often combines elements of Information Retrieval (finding potential source documents) and Text Similarity (measuring how similar the passages are).
* **Conceptual Example:**
    1.  A student submits an essay.
    2.  The plagiarism detection software breaks the essay into short phrases (n-grams).
    3.  It searches a massive database (the internet, academic journals) for documents containing those same phrases.
    4.  If a high degree of overlap is found with a source document, it flags the passage for review.

---

### 13. Language Model (LM)
* **What is it?** A probabilistic model that can predict the next word in a sequence given the words that came before it. 🧠
* **Why is it done?** LMs are the core of modern NLP. They provide a way for machines to "understand" the patterns, grammar, and semantics of a language. They are foundational for text generation, machine translation, and speech recognition.
* **More Details:**
    * **N-gram models:** A simple, statistical LM that predicts the next word based on the previous `n-1` words. It calculates probabilities from frequencies in a large text corpus.
    * **Neural Language Models:** Use recurrent neural networks (RNNs, LSTMs) or Transformers to learn complex patterns from text.
    * **Large Language Models (LLMs):** Massive Transformer-based models (like GPT-3, BERT, Gemini) trained on internet-scale data. They are extremely powerful and can perform many NLP tasks with little to no task-specific training ("zero-shot" or "few-shot" learning).
* **Math (N-gram Model Probability):**
    The probability of a sentence $`W = w_1, w_2, ..., w_m`$ is factored using the chain rule of probability:
    $$ P(W) = P(w_1) P(w_2|w_1) P(w_3|w_1, w_2) \dots P(w_m|w_1, \dots, w_{m-1}) $$
    An n-gram model applies a **Markov assumption** that the next word only depends on the previous $`n-1`$ words. For a bigram model ($`n=2`$):
    $$ P(W) \approx \prod_{i=1}^{m} P(w_i | w_{i-1}) $$
    The probability $`P(w_i | w_{i-1})`$ is estimated by counting occurrences in a corpus:
    $$ P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$

---

### 14. Text Summarization
* **What is it?** The process of automatically creating a short, coherent, and fluent summary of a longer text document.
* **Why is it done?** To help users quickly digest large amounts of information, such as news articles, scientific papers, or long emails.
* **More Details:**
    * **Extractive Summarization:** The model selects important sentences or phrases from the original text and stitches them together to form a summary. It's like highlighting the key points. This is an easier approach.
    * **Abstractive Summarization:** The model generates new sentences that capture the essence of the original text, potentially using words and phrases not present in the source. This is much harder but produces more human-like summaries. Modern LLMs excel at this.
* **Conceptual Example:**
    * **Original Text:** A 3-page news article about a new scientific discovery.
    * **Extractive Summary:** A 3-sentence summary composed of the first sentence of the article, a key quote from a scientist, and the concluding sentence.
    * **Abstractive Summary:** A 3-sentence summary written in fresh words that explains the background, the discovery, and its potential impact.

---

### 15. Coreference Resolution
* **What is it?** The task of finding all expressions in a text that refer to the same real-world entity.
* **Why is it done?** It's crucial for true reading comprehension. A machine needs to know that in "Susan arrived late. She said she missed the bus," the words "Susan," "She," and "she" all refer to the same person.
* **More Details:**
    * This includes resolving pronouns ("he", "she", "it"), definite nouns ("the car"), and names/aliases.
    * It's a very challenging task that often requires syntactic, semantic, and world knowledge.
    * It is often modeled as a clustering problem: group all mentions that refer to the same entity into a cluster.
* **Example:**
    * In the text: "**Barack Obama** was the 44th president. **He** was born in Hawaii. Many people admire **the former president**."
    * A coreference resolution system would identify the cluster: {`Barack Obama`, `He`, `the former president`}.

---

### 16. Question Answering (QA)
* **What is it?** A task where a system is designed to automatically answer questions posed by humans in a natural language.
* **Why is it done?** To provide direct, concise answers to user queries, moving beyond the traditional list of blue links from a search engine. Think of smart assistants like Google Assistant or Alexa.
* **More Details:**
    * **Extractive QA:** The system is given a context (e.g., a Wikipedia article) and a question, and its task is to find and extract the span of text from the context that contains the answer.
    * **Generative QA (or Abstractive QA):** The system generates a free-text answer based on the information it has learned or is given. LLMs are very good at this.
    * **Open-domain vs. Closed-domain:** Closed-domain QA answers questions about a specific topic (e.g., a company's internal documents), while open-domain QA aims to answer questions about nearly anything, typically using the entire web as its knowledge source.
* **Conceptual Example (Extractive QA):**
    * **Context:** "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower."
    * **Question:** "Who designed the Eiffel Tower?"
    * **Answer:** "Gustave Eiffel" (extracted directly from the text).

---

### 17. Conversational Agents (Chatbots)
* **What is it?** A computer program designed to simulate human conversation through voice or text. 🤖
* **Why is it done?** For customer service automation, personal assistance (Siri, Alexa), information retrieval, and entertainment.
* **More Details:**
    * **Rule-based chatbots:** Follow a pre-defined script or decision tree. They are very limited and can't handle unexpected user inputs.
    * **Retrieval-based chatbots:** Have a repository of pre-defined responses. They use a model to pick the best response for a given user query, but they can't generate new answers.
    * **Generative chatbots:** Use language models to generate new responses from scratch. This allows for more flexible and human-like conversations. Modern LLMs have made this approach extremely powerful.
    * A sophisticated chatbot combines many NLP tasks: Intent Recognition, NER, Dialogue Management, and Text Generation.

***

### New Terms Explained

#### Hidden Markov Model (HMM)
* **What is it?** A statistical model that assumes a system is a Markov process with unobserved (hidden) states. For POS tagging, the hidden states are the POS tags, and the observations are the words.
* **Why is it done?** It's a powerful tool for modeling sequential data where the underlying state is not directly visible.
* **More Details:**
    * An HMM is defined by two key probabilities:
        1.  **Transition Probability** $`P(tag_i | tag_{i-1})`$: The probability of moving from one hidden state (tag) to another. (e.g., a determiner `DT` is very likely to be followed by a noun `NN`).
        2.  **Emission Probability** $`P(word_i | tag_i)`$: The probability of observing a certain word given a hidden state (tag). (e.g., given the tag `NN`, the word "cat" is more probable than the word "jump").
    * The goal of an HMM-based POS tagger is to find the most likely sequence of hidden tags given the observed sequence of words. This is efficiently solved using the **Viterbi algorithm**.
* **Math (Core Idea):**
    Given a sequence of words $`W = w_1, ..., w_n`$, we want to find the sequence of tags $`T = t_1, ..., t_n`$ that maximizes the posterior probability $`P(T|W)`$. Using Bayes' theorem, this is equivalent to maximizing $`P(W|T)P(T)`$.
    $$ \hat{T} = \underset{T}{\arg\max} \, P(W|T) P(T) $$
    The HMM assumptions simplify this to:
    $$ \hat{T} = \underset{T}{\arg\max} \prod_{i=1}^{n} P(w_i | t_i) \times P(t_i | t_{i-1}) $$
    Where $`P(w_i | t_i)`$ is the emission probability and $`P(t_i | t_{i-1})`$ is the transition probability.

#### Bag-of-Words (BoW)
* **What is it?** A simple way to represent a piece of text as a collection of its words, disregarding grammar and even word order but keeping multiplicity.
* **Why is it done?** To convert unstructured text into a fixed-length numerical vector that machine learning models can understand.
* **Conceptual Example:**
    * Sentence 1: "The cat sat on the mat."
    * Sentence 2: "The dog ate the cat."
    * **Vocabulary:** {The, cat, sat, on, mat, dog, ate}
    * **BoW Vector for Sentence 1:** [2, 1, 1, 1, 1, 0, 0] (The=2, cat=1, sat=1, ...)
    * **BoW Vector for Sentence 2:** [2, 1, 0, 0, 0, 1, 1] (The=2, cat=1, dog=1, ...)

#### Term Frequency-Inverse Document Frequency (TF-IDF)
* **What is it?** A numerical statistic that reflects how important a word is to a document in a collection or corpus.
* **Why is it done?** It improves upon Bag-of-Words by down-weighting common words (like "the", "a") that appear in many documents and are less informative, while giving more weight to words that are frequent in a document but rare across the corpus.
* **Math:**
    The TF-IDF score for a term $`t`$ in a document $`d`$ from a corpus $`D`$ is:
    $$ \text{tfidf}(t, d, D) = \text{tf}(t, d) \times \text{idf}(t, D) $$
    * **Term Frequency (tf):** How often the term appears in the document.
        $$ \text{tf}(t, d) = \frac{\text{count of } t \text{ in } d}{\text{number of words in } d} $$
    * **Inverse Document Frequency (idf):** A measure of how rare the term is across the whole corpus. The logarithm is used to dampen the effect of very rare words.
        $$ \text{idf}(t, D) = \log \frac{|D|}{|\{d \in D : t \in d\}|} $$
        where $|D|$ is the total number of documents.

#### N-grams
* **What is it?** A contiguous sequence of $`n`$ items (words, characters) from a given sample of text.
* **Why is it done?** They capture some local word order information that Bag-of-Words discards. This is useful for language modeling and text classification.
* **Example:** For the sentence "The quick brown fox jumps."
    * **Unigrams (1-grams):** "The", "quick", "brown", "fox", "jumps"
    * **Bigrams (2-grams):** "The quick", "quick brown", "brown fox", "fox jumps"
    * **Trigrams (3-grams):** "The quick brown", "quick brown fox", "brown fox jumps"

***

## Questions

### **1. What makes NLP, which deals with text understanding, different from other domains of ML?**

* **Short Answer:** NLP deals with unstructured, sequential, and highly ambiguous data, whereas many other ML domains (like image or tabular data) work with structured numerical inputs.

* **Long Answer:**
    1.  **Unstructured Nature:** Text data doesn't come in neat rows and columns. It's free-form, requiring significant pre-processing (tokenization, vectorization) to be usable by ML models.
    2.  **Ambiguity:** Language is inherently ambiguous at multiple levels.
        * **Lexical Ambiguity:** A word can have multiple meanings (e.g., "bank").
        * **Syntactic Ambiguity:** A sentence can be parsed in multiple ways (e.g., "I saw a man on a hill with a telescope." - Who has the telescope?).
    3.  **Sequential and Contextual:** The order of words matters immensely. "The dog bit the man" is very different from "The man bit the dog". Models must be able to capture these sequential dependencies.
    4.  **High Dimensionality:** The vocabulary of a language can be huge (hundreds of thousands of words), leading to very high-dimensional feature spaces (the "curse of dimensionality").

### **2. Find at least 5 more NLP tasks that are not listed above.**

* **Short Answer:** Automatic Speech Recognition, Text-to-Speech Synthesis, Information Retrieval, Spell Checking, and Grammar Correction.

* **Long Answer:**
    1.  **Automatic Speech Recognition (ASR):** Converting spoken language into text. This is what powers voice assistants like Siri and dictation software.
    2.  **Text-to-Speech (TTS) Synthesis:** Converting written text into spoken language.
    3.  **Information Retrieval (IR):** The task of finding documents relevant to a user's query from a large collection. Search engines are the most prominent example.
    4.  **Spell Checking:** Identifying and correcting spelling errors in a text.
    5.  **Grammar Correction:** Identifying and correcting grammatical errors, going beyond simple spelling mistakes.

### **3. How did we solve NLP problems before the deep learning era? What are the pros and cons?**

* **Short Answer:** We used rule-based systems and classical statistical machine learning models that relied heavily on manual feature engineering.

* **Long Answer:**
    Before deep learning, the dominant paradigms were:
    1.  **Rule-Based Systems:** Hand-crafted rules written by linguists or domain experts. For example, a simple sentiment analyzer might have a list of positive and negative words and count them.
    2.  **Statistical Machine Learning:** Models like Naive Bayes, Support Vector Machines (SVMs), and Logistic Regression were used. The key challenge was **feature engineering**. We had to manually design features to represent the text, such as:
        * Bag-of-Words (BoW) counts
        * TF-IDF scores
        * N-gram counts
        * POS tag counts
        * Syntactic features from parse trees

    * **Pros:**
        * **More Interpretable:** It was easier to understand why a model made a particular decision by looking at the feature weights.
        * **Less Data Hungry:** These models could often achieve reasonable performance with smaller datasets compared to deep learning models.
        * **Computationally Cheaper:** Training was generally faster and required less specialized hardware.

    * **Cons:**
        * **Brittle and Laborious:** Manual feature engineering was time-consuming, required deep domain expertise, and didn't generalize well to new domains.
        * **Inability to Capture Semantics:** Features like BoW or TF-IDF lose word order and struggle to capture the underlying meaning or semantic similarity (e.g., they don't know that "king" and "queen" are related).

### **4. Are there unsupervised NLP tasks?**

* **Short Answer:** Yes, absolutely.

* **Long Answer:**
    Many important NLP tasks are unsupervised, meaning they find patterns in data without relying on pre-labeled examples.
    * **Topic Modeling (e.g., LDA):** As described above, it discovers abstract topics from a collection of documents.
    * **Word Embeddings (e.g., Word2Vec, GloVe):** These algorithms learn dense vector representations of words from raw text. The key idea is that words appearing in similar contexts have similar meanings. These embeddings are a cornerstone of modern NLP.
    * **Text Clustering:** Grouping similar documents together based on their content, without any predefined categories.
    * **Language Modeling:** In its purest form, training a language model is unsupervised—it just learns to predict the next word from a massive, unlabeled text corpus.

### **5. Analyzing text is one thing, generating text is another. Which NLP tasks fall under which category?**

* **Short Answer:** Analysis tasks understand and classify text; generation tasks create new text.

* **Long Answer:**
    * **Analysis (or NLU - Natural Language Understanding):** These tasks focus on extracting meaning, structure, or information from text.
        * Text Classification
        * Sentiment Analysis
        * Named Entity Recognition (NER)
        * Part-of-Speech Tagging
        * Syntax Parsing
        * Coreference Resolution
        * Plagiarism Detection

    * **Generation (or NLG - Natural Language Generation):** These tasks focus on producing human-like text.
        * Machine Translation
        * Text Summarization (especially abstractive)
        * Language Modeling
        * Conversational Agents (Chatbots)
        * Text-to-Speech

    * **Mixed Tasks:** Some tasks sit in the middle, requiring both understanding and generation.
        * **Question Answering:** Understands a question and context, then either extracts or generates an answer.

### **6. List some key differences between Named Entity Recognition and Named Entity Resolution - both in problem statement and in how they may be solved.**

* **Short Answer:** NER finds and classifies mentions (e.g., "Apple" is an ORG), while Resolution links that mention to a unique entity in a knowledge base (e.g., Apple Inc., not the fruit).

* **Long Answer:**

| Feature         | **Named Entity Recognition (NER)** | **Named Entity Resolution (NERes) / Entity Linking** |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Problem** | Identify spans of text that are named entities and classify them into predefined categories (PERSON, ORG, LOC).                  | Link an entity mention in text to its corresponding unique entry in a knowledge base (like Wikipedia or a corporate database).                            |
| **Input** | A sentence or document.                                                                                                      | A sentence with an identified entity mention, and a knowledge base (KB) of unique entities.                                                                 |
| **Output** | The original text with annotated entity spans and their types. `[Apple (ORG)] is a company.`                                   | A unique identifier from the KB. `[Apple]` -> `KB_ID:Q312` (the ID for Apple Inc.).                                                                           |
| **Challenge** | Boundary detection (is it "Steve" or "Steve Jobs"?) and classification.                                                        | **Disambiguation**. "Apple" could be the tech company or the fruit. "Paris" could be Paris, France or Paris, Texas.                                          |
| **How to Solve**| Typically a **sequence labeling** problem. Solved with models like Conditional Random Fields (CRFs), BiLSTMs, and Transformers (BERT). | Often a **ranking or similarity** problem. Compare the context of the mention in the text to the description of candidate entities in the KB to find the best match. |

### **7. Which is better, stemming or lemmatization?**

* **Short Answer:** It depends on the application. Lemmatization is more accurate, while stemming is faster.

* **Long Answer:**
    There's no single "better" one; it's a trade-off.
    * **Choose Lemmatization when:**
        * **Accuracy is paramount.**
        * The application needs to understand the meaning of words.
        * Examples: Question Answering systems, Chatbots, Machine Translation.
        * You need the output to be actual dictionary words.
    * **Choose Stemming when:**
        * **Speed and performance are critical.**
        * The application is focused on information retrieval and doesn't need deep semantic understanding.
        * Examples: Search engines, indexing large document corpora.
        * Slight inaccuracies (like "studi" instead of "study") don't harm the overall goal.

    **Analogy:** Stemming is like using a blunt axe to chop wood—it's fast but messy. Lemmatization is like using a scalpel—it's precise and careful, but much slower.

### **8. A big challenge in some NLP tasks is that there may be many different correct outputs for the same input. Identify the NLP tasks where that would be a problem, and find how is that reflected in different common metrics constructed for these tasks.**

* **Short Answer:** This is a major issue in generative tasks like Machine Translation and Summarization. Metrics like BLEU and ROUGE were invented to handle it.

* **Long Answer:**
    * **Tasks with this problem:**
        * **Machine Translation:** There are many valid ways to translate a sentence. "Je suis étudiant" can be "I am a student," "I'm a student," or "I am a pupil," all of which are correct.
        * **Text Summarization:** Different people will write different, yet equally valid, summaries of the same article.
        * **Dialogue Systems / Chatbots:** There is no single "correct" response to "How are you?".

    * **How Metrics Reflect This:**
        Standard metrics like accuracy are useless here. You can't just check for an exact match. Instead, we use metrics that compare the model-generated output against one or more human-written reference outputs.
        * **BLEU (Bilingual Evaluation Understudy):** Primarily used for Machine Translation. It measures the overlap of **n-grams** (unigrams, bigrams, etc.) between the generated text and the reference translations. It rewards outputs that use the same words and phrases as the references, but it doesn't require an exact match. It also has a brevity penalty to punish translations that are too short.
        * **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Primarily used for Summarization. It's similar to BLEU but is recall-oriented. It checks how many of the n-grams from the human reference summaries appear in the model-generated summary.

### **9. Which classical ML models can be used for NLP problems? Can any of them take into account the order of words?**

* **Short Answer:** Naive Bayes, Logistic Regression, and Support Vector Machines (SVMs) are commonly used. They cannot inherently account for word order, but we can help them by using n-grams as features.

* **Long Answer:**
    * **Common Classical Models:**
        1.  **Naive Bayes:** A probabilistic classifier based on Bayes' theorem with a "naive" assumption of feature independence. It's simple, fast, and works surprisingly well for tasks like spam detection and document classification.
        2.  **Logistic Regression:** A linear model that predicts the probability of a class. It's a very strong baseline for many text classification tasks.
        3.  **Support Vector Machines (SVMs):** A powerful model that finds the optimal hyperplane to separate data points into different classes. It works very well in high-dimensional spaces, which is perfect for text data represented by TF-IDF.

    * **Handling Word Order:**
        These models see input as a flat vector of feature values (e.g., TF-IDF scores). They have no built-in mechanism to understand that "quick brown fox" is a sequence.
        The standard trick to incorporate *local* word order is to add **n-grams** to the feature set. Instead of just using individual words (unigrams), you also treat pairs of words (bigrams) and triplets of words (trigrams) as features.
        * For example, when classifying movie reviews, the feature "not good" (a bigram) is much more informative for a negative sentiment than the individual features "not" and "good".
        * However, this is still a workaround. These models don't handle long-range dependencies the way modern recurrent or attention-based models do.

### **10. Everyone totally gets sarcasm, so... Like... Why would detecting it be any sort of a "challenge" for a genius computer?**

* **Short Answer:** Sarcasm often involves saying the opposite of what you mean, and detecting it requires deep contextual understanding, world knowledge, and sometimes even tone of voice—all things computers struggle with.

* **Long Answer:**
    Detecting sarcasm is an "AI-complete" problem, meaning it's as hard as solving general artificial intelligence. Here's why:
    1.  **Contradiction with Context:** Sarcasm relies on a mismatch between the literal meaning of words and the context.
        * *Example:* "I love being stuck in traffic for two hours." The positive sentiment of "love" is completely inverted by the universally negative context of a traffic jam. A computer needs world knowledge to know that traffic jams are bad.
    2.  **Pragmatic and World Knowledge:** It requires understanding social norms and what is expected in a situation.
        * *Example:* After dropping a plate, someone says, "Great job." The machine needs to know that breaking things is not a "great job".
    3.  **Lack of Explicit Markers:** Unlike other sentiment, there are often no specific words that signal sarcasm. It's about the combination and the situation.
    4.  **Dependence on Tone (in Speech):** In spoken language, prosody (tone, pitch, volume) is a huge indicator of sarcasm. This is completely lost in written text.
    5.  **Subtlety and Nuance:** Sarcasm exists on a spectrum from obvious to incredibly subtle. It often relies on a shared understanding between the speaker and the listener that a machine does not have.

***

## Exercises

Here are some ideas to get your hands dirty with a real NLP tool. We'll use **spaCy**, a modern and powerful library.

**Goal:** Find an open-source NLP tool that can provide (and preferably visualize) syntax trees, POS tags, and dependency trees.

**Proposed Tool:** **spaCy** with its built-in `displaCy` visualizer.

**Steps to Play Around:**

1.  **Installation:** First, install spaCy and download its small English model.
    ```bash
    pip install spacy
    python -m spacy download en_core_web_sm
    ```

2.  **Basic Script:** Create a Python script and use this code to analyze and visualize a sentence. If you're running this in a Jupyter Notebook or Google Colab, the visualization will appear directly in your output.
    ```python
    import spacy
    from spacy import displacy
    
    # Load the model
    nlp = spacy.load("en_core_web_sm")
    
    # === SENTENCES TO TRY ===
    # 1. Simple sentence
    # text = "The quick brown fox jumps over the lazy dog."
    
    # 2. More complex sentence with a clause
    # text = "Although he was tired, the student finished his homework."
    
    # 3. A question
    # text = "Who built the great pyramids in Egypt?"
    
    # 4. Sentence with named entities
    text = "Apple and Google are competing for the future of AI."
    
    # Process the text
    doc = nlp(text)
    
    # --- Part 1: Print POS and Dependencies ---
    print("--- Tokens, POS Tags, and Dependencies ---")
    for token in doc:
        print(f"{token.text:<15} {token.lemma_:<15} {token.pos_:<10} {token.dep_:<10}")
    
    # --- Part 2: Visualize the Dependency Tree ---
    # To run this from a script, displacy.serve is needed.
    # In a Jupyter notebook, just calling displacy.render is enough.
    print("\n--- Visualizing Dependency Parse ---")
    # displacy.serve(doc, style="dep")
    
    # For Jupyter/Colab:
    displacy.render(doc, style="dep", jupyter=True)
    
    # --- Part 3: Visualize Named Entities ---
    print("\n--- Visualizing Named Entities ---")
    displacy.render(doc, style="ent", jupyter=True)
    ```


**How to Interpret the Results:**

* **POS Tags:** Look at the `token.pos_` output. You'll see `PROPN` (proper noun), `VERB`, `ADP` (adposition, like 'for'), `DET` (determiner, like 'the'). Do they make sense? Try changing a word (e.g., "competing" to "competition") and see how the POS tag changes.
* **Dependencies:** The visualization is key here. Arrows point from a "head" word to a "dependent" word.
    * Find the main verb of the sentence. It will often be the `ROOT`.
    * Look for the `nsubj` (nominal subject) arrow pointing from the verb to the subject (e.g., from `competing` to `Apple` and `Google`). This tells you *who* is doing the action.
    * Look for `dobj` (direct object) or `pobj` (object of a preposition) to see *what* the action is being done to. In the example, `future` is the `pobj` of the preposition `for`.

By playing with different sentences, you'll start to build an intuition for how machines deconstruct language into a structured, grammatical format. Have fun exploring! 🚀