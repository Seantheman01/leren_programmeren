naam = input("Wat is uw naam? ")
if naam == 'jan':
    raise NameError("Wij hebben een trauma aan de naam Jan.")
elif naam == 'klaas':
    raise NameError("Wij vinden de naam Klaas een beetje saai.")
elif naam == 'piet':
    raise NameError("Wij vinden de naam Piet een beetje raar.")
elif naam == 'henk':
    raise NameError("Wij vinden de naam Daan iets te typisch.")
elif naam == 'daan':
    raise NameError("Wij worden verdrietig van de naam Daan.")
leeftijd = int(input("Hoe oud bent u?"))
leeftijd_totaal = leeftijd >= 18 and leeftijd <= 40
diploma = input("Bezit u een diploma van HBO-4? ")
rijbewijs = input("Bezit u een geldig vrachtwagen rijbewijs? ")
hoed = input("Bezit u een hoge hoed? ")
lichaam_lengte = int(input("Hoe lang bent u in cm? "))
gewicht = int(input("Hoe zwaar bent u in kg? "))
certificaat = input("Bezit u het certificaat Overleven met gevaarlijk personeel? ")
dieren = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
volledige_lengte = lichaam_lengte >= 150 and lichaam_lengte <= 220
volledige_gewicht = gewicht >= 90 and gewicht <= 120
ervaring = dieren >= 4 or jongleren >= 5 or acrobatiek >= 3
m_of_v = input("Bent u een man of een vrouw? ")
snor_breedte = 0
haar_lengte = 0
if m_of_v == 'man':
    snor = input("Heeft u een snor? ")
    if snor == 'ja':
        snor_breedte = int(input("Hoe breed is uw snor in cm? "))
elif m_of_v == 'vrouw':
    haar = input("Heeft u rood gerkult haar? ")
    if haar == 'ja':
        haar_lengte = int(input("Hoe lang is uw haar in cm? "))

if naam and leeftijd_totaal and diploma == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and (snor_breedte > 10 or haar_lengte > 20) and volledige_lengte and volledige_gewicht and ervaring:
    print("U bent aangenomen! We sturen u zo snel mogelijk een cv.")
else:
    print("Het spijt ons, maar u bent helaas niet aangenomen.")