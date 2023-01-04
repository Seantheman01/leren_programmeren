from fruitmand import fruitmand

for x in fruitmand:
    gewicht = x['weight']
    print(sorted(fruitmand, key=lambda a: (a[gewicht])))