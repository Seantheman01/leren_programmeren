def vraag_woord(vraag: str):
    
    while True:
        try:
            woord = input(vraag)
            break
        
        except ValueError:
            print("Je moet wel een woord invullen.")
            continue
        
    return woord

typ_woord = vraag_woord("Vul een woord in: ")

print(typ_woord.lower())