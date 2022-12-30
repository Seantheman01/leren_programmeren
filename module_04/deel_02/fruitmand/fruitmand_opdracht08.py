from fruitmand import fruitmand

fruitmand.append({'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True})

gewicht = 0
for x in fruitmand:
    totaal_gewicht = gewicht + x['weight']
    
print(totaal_gewicht)