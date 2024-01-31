import re
transformation_rules = [
    (r'\b[Aa]pple\b', 'Noun'),           
    (r'\b\d+\b', 'Number'),               
    (r'\b\w+ly\b', 'Adverb'),             
    (r'\b\w+ing\b', 'Verb'),              
    (r'\b\w+ed\b', 'Verb'),                
]
def transform_based_pos_tagging(text):
    tagged_words = []
    words = text.split()
    for word in words:
        tagged = False
        for pattern, tag in transformation_rules:
            if re.match(pattern, word, re.IGNORECASE):
                tagged_words.append((word, tag))
                tagged = True
                break
        if not tagged:
            tagged_words.append((word, 'Noun'))  
    return tagged_words
text = "I ate an Apple and it tasted delicious."
tagged_text = transform_based_pos_tagging(text)
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")
