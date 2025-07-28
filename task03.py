import requests
import json

response = requests.get("https://randomuser.me/api/?results=10&gender=female")
data = response.json()

female_users = data['results']

female_list = []

for user in female_users:
    info = {
        "name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "phone": user['phone'],
        "country": user['location']['country']
    }
    female_list.append(info)

with open("females.json", "w") as f:
    json.dump(female_list, f, indent=2)
