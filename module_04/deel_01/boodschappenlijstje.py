lijstje = {}

while True:
    boodschappen = input("Welke boodschappen heb je nodig? ")
    if boodschappen == '':
        input("Vul een product in: ")

    hoeveelheid = int(input("Hoeveel heb je daarvan nodig? "))
    if hoeveelheid == '':
        int(input("Vul een getal in: "))
    
    if boodschappen not in lijstje:
        lijstje[boodschappen] = hoeveelheid
        
    else:
        lijstje[boodschappen] += hoeveelheid
    
    verder = input("Heb je meer spullen nodig? ")
    if verder == 'nee':
        break
    elif verder != 'ja' and verder != 'nee':
        input("Vul ja of nee in: ")
 
print("-[ BOODSCHAPPENLIJSTJE ]-")   
for x in lijstje:
    print(f"{lijstje[x]}x {x}")
print("-------------------------")