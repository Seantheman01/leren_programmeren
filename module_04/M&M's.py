import random

kleuren = ("oranje", "blauw", "groen", "bruin")
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))
inhoud = []


for x in range(aantal):
    random_kleuren = random.randint(0,3)
    inhoud.append(kleuren[random_kleuren])
    
print(f"""Je hebt {inhoud[]} oranje, {inhoud[]} blauwe, {inhoud[]} groene en {inhoud[]} bruine M&M's.""")