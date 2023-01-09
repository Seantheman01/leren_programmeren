def vraag_getal(vraag: str) -> int:

    while True:
        try:
            getal = int(input(vraag))
            break
        
        except ValueError:
            print("Je moet wel een getal invullen.")
            continue   
        
    return getal

leeftijd = vraag_getal("Voer uw leeftijd in: ")
geboorte_jaar = vraag_getal("Voer uw geboortejaar in: ")
geboorte_maand = vraag_getal("Voer uw geboortemaand in: ")
geboorte_dag = vraag_getal("Voer uw geboortedag in: ")

print(leeftijd)