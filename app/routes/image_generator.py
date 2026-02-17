from flask import Blueprint, request, jsonify
import requests

image_generator_bp = Blueprint('image_generator', __name__)

@image_generator_bp.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Call Stable Diffusion API to generate image
    response = requests.post('https://api.stablediffusionapi.com/v3/generate', json={
        'prompt': prompt,
        'num_images': 1,
        'size': '1024x1024'
    })

    if response.status_code != 200:
        return jsonify({'error': 'Failed to generate image'}), 500

    image_url = response.json().get('url')
    return jsonify({'image_url': image_url}), 200

