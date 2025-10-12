a = []
while True:
    input_num = (input("Enter a number, leave blank to stop: "))
    if input_num == "":
        break
    try:
        num = float(input_num)
        a.append(num)
    except ValueError:
        print("Please enter a valid number.")
if a:
    print(f"Smallest: {min(a)}")
    print(f"Largest: {max(a)}")

