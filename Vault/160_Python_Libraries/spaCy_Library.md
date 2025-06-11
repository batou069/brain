---
tags:
  - python
  - library
  - spacy
  - natural_language_processing
  - nlp
  - text_processing
  - machine_learning
  - concept
  - example
aliases:
  - spaCy NLP
related:
  - "[[_Python_Libraries_MOC]]"
  - "[[NLTK_Library]]"
  - "[[Transformers_Library]]"
  - "[[Text_Preprocessing_NLP]]"
worksheet:
  - WS_NLP_Libraries_1
date_created: 2025-06-09
---
# spaCy Library

## Overview
**spaCy** is an open-source library for advanced Natural Language Processing (NLP) in Python. It is designed with a focus on **performance, ease of use, and providing production-ready NLP capabilities**. spaCy comes with pre-trained statistical models and word vectors for many languages, enabling users to quickly perform common NLP tasks with high accuracy.

Unlike [[NLTK_Library|NLTK]], which is often seen as a research and educational toolkit with a wide array of algorithms, spaCy is more opinionated and aims to provide the best or most efficient implementation for common tasks.

## Key Features and Philosophy
[list2tab|#spaCy Features]
- Production-Ready & Performant
    -   Written in Cython, making it very fast.
    -   Designed for building real-world applications.
- Pre-trained Statistical Models
    -   Offers downloadable models for various languages (e.g., `en_core_web_sm`, `en_core_web_md`, `en_core_web_lg` for English with increasing size/accuracy).
    -   These models provide capabilities for tokenization, part-of-speech (POS) tagging, named entity recognition (NER), dependency parsing, text classification, and word vectors out-of-the-box.
- Linguistic Features as Objects
    -   Processes text and returns `Doc` objects, which are containers for sequences of `Token` objects.
    -   `Token` objects have rich linguistic annotations (e.g., `.text`, `.lemma_`, `.pos_`, `.tag_`, `.dep_`, `.head`, `.ent_type_`, `.is_stop`).
- Non-Destructive Tokenization
    -   Tokenization in spaCy is non-destructive, meaning the original string can always be reconstructed from the tokenized `Doc`.
- Word Vectors and Similarity
    -   Medium and large models include word vectors (embeddings) allowing for semantic similarity comparisons between words, phrases, and documents.
    -   `.similarity()` method on `Doc`, `Span`, and `Token` objects.
- Named Entity Recognition (NER)
    -   Efficient and accurate NER for identifying entities like persons, organizations, locations, dates, etc.
    -   Access entities via `doc.ents`.
- Dependency Parsing
    -   Analyzes the grammatical structure of a sentence by identifying relationships between words (head words and dependents).
- Text Classification
    -   Includes components for training and using text classification models.
- Customizable Pipelines
    -   NLP tasks are processed as a pipeline (e.g., tokenizer -> tagger -> parser -> NER). Users can customize this pipeline, add custom components, or disable unneeded ones for efficiency.
- Integration with Deep Learning Frameworks
    -   Can integrate with frameworks like PyTorch and TensorFlow for training custom models or using transformer-based components (e.g., via `spacy-transformers` package).

## Example Usage (Analyzing Product Reviews)

First, install spaCy and download a model (e.g., small English model):
```bash
# pip install spacy
# python -m spacy download en_core_web_sm
```

```python
import spacy

# Load the English model
# For more features like word vectors, use 'en_core_web_md' or 'en_core_web_lg'
# nlp = spacy.load('en_core_web_sm') # This line would be active in a script

# Sample product review text
review_text = "This ACME Anvil is an amazing e-commerce product! The build quality is excellent, and it arrived in New York very quickly from their California warehouse. John Doe signed for it."

# Process the text with the spaCy pipeline
# doc = nlp(review_text) # This line would be active

# print(f"--- Review Text ---\n{review_text}\n")

# 1. Tokenization (Accessing tokens)
# print("--- Tokens ---")
# for token in doc:
#     print(f"{token.text:<15} | Lemma: {token.lemma_:<15} | POS: {token.pos_:<10} | Tag: {token.tag_:<8} | Is Stopword: {token.is_stop}")

# 2. Sentence Segmentation (spaCy does this automatically)
# print("\n--- Sentences ---")
# for sent in doc.sents:
#     print(sent.text)

# 3. Named Entity Recognition (NER)
# print("\n--- Named Entities ---")
# if doc.ents:
#     for ent in doc.ents:
#         print(f"Entity: {ent.text:<25} | Label: {ent.label_:<15} ({spacy.explain(ent.label_)})")
# else:
#     print("No named entities found by this model.")

# 4. Noun Chunks (Base noun phrases)
# print("\n--- Noun Chunks ---")
# for chunk in doc.noun_chunks:
#     print(f"Chunk: {chunk.text:<25} | Root Text: {chunk.root.text:<15} | Root Dep: {chunk.root.dep_}")

# 5. Word Vectors & Similarity (Requires medium/large model like 'en_core_web_md')
# Example (conceptual, assuming 'en_core_web_md' or 'lg' is loaded):
# nlp_md = spacy.load('en_core_web_md') # Or _lg
# doc1 = nlp_md("apple")
# doc2 = nlp_md("orange")
# doc3 = nlp_md("car")
# print(f"\n--- Similarity (requires md/lg model) ---")
# print(f"Similarity(apple, orange): {doc1.similarity(doc2):.3f}")
# print(f"Similarity(apple, car): {doc1.similarity(doc3):.3f}")

# Placeholder if spaCy or model isn't fully set up for execution in this environment
if 'nlp' not in locals(): # Check if nlp object was created (it's commented out above)
    print("spaCy 'nlp' object not loaded. Examples are conceptual.")
    print("\n--- Tokens (Example Output Structure) ---")
    print("This            | Lemma: this            | POS: DET        | Tag: DT       | Is Stopword: True")
    print("ACME            | Lemma: ACME            | POS: PROPN      | Tag: NNP      | Is Stopword: False")
    print("Anvil           | Lemma: Anvil           | POS: PROPN      | Tag: NNP      | Is Stopword: False")
    print("is              | Lemma: be              | POS: AUX        | Tag: VBZ      | Is Stopword: True")
    print("... (and so on)")
    print("\n--- Named Entities (Example Output Structure) ---")
    print("Entity: ACME Anvil                | Label: PRODUCT         (Products, services, and brands)")
    print("Entity: New York                  | Label: GPE             (Countries, cities, states)")
    print("Entity: California                | Label: GPE             (Countries, cities, states)")
    print("Entity: John Doe                  | Label: PERSON          (People, including fictional)")

```

## Notable Use Cases & "Cool Stuff"
-   **Fast and Efficient Preprocessing:** Quickly tokenize, tag, parse, and find entities in large volumes of text for downstream ML tasks.
-   **Information Extraction:** Extracting structured information from unstructured text, such as identifying product names, brands, prices, locations, or customer names from reviews or support tickets.
-   **Building Chatbots and Virtual Assistants:** Understanding user queries by parsing intent and extracting entities.
-   **Semantic Similarity for Recommendation/Search:** Using word/document vectors from spaCy models to find similar product descriptions, articles, or customer queries.
-   **Text Summarization (Extractive):** Identifying key sentences based on dependency parsing or entity density.
-   **Rule-Based Matching (`Matcher`, `PhraseMatcher`):** Efficiently find sequences of tokens based on patterns (e.g., specific product mentions, sequences of POS tags).
    ```python
    # from spacy.matcher import Matcher
    # nlp = spacy.load('en_core_web_sm') # Assuming nlp is loaded
    # matcher = Matcher(nlp.vocab)
    # pattern = [{"LOWER": "iphone"}, {"IS_DIGIT": True, "OP": "?"}, {"LOWER": "pro", "OP": "?"}] # Matches "iphone", "iphone 15", "iphone pro", "iphone 15 pro"
    # matcher.add("IPHONE_PATTERN", [pattern])
    # doc = nlp("I want to buy an iphone 15 pro max.")
    # matches = matcher(doc)
    # for match_id, start, end in matches:
    #     print("Matched span:", doc[start:end].text)
    ```
-   **Customizable Components:** Easily create and add custom pipeline components for specialized tasks (e.g., custom entity linkers, sentiment analyzers).

## Advantages
-   **Speed and Efficiency:** One of the fastest NLP libraries available.
-   **Accuracy:** Pre-trained models offer good accuracy on many common NLP tasks.
-   **Ease of Use:** Well-designed API, easy to get started with common tasks.
-   **Production-Oriented:** Suitable for building robust, scalable NLP applications.
-   **Integrated Pipeline:** Processes text through a series of components, providing rich annotations.

## Limitations
-   **Opinionated:** Provides one (often very good) way to do things, which might be less flexible than NLTK for researchers wanting to experiment with many different algorithms for the same task.
-   **Model Size:** Larger models (medium, large, transformer-based) can be substantial in size, which might be a consideration for deployment in resource-constrained environments.
-   **Learning Curve for Customization:** While easy for standard tasks, deep customization of models or training new model types from scratch can have a steeper learning curve.

spaCy is an excellent choice for developers and data scientists who need to build applications that process and understand text efficiently and accurately, especially when leveraging pre-trained models.

---