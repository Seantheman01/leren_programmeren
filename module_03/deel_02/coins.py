# name of student: Sean
# number of student: 99073596
# purpose of program: to see how many cents you get back
# function of program: 
# structure of program: 

aantal = ' '
toPay = int(float(input('Amount to pay: '))* 100) # here you have to type how much you have to pay
paid = int(float(input('Paid amount: ')) * 100) # here you have to type how much you have paid
change = paid - toPay # this tells you how much the change is

if change > 0: # if the change is bigger than 0, it will run the codes underneath
  coinValue = 500 # starts with 500 cents
    
  while change > 0 and coinValue > 0: # checks if there are coins to give
    nrCoins = change // coinValue # this calculates the amount of coins

    if nrCoins > 0: # if the change is bigger than 0, it will run te codes underneath
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # this prints the amount of cents you need to return
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # here you have to type how many cents you returned
      (f"Gave {nrCoinsReturned} of {coinValue / 100} euros")# this shows how many coins you returned
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
  print("You did not return enough change.")
  print('Change not returned: ', str(change) + ' cents')
    
  aantal += toPay
  print(f'{aantal}')
    
else:
  print('done')