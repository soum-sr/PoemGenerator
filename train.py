import tensorflow as tf
from pickle import dump
from buildModel import build_rnn_model
from dataPreprocessing import process_data,create_training_data
from tokenize_sentence import tokenize_sentence

def train(model, batch_size, epochs, learning_rate,X,y):
	optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
	model.compile(loss='categorical_crossentropy', optimizer = optimizer, metrics=['accuracy'])
	history = model.fit(X,y,batch_size=batch_size,epochs=epochs)
	print("--"*10)
	print("Model Training Complete")
	print("--"*10)
	print("Saving model...")
	filename = 'model_RNN_Shakespeare.h5'
	model.save(filename)
	print("Model saved as : ",filename)
	print("--"*10)
	return history, model

### TODO: Make all inputs from ARG
print("We are here")
# Processing data
path = 't8.shakespeare.txt'
sentences = process_data(path)
tokenizer, numeric_sentences = tokenize_sentence(sentences)
X,y,vocabulary_size,input_length = create_training_data(tokenizer, numeric_sentences)

model = build_rnn_model(vocabulary_size,input_length)
print("--"*10)
print("Starting the traing of the model: ")
print("--"*10)

batch_size = 128
epochs = 150
learning_rate = 0.0009
train(model, batch_size, epochs, learning_rate, X,y)

# Dump the tokenizer
print("--"*10)
print("Saving tokenizer... ")
dump(tokenizer, open('tokenizer.pkl', 'wb'))
print("Tokenizer saved!!")
print("--"*10)