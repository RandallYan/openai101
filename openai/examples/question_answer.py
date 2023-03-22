# Answer questions based on existing knowledge.
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = '''I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: What is human life expectancy in the United States?
A: Human life expectancy in the United States is 78 years.

Q: Who was president of the United States in 1955?
A: Dwight D. Eisenhower was president of the United States in 1955.

Q: Which party did he belong to?
A: He belonged to the Republican Party.

Q: What is the square root of banana?
A: Unknown

Q: How does a telescope work?
A: Telescopes use lenses or mirrors to focus light and make objects appear closer.

Q: Where were the 1992 Olympics held?
A: The 1992 Olympics were held in Barcelona, Spain.

Q: How many squigs are in a bonk?
A: Unknown

Q: Where is the Valley of Kings?
A:"
'''

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        # {"role": "system", "content": prompt},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where is the Valley of Kings?"}
    ]
)
print(response.choices[0].message.content)

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n", " Q:", " A:"]
)

print(response.choices[0].text)
