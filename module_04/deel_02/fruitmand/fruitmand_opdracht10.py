from fruitmand import fruitmand
from operator import itemgetter

gewichten = sorted(fruitmand, key=itemgetter('weight'))

for x in fruitmand:
    gewichten.append(x['weight'])

print(gewichten)