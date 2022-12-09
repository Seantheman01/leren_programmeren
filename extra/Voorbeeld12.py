namen_lijst = {}

while True:
    naam = input("Wat is je naam? ")
    
    if naam in namen_lijst:
        if input("Wil je bijwerken? Typ ja of nee: ") != 'ja':
            continue