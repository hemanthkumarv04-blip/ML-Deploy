from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/prediction', methods = ['POST'])

def preds():
    sl = request.form['sl']
    sw = request.form['sw']
    pl = request.form['pl']
    pw = request.form['pw']

    with open('notebooks/iris-model.pkl', 'rb') as f:
        model = pickle.load(f)

    prediction_result = model.predict([[sl,sw,pl,pw]])

    return f"Predicted value is {prediction_result}"

app.run()
