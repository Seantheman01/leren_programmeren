from fruitmand import fruitmand
import random

fruit = []
aantal = input("Hoeveel? ")

for x in fruitmand:
    fruit.append(x['name'])
print(f"{random.choice(fruit)} {aantal}")