airports_icao = {
    "NTGA": "Anaa Airport",
    "GUFH": "Faranah Airport"
}

while True:
    new_airport = str(input(
        "1. Add airport\n"
        "2. Fetch info.\n"
        "3. Quit\n"))
    if new_airport == "3":
        print("Program quit.")
        break
    elif new_airport == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports_icao[icao] = name
        print(f"{name} - {icao} added.")
    elif new_airport == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports_icao:
            print(f"{airports_icao[icao]} - {icao}")
        else:
            print("Airport not found.")
    else:
        print("Invalid input.")