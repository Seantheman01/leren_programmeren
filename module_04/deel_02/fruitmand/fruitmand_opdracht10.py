from fruitmand import fruitmand

for x in fruitmand:
    print(sorted(fruitmand, key=lambda a: (a['weight'])))