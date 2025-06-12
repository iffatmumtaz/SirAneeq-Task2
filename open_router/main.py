import requests, json

BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = "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"  
MODEL = "deepseek/deepseek-r1-0528:free"

response = requests.post(
    url=f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
    data=json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "user", "content": "What is the meaning of life?"}

        ]
    })
)

print(response.json()['choices'][0]['message']['content'])
