# Chatbot with Web Search Integration

This project implements an interactive chatbot using **Streamlit** for the user interface, **Natural Language Processing (NLP)** techniques for chatbot responses, and **Google Custom Search** for retrieving relevant web results when the chatbot does not understand a query. 

## Features

- Basic conversation and greeting handling
- NLP-based query processing and response generation
- **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization to find relevant responses
- **Web Search Integration** using Google Custom Search API for enhanced responses
- Built with **Streamlit** for a lightweight, interactive user interface

---

## Tech Stack

- **Python 3.x**
- **Streamlit** for UI
- **NLTK** for text preprocessing and tokenization
- **Scikit-learn** for TF-IDF vectorization and cosine similarity
- **BeautifulSoup** and **Requests** for web scraping and API calls
- **Google Custom Search API** for web-based responses

---

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install streamlit requests beautifulsoup4 nltk scikit-learn
```

You will also need an API key for Google Custom Search. Obtain your key from [Google Cloud Console](https://console.cloud.google.com/).

### NLTK Data

You'll also need to download the necessary NLTK data for tokenization and lemmatization:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

---

## How It Works

1. **Chatbot Text Response**:
   - The chatbot reads a text file `chatbot.txt` containing pre-defined conversations or knowledge.
   - When the user inputs a query, the chatbot processes the input using **TF-IDF vectorization** and **cosine similarity** to find the closest matching response from the `chatbot.txt` file.

2. **Greetings**:
   - The chatbot recognizes simple greetings like "hello" and "hi" and responds with a random greeting from a list.

3. **Web Search Integration**:
   - If the chatbot doesn't understand a query, it performs a **Google Custom Search** and retrieves the most relevant result snippet using the provided API key and search engine ID.

---

## File Structure

```plaintext
.
├── chatbot.py                # Main Streamlit app
├── chatbot_corpus.txt        # Text file containing pre-defined responses
├── README.md                 # This file
```

---

## Usage

1. **Run the app**:
   To run the chatbot, use Streamlit:

   ```bash
   streamlit run chatbot.py
   ```

2. **Interact with the chatbot**:
   - Enter queries into the text box in the web interface.
   - If the chatbot cannot find a relevant response in its predefined text, it will perform a web search to find an answer.

3. **Exit**:
   - Type "bye", "exit", or "quit" to end the conversation.

---

## Example

### User Interaction:

```plaintext
You: Hello
Chatbot: Hi there!

You: Can you tell me about Machine Learning?
Chatbot: Machine learning is a method of data analysis that automates analytical model building...

You: Who is Elon Musk?
Chatbot: Elon Musk is a business magnate and investor. (retrieved via web search)

You: Bye
Chatbot: Bye! Take care.
```

---

## Customization

1. **Edit the chatbot responses**:
   Modify the `chatbot_corpus.txt` file to include more knowledge or predefined responses.

2. **API Key Configuration**:
   Replace the `API_KEY` and `CSE_ID` with your own values from the Google Cloud Console.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- [Streamlit Documentation](https://docs.streamlit.io/)
- [NLTK Documentation](https://www.nltk.org/)
- [Google Custom Search API](https://developers.google.com/custom-search)
