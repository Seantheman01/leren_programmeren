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
    

print(f"Je hebt {zak['rood']} rode, {zak['blauw']} blauwe, {zak['groen']} groene, {zak['geel']} gele, en {zak['bruin']} bruine M&M's.")