import psutil
import pyautogui
from speak_function import *
def copycontent():
    pyautogui.keyDown("ctrl")

    pyautogui.press("a")

    pyautogui.keyUp("ctrl")


    pyautogui.keyDown("ctrl")

    pyautogui.press("c")

    pyautogui.keyUp("ctrl")
def swich():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def pause():
    pyautogui.press("pause")
def printsreen():
    pyautogui.press("PrtSc")

def write_():
    pyautogui.write()
def save():
    pyautogui.keyDown("ctrl")

    pyautogui.press("s")

    pyautogui.keyUp("ctrl")

def volumeincrease(value):
    i=1
    while value >=i:
        pyautogui.press('volumeup')
        i=i+1
    
def volumedecrease(value):
    i=1
    while value >=i:
        pyautogui.press('volumedown')


def previous_Tab():
    # check if chrome is open   
    check = "chrome.exe" in (i.name() for i in psutil.process_iter())
    if True == check:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("t")
        pyautogui.keyUp("ctrl")  
        pyautogui.keyUp("shift")
    else:
        speak("chrome is not open")
  

def mute():
    pyautogui.press("volumemute")

def unmute():
    pyautogui.press("volumemute")

def zoom_(x):
    i=1
    while x >=i:
        pyautogui.keyDown("ctrl")
        pyautogui.press("+")
        pyautogui.keyUp("ctrl")

def decelerate(x):
    i=1
    while x >=i:
        pyautogui.keyDown("ctrl")
        pyautogui.press("-")
        pyautogui.keyUp("ctrl")

