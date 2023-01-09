from fruitmand import fruitmand
from operator import itemgetter

gewichten = sorted(fruitmand, key=itemgetter('weight'))

# gewichten = []

# for x in fruitmand:
#     gewichten.append(x['weight'])

# print(sorted(gewichten)