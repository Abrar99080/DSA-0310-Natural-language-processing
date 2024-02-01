from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained model and tokenizer for English to French translation
model_name = "Helsinki-NLP/opus-mt-en-fr"  # You can choose a different model if needed
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# English text to be translated
english_text = "Hello, how are you?"

# Tokenize the input text
inputs = tokenizer(english_text, return_tensors="pt")

# Translate the input text to French
with tokenizer.as_target_tokenizer():
    outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)

# Decode and print the translation
french_translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print("English: ", english_text)
print("French: ", french_translation[0])
