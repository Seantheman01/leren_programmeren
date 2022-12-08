dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen van de week: ")
for x in dagen:
    print(x)

print("")

print("Werkdagen: ")
for y in range(5):
    print(dagen[y])

print("")

print("Weekenddagen: ")
for z in range(5,7):
    print(dagen[z])
    
print("")    
    
print("Alle dagen omgekeerd: ")
for a in range(6,-1,-1):
    print(dagen[a])

print("")

print("Werkdagen omgekeerd: ")
for b in range(4,-1,-1):
    print(dagen[b])
    
print("")
    
print("Weekenddagen omgekeerd: ")
for c in range(6,4,-1):
    print(dagen[c])