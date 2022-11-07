toegang_pp = 745
VIP_VR_45min_geld= 333
aantal_personen = int(input("Met hoeveel personen ben je?"))
VR_geld_pp = VIP_VR_45min_geld * aantal_personen
toegang_geld = toegang_pp * aantal_personen
totaal_betalen = toegang_geld + VR_geld_pp
print(f'Dit geweldige dagje-uit met {aantal_personen} personen in de Speelhal met 45 minuten VR kost je maar {totaal_betalen / 100} euro')