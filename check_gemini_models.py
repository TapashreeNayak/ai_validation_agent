import os
from google import genai

client = genai.Client(
    api_key=os.environ["GOOGLE_API_KEY"]
)

for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)