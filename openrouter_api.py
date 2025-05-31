import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENROUTER_API_KEY')

def generate_text(prompt, model="openai/gpt-3.5-turbo", max_tokens=150):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "RishtaNAMA",
        "X-Title": "RishtaNAMA"
    }
    json_data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise error for 4xx/5xx
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
