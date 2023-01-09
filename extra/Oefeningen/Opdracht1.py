woord = " "
teller = 0

while woord != 'stop':
    woord = input("Typ iets in. Als je 'stop' intypt, stopt het programma. ")
    teller += 1
    print(teller)
    
print(f"aantal keer enter gedrukt: {teller}")