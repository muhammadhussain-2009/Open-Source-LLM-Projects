# RAG Evaluations - Evaluation Metrics Documentation

## Overview
This project provides a comprehensive evaluation framework for Retrieval-Augmented Generation (RAG) systems using multiple evaluation metrics to assess the quality, fairness, and fluency of generated text.

## Evaluation Metrics

### 1. BLEU (Bilingual Evaluation Understudy)
- **Purpose**: Measures the similarity between generated text and reference text based on n-gram overlap
- **Range**: 0 to 1 (higher is better)
- **Use Case**: Evaluating machine translation and text generation tasks
- **How it works**: Compares n-grams (1-grams, 2-grams, etc.) in the candidate text with those in reference translations
- **Interpretation**: 
  - 0.0-0.2: Poor translation
  - 0.2-0.4: Fair translation
  - 0.4-0.6: Good translation
  - 0.6-0.8: Very good translation
  - 0.8-1.0: Excellent translation

### 2. ROUGE-1 (Recall-Oriented Understudy for Gisting Evaluation)
- **Purpose**: Evaluates the quality of generated text by measuring unigram (single word) overlap with reference text
- **Range**: 0 to 1 (higher is better)
- **Use Case**: Text summarization and abstractive text generation evaluation
- **How it works**: Calculates recall of unigrams in the generated text compared to reference text
- **Variants**:
  - ROUGE-1: Unigram overlap
  - ROUGE-2: Bigram overlap
  - ROUGE-L: Longest common subsequence

### 3. BERTScore
- **Purpose**: Uses contextual embeddings from BERT to evaluate semantic similarity between generated and reference text
- **Components**:
  - **Precision (P)**: Percentage of generated tokens that are similar to reference tokens
  - **Recall (R)**: Percentage of reference tokens that are similar to generated tokens
  - **F1 Score**: Harmonic mean of precision and recall
- **Range**: 0 to 1 (higher is better)
- **Advantages**: Captures semantic meaning better than n-gram based metrics
- **Use Case**: More nuanced evaluation of text quality and semantic correctness

### 4. Perplexity
- **Purpose**: Measures how well a language model (GPT-2) predicts the generated text
- **Range**: 1 to ∞ (lower is better)
- **Interpretation**:
  - Lower perplexity: Better fluency and coherence
  - Higher perplexity: Text is less predictable/coherent
- **How it works**: Calculates the average negative log probability of the text
- **Use Case**: Evaluating text fluency and language naturalness

### 5. Diversity
- **Purpose**: Measures the variety and uniqueness of generated text to avoid repetition
- **Metric Used**: Unique bigram ratio
- **Range**: 0 to 1 (higher is better)
- **How it works**: Counts unique bigrams in the generated text divided by total number of tokens
- **Interpretation**:
  - High diversity: Text contains varied and diverse vocabulary
  - Low diversity: Text is repetitive

### 6. Racial Bias Detection
- **Purpose**: Detects and quantifies the presence of hate speech, offensive language, and bias in generated text
- **Model Used**: DehateRBERT (Hate-speech-CNERG/dehatebert-mono-english)
- **Categories Detected**:
  - Hate speech
  - Offensive content
  - Neutral/Safe content
- **Use Case**: Ensuring fairness and preventing biased or harmful outputs in RAG systems

## Installation

### Using pip
```bash
pip install -r requirements.txt
```

### Using poetry
```bash
poetry install
```

### Project Structure
```sh
Rag Evaluations/
├── evaluator/
│   ├── __init__.py
│   ├── evaluator.py          # Main RAGEvaluator class
│   └── test_evaluator.py     # Unit tests
├── frontend/
│   ├── app.py               # Streamlit dashboard
│   ├── evaluation_module.py # Evaluation functions
│   └── requirements.txt
├── pyproject.toml
├── setup.py
└── README.md
```
