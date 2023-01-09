a = "Jan"
b = "Umut"
c = "Menno"

d = a == "Jan"
print(type(d))

if a == "Berat" or b == "Klaas" and False or False:
    print("Aangenomen")

if (d and b == "umut") or c == "Yassine":
    print("Het feest gaat door!")
else:
    print("Het feest gaat niet door!")

def getBool(letter: str) -> bool:
    print(letter)
    if letter == "a":
        return True
    elif letter == "b":
        return True
    elif letter == "c":
        return False
print(getBool("a"))