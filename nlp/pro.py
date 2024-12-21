import re
import spacy
from textblob import TextBlob
from gingerit.gingerit import GingerIt
from nltk.tokenize import sent_tokenize


# Initialize Spacy NLP model (you can choose another model if you prefer)
nlp = spacy.load("en_core_web_sm")

# Function to clean the text (removes extra spaces, punctuation)
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

# Function to simplify the text (processes each sentence with spaCy)
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

# Grammar and spelling correction using TextBlob and Gingerit
def grammar_and_spelling_correction(text):
    # Correct spelling with TextBlob
    spelled_text = TextBlob(text).correct()

    # Correct grammar and spelling with Gingerit
    parser = GingerIt()
    result = parser.parse(str(spelled_text))

    return result['result']

# The main function to process and clean text using NLP
def clean_text_using_nlp(input_text):
    # Step 1: Remove filler words
    text = remove_fillers(input_text)

    # Step 2: Perform grammar and spelling correction
    corrected_text = grammar_and_spelling_correction(text)

    # Step 3: Clean up the text (remove extra spaces, punctuation)
    cleaned_text = clean_text(corrected_text)

    # Step 4: Simplify the text for better readability
    simplified_text = simplify_text(cleaned_text)

    return simplified_text

# Sample text for testing
input_text = """
Uh, I think this is an example text with um, some filler words and maybe some incorrect spellings. like, We want to test the text cleaning methods!
"""

# Call the main function to clean and process the text
processed_text = clean_text_using_nlp(input_text)
print("Processed Text:")
print(processed_text)
