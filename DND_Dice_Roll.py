from random import randint
from time import sleep

def rolling(func):
    def wrapper():
        print('Rolling...')
        sleep(1)
        func()
    return wrapper

@rolling
def roll():
    random_num = randint(1, 20)
    if random_num == 20:
        print(f'NAT 20 BABY!')
    elif random_num == 1:
        print(f'nat 1... sucks')
    else:
        print(f'{random_num}')

roll()
