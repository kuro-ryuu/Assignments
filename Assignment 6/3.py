def gasoline(gallons):
        return gallons * 3.78541

litres = float(input("Enter amount in gallons: "))
while True:
    if litres < 0:
        break
    else:
        print(f"{litres} gallons is {gasoline(litres)} litres")
        litres = float(input("Enter amount in gallons: "))
