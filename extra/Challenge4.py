grootste = 0
kleinste = 0
deelbaar = 0

for x in range(10):
    getal = int(input("Noem een getal (tussen de 0 en 1000): "))
    if getal > grootste:
        grootste = getal
        
    if getal < kleinste:
        kleinste = getal
        
    if getal % 3 == 0:
       aantal_deelbaar = aantal_deelbaar + 1 
        
print(f"Het grootste getal is: {grootste} ")
print(f"Het kleinste getal is: {kleinste} ")
print(f"Het getal dat deelbaar door 3 (zonder rest) is: {aantal_deelbaar} ")