punten = 0
import random
getal = random.randint(1,1000)
print(getal)
for x in range(10):
    getal_typen = int(input("Typ een getal: "))
    if getal_typen != getal:
        if getal_typen < getal:
            print("hoger")
        elif getal_typen > getal:
            print("lager")
    elif getal_typen == getal:
        print("Dat is het getal!")
        punten += 1
        print(f"punten: {punten}")
        input("Nog een ronde? ")