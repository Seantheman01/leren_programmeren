import random


getal = random.randint(1,1000)
print(getal)
punten = 0
verschil = 0
RONDES = 20
POGINGEN = 10

begin = input("Wil je beginnen? ")
for x in range(RONDES):
    if begin == 'nee':
        break
    
    elif begin == 'ja':
        for y in range(POGINGEN):
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
                    if (50):
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
if RONDES == 20:
    print("Klaar")