import random

vormen = ['harten', 'klaveren', 'schoppen', 'ruiten']
soorten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw','heer', 'aas']
jokers = ['joker1', 'joker2']
kaarten = []
deck = 1

for x in range(len(jokers)):
    kaarten.append(jokers[x])

while len(kaarten) < 47:
    random_getal = random.choice(vormen) + " " + random.choice(soorten)
    if random_getal not in kaarten:
        kaarten.append(random_getal)
        
while deck < 8:
    random_kaart = random.choice(kaarten)
    print(f"kaart {deck}: {random_kaart}")
    kaarten.remove(random_kaart)
    deck += 1
    
print(f"deck (47 kaarten): {kaarten}")