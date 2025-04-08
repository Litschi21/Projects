import time

def countdown(hours=0, minutes=0, seconds=0):
    sec = int(hours * 3600 + minutes * 60 + seconds)
    for i in range(0, sec+1):
        time.sleep(1)
        print(f'{round(sec / 3600, 2)} hrs or {round(sec / 60, 2)} min or {sec} sec left')
        sec -= 1

countdown(0, 1, 30)
