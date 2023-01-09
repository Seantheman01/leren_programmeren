from fruitmand import fruitmand
import random

fruit = []
aantal = int(input("Hoeveel? "))

for x in fruitmand:
    fruit.append(x['name'])
    
for y in range(aantal):
    print(random.choice(fruit))