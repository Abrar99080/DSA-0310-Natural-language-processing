import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    detokenizer = TreebankWordDetokenizer()
    ps = PorterStemmer()

    preprocessed_sentences = []

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        filtered_words = [ps.stem(word) for word in words if word.isalnum() and word not in stop_words]
        preprocessed_sentences.append(detokenizer.detokenize(filtered_words))

    return preprocessed_sentences

def calculate_coherence(preprocessed_sentences):
    word_freq = FreqDist()

    for sentence in preprocessed_sentences:
        word_freq.update(sentence.split())

    coherence_score = sum(word_freq[word] for word in word_freq) / len(preprocessed_sentences)

    return coherence_score

def main():
    input_text = """Your input text goes here."""
    
    preprocessed_sentences = preprocess_text(input_text)
    coherence_score = calculate_coherence(preprocessed_sentences)

    print(f"Coherence Score: {coherence_score:.2f}")

if __name__ == "__main__":
    main()
