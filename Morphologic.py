import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
text = "The quick brown foxes jumped over the lazy dogs."
tokens = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token, wordnet.VERB) for token in tokens]
print("Original Tokens:", tokens)
print("Lemmatized Tokens:", lemmatized_tokens)
