import re

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Install necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

def load_data(path_data='./data/dataset.json', logs=False):
    import json

    from pandas import json_normalize

    # load JSON-file
    with open(path_data, 'r') as file:
        data = json.load(file)
        # normalize data (return data frame)
        df = json_normalize(data)
    
    # Parse `timestamp` into Readable Datetime Format
    # Assuming timestamp is in milliseconds, convert it to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.reset_index(drop=True)

    if logs:
        # Summary of cleaning
        print("\nCleaned DataFrame:")
        print(df.info())

        # Display a few rows of the cleaned DataFrame
        print("\nCleaned DataFrame Head:")
        print(df.head())

    return df

def normalize_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Remove extra whitespaces
    text = text.strip()

    # Remove punctuation (from preprocess_lemmatizer)
    # text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers (from preprocess_lemmatizer)
    text = re.sub(r'\d+', '', text)

    # Convert to lowercase again (already covered above, so skipped)

    # Tokenize and process words
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stopwords.words("english")]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)

def normalize_data(df):
    # Apply the normalization function to the 'text' column
    df['text'] = df['text'].apply(normalize_text)
    return df