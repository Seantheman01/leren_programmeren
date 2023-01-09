import random

name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteSeason = input(f'Wat is jouw favorite seizoen, {name}? A) Lente, B) Zomer, C) Herfst of D) Winter ')
answer = favoriteSeason.lower

if favoriteSeason == 'a':
    print("Ik hou ook van de lente!")
elif favoriteSeason == 'b':
    print("De zomer is voor mij te warm.")
elif favoriteSeason == 'c':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif favoriteSeason ==  'd':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = str(random.randint(0,1))
if True:
    print('Ik vind dat ook een mooie kleur!')
elif not False:
    print('TBH, ik hou niet zo van {}...'.format(favoritecolor))

num1 = random.randint(1,10)
num2 = random.randint(5,15)

try:
    number = int(input(f'En weet jij wat {num1} + {num2} is? '))
except:
    print('Dat is geen nummer!')
if number == num1+num2:
    print('Dat is juist')
else:
    print(f'Nee dat klopt niet, {name}')