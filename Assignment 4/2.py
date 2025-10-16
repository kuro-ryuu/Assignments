inch = int(input("Please enter the length in inch: "))
brute_force_quit_thing = 0
while inch >= 0 and brute_force_quit_thing == 0:
        print(f"{inch} inch is equal to {inch*2.54} centimeter.")
        brute_force_quit_thing += 1
        if inch < 0:
            break


