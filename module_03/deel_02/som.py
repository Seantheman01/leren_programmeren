totaal = 50
getal = 50
str_getal = '50'
erbij = 0
while totaal + 1 <= 1000:
    getal += 1
    str_getal += " + " + str(getal)
    totaal += getal
    erbij += 1
    print(f"{erbij}. {str_getal} = {totaal}")