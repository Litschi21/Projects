import random

done = False


def get_rand_num():
    return random.randint(1, 10)


def check_win(rand_num, player_num):
    if rand_num == player_num:
        print('You won!')
        done = True
    elif rand_num > player_num:
        print('Too low.')
        done = False
    elif rand_num < player_num:
        print('Too high.')
        done = False
    else:
        print('Invalid.')
        done = True


rand_num = get_rand_num()

while done != True:
    player_num = int(input('Guess the number between 1 and 10: '))
    check_win(rand_num, player_num)
    if done == True:
        quit()
