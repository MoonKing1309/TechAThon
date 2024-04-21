from flask import Flask,request, render_template
import pickle,joblib
import numpy as np
app = Flask(__name__, template_folder='templates')
import os
path=os.chdir(str("D:/MoonDrive/TechAThon/flask"))

model=pickle.load(open('./LogReg.pickle','rb'))
vectoriser = pickle.load(open('./vectoriser.pickle','rb'))
import dill 
preprocess = dill.load(open('./PreProcess.dill','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predictLR',methods=['POST','GET'])
def predict():
    i =''
    for key, value in request.form.items():
        if key == 'text':  # Replace 'input1', 'input2' with your desired input keys
            i = value
    text =[]
    text.append(i)
    textdata = vectoriser.transform(preprocess(text))
    sentiment = model.predict(textdata)

    if sentiment[0]==0:
        return render_template('index.html',pred='The Sentiment of the given text is Negative')
    else:
        return render_template('index.html',pred='The Sentiment of the given text is Positive')



if __name__ == '__main__':
    app.run(debug=False)
