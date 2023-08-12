#testing
import tts

if __name__ == "__main__":
    engine = tts.SpeechEngine()
    print("listening")
    voice = engine.get_command()
    engine.talk(f"you said: {voice}")
    print(f"you said: {voice}")