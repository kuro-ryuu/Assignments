import random

def roll_dice():
    return random.randint(1, 6)

while True:
    roll = roll_dice()
    print(roll)
    if roll == 6:
        break
