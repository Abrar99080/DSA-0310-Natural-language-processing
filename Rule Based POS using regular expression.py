import re
patterns = [
    (r'\b(?:\w*ed|ing)\b', 'Verb'),       
    (r'\b(?:\w*\'s)\b', 'Noun'),           
    (r'\b(?:The|A|An)\b', 'Determiner'),   
    (r'\b(?:\d+[\.,]?\d*)\b', 'Number'), 
    (r'\b(?:\w+ly)\b', 'Adverb'),         
    (r'\b(?:\w+est)\b', 'Adjective'),      
    (r'\b(?:\w+er)\b', 'Adjective'),      
    (r'\b(?:\w+ing)\b', 'Verb'),          
    (r'\b(?:\w+ed)\b', 'Verb'),           
    (r'\b(?:\w+s)\b', 'Noun'),             
    (r'\b(?:\w+\'re)\b', 'Verb'),         
    (r'\b(?:\w+\'m)\b', 'Verb'),           
    (r'\b(?:\w+\'ve)\b', 'Verb'),          
    (r'\b(?:\w+\'ll)\b', 'Verb'),          
    (r'\b(?:\w+\'d)\b', 'Verb'),            
    (r'\b(?:\w+)\b', 'Noun'),              
]

def rule_based_pos_tagging(text):
    tagged_words = []
    for word in text.split():
        for pattern, tag in patterns:
            if re.match(pattern, word, re.IGNORECASE):
                tagged_words.append((word, tag))
                break
        else:
            tagged_words.append((word, 'Noun')) 
    return tagged_words
text = "I love running daily I run 2 kms as quickly as i can"
tagged_text = rule_based_pos_tagging(text)
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")
