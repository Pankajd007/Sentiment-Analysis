from flask import Flask, request, render_template,jsonify
from spacy.lang.en.stop_words import STOP_WORDS
import pickle
from flasgger.utils import  swag_from
from flasgger import Swagger
import os
from flask import Blueprint
import pathlib

app = Flask(__name__)
swagger_config_dir = str(pathlib.Path(__file__).resolve().parent.parent)

swagger = Swagger(app)
@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
@swag_from(os.path.join(swagger_config_dir, 'swagger_configs', 'swagger_config1.yml'))

def my_form_post():
    stop_words = list(STOP_WORDS)
    text1 = request.form['text1'].lower()

    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])
    model = pickle.load(open('model.pkl', 'rb'))
    compound = model.predict([text1])

    return render_template('form.html', final=compound[0], text1=text1)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
