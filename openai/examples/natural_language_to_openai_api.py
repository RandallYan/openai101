# Create code to call to the OpenAI API using a natural language instruction.

prompt = '''\"\"\"
Util exposes the following:
util.openai() -> authenticates & returns the openai module, which has the following functions:
openai.Completion.create(
    prompt="<my prompt>", # The prompt to start completing from
    max_tokens=123, # The max number of tokens to generate
    temperature=1.0 # A measure of randomness
    echo=True, # Whether to return the prompt in addition to the generated completion
)
\"\"\"
import util
\"\"\"
Create an OpenAI completion starting from the prompt "Once upon an AI", no more than 5 tokens. Does not include the prompt.
\"\"\"
'''

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)

print(response.choices[0].text)