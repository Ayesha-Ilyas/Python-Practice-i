import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr


engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def wishme():
 hour=int(dateime.datetime.now().hour)
 if hour >= 0 and hour < 12:
  speak("good morning!")
 elif hour >= 12 and hour < 18:
  speak("good evening!")
 speak("I'm jarvis Sir")
 print("I m jarvis")


def take_command():
 with sr.Microphone as source :
  r=sr.recognizer()
  print("listening....")
  r.pause_threshold=1
  audio= r.listen(source)
 try:
  print("recognizing.....")
  query=r.recognize_google(audio,language='en_in')
  print(f"users said: {query}\n")
 except Exception as e:
  print('again say')
  return None
 return query


def sendEmail(to,content):
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.ehlo()
 server.starttls()
 server.login('ayeshailyas279@gamil.com','ayeshailyas279')
 server.sendmail('ayeshailyas279@gamil.com',to,content)
 server.close()


if __name__ == "_main_":
  wishme()
  while True:
   query = take_command().lower()
   if wikipedia in query:
    speak("searching wikipedia")
    query =query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak("According to wikipwdia:")
    print("According to wikipwdia:")
    speak("results ")
   elif "open google" in query:
    webbrowser.open("google.com")
   elif "open youtube" in query:
    webbrowser.open("youtube.com")
   elif "open stackoverflow " in query:
    webbrowser.open("stackoverflow.com")
