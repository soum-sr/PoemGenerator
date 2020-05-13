import tensorflow as tf
from buildModel import build_rnn_model
from dataPreprocessing import process_data,create_training_data
from tokenize import tokenize_sentence

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

# Processing data
path = 't8.shakespeare.txt'
sentences = process_data(path)
tokenizer, numeric_sentences = tokenize_sentence(sentences)
X,y,vocabulary_size = create_training_data(tokenizer, numeric_sentences)


model = build_rnn_model()