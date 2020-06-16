from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_bootstrap import Bootstrap
import os
import subprocess
import sys
import numpy as np
import pickle

app = Flask(__name__)
Bootstrap(app)

"""
Routes
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            model_path = os.path.join('static', 'model.pkl')
            uploaded_file.save(model_path)
            # class_name = inference.get_prediction(image_path)
            # print('CLASS NAME=', class_name)
            result = {
                'model_path': model_path
            }
            return render_template('show.html', result=result)
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model = pickle.load(open('static/model.pkl','rb'))
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([list(data.values())])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
