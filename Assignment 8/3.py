import mysql.connector, geopy
from geopy import distance

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="CDKR",
        password="1507",
        database="flight_game",
        port=3306,
        autocommit=True,
    )

connection = connect_to_db()
cursor = connection.cursor()

ident  = str(input("Enter first ICAO code: ")).upper()
ident2 = str(input("Enter second ICAO code: ")).upper()

query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(query, (ident,))
row1 = cursor.fetchone()

cursor.execute(query, (ident2,))
row2 = cursor.fetchone()

if row1 is None or row2 is None:
    print("Airport not found.")
else:
    coord1 = (row1[0], row1[1])
    coord2 = (row2[0], row2[1])
    print(f"The distance between the airports is {geopy.distance.distance(coord1, coord2).km} km.")