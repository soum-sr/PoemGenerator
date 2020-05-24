import pickle
from flask import Flask 
from flask import render_template, request
from buildModel import build_rnn_model

from generate_app import poem_generator

app = Flask(__name__)

	
with open('tokenizer.pkl' , 'rb') as f:
	tokenizer = pickle.load(f)

vocabulary_size = len(tokenizer.word_index) + 1
input_length = 10
model = build_rnn_model(vocabulary_size, input_length)
model.load_weights('model_RNN_Shakespeare.h5')

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == "POST":
		sentence = request.form['line_input']
		if len(sentence) != 0:
			output = poem_generator(sentence, model, tokenizer,input_length) 
			return render_template('index.html', output=output)
		
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)