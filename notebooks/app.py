from flask import Flask, requests
import pickle

app = Flask(__name__)

@app.route('/prediction', methods = ['POST'])

def preds():
    sl = request.form['']
    sw = request.form['']
    pl = request.form['']
    pw = request.form['']

    with open('iris-model.pkl', 'rb') as f:
        model = pickle.load(f)

    prediction_result = model.predict([[sl,sw,pl,pw]])

    return f"Predicted value is {prediction_result}"

app.run()