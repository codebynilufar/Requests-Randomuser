import requests
import json

response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()

users = data['results']
users_with_images = []

for user in users:
    info = {
        "name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "image_url": user['picture']['large']
    }
    users_with_images.append(info)

with open("users_with_images.json", "w") as f:
    json.dump(users_with_images, f, indent=2)
