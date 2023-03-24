import utils

prompt = utils.get_template("text_to_command.txt").render()
print(utils.create(prompt))
