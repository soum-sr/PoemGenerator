# PoemGenerator
<img src="https://img.shields.io/github/license/soum-sr/PoemGenerator">

Write like Shakespeare with the power of Recurrent Neural Networks. A flask webapp equipped with a tensorflow RNN model that takes in sentence and generates poem like the great poet William Shakespeare. 

![In-use Animation](https://github.com/soum-sr/PoemGenerator/blob/master/poemGen-gif.gif?raw=true "In-use Animation")

#### Checkout the app: https://ml-poem-generator.herokuapp.com/
#### Checkout the article: https://digitaltesseract.com/2020/05/26/sentence-generation-using-rnn/
#
### Create a Virtual Environment in Python

- Install virtualenv
```
pip install virtualenv
```
- Create a virtual environment (Here the name of the virtualenv is 'poemgenerator' you can name it whatever you want and it will be created in your pwd)
```
virtualenv poemgenerator
```
- Start the virtual environment
 * Linux/Mac
```
source poemgenerator/bin/activate
```
 * Windows
```
poemgenerator\Scripts\activate
```

### Install all packages used here
```
pip install -r requirements.txt
```

### To train the model
```
python train.py
```
### To generate poems on terminal
```
python generate.py
```
### To run the flask app
```
python app.py
```


