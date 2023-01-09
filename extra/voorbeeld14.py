def vraag_letter(vraag: str) -> str:
    while True:
        letter = input(vraag)
        
        if len(letter) >1:
            print("Je moet wel een letter invoeren! ")
        else:
            return letter   

print(vraag_letter("Voer een letter in: "))