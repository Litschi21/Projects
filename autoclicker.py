import keyboard
# import pyautogui
import time
import win32api, win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    keyboard.wait('alt+p')
    while not keyboard.is_pressed('q'):
        click()
