from flask import Flask, request
import requests
import sys
sys.path.append('nlp/')
from pro import clean_text_using_nlp
from open import report_gen
from smt import gmail_transfer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def hello():
    clean = clean_text_using_nlp(request.get_json()['text'])

    resp = requests.post('https://text-correction-ccu9.onrender.com/correct',json={'text':clean})
    
    data = report_gen(resp.text)

    gmail_transfer(request.get_json()['email'],request.get_json()['name'],data)
    
    
    print(data)
    return ''
if __name__ == '__main__':
    app.run(debug=True)