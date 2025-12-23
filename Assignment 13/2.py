from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "CDKR",
    "password": "1507",
    "database": "flight_game"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    cursor.execute(query, (icao,))
    airport = cursor.fetchone()

    cursor.close()
    conn.close()

    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify({
        "ICAO": airport["ident"],
        "Name": airport["name"],
        "Location": airport["municipality"]
    })

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
