import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

print("initializing Vision")

MASTER = "Furqan"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string passed to it


def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the currrent time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am vision. How may I help you?")

# This function will take the command from user


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        query = None
    return query.lower()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # This is a less secured app and  would recommend not
    #  not using your personal email for this. Just use a test email
    # as long as you are doing it for testing purpose.
    server.login('youremail@gmail.com', 'password')
    server.sendmail("reciever email", to, content)
    server.close()


# Logic for executing tasks as per the query
# Main program starts here
def main():
    speak("initializing Vision...")
    wishMe()
    query = takeCommand()

    if 'wikipedia' in query:
        speak('Seacrhing wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        url = "youtube.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query:
        url = "google.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query:
        url = "reddit.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query:
        songs_dir = "D:\\songs\\Indian"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query:
        codePath = "D:\\Users\\Furqan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to furqan' in query:
        try:
            speak("What should I send")
            content = takeCommand()
            to = "reciever email"
            sendEmail(to, content)
            speak("Email has been send successfully")
        except Exception as e:
            print(e)


# First call to main function
main()
