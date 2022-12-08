LANDEN = 3
for x in range(LANDEN):
    LANDEN = input("Noem een land dat speelt in groep A: ")

score = 0
for y in range(3):
    score += 1
    wed1_score = input(f"Wat is de score van {score}e land in de 2e wedstrijd?")


# print(f"""Wedstrijd {land1} - {land2} eindigde in: {wed1_land1} - {wed1_land2}
# Overzicht groep A
# {land1}:   Doelsaldo:  - {land2};   Puntentotaal:                 
# {land2}:   Doelsaldo:  - {land1};   Puntentotaal:                         
# {land3}:   Doelsaldo:           ;   Puntentotaal: """)