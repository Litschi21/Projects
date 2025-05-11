import cv2
import keyboard
import pyautogui
import numpy as np
import time
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

image_positions = {
    'albania.png': (1310, 1159),
    'andorra.png': (1021, 1126),
    'austria.png': (1237, 1027),
    'belarus.png': (1437, 880),
    'belgium.png': (1082, 949),
    'bosnia.png': (1277, 1097),
    'bulgaria.png': (1394, 1128),
    'croatia.png': (1254, 1061),
    'cyprus.png': (1512, 1278),
    'czechia.png': (1230, 969),
    'denmark.png': (1154, 810),
    'estonia.png': (1404, 731),
    'finland.png': (1398, 656),
    'france.png': (1030, 1036),
    'germany.png': (1167, 951),
    'greece.png': (1345, 1185),
    'hungary.png': (1291, 1031),
    'iceland.png': (909, 633),
    'ireland.png': (896, 885),
    'italy.png': (1183, 1118),
    'kosovo.png': (1325, 1126),
    'latvia.png': (1397, 785),
    'liechtenstein.png': (1157, 1031),
    'lithuania.png': (1375, 831),
    'luxembourg.png': (1100, 968),
    'malta.png': (1225, 1259),
    'moldova.png': (1441, 1026),
    'monaco.png': (1118, 1104),
    'montenegro.png': (1294, 1121),
    'netherlands.png': (1090, 908),
    'macedonia.png': (1337, 1144),
    'norway.png': (1167, 701),
    'poland.png': (1287, 919),
    'portugal.png': (880, 1179),
    'romania.png': (1381, 1054),
    'russia.png': (1538, 878),
    'san_marino.png': (1199, 1095),
    'serbia.png': (1319, 1086),
    'slovakia.png': (1288, 999),
    'slovenia.png': (1231, 1052),
    'spain.png': (966, 1159),
    'sweden.png': (1227, 744),
    'switzerland.png': (1132, 1033),
    'ukraine.png': (1499, 972),
    'uk.png': (986, 899),
    'vatican.png': (1199, 1147)
}

templates = {}
for flag in image_positions.keys():
    try:
        path = f'E:/Desk/Programming/Python/Projects/images/flags/{flag}'
        img = cv2.imread(path)
        if img is not None:
            templates[flag] = img
    except Exception as e:
        print(f"Failed to load {flag}")

print("Switch to your target window in 2 seconds...")
time.sleep(2)

region = (1548, 518, 164, 90)

while not keyboard.is_pressed('q'):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    best_match = None
    best_score = 0

    for flag, template in templates.items():
        try:
            h, w = screenshot.shape[:2]
            resized_template = cv2.resize(template, (w, h))
            
            result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)

            if max_val > best_score:
                best_score = max_val
                best_match = flag
        except Exception as e:
            continue

        if best_score > 0.8 and best_match:
            coords = image_positions[best_match]
            click(*coords)
