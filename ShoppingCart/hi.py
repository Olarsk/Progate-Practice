from food import Food

from drink import Drink

print('-------------------------------------')
print('--------WELCOME TO OUR STORE---------')
print('-------------------------------------')

food1 = Food('Bread', 500, 250)
food2 = Food('Butter', 350, 350)
food3 = Food('Sugar', 200, 400)
food4 = Food('Mayonnaise', 700, 200)
food5 = Food('Jam', 800, 300)

foods = [food1, food2, food3, food4, food5]

drink1 = Drink('Milk Shake', 2000, 50)
drink2 = Drink('Water', 100, 75)
drink3 = Drink('Iced cream', 500, 100)
drink4 = Drink('Fruit juice', 1000, 1000)
drink5 = Drink('Soda', 150, 75)

drinks = [drink1, drink2, drink3, drink4, drink5]

print('FOOD')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1
print('-------------------------------------')

print('DRINKS')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1
print('-------------------------------------')

food_order = int(input('Please enter food item number: '))
selected_food = foods[food_order]
print('Selected food: ' + selected_food.name)

drink_order = int(input('Please enter drink item number: '))
selected_drink = drinks[drink_order]
print('Selected drink: ' + selected_drink.name)

count = int(input('Enter quantity (30% off for 3 or more): '))

result = selected_food.get_total_price(
    count) + selected_drink.get_total_price(count)
print('Your total price is ' + str(result) + ' Naira')

print('-------------------------------------')
print('Thanks for coming')
print('-------------------------------------')
