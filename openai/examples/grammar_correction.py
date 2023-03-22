import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = '''Correct this to standard English:

She no went to the market.'''

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        # {"role": "system", "content": prompt},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": prompt}
    ]
)
print(prompt)
print(response.choices[0].message.content)
