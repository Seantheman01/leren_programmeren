CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15
nieuw_bedrag = CONSOLE_PRIJS - MEMBER_KORTING
platform = input('Speel je op pc of console?')
    
prijs = PC_PRIJS # prijs van pc game
if platform == 'pc':
    print(f'Als je speelt op {platform}, kost je game {prijs} euro')

prijs = CONSOLE_PRIJS # prijs van console game
if platform == 'console':
    print(f'Je krijgt {MEMBER_KORTING} euro korting, dus je game kost nu {nieuw_bedrag} euro')