import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))
inhoud = []

for x in range(aantal):
    zak = {
        'rood' : 1,
        'blauw' : 1,
        'groen' : 1,
        'geel' : 1,
        'bruin' : 1
    }
    
print("Je hebt {} rode, {} blauwe, {} groene, {} gele, en {} bruine M&M's.")