namen_lijst = {}

while True:
    naam = input("Wat is je naam? (Typ 'stop' om te stoppen) ")
    if naam == 'stop':
        break
    
    if naam in namen_lijst:
        if input("Wil je bijwerken? Typ ja of nee: ") != 'ja':
            continue

leeftijd = int(input("Wat is je leeftijd? "))

namen_lijst[naam] = leeftijd
print(namen_lijst)