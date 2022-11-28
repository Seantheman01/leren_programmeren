from random import randint


naam = input("Wat is je naam? ")
complimenten = int(input("Hoeveel complimenten wil je hebben? "))
vorig_getal = 0

for x in range(complimenten):
    getal = randint(1, 5)
    while getal == vorig_getal:
        getal = randint(1, 5)
       
    vorig_getal = getal
        
    if getal == 1:
        print(f"Jij bent geweldig, {naam}!")
    elif getal == 2:
        print(f"Jij bent gang gang, {naam}!")
    elif getal == 3:
        print(f"Jij bent aardig, {naam}!")
    elif getal == 4:
        print(f"Jij bent een toffe peer, {naam}!")
    else:
        print(f"Jij bent echt een topgozer, {naam}!")