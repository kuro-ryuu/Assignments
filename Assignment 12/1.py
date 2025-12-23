import requests
endpoints="https://api.chucknorris.io/jokes/random"
response = requests.get(endpoints)
print(response.json()['value'])