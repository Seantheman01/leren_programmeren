import random


punten = 0
verschil = 0
ronden = 0
kansen = 0

begin = input("Wil je beginnen? ")
for x in range(20):
    if begin == 'ja':
        getal = random.randint(1,1000)
        for y in range(10):
            print(getal)
            getal_typen = int(input("Typ een getal: "))
            verschil = abs(getal_typen - getal)
            
            if getal_typen != getal:
                if getal_typen < getal:
                    print("hoger")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                        kansen += 1
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        kansen += 1
                        
                elif getal_typen > getal:
                    print("lager")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                        kansen += 1
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        kansen += 1
                
                        if kansen == 10:
                            print("Je hebt het niet kunnen raden. ")
                        
                elif getal_typen >= 1000:
                    input("Dat is te hoog! Typ een ander getal: ")
                    kansen += 1
                elif getal_typen <= 1:
                    input("Dat is te laag! Typ een ander getal: ")
                    kansen += 1

            elif getal_typen == getal:
                print("Geraden!")
                punten += 1
                print(f"punten: {punten}")
                ronden += 1
                
                verder = input("Nog een ronde? ")
                if verder == 'nee':
                    print(f"Totale punten: {punten}")
                    quit()
                elif verder != 'ja' and verder != 'nee':
                    input("Kies ja of nee: ")
                
            else:
                input("Typ een getal in: ")
            
    elif begin == 'nee':
        print('O, jammer...')
        break
        
    else:
        begin = input("Typ ja of nee: ")

    if kansen == 10:
        print("Je hebt het niet kunnen raden. ")
        verder = input("Nog een ronde? ")