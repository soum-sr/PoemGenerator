import numpy as np 
from tensorflow.keras.utils import to_categorical
print("We are good in data preprocessing")

def clean_text(text):
    words = text.split()
    # To remove punctuations
    table = str.maketrans('','', string.punctuation)
    words = [w.translate(table) for w in words]
    # Remove anything that is not alphabetic
    words = [word for word in words if word.isalpha()]
    return words

def generate_sequences(words):
	length = 10 + 1
	sentences = []
	for i in range(length, len(words)):
		seq = words[i-length:i]
		line = ' '.join(seq)
		sentences.append(line)
	return sentences

def process_data(path):
	raw_data = open(path, 'r', encoding='utf-8').read()
	lower_text = raw_data.lower()
	words = clean_text(lower_text)
	sentences = generate_sequences(words)
	return sentences

def create_training_data(tokenizer, numeric_sentences):
	vocabulary_size = len(tokenizer.word_index) + 1
	data_array = np.array(numeric_sentences)
	X, y = data_array[:,:-1], data_array[:,-1]
	y = to_categorical(y, num_classes=vocabulary_size)
	input_length = X.shape[1]
	return X, y, vocabulary_size,input_length



