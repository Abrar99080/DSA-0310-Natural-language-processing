import random
pos_tags = ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun']
transition_probabilities = {
    'Start': {'Noun': 0.4, 'Verb': 0.3, 'Adjective': 0.1, 'Adverb': 0.1, 'Pronoun': 0.1},
    'Noun': {'Noun': 0.2, 'Verb': 0.4, 'Adjective': 0.2, 'Adverb': 0.1, 'Pronoun': 0.1},
    'Verb': {'Noun': 0.3, 'Verb': 0.2, 'Adjective': 0.2, 'Adverb': 0.2, 'Pronoun': 0.1},
    'Adjective': {'Noun': 0.2, 'Verb': 0.3, 'Adjective': 0.2, 'Adverb': 0.2, 'Pronoun': 0.1},
    'Adverb': {'Noun': 0.1, 'Verb': 0.2, 'Adjective': 0.2, 'Adverb': 0.3, 'Pronoun': 0.2},
    'Pronoun': {'Noun': 0.2, 'Verb': 0.2, 'Adjective': 0.2, 'Adverb': 0.1, 'Pronoun': 0.3},
}
emission_probabilities = {
    'Noun': {'cat': 0.2, 'dog': 0.2, 'tree': 0.1, 'house': 0.1, 'man': 0.4},
    'Verb': {'runs': 0.3, 'jumps': 0.2, 'sleeps': 0.2, 'eats': 0.2, 'walks': 0.1},
    'Adjective': {'big': 0.2, 'small': 0.2, 'happy': 0.2, 'red': 0.2, 'green': 0.2},
    'Adverb': {'quickly': 0.2, 'slowly': 0.2, 'happily': 0.2, 'loudly': 0.2, 'well': 0.2},
    'Pronoun': {'he': 0.2, 'she': 0.2, 'it': 0.2, 'they': 0.2, 'we': 0.2},
}
def stochastic_pos_tagging(sentence):
    tags = []
    current_state = 'Start'
    words = sentence.split()
    for word in words:
        if word in emission_probabilities['Noun']:
            word_pos = 'Noun'
        elif word in emission_probabilities['Verb']:
            word_pos = 'Verb'
        elif word in emission_probabilities['Adjective']:
            word_pos = 'Adjective'
        elif word in emission_probabilities['Adverb']:
            word_pos = 'Adverb'
        elif word in emission_probabilities['Pronoun']:
            word_pos = 'Pronoun'
        else:
            word_pos = random.choice(pos_tags)
        tags.append(word_pos)
        next_state = random.choices(pos_tags, weights=list(transition_probabilities[current_state].values()))[0]
        current_state = next_state
    return list(zip(words, tags))
sentence = "The cat slowly walks happy loudly jumps"
tagged_sentence = stochastic_pos_tagging(sentence)
print(tagged_sentence)
