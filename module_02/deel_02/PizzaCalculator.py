# Sean van Gooswilligen
# Pizza Calculator

SMALL_PIZZA_GELD = 6.50
MEDIUM_PIZZA_GELD = 7.50
LARE_PIZZA_GELD = 9.00
while True:
    try:
        small_pizza_aantal = int(input('Hoeveel small pizzas wil je? '))
        medium_pizza_aantal = int(input('Hoeveel medium pizzas wil je? '))
        large_pizza_aantal = int(input('Hoeveel large pizzas wil je? '))
        print(f'Aantal small pizzas: {small_pizza_aantal} | Prijs: {small_pizza_aantal * SMALL_PIZZA_GELD} euro')
        print(f'Aantal medium pizzas: {medium_pizza_aantal} | Prijs: {medium_pizza_aantal * MEDIUM_PIZZA_GELD} euro ')
        print(f'Aantal large pizzas: {large_pizza_aantal} | Prijs: {large_pizza_aantal * LARE_PIZZA_GELD} euro')
        print(f'Totaal: {small_pizza_aantal * SMALL_PIZZA_GELD + medium_pizza_aantal * MEDIUM_PIZZA_GELD + large_pizza_aantal * LARE_PIZZA_GELD} euro')
    except ValueError:
        print("Je moet wel een getal invullen.")