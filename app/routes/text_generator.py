from fastapi import APIRouter
import requests

router = APIRouter()

@router.post("/generate-text/")
async def generate_text(prompt: str):
    # Call the Hugging Face API to generate text based on the prompt
    url = 'https://api-inference.huggingface.co/models/gpt2'
    headers = {'Authorization': f'Bearer YOUR_HUGGING_FACE_API_KEY'}
    payload = {'inputs': prompt}

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Raises an error for bad responses

    generated_text = response.json()  # Assuming you get the generated text in the JSON response
    return {'generated_text': generated_text}
