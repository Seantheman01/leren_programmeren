import random

nummers = ['1','2','3','4']
letters = ['a','b','c','d']
appel = []

for x in range(10):
    appel.append(random.choice(nummers) + " " + random.choice(letters))
    
print(appel)