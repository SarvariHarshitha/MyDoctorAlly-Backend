import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import sent_tokenize
import spacy
import re
from textblob import TextBlob



nlp = spacy.load("en_core_web_sm")#lightweight English model optimized for small memory usage and fast performance
#tokenization, part-of-speech tagging, dependency parsing, named entity recognition, and lemmatization.

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()


def remove_fillers(text):
    """
    Remove filler words and excessive ellipsis
    """
    filler_words = ['uh', 'um', 'like']
    pattern = r'\b(' + '|'.join(filler_words) + r')\b\.{0,3}\s*'
    text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    # Clean up multiple dots
    text = re.sub(r'\.{2,}', '.', text)
    return text


def simplify_text(text):
    """
    Simplify the input text for better readability.
    """
    # Break text into sentences
    sentences = sent_tokenize(text)
    simplified_sentences = []

    for sentence in sentences:
        doc = nlp(sentence)
        simplified_sentence = []

        for token in doc:
            
            # Keep punctuation and numbers unchanged
            simplified_sentence.append(token.text)

        # Reconstruct the sentence
        simplified_sentences.append(" ".join(simplified_sentence))

    # Reconstruct the text
    return " ".join(simplified_sentences)

def clean_text_using_nlp(input_text):

    
    #remove filters 
    text= remove_fillers(input_text)

    #spell checker
    spelled_text = TextBlob(text).correct()



    # Process the text
    cleaned_text = clean_text(spelled_text)


    simplified_text = simplify_text(cleaned_text)


    return simplified_text










