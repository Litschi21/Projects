import keyboard
from PIL import Image
import pyautogui
import pytesseract
import random
import time

def typing(text, delay):
    keyboard.write(text, delay=random.uniform(delay*0.95, delay*1.05))

def screenshot():
    # Take a screenshot and save it
    image = pyautogui.screenshot(region=[828, 510, 882, 89])
    image.save('E:/Desk/Programming/Python/Projects/images/typing_screenshot.png')

def to_string():
    # Open the screenshot and output the text into the msg variable
    img = Image.open('E:/Desk/Programming/Python/Projects/images/typing_screenshot.png')
    output = pytesseract.image_to_string(img)
    
    return output.replace('\n', ' ')

def random_uppercase(string, num_uppercase):
    upper_indices = random.sample(range(len(string)), num_uppercase)
    string_bytes = bytearray(string, encoding='utf-8')
    for i in upper_indices:
        string_bytes[i] = string_bytes[i] - 32
    return string_bytes.decode('utf-8')

# Initialize Pytesseract with the given path
pytesseract.pytesseract.tesseract_cmd = r"E:\Desk\Programming\Pytesseract\tesseract.exe"

while True:
    # Wait for user to give the go to take the screenshot
    keyboard.wait('enter')

    screenshot()
    msg = to_string()

    # msg = random_uppercase(msg, random.randint(2, 6))
    
    # Print msg to be typed for debugging
    print(msg)
    
    # Time how long the function takes and start typing
    start = time.time()
    typing(msg, 0.06)
    end = time.time()
    
    # Print the time it took in seconds
    print(f'Time taken: {round(end - start, 2)} sec\n')

# Delays for WPMs:
# 100 WPM: 0.12 sec
# 150 WPM: 0.08 sec
# 180 WPM: 0.0666666667 sec
# 200 WPM: 0.06 sec
# 300 WPM: 0.04 sec
# 350 WPM: 0.0342857143 sec
# 400 WPM: 0.03 sec
# 500 WPM: 0.024 sec
# 600 WPM: 0.02 sec
# 700 WPM: 0.017 sec
# 800 WPM: 0.015 sec
# 900 WPM: 0.013 sec
# 1000 WPM: 0.012 sec

# Regions for different websites:
# Keybr.com Multiplayer: region=[713, 722, 1261, 179]
# Keybr.com Practice: region=[539, 579, 1536, 379]
# Keybr.com Test: region=[737, 552, 1132, 245]
# Typeracer Solo: region=[828, 510, 882, 89]
