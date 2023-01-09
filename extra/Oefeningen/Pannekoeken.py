# Nodig voor 20 pannekoeken: 500 gram bloem, 3 eieren, 800 ml melk, 1 theelepel zout en 50 gram boter

print("""Nodig voor 20 pannekoeken: 
         500 gram bloem, 
         3 eieren, 
         800 ml melk, 
         1 theelepel zout, 
         50 gram boter""")
aantal_pannekoeken = int(input("Hoeveel pannekoeken?"))
bloem = 500
eieren = 3
melk = 800
zout = 1
boter = 50

multiline_zin = f"""Voor {aantal_pannekoeken} heb je nodig:
{bloem/20*aantal_pannekoeken} gram bloem, {eieren/20*aantal_pannekoeken} eieren, {melk/20*aantal_pannekoeken} ml melk, {zout/20*aantal_pannekoeken} theelepel zout en {boter/20*aantal_pannekoeken} gram boter"""

print(multiline_zin)