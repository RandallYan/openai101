import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """\"\"\"
Util exposes the following:

util.stripe() -> authenticates & returns the stripe module; usable as stripe.Charge.create etc
\"\"\"
import util
\"\"\"
Create a Stripe token using the users credit card: 5555-4444-3333-2222, expiration date 12 / 28, cvc 521
\"\"\"
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