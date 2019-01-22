import subprocess
import os
import time
import pyautogui
import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref
import sys
import ctypes

#Define hours you want the program to run below
hour1 = 3
hour2 = 6


def warthunder():
    os.startfile("E:\Program Files (86x)\steamapps\common\War Thunder\launcher.exe")
    time.sleep(200)
    pyautogui.press('enter')
    time.sleep(40)
    pyautogui.press('enter')
    time.sleep(30)
    pyautogui.press('enter')


def killProcess():
    os.system("taskkill /f /im aces.exe")
    time.sleep(1)

def shutdown():
    subprocess.call(["shutdown", "/s"])



class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0
#Call get_idle_duration() to get idle time in seconds

def wait():
    while 1:
        now = datetime.datetime.now()
        hour = now.hour
        if hour > int(hour1) and hour < int(hour2):
            time.sleep(1)
            if get_idle_duration() == 0.0:
                break
            elif get_idle_duration() > 120:
                warthunder()
                killProcess()
                shutdown()
                break
        else:
            while 1:
                if get_idle_duration() > 1200:
                    warthunder()
                    killProcess()
                    shutdown()
            #ask = int(input("You\'ve selected the program to run between the hours "+ str(hour1) + " and " +str(hour2) + ". Unfortunatly, it's hour " + str(now.hour) +" right now. What would you like to do? (Select number and hit enter) \n 1) Run anyways \n 2) Wait 3 hours \n 3) Close \n"))
            #if ask == '1':
            #    close = input("Close War Thunder afterwords? (Y/N)")
            #    if close == 'Y' or 'y' or 'yes' or 'Yes':
            #        shutdownComputer = input("Would you like to turn your computer off afterword?")
            #        if shutdownComputer == 'Y' or 'y' or 'yes' or 'Yes':
            #            warthunder()
            #            killProcess()
            #            shutdown()
            #        elif shutdownComputer == 'N' or 'n' or 'No' or 'no':
            #            warthunder()
            #            killprocess()
            #        else:
            #            print('Answer not recognized')
            #            wait()
            #    if close == 'N' or 'n' or 'No' or 'no':
            #        warthunder()
            #elif ask == '2':
            #    print('waiting...')
            #    time.sleep(7200)
            #    wait()
            #elif ask == '3':
            #    break
            #else:
            #    print('Value not recognized, try again dickwad')
            #    wait()
            #time.sleep(7200)
            #hour()
wait()