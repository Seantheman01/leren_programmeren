def vraag_woord(vraag: str) -> str:
    
    woord = input(vraag)

    return woord

typ_woord = input("Vul een woord in: ").lower()
print(typ_woord)

# zin  = "Vul een woord in: "
# typ_woord = input(zin) zo kan het ook


def vraag_naam(naam: str) -> str:
    return f"Hallo {naam}!"
    
antwoord = vraag_naam("Sean")
print(antwoord)