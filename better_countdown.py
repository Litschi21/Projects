import keyboard
import time

def time_up_yt():
    keyboard.send('space')
    keyboard.send('ctrl+t')
    time.sleep(0.03)
    keyboard.write('Time\'s up!', delay=0.02)

def time_up():
    keyboard.send('windows')
    time.sleep(0.03)
    keyboard.write('Time\'s up!', delay=0.02)

timer = input('Enter the time in seconds: ')
evaluated_timer = eval(timer)
mode = input('YT mode or otherwise or none? ')

for x in range(evaluated_timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f'\r{hours:02}:{minutes:02}:{seconds:02}', end='', flush=True)
    time.sleep(1)

print(f'\r00:00:00', end='', flush=True)

if mode.lower() == 'yt':
    time_up_yt()
elif 'no' in mode.lower():
    print('Time\'s up!')
else:
    time_up()
