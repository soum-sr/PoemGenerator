import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pickle
import sys
import os
from buildModel import build_rnn_model
from tensorflow.keras.preprocessing.sequence import pad_sequences



def poem_generator():
	user_input = input("Write the first line of your poem, the poem generator will complete it!! \n>>  ")
	in_text = user_input.lower()
	sys.stdout.write('\n\nYour Poem\n\n')
	start = ' '+ in_text+'\n'
	sys.stdout.write(start)
	for i in range(99):
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		encoded = pad_sequences([encoded], maxlen = input_length, truncating = 'pre')
		yhat = model.predict_classes(encoded, verbose = 0)
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		in_text += ' ' + out_word
		out_word = ' ' + out_word
		if i % 7 ==0 and i !=0:
			out_word = out_word + '\n'
            
		sys.stdout.write(out_word)
		sys.stdout.flush()
	sys.stdout.write('\n\n')
	
with open('tokenizer.pkl' , 'rb') as f:
	tokenizer = pickle.load(f)

vocabulary_size = len(tokenizer.word_index) + 1
input_length = 10
model = build_rnn_model(vocabulary_size, input_length)
model.load_weights('model_RNN_Shakespeare.h5')

# Generate poem
poem_generator()