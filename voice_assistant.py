import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import json
import requests
import sys
import importlib
import threading

# TODO: support wikipedia, pictures, weather, and more
#use sapi5 for Windows; espeak for other non-OSX
class _TTS:
    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init('nsss')


    def speak(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()
        print(text_)


def speak(message):
    tts = _TTS()
    tts.speak(message)
    print(message)
    del(tts)
    # engine.say(message)
    # engine.runAndWait()

def greet():
    speak(f'Good day, {name}!')
    
def captureSpeech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = recognizer.listen(source)
        
        try:
            statement=recognizer.recognize_google(audio,language='en-uk')
            print(f"{name} said:{statement}\n")

        except Exception as e:
            speak("Sorry, I didn't quite catch that")
            return "None"
        return statement

#print('Booting up PAVel')
#speak('Booting up PAVel')

speak('Good day, could I have your name?')
name = input('What is your name?\n') #os.getlogin()
greet()

if __name__ == '__main__':
    while True:
        speak('How may I help you today?')
        statement = captureSpeech().lower()
        if statement == 0:
            continue
        
        endPhrases = ['goodbye', 'bye', 'see you', 'stop', 'cancel', 'goodnight']
        
        if any(endPhrase in statement for endPhrase in endPhrases):
            speak('PAVel is shutting down, goodbye')
            break
        
        if 'Youtube' in statement:
            speak("Opening Youtube")
            if 'search' in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(f"http://www.youtube.com/results?search_query={statement}")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)

        if 'Google' in statement:
            speak("Opening Google Chrome")
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(5)
            
        if 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        if 'news' in statement:
            speak("Taking you to the BBC")
            webbrowser.open_new_tab("https://www.bbc.com/")
            time.sleep(5)
            
        timePhrases = ['current time', 'time now']
        if any(timePhrase in statement for timePhrase in timePhrases):
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")