import utils

prompt = """Translate this into 1. French, 2. Spanish and 3. Japanese:

# What rooms do you have available?
# """

print(utils.create(model="gpt-3.5-turbo",prompt=prompt))