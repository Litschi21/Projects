import keyboard
import random
import time

p1 = ['Deine Oma ', 'Your mom ', 'Spongebob ', 'Jojo ', 'Big Chungus ', 'Walter White ', 'Your FBI Agent ', 'Bigfoot ', 'The Rizzler ', 'Your stepdad ', 'ChatGPT ', 'My foot ', 'Raderkastl ', 'Filip ', 'A minor ', 'Your cat ', 'Jesus ', 'P. Diddy ',  'A fly in your room ', 'Alexa ', 'A Panda ', 'I ', 'You ', 'Your grandpa ', 'Sonic ', 'A BBC ', 'Michael Jackson ', 'A Fortnite Kid ', 'A fish ', 'A shrimp ', 'Xi Jinping ', 'The entire class ', 'Your dad\'s dog ', 'Your grandpa ', 'Your brother ', 'A Youtuber ', 'Fr Lesjak ', 'Your teacher ', 'A robot ', 'A cat ', 'A ninja ', 'Queen Elizabeth ', 'A ghost ', 'The president ', 'A janitor ', 'A skeleton ', 'An astronaut ', 'A baby ', 'ChatGPT ', 'A gamer ', 'A dog ', 'A cyborg ', 'Your clone ', 'A giant hamster ', 'A llama ', 'Fr Giefing ', 'Bowser ', 'Mario ', 'Luigi ', 'A shark ']
p2 = ['killed ', 'deleted ', 'removed ', 'ate ', 'fingered ', 'hacked ', 'just came inside of ', 'accidentally kissed ', 'discovered ', 'respawned in ', 'started touching ', 'entered ', 'rage quit ', 'got banned from ', 'speedran ', 'just teleported behind ', 'had sex with ', 'played with ', 'came inside of ', 'fucked ', 'infiltrated ', 'raped ', 'created ', 'invaded ', 'exploded ', 'stole ', 'unlocked ', 'busted all over ', 'made out with ', 'broke into ', 'crashed ', 'spawned inside ', 'drowned ', 'jumped into ', 'became ', 'punched ', 'shot ', 'kidnapped ', 'rebooted ', 'uploaded ', 'unloaded onto ', 'charged ', 'has sucked ', 'likes to suck ', 'has eaten ', 'bit ', 'got doxxed by ', 'is trapped inside ', 'was twerking on ', 'gave a blowjob to ', 'got a boobjob by ', 'broke ']
p3 = ['you from behind.', 'your Oma.', 'your Mom.', 'a gay person.', 'a black person.', 'your window.', 'inside of you.', 'the shower.', 'your dad.', 'your search history.', 'your last brain cell.', 'your stepbro.', 'the backrooms.', 'a McDonald\'s Parking Lot.', 'your dog\'s OnlyFans.', 'your sleep paralysis demon.', 'your home.', 'your life.', 'your browser history.', 'your Windows PC.', 'your Laptop.', 'your school.', 'a minor.', 'fire.', 'your ass cheeks.', 'your hamster.', 'your fridge.', 'your gaming chair.', 'your table.', 'your phone.', 'your room.', 'your privacy.', 'a gun.', 'your passwords.', 'Jojo.', 'your girlfriend.', 'your wife.', 'your husband.', 'Goku.', 'Pepe the Frog.', 'your door.', 'your bed.', 'your balls.', 'me.', 'my cock.', 'my ears.', 'my hair.', 'your sleep schedule.', 'the Geneva Convention.', 'Austria.', 'my pizza.', 'a YouTube Short Comment.', 'Fr Lesjak.', 'Fr Giefing.']

print(f'P1: {len(p1)}')
print(f'P2: {len(p2)}')
print(f'P3: {len(p3)}')
print(f'Total: {len(p1) * len(p2) * len(p3):,}\n')
# quit()

keyboard.wait('enter')
while not keyboard.is_pressed('q'):
    for i in range(1):
        text = random.choice(p1) + random.choice(p2) + random.choice(p3)
        keyboard.write(text, delay=0.02)
        keyboard.send('shift+enter')
    keyboard.send('enter')

    a = 20
    for x in range(a, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)

        print(f'\r{hours:02}:{minutes:02}:{seconds:02}', end='', flush=True)
        time.sleep(1)

    print(f'\r00:00:00', end='', flush=True)
    print('\n')
