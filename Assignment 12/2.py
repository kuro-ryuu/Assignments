import requests

prompt = input("Which municipaility's weather would you like to check?: ")
endpoints = f"https://api.openweathermap.org/data/2.5/weather?q={prompt}&appid=0806de083514229390216ae725220eac"
response = requests.get(endpoints)


products = response.json()
print(products['weather'][0]['description'])
print((int(products['main']['temp'])-273))

