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

query_lat = "SELECT latitude_deg FROM airport WHERE ident = %s"
query_long = "SELECT longitude_deg FROM airport WHERE ident = %s"

cursor.execute(query_lat, (ident,))
row1_lat = cursor.fetchone()
cursor.execute(query_long, (ident,))
row1_long = cursor.fetchone()

cursor.execute(query_lat, (ident2,))
row2_lat = cursor.fetchone()
cursor.execute(query_long, (ident2,))
row2_long = cursor.fetchone()

if row1_lat is None or row1_long is None or row2_lat is None or row2_long is None:
    print("Airport not found.")
else:
    coord1 = (row1_lat[0], row1_long[0])
    coord2 = (row2_lat[0], row2_long[0])
    print(f"The distance between the airports is {geopy.distance.distance(coord1, coord2).km} km.")