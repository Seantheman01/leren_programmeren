def vraag_woord(vraag: str) -> str:
    
    while True:
        try:
            woord = input(vraag)
            break
        
        except ValueError:
            print("Je moet wel een woord invullen.")
            continue
        
    return woord

typ_woord = input("Vul een woord in: ").lower()

print(typ_woord)

# zin  = "Vul een woord in: "
# typ_woord = input(zin) zo kan het ook