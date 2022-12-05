import random

punten = 0
verschil = 0
rondes = 0
kansen = 0

begin = input("Wil je beginnen? ")
while rondes < 3:
    if begin == 'ja':
        getal = random.randint(1,1000)
        print(getal)
        while kansen < 10:
            getal_typen = int(input("Typ een getal: "))
            rondes += 1
            verschil = abs(getal_typen - getal)
            
            if getal_typen != getal:
                if getal_typen < getal:
                    print("hoger")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        
                    elif getal_typen >= 1000:
                        print("Dat is te hoog!")
                    elif getal_typen <= 1:
                        print("Dat is te laag!")
                        
                elif getal_typen > getal:
                    print("lager")
                    kansen += 1
                    if verschil <= 20:
                        print("Je bent heel warm! ")
                    elif verschil <= 50:
                        print("Je bent warm! ")
                        
                    elif getal_typen >= 1000:
                        print("Dat is te hoog!")
                    elif getal_typen <= 1:
                        print("Dat is te laag!")
                    
            if getal_typen == getal:
                print("Geraden!")
                punten += 1
                print(f"punten: {punten}")
                break
        
        if rondes < 3:
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
        
print(f"""EINDE!
Totale punten: {punten}""")