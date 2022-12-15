import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))
inhoud = {}

for x in kleuren:
    inhoud[x] = 0
    
for x in range(aantal):
    inhoud[random.choice(kleuren)] += random.randint(0,3)
    
print(inhoud)