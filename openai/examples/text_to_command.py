import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """Convert this text to a programmatic command:

Example: Ask Constance if we need some bread
Output: send-msg `find constance` Do we need some bread?

Reach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday
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
