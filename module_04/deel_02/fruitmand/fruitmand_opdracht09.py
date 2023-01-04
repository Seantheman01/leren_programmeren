from fruitmand import fruitmand

fruitmand.remove({'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True})

for x in fruitmand:
    alle_kleuren = x['color']
    
print(alle_kleuren)