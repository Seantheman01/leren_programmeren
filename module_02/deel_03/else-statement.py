a = input('Noem een heel getal op ')
b = input('Noem een heel getal op ')
if a > b:
    Max = a
    print(f'a is het grootste getal {Max}')
elif a < b:
    Min = a
    print(f'a is het kleinste getal {Min}')
else:
    print('a en b zijn even groot')

Min = int(input('Noem een heel getal op '))
Max = int(input('Noem een heel getal op '))
if Min < Max:
    print(f'Het minimum is: {Min}')
    print(f'Het maximum is: {Max}')
else:
    print(f'Het minimum is: {Max}')
    print(f'Het maximum is: {Min}')