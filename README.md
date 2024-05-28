# Quantum: Corpus based chatbot

Welcome to Quantum, your friendly virtual assistant!

This repository houses a versatile chatbot project capable of handling a wide array of topics. The chatbot is powered by natural language processing (NLP) algorithms and artificial intelligence (AI) techniques, making it adept at engaging conversations and providing informative responses.Quantum can handle a variety of tasks including greeting you, solving mathematical problems, and providing information on various topics.

## Features

- **Greetings:** Quantum can recognize and respond to various greetings.
- **Thank You Responses:** Quantum acknowledges and responds to expressions of gratitude.
- **Farewell Responses:** Quantum can recognize and respond to farewells.
- **Math Problem Solver:** Quantum can solve simple arithmetic and algebraic equations.
- **Information Retrieval:** Quantum can provide information on a wide range of topics using Wikipedia.
- **Contextual Responses:** Quantum uses a predefined corpus to generate relevant responses based on input.

## Installation

To set up Quantum, you'll need to install several Python libraries. You can install them using pip:

```bash
pip install requirements
```

The requirements may include folllowing:

```plaintext
nltk
scipy
scikit-learn
wikipedia
sympy
```

## Downloading NLTK Data

Quantum uses NLTK for natural language processing. Download the necessary NLTK data by running the following in a Python script or interpreter:

```python
import nltk
nltk.download('popular', quiet=True)  # for downloading popular NLTK packages
# Uncomment the following lines if running for the first time
# nltk.download('punkt')  # first-time use only
# nltk.download('wordnet')  # first-time use only
# nltk.download('stopwords')
```

## Preparing the Corpus

Quantum needs a text corpus to generate responses. Save your corpus as corpus.txt in the same directory as your script. Here is an example of how to read the corpus:

```python

with open('corpus.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()
```

## Running Quantum

1. Ensure that `chatbot.py` and `corpus.txt` in the same directory.
2. open terminal or command prompt.
3. Run the following prompt:

   ```bash
   python chatbot.py
   ```

4. Follow the command line instructions to get desired results.

Once Quantum is running, you can interact with it by typing your queries. Here are some examples:

## Examples

### Greetings

- User: "Hello"
- Quantum: "Hi there!"

### Math Queries

- User: "What is 5 + 3?"
- Quantum: "The result is: 8"

- User: "Solve 2x + 3 = 7"
- Quantum: "The solution is: [2]"

### Information Queries

- User: "Tell me about Python programming."
- Quantum: "Python is a widely used programming language"
