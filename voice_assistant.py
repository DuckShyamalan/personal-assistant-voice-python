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


#use sapi5 for Windows; espeak for others (non-OSX)
engine=pyttsx3.init('nsss') 
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

engine.say('Good day, could I have your name?')
name = input('What is your name?\n') #os.getlogin()
engine.say(f'Good day, {name}! How may I help you today?')
engine.runAndWait()