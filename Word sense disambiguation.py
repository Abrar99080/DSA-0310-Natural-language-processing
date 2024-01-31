from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def lesk_algorithm(word, sentence):
    best_sense = None
    max_overlap = 0
    word = word.lower()
    context = set(word_tokenize(sentence))
    context = [w for w in context if w not in stopwords.words('english')]
    for sense in wordnet.synsets(word):
        definition = set(word_tokenize(sense.definition())
                     + [w for lemma in sense.lemmas() for w in lemma.name().split('_')])
        
        overlap = len(definition.intersection(context))   
        for example in sense.examples():
            example_words = set(word_tokenize(example))
            overlap += len(definition.intersection(example_words))        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense   
    return best_sense
if __name__ == "__main__":
    word = "bank"
    sentence = "I deposited my money in the bank by the river."
    sense = lesk_algorithm(word, sentence)
    if sense:
        print(f"Word: {word}")
        print(f"Sense: {sense.name()}")
        print(f"Definition: {sense.definition()}")
    else:
        print("No sense found.")
