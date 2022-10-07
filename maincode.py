from logging import exception
from numpy import take
from setuptools import Command
from geo_location import start  
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import openfile
import playmusic
from speak_function import*
import removefolder
from message import send_message
# import smtplib
import threading
# from md5 import passcheck
from notify import*
import playsound
# from newwifi import*
import keypress
import todo
# function to add current script to the registry
chrome_path = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning nilesh!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon nilesh!")   

    else:
        speak("Good Evening nilesh!")  



def opweb(name):
    webbrowser.get("chrome").open(name)

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')#recognize_google 
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")    
        print("Say that again please...")  
        return "None"
    return query
    
def findquery():
    query = takeCommand().lower()
        # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return
    elif 'open youtube' in query:
        name = 'youtube.com'
        opweb(name)
        return

    elif 'close youtube' in query:
        os.system("taskkill /f /im chrome.exe") 
        return
    elif 'repository' in query:
        name = 'github.com/AJDESAI'
        opweb(name)
        return
    elif 'close repository' in query:
        os.system("taskkill /f /im chrome.exe") 
        return
    elif 'git' in query:
        name = 'github.com'
        opweb(name)
        return
    elif 'close git' in query:
        os.system("taskkill /f /im chrome.exe") 
        return
    elif 'gfg' in query:
        name = 'geeksforgeeks.org'
        opweb(name)
        return
    elif 'close gfg' in query:
        os.system("taskkill /f /im chrome")
        return
    elif 'ignore' in query:
        speak("ok")
        return
    elif 'open google' in query:
        name = 'google.com'
        opweb(name)
        return
    elif 'close google' in query:
        os.system("taskkill /f /im chrome")


    elif 'open stackoverflow' in query:
            name = 'stackoverflow.com'
            opweb(name)
            return   
    elif 'close stackoverflow' in query:
        os.system("taskkill /f /im chrome")
        
    elif 'open java' in query:
        name = 'onlinegdb.com'
        opweb(name)
        return
    elif 'close java' in query:
        os.system("taskkill /f /im chrome")

        
    elif 'open python' in query:
        name = 'programiz.com'
        opweb(name)
        return
    elif 'close python' in query:
        os.system("taskkill /f /im chrome")
           
    elif 'play music' in query:
        try:
           playmusic.music()
        except exception as e:
            print(e)
        return
    elif 'stop music' in query:
        pass
    
    elif 'open keyboard' in query:
        try:
            KeyboardPath = "C:\\Users\\niles\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\On-Screen Keyboard"
            os.startfile(KeyboardPath)
        except exception as e:
            print(e)
        return
    elif 'close keyboard' in query:
        os.system("taskkill /f /im On-Screen Keyboard")

    elif 'open chrome' in query:
        try:
            KeyboardPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome"
            os.startfile(KeyboardPath)
        except exception as e:
            print(e)
        return
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
            
    # elif 'open cmd' or 'terminal' in query:
    #     try:
    #         cmdPath ="C:\\Users\\lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
    #         os.startfile(cmdPath)
    #     except exception as e:
    #         print(e)
    #     return        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
        return 
    # elif 'open powershell' or 'terminal' in query:
    #     try:
    #         cmdPath ="C:\\Users\\niles\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
    #         os.startfile(cmdPath)
    #     except exception as e:
    #         print(e)
    #     return  
    elif 'open vs code' in query:
        try:
            codePath =  "C:\\Users\\niles\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close vs code' in query:
        os.system("taskkill /f /im code.exe")

    elif 'open virtualbox' in query:
        try:
            codePath =  "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close virtualbox' in query:
        os.system("taskkill /f /im VirtualBox.exe")

    elif 'open obs' in query:
        try:
            codePath =  "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close obs' in query:
        os.system("taskkill /f /im obs64.exe")

   
    elif 'open free fire' in query:
        try:
            codePath =  " C:\\Program Files\\BlueStacks_nxt\\HD-Player"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close free fire' in query:
        os.system("taskkill /f /im HD-Player.exe")
        
   
    elif 'open filmora' in query:
        try:
            codePath =  " C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close filmora' in query:
        os.system("taskkill /f /im Wondershare Filmora X.exe")
    
    elif 'open audacity' in query:
        try:
            codePath =  "C:\\Program Files\\Audacity\\Audacity"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close audacity' in query:
        os.system("taskkill /f /im Audacity.exe")

    elif 'open one note' in query:
        try:
            codePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close one note' in query:
        os.system("taskkill /f /im OneNote.exe")   

    elif 'open word' in query:
        try:
            codePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close one word' in query:
        os.system("taskkill /f /im Word.exe")  

    elif 'open excel' in query:
        try:
            codePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close excel' in query:
        os.system("taskkill /f /im Excel.exe")  

    elif 'open Android studio' in query:
        try:
            codePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\Android Studio"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close Android studio' in query:
        os.system("taskkill /f /im Android Studio.exe")


    elif 'open ppt' in query or 'open power point' in query:
        try:
            codePath =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
            os.startfile(codePath)
            return
        except exception as e:
            print(e)
            return 
    elif 'close ppt' in query or 'close power point' in query:
        os.system("taskkill /f /im PowerPoint.exe") 

    elif 'open downloads' in query:
        codePath = "C:\\Users\\lenovo\\Downloads"
        os.startfile(codePath)
        return 
    elif 'open documents' in query:
        codePath = "C:\\Users\\lenovo\\Documents"
        os.startfile(codePath)
        return 
        
    elif 'open notepad' in query:
        codePath ="C:\\Program Files (x86)\\Notepad++\\notepad++"
        os.startfile(codePath)
        return 
    elif 'increase volume' in query:
        keypress.volumeincrease(5)
        return
    elif 'zoom 2x' in query:
        keypress.zoom_(2)
        return
    elif 'zoom 3x' in query:
        keypress.zoom_(3)
        return
    elif 'decelerate' in query:
        keypress.decelerate(1)
    elif 'mute' in query:
        keypress.mute()
        return
    elif 'volume full' in query:
        keypress.mute(100)
        return
    elif 'unmute' in query:
        keypress.mute()
        return 
    elif 'decrease volume' in query:
        keypress.volumedecrease(5)
        return
    elif 'copy' in query:
        keypress.copycontent()
        return 
    elif 'swich' in query:
        keypress.swich()
        return 
    elif 'save' in query:
        keypress.save()
        return 
    elif 'delet file' in query:
        speak(" tell me the name of file ")
        name = takeCommand().lower()
        removefolder.remoefile(name)
        return
    elif 'write' in query:
        speak("wthat should i write")
        cnt = takeCommand().lower()
        if('enter' in cnt):
            keypress.write_(cnt)
        
        return 
    
    elif 'pause' in query:
        keypress.pause()
        return 
    elif 'previous tab' in query:
        keypress.previous_Tab()
        return 
    
    elif 'sreenshot' in query:
        keypress.printsreen()
        return 
        
    elif 'shutdown' in query:
        try:
            speak("Are you shure")
            password = takeCommand()
            if 'yes' in password:
                os.system("shutdown /s /t 1")
            else:
                pass
        except Exception as e:
            print(e)
            speak("Sorry my friend nilesh. I am not able to process the command")
        return 
            
    elif 'restart' in query:
        try:
            speak("Are you shure")
            password = takeCommand()
            if 'yes' in password:
                os.system("shutdown /r /t 1")
            else :
                pass
        except Exception as e:
            print(e)
            speak("Sorry my friend nilesh. I am not able to process the command")
        return 
        
        
    elif 'sleep' in query:
        try:
            # speak(" password : ")
            # password = takeCommand()
            # if '0 7' in password:
            
            os.system("run1132.exe powerprof.d11,SetSuspendState Sleep")
                
        except Exception as e:
            print(e)
            speak("Sorry my friend nilesh. I am not able to process the command")
        return 
    # elif 'connect wifi' in query:
    #     try:
    #         wificommand()
    #     except Exception as e:
    #         print(e)
    #         speak(e)
    #     return 
                            
    elif 'send message' in query:
                
        try:
            speak("What should I say?")
            content = takeCommand()
            speak("whom should i say")
            to = takeCommand() 
            pass   
            send_message(to,content)
        except Exception as e:
            print(e)
            speak("Sorry my friend nilesh. I am not able to send this message")  
        return 
    elif 'todo list' in query:
        todo.todolist()
        return 
    elif 'open map' in query:
        openfile.math()
        return
    elif 'close map' in query:
        os.system("taskkill /f /im msedge.exe") 
        return
    elif 'open oec' in query:
        openfile.oec()
        return
    elif 'close oec' in query:
        os.system("taskkill /f /im msedge.exe") 
    elif 'open dsa' in query:
        openfile.dsa()
    elif 'close dsa' in query:
        pass
    else:
        speak("Say that again please...")  
        takeCommand()
        
        