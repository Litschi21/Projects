import cv2
import pyautogui
import time
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image


image_positions = {
    'algeria.png': (1086, 634),
    'angola.png': (1203, 961),
    'benin.png': (1052, 779),
    'botswana.png': (1249, 1046),
    'burkina_faso.png': (1033, 745),
    'burundi.png': (1309, 891),
    'cameroon.png': (1161, 796),
    'cape_verde.png': (830, 711),
    'central_african_republic.png': (1235, 800),
    'chad.png': (1208, 756),
    'comoros.png': (1430, 966),
    'democratic_republic_of_the_congo.png': (1246, 844),
    'djibouti.png': (1427, 752),
    'egypt.png': (1284, 640),
    'equatorial_guinea.png': (1137, 849),
    'eritrea.png': (1380, 723),
    'eswatini.png': (1325, 1117),
    'ethiopia.png': (1368, 797),
    'gabon.png': (1161, 851),
    'ghana.png': (1030, 802),
    'guinea_bissau.png': (897, 749),
    'guinea.png': (951, 774),
    'ivory_coast.png': (997, 807),
    'kenya.png': (1361, 854),
    'lesotho.png': (1293, 1148),
    'liberia.png': (952, 809),
    'libya.png': (1249, 658),
    'madagascar.png': (1451, 1033),
    'malawi.png': (1345, 966),
    'mali.png': (1046, 708),
    'mauritania.png': (969, 707),
    'mauritius.png': (1563, 1042),
    'morocco.png': (966, 567),
    'mozambique.png': (1332, 1006),
    'namibia.png': (1191, 1045),
    'niger.png': (1141, 727),
    'nigeria.png': (1133, 792),
    'republic_of_the_congo.png': (1191, 847),
    'rwanda.png': (1311, 884),
    'sao_tome_and_principe.png': (1104, 849),
    'senegal.png': (913, 737),
    'seychelles.png': (1512, 913),
    'sierra_leone.png': (930, 782),
    'somalia.png': (1429, 831),
    'south_africa.png': (1259, 1118),
    'south_sudan.png': (1291, 801),
    'sudan.png': (1277, 752),
    'tanzania.png': (1325, 906),
    'the_gambia.png': (892, 733),
    'togo.png': (1044, 792),
    'tunisia.png': (1122, 553),
    'uganda.png': (1328, 848),
    'western_sahara.png': (909, 636),
    'zambia.png': (1268, 980),
    'zimbabwe.png': (1304, 1025)
}

threshold = 0.8
match_found = False

for flag, coords in image_positions.items():
    match = pyautogui.locateOnScreen(f'flags/{flag}', confidence=threshold, region=[1604, 452, 96, 63], grayscale=True)

    if match:
        print(f'Found {flag} at {coords}!')
        click(*coords)
        match_found = True
        break

# x-axis: 1604 - 1700 (Diff: 96)
# y-axis: 452 - 515 (Diff: 63)
