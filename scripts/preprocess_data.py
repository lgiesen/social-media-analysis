import re

import pandas as pd


def load_data(path_data='./data/dataset.json'):
    import json

    from pandas import json_normalize

    # load JSON-file
    with open(path_data, 'r') as file:
        data = json.load(file)
        # normalize data (return data frame)
        df = json_normalize(data)
    
    return df

def clean_data(df, logs=False):
    # 1. Handle Missing or Null Values
    # Check for null values
    if logs:
        print("Null Values Before Cleaning:")
        print(df.isnull().sum())

    
    
    
    
    # TODO: do not drop null values - first check if null





    # Fill or drop missing values based on your preference
    # Example: Fill missing values in 'text' column with an empty string
    df['text'] = df['text'].fillna('')

    # Drop rows where critical columns (e.g., 'text_id', 'user_id') have null values
    # df = df.dropna(subset=['text_id', 'user_id'])

    # 2. Parse `timestamp` into Readable Datetime Format
    # Assuming timestamp is in milliseconds, convert it to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # 3. Remove Duplicates
    # Remove duplicates based on 'text_id' (you can also include 'user_id' if needed)
    df = df.drop_duplicates(subset=['text_id'])

    # Optional: Reset the index after cleaning
    df = df.reset_index(drop=True)

    if logs:
        # Summary of cleaning
        print("\nCleaned DataFrame:")
        print(df.info())

        # Display a few rows of the cleaned DataFrame
        print("\nCleaned DataFrame Head:")
        print(df.head())

    return df

# Function to normalize text
def normalize_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespaces
    text = text.strip()

    return text

def normalize_data(df):
    # Apply the normalization function to the 'text' column
    df['text'] = df['text'].apply(normalize_text)
    return df