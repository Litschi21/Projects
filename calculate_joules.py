mass = 0.1 # kg
speed = 60 # km/h

speed = speed / 3.6
joules = 0.5 * mass * (speed ** 2)

print(f'Joules: {round(joules, 2):,}')
