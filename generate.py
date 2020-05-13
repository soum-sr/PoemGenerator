import pickle
import sys
from buildModel import build_rnn_model

with open('tokenizer.pkl' , 'rb') as f:
	tokenizer = pickle.load(f)

vocabulary_size = len(tokenizer.word_index) + 1
input_length = 10
model = build_rnn_model(vocabulary_size, input_length)
model.load_weights('model_RNN_Shakespeare.h5')

# Generate poem

user_input = input("Write the first line of your poem, the generator will complete it!!: \n ")
in_text = user_input.lower()
sys.stdout.write('\n\nYour Poem\n\n')
start = ' ' + in_text + '\n'
sys.stdout.write(start)

for i in range(99):
	encoded = tokenizer.texts_to_sequences([in_text])[0]
	encoded = pad_sequences([encoded], maxlen=input_length, truncating='pre')
	word_pred= model.predict_classes(encoded, verbose=0)
	out_word = ''
	for word, index in tokenizer.word_index.items():
		if index == word_pred:
			out_word = word 
			break
		in_text += ' ' + out_word
		out_word = ' ' + out_word
		if i % 7 == 0 and i != 0:
			out_word = out_word + '\n'
		sys.stdout.write(out_word)
		sys.stdout.flush()