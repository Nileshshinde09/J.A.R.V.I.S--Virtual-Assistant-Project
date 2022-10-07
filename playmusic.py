import os
import random 
import playsound
import pyaudio

def music():
    path="D:\\AI\\python\\jarvis\\music"

    files=os.listdir(path)

    d=random.choice(files)

    playsound(os.startfile("D:\\AI\\python\\jarvis\\music\\"+d))
    return