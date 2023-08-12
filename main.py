import tts
import gpt

if __name__ == "__main__":
    engine = tts.SpeechEngine()
    chatbot = gpt.ChatGPT()
    conversation_started = False
    while True:
        voice = ""
        print("listening...")
        voice = engine.get_command(conversation_started)
        conversation_started = True
        if "stop {engine.identifier}" in voice:
            break
        print(f"you said: {voice}")
        response = chatbot.ask(voice)
        engine.talk(response)
        print(f"engine said: {response}")
    