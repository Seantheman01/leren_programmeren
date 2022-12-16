def vraag_woord(vraag: str) -> int:
    
    while True:
        try:
            woord = input(vraag)
            break
        
        except ValueError:
            print("Je moet wel een woord invullen.")
            continue