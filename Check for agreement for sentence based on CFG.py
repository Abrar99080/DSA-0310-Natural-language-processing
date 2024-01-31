import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> 'cat' | 'dog'
    NP_PL -> 'cats' | 'dogs'
    VP_SG -> 'chases' | 'eats'
    VP_PL -> 'chase' | 'eat'
""")
parser = ChartParser(grammar)
def check_agreement(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [token for token in tokens if token in grammar._lexical_index]
    for tree in parser.parse(tokens):
        return True 
    return False  
sentences = [
    "the cat chases",
    "the cats chase",
    "dogs eat",
    "dog eats"
]
for sentence in sentences:
    if check_agreement(sentence):
        print(f"'{sentence}' follows the grammar rules.")
    else:
        print(f"'{sentence}' violates the grammar rules.")
