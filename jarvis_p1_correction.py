import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("good morning!")
    elif hour >= 12 and hour< 6:
        speak("good evening!")
    else:
        speak('good night')

    speak("I'm jarvis Sir")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print('users said'+query)
    except:
        print('again say')
        return 'none'
    return query


if __name__ == '__main__':
    wishme()
    query = take_command().lower()
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipwdia:")
        print("According to wikipwdia:")
        speak("results ")
    elif "open google" in query:
        webbrowser.open("google.com")

    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open stackoverflow " in query:
        webbrowser.open("stackoverflow.com")













