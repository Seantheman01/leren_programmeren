namen_dict = {}

while True:
    naam = input("Wat is je naam? (Typ 'stop' om te stoppen) ")
    if naam == 'stop':
        break
    
    if naam in namen_dict:
        if input("Wil je bijwerken? Typ ja of nee: ") != 'ja':
            continue

    leeftijd = int(input("Wat is je leeftijd? "))
    
    if leeftijd in namen_dict.values():
        for n, l in namen_dict.item():
            if l == leeftijd:
                break
    print(f"Er zit al iemand in die {leeftijd} jaar oud is.")
    if input("Toch doorgaan? Typ ja of nee: ") != 'ja':
        continue

    namen_dict[naam] = leeftijd
    # namen_lijst.update({naam : leeftijd}) zo kan het ook

print(namen_dict)

leeftijd_lijst = list(namen_dict.values())
namen_lijst = list(namen_dict.keys())
print(leeftijd_lijst)
print(namen_lijst[leeftijd_lijst.index(max(leeftijd_lijst))])