import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["jumping", "jumps", "jumped", "running", "flies", "flies", "stemming", "stemmer"]
stemmed_words = [stemmer.stem(word) for word in words]
for i in range(len(words)):
    print(f"{words[i]} -> {stemmed_words[i]}")
