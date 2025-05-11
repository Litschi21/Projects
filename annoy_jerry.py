import keyboard
import random
import time

p1 = ['John Pork ', 'Skibidi Toilet ', 'Deine Oma ', 'Deine Mutter ', 'Spongebob ', 'A gay person ', 'Jojo ', 'Big Chungus ', 'Walter White ', 'Skibidi Sigma ', 'Mr. Beast ', 'Your FBI Agent ', 'Amogus Imposter ', 'Bigfoot ', 'The Rizzler ', 'Your browser history ', 'Elon Musk ', 'Ohio ', 'Your stepdad ', 'A Redditor ', 'Your right booty cheek ', 'Your left booty cheek ', 'ChatGPT ', 'My foot ', 'Raderkastl ', 'Filip ', 'A minor ', 'Your cat ', 'Jesus ', 'God ', 'Diddy Hooligan ', 'P. Diddy ', 'Dogecoin ', 'The Universe ', 'A rainbow ', 'Rainbow Six Siege ', 'A fly in your room ', 'Alexa ', 'A tank ', 'Your brain ', 'A Panda ', 'Mein Kaugummi ', 'I ', 'You ', 'Your grandpa ', 'Sonic ', 'A BBC ', 'Michael Jackson ', 'A Fortnite Kid ', 'Mark Zuckerberg ', 'Your microwave ', 'A fish ', 'A shrimp ', 'Absolute Cinema ', 'Xi Jingping ', 'These titties ', 'My ass ', 'Your ass ', 'Every frog ', 'The entire class ', 'Your dad\'s dog ', 'Your grandpa\'s porn collection ', 'Your brother\'s brain ']
p2 = ['is ', 'was ', 'has killed ', 'called ', 'has deleted ', 'has removed ', 'ate ', 'is fingering ', 'hacked ', 'just came inside of ', 'accidentally kissed ', 'has discovered ', 'respawned in ', 'is touching ', 'has entered ', 'rage quit ', 'got banned from ', 'is speedrunning ', 'just teleported behind ', 'had sex with ', 'is playing with ', 'is coming inside of ', 'fucked ', 'has infiltrated ', 'is calculating how to destroy ', 'has raped ', 'has created ', 'invaded ', 'exploded ', 'stole ', 'unlocked ', 'busted all over ', 'is making out with ', 'broke into ', 'crashed ', 'spawned inside ', 'drowned ', 'jumped into ', 'became ', 'punched ', 'shot ', 'has ', 'kidnapped ', 'rebooted ', 'uploaded ', 'unloaded ', 'has charged ', 'has sucked ', 'likes to suck ', 'has eaten ', 'bit ', 'got doxxed by ', 'is trapped inside ', 'was twerking on ', 'is illegally downloading ', 'gave a blowjob to ', 'got a boobjob by ', 'broke '] 
p3 = ['you from behind.', 'dead.', 'your Oma.', 'your Mom.', 'a gay person.', 'a black person.', 'your window.', 'inside of you.', 'the shower.', 'your dad.', 'your search history.', 'your last brain cell.', 'your stepbro.', 'the backrooms.', 'a McDonald\'s Parking Space.', 'your dog\'s OnlyFans.', 'your sleep paralysis demon.', 'your home.', 'your life.', 'Ohio.', 'your browser history.', 'your Windows PC.', 'your Laptop.', 'your school.', 'a minor.', 'fire.', 'your ass cheeks.', 'your hamster.', 'your fridge.', 'your gaming chair.', 'your table.', 'your phone.', 'your room.', 'your privacy.', 'a gun.', 'your passwords.', 'Jojo.', 'your girlfriend.', 'your wife.', 'your husband.', 'Goku.', 'Pepe the Frog.', 'your door.', 'your bed.', 'your balls.', 'me.', 'my cock.', 'my ears.', 'my hair.', 'your sleep schedule.', 'the Geneva Convention.', 'Austria.', 'my pizza.', 'a YouTube Short Comment.']

print(f'P1: {len(p1)}')
print(f'P2: {len(p2)}')
print(f'P3: {len(p3)}')
print(f'Total: {len(p1) * len(p2) * len(p3):,}\n')
# quit()

keyboard.wait('enter')
while not keyboard.is_pressed('q'):
    for i in range(2):
        text = random.choice(p1) + random.choice(p2) + random.choice(p3)
        keyboard.write(text, delay=0.02)
        keyboard.send('shift+enter')
    keyboard.send('enter')

    a = 30
    for x in range(a, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)

        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)
    print('\n')
