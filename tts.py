import pyttsx3 as tts
import speech_recognition as sr
import json
from exceptions import UnsupportedLanguage
# import asyncio


class SpeechEngine:
    def __init__(self, language="english"):
        self.listener = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        # initialize engine
        self.engine = tts.init()

        self.voices = self.engine.getProperty('voices')
        voice_pronounciation = [voice.id for voice in self.voices if self.language == voice.id]
        print(voice_pronounciation)
        if not voice_pronounciation:
            raise UnsupportedLanguage(f"Sorry your language '{self.language}' can not be spoken by the computer")
        self.engine.setProperty('voice', voice_pronounciation[0])
        self.engine.setProperty('rate', 100) #change depending on computer speed
    
        self.identifier = "chatbot"

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_command(self, conversation=False):
        with self.microphone as source:
            self.listener.adjust_for_ambient_noise(source,duration=1)
            # print('listening...')
            user_input = self.listener.listen(source)                # get user input (voice)
            voice = self.listener.recognize_google(user_input, language=self.language)
            print(voice)
            voice = json.dumps(voice, ensure_ascii=False).encode('utf8').decode("ascii")
            voice = voice.lower()                               # makes sure input string is lowercase
        if self.identifier not in voice and not conversation:
            return self.get_command()
        return voice
        # print(voice)
        # if "hey engine" in voice:
        #     self.talk("ok, I will now answer")
        #     response = self.chat.start(voice)
        #     print(response)
        #     with open("text.txt", "w") as fh:
        #         fh.write(f"""
        #         What you said:
        #         '
        #         {voice}
        #         '
        #         What engine said:
        #         '
        #         {response}
        #         '
        #         """)
        #     self.talk(response)