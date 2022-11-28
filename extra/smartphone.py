prijs_iPhone_13 = int(input('Hoe duur is de iPhone 13? '))
prijs_Samsung_Galaxy_S22 = int(input('Hoe duur is de Samsung Galaxy S22? '))

if prijs_iPhone_13 > prijs_Samsung_Galaxy_S22:
    print(f'De iPhone 13 is het duurst, de telefoon kost: {prijs_iPhone_13} Euro')
else:
    print(f'De iPhone 13 is het goedkoopst, de telefoon kost: {prijs_iPhone_13} Euro')

verschil = prijs_iPhone_13 - prijs_Samsung_Galaxy_S22 + 50
if verschil > 50:
    advies = 'Samsung Galaxy S22'
    aankoop_prijs = prijs_Samsung_Galaxy_S22
    geen_prijs = prijs_iPhone_13
    geen_advies = 'iPhone 13'
else:
    advies = 'iPhone 13'
    aankoop_prijs = prijs_iPhone_13
    geen_prijs = prijs_Samsung_Galaxy_S22
    geen_advies = 'Samsung Galaxy S22'
print(f'Het advies is dus de {advies} te kopen. Deze is namelijk {verschil} euro goedkoper/duurder dan de {geen_advies}')