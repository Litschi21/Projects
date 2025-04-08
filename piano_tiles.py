import keyboard
import pyautogui
import time
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

y = 200
while not keyboard.is_pressed('q'):
    if pyautogui.pixel(1608, y)[0] == 0:
        click(1608, y)
    elif pyautogui.pixel(1381, y)[0] == 0:
        click(1381, y)
    elif pyautogui.pixel(1158, y)[0] == 0:
        click(1158, y)
    elif pyautogui.pixel(946, y)[0] == 0:
        click(946, y)
