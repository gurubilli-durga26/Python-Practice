'''
gTTs -->Google text to Speech

from gtts import gTTS
text = gTTS("Hello guy's,how are you doing?")
text.save("audio.mp3")

gTTs -->Google text to Speech
playsound-->pip install playsound==1.2.2
pyaudio-->pip install pyaudio
'''
from gtts import gTTS
import playsound
text = gTTS("Hello guy's,how are you doing?")
#text.save("audio.mp3")
playsound.playsound('audio.mp3')

'''

3 Functions-->1)Listen (SpeechRecognition)
              2)respond(gtts)
              3)Assistant(conditions)-->conversation,Greeting,datetime,locate a place,open a browser,play a youtube video

#import the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
#let us create listen function
def listen():
    """Function for speech Recogntion"""
    r=sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print("start talking now")
        audio=r.listen(source,phrase_time_limit=10)
    #We need to give our text as voice
    data=""
    #here we will give exceptions(try,except)
    try:
        data =r.recognize_google(audio)
        print("you said:",data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speak clearly request is failing")
    return data
    #tts = gTTS(data)
    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")
#listen()
def respond(String):
    "Function to respond back"""
    print(String)
    tts=gTTS(String)
    tts.save("Speech.mp3")
    #we are using uuid -->to randomize the content in the audio file.
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#here we will make our virtual assitant into action
def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listenning=True
        respond("I am fine thanks for asking")
    elif "what are your plans" in data:
        listening =True
        respond("Only Study...one focus in 2026")
    elif "how are things going" in data:
        listening=True
        respond("antha okay inka niney set avali")
    elif "time" in data:
        listening=True
        respond(time.ctime())
    elif "stop talking" in data:
        listening=False
        respond("okay cool..kopadakuu bye")
    elif "locate" in data:
        listening=True
        respond(webbrowser.open("https://www.google.com/maps/search" + data.replace("locate","")))
        print("located")
    elif "open Google" in data:
        listenning=True
        respond("Opening Google")
        webbrowser.open("https://www.google.com/?zx=1789455524408")
    elif "open LinkedIn" in data:
        listening=True
        respond("Opening linkedln")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open github" in data:
        listening=True
        respond("opening github")
        webbrowser.open("https://github.com/")
    elif "open youtube" in data:
        listening=True
        respond("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    try:
        return listening
    except UnboundLocalError as e:
        print("make sure to speak lounder and faster")
respond("hey durga..Good to hear from you .how are you?")
listening=True
while listening:
    data =listen()
    listening=va(data)
#https://github.com/
#https://www.linkedin.com/feed/
#https://www.google.com/maps

#Finish your tasks-->choice of games-->github links.
#Virtual automation-->qrcode,play a game.

'''












