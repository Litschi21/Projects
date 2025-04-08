import keyboard
# import threading
import time

def hold_key(key):
    keyboard.press(key)
    keyboard.wait('alt+q')
    keyboard.release(key)
    keyboard.press('s')
    time.sleep(4)
    keyboard.release('s')

# def hold_key2(key):
    # keyboard.press(key)
    # keyboard.wait('q')
    # keyboard.release(key)

# t1 = threading.Thread(target=hold_key, args=args.key)
# t2 = threading.Thread(target=hold_key2, args=args.key)

while not keyboard.is_pressed('alt+z'):
    keyboard.wait('alt+p')
    hold_key('w')
    # t1.start()
    # t2.start()
