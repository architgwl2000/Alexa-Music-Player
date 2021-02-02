import pyttsx3

#initialisation
engine = pyttsx3.init()

#newVoiceRate = 50
sen = '.......Welcome to Our Project on playing music using speech recognition. '

#engine processes
engine.say(sen)
engine.runAndWait()
# get audio from microphone

import speech_recognition as sr
from playsound import playsound


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Currently available songs are : Diamond, Agar Tum Saath Ho, Tum Hi Aana, Tera Ban Jaunga")
    print("which song you wanna listen:")
    audio = r.listen(source)

# get the text from audio
msg = r.recognize_google(audio)

song=msg+'.mp3'

print(song)

playsound(song)
