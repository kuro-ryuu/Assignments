from db import connect_to_db

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
