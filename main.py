#testing
import tts
import gpt

if __name__ == "__main__":
    engine = tts.SpeechEngine()
    chatbot = gpt.ChatGPT()
    while True:
        print("listening")
        voice = engine.get_command()
        print(f"you said: {voice}")
        if "chatbot" in voice:
            response = chatbot.ask(voice)
            engine.talk(response)
            print(f"engine said: {response}")
    