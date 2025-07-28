import requests
import json

response = requests.get("https://randomuser.me/api/?results=20")
data = response.json()

users = data['results']
young_users = []

for user in users:
    birth_date = user['dob']['date']
    birth_year = int(birth_date[:4])
    if birth_year > 1990:
        info = {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "birth_year": birth_year,
            "email": user['email']
        }
        young_users.append(info)

with open("young_users.json", "w") as f:
    json.dump(young_users, f, indent=2)
