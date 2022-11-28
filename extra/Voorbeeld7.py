UITGRAVEN_M3 = 25
AFVOEREN_M3 = 32.5
VOORRIJKOSTEN_GROOTTE = 20
VOORRIJKOSTEN_AFTSAND = 50

lengte = float(input("Wat is de lengte? in m) "))
breedte = float(input("Wat is de breedte? (in m) "))
diepte = float(input("Wat is de diepte? (in m) "))
afstand_klant = int(input("Afstand in km: "))

inhoud = round(lengte + breedte + diepte) #inhoud in m3
kosten_uitgraven = inhoud * UITGRAVEN_M3
kosten_afvoeren = inhoud * AFVOEREN_M3
grond_verwerken = kosten_uitgraven + kosten_afvoeren

voorrijkosten = 0
if inhoud < VOORRIJKOSTEN_GROOTTE and afstand_klant < VOORRIJKOSTEN_AFTSAND:
    voorrijkosten += 100 + 1.25 * afstand_klant
elif inhoud < VOORRIJKOSTEN_GROOTTE and afstand_klant >= VOORRIJKOSTEN_AFTSAND:
    voorrijkosten += 100 + 1.15 * afstand_klant
elif inhoud > VOORRIJKOSTEN_GROOTTE and afstand_klant < VOORRIJKOSTEN_AFTSAND:
    voorrijkosten += 100 + 2.15 * afstand_klant
elif inhoud > VOORRIJKOSTEN_GROOTTE and afstand_klant >= VOORRIJKOSTEN_AFTSAND:
    voorrijkosten += 100 + 2.05 * afstand_klant
    
print(inhoud)
print(f"afvoeren + graven: {grond_verwerken:.2f}")