import spacy
nlp = spacy.load("en_core_web_sm")
text = "Hi I am Jeff Bejos the owner of Amazon pvt lmtd"
doc = nlp(text)
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
