from tensorflow.keras.preprocessing.text import Tokenizer

def tokenize_sentence(sentences):
	tokenizer = Tokenizer()
	tokenizer.fit_on_texts(sentences)
	numeric_sentences = tokenizer.texts_to_sequences(sentences)
	return tokenizer, numeric_sentences