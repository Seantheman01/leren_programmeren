punten = 0
import random
getal = random.randint(1,1000)

begin = input("Wil je beginnen? ")
if begin == 'nee':
    print("O, jammer...")
    print(f"punten: {punten}")
elif begin == 'ja':
    for x in range(10):
        getal_typen = int(input("Typ een getal: "))
        if getal_typen != getal:
            if getal_typen < getal:
                print("hoger")
            elif getal_typen > getal:
                print("lager")
        elif getal_typen == getal:
            print("Geraden!")
            punten += 1
            print(f"punten: {punten}")
            verder = input("Nog een ronde? ")
            if verder == 'nee':
                print(f"punten: {punten}")
                break
            elif verder != 'ja' and verder != 'nee':
                input("Kies ja of nee: ")