username = "python"
pw = "rules"
attempt = 0
while attempt < 5:
        user = input("Username: ")
        password = input("Password: ")
        if user != username or password != pw:
            print("Wrong password or username")
            attempt += 1
        else:
            print("Welcome")
            break
else:
    print("Access Denied")



