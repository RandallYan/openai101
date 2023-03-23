import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more than 10 employees in the last 3 months
SELECT
"""

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
#         {"role": "user", "content": prompt}
#         ],
#     temperature=0,
#     stop=["###"]
# )
# print(response.choices[0].message.content)

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
#   prompt="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["#", ";"]
)
print(response.choices[0].text)