from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk

# Install necessary NLTK data
#nltk.download("stopwords")



def preprocess_lemmatizer(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [word for word in words if word not in stopwords.words("english")]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]  # Stem words
    return ' '.join(words)