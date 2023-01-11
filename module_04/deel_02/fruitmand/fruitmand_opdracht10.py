from fruitmand import fruitmand
from operator import itemgetter

gewichten = sorted(fruitmand, key=itemgetter('name', 'weight'))
    
print(gewichten)