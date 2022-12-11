import random

vormen = ('harten', 'klaveren', 'schoppen', 'ruiten')
soorten = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw','heer', 'aas', 'joker', 'joker')
kaarten = []

for x in soorten:
    random_vorm = random.choice(vormen)
    kaarten.append(random_vorm)
    
print(f"""kaart 1:
kaart 2:
kaart 3:
kaart 4:
kaart 5:
kaart 6:
kaart 7:

deck (47 kaarten): {kaarten}""")