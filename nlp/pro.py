import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
import spacy
import re
from textblob import TextBlob

# Load SpaCy's lightweight English model
nlp = spacy.load("en_core_web_sm")

# Function to clean the text (remove extra spaces and punctuation)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

# Function to remove filler words (uh, um, like)
def remove_fillers(text):
    filler_words = ['uh', 'um', 'like']
    pattern = r'\b(' + '|'.join(filler_words) + r')\b\.{0,3}\s*'
    text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    # Clean up multiple dots
    text = re.sub(r'\.{2,}', '.', text)
    return text

# Function to simplify text using SpaCy
def simplify_text(text):
    sentences = sent_tokenize(text)
    simplified_sentences = []

    for sentence in sentences:
        doc = nlp(sentence)
        simplified_sentence = []

        for token in doc:
            # Keep punctuation and numbers unchanged
            simplified_sentence.append(token.text)

        simplified_sentences.append(" ".join(simplified_sentence))

    return " ".join(simplified_sentences)

# Function to clean text using NLP
def clean_text_using_nlp(input_text):
    # Step 1: Remove fillers
    text = remove_fillers(input_text)

    # Step 2: Perform spell checking with TextBlob
    spelled_text = TextBlob(text).correct()
    
    # Convert TextBlob object to string for further processing
    spelled_text_str = str(spelled_text)

    # Step 3: Clean up the text (remove extra spaces, punctuation)
    cleaned_text = clean_text(spelled_text_str)

    # Step 4: Simplify the text for better readability
    simplified_text = simplify_text(cleaned_text)

    return simplified_text

