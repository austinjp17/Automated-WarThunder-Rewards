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
    os.startfile("E:\Program Files (86x)\steamapps\common\War Thunder\launcher.exe")#Path to launcher.exe here
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
if __name__ == '__main__':
    main()
