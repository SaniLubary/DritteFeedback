from flask import Flask, request, jsonify
from textblob import TextBlob
import requests

app = Flask(__name__)

# LibreTranslate URL
url = 'http://localhost:5000/translate'

@app.route('/feedback', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    translatedText = requests.post(url, json={
        "q": text,
        "source": "auto",
        "target": "en"
    })
    print(translatedText)
    print('translatedText')
    return {"hihi": 'hello'}

    textBlob = TextBlob(translatedText)
    emotion = textBlob.sentiment

    response = {
        'emotion': emotion,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
