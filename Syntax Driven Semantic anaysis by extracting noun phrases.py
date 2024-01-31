import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet
sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
grammar = r"NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(pos_tags)
noun_phrases = []
for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
    noun_phrases.append(' '.join(word for word, tag in subtree.leaves()))
for noun_phrase in noun_phrases:
    words = word_tokenize(noun_phrase)
    head_noun = words[-1] 
    meanings = []
    for synset in wordnet.synsets(head_noun):
        meanings.append(synset.definition())

    print(f"Noun Phrase: '{noun_phrase}'")
    print(f"Meanings: {', '.join(meanings)}\n")
