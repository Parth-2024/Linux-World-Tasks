from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(txt,filename):
    speech=gTTS(text=txt,lang="en")
    speech.save(filename)
    return filename

def play(filename):
    playsound(filename)

txt=input("Enter a text:")
filename=input("Enter a file name:")

file=text_to_speech(txt,filename)

play(file)

os.remove(file)