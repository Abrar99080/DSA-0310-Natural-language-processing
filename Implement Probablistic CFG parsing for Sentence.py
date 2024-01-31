import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "The quick brown fox jumps over the lazy dog."
doc = nlp(sentence)
for token in doc:
    print(f"{token.text}: {token.dep_} --> {token.head.text}")
