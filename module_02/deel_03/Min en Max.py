a = int(input('Noem een heel getal op? '))
b = int(input('Noem een heel getal op? '))
if a > b:
    Max = a
    print(f'a is het grootste getal {Max}.')
    print(f'Het minimum is: {b}')
    print(f'Het maximum is: {a}')
elif a < b:
    Min = a
    print(f'a is het kleinste getal {Min}.')
    print(f'Het minimum is: {a}')
    print(f'Het maximum is: {b}')
else:
    print('a en b zijn even groot.')