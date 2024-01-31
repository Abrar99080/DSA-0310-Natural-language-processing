import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "This is a sample sentence for part-of-speech tagging."
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)
print("Word\t\tPOS Tag")
print("-" * 20)
for word, pos in pos_tags:
    print(f"{word}\t\t{pos}")
