import streamlit as st
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# API configuration
API_KEY = "AIzaSyARJaqV15qwi1R8jEQTvl7npaby8LVGalY"
CSE_ID = "83be00107795e467f"

# Lemmatizer
lemmer = WordNetLemmatizer()

# Stop words removal
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# Preprocessing functions
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Read the text file
with open('chatbot.txt', 'r', errors='ignore') as f:
    raw = f.read()

# Convert to lowercase
raw = raw.lower()

# Tokenize the text
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Greeting inputs and responses
GREETING_INPUTS = ("hello", "hi")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

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
    if req_tfidf == 0:
        robo_response = "I am sorry! I don't understand you"
    else:
        robo_response = sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

def search_web(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CSE_ID}"
    data = requests.get(url).json()
    results = data.get('items', [])
    return results

# Streamlit UI
st.title("Interactive Chatbot with Web Search Integration")
st.write("This chatbot uses NLP techniques and web search to respond to your queries.")

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

user_input = st.text_input("You: ", "")
if user_input:
    if user_input.lower() in ['bye', 'exit', 'quit']:
        st.session_state.conversation.append(f"You: {user_input}")
        st.session_state.conversation.append("Chatbot: Bye! Take care.")
    else:
        st.session_state.conversation.append(f"You: {user_input}")
        if greeting(user_input) is not None:
            response_text = greeting(user_input)
        else:
            response_text = response(user_input)
            if response_text == "I am sorry! I don't understand you":
                web_results = search_web(user_input)
                if web_results:
                    response_text = web_results[0].get('snippet', 'No information available.')
        st.session_state.conversation.append(f"Chatbot: {response_text}")

for line in st.session_state.conversation:
    st.write(line)
