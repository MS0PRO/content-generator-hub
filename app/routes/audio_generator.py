from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HUGGING_FACE_API_URL = 'https://api.huggingface.co/models/facebook/tts_transformer'
HUGGING_FACE_API_TOKEN = 'your_hugging_face_api_token'

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    headers = {'Authorization': f'Bearer {HUGGING_FACE_API_TOKEN}', 'Content-Type': 'application/json'}
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json={'inputs': text})

    if response.status_code == 200:
        audio_url = response.json().get('audio_url')
        return jsonify({'audio_url': audio_url}), 200
    else:
        return jsonify({'error': 'Failed to generate audio'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)