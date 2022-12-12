import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))
inhoud = []

for x in range(aantal):
    random_kleur = random.choice(kleuren)
    inhoud.append(random_kleur)
    
print("Je hebt {} rode, {} blauwe, {} groene, {} gele, en {} bruine M&M's.")