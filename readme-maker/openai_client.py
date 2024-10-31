import requests

def call_openai_api(prompt, api_key):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an assistant that generates detailed and accurate README files for any type of code repository."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code != 200:
        print("Failed to access OpenAI API:", response.json().get("error", {}).get("message", "Unknown error"))
        exit(1)
    return response.json()["choices"][0]["message"]["content"]