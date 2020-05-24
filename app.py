from flask import Flask 
from flask import render_template, request
app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
	if request.method == "POST":
		sentence = request.form['line_input']
		output = 
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)