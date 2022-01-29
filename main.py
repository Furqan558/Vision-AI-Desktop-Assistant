import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

print("initializing Vision")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string passed to it


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    speak("initializing Vision...")
