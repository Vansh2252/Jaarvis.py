import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

print("press 0 for male voice assistant,press 1 for female voice assistant")
n=(int)(input())
engine = pyttsx3.init('sapi5')
voice=engine.getProperty('Voices')
#getting detail of current voice
engine.setProperty('voice',voices[n].id)
def speak(audio):
  engine.say(audio)
  engine.runandWait()
  def wishMe():
    hour=int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am excalibur Sir. Please tell me how may I help you")       
def takeCommand():
    
