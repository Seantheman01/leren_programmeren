import random


punten = 0
getal = random.randint(1,1000)

print(getal)
begin = input("Wil je beginnen? ")
for x in range(20):
    if begin == 'nee':
        break
    elif begin == 'ja':
        for y in range(10):
            print(getal)
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