import nltk
from nltk import CFG
from nltk.parse.earleychart import EarleyChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'barked'
""")
parser = EarleyChartParser(grammar)
sentence = "the cat chased a dog"
tokens = nltk.word_tokenize(sentence)
for tree in parser.parse(tokens):
    tree.pretty_print()
