# PoemGenerator
<img src="https://img.shields.io/github/license/soum-sr/PoemGenerator">
#### Write like shakespeare with the power of Recurrent Neural Networks

![In-use Animation](https://github.com/soum-sr/PoemGenerator/blob/master/poemGen-gif.gif?raw=true "In-use Animation")

#### Checkout the app: https://ml-poem-generator.herokuapp.com/
#### Checkout the article: https://digitaltesseract.com/2020/05/26/sentence-generation-using-rnn/
#
### Create a Virtual Environment in Python

- Install virtualenv
```
pip install virtualenv
```
- Create a virtual environment (Here the name of the virtualenv is 'streamlitapp' you can name it whatever you want and it will be created on your pwd)
```
virtualenv streamlitapp
```
- Start the virtual environment
 * Linux/Mac
```
source streamlitapp/bin/activate
```
 * Windows
```
streamlitapp\Scripts\activate
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


