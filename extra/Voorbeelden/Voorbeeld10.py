antwoord = input("Voer ja of nee in: ")

if antwoord in ("ja", "nee"):
    print("Dat is goed!")

while antwoord not in ("ja", "nee"):
    antwoord = input("Voer ja of nee in: ")

while True:
    antwoord = input("Voer ja of nee in: ")
    if antwoord in ("ja", "nee"):
        break