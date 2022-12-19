import random

vormen = ['harten', 'klaveren', 'schoppen', 'ruiten']
soorten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw','heer', 'aas']
jokers = ['joker1', 'joker2']
kaarten = []
aantal = 1

for x in range(len(jokers)):
    kaarten.append(jokers[x])

for vorm in vormen:
    for soort in soorten:
        print(vorm + " " + soort)
        

    
# while aantal < 8:
#     random_kaart = random.choice(kaarten)
#     print(f"kaart {aantal}: {random_kaart}")
#     kaarten.remove(random_kaart)
#     aantal += 1
    
# print(f"deck (47 kaarten): {random_getal}")