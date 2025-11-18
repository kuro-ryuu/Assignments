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