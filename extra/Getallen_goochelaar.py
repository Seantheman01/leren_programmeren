getal1 = int(input("Voer getal 1 in"))
getal2 = int(input("Voer getal 2 in"))
actie = input("Welke actie wilt u, kies: (o)ptellen, (a)ftrekken, (v)ermenigvuldigen, (d)elen: ")

if actie == 'a':
    zin = 'aftrekken:'
    antwoord = getal1 - getal2
elif actie == 'o':
    zin = 'optellen'
    antwoord = getal1 + getal2
elif actie == 'v':
    zin = 'vermenigvuldigen'
    antwoord = getal1 * getal2
elif actie == 'd':
    zin = 'delen'
    antwoord = getal1 / getal2
elif actie == 'k':
    if getal1 > getal2:
        zin = "volgorde(k):" + str(getal1) + ', ' + str(getal2)
    else:
        zin = "volgorde(k):" + str(getal2) + ', ' + str(getal1)
elif actie == 'g':
    if getal1 > getal2:
        zin = "volgorde(g):" + str(getal1) + ', ' + str(getal2)
    else:
        zin = "volgorde(g):" + str(getal2) + ', ' + str(getal1)
else:
    zin = "Tik eens iets nuttigs in"

print(zin)
if actie == 'a' or actie == 'o' or actie == 'v' and actie == 'd':
    print(antwoord)