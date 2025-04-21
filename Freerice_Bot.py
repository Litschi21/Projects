import win32api, win32con
from PIL import Image
import pytesseract
import pyautogui
import keyboard
import random
import time


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


pytesseract.pytesseract.tesseract_cmd = r"E:\Desk\Pytesseract\tesseract.exe"
y_coords = [766, 959, 1163, 1370]


def answer_question():
    freerice_screenshot = pyautogui.screenshot(region=[1158, 490, 250, 100])
    freerice_screenshot.save("images/freerice_screenshot.png")

    img = Image.open("images/freerice_screenshot.png")
    output = pytesseract.image_to_string(img)
    expression = output.replace('x', '*').replace('X', '*').replace('/', '').replace('(', '').replace(')', '')
    expression = expression.replace('**', '*')
    try:
        calculation = eval(expression)

        print(expression)
        print(calculation)
    except:
        click(100, 720)
        y_coord = random.choice(y_coords)
        if y_coord == 766:
            click(1269, 766)
        elif y_coord == 959:
            click(1269, 959)
        elif y_coord == 1163:
            click(1269, 1163)
        elif y_coord == 1370:
            click(1269, 1370)

    answer_screenshot1 = pyautogui.screenshot(region=[1200, 732, 250, 100])
    answer_screenshot1.save("images/answer_screenshot1.png")
    answer_screenshot2 = pyautogui.screenshot(region=[1200, 929, 250, 100])
    answer_screenshot2.save("images/answer_screenshot2.png")
    answer_screenshot3 = pyautogui.screenshot(region=[1200, 1136, 250, 100])
    answer_screenshot3.save("images/answer_screenshot3.png")
    answer_screenshot4 = pyautogui.screenshot(region=[1200, 1338, 250, 100])
    answer_screenshot4.save("images/answer_screenshot4.png")

    answer_1 = pytesseract.image_to_string("images/answer_screenshot1.png")
    answer_2 = pytesseract.image_to_string("images/answer_screenshot2.png")
    answer_3 = pytesseract.image_to_string("images/answer_screenshot3.png")
    answer_4 = pytesseract.image_to_string("images/answer_screenshot4.png")

    print(answer_1)
    print(answer_2)
    print(answer_3)
    print(answer_4)

    try:
        if int(answer_1) == int(calculation):
            click(1269, 766)
        elif int(answer_2) == int(calculation):
            click(1269, 959)
        elif int(answer_3) == int(calculation):
            click(1269, 1163)
        elif int(answer_4) == int(calculation):
            click(1269, 1370)
        else:
            y_coord = random.choice(y_coords)
            if y_coord == 766:
                click(1269, 766)
            elif y_coord == 959:
                click(1269, 959)
            elif y_coord == 1163:
                click(1269, 1163)
            elif y_coord == 1370:
                click(1269, 1370)
    except ValueError:
        y_coord = random.choice(y_coords)
        if y_coord == 766:
            click(1269, 766)
        elif y_coord == 959:
            click(1269, 959)
        elif y_coord == 1163:
            click(1269, 1163)
        elif y_coord == 1370:
            click(1269, 1370)
    
    win32api.SetCursorPos((1000, 1000))

while not keyboard.is_pressed("q"):
    answer_question()
    time.sleep(3.5)
