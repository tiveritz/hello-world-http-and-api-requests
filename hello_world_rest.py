import json
import requests


r = requests.get("https://reqres.in/api/users/2")

print("-------------------- status code")
print(r.status_code)
print("-------------------- headers")
print(r.headers)
print("-------------------- encoding")
print(r.encoding)
print("-------------------- text")
print(r.text)
print("-------------------- json")
print(r.json())
print("--------------------")