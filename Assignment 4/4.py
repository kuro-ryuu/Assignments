import random
x = random.randint(1,10)
print("Guess the number (1-10)")

while True:
    try:
        answer =int(input("What's your guess?: "))
        if answer < 1 or answer > 10:
            print("Please enter a value within the given range!")
        elif answer > x:
            print("Too high")
        elif answer < x:
            print("Too low")
        else:
            print("Correct")
            print("Try again? (Y/N)")
            replay = input("").strip().upper()
            if replay == "N":
                break
            else:
                x = random.randint(1,10)
                print("Guess the number (1-10): ")
                answer = 0
    except ValueError:
        print("Invalid input")