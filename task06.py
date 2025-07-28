import requests
import csv

response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()

users = data['results']

with open("users.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Full Name", "Gender", "Email", "Phone", "Country"])

    for user in users:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        gender = user['gender']
        email = user['email']
        phone = user['phone']
        country = user['location']['country']
        writer.writerow([full_name, gender, email, phone, country])
