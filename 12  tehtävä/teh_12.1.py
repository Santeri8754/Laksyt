import requests
import json
for i in range(100):
    vastaus = requests.get("https://api.chucknorris.io/jokes/random").json()

    print(vastaus["value"])