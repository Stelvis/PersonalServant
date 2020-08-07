#All you need to do so he recognizes your voice
import speech_recognition as sr
from gtts import gTTS
import os
language = 'en'


r = sr.Recognizer()

with sr.Microphone() as source:
    while(1):
        audio = r.listen(source)
        try:
            iSaid = r.recognize_google(audio)
            if iSaid == "tell me a joke":
                Response = "I am currently looking at a joke "
            elif iSaid == "how are you doing":
                Response ="I am a humble servent with a robot type voice i am not programmed to have emotions"
            elif iSaid  == "exit":
                break
            output=gTTS(text = Response,lang=language,slow=False)
            output.save("answer.mp3")
            os.system("start answer.mp3")
            audio = r.listen(source)
        except:
            print('Didnt quite get that')



