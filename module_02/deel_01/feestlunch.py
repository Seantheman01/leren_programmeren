aantal_croissantjes = int(input("Hoeveel croissantjes wil je?"))
geld_croissantjes = 39
aantal_stokbroden = int(input("Hoeveel stokbroden wil je?"))
geld_stokbroden = 278
aantal_kortingsbonnen = int(input("Hoeveel kortingsbonnen heb je?"))
korting = 50
totaal_korting = aantal_kortingsbonnen * korting
totaal_geld_croissantjes = aantal_croissantjes + geld_croissantjes
totaal_geld_stokbroden = aantal_stokbroden + geld_stokbroden
feestlunch_geld = totaal_geld_croissantjes + totaal_geld_stokbroden - totaal_korting
print(f'De feestlunch kost je bij de bakker {feestlunch_geld / 100} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!')