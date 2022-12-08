land1 = input("Noem het eerste land dat speelt in groep A: ")
land2 = input("Noem het tweede land dat speelt in groep A: ")
land3 = input("Noem het derde land dat speelt in groep A: ")

print(f"""Wedstrijd |'thuis'|'uit'| Doelpunten land 1 | Doelpunten land 2 | Winnaar
1         | {land1}    | {land2}  | 2                 | 0                 | {land1}
2         | {land2}    | {land3}  | 1                 | 2                 | {land3}
3         | {land1}    | {land3}  | 3                 | 1                 | {land1} """)


print(f"""Wedstrijd {land1} - {land2} eindigde in: 2 - 0
Overzicht groep 
Land | Doelsalo (gemaakt - tegen) | Puntentotaal
{land1}   | 2 - {land2}                     | 3
{land2}   | 0 - {land1}                     | -3
{land3}   | 0                          | 0 """)