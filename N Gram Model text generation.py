import random
corpus = "This is a sample text corpus used for building a basic bigram model for text generation. The model predicts the next word based on the previous word."
words = corpus.split()
bigrams = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word in bigrams:
        bigrams[current_word].append(next_word)
    else:
        bigrams[current_word] = [next_word]
def generate_text(start_word, num_words):
    generated_text = [start_word]
    current_word = start_word
    for _ in range(num_words - 1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    return " ".join(generated_text)
start_word = "This"
num_words = 10
generated_text = generate_text(start_word, num_words)
print(generated_text)
