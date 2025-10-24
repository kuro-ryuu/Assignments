import math
def le_pizzauh_priceuh(diameter, price_per_m_square):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area * price_per_m_square


while True:
    diameter = float(input("Enter the diameter of the first pizza in meters: "))
    price_per_m_square = float(input("Enter the price per square meter: "))