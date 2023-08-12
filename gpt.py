import openai

def getapikey():
    with open("token.txt", "r") as fh:
        token = fh.read()

    return token.split("\n")[0]

class ChatGPT:
    def __init__(self, model=""):
        openai.api_key = getapikey()
        if not model:
            self.model = "gpt-3.5-turbo-0301"
        else:
            self.model = model

    def ask(self, message):
        chat_completion = openai.ChatCompletion.create(model=self.model, messages=[{"role": "user", "content": message}])

        return chat_completion.choices[0].message.content