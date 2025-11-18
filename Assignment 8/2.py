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
area = str(input("Input area: ")).upper()
query = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country AND country.iso_country = %s ORDER BY airport.name ASC"
cursor.execute(query, (area,))
rows = cursor.fetchall()
for row in rows:
    print(row[0])