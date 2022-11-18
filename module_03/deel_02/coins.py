# name of student: Sean
# number of student: 99073596
# purpose of program: to see how many cents you get back
# function of program: 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay # this tells you how much the change is

if change > 0: #
  coinValue = 500 # starts with 500 cents
    
  while change > 0 and coinValue > 0: # checks if there are coins to give
    nrCoins = change // coinValue # this calculates the amount of coins

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue # this calculates how many cents you get back

# comment on code below:
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # this tells you that if the change is bigger than 0, it will print the underneath
  print('Change not returned: ', str(change) + ' cents')
  
  while change > 0:
    print(f'''Aantal 5 euro:
Aantal 2 euro:
Aantal 1 euro:
Aantal 50 cent:
Aantal 20 cent:
Aantal 10 cent:
Aantal 5 cent:
Aantal 2 cent:
Aantal 1 cent:''')
    
else:
  print('done')