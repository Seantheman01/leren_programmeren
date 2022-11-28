hoogte = int(input("Hoe hoog is uw zwembad? "))
breedte = int(input("Hoe breedt is uw zwembad? "))
diepte = int(input("Hoe diep is uw zwembad?"))
inhoud1 = hoogte * breedte * diepte
print(f"Uitgraven: €{25*inhoud1}")
afvoeren = round(32.20*inhoud1)
print(f"Afvoeren grond: €{afvoeren}")
voorrijkosten = round(60*2.05)
print(f"Voorrijkosten: €{voorrijkosten}")
inhoud2 = (inhoud1 / 10)
kleur = input("Welke kleur wilt u? ")
if inhoud2 < 20:
    geld = 250
    if kleur == 'rood':
        kleur_geld = 25
    else:
        kleur_geld = 100
elif inhoud2 >=20:
    geld = 200
    if kleur == 'rood':
        kleur_geld = 20
    else:
        kleur_geld = 125
print(f"Beton + tegel: €{geld + kleur_geld}")
print(f"Totaal: €{250 + 25*inhoud1 + 32.20*inhoud1 + voorrijkosten + geld + kleur_geld}")