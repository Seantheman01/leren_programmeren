if "woord" in "zijn met woorden":
    print("woord zit erin.")

while True:
    richting = input("Welke kant wil je op? a = links b = rechts ") # richting = input("Welke kant wil je op? 1 = link b = rechts ")
    if richting in "ab":                                            # if richting in "12"   dit kan ook
        break
    else:
        print("Je gaat de verkeerde kant op.")


if  "d" in "aapje":
    print("Er zit a in.")
    
if "1" in "123456":
    print("Er zit 1 in.")