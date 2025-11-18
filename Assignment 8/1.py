import mysql.connector

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
ident = str(input("Enter ICAO code: ")).upper()
query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (ident,))
row = cursor.fetchone()
if row is None:
    print("Airport not found.")
else:
    print("\n"
    f"Name: {row[0]}\n"
    f"Municipality: {row[1]}\n")
