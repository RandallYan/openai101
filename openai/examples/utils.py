import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
def create(prompt, model="gpt-3.5-turbo", temperature=0, max_tokens=4096, top_p=2, frequency_penalty=1, presence_penalty=1, stop=["###"]):
    if model == "gpt-3.5-turbo" :
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
                {"role": "user", "content": prompt}
                ],
            temperature=temperature,
            stop=stop
        )
        return response.choices[0].message.content
    else :
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop
        )
        return response.choices[0].text

from jinja2 import Environment, FileSystemLoader
def get_template(template_name):
    # 创建一个 Environment 对象，用于加载模板文件
    env = Environment(loader=FileSystemLoader('templates'))
    # 加载模板文件
    template = env.get_template(template_name)
    return template