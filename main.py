import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

print("press 0 for male voice assistant,press 1 for female voice assistant")
n=(int)(input())
engine = pyttsx3.init('sapi5')

