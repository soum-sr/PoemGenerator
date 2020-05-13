from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
from tensorflow.kears.models import Sequential


def build_rnn_model(seq_length,vocabulary_size,input_length):
	model = Sequential()
	model.add(Embedding(vocabulary_size, 50, input_length = input_length))
	model.add(SimpleRNN(25, return_sequences=False))
	model.add(SimpleRNN(25))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(vocabulary_size, activation='softmax'))
	return model
