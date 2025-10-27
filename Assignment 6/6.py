import math
def le_pizzauh_priceuh(diameter, price):
    diameter_meters = diameter / 100
    radius = diameter_meters / 2
    area = math.pi * (radius ** 2)
    return price / area


d1 = float(input("Enter the diameter of the first pizza in centimeters: "))
price1 = float(input("Enter the price of the first pizza in Euro: "))
d2 = float(input("Enter the diameter of the second pizza in centimeters: "))
price2 = float(input("Enter the price of the second pizza in Euro: "))

price_1 = le_pizzauh_priceuh(d1, price1)
price_2 = le_pizzauh_priceuh(d2, price2)

if price_1 < price_2:
    print("The first pizza provides better value for money.")
elif price_1 > price_2:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide equal value for money.")