import json
import requests

url = 'https://randomuser.me/api/'
r = requests.get(url)
data = r.json()

user = {
    'first_name': data['results'][0]['name']['first'],
    'last_name': data['results'][0]['name']['last'],
    'gender': data['results'][0]['gender'],
    'phone': data['results'][0]['phone'],
    'address': {
        'street_name': data['results'][0]['location']['street']['name'],
        'city': data['results'][0]['location']['city'],
        'country': data['results'][0]['location']['country'],
    }
}

with open('user.json', 'w') as jsonfile:
    json.dump(user, jsonfile, indent=4)