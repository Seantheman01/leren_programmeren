antwoord = input("Is de kaas geel? ")
if antwoord =='ja':
    antwoord = input("Zitten er gaten in? ")
    if antwoord == 'ja':
        antwoord = input("Is de kaas belachelijk duur? ")
        if antwoord == 'ja':
            print("Jouw kaas is Emmethaler.")
        elif antwoord == 'nee':
            print("Jouw kaas is Leerdammer.")
        else:
            print("Kies voor ja of nee.")
    elif antwoord == 'nee':
        antwoord = input("is de kaas hard als steen? ")
        if antwoord == 'ja':
            print("Jouw kaas is Parmigiano Regianno.")
        elif antwoord == 'nee':
            print("Jouw kaas is Goudse Kaas.")
        else:
            print("Kies voor ja of nee.")
    else:
        print("Kies voor ja of nee.")
elif antwoord == 'nee':
    antwoord = input("Heeft de kaas blauwe schimmel? ")
    if antwoord == 'ja':
        antwoord = input("Heeft de kaas een korts? ")
        if antwoord == 'ja':
            print("Jouw kaas is Blue de Rochbaron.")
        elif antwoord == 'nee':
            print("Jouw kaas is Faume d'Ambert.")
        else:
            print("Kies voor ja of nee.")
    elif antwoord == 'nee':
        antwoord = input("Heeft de kaas een korst? ")
        if antwoord == 'ja':
            input("Stinkt de kaas? ")
            if antwoord == 'ja':
                print("Jouw kaas is Brie.")
            elif antwoord == 'nee':
                print("Jouw kaas is Camembert.")
            else:
                print("Kies voor ja of nee.")
        elif antwoord == 'nee':
            print("Jouw kaas is Mozzarella.")
        else:
            print("Kies voor ja of nee.")
    else:
        print("Kies voor ja of nee.")
else:
    print("Kies voor ja of nee.")