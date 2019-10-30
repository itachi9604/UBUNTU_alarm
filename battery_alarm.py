import os
import time
import pyttsx3
from tkinter import *

def opengui(inp_msg):
    root = Tk()
    root.geometry("+{}+{}".format(850, 400))
    root.title("Battery Alert")
    root.minsize(350, 120)
    root.maxsize(350, 120)
    lab = Label(text=inp_msg, pady=400, font="ariel 12 bold")
    lab.pack()
    root.lift()
    button = Button(root, text='Close', width=10, font="ariel 10 bold", command=root.destroy).place(x=100, y=75)
    root.mainloop()



def call_here(inp_string):
    eng = pyttsx3.init()
    eng.setProperty('rate', 100)
    eng.setProperty('voice', 'english+f5')
    eng.say(inp_string)
    eng.runAndWait()



flag_20=1
flag_15=1
flag_10=1
curr_status=""
while True:
    os.chdir("/sys/class/power_supply/BAT0")
    f = open("capacity", 'r')

    k = f.read().strip("\n")
    to_int = int(k)

    status_in = open("status", 'r')
    curr_status=(status_in.read()).strip("\n")

    if curr_status!="Charging" and to_int<=20:
        if flag_20==1:
            call_here("battery low")
            flag_20=0
    elif curr_status!="Charging" and to_int<=15:
        if flag_15==1:
            call_here("battery low")
            opengui("BATTERY LOW")
            flag_15=0
    elif curr_status != "Charging" and to_int <= 10:
        if flag_10==1:
            call_here("battery critically low")
            opengui("BATTERY BOHOT LOW HAI BE")
            flag_10=0
    elif to_int>=21:
        flag_20 = 1
        flag_15 = 1
        flag_10 = 1


    status_in.close()
    f.close()
    time.sleep(3)
