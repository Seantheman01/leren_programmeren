zin1 = input("Typ een zin in: ")
zin2 = ""
woord = ""

for c in zin1:
    if c == " ":
       zin2 += woord + " " + woord + " "
       woord = ""
    else:
        woord += c

zin2 += woord + " " + woord + " "
print(zin2)