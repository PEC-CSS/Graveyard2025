
"""
Sentiment Analysis of IMDB Movie Reviews

Task Overview:
My goal is to develop a sentiment analysis pipeline that classifies movie reviews 
into positive or negative sentiments. 
I perform text cleaning, extract features using TF-IDF, and compare two 
models: Logistic Regression and Multinomial Naive Bayes. I then choose my final model 
based on performance.


"""


# Importing Necessary Libraries
import pandas as pd                
import numpy as np                
import re                        # For using regular expressions called as regex
import string                    # For string operations like punctuation removal
import nltk                      # For various NLP tasks like tokenization
import seaborn as sns            # For plotting confusion matrix
import matplotlib.pyplot as plt 

from bs4 import BeautifulSoup    # To strip HTML tags from reviews

# NLTK components for text processing:
from nltk.corpus import stopwords            # For stopword lists
from nltk.tokenize import word_tokenize        # To split text into words
from nltk.stem import WordNetLemmatizer        # To get the base (lemma) form of words

# For feature extraction using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

# For splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split

# Machine Learning models (Logistic Regression and Naive Bayes)
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# For model evaluation: classification report, accuracy, confusion matrix
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix




# Downloading NLTK Resources
# You need to download the necessary NLTK data files (only required the first time)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# STEP 1: Load the Dataset Locally
print("Loading the IMDB dataset locally...")

# Load the dataset from the local file (Ensure IMDB_Dataset.csv is in the same directory)
dataset_path = "IMDB_Dataset.csv"

try:
    df = pd.read_csv(dataset_path)
    print(" Successfully loaded dataset from local file!")
except FileNotFoundError:
    print(f" Error: {dataset_path} not found. Please download and place it in the same directory.")
    exit()

# I check the shape and first few rows to see what I'm working with.
print("Dataset shape:", df.shape)
print(df.head(5))

# I assume the dataset has two columns: 'review' and 'sentiment'.
# I convert the sentiment labels to binary (1 for positive, 0 for negative).
df['sentiment'] = df['sentiment'].map({"positive": 1, "negative": 0})

# STEP 2: Data Cleaning & Preprocessing
print("\nStarting text preprocessing...")

def strip_html(text):
    
    # I remove HTML tags from the text.
    # Argument:text (str): The text that might contain HTML.    
    # Returns:str: The text with HTML removed.
    
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    # I remove any text within square brackets using regex.   
    # Args:text (str): The input text.
    # Returns:str: Text without square bracket content.
    
    return re.sub(r'\[[^]]*\]', '', text)

def remove_special_characters(text):
    
    # I remove special characters from the text.
    # Args:text (str): Input text.
    # Returns:str: Clean text with only letters, numbers, and spaces.
    
    # The pattern allows letters, numbers, and whitespace
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', text)

def preprocess_text(text):

    # I preprocess the text by cleaning and normalizing it.
    #  Steps:
    #   1. Remove HTML tags.
    #   2. Remove text between square brackets.
    #   3. Remove special characters.
    #   4. Convert text to lowercase.
    #   5. Tokenize text into words.
    #   6. Remove stopwords.
    #   7. Lemmatize the words.
    # Args:text (str): The raw input text.    
    # Returns:str: The cleaned and preprocessed text.
    
    # Remove HTML and square brackets
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    # Remove special characters
    text = remove_special_characters(text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize text into words
    tokens = word_tokenize(text)
    # Get the list of English stopwords
    stop_words = set(stopwords.words("english"))
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    # Lemmatize each token (I could choose 'n' for noun or adjust based on context; here I use default which is noun)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Join the tokens back into a single string
    return " ".join(tokens)

# I apply the preprocessing to every review in my dataset.

df['clean_review'] = df['review'].apply(preprocess_text)
print("Sample preprocessed review:")
print(df['clean_review'].iloc[0])

# STEP 3: Feature Extraction using TF-IDF
# I use TF-IDF to convert the preprocessed text into a numerical matrix.
# max_features=5000 limits the vocabulary to 5000 most important words, and ngram_range=(1,2) uses single words and pairs.
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = tfidf.fit_transform(df['clean_review'])
y = df['sentiment']
print("TF-IDF matrix shape:", X.shape)

# STEP 4: Splitting the Dataset
# I split the data into 80% training and 20% testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# STEP 5: Model Training & Evaluation
# I set up two models for comparison: Logistic Regression and Multinomial Naive Bayes.
# I choose these because they are fast, simple, and often perform well for text classification.

# Model 1: Logistic Regression
print("\n--- Logistic Regression ---")
lr = LogisticRegression(max_iter=500, random_state=42,solver='liblinear')
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_lr))

# Model 2: Multinomial Naive Bayes
print("\n--- Multinomial Naive Bayes ---")
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_pred_mnb = mnb.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_mnb))

# STEP 6: Model Selection
best_model = "Logistic Regression" if accuracy_score(y_test, y_pred_lr) >= accuracy_score(y_test, y_pred_mnb) else "Multinomial Naive Bayes"
print(f"\nFinal Model Choice: {best_model}")


#STEP 7 : Visualizing the Confusion Matrix
def plot_confusion_matrix(y_true, y_pred, model_name):
    """Plots a confusion matrix using Seaborn heatmap."""
    cm = confusion_matrix(y_true, y_pred)  # Generate confusion matrix
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, xticklabels=["Negative", "Positive"], yticklabels=["Negative", "Positive"])
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# Plot confusion matrices for both models
print("\n📉 Confusion Matrix - Logistic Regression")
plot_confusion_matrix(y_test, y_pred_lr, "Logistic Regression")

print("\n📉 Confusion Matrix - Multinomial Naive Bayes")
plot_confusion_matrix(y_test, y_pred_mnb, "Multinomial Naive Bayes")
# Conclusion

print("\n🚀 Sentiment Analysis Completed! 🔥")

#THANK YOUUUUU FOR READING THIS :)