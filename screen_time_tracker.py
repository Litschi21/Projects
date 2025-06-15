from datetime import datetime, timedelta
import json
import keyboard
import time

filename = "E:/Desk/Programming/Python/Projects/txt/screen_times.txt"

i = 0
while not keyboard.is_pressed('ctrl+alt+q'):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f'\r{hours:02}:{minutes:02}:{seconds:02}', end='', flush=True)
    i += 1
    time.sleep(1)

screen_time = { "date": datetime.now().date().isoformat(), "hours": hours, "minutes": minutes, "seconds": seconds }

with open(filename, 'a+') as f:
    json.dump(screen_time, f, indent=4)
    f.write('\n\n')
