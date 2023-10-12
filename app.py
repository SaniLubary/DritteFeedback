from flask import Flask, request, jsonify
from textblob import TextBlob
import requests

app = Flask(__name__)

# LibreTranslate URL
url = 'http://localhost:5003/translate'

@app.route('/feedback', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    try: 
        response = requests.post(url, json={
            "q": text,
            "source": "es",
            "target": "en"
        })
        if response.status_code == 200:
            # If the response contains JSON data, you can use the json() method
            translatedText = response.json()['translatedText']
            print('JSON Data:', translatedText)
            try:
                textBlob = TextBlob(translatedText)
                emotion = textBlob.sentiment
                return {'emotion': emotion[0]}
            except Exception as e:
                print('Error is', e)
                return {'error': 'Exception with sentiment api'}
        else:
            print(f'Request failed with status code {response.status_code}')
            print('Response content:', response.content)
            return {"error": 'Error unknown'}
    except Exception as e:
        print(e)
        return {'error': "Some error occurred"}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
