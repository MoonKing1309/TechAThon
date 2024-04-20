from flask import Flask,request, render_template
import pickle,joblib
import numpy as np
app = Flask(__name__, template_folder='templates')
import os
path=os.chdir(str('/Users/moon/Documents/Programming/Python/Machine_Learning/TechAThon/flask'))

model=pickle.load(open('./LogReg.pickle','rb'))
vectoriser = pickle.load(open('./vectoriser.pickle','rb'))
import dill 
preprocess = dill.load(open('./PreProcess.dill','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    text =''
    for key, value in request.form.items():
        if key == 'text':  # Replace 'input1', 'input2' with your desired input keys
            text = value
    textdata = vectoriser.transform(preprocess(text))
    sentiment = model.predict(textdata)
    if sentiment==0:
        return render_template('index.html',pred='The Sentiment of the given text is {}'.format("Negative"))
    else:
        return render_template('index.html',pred='The Sentiment of the given text is {}'.format("Positive"))



if __name__ == '__main__':
    app.run(debug=False)
