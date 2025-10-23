import random
dice = int(input("How many dices would you like to use?: "))
sum = 0
for x in range(dice):
    roll = random.randint(1,6)
    sum += roll
print(f"The sum of all rolls is {sum}")