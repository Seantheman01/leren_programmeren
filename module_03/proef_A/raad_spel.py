import random


punten = 0
verschil = 0
rondes = 0
kansen = 0

begin = input("Wil je beginnen? ")
for x in range(20):
    if begin == 'ja':
        getal = random.randint(1,1000)
        print(getal)
        for y in range(10):
            getal_typen = int(input("Typ een getal: "))
            verschil = abs(getal_typen - getal)
            
            if getal_typen != getal:
                if getal_typen < getal:
                    print("hoger")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        
                elif getal_typen > getal:
                    print("lager")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        
            if getal_typen == getal:
                print("Geraden!")
                punten += 1
                rondes += 1
                print(f"punten: {punten}")
                break
            
            if kansen == 10:
                rondes += 1
                print("Je hebt het niet kunnen raden.")
                print(f"Het getal was: {verschil}")
                break
            
        verder = input("Nog een ronde? ")
        if verder == 'nee':
            print(f"Totale punten: {punten}")
            quit()
        elif verder != 'ja' and verder != 'nee':
            input("Kies ja of nee: ")
            
    elif begin == 'nee':
        print('O, jammer...')
        break

    else:
        begin = input("Typ ja of nee: ")
        
    if rondes == 20:
        print(f"Totale punten: {punten}")
        quit()