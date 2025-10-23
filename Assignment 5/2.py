num =[]
while True:
    n = (input("Enter a number: "))
    if n == '':
        break
    else:
        n = int(n)
        num.append(n)
num.sort(reverse=True)
print(num[:5])
