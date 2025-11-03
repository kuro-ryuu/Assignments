names = set()

while True:
    name = input("Enter a name: ").strip()
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nList of names:")
for n in names:
    print(n)
