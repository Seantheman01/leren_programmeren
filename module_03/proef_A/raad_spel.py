import random


getal = random.randint(1,1000)
punten = 0
RONDES = 20

begin = input("Wil je beginnen? ")
for x in range(20):
    if begin == 'nee':
        break
    elif begin == 'ja':
        for y in range(10):
            getal_typen = int(input("Typ een getal: "))
            if getal_typen != getal:
                if getal_typen < getal:
                    print("hoger")
                    if abs(50):
                        print("Je bent warm! ")
                    elif abs(20):
                        print("Je bent heel warm! ")
                elif getal_typen > getal:
                    print("lager")
                    if abs(50):
                        print("Je bent warm! ")
                    elif abs(20):
                        print("Je bent heel warm! ")
                elif getal_typen >= 1000:
                    input("Dat is te hoog! ")
                elif getal_typen <= 1:
                    input("Dat is te laag! ")
            elif getal_typen == getal:
                print("Geraden!")
                punten += 1
                print(f"punten: {punten}")
                verder = input("Nog een ronde? ")
                if verder == 'nee':
                    print(f"punten: {punten}")
                    quit()
                elif verder != 'ja' and verder != 'nee':
                    input("Kies ja of nee: ")
    else:
        input("Typ ja of nee: ")
print(f"{punten}")