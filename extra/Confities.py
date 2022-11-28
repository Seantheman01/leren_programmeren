rekenen = 6 # rekenen altijd voldoende
Engels = 4 # minimaal één voldoende voor Engels of Nederlands
Nederlands = 5

if rekenen > 5 and Engels > 5 and Nederlands > 4:
    print("Je mag naar leerjaar 2.")
elif rekenen > 5 and (Engels > 5 or Nederlands > 4):
    print("Je mag naar leerjaar 2.")
else:
    print("Helaas, je blijft zitten.")