print("Meet Quantum: your virtual assistant")

# Import necessary libraries
import io
import random
import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import wikipedia
warnings.filterwarnings('ignore')
import numpy as np
import sympy as sp
import re

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('popular', quiet=True)  # for downloading packages

# uncomment the following only the first time
# nltk.download('punkt')  # first-time use only
# nltk.download('wordnet')  # first-time use only
#nltk.download('stopwords')
# Reading in the corpus
with open('C:/Users/tikan/Desktop/SLASHMARK/chatbot-1/corpus.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# Tokenisation
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "hi there", "how are you", "is anyone there?", "hola", "good day")
GREETING_RESPONSES = ["Hi", "Hey", "*nods*", "Hi there!", "Hello", "I am glad! You are talking to me", "Good to see you again", "Hi there, how can I help?"]
THANKS_INPUTS = ("thanks", "thank you", "that's helpful", "awesome", "thanks for helping me")
THANKS_RESPONSES = ["My pleasure", "You're welcome", "Glad to help!", "Anytime!", "Happy to assist!"]
FAREWELL_INPUTS = ("bye", "goodbye", "see you later", "take care", "bye bye")
FAREWELL_RESPONSES = ["Bye! Take care..", "Goodbye! Have a nice day!", "See you later!", "Take care!"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    sentence_lower=sentence.lower()
    for phrase in GREETING_INPUTS:
        if phrase in sentence_lower:
            return random.choice(GREETING_RESPONSES)
    return None

def thanks(sentence):
    """If user's input is a thanks, return a thanks response"""
    sentence_lower = sentence.lower()
    for phrase in THANKS_INPUTS:
        if phrase in sentence_lower:
            return random.choice(THANKS_RESPONSES)
    return None


def farewell(sentence):
    """If user's input is a farewell, return a farewell response"""
    sentence_lower=sentence.lower()
    for phrase in FAREWELL_INPUTS,:
        if phrase in sentence_lower:
            return random.choice(FAREWELL_RESPONSES)
    return None
def is_math_query(query):
    # Simple heuristic to check if the query is a mathematical problem
    return bool(re.search(r'[\d\+\-\*/\^\=\(\)]+', query))

def solve_math_query(query):
    try:
        # Remove any non-mathematical characters
        query = re.sub(r'[^0-9\+\-\*/\^\=\(\)\s]', '', query)
        # Parse and solve the equation
        lhs, rhs = query.split('=')
        equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        solution = sp.solve(equation)
        return f"The solution is: {solution}"
    except Exception as e:
        return f"Sorry, I couldn't solve the mathematical query. Error: {str(e)}"


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf != 0:
        robo_response = robo_response + sent_tokens[idx]
    else:
        try:
            robo_response = wikipedia.summary(user_response, sentences=3)
        except wikipedia.exceptions.DisambiguationError as e:
            robo_response = "There are multiple results for this query. Please be more specific."
        except wikipedia.exceptions.PageError:
            robo_response = "Sorry, I couldn't find any information on that topic."  
    sent_tokens.pop()
    return robo_response

# Chatbot main loop
flag = True
print("QUANTUM: My name is QUANTUM. I will answer your queries based on my recent updated knowledge. If you want to exit, type Bye!")
while flag:
    user_response = input().lower()
    if user_response not in FAREWELL_INPUTS:
        if greeting(user_response):
            print("QUANTUM: " + greeting(user_response))
        elif thanks(user_response):
            print("QUANTUM: " + thanks(user_response))
        else:
            print("QUANTUM: ", end="")
            print(response(user_response))
    else:
        print("QUANTUM: " + farewell(user_response))
        flag = False
