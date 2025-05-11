import keyboard
import pyautogui
import random
import time
import win32api, win32con

south_america_coords = [(1369, 906), (1323, 904), (1353, 873), (1407, 883), (1427, 973), (1450, 833), (1295, 811), (1250, 710), (1296, 671), (1351, 675), (1409, 675), (1429, 671), (1454, 669)]
# us_states_coords = [(884, 653), (883, 693), (920, 702), (995, 694), (1007, 726), (810, 781), (877, 797), (982, 812), (976, 910), (1051, 861), (1049, 941), (1158, 674), (1141, 744), (1157, 816), (1154, 876), (1174, 937), (1168, 997), (883, 1118), (1044, 1176), (1247, 722), (1253, 802), (1273, 874), (1290, 972), (1282, 1027), (1328, 1015), (1353, 934), (1363, 902), (1344, 863), (1325, 762), (1383, 989), (1454, 985), (1472, 856), (1489, 1070), (1384, 835), (1396, 762), (1436, 830), (1487, 1060), (1495, 967), (1516, 921), (1511, 884), (1542, 831), (1564, 831), (1574, 804), (1518, 793), (1542, 742), (1592, 762), (1612, 755), (1596, 745), (1579, 703), (1603, 715), (1618, 684)]

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def clicking():
    (rand_x, rand_y) = random.choice(south_america_coords)
    
    click(rand_x, rand_y)

while True:
    keyboard.wait('esc')
    while not keyboard.is_pressed('q'):
        clicking()
        time.sleep(0.001)

# Coords: 1200 - 1478, 602 - 1021
# South America PR: 1.141 sec
# South America WR: 3.947 sec

# Coords: 861 - 1533, 630 - 1276
# Europe PR: ;- sec
# Europe WR: 20.117 sec

# US States PR: 26.739 sec
# US States WR: 21.725 sec
