import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """Translate this into 1. French, 2. Spanish and 3. Japanese:

What rooms do you have available?
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content": prompt}
        ],
    temperature=0,
)
print(response.choices[0].message.content)