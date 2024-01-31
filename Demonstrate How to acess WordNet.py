from nltk.corpus import wordnet
word = "car"
synsets = wordnet.synsets(word)
for synset in synsets:
    print(f"Synset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {', '.join(synset.examples())}")
    print()
if synsets:
    hypernyms = synsets[0].hypernyms()
    if hypernyms:
        print(f"Hypernyms for {synsets[0].name()}: {', '.join([h.name() for h in hypernyms])}")
if synsets:
    hyponyms = synsets[0].hyponyms()
    if hyponyms:
        print(f"Hyponyms for {synsets[0].name()}: {', '.join([h.name() for h in hyponyms])}")
