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

    namen_lijst[naam] = leeftijd
    # namen_lijst.update({naam : leeftijd}) zo kan het ook

print(namen_lijst)