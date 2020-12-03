from flask import Flask, request, render_template
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
import string
from spacy.lang.en.stop_words import STOP_WORDS
import pickle


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = list(STOP_WORDS)
    text1 = request.form['text1'].lower()

    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])
    model = pickle.load(open('model.pkl', 'rb'))
    compound = model.predict([text1])

    return render_template('form.html', final=compound[0], text1=text1)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
