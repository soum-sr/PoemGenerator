import tensorflow as tf

def train(model, batch_size, epochs, learning_rate,X,y):
	optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
	model.compile(loss='categorical_crossentropy', optimizer = optimizer, metrics=['accuracy'])
	history = model.fit(X,y,batch_size=batch_size,epochs=epochs)
	return history, model
