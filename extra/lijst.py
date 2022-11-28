getallen = [3,7,4,14,13]

for x in getallen:
    print(x)

# nieuw_getal = int(input("Welk getal moet er toegevoegd worden? "))    
# getallen.append(nieuw_getal)
# print(getallen)

print(len(getallen))

getallen.pop(0)
print(getallen)

getallen.remove(4)
print(getallen)

getallen.insert(0,36)
print(getallen)