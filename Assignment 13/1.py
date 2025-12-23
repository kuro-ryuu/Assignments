from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/prime_number/<number>', methods=['GET'])
def prime_number(number):
    number = int(number)
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    return jsonify({
        "Number" : number,
        "isPrime" : is_prime
    })




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)