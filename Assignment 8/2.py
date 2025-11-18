from db import connect_to_db

connection = connect_to_db()
cursor = connection.cursor()

area = str(input("Input area: ")).upper()
query = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country AND country.iso_country = %s ORDER BY airport.name ASC"
cursor.execute(query, (area,))
rows = cursor.fetchall()

for row in rows:
    print(row[0])