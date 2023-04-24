from email.mime import audio
from logging import exception
# from operator import imod
from tracemalloc import stop
# from unittest import result
from plyer import notification
import pyttsx3
import subprocess
import speech_recognition as sr
import datetime
from ecapture import ecapture as ec
import wikipedia
import webbrowser
import pyautogui
import pyjokes
import os
from twilio.rest import Client
import shutil
import smtplib
import requests
import winshell
import pywhatkit as kit
import cv2
import sys
import ctypes
import random
from bs4 import BeautifulSoup
from datetime import date
import time
 
 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def make_request(url):
    response = requests.get(url)
    return response.text
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else: 
        speak("Good Evening")
    speak("Please tell me how may I help you")
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
 
    except Exception as e:
        print(e)
        print("Say that Again please...")
        speak('Please Repeat')
        return "None"
    return query

def tellDay():
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

 
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avenue2901@gmail.com', 'harsh4823')
    server.sendmail('avenue2901@gmail.com', to, content)
    server.close()
      
if __name__ == "__main__":
    wishMe()
    while True: 
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)
 
        elif 'covid information' in query:
            speak("opening covid stats")
            webbrowser.open("https://www.worldometers.info/coronavirus/")
 
        elif "no jarvis" in query:
            speak("Thanks for using me, have a good day")
            sys.exit()
 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
 
        elif "switch the window" in query or "switch window" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
 
        elif 'play random music' in query:
            music_dir = 'C:\\Jarvis\\music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
 
        elif 'play music in loop' in query:
            music_dir = 'C:\Jarvis\music'
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\harshit.singh\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)
 
 
        elif 'pause' in query:
            speak("GoodBye Sir")
            exit()
        
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save(r'C:\Users\\harshit.singh\\Pictures\\Screenshots\\picture.png')
            speak("Screenshot taken")
        
        elif 'send email'in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "shelly.gupta@abes.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry")                
 
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(58)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
 
        elif "open google" in query:
            speak("sir what should I search on google for you")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
 
        elif 'play song on youtube' in query:
            kit.playonyt('snap song')

        elif 'day' in query:
            tellDay()
 
        elif 'covid stats' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[0]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
				title="COVID-19 Statistics",
				message=notification_message,
				timeout=5
			)
            speak("here are the stats for COVID-19")

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            # webbrowser.open(query)	
            kit.playonyt(query)

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("http://maps.google.com/?q=" + location)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('C:\\Users\\harshit.singh\\Desktop\\Notes\\jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("C:\\Users\\harshit.singh\\Desktop\\Notes\\jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "send message" in query:
                account_sid = 'AC17c997778bc5197f660423e373b03203'
                auth_token = '6cbe75532de4b8394b17bddfd81cb6c0'
                client = Client(account_sid, auth_token)
                message = client.messages.create(body = takeCommand(),from_='+15719464238',to ='+15558675310')
                print(message.sid)

        speak("sir, do you have any other work for me")

        
