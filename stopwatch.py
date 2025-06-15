import time

for i in range(99999999):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f'\r{hours:02}:{minutes:02}:{seconds:02}', end='', flush=True)
    time.sleep(1)
