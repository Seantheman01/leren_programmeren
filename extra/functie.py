def vraag_woord(vraag: str) -> int:
    
    while True:
        try:
            woord = input(vraag)
            break
        
        except ValueError:
            print("Je moet wel 'SEAN' invullen.")
            continue
        
    return woord

input("Vul 'SEAN' in: ")

print('SEAN'.lower())