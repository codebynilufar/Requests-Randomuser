import requests
import json

response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()

users = data['results']

user_list = []

for user in users:
    user_info = {
        "full_name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "gender": user['gender'],
        "country": user['location']['country']
    }
    user_list.append(user_info)

with open('users.json', 'w') as f:
    json.dump(user_list, f, indent=2)
