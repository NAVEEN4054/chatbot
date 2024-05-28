
print("Meet Quantum: your virtual alexa")

#import necessary libraries
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only


#Reading in the corpus
with open('C:/Users/tikan/Desktop/SLASHMARK/chatbot/corpus.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","hi there", "how are you", "is anyone there?","hey","hola", "hello", "good day")
GREETING_RESPONSES = ["Hi", "Hey", "*nods*", "Hi there!", "Hello", "I am glad! You are talking to me","Hello", "Good to see you again", "Hi there, how can I help?"]
GREETING_INPUTS1 = ("thanks", "thank you", "that's helpful", "awesome","thanks", "thanks for helping me")
GREETING_RESPONSES1 = ["My pleasure", "You're Welcome"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    sentence_lower = sentence.lower()
    
    for phrase in GREETING_INPUTS:
        if phrase in sentence_lower:
            return random.choice(GREETING_RESPONSES)
    
    for phrase in GREETING_INPUTS1:
        if phrase in sentence_lower:
            return random.choice(GREETING_RESPONSES1)


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("QUANTUM: My name is QUANTUM. I will answer your queries based on my recent updated knowlwdge. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
            if(greeting(user_response)!=None):
                print("QUANTUM: "+greeting(user_response))
            else:
                print("QUANTUM: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("QUANTUM: Bye! take care..")    
        
        

