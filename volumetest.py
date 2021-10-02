from pynput.keyboard import Key,Controller
keyboard = Controller()
import webbrowser
import time
import os
import pyautogui

def open_chrome():
   url2 = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
   browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

   webbrowser.get(browser)
   #You can do webbrowser.open(url, 0) if you want to open in the same window, 1 is a new window, 2 is a new tab. Default behaviour opens them in a new tab anyway.
   #See https://docs.python.org/2/library/webbrowser.html
   webbrowser.open(url2) 

def lock_screen():
    #pyautogui.keyDown('win')
    #pyautogui.keyDown('l')
    time.sleep(1)
    #pyautogui.keyUp('win')
    #pyautogui.keyUp('l')
    os.system('cmd /c "rundll32.exe user32.dll,LockWorkStation"')


def raise_volume():
    for i in range(100):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)



raise_volume()
open_chrome()
time.sleep(1)
lock_screen()
os.system('cmd /c "rundll32.exe user32.dll,LockWorkStation"')





