import requests
import json

r = requests.get("https://reqres.in/api/users?page=2")

response = r.json()

for data in response["data"]:
    #print(data["id"])
    print('id: {}'.format(data["id"]))
    print('email: {}'.format(data["email"]))
    print('first_name: {}'.format(data["first_name"]))
    print('last_name: {}'.format(data["last_name"]))

print("-" * 20)

headers = r.headers

for header in headers:
    print('{} -> {}'.format(header, headers[header]))
