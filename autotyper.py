from functools import reduce
import keyboard
import random
import time

def typing(text, delay):
    keyboard.write(text, delay=random.uniform(delay*0.95, delay*1.05))

msg = ""

# Wait for user to give the go to take the screenshot
keyboard.wait('esc')
time.sleep(0.01)

# Time how long the function takes and start typing
start = time.time()
typing(msg, 0.06)
end = time.time()

# Print the time it took in seconds
print(f'Time taken: {end - start} sec')
# a = list(range(1, 2501))
# b = reduce(lambda x, y: str(x) + ' ' + str(y), a)

# print(b)

# Delays for WPMs:
# 100 WPM: 0.12 sec
# 150 WPM: 0.08 sec
# 200 WPM: 0.06 sec
# 300 WPM: 0.04 sec
# 400 WPM: 0.03 sec
# 500 WPM: 0.024 sec
# 600 WPM: 0.02 sec
# 700 WPM: 0.017 sec
# 800 WPM: 0.015 sec
# 900 WPM: 0.013 sec
# 1000 WPM: 0.012 sec
# 2000 WPM: 0.006 sec
# 5000 WPM: 0.0024 sec
# 10.000 WPM: 0.0012 sec
