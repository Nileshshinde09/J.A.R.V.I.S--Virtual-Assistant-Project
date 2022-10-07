from logging import exception
from tkinter import *
from tkinter import ttk
from turtle import tilt
import maincode
import os
import speech_recognition as sr 
from playsound import playsound
import win32gui,win32con
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)



from pydub import AudioSegment
from pydub.playback import play
import os
# try:

#     song = AudioSegment.from_wav("D:\\python\\venv\\Jarvis_Startup.wav")
#     play(song)
# except exception as e:
#     print(e)
# while True:
#     maincode.findquery()
import urllib.request

def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        print("Disconnected.....")
        return False
while True:
    if connect():
        try:
            print("connected...")
            maincode.wishMe()

            while True:
                    hot_word='Jarvis'
                    r=sr.Recognizer()
                    print("start")
                    r.pause_threshold=0.5
                    with sr.Microphone() as source:
                        text=r.listen(source)
                    try:
                        print("Recognizing...")
                        # text=r.recognize_google(text)
                        text = r.recognize_google(text,language='en-in')
                        print(text)
                        if hot_word in text or 'jervis' in text or 'javis' in text:
                            chime = AudioSegment.from_wav("D:\\AI\\python\\jarvis\\chime.wav")
                            play(chime)
                            maincode.findquery()
                    except sr.UnknownValueError:
                        print("Retry")
                    except:
                        continue
        except exception as e:
                print(e)