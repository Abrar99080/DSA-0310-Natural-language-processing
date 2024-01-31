import spacy
nlp = spacy.load("en_core_web_sm")
def resolve_references(text):
    doc = nlp(text)
    resolved_text = []
    previous_noun = None
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            previous_noun = token.text
            resolved_text.append(token.text)
        elif token.pos_ == "PRON" and previous_noun:
            resolved_text.append(previous_noun)
        else:
            resolved_text.append(token.text)
    return ' '.join(resolved_text)
if __name__ == "__main__":
    text = "John is a software engineer. He loves coding. Mary is a data scientist. She is also passionate about her work."
    resolved_text = resolve_references(text)
    print(resolved_text)
