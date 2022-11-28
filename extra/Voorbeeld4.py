PRIJS = 7.99

while True:
    try:   
        hoeveel_pizza = int(input("Hoeveel pizza's wil je hebben? "))
        break
    except ValueError:
        print("Je moet wel een getal invullen, zoals bijvoorbeeld: 1, 4 of 7")

bedrag = hoeveel_pizza * PRIJS
print(bedrag)