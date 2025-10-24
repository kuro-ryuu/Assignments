import random

def roll_dice(sides):
    return random.randint(1, sides)

side = int(input("How many sides would the dice be?: "))

while True:
    roll = roll_dice(side)
    print(roll)
    if roll == side:
        break
