#Import the required Libraries
import string
from tkinter import *
from tkinter import ttk
from turtle import tilt
import geo_location
import threading

win= Tk()

win.geometry("750x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)
   if(string!="9403"):
        def fun():
            geo_location.start()
        d = 40
        start_time = threading.Timer(d,fun)
        start_time.start()
   
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

def multi():
    display_text()
    win.destroy()
ttk.Button(win, text= "Okay",width= 20, command= multi).pack(pady=20)

win.mainloop()