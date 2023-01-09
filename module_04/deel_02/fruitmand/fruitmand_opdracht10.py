from fruitmand import fruitmand

gewichten = []

for x in fruitmand:
    gewichten.append(x['weight'])
   
 
print(sorted(gewichten))