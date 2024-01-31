import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'ball'
    V -> 'chased' | 'ate'
""")

sentence = "the cat chased the dog"

tokens = sentence.split()
parser = EarleyChartParser(grammar)
for tree in parser.parse(tokens):
    tree.pretty_print()
