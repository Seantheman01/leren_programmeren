def vraag_woord(vraag: str):
    
    while True:
        try:
            woord = input(vraag)
            break
        
        except ValueError:
            print("Je moet wel 'SEAN' invullen.")
            continue
        
    return woord

naam = vraag_woord("Vul 'SEAN' in: ")

print(naam.lower())