fysiek = input("Is het spel fysiek? ")
if fysiek == 'ja':
    bordspel = input("Is het een borspel? ")
    if bordspel == 'nee':
        oranje = input("Is het spel oranje? ")
        if oranje == 'ja':
            print("Het is het kaartspel.")
        elif oranje == 'nee':
            print("Het is Sushi Go.")
    elif bordspel == 'ja':
        treintjes = input("Heeft het spel treintjes? ")
        if treintjes == 'ja':
            print("Het is Ticket To Ride.")
        elif treintjes == 'nee':
            print("Het is Catan.")
elif fysiek == 'nee':
    sport = input("Is het een sport spel? ")
    if sport == 'ja':
        print("Het is Fifa.")
    elif sports == 'nee':
        print("Het is Age Of Empires IV.")