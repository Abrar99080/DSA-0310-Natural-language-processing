class PluralStateMachine:
    def __init__(self):
        self.state = 'start'
    def reset(self):
        self.state = 'start'
    def transition(self, input_char):
        transitions = {
            'start': {
                's': 'es',
                'x': 'es',
                'y': 'ies',
            },
            'start_vowel': {
                's': 's',
                'x': 'x',
                'y': 'ys',
            },
        }
        if input_char.isalpha():
            input_char = input_char.lower() 

        if self.state in transitions and input_char in transitions[self.state]:
            plural_suffix = transitions[self.state][input_char]
            return plural_suffix
        else:
            return input_char 
    def generate_plural(self, noun):
        plural = ''
        self.reset()
        for char in noun:
            plural += self.transition(char)
        return plural
noun = "baby"
pluralizer = PluralStateMachine()
plural_form = pluralizer.generate_plural(noun)
print(f"The plural form of '{noun}' is '{plural_form}'")
