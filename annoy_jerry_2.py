import keyboard
import pyautogui
import random
import threading
import time
import win32api
import win32con

pyautogui.FAILSAFE = False

def mouse_jitter():
    while True:
        time.sleep(random.uniform(5, 10))
        pyautogui.move(random.randint(-10, 10), random.randint(-10, 10))

def capslock():
    while True:
        time.sleep(random.uniform(30, 60))
        keyboard.send('capslock')

def click():
    keyboard.wait('alt+p')
    while not keyboard.is_pressed('alt+q'):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

t0 = threading.Thread(target=mouse_jitter, daemon=True)
t1 = threading.Thread(target=capslock, daemon=True)
t2 = threading.Thread(target=click, daemon=True)

t0.start()
t1.start()
t2.start()

t0.join()
t1.join()
t2.join()
