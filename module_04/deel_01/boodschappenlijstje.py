lijstje = {}

while True:
    boodschappen = input("Welke boodschappen heb je nodig? ")
    if boodschappen == '':
        input("Vul een product in: ")

    hoeveelheid = int(input("Hoeveel heb je daarvan nodig? "))
    if hoeveelheid == '':
        int(input("Vul een getal in: "))
        
    verder = input("Heb je meer spullen nodig? ")
    if verder == 'nee':
        break
    elif verder != 'ja' and verder != 'nee':
        input("Vul ja of nee in: ")
    
for x in boodschappen:
    print("-[ BOODSCHAPPENLIJST ]-")
    print(f"{x}x {lijstje[x]}")        
    print("-----------------------")