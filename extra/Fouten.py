gastheer = input("Wie is de gastheer? ")
gasten = int(input("Hoeveel gasten komen er? "))
drank = True
chips = True

aanwezigen = gasten if gastheer == '' else gasten + 1
if gastheer != 'corbijn' or (gastheer == 'sean' or (drank and aanwezigen <=20 and (gasten >= 4 or gastheer))):
    print('Start the Party')
else:
    print('No Party')