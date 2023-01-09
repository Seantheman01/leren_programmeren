lijst1 = ["Sean", "Berat", "Umut", "Noa", "Tobias"]
lijst2 = ["16", "17", "15", "18", "15"]
for naam, leeftijd in zip(lijst1, lijst2):
    print("Hallo", naam, ". Je bent", leeftijd, "jaar oud.")
    
for positie, naam in enumerate(lijst1, lijst2):
    print(positie)
    print("Hallo", naam, ", je bent ", leeftijd[positie], "jaar oud.")