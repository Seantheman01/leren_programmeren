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
        for n, l in namen_lijst.item():
            if l == leeftijd:
                break
    print(f"Er zit al iemand in die {leeftijd} jaar oud is.")
    if input("Toch doorgaan? Typ ja of nee: ") != 'ja':
        continue

    namen_lijst[naam] = leeftijd
    # namen_lijst.update({naam : leeftijd}) zo kan het ook

print(namen_lijst)

leeftijd_lijst = list(namen_lijst.values())
nieuwe_namen_lijst = list(namen_lijst.keys())
print(leeftijd_lijst)
print(nieuwe_namen_lijst[leeftijd_lijst.index(max(leeftijd_lijst))])