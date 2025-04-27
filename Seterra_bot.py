import pyautogui
import time
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


image_positions = {
    'albania.png': (1310, 1058),
    'andorra.png': (1016, 1027),
    'austria.png': (1234, 919),
    'belarus.png': (1426, 776),
    'belgium.png': (1077, 847),
    'bosnia.png': (1276, 996),
    'bulgaria.png': (1273, 982),
    'croatia.png': (1256, 961),
    'cyprus.png': (1508, 1167),
    'czechia.png': (1229, 869),
    'denmark.png': (1148, 712),
    'estonia.png': (1405, 635),
    'finland.png': (1398, 523),
    'france.png': (1088, 896),
    'germany.png': (1163, 853),
    'greece.png': (1344, 1100),
    'hungary.png': (1282, 926),
    'iceland.png': (926, 520),
    'ireland.png': (911, 785),
    'italy.png': (1166, 970),
    'kosovo.png': (1324, 1023),
    'latvia.png': (1403, 689),
    'liechtenstein.png': (1157, 931),
    'lithuania.png': (1374, 733),
    'luxembourg.png': (1100, 869),
    'malta.png': (1220, 1158),
    'moldova.png': (1438, 923),
    'monaco.png': (1116, 1004),
    'montenegro.png': (1298, 1021),
    'netherlands.png': (1090, 801),
    'macedonia.png': (1339, 1050),
    'norway.png': (1143, 600),
    'poland.png': (1314, 814),
    'portugal.png': (882, 1072),
    'romania.png': (1399, 967),
    'russia.png': (1536, 734),
    'san_marino.png': (1195, 995),
    'serbia.png': (1323, 996),
    'slovakia.png': (1293, 893),
    'slovenia.png': (1226, 951),
    'spain.png': (972, 1085),
    'sweden.png': (1233, 538),
    'switzerland.png': (1127, 931),
    'ukraine.png': (1436, 872),
    'uk.png': (985, 799),
    'vatican.png': (1198, 1047),
}

for flag, coords in image_positions.items():
    try:
        match = pyautogui.locateOnScreen(f'E:/Desk/Programming/Python/Projects/images/flags/{flag}', region=[0, 156, 2559, 1119])
    except pyautogui.ImageNotFoundException:
        continue

    if match is None:
        continue
    else:
        click(*coords)

# x-axis: 1604 - 1700 (Diff: 96)
# y-axis: 452 - 515 (Diff: 63)
