import os
import time
import pyttsx3
def call_here():
    eng = pyttsx3.init()
    eng.setProperty('rate', 100)
    eng.setProperty('voice', 'english+f5')
    eng.say("battery low")
    eng.runAndWait()

cnt=1
while True:
    os.chdir("/sys/class/power_supply/BAT0")
    f = open("capacity", 'r')

    k = f.read().strip("\n")
    to_int = int(k)
    status_in=open("status",'r')

    
    if to_int>=21:
        cnt=1
    if cnt==1 :

        if to_int <= 15:
            call_here()
            cnt=2
    if cnt==2 and to_int<=10:

        call_here()
        cnt=0

    time.sleep(4)
