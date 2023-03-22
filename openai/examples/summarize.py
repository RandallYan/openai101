# Summarize for a 2nd grader
# Translates difficult text into simpler concepts.

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = '''Summarize this for a second-grade student:

Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
'''

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
