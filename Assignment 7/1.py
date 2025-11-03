seasons = ("Spring", "Summer", "Autumn", "Winter")
month = int(input("Enter month number (1-12): "))


if month in (12, 1, 2):
    season = seasons[3]
elif month in (3, 4, 5):
    season = seasons[0]
elif month in (6, 7, 8):
    season = seasons[1]
elif month in (9, 10, 11):
    season = seasons[2]
else:
    season = "Invalid month number"

print(f"The season is {season}.")
