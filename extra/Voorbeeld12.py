namen_lijst = {}

while True:
    naam = input("Wat is je naam? (Typ 'stop' om te stoppen) ")
    if naam == 'stop':
        break
    
    if naam in namen_lijst:
        if input("Wil je bijwerken? Typ ja of nee: ") != 'ja':
            continue

    leeftijd = int(input("Wat is je leeftijd? "))
    
    if leeftijd in namen_lijst.values():
        print(f"Er zit al iemand in die {leeftijd} jaar oud is.")
        
        for n, l in namen_lijst.item():
            if l == leeftijd:
                break
    print(f"{n} is al zo oud!")
    if input("Toch doorgaan? Typ ja of nee: ") != 'ja':
        continue

    namen_lijst[naam] = leeftijd
    # namen_lijst.update({naam : leeftijd}) zo kan het ook

print(namen_lijst)

leeftijd_lijst = list(namen_lijst.values())
print(leeftijd_lijst)